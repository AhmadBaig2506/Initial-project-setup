# Labelling spec: source-grounded answers

You are writing training and test data for a small on-device model. At run time that model receives **exactly** the numbered sources shown for a topic, plus a question, and must answer **only** from those sources.

The rules the model is given (follow them exactly in every answer you write):

> Answer the question using ONLY the numbered sources provided. Do not use any outside knowledge.
> - Cite every sentence with the source number(s) it comes from, like [1] or [2][3].
> - Keep the answer to 2-5 sentences.
> - If the sources do not contain the answer, reply exactly: The sources do not contain the answer.

## What to produce per topic

Each topic in a batch file has a seed question and sources [1]–[5]. For every topic, write these items:

| item | question | label | answer |
|---|---|---|---|
| `seed` | the seed question, unchanged | `answerable`, `partial` or `unanswerable`, judged ONLY from sources [1]–[5] | according to the label (see below) |
| `gen` | a NEW question, different from the seed, that sources [1]–[5] answer **fully** | `answerable` | a cited answer |
| `hard_neg` | a NEW question on the **same topic** that sources [1]–[5] do **not** answer at all, i.e. a natural follow-up a user might ask. Check every source carefully: no part of the answer may be present. | `unanswerable` | exactly `The sources do not contain the answer.` |
| `partial` | **only for topics marked `PARTIAL: yes`**: a two-part question where sources [1]–[5] answer one part and **not** the other | `partial` | the covered part, cited, then one final sentence `The sources do not say <the missing part>.` |

Labels:
- `answerable`: the sources contain enough to answer the question properly.
- `partial`: the sources answer part of the question; another clearly asked part is missing. Answer the covered part, then end with one uncited sentence starting `The sources do not say ...`.
- `unanswerable`: the sources do not answer the question. Answer is exactly `The sources do not contain the answer.`

Edge cases:
- **Thin coverage:** if the sources give a real but brief answer to a one-part question, label it `answerable` and answer with what they say. Use `partial` only when a clearly asked part is missing.
- **Mentions are not answers:** a source that merely mentions something ("sometimes caused by a medical condition") without giving the asked fact does **not** answer it. Avoid such near-misses for `hard_neg`; they work well as the missing half of a `partial` question.

## Answer style (answerable and partial)

- 2–4 sentences, **at most 90 words** (a partial answer may be one cited sentence plus the gap sentence). Concise and direct; lead with the answer.
- End every sentence with `.`, `!` or `?` followed by its citation, and avoid colons or semicolons joining separate claims, so each claim's citation is unambiguous. Avoid abbreviations with internal periods ("A.K.", "v.", "e.g."), because answers are split into sentences at periods.
- **Every sentence ends with its citation(s)**, e.g. `... into glucose [2].` or `... [1][3].` Cite the source(s) that actually support that sentence. Never cite a number above 5. In a partial answer, only the final "The sources do not say ..." sentence is uncited.
- **Only facts stated in the sources.** No outside knowledge, even if you know it is true. If you'd need outside knowledge to fill a gap, leave the gap out (or label `partial` / `unanswerable`).
- Paraphrase naturally. Don't copy long stretches verbatim, but keep key terms, numbers and names exactly as the sources give them.
- Sources may be messy (navigation text, ads, cut-off sentences). Ignore junk; use only clear statements.
- No preamble ("According to the sources..."), no lists, no markdown, no questions back to the user.

## Test topics only: sources [6]–[20]

Topics marked `TEST: yes` also show sources [6]–[20] (lower-ranked passages from the same search). They are **not** given to the model in normal runs; they're used later to test a retry loop. For these topics, for the `seed` item if it isn't `answerable`, and for the `hard_neg` item, also report:
- `answer_in_6_20`: `true` if sources [6]–[20] contain the missing answer, otherwise `false`
- `ranks_6_20`: the list of those source numbers (empty if none)

Everything else (labels, answers, citations) is still judged from sources [1]–[5] only.

## Output

Write **JSON Lines** to the output path given in the batch file: one object per item, no other text. Keys:

```json
{"topic_id": "s0042", "item": "seed", "question": "...", "label": "answerable", "answer": "...", "answer_in_6_20": null, "ranks_6_20": []}
```

- `item`: `seed`, `gen`, `hard_neg` or `partial`
- `label`: `answerable`, `partial` or `unanswerable`
- `answer_in_6_20` / `ranks_6_20`: only meaningful on `TEST: yes` topics; otherwise `null` / `[]`

Every topic needs `seed`, `gen` and `hard_neg` lines, plus `partial` when marked. If a topic's sources are so poor that no fully answerable `gen` question exists, omit only that `gen` line.

## Self-check before finishing

Run a short Python check on your output file:
- valid JSON on every line
- every topic present, with the right items
- every non-refusal answer has citations only in 1–5
- every sentence is cited (except the final partial gap sentence)
- ≤ 90 words
- unanswerable answers are exactly the refusal sentence

Fix any problems, then reply with only: the topic count, the item count per label, and anything you had to skip.
