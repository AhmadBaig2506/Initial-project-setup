"""
Build a small 5-question test set for quick comparisons
(local models and frontier models answering by hand).

Reuses q003 from the frozen baseline set and retrieves passages for
three new questions. The fifth item is unanswerable: its passages come
from an unrelated question, so the correct reply is a refusal.

    python eval/build_mini_testset.py
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from pipeline import run_retrieval  # noqa: E402

BASELINE = ROOT / "eval" / "data" / "baseline_test.jsonl"
OUTPUT = ROOT / "eval" / "data" / "mini_test.jsonl"

REUSED_ID = "q003"  # What is the difference between weather and climate?

NEW_QUESTIONS = [
    ("m001", "What is the difference between a virus and a bacterium?"),
    ("m002", "How does regenerative braking work in electric cars?"),
    ("m003", "How does the liver help remove toxins from the body?"),
]

# Asked against the passages of m002 (regenerative braking).
UNANSWERABLE = ("m004", "What is the population of Reykjavik?", "m002")


def main(top_k=5):
    baseline = {
        item["id"]: item
        for item in map(json.loads, open(BASELINE, encoding="utf-8"))
    }
    items = [baseline[REUSED_ID]]

    for item_id, question in NEW_QUESTIONS:
        print(f"Retrieving: {question}")
        result = run_retrieval(question, top_k=top_k)

        if not result["passages"]:
            raise SystemExit(f"No passages for {question!r}; try again later.")

        items.append({
            "id": item_id,
            "question": question,
            "answerable": True,
            "passages": [
                {"title": p["title"], "url": p["url"], "text": p["text"]}
                for p in result["passages"]
            ],
        })

    item_id, question, donor_id = UNANSWERABLE
    donor = next(item for item in items if item["id"] == donor_id)
    items.append({
        "id": item_id,
        "question": question,
        "answerable": False,
        "passages": donor["passages"],
    })

    with open(OUTPUT, "w", encoding="utf-8") as file:
        for item in items:
            file.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"Wrote {len(items)} items to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
