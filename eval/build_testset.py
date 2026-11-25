"""
Build a frozen test set by running the retrieval pipeline once.

Each item stores the question and its top passages, so every model is
evaluated on exactly the same input (no live search during evaluation).

About a fifth of the items are "unanswerable": the question is paired
with passages retrieved for a different, unrelated question. The
correct behaviour there is to refuse.

    python eval/build_testset.py
"""

import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from pipeline import run_retrieval  # noqa: E402

OUTPUT = ROOT / "eval" / "data" / "baseline_test.jsonl"

QUESTIONS = [
    "What causes sleep apnea?",
    "How do vaccines train the immune system?",
    "Why is the sky blue?",
    "What is the difference between weather and climate?",
    "How does a heat pump work?",
    "What are the main symptoms of type 2 diabetes?",
    "How do lithium-ion batteries degrade over time?",
    "What is the role of mitochondria in a cell?",
    "How does compound interest work?",
    "What causes the seasons on Earth?",
    "How does photosynthesis convert light into energy?",
    "What is quantization in machine learning models?",
    "How do noise-cancelling headphones work?",
    "What are the health benefits of regular walking?",
    "Why do onions make people cry?",
    "How does the BM25 ranking function score documents?",
    "What causes inflation in an economy?",
    "How do coral reefs form?",
    "What is the purpose of a VPN?",
    "How does caffeine affect the brain?",
    "What is the greenhouse effect?",
    "How do solar panels generate electricity?",
    "What causes earthquakes?",
    "How does a refrigerator keep food cold?",
]

# (question, index of an unrelated question whose passages are used)
UNANSWERABLE = [
    ("Who won the 1998 FIFA World Cup?", 4),
    ("What is the boiling point of mercury?", 8),
    ("How many moons does Neptune have?", 12),
    ("What year was the Eiffel Tower completed?", 16),
    ("What is the capital city of Mongolia?", 0),
    ("Who wrote the novel Pride and Prejudice?", 19),
]


def main(top_k=5):
    items = []

    for index, question in enumerate(QUESTIONS):
        print(f"[{index + 1}/{len(QUESTIONS)}] {question}")
        result = run_retrieval(question, top_k=top_k)

        if not result["passages"]:
            print("  no passages, skipped")
            continue

        items.append({
            "id": f"q{index:03d}",
            "question": question,
            "answerable": True,
            "passages": [
                {"title": p["title"], "url": p["url"], "text": p["text"]}
                for p in result["passages"]
            ],
        })

    by_question = {item["question"]: item for item in items}

    for number, (question, source_index) in enumerate(UNANSWERABLE):
        donor = by_question.get(QUESTIONS[source_index])
        if donor is None:
            continue

        items.append({
            "id": f"u{number:03d}",
            "question": question,
            "answerable": False,
            "passages": donor["passages"],
        })

    random.Random(0).shuffle(items)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as file:
        for item in items:
            file.write(json.dumps(item, ensure_ascii=False) + "\n")

    answerable = sum(item["answerable"] for item in items)
    print(f"\nWrote {len(items)} items ({answerable} answerable, "
          f"{len(items) - answerable} unanswerable) to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
