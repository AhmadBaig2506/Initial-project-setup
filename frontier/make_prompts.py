"""
Write paste-ready prompts for frontier chat models, plus empty answer
files to fill in.

    python frontier/make_prompts.py                                  # mini set -> frontier/
    python frontier/make_prompts.py --testset eval/data/baseline_test.jsonl \
        --dir frontier/baseline --models claude-opus-5_5

Creates inside --dir:
    prompts/<id>.md                 one question per chat (most faithful)
    batches/batch_NN.md             several questions per chat (faster)
    responses/<model>/<id>.txt      paste a single-question reply here, or
    responses/<model>/batch_NN.txt  paste a whole batch reply here

Existing answer files are never overwritten.
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from prompts import SYSTEM_PROMPT, build_messages  # noqa: E402

DEFAULT_DIR = ROOT / "frontier"
DEFAULT_TESTSET = ROOT / "eval" / "data" / "mini_test.jsonl"
DEFAULT_MODELS = ["chatgpt", "gemini", "claude"]
BATCH_SIZE = 9


def paste_text(messages):
    """
    One plain-text message: the same instructions and sources the local
    models get, without any model-specific chat template.
    """

    system, user = messages[0]["content"], messages[1]["content"]
    return f"{system}\n\n{user}\n"


def batch_text(items):
    """
    Several items in one message, each answered independently.
    """

    parts = [
        "You will answer several independent questions. Each question has "
        "its own numbered sources; use ONLY that item's sources for its "
        "answer and treat every item as if it were the only one.\n\n"
        f"Rules for every item:\n{SYSTEM_PROMPT}\n\n"
        "Output format: for each item, a header line `=== <id> ===` "
        "followed by the answer only. No other text.\n"
    ]

    for item in items:
        user = build_messages(item["question"], item["passages"])[1]["content"]
        parts.append(f"\n########## ITEM {item['id']} ##########\n\n{user}\n")

    ids = ", ".join(item["id"] for item in items)
    parts.append(f"\nAnswer all {len(items)} items in this order: {ids}.\n")
    return "".join(parts)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--testset", type=Path, default=DEFAULT_TESTSET)
    parser.add_argument("--dir", type=Path, default=DEFAULT_DIR)
    parser.add_argument("--models", nargs="*", default=DEFAULT_MODELS)
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE)
    args = parser.parse_args()

    items = [json.loads(line) for line in open(args.testset, encoding="utf-8")]
    items.sort(key=lambda item: item["id"])

    args.dir = args.dir.resolve()
    prompts_dir = args.dir / "prompts"
    batches_dir = args.dir / "batches"
    responses_dir = args.dir / "responses"
    prompts_dir.mkdir(parents=True, exist_ok=True)
    batches_dir.mkdir(parents=True, exist_ok=True)

    for item in items:
        messages = build_messages(item["question"], item["passages"])
        (prompts_dir / f"{item['id']}.md").write_text(
            paste_text(messages), encoding="utf-8"
        )

    batches = [
        items[start:start + args.batch_size]
        for start in range(0, len(items), args.batch_size)
    ]
    for number, batch in enumerate(batches, start=1):
        (batches_dir / f"batch_{number:02d}.md").write_text(
            batch_text(batch), encoding="utf-8"
        )

    for model in args.models:
        model_dir = responses_dir / model
        model_dir.mkdir(parents=True, exist_ok=True)
        names = [f"{item['id']}.txt" for item in items]
        names += [f"batch_{n:02d}.txt" for n in range(1, len(batches) + 1)]
        for name in names:
            path = model_dir / name
            if not path.exists():
                path.write_text("", encoding="utf-8")

    print(f"{len(items)} prompts -> {prompts_dir.relative_to(ROOT)}/")
    print(f"{len(batches)} batches -> {batches_dir.relative_to(ROOT)}/")
    print(f"Answer files -> {responses_dir.relative_to(ROOT)}/"
          f"{{{','.join(args.models)}}}/")


if __name__ == "__main__":
    main()
