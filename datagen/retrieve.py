"""
Run the real retrieval pipeline for every seed question and save the
top 20 ranked passages, so dataset generation and evaluation never need
to search again.

    python datagen/retrieve.py                 # all seed questions
    python datagen/retrieve.py --workers 3     # parallel searches

Resumable: questions with a saved file in datagen/raw/ are skipped, so
rerunning retries only the ones that failed (search often rate-limits).
"""

import argparse
import contextlib
import io
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from pipeline import run_retrieval  # noqa: E402

SEEDS = ROOT / "datagen" / "seed_questions.jsonl"
RAW_DIR = ROOT / "datagen" / "raw"
TOP_K = 20
MIN_PASSAGES = 5


def retrieve_one(seed):
    out_path = RAW_DIR / f"{seed['id']}.json"

    # Silence the per-URL prints from search/extract.
    with contextlib.redirect_stdout(io.StringIO()):
        result = run_retrieval(seed["question"], top_k=TOP_K)

    passages = [
        {"title": p["title"], "url": p["url"], "text": p["text"],
         "source_id": p["source_id"], "chunk_id": p["chunk_id"],
         "score": p["score"]}
        for p in result["passages"]
    ]

    if len(passages) < MIN_PASSAGES:
        return seed["id"], False, f"only {len(passages)} passages"

    record = {
        **seed,
        "sources_found": result["sources_found"],
        "chunks_created": result["chunks_created"],
        "passages": passages,
    }
    out_path.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")
    return seed["id"], True, f"{len(passages)} passages"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--ids", nargs="*", help="only these seed ids")
    args = parser.parse_args()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    seeds = [json.loads(line) for line in open(SEEDS, encoding="utf-8")]
    if args.ids:
        seeds = [s for s in seeds if s["id"] in set(args.ids)]
    todo = [s for s in seeds if not (RAW_DIR / f"{s['id']}.json").exists()]

    print(f"{len(seeds)} seeds, {len(seeds) - len(todo)} already done, "
          f"{len(todo)} to retrieve", flush=True)

    start = time.time()
    done = failed = 0

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(retrieve_one, seed): seed for seed in todo}
        for future in as_completed(futures):
            seed = futures[future]
            try:
                seed_id, ok, info = future.result()
            except Exception as error:  # network errors, parser crashes
                seed_id, ok, info = seed["id"], False, repr(error)

            done += ok
            failed += not ok
            if not ok or (done + failed) % 25 == 0:
                rate = (done + failed) / max(time.time() - start, 1) * 60
                print(f"[{done + failed}/{len(todo)}] ok={done} failed={failed} "
                      f"({rate:.1f}/min) {seed_id}: {info}", flush=True)

    total = len(list(RAW_DIR.glob("s*.json")))
    print(f"Finished: {done} new, {failed} failed, {total}/{len(seeds)} on disk. "
          "Rerun to retry failures.", flush=True)


if __name__ == "__main__":
    main()
