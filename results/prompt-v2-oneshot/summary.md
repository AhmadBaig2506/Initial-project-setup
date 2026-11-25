# Results: prompt-v2-oneshot

Test set: `eval/data/baseline_test.jsonl` (27 items). Local models: llama.cpp CPU, 8 threads, context 4096, temperature 0. Frontier models: answers pasted from a chat interface (no speed or RAM figures).

| Model | Params | Prompt | File GB | Device | Peak RAM MB | Peak VRAM MB | Behaviour acc | Answers (answerable) | Refuses (unanswerable) | Exact refusal text | Has citations | Citations valid | Sentence coverage | Groundedness | Off-topic | Words | Prompt tok/s | Gen tok/s | Latency s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| granite-4.0-h-1b | 1B | v2-oneshot+norm | 0.90 | - | 1854 | - | 96% | 95% | 100% | 100% | 57% | 100% | 50% | 83% | 1 | 41 | 148 | 26.3 | 10.0 |
| qwen3-4b-instruct-2507 | 4B | v2-oneshot+norm | 2.50 | - | 4782 | - | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 78% | 0 | 89 | 59 | 9.6 | 31.1 |
| qwen3.5-0.8b | 0.8B | v2-oneshot+norm | 0.53 | - | 938 | - | 96% | 95% | 100% | 100% | 71% | 100% | 69% | 81% | 0 | 56 | 355 | 43.9 | 4.9 |

- **Behaviour acc**: answered answerable questions and refused unanswerable ones.
- **Citations valid**: no citation points to a source number that doesn't exist.
- **Sentence coverage**: share of answer sentences with a citation.
- **Groundedness**: share of an answer's content words found in the passages it cites (a rough proxy for not using outside knowledge).
- **Peak RAM**: peak resident memory of the llama-server process.
- **Exact refusal text**: on unanswerable items, replied exactly "The sources do not contain the answer."
- **Prompt**: prompt variant from `prompts.py` (+norm = paraphrased refusals replaced by the exact text).
