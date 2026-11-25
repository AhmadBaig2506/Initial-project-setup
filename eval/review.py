"""
Write a short review.md per model listing only the answers with problems.

Called automatically by run_eval.py, rescore.py and
frontier/import_responses.py. Can also be run on its own:

    python eval/review.py --run baseline
"""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = ROOT / "results"

MAX_SENTENCES = 5
LOW_GROUNDEDNESS = 0.6
LOW_COVERAGE = 0.8


def flags_for(row):
    """
    Problems with one answer as (category, description) pairs.
    """

    flags = []

    if row.get("error"):
        return [("error", f"ERROR: {row['error']}")]

    if not row["behaviour_correct"]:
        flags.append(("wrong answer/refuse decision",
                      "WRONG DECISION: answered an unanswerable question"
                      if not row["answerable"] else
                      "WRONG DECISION: refused an answerable question"))

    if row["refused"]:
        if not row["answerable"] and not row.get("exact_refusal", True):
            flags.append(("refusal not exact",
                          "refusal not worded exactly as instructed"))
        return flags

    if row.get("off_topic"):
        flags.append(("off-topic answer",
                      "OFF-TOPIC: answer shares no key words with the question "
                      "(copied example or wrong passage?)"))

    if not row["citations"]:
        flags.append(("no citations", "no citations"))
    elif not row["citation_valid"]:
        flags.append(("invalid citations",
                      f"invalid citation numbers {sorted(set(row['citations']))}"))

    coverage = row.get("citation_coverage")
    if row["citations"] and coverage is not None and coverage < LOW_COVERAGE:
        flags.append(("some sentences uncited",
                      f"only {coverage:.0%} of sentences cited"))

    groundedness = row.get("groundedness")
    if groundedness is not None and groundedness < LOW_GROUNDEDNESS:
        flags.append(("low groundedness",
                      f"low groundedness {groundedness:.0%} "
                      "(possible outside knowledge or heavy paraphrase)"))

    sentences = len([s for s in re.split(r"(?<=[.!?])\s+(?!\[)",
                                         row["answer"]) if s.strip()])
    if sentences > MAX_SENTENCES:
        flags.append(("too long",
                      f"too long: {sentences} sentences (limit {MAX_SENTENCES})"))

    if row.get("finish_reason") == "length":
        flags.append(("cut off", "cut off at the token limit"))

    if row.get("had_thinking"):
        flags.append(("thinking text", "emitted <think> text"))

    return flags


def write_review(model_dir):
    answers_path = model_dir / "answers.jsonl"
    if not answers_path.exists():
        return

    rows = [json.loads(line) for line in open(answers_path, encoding="utf-8")]
    flagged = [(row, flags_for(row)) for row in rows]
    flagged = [(row, flags) for row, flags in flagged if flags]

    counts = {}
    for _, flags in flagged:
        for category, _ in flags:
            counts[category] = counts.get(category, 0) + 1

    lines = [
        f"# Review: {model_dir.name} ({model_dir.parent.name})",
        "",
        f"{len(flagged)} of {len(rows)} answers flagged. "
        "Full prompts are in `prompts.md`, raw data in `answers.jsonl`.",
        "",
        "| Problem | Count |",
        "|---|---|",
    ]
    lines += [f"| {key} | {count} |"
              for key, count in sorted(counts.items(), key=lambda kv: -kv[1])]

    for row, flags in flagged:
        lines += [
            "",
            "---",
            "",
            f"## {row['id']}: {row['question']}",
            "",
            f"Answerable: {row['answerable']}",
            "",
            "Problems:",
            *[f"- {text}" for _, text in flags],
            "",
            "Answer:",
            "",
            "````text",
            row.get("answer", ""),
            "````",
        ]
        if row.get("raw_answer") and row["raw_answer"] != row["answer"]:
            lines += ["", "Raw answer before refusal normalization:", "",
                      "````text", row["raw_answer"], "````"]

    (model_dir / "review.md").write_text("\n".join(lines) + "\n",
                                         encoding="utf-8")


def write_reviews(run_dir):
    for model_dir in sorted(p for p in run_dir.iterdir() if p.is_dir()):
        write_review(model_dir)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", required=True)
    args = parser.parse_args()
    write_reviews(RESULTS_DIR / args.run)
    print(f"Wrote review.md files in results/{args.run}/")


if __name__ == "__main__":
    main()
