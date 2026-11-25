"""
Download the baseline GGUF models and the llama.cpp CPU binaries.

    python scripts/download_models.py            # all models + llama.cpp
    python scripts/download_models.py qwen3.5-2b # one model

Models go to models/<name>/<file>.gguf, llama.cpp to tools/llama.cpp/.
Both are git-ignored.
"""

import json
import sys
import tarfile
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = ROOT / "models"
TOOLS_DIR = ROOT / "tools" / "llama.cpp"

# Pinned llama.cpp release (CPU build). Supports Qwen3.5 and Granite-4.0-H.
LLAMA_CPP_TAG = "b12314"
LLAMA_CPP_URL = (
    "https://github.com/ggml-org/llama.cpp/releases/download/"
    f"{LLAMA_CPP_TAG}/llama-{LLAMA_CPP_TAG}-bin-ubuntu-x64.tar.gz"
)


def download(url, dest):
    if dest.exists():
        print(f"Already present: {dest.relative_to(ROOT)}")
        return

    dest.parent.mkdir(parents=True, exist_ok=True)
    partial = dest.with_suffix(dest.suffix + ".part")

    with requests.get(url, stream=True, timeout=60) as response:
        response.raise_for_status()
        total = int(response.headers.get("Content-Length", 0))
        done = 0

        with open(partial, "wb") as file:
            for block in response.iter_content(chunk_size=1 << 20):
                file.write(block)
                done += len(block)
                if total:
                    print(f"\r{dest.name}: {done / total:6.1%}", end="")

    print()
    partial.rename(dest)


def get_llama_cpp():
    server = next(TOOLS_DIR.rglob("llama-server"), None) if TOOLS_DIR.exists() else None
    if server:
        print(f"llama.cpp already present: {server.relative_to(ROOT)}")
        return

    archive = TOOLS_DIR / f"llama-{LLAMA_CPP_TAG}.tar.gz"
    download(LLAMA_CPP_URL, archive)

    with tarfile.open(archive) as tar:
        tar.extractall(TOOLS_DIR, filter="data")

    archive.unlink()

    for binary in TOOLS_DIR.rglob("llama-*"):
        if binary.is_file():
            binary.chmod(0o755)


def main():
    registry = json.loads((MODELS_DIR / "models.json").read_text())
    names = sys.argv[1:] or list(registry)

    get_llama_cpp()

    for name in names:
        entry = registry[name]
        if not entry.get("repo"):
            continue  # locally produced model (e.g. fine-tuned), nothing to download
        url = f"https://huggingface.co/{entry['repo']}/resolve/main/{entry['file']}"
        download(url, MODELS_DIR / name / entry["file"])


if __name__ == "__main__":
    main()
