"""
LoRA fine-tuning on the grounded-answer dataset (RTX 4070, 8 GB).

    training/.venv/bin/python training/finetune.py --name qwen35-08b-v1
    training/.venv/bin/python training/finetune.py --name smoke --max-train 50 --epochs 1

Data: data/train.jsonl and data/val.jsonl from datagen/build_dataset.py.
Each record has "messages" = [system, user, assistant] built with the
v1 (0-shot) prompt, so the trained model needs no examples in its prompt.

The prompt is rendered with the model's own chat template (thinking off),
and the loss is computed on the assistant answer only.

Outputs, in training/runs/<name>/:
    adapter/      LoRA adapter
    merged/       base + adapter merged, ready for GGUF export (training/export.py)
    train_log.json, config.json
"""

import argparse
import json
import math
import time
from pathlib import Path

import torch
from peft import LoraConfig, get_peft_model
from transformers import (
    AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments,
)

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "training" / "runs"


def render(tokenizer, messages, add_generation_prompt):
    kwargs = dict(tokenize=False, add_generation_prompt=add_generation_prompt)
    try:
        return tokenizer.apply_chat_template(messages, enable_thinking=False, **kwargs)
    except TypeError:  # templates without the thinking switch
        return tokenizer.apply_chat_template(messages, **kwargs)


def encode(tokenizer, record, max_len):
    """
    input_ids for prompt + answer, with labels masked (-100) on the prompt.
    """

    messages = record["messages"]
    prompt = render(tokenizer, messages[:-1], add_generation_prompt=True)
    full = render(tokenizer, messages, add_generation_prompt=False)

    if not full.startswith(prompt):
        # Some templates rewrite earlier turns; fall back to prompt + answer.
        full = prompt + messages[-1]["content"] + (tokenizer.eos_token or "")

    prompt_ids = tokenizer(prompt, add_special_tokens=False)["input_ids"]
    full_ids = tokenizer(full, add_special_tokens=False)["input_ids"]

    if len(full_ids) > max_len:
        return None

    labels = [-100] * len(prompt_ids) + full_ids[len(prompt_ids):]
    return {"input_ids": full_ids, "labels": labels}


def load(path, tokenizer, max_len, limit=None):
    records = [json.loads(line) for line in open(path, encoding="utf-8")]
    if limit:
        records = records[:limit]
    encoded = [encode(tokenizer, r, max_len) for r in records]
    kept = [e for e in encoded if e is not None]
    print(f"{path.name}: {len(kept)}/{len(records)} examples "
          f"(dropped {len(records) - len(kept)} over {max_len} tokens)")
    return kept


class Collator:
    def __init__(self, pad_id):
        self.pad_id = pad_id

    def __call__(self, batch):
        width = max(len(b["input_ids"]) for b in batch)
        ids, labels, mask = [], [], []
        for b in batch:
            pad = width - len(b["input_ids"])
            ids.append(b["input_ids"] + [self.pad_id] * pad)
            labels.append(b["labels"] + [-100] * pad)
            mask.append([1] * len(b["input_ids"]) + [0] * pad)
        return {
            "input_ids": torch.tensor(ids),
            "labels": torch.tensor(labels),
            "attention_mask": torch.tensor(mask),
        }


class AnswerOnlyTrainer(Trainer):
    """
    Computes logits only for the answer span. With a 248k-token vocabulary,
    full-sequence logits for ~1,400-token prompts don't fit in 8 GB, and the
    prompt positions carry no loss anyway. Batches have no padding
    (batch size 1), so the answer is always the tail of the sequence.
    """

    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
        labels = inputs["labels"]
        answer_len = int((labels != -100).sum(dim=1).max())
        keep = answer_len + 1
        outputs = model(input_ids=inputs["input_ids"],
                        attention_mask=inputs["attention_mask"],
                        logits_to_keep=keep)
        logits = outputs.logits[:, :-1, :].float()
        targets = labels[:, -keep:][:, 1:]
        loss = torch.nn.functional.cross_entropy(
            logits.reshape(-1, logits.size(-1)), targets.reshape(-1),
            ignore_index=-100,
        )
        return (loss, outputs) if return_outputs else loss


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--model", default="Qwen/Qwen3.5-0.8B")
    parser.add_argument("--train", type=Path, default=ROOT / "data" / "train.jsonl")
    parser.add_argument("--val", type=Path, default=ROOT / "data" / "val.jsonl")
    parser.add_argument("--epochs", type=float, default=3)
    parser.add_argument("--lr", type=float, default=2e-4)
    parser.add_argument("--lora-r", type=int, default=16)
    parser.add_argument("--lora-alpha", type=int, default=32)
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--grad-accum", type=int, default=16)
    parser.add_argument("--max-len", type=int, default=2048)
    parser.add_argument("--max-train", type=int, help="use only the first N examples")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--grad-checkpointing", action="store_true",
                        help="save VRAM at the cost of speed (not needed for 0.8B)")
    args = parser.parse_args()

    out_dir = RUNS / args.name
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "config.json").write_text(json.dumps(
        {k: str(v) for k, v in vars(args).items()}, indent=2))

    torch.manual_seed(args.seed)
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    train = load(args.train, tokenizer, args.max_len, args.max_train)
    val = load(args.val, tokenizer, args.max_len)

    model = AutoModelForCausalLM.from_pretrained(
        args.model, dtype=torch.bfloat16, device_map={"": 0},
    )
    if args.grad_checkpointing:
        model.gradient_checkpointing_enable()
        model.enable_input_require_grads()

    lora = LoraConfig(
        r=args.lora_r, lora_alpha=args.lora_alpha, lora_dropout=0.05,
        target_modules="all-linear", task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora)
    model.print_trainable_parameters()

    steps_per_epoch = math.ceil(len(train) / (args.batch_size * args.grad_accum))
    training_args = TrainingArguments(
        output_dir=str(out_dir / "checkpoints"),
        num_train_epochs=args.epochs,
        learning_rate=args.lr,
        lr_scheduler_type="cosine",
        warmup_steps=max(1, int(0.05 * steps_per_epoch * args.epochs)),
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=1,
        gradient_accumulation_steps=args.grad_accum,
        bf16=True,
        logging_steps=max(1, steps_per_epoch // 10),
        eval_strategy="steps",
        eval_steps=max(1, steps_per_epoch // 2),
        save_strategy="no",
        report_to=[],
        seed=args.seed,
        remove_unused_columns=False,
    )

    trainer = AnswerOnlyTrainer(
        model=model, args=training_args,
        train_dataset=train, eval_dataset=val,
        data_collator=Collator(tokenizer.pad_token_id),
    )

    start = time.time()
    trainer.train()
    minutes = (time.time() - start) / 60
    final_eval = trainer.evaluate()

    log = {
        "minutes": minutes,
        "train_examples": len(train),
        "val_examples": len(val),
        "peak_vram_gb": torch.cuda.max_memory_allocated() / 1e9,
        "final_eval": final_eval,
        "history": trainer.state.log_history,
    }
    (out_dir / "train_log.json").write_text(json.dumps(log, indent=2))
    print(f"Trained in {minutes:.1f} min, peak VRAM {log['peak_vram_gb']:.1f} GB, "
          f"val loss {final_eval.get('eval_loss'):.4f}")

    model.save_pretrained(out_dir / "adapter")
    merged = model.merge_and_unload()
    merged.save_pretrained(out_dir / "merged", safe_serialization=True)
    tokenizer.save_pretrained(out_dir / "merged")
    print(f"Saved adapter and merged model to {out_dir.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
