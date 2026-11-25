# Results: single-question

Test set: `eval/data/baseline_test.jsonl` (1 items). llama.cpp CPU, 8 threads, context 4096, temperature 0.

| Model | Params | File GB | Peak RAM MB | Behaviour acc | Answers (answerable) | Refuses (unanswerable) | Has citations | Citations valid | Sentence coverage | Groundedness | Words | Prompt tok/s | Gen tok/s | Latency s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3.5-0.8b | 0.8B | 0.53 | 931 | 100% | 100% | - | 0% | 100% | 0% | 83% | 30 | 335 | 44.2 | 4.6 |
| granite-4.0-h-1b | 1B | 0.90 | 1846 | 100% | 100% | - | 100% | 100% | 100% | 100% | 82 | 148 | 27.5 | 12.0 |
| qwen3.5-2b | 2B | 1.28 | 1992 | 100% | 100% | - | 100% | 100% | 100% | 74% | 82 | 140 | 19.4 | 14.3 |
| qwen3-4b-instruct-2507 | 4B | 2.50 | 4775 | 100% | 100% | - | 100% | 100% | 100% | 78% | 115 | 60 | 9.7 | 37.3 |
| gemma-3-4b-it | 4B | 2.49 | 4445 | 100% | 100% | - | 100% | 100% | 100% | 61% | 64 | 67 | 11.7 | 27.0 |

- **Behaviour acc**: answered answerable questions and refused unanswerable ones.
- **Citations valid**: no citation points to a source number that doesn't exist.
- **Sentence coverage**: share of answer sentences with a citation.
- **Groundedness**: share of an answer's content words found in the passages it cites (a rough proxy for not using outside knowledge).
- **Peak RAM**: peak resident memory of the llama-server process.
