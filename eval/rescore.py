"""
Recompute metrics from saved answers without re-running any model.

Use after changing eval/metrics.py. Speed, RAM and run settings are kept
from the existing metrics.json.

    python eval/rescore.py --run baseline --testset eval/data/baseline_test.jsonl
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from eval.metrics import aggregate, score_answer  # noqa: E402
from eval.review import write_reviews  # noqa: E402
from eval.run_eval import DEFAULT_TESTSET, RESULTS_DIR, write_summary  # noqa: E402


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", required=True)
    parser.add_argument("--testset", type=Path, default=DEFAULT_TESTSET)
    args = parser.parse_args()

    testset = args.testset.resolve()
    items = {
        item["id"]: item
        for item in map(json.loads, open(testset, encoding="utf-8"))
    }
    run_dir = RESULTS_DIR / args.run
    all_metrics = []

    for metrics_path in sorted(run_dir.glob("*/metrics.json")):
        answers_path = metrics_path.with_name("answers.jsonl")
        rows = [json.loads(line) for line in open(answers_path, encoding="utf-8")]

        for row in rows:
            item = items[row["id"]]
            row.update(score_answer(row["answer"], item["passages"],
                                    item["answerable"],
                                    question=item["question"]))

        with open(answers_path, "w", encoding="utf-8") as file:
            for row in rows:
                file.write(json.dumps(row, ensure_ascii=False) + "\n")

        metrics = json.loads(metrics_path.read_text())
        metrics.setdefault("prompt_variant", "v1")
        metrics.update(aggregate(rows))
        metrics_path.write_text(json.dumps(metrics, indent=2))
        all_metrics.append(metrics)
        print(f"rescored {metrics['model']}")

    all_metrics.sort(key=lambda m: m["model"].startswith("frontier-"))
    write_summary(run_dir, all_metrics, testset)
    write_reviews(run_dir)


if __name__ == "__main__":
    main()
