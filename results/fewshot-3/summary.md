# Results: fewshot-3

Test set: `eval/data/baseline_test.jsonl` (27 items). Local models: llama.cpp GPU, 8 threads, context 4096, temperature 0. Frontier models: answers pasted from a chat interface (no speed or RAM figures).

| Model | Params | Prompt | File GB | Device | Peak RAM MB | Peak VRAM MB | Behaviour acc | Answers (answerable) | Refuses (unanswerable) | Exact refusal text | Has citations | Citations valid | Sentence coverage | Groundedness | Off-topic | Words | Prompt tok/s | Gen tok/s | Latency s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| granite-4.0-h-1b | 1B | v3-3shot+norm | 0.90 | gpu | 1230 | 1179 | 74% | 73% | 80% | 80% | 50% | 100% | 42% | 88% | 0 | 71 | 4269 | 143.9 | 0.7 |
| qwen3-4b-instruct-2507 | 4B | v3-3shot+norm | 2.50 | gpu | 2770 | 3191 | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 77% | 0 | 101 | 3778 | 68.1 | 1.9 |
| qwen3.5-0.8b | 0.8B | v3-3shot+norm | 0.53 | gpu | 932 | 610 | 100% | 100% | 100% | 100% | 86% | 100% | 84% | 70% | 0 | 48 | 10527 | 211.3 | 0.4 |

- **Behaviour acc**: answered answerable questions and refused unanswerable ones.
- **Citations valid**: no citation points to a source number that doesn't exist.
- **Sentence coverage**: share of answer sentences with a citation.
- **Groundedness**: share of an answer's content words found in the passages it cites (a rough proxy for not using outside knowledge).
- **Peak RAM**: peak resident memory of the llama-server process.
- **Exact refusal text**: on unanswerable items, replied exactly "The sources do not contain the answer."
- **Prompt**: prompt variant from `prompts.py` (+norm = paraphrased refusals replaced by the exact text).
