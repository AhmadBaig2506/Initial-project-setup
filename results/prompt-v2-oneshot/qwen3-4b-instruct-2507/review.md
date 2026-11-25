# Review: qwen3-4b-instruct-2507 (prompt-v2-oneshot)

1 of 27 answers flagged. Full prompts are in `prompts.md`, raw data in `answers.jsonl`.

| Problem | Count |
|---|---|
| low groundedness | 1 |

---

## q015: How does the BM25 ranking function score documents?

Answerable: True

Problems:
- low groundedness 51% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The BM25 ranking function scores documents by multiplying the inverse document frequency (IDF) of each query term by the term frequency in the document, adjusted for document length normalization and term frequency saturation [3]. It sums these values across all query terms to produce a total score, where higher scores indicate greater relevance [2]. The function normalizes by the document length relative to the corpus average, allowing short, focused documents to outrank longer ones [5]. This scoring is based on the rarity of terms and their frequency in the document, with adjustments to prevent over-penalization of long documents [4]. The formula incorporates tuning parameters to balance term frequency and document length effects [2].
````
