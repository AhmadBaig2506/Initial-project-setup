# Results: mini

Test set: `eval/data/mini_test.jsonl` (5 items). Local models: llama.cpp CPU, 8 threads, context 4096, temperature 0. Frontier models: answers pasted from a chat interface (no speed or RAM figures).

| Model | Params | Prompt | File GB | Device | Peak RAM MB | Peak VRAM MB | Behaviour acc | Answers (answerable) | Refuses (unanswerable) | Exact refusal text | Has citations | Citations valid | Sentence coverage | Groundedness | Off-topic | Words | Prompt tok/s | Gen tok/s | Latency s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gemma-3-4b-it | 4B | v1 | 2.49 | - | 4456 | - | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 74% | 0 | 72 | 67 | 10.0 | 27.3 |
| granite-4.0-h-1b | 1B | v1 | 0.90 | - | 1849 | - | 100% | 100% | 100% | 0% | 75% | 100% | 75% | 90% | 0 | 43 | 149 | 26.3 | 10.1 |
| qwen3-4b-instruct-2507 | 4B | v1 | 2.50 | - | 4777 | - | 100% | 100% | 100% | 100% | 100% | 100% | 95% | 66% | 0 | 106 | 60 | 9.9 | 32.4 |
| qwen3.5-0.8b | 0.8B | v1 | 0.53 | - | 933 | - | 100% | 100% | 100% | 0% | 0% | 100% | 0% | 77% | 0 | 60 | 335 | 43.1 | 5.3 |
| qwen3.5-2b | 2B | v1 | 1.28 | - | 1995 | - | 100% | 100% | 100% | 0% | 100% | 100% | 100% | 64% | 0 | 79 | 154 | 22.7 | 12.1 |
| frontier-claude-opus-5_5 | frontier | v1 | - | - | - | - | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 86% | 0 | 132 | - | - | - |

- **Behaviour acc**: answered answerable questions and refused unanswerable ones.
- **Citations valid**: no citation points to a source number that doesn't exist.
- **Sentence coverage**: share of answer sentences with a citation.
- **Groundedness**: share of an answer's content words found in the passages it cites (a rough proxy for not using outside knowledge).
- **Peak RAM**: peak resident memory of the llama-server process.
- **Exact refusal text**: on unanswerable items, replied exactly "The sources do not contain the answer."
- **Prompt**: prompt variant from `prompts.py` (+norm = paraphrased refusals replaced by the exact text).
