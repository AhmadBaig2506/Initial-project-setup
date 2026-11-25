"""
Assign topics to test / val / train and write labelling batch files.

    python datagen/make_label_batches.py

Split (by topic, stratified by domain, fixed seed):
    test:  1 topic per domain  (shown with sources [6]-[20] as well)
Batches are fixed from the seed list. A batch file is written once all
its topics are retrieved (or with --final, using whatever is retrieved);
existing batch files are never rewritten.
    val:   1 topic per domain
    train: the rest

Writes:
    datagen/splits.json                 topic id -> split
    datagen/batches/batch_NN.md         labelling input (see SPEC.md)
Labels are written by the labellers to datagen/labels/batch_NN.jsonl.
"""

import json
import random
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from prompts import MAX_PASSAGE_WORDS, format_passages  # noqa: E402

SEEDS = ROOT / "datagen" / "seed_questions.jsonl"
RAW_DIR = ROOT / "datagen" / "raw"
BATCH_DIR = ROOT / "datagen" / "batches"
LABEL_DIR = ROOT / "datagen" / "labels"
SPLITS = ROOT / "datagen" / "splits.json"

TRAIN_BATCH = 20
TEST_BATCH = 6
PARTIAL_EVERY = 3  # every 3rd topic also gets a partial item


def format_extra(passages, first_number=6):
    """
    Ranks 6-20 for test topics, numbered [6]..[20], each truncated to the
    same per-passage length as the model's own sources (no total cap).
    """

    return "\n\n".join(
        f"[{number}] {p['title']}\n{' '.join(p['text'].split()[:MAX_PASSAGE_WORDS])}"
        for number, p in enumerate(passages, start=first_number)
    )


def topic_block(record, split, partial):
    top5 = record["passages"][:5]
    lines = [
        f"## TOPIC {record['id']}",
        f"Domain: {record['domain']}",
        f"Seed question: {record['question']}",
        f"PARTIAL: {'yes' if partial else 'no'}",
        f"TEST: {'yes' if split == 'test' else 'no'}",
        "",
        "Sources [1]-[5] (exactly what the model sees):",
        "",
        format_passages(top5),
    ]
    if split == "test":
        extra = record["passages"][5:20]
        lines += ["", "Sources [6]-[20] (test only, for answer_in_6_20):", "",
                  format_extra(extra)]
    return "\n".join(lines)


def main():
    final = "--final" in sys.argv
    seeds = [json.loads(line) for line in open(SEEDS, encoding="utf-8")]
    raw = {p.stem: json.loads(p.read_text(encoding="utf-8"))
           for p in RAW_DIR.glob("s*.json")}
    print(f"{len(raw)}/{len(seeds)} topics retrieved")

    # Split from the seed list (not from what's retrieved), so batches are
    # stable and can be labelled while retrieval is still running.
    by_domain = defaultdict(list)
    for seed in seeds:
        by_domain[seed["domain"]].append(seed["id"])

    rng = random.Random(42)
    splits = {}
    for domain, ids in sorted(by_domain.items()):
        ids = sorted(ids)
        rng.shuffle(ids)
        splits[ids[0]] = "test"
        splits[ids[1]] = "val"
        for topic_id in ids[2:]:
            splits[topic_id] = "train"
    SPLITS.write_text(json.dumps(splits, indent=1))

    test = sorted(t for t, sp in splits.items() if sp == "test")
    other = sorted(t for t, sp in splits.items() if sp != "test")
    groups = [test[i:i + TEST_BATCH] for i in range(0, len(test), TEST_BATCH)]
    groups += [other[i:i + TRAIN_BATCH] for i in range(0, len(other), TRAIN_BATCH)]

    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    LABEL_DIR.mkdir(parents=True, exist_ok=True)
    ready, waiting = [], []

    for number, group in enumerate(groups, start=1):
        name = f"batch_{number:02d}"
        batch_path = BATCH_DIR / f"{name}.md"
        missing = [t for t in group if t not in raw]

        if batch_path.exists():
            ready.append(name)
            continue
        if missing and not final:
            waiting.append(f"{name} ({len(missing)} missing)")
            continue

        present = [raw[t] for t in group if t in raw]
        if not present:
            continue
        out_path = LABEL_DIR / f"{name}.jsonl"
        header = (
            f"# Labelling {name}\n\n"
            f"Follow `datagen/SPEC.md` exactly.\n\n"
            f"Write your output to: {out_path}\n\n"
            f"Topics in this batch: {len(present)} "
            f"({', '.join(r['id'] for r in present)})\n"
        )
        blocks = [
            topic_block(r, splits[r["id"]],
                        partial=int(r["id"][1:]) % PARTIAL_EVERY == 0)
            for r in present
        ]
        batch_path.write_text(
            header + "\n\n" + "\n\n---\n\n".join(blocks) + "\n", encoding="utf-8"
        )
        ready.append(name)

    n_test = len(range(0, len(test), TEST_BATCH))
    print(f"{len(groups)} batches total (batch_01..batch_{n_test:02d} are test). "
          f"Ready: {len(ready)}. Waiting: {len(waiting)}")
    print("ready:", " ".join(ready))
    if waiting:
        print("waiting:", " ".join(waiting))


if __name__ == "__main__":
    main()
