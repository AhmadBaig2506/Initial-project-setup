# Results: fewshot-5

Test set: `eval/data/baseline_test.jsonl` (27 items). Local models: llama.cpp GPU, 8 threads, context 4096, temperature 0. Frontier models: answers pasted from a chat interface (no speed or RAM figures).

| Model | Params | Prompt | File GB | Device | Peak RAM MB | Peak VRAM MB | Behaviour acc | Answers (answerable) | Refuses (unanswerable) | Exact refusal text | Has citations | Citations valid | Sentence coverage | Groundedness | Off-topic | Words | Prompt tok/s | Gen tok/s | Latency s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| granite-4.0-h-1b | 1B | v5-5shot+norm | 0.90 | gpu | 1230 | 1179 | 85% | 86% | 80% | 80% | 47% | 100% | 36% | 87% | 0 | 56 | 4366 | 141.0 | 0.7 |
| qwen3-4b-instruct-2507 | 4B | v5-5shot+norm | 2.50 | gpu | 2770 | 3199 | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 79% | 0 | 98 | 3691 | 67.4 | 1.9 |
| qwen3.5-0.8b | 0.8B | v5-5shot+norm | 0.53 | gpu | 932 | 757 | 93% | 91% | 100% | 100% | 95% | 100% | 95% | 70% | 0 | 44 | 10522 | 207.7 | 0.3 |

- **Behaviour acc**: answered answerable questions and refused unanswerable ones.
- **Citations valid**: no citation points to a source number that doesn't exist.
- **Sentence coverage**: share of answer sentences with a citation.
- **Groundedness**: share of an answer's content words found in the passages it cites (a rough proxy for not using outside knowledge).
- **Peak RAM**: peak resident memory of the llama-server process.
- **Exact refusal text**: on unanswerable items, replied exactly "The sources do not contain the answer."
- **Prompt**: prompt variant from `prompts.py` (+norm = paraphrased refusals replaced by the exact text).
