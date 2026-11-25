# Results: test-v2-5shot

Test set: `eval/data/test_v2.jsonl` (114 items). Local models: llama.cpp GPU, 8 threads, context 4096, temperature 0. Frontier models: answers pasted from a chat interface (no speed or RAM figures).

| Model | Params | Prompt | File GB | Device | Peak RAM MB | Peak VRAM MB | Behaviour acc | Answers (answerable) | Refuses (unanswerable) | Exact refusal text | Has citations | Citations valid | Sentence coverage | Groundedness | Off-topic | Words | Prompt tok/s | Gen tok/s | Latency s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3.5-0.8b | 0.8B | v5-5shot+norm | 0.53 | gpu | 933 | 767 | 76% | 66% | 97% | 97% | 92% | 100% | 90% | 68% | 0 | 43 | 9233 | 198.0 | 0.3 |
| granite-4.0-h-1b | 1B | v5-5shot+norm | 0.90 | gpu | 1231 | 1195 | 79% | 87% | 62% | 62% | 43% | 100% | 37% | 79% | 2 | 45 | 4121 | 143.1 | 0.5 |
| qwen3-4b-instruct-2507 | 4B | v5-5shot+norm | 2.50 | gpu | 2770 | 3199 | 98% | 99% | 97% | 97% | 100% | 100% | 96% | 77% | 0 | 84 | 2423 | 67.6 | 1.4 |

- **Behaviour acc**: answered answerable questions and refused unanswerable ones.
- **Citations valid**: no citation points to a source number that doesn't exist.
- **Sentence coverage**: share of answer sentences with a citation.
- **Groundedness**: share of an answer's content words found in the passages it cites (a rough proxy for not using outside knowledge).
- **Peak RAM**: peak resident memory of the llama-server process.
- **Exact refusal text**: on unanswerable items, replied exactly "The sources do not contain the answer."
- **Prompt**: prompt variant from `prompts.py` (+norm = paraphrased refusals replaced by the exact text).
