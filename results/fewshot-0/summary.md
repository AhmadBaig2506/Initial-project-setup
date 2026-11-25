# Results: fewshot-0

Test set: `eval/data/baseline_test.jsonl` (27 items). Local models: llama.cpp GPU, 8 threads, context 4096, temperature 0. Frontier models: answers pasted from a chat interface (no speed or RAM figures).

| Model | Params | Prompt | File GB | Device | Peak RAM MB | Peak VRAM MB | Behaviour acc | Answers (answerable) | Refuses (unanswerable) | Exact refusal text | Has citations | Citations valid | Sentence coverage | Groundedness | Off-topic | Words | Prompt tok/s | Gen tok/s | Latency s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| granite-4.0-h-1b | 1B | v1+norm | 0.90 | gpu | 1230 | 1179 | 100% | 100% | 100% | 100% | 41% | 100% | 33% | 94% | 0 | 47 | 4324 | 146.8 | 0.7 |
| qwen3-4b-instruct-2507 | 4B | v1+norm | 2.50 | gpu | 2770 | 3191 | 100% | 100% | 100% | 100% | 100% | 100% | 98% | 78% | 0 | 91 | 3920 | 69.4 | 1.7 |
| qwen3.5-0.8b | 0.8B | v1+norm | 0.53 | gpu | 932 | 757 | 100% | 100% | 100% | 100% | 9% | 100% | 9% | 85% | 0 | 54 | 10577 | 214.0 | 0.4 |

- **Behaviour acc**: answered answerable questions and refused unanswerable ones.
- **Citations valid**: no citation points to a source number that doesn't exist.
- **Sentence coverage**: share of answer sentences with a citation.
- **Groundedness**: share of an answer's content words found in the passages it cites (a rough proxy for not using outside knowledge).
- **Peak RAM**: peak resident memory of the llama-server process.
- **Exact refusal text**: on unanswerable items, replied exactly "The sources do not contain the answer."
- **Prompt**: prompt variant from `prompts.py` (+norm = paraphrased refusals replaced by the exact text).
