"""
Evaluate GGUF models on the frozen test set with llama.cpp's llama-server.

    python eval/run_eval.py                       # all downloaded models
    python eval/run_eval.py --models qwen3.5-2b   # selected models
    python eval/run_eval.py --run finetuned-v1    # results/finetuned-v1/

Writes, per model, results/<run>/<model>/:
    answers.jsonl   every answer with its per-item scores
    metrics.json    aggregated metrics + speed + peak RAM
    server.log      llama-server output
and results/<run>/summary.md + summary.csv comparing all models.
"""

import argparse
import csv
import json
import os
import subprocess
import sys
import threading
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from prompts import VARIANTS, build_messages, normalize_refusal  # noqa: E402
from eval.metrics import aggregate, score_answer, strip_thinking  # noqa: E402
from eval.review import write_reviews  # noqa: E402

MODELS_DIR = ROOT / "models"
RESULTS_DIR = ROOT / "results"
DEFAULT_TESTSET = ROOT / "eval" / "data" / "baseline_test.jsonl"
PORT = 8090


def find_server(gpu=False):
    folder = ROOT / "tools" / ("llama.cpp-cuda" if gpu else "llama.cpp")
    server = next(folder.rglob("llama-server"), None) if folder.exists() else None
    if server is None:
        raise SystemExit(f"llama-server not found in {folder}. "
                         "Run scripts/download_models.py"
                         + (" --cuda" if gpu else ""))
    return server


def gpu_memory_used_mb():
    """
    Total GPU memory in use (MB). Per-process figures aren't available
    under WSL, so VRAM is measured as the increase over the idle level.
    """

    try:
        output = subprocess.run(
            ["nvidia-smi", "--query-gpu=memory.used",
             "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=10,
        ).stdout
        return float(output.strip().splitlines()[0])
    except (OSError, ValueError, IndexError, subprocess.SubprocessError):
        return None


class VramMonitor:
    """
    Polls nvidia-smi in the background and keeps the peak.
    """

    def __init__(self, interval=0.5):
        self.idle = gpu_memory_used_mb()
        self.peak = self.idle
        self.interval = interval
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._run, daemon=True)

    def _run(self):
        while not self._stop.is_set():
            used = gpu_memory_used_mb()
            if used is not None and (self.peak is None or used > self.peak):
                self.peak = used
            self._stop.wait(self.interval)

    def start(self):
        self._thread.start()
        return self

    def stop(self):
        self._stop.set()
        self._thread.join(timeout=5)
        if self.idle is None or self.peak is None:
            return None
        return self.peak - self.idle


def peak_rss_mb(pid):
    """
    Peak resident memory of a process (VmHWM), in MB.
    """

    try:
        for line in Path(f"/proc/{pid}/status").read_text().splitlines():
            if line.startswith("VmHWM:"):
                return int(line.split()[1]) / 1024
    except FileNotFoundError:
        pass
    return None


def start_server(server, model_path, log_file, args):
    command = [
        str(server),
        "-m", str(model_path),
        "--port", str(PORT),
        "-c", str(args.ctx),
        "-t", str(args.threads),
        "-np", "1",
        # No host-RAM prompt cache (default 8 GiB): it inflates peak RAM
        # and isn't used in a single-user on-device deployment.
        "--cache-ram", "0",
        "--jinja",
        "--no-webui",
    ]

    env = os.environ.copy()
    if args.gpu:
        # Offload every layer; the CUDA runtime libs ship next to the binary.
        command += ["-ngl", "999"]
        lib_dirs = {str(p.parent) for p in server.parents[1].rglob("libcudart.so*")}
        lib_dirs.add(str(server.parent))
        env["LD_LIBRARY_PATH"] = ":".join(
            sorted(lib_dirs) + [env.get("LD_LIBRARY_PATH", "")]
        )

    process = subprocess.Popen(
        command, stdout=log_file, stderr=subprocess.STDOUT, env=env
    )

    deadline = time.time() + 300
    while time.time() < deadline:
        if process.poll() is not None:
            raise RuntimeError("llama-server exited; see server.log")
        try:
            if requests.get(f"http://127.0.0.1:{PORT}/health", timeout=2).ok:
                return process
        except requests.RequestException:
            pass
        time.sleep(1)

    process.kill()
    raise RuntimeError("llama-server did not become ready in time")


def render_prompt(messages):
    """
    The exact text the model receives after its chat template is applied.
    """

    response = requests.post(
        f"http://127.0.0.1:{PORT}/apply-template",
        json={
            "messages": messages,
            "chat_template_kwargs": {"enable_thinking": False},
        },
        timeout=60,
    )
    response.raise_for_status()
    return response.json()["prompt"]


def ask(messages, max_tokens):
    start = time.perf_counter()

    response = requests.post(
        f"http://127.0.0.1:{PORT}/v1/chat/completions",
        json={
            "messages": messages,
            "temperature": 0,
            "seed": 0,
            "max_tokens": max_tokens,
            # Qwen3.5 / Qwen3 thinking off; ignored by other templates.
            "chat_template_kwargs": {"enable_thinking": False},
        },
        timeout=600,
    )
    response.raise_for_status()
    data = response.json()

    timings = data.get("timings", {})

    return {
        "answer": data["choices"][0]["message"].get("content") or "",
        "latency_s": time.perf_counter() - start,
        "prompt_tokens": timings.get("prompt_n"),
        "gen_tokens": timings.get("predicted_n"),
        "prompt_tok_per_s": timings.get("prompt_per_second"),
        "gen_tok_per_s": timings.get("predicted_per_second"),
        "finish_reason": data["choices"][0].get("finish_reason"),
    }


def evaluate_model(name, entry, items, server, run_dir, args):
    model_path = MODELS_DIR / name / entry["file"]
    if not model_path.exists():
        print(f"Skipping {name}: {model_path.relative_to(ROOT)} not downloaded")
        return None

    out_dir = run_dir / name
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n=== {name} ===")

    with open(out_dir / "server.log", "w") as log_file:
        vram = VramMonitor().start() if args.gpu else None
        process = start_server(server, model_path, log_file, args)
        rows = []

        try:
            for number, item in enumerate(items, start=1):
                row = {"id": item["id"], "question": item["question"],
                       "answerable": item["answerable"]}

                messages = build_messages(item["question"], item["passages"],
                                          variant=args.prompt)
                row["messages"] = messages

                try:
                    row["rendered_prompt"] = render_prompt(messages)
                    row.update(ask(messages, args.max_tokens))
                    row["raw_answer"] = strip_thinking(row["answer"])[0]
                    row["answer"] = (normalize_refusal(row["raw_answer"])
                                     if args.normalize_refusal
                                     else row["raw_answer"])
                    row.update(score_answer(
                        row["answer"], item["passages"], item["answerable"],
                        question=item["question"],
                    ))
                except Exception as error:  # keep going on one bad item
                    row.update({"error": str(error), "refused": False,
                                "behaviour_correct": False, "latency_s": None,
                                "prompt_tok_per_s": None, "gen_tok_per_s": None,
                                "citations": [], "citation_valid": False,
                                "citation_coverage": None, "groundedness": None,
                                "words": 0, "had_thinking": False,
                                "exact_refusal": False})

                status = "OK " if row["behaviour_correct"] else "BAD"
                print(f"  [{number:2d}/{len(items)}] {status} {item['id']} "
                      f"{row.get('latency_s') or 0:5.1f}s")
                rows.append(row)

            peak = peak_rss_mb(process.pid)
        finally:
            process.terminate()
            process.wait(timeout=30)
            peak_vram = vram.stop() if vram else None

    with open(out_dir / "answers.jsonl", "w", encoding="utf-8") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")

    # Human-readable: full prompt and answer for every item.
    with open(out_dir / "prompts.md", "w", encoding="utf-8") as file:
        file.write(f"# {name}: prompts and answers\n\n"
                   "Rendered prompt = the exact text the model received, "
                   "after its own chat template was applied.\n")
        for row in rows:
            file.write(
                f"\n---\n\n## {row['id']}: {row['question']}\n\n"
                f"Answerable: {row['answerable']}\n\n"
                f"### Rendered prompt\n\n````text\n"
                f"{row.get('rendered_prompt', '(not available)')}\n````\n\n"
                f"### Answer\n\n````text\n{row.get('answer', '')}\n````\n"
            )

    metrics = {
        "model": name,
        "file": entry["file"],
        "params": entry.get("params"),
        "file_size_gb": model_path.stat().st_size / 1e9,
        "peak_ram_mb": peak,
        "peak_vram_mb": peak_vram,
        "device": "gpu" if args.gpu else "cpu",
        "threads": args.threads,
        "ctx": args.ctx,
        "prompt_variant": args.prompt + ("+norm" if args.normalize_refusal else ""),
        "normalize_refusal": args.normalize_refusal,
        **aggregate(rows),
    }

    (out_dir / "metrics.json").write_text(json.dumps(metrics, indent=2))
    return metrics


COLUMNS = [
    ("model", "Model", "{}"),
    ("params", "Params", "{}"),
    ("prompt_variant", "Prompt", "{}"),
    ("file_size_gb", "File GB", "{:.2f}"),
    ("device", "Device", "{}"),
    ("peak_ram_mb", "Peak RAM MB", "{:.0f}"),
    ("peak_vram_mb", "Peak VRAM MB", "{:.0f}"),
    ("behaviour_accuracy", "Behaviour acc", "{:.0%}"),
    ("answer_rate", "Answers (answerable)", "{:.0%}"),
    ("refusal_rate_unanswerable", "Refuses (unanswerable)", "{:.0%}"),
    ("exact_refusal_unanswerable", "Exact refusal text", "{:.0%}"),
    ("answers_with_citations", "Has citations", "{:.0%}"),
    ("citation_validity", "Citations valid", "{:.0%}"),
    ("citation_coverage", "Sentence coverage", "{:.0%}"),
    ("groundedness", "Groundedness", "{:.0%}"),
    ("off_topic_answers", "Off-topic", "{}"),
    ("mean_words", "Words", "{:.0f}"),
    ("prompt_tok_per_s", "Prompt tok/s", "{:.0f}"),
    ("gen_tok_per_s", "Gen tok/s", "{:.1f}"),
    ("mean_latency_s", "Latency s", "{:.1f}"),
]


def fmt(value, pattern):
    return "-" if value is None else pattern.format(value)


def write_summary(run_dir, all_metrics, testset):
    with open(run_dir / "summary.csv", "w", newline="") as file:
        fieldnames = list(dict.fromkeys(k for m in all_metrics for k in m))
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_metrics)

    local = next((m for m in all_metrics if "threads" in m),
                 {"threads": "-", "ctx": "-"})
    header = "| " + " | ".join(title for _, title, _ in COLUMNS) + " |"
    divider = "|" + "---|" * len(COLUMNS)
    lines = [
        f"# Results: {run_dir.name}",
        "",
        f"Test set: `{testset.relative_to(ROOT)}` "
        f"({all_metrics[0]['items']} items). Local models: llama.cpp "
        f"{local.get('device', 'cpu').upper()}, "
        f"{local['threads']} threads, context {local['ctx']}, temperature 0. "
        "Frontier models: answers pasted from a chat interface "
        "(no speed or RAM figures).",
        "",
        header,
        divider,
    ]

    for metrics in all_metrics:
        lines.append("| " + " | ".join(
            fmt(metrics.get(key), pattern) for key, _, pattern in COLUMNS
        ) + " |")

    lines += [
        "",
        "- **Behaviour acc**: answered answerable questions and refused "
        "unanswerable ones.",
        "- **Citations valid**: no citation points to a source number that "
        "doesn't exist.",
        "- **Sentence coverage**: share of answer sentences with a citation.",
        "- **Groundedness**: share of an answer's content words found in the "
        "passages it cites (a rough proxy for not using outside knowledge).",
        "- **Peak RAM**: peak resident memory of the llama-server process.",
        "- **Exact refusal text**: on unanswerable items, replied exactly "
        "\"The sources do not contain the answer.\"",
        "- **Prompt**: prompt variant from `prompts.py` "
        "(+norm = paraphrased refusals replaced by the exact text).",
    ]

    (run_dir / "summary.md").write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", default="baseline")
    parser.add_argument("--models", nargs="*")
    parser.add_argument("--threads", type=int, default=8)
    parser.add_argument("--ctx", type=int, default=4096)
    parser.add_argument("--max-tokens", type=int, default=320)
    parser.add_argument("--prompt", choices=list(VARIANTS), default="v1",
                        help="prompt variant from prompts.py")
    parser.add_argument("--gpu", action="store_true",
                        help="use the CUDA llama.cpp build with all layers on the GPU")
    parser.add_argument("--normalize-refusal", action="store_true",
                        help="replace paraphrased refusals with the exact text")
    parser.add_argument("--limit", type=int, help="only the first N items")
    parser.add_argument("--testset", type=Path, default=DEFAULT_TESTSET)
    args = parser.parse_args()

    registry = json.loads((MODELS_DIR / "models.json").read_text())
    names = args.models or list(registry)

    testset = args.testset.resolve()
    items = [json.loads(line) for line in open(testset, encoding="utf-8")]
    if args.limit:
        items = items[:args.limit]

    server = find_server(gpu=args.gpu)
    run_dir = RESULTS_DIR / args.run
    run_dir.mkdir(parents=True, exist_ok=True)

    all_metrics = []
    for name in names:
        metrics = evaluate_model(name, registry[name], items, server, run_dir, args)
        if metrics:
            all_metrics.append(metrics)

    # Merge with models evaluated earlier in the same run folder.
    evaluated = {m["model"] for m in all_metrics}
    for path in sorted(run_dir.glob("*/metrics.json")):
        previous = json.loads(path.read_text())
        if previous["model"] not in evaluated:
            all_metrics.append(previous)

    if all_metrics:
        order = list(registry)
        all_metrics.sort(key=lambda m: order.index(m["model"])
                         if m["model"] in order else len(order))
        write_summary(run_dir, all_metrics, testset)
        write_reviews(run_dir)
        print(f"\nSummary: {(run_dir / 'summary.md').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
