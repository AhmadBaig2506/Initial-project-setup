"""
Measure what each prompt variant costs: full prompt tokens and the
prompt-processing (prefill) time with llama.cpp's prompt cache disabled.

run_eval.py's timings reuse the cached system prompt between questions,
which hides the cost of longer few-shot prompts. This script measures
the uncached cost, i.e. the first question after the model loads.

    python eval/prompt_cost.py --gpu
    python eval/prompt_cost.py --gpu --variants v1 v3-3shot v5-5shot --limit 10

Writes results/prompt-cost/<device>.json and .md
"""

import argparse
import json
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from prompts import VARIANTS, build_messages  # noqa: E402
from eval.run_eval import (  # noqa: E402
    DEFAULT_TESTSET, MODELS_DIR, PORT, RESULTS_DIR, find_server,
    peak_rss_mb, render_prompt, start_server, VramMonitor,
)


def measure(messages):
    prompt = render_prompt(messages)
    tokens = requests.post(f"http://127.0.0.1:{PORT}/tokenize",
                           json={"content": prompt}, timeout=60).json()["tokens"]

    response = requests.post(
        f"http://127.0.0.1:{PORT}/completion",
        json={"prompt": prompt, "n_predict": 1, "cache_prompt": False,
              "temperature": 0},
        timeout=600,
    ).json()
    timings = response.get("timings", {})
    return len(tokens), timings.get("prompt_ms"), timings.get("prompt_per_second")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", nargs="*",
                        default=["qwen3.5-0.8b", "granite-4.0-h-1b",
                                 "qwen3-4b-instruct-2507"])
    parser.add_argument("--variants", nargs="*",
                        default=["v1", "v2-oneshot", "v3-3shot", "v5-5shot"])
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--gpu", action="store_true")
    parser.add_argument("--threads", type=int, default=8)
    parser.add_argument("--ctx", type=int, default=4096)
    args = parser.parse_args()

    registry = json.loads((MODELS_DIR / "models.json").read_text())
    items = [json.loads(line) for line in open(DEFAULT_TESTSET, encoding="utf-8")]
    items = items[:args.limit]
    server = find_server(gpu=args.gpu)
    device = "gpu" if args.gpu else "cpu"

    out_dir = RESULTS_DIR / "prompt-cost"
    out_dir.mkdir(parents=True, exist_ok=True)
    results = []

    for name in args.models:
        model_path = MODELS_DIR / name / registry[name]["file"]
        log_path = out_dir / f"{name}-{device}.log"

        with open(log_path, "w") as log_file:
            vram = VramMonitor().start() if args.gpu else None
            process = start_server(server, model_path, log_file, args)
            try:
                for variant in args.variants:
                    stats = [measure(build_messages(i["question"], i["passages"],
                                                    variant=variant))
                             for i in items]
                    tokens = sum(s[0] for s in stats) / len(stats)
                    prefill_ms = sum(s[1] for s in stats) / len(stats)
                    results.append({
                        "model": name, "device": device, "variant": variant,
                        "prompt_tokens": tokens,
                        "system_tokens": None,
                        "prefill_ms": prefill_ms,
                        "prefill_tok_per_s": tokens / (prefill_ms / 1000),
                    })
                    print(f"{name:24} {variant:11} {tokens:7.0f} tokens "
                          f"{prefill_ms:8.1f} ms prefill", flush=True)
                ram = peak_rss_mb(process.pid)
            finally:
                process.terminate()
                process.wait(timeout=30)
                peak_vram = vram.stop() if vram else None

        for row in results:
            if row["model"] == name:
                row["peak_ram_mb"], row["peak_vram_mb"] = ram, peak_vram

    (out_dir / f"{device}.json").write_text(json.dumps(results, indent=2))

    lines = [f"# Prompt cost per variant ({device.upper()}, prompt cache off, "
             f"{len(items)} items)", "",
             "| Model | Variant | Prompt tokens | +tokens vs v1 | Prefill ms | "
             "+ms vs v1 | Peak RAM MB | Peak VRAM MB |",
             "|---|---|---|---|---|---|---|---|"]
    for row in results:
        base = next(r for r in results
                    if r["model"] == row["model"] and r["variant"] == "v1")
        lines.append(
            f"| {row['model']} | {row['variant']} | {row['prompt_tokens']:.0f} | "
            f"{row['prompt_tokens'] - base['prompt_tokens']:+.0f} | "
            f"{row['prefill_ms']:.0f} | {row['prefill_ms'] - base['prefill_ms']:+.0f} | "
            f"{row['peak_ram_mb']:.0f} | "
            f"{row['peak_vram_mb'] if row['peak_vram_mb'] is not None else '-'} |"
        )
    (out_dir / f"{device}.md").write_text("\n".join(lines) + "\n")
    print(f"Wrote {(out_dir / f'{device}.md').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
