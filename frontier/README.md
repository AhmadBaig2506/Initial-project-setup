# Frontier model answers

Compare frontier chat models (ChatGPT, Gemini, Claude, ...) with the local
models on exactly the same instructions and sources.

## Sets

| Folder | Test set | Items |
|---|---|---|
| `frontier/` (`prompts/`, `responses/`) | `eval/data/mini_test.jsonl` | 5 |
| `frontier/baseline/` | `eval/data/baseline_test.jsonl` | 27 (22 answerable, 5 unanswerable) |

Inside each set:

| Folder | What it holds |
|---|---|
| `prompts/<id>.md` | One question per chat: the most faithful comparison |
| `batches/batch_NN.md` | 9 questions per chat: much faster to fill |
| `responses/<model>/` | Empty answer files to fill: `<id>.txt` and `batch_NN.txt` |

## How to fill it

Use **either** the single-question prompts **or** the batches; you don't need both.

**Single questions**
1. Open a new chat per question. Turn off web search, memory and custom instructions.
2. Paste (or upload) `prompts/<id>.md` and send it.
3. Paste the reply into `responses/<model>/<id>.txt`. Copying the prompt along with the reply is fine; the importer removes it.

**Batches**
1. Open a new chat per batch, with the same settings as above.
2. Paste (or upload) `batches/batch_NN.md` and send it.
3. Paste the whole reply into `responses/<model>/batch_NN.txt`. It must keep the `=== <id> ===` headers.

To add another model, create `responses/<name>/` with the same file names. Leave a file empty to skip it.
A single-question answer wins over a batch answer for the same id.

## Score the answers

```bash
# mini set -> results/mini/
python frontier/import_responses.py

# 27-question set -> results/baseline/
python frontier/import_responses.py --dir frontier/baseline --run baseline \
    --testset eval/data/baseline_test.jsonl
```

This scores the answers with the same metrics as the local models, adds
`frontier-<model>/` to the results run, and rebuilds `summary.md` with local
and frontier models in one table.

## Regenerate prompts

```bash
python frontier/make_prompts.py --testset eval/data/baseline_test.jsonl \
    --dir frontier/baseline --models claude-opus-5_5
```
