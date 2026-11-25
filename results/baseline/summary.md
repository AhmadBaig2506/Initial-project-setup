# Results: baseline

Test set: `eval/data/baseline_test.jsonl` (27 items). Local models: llama.cpp CPU, 8 threads, context 4096, temperature 0. Frontier models: answers pasted from a chat interface (no speed or RAM figures).

| Model | Params | Prompt | File GB | Device | Peak RAM MB | Peak VRAM MB | Behaviour acc | Answers (answerable) | Refuses (unanswerable) | Exact refusal text | Has citations | Citations valid | Sentence coverage | Groundedness | Off-topic | Words | Prompt tok/s | Gen tok/s | Latency s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| granite-4.0-h-1b | 1B | v1 | 0.90 | - | 1854 | - | 100% | 100% | 100% | 20% | 32% | 100% | 27% | 90% | 0 | 45 | 155 | 28.0 | 9.7 |
| qwen3-4b-instruct-2507 | 4B | v1 | 2.50 | - | 4781 | - | 100% | 100% | 100% | 100% | 100% | 100% | 98% | 77% | 0 | 91 | 57 | 9.1 | 33.6 |
| qwen3.5-0.8b | 0.8B | v1 | 0.53 | - | 937 | - | 100% | 100% | 100% | 0% | 9% | 100% | 8% | 85% | 0 | 54 | 350 | 44.5 | 4.9 |

- **Behaviour acc**: answered answerable questions and refused unanswerable ones.
- **Citations valid**: no citation points to a source number that doesn't exist.
- **Sentence coverage**: share of answer sentences with a citation.
- **Groundedness**: share of an answer's content words found in the passages it cites (a rough proxy for not using outside knowledge).
- **Peak RAM**: peak resident memory of the llama-server process.
- **Exact refusal text**: on unanswerable items, replied exactly "The sources do not contain the answer."
- **Prompt**: prompt variant from `prompts.py` (+norm = paraphrased refusals replaced by the exact text).
