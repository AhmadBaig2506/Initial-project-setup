"""
Convert a fine-tuned (merged) model to GGUF, quantize it, and register
each file in models/models.json so eval/run_eval.py can benchmark it.

    training/.venv/bin/python training/export.py --run qwen35-08b-v1
    training/.venv/bin/python training/export.py --run qwen35-08b-v1 --quants Q4_K_M Q8_0

Uses llama.cpp b12314: tools/llama.cpp-src/ for convert_hf_to_gguf.py and
tools/llama.cpp/ for llama-quantize (same version as inference).

Outputs: models/<run>-<quant>/<run>-<quant>.gguf
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "training" / "runs"
MODELS_DIR = ROOT / "models"


def find(pattern, folder):
    match = next(folder.rglob(pattern), None)
    if match is None:
        raise SystemExit(f"{pattern} not found under {folder}")
    return match


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", required=True, help="training/runs/<run>")
    parser.add_argument("--quants", nargs="*", default=["Q4_K_M"])
    parser.add_argument("--keep-f16", action="store_true")
    args = parser.parse_args()

    merged = RUNS / args.run / "merged"
    if not merged.exists():
        raise SystemExit(f"{merged} not found; run training/finetune.py first")

    convert = find("convert_hf_to_gguf.py", ROOT / "tools" / "llama.cpp-src")
    quantize = find("llama-quantize", ROOT / "tools" / "llama.cpp")
    gguf_py = convert.parent / "gguf-py"

    f16 = RUNS / args.run / f"{args.run}-F16.gguf"
    env = {**os.environ, "PYTHONPATH": str(gguf_py)}
    subprocess.run([sys.executable, str(convert), str(merged),
                    "--outfile", str(f16), "--outtype", "f16"],
                   check=True, env=env)

    registry_path = MODELS_DIR / "models.json"
    registry = json.loads(registry_path.read_text())
    train_log = RUNS / args.run / "train_log.json"
    config = json.loads((RUNS / args.run / "config.json").read_text())

    for quant in args.quants:
        name = f"{args.run}-{quant.lower()}"
        out = MODELS_DIR / name / f"{name}.gguf"
        out.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run([str(quantize), str(f16), str(out), quant], check=True,
                       env={**os.environ, "LD_LIBRARY_PATH": str(quantize.parent)})
        registry[name] = {
            "repo": None,
            "file": out.name,
            "params": config.get("model", "").split("/")[-1],
            "notes": f"fine-tuned run {args.run} ({quant}); base {config.get('model')}"
                     + ("; see training/runs/" + args.run if train_log.exists() else ""),
        }
        print(f"Wrote {out.relative_to(ROOT)} ({out.stat().st_size / 1e9:.2f} GB)")

    registry_path.write_text(json.dumps(registry, indent=2) + "\n")
    if not args.keep_f16:
        f16.unlink()
    print("Registered in models/models.json:",
          ", ".join(f"{args.run}-{q.lower()}" for q in args.quants))


if __name__ == "__main__":
    main()
