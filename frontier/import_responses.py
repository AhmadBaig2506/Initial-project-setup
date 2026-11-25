"""
Score frontier-model answers with the same metrics as the local models
and add them to a results run.

    python frontier/import_responses.py                       # mini set
    python frontier/import_responses.py --dir frontier/baseline \
        --run baseline --testset eval/data/baseline_test.jsonl

Reads <dir>/responses/<model>/:
    <id>.txt        a single-question reply
    batch_NN.txt    a batch reply with `=== <id> ===` headers
Empty files are skipped; a single-question file wins over a batch answer.

Writes results/<run>/frontier-<model>/answers.jsonl, metrics.json and
prompts.md, then rebuilds results/<run>/summary.md so local and frontier
models appear in one table.
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from prompts import build_messages  # noqa: E402
from eval.metrics import aggregate, score_answer, strip_thinking  # noqa: E402
from eval.review import write_reviews  # noqa: E402
from eval.run_eval import RESULTS_DIR, write_summary  # noqa: E402
from frontier.make_prompts import DEFAULT_DIR, DEFAULT_TESTSET, paste_text  # noqa: E402

BATCH_HEADER = re.compile(r"^\s*=+\s*([A-Za-z0-9_\-]+)\s*=+\s*$", re.MULTILINE)


def strip_pasted_prompt(text, prompt):
    """
    If the file starts with the pasted prompt (e.g. a whole chat was
    copied), keep only what comes after the final "Question: ..." line.
    """

    question_line = prompt.rstrip().splitlines()[-1]
    starts_with_prompt = text.lstrip().startswith(prompt.strip()[:200])

    if starts_with_prompt and question_line in text:
        return text[text.rfind(question_line) + len(question_line):].strip(), True

    return text.strip(), False


def parse_batch(text):
    """
    Split a batch reply into {id: answer} using `=== <id> ===` headers.
    """

    answers = {}
    matches = list(BATCH_HEADER.finditer(text))

    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        answer = text[match.end():end].strip().strip("`").strip()
        if answer:
            answers[match.group(1)] = answer

    return answers


def collect_answers(model_dir, items):
    """
    {id: answer} from single-question files, then batch files.
    """

    answers = {}

    for batch_file in sorted(model_dir.glob("batch_*.txt")):
        found = parse_batch(batch_file.read_text(encoding="utf-8"))
        if found:
            print(f"  {model_dir.name}/{batch_file.name}: {len(found)} answers")
        answers.update(found)

    for item in items:
        answer_file = model_dir / f"{item['id']}.txt"
        if not answer_file.exists():
            continue

        prompt = paste_text(build_messages(item["question"], item["passages"]))
        answer, had_prompt = strip_pasted_prompt(
            answer_file.read_text(encoding="utf-8"), prompt
        )
        if not answer:
            continue
        if had_prompt:
            print(f"  {model_dir.name}/{answer_file.name}: "
                  "removed the pasted prompt, kept the reply")
        answers[item["id"]] = answer

    return answers


def import_model(model_dir, items, run_dir):
    answers = collect_answers(model_dir, items)
    rows = []

    for item in items:
        if item["id"] not in answers:
            continue

        answer = answers[item["id"]]
        row = {
            "id": item["id"],
            "question": item["question"],
            "answerable": item["answerable"],
            "messages": build_messages(item["question"], item["passages"]),
            "latency_s": None,
            "prompt_tok_per_s": None,
            "gen_tok_per_s": None,
        }
        row.update(score_answer(answer, item["passages"], item["answerable"],
            question=item["question"]))
        row["answer"] = strip_thinking(answer)[0]
        rows.append(row)

    if not rows:
        return None

    name = f"frontier-{model_dir.name}"
    out_dir = run_dir / name
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "answers.jsonl", "w", encoding="utf-8") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")

    with open(out_dir / "prompts.md", "w", encoding="utf-8") as file:
        file.write(f"# {name}: prompts and answers\n\n"
                   "Prompt = the single-question text for this item "
                   "(batch answers used the same instructions and sources).\n")
        for row in rows:
            file.write(
                f"\n---\n\n## {row['id']}: {row['question']}\n\n"
                f"Answerable: {row['answerable']}\n\n"
                f"### Prompt\n\n````text\n{paste_text(row['messages'])}````\n\n"
                f"### Answer\n\n````text\n{row['answer']}\n````\n"
            )

    metrics = {"model": name, "params": "frontier", **aggregate(rows)}
    missing = [item["id"] for item in items if item["id"] not in answers]
    if missing:
        metrics["note"] = f"missing answers: {', '.join(missing)}"

    (out_dir / "metrics.json").write_text(json.dumps(metrics, indent=2))
    print(f"{name}: {len(rows)}/{len(items)} answers scored"
          + (f" (missing {len(missing)})" if missing else ""))
    return metrics


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=Path, default=DEFAULT_DIR)
    parser.add_argument("--run", default="mini")
    parser.add_argument("--testset", type=Path, default=DEFAULT_TESTSET)
    args = parser.parse_args()

    testset = args.testset.resolve()
    items = [json.loads(line) for line in open(testset, encoding="utf-8")]
    run_dir = RESULTS_DIR / args.run
    run_dir.mkdir(parents=True, exist_ok=True)

    responses_dir = args.dir / "responses"
    for model_dir in sorted(p for p in responses_dir.iterdir() if p.is_dir()):
        if not import_model(model_dir, items, run_dir):
            print(f"frontier-{model_dir.name}: no answers filled in, skipped")

    all_metrics = [
        json.loads(path.read_text())
        for path in sorted(run_dir.glob("*/metrics.json"))
    ]
    # Local models first, frontier models last.
    all_metrics.sort(key=lambda m: m["model"].startswith("frontier-"))

    if all_metrics:
        write_summary(run_dir, all_metrics, testset)
        write_reviews(run_dir)
        print(f"Summary: {(run_dir / 'summary.md').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
