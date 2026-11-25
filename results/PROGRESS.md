# Progress log

A dated log of every experiment. The newest entry goes at the bottom. Old entries are never rewritten; corrections are added as new entries.

Branch: `local-model-baseline`. All local runs use llama.cpp b12314, CPU only, 8 threads, context 4096, temperature 0, Q4_K_M weights.

**Agreed order of operations**
1. Baseline the candidate models ✅
2. Try cheap fixes: a prompt with one worked example (`v2-oneshot`) and refusal normalization
3. Grow the held-out test set to about 100 items with harder unanswerable and partially answerable cases, saving the top 20 passages per question
4. Generate a 300-example pilot training set with a frontier model
5. Fine-tune Qwen3.5-0.8B (QLoRA, RTX 4070) and compare
6. Retry loop: if the model refuses, retry with passages ranked 6–10, then with a new search (at most 2 retries, controlled in code). Evaluated offline on the saved top-20 passages.
7. Scale to 1,000+ examples only if the pilot clearly helps. A later round may teach a `NEED_MORE: <what's missing>` reply.
8. Quantization and pruning plus healing

**How to read the metrics** (definitions also in each `summary.md`)
- **Behaviour acc**: answered the answerable questions and refused the unanswerable ones.
- **Exact refusal**: on unanswerable items, replied exactly "The sources do not contain the answer."
- **Has citations / Sentence coverage**: share of answers with any [n], and share of sentences with one.
- **Groundedness**: share of an answer's content words found in the passages it cites. This is a rough proxy that rewards copying and penalises paraphrase.
- **Peak RAM**: peak resident memory of the `llama-server` process.

---

## 2026-11-24 20:58 — Setup: models, inference engine, test set

- Downloaded 5 candidate models (Q4_K_M GGUF) into `models/<name>/`, registered in `models/models.json`:
  - Qwen3.5-0.8B (0.53 GB)
  - Granite-4.0-H-1B (0.90 GB)
  - Qwen3.5-2B (1.28 GB)
  - Qwen3-4B-Instruct-2507 (2.50 GB)
  - Gemma 3 4B-it (2.49 GB)
- Inference uses the llama.cpp `llama-server` binary (build b12314) instead of `llama-cpp-python`, because Qwen3.5 and Granite-H are newer architectures.
- Built a frozen test set, `eval/data/baseline_test.jsonl`, from live search, top 5 passages per question.
  - 27 items: 22 answerable and 5 unanswerable. The unanswerable ones pair a question with an unrelated question's passages.
  - 2 of 24 questions were dropped because the search returned nothing.
- Shared prompt in `prompts.py`. Each model gets the same text, wrapped in its own chat template.
- GPU: the RTX 4070 was not visible because its Windows display driver was broken. Fixed by reinstalling the driver; `nvidia-smi` in WSL now shows the RTX 4070 Laptop with 8 GB.
- Measurement fix: `llama-server` keeps up to 8 GiB of prompt cache in RAM by default, which inflated peak RAM. All runs from here use `--cache-ram 0`.

## 2026-11-24 22:12 — Single-question smoke benchmark (`results/single-question/`)

All 5 models on q003, "What is the difference between weather and climate?" All answered correctly.

| Model | Peak RAM | Cites | Gen tok/s | Time |
|---|---|---|---|---|
| Qwen3.5-0.8B | 0.9 GB | no | 43.1 | 4.9 s |
| Granite-4.0-H-1B | 1.8 GB | yes | 23.8 | 13.2 s |
| Qwen3.5-2B | 2.0 GB | yes | 19.7 | 13.9 s |
| Qwen3-4B-2507 | 4.8 GB | yes | 9.5 | 39.1 s |
| Gemma 3 4B | 4.4 GB | yes | 11.7 | 26.4 s |

- Added the rendered prompt for every item (`prompts.md` per model). The content is identical across models; only the chat-template wrapper differs. Gemma has no system role, and Qwen3.5 gets an empty `<think></think>`.

## 2026-11-24 23:36 — Mini benchmark, 5 questions, with Claude Opus 5.5 as reference (`results/mini/`)

Test set `eval/data/mini_test.jsonl`: q003 plus 3 new answerable questions plus 1 unanswerable (m004, Reykjavik population asked against regenerative-braking passages). Opus 5.5 answers were pasted from claude.ai (`frontier/responses/claude-opus-5_5/`).

| Model | Peak RAM | Behaviour | Exact refusal | Has citations | Coverage | Groundedness | Words | Latency |
|---|---|---|---|---|---|---|---|---|
| Claude Opus 5.5 | – | 100% | 100% | 100% | 100% | 86% | 132 | – |
| Gemma 3 4B | 4.5 GB | 100% | 100% | 100% | 100% | 74% | 72 | 27.3 s |
| Qwen3-4B-2507 | 4.8 GB | 100% | 100% | 100% | 95% | 66% | 106 | 32.4 s |
| Qwen3.5-2B | 2.0 GB | 100% | 0% | 100% | 100% | 64% | 79 | 12.1 s |
| Granite-4.0-H-1B | 1.8 GB | 100% | 0% | 75% | 75% | 90% | 43 | 10.1 s |
| Qwen3.5-0.8B | 0.9 GB | 100% | 0% | 0% | 0% | 77% | 60 | 5.3 s |

- Opus 5.5 is the reference: it cites every sentence and refuses with the exact text. It is the most verbose at 132 words. Its lower groundedness on m001 came from linking and paraphrase words, not outside facts (checked by hand).
- Five items can't separate the models on behaviour; everyone scored 100%.
- **Decision:** focus on **Qwen3.5-0.8B, Granite-4.0-H-1B and Qwen3-4B-2507**. Qwen3.5-2B and Gemma 3 4B are kept on disk but dropped from further runs.

## 2026-11-24 23:50 — Full baseline, 27 questions, 3 focus models (`results/baseline/`)

Prompt `v1`, no refusal normalization.

| Model | File | Peak RAM | Behaviour | Exact refusal | Has citations | Coverage | Groundedness | Words | Prompt tok/s | Gen tok/s | Latency |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Qwen3.5-0.8B | 0.53 GB | 0.94 GB | 100% | 0% | 9% | 8% | 85% | 54 | 350 | 44.5 | 4.9 s |
| Granite-4.0-H-1B | 0.90 GB | 1.85 GB | 100% | 20% | 32% | 27% | 90% | 45 | 155 | 28.0 | 9.7 s |
| Qwen3-4B-2507 | 2.50 GB | **4.78 GB** | 100% | 100% | 100% | 98% | 77% | 91 | 57 | 9.1 | 33.6 s |

Flagged answers (`review.md` per model):

| Model | Flagged | Problems |
|---|---|---|
| Qwen3.5-0.8B | 26 / 27 | no citations 20, refusal not exact 5, some sentences uncited 1 |
| Granite-4.0-H-1B | 22 / 27 | no citations 15, refusal not exact 4, some sentences uncited 2, low groundedness 1 |
| Qwen3-4B-2507 | 0 / 27 | – |

**Observations**
- **Every model gets the answer-or-refuse decision right.** The unanswerable items in this set are easy, because the passages are about a completely unrelated topic. Harder cases (related but insufficient passages) are needed to stress this.
- **Citations are the main gap for the small models.** Qwen3.5-0.8B cites in only 2 of 22 answers, Granite in 7 of 22. Granite's mini-set rate (75%) was luck from a small sample.
- **Qwen3-4B behaves correctly in every way, but misses the deployment target.** Peak RAM is 4.78 GB against the < 4 GB target, and each answer takes about 34 s on the CPU. It still needs checking whether mmap double-counts memory (rerun with `--no-mmap`).
- The small models' high groundedness (85–90%) partly comes from copying text verbatim.

**Tooling added in this entry**
- `eval/review.py`: a `review.md` per model listing only the flagged answers and why.
- `eval/rescore.py`: recompute metrics from saved answers without rerunning models.
- Exact-refusal metric.
- `--prompt` / `--normalize-refusal` options in `eval/run_eval.py`.
- `frontier/baseline/`: 27 single-question prompts plus 3 batch prompts of 9 for frontier models. The importer accepts either.

**Next:** step 2. Rerun the 3 models with prompt `v2-oneshot` and refusal normalization, then compare with this baseline.

## 2026-11-25 00:06 — Plan update: retry loop added

- Added step 6, a retry loop controlled in code: if the model refuses, retry with passages ranked 6–10, then with a new search using a reworded query, at most 2 retries.
- Step 3 (bigger test set) will save the **top 20 ranked passages** per question, so the loop can be tested offline and reproducibly. Models still see only the top 5 in normal runs.
- Step 3 will also add harder unanswerable items (on-topic passages without the answer) and partially answerable items, because the baseline refusal cases were too easy.
- A model-controlled `NEED_MORE` reply is deferred to a later dataset round.

## 2026-11-25 00:14 — Step 2: one-example prompt + refusal normalization (`results/prompt-v2-oneshot/`)

Same 27 questions and settings as the baseline. Prompt `v2-oneshot` adds one worked example (a tides question with cited sentences, plus an exact refusal) to the system prompt. `--normalize-refusal` replaces short, uncited, paraphrased refusals with the exact sentence.

| Model | Prompt | Behaviour | Exact refusal | Has citations | Coverage | Groundedness | Off-topic | Words | Latency | Flagged |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen3.5-0.8B | v1 (baseline) | 100% | 0% | 9% | 8% | 85% | 0 | 54 | 4.9 s | 26/27 |
| Qwen3.5-0.8B | v2-oneshot+norm | 96% | **100%** | **71%** | 69% | 81% | 0 | 56 | 4.9 s | **9/27** |
| Granite-4.0-H-1B | v1 (baseline) | 100% | 20% | 32% | 27% | 90% | 0 | 45 | 9.7 s | 22/27 |
| Granite-4.0-H-1B | v2-oneshot+norm | 96% | **100%** | 57% | 50% | 83% | **1** | 41 | 10.0 s | 15/27 |
| Qwen3-4B-2507 | v1 (baseline) | 100% | 100% | 100% | 98% | 77% | 0 | 91 | 33.6 s | 0/27 |
| Qwen3-4B-2507 | v2-oneshot+norm | 100% | 100% | 100% | 100% | 78% | 0 | 89 | 31.1 s | 1/27 |

**What changed**
- **Citations improved a lot:** 0.8B went from 9% to 71% of answers cited, and Granite from 32% to 57%. Granite's real figure is about 52%, because one cited answer is the copied example (see below).
- **Exact refusal reached 100% for all models.** Normalization rewrote 3 paraphrased refusals (0.8B: u002, u003; Granite: u002). The other exact refusals came from the example itself. Normalization did not touch any real answer.
- **Side effect 1: false refusals.** 0.8B refused q017 (coral reefs) and Granite refused q014 (onions), although both have good sources. The example seems to make small models quicker to refuse.
- **Side effect 2: copying the example.** On q017 (coral reefs), Granite answered with the **tides example text word for word**, with citations. The old metrics scored this as a valid cited answer.
- Qwen3-4B was essentially unchanged; it already followed the instructions. No extra latency for any model: about 190 extra prompt tokens, which is small next to the ~1,250-token sources.

**Metric fix:** added an **off-topic check**, which flags an answer that shares no key words with the question. It's now in `review.md` and the summary column "Off-topic". Rescored `baseline`, `prompt-v2-oneshot` and `mini`. After fixing acronym handling (e.g. "VPN"), the only off-topic answer in any run is Granite's copied example.

**Conclusions**
- **Keep refusal normalization.** It's safe and gets exact refusals to 100% for free.
- **The worked example is a mixed result for the small models:** many more citations, but they now refuse a little too readily and can copy the example. Fine-tuning should do better on all three: citations without an example in the prompt, no copying, and no extra refusals.
- **Baseline to beat with fine-tuning:** Qwen3.5-0.8B at v2-oneshot+norm (71% cited, 1 false refusal, 9/27 flagged).

**Next:** step 3, growing the test set to about 100 items (top 20 passages saved; harder unanswerable and partially answerable items).

## 2026-11-25 00:57 — Few-shot comparison: 0 / 3 / 5 examples, on the GPU (`results/fewshot-0/`, `fewshot-3/`, `fewshot-5/`)

**Switched inference to the GPU** at the user's request. Same llama.cpp version (b12314) in its CUDA 13.5 build (`tools/llama.cpp-cuda/`), with all layers offloaded (`--gpu` in `eval/run_eval.py`). VRAM is measured as the increase in `nvidia-smi` memory use over idle. The 27-question run takes about 4 min per prompt on the GPU, versus about 20 min on the CPU.

Prompt variants in `prompts.py`:
- `v1`: 0 examples
- `v3-3shot`: tides answer, bees answer, and a refusal on unrelated sources
- `v5-5shot`: the 3-shot set, plus a refusal on **on-topic** sources and a **partial** answer ("The sources do not say …")

Examples are labelled "never copy their content". All runs use `--normalize-refusal`.

| Model | Examples | Behaviour | Exact refusal | Has citations | Coverage | Groundedness | Off-topic | Words | Flagged |
|---|---|---|---|---|---|---|---|---|---|
| Qwen3.5-0.8B | 0 | 100% | 100% | 9% | 9% | 85% | 0 | 54 | 20/27 |
| Qwen3.5-0.8B | 3 | 100% | 100% | **86%** | 84% | 70% | 0 | 48 | 10/27 |
| Qwen3.5-0.8B | 5 | 93% | 100% | **95%** | 95% | 70% | 0 | 44 | 7/27 |
| Granite-4.0-H-1B | 0 | 100% | 100% | 41% | 33% | 94% | 0 | 47 | 16/27 |
| Granite-4.0-H-1B | 3 | **74%** | 80% | 50% | 42% | 88% | 0 | 71 | 19/27 |
| Granite-4.0-H-1B | 5 | 85% | 80% | 47% | 36% | 87% | 0 | 56 | 20/27 |
| Qwen3-4B-2507 | 0 | 100% | 100% | 100% | 98% | 78% | 0 | 91 | 1/27 |
| Qwen3-4B-2507 | 3 | 100% | 100% | 100% | 100% | 77% | 0 | 101 | 1/27 |
| Qwen3-4B-2507 | 5 | 100% | 100% | 100% | 100% | 79% | 0 | 98 | 0/27 |

**Cost of the examples** (`results/prompt-cost/`). The prompt cache is disabled here to measure the full first-question cost. The `run_eval` timings above hide most of it because llama.cpp reuses the identical start of the prompt between questions.

| Model | Prompt tokens (0 → 3 → 5 examples) | GPU prefill (0 → 3 → 5) | CPU prefill (0 → 3 → 5) | CPU extra time (3 / 5) |
|---|---|---|---|---|
| Qwen3.5-0.8B | 1,328 → 1,806 → 2,037 (+36% / +53%) | 149 → 145 → 159 ms | 4.1 → 5.4 → 6.3 s | +1.3 s / +2.2 s |
| Granite-4.0-H-1B | 1,306 → 1,765 → 1,982 | 290 → 318 → 347 ms | 8.6 → 11.4 → 13.3 s | +2.8 s / +4.7 s |
| Qwen3-4B-2507 | 1,319 → 1,780 → 2,001 | 340 → 440 → 492 ms | 21.9 → 31.2 → 35.8 s | +9.3 s / +13.9 s |

- **RAM / VRAM: no increase** from 0 to 5 examples for any model (0.8B: 0.93 GB RAM / 0.76 GB VRAM; Granite 1.23 / 1.18 GB; Qwen3-4B 2.77 / 3.19 GB on the GPU; the CPU figures in earlier entries). llama.cpp allocates the KV cache for the full 4,096-token context up front, so a longer prompt costs nothing extra while it fits.
- On the CPU (the deployment target), prefill grows roughly in proportion to prompt length: **+33% (3-shot) and +54% (5-shot) time to first token.** The CPU prefill was measured while dataset retrieval was running, so it is slightly pessimistic.
- On the GPU, prefill grows by 0–150 ms, which is negligible.

**Observations**
- **Qwen3.5-0.8B benefits most:** citations rise from 9% to 86% to 95%, and flagged answers fall from 20 to 10 to 7. The 5-example prompt also causes 2 false refusals (q006 batteries, q017 coral reefs).
- **Granite gets worse with more examples.** It falsely refuses 6 answerable questions with 3 examples (3 with 5), and on u003 it **answered from its own knowledge: "The Eiffel Tower was completed in 1889 [1]"**, with a fake citation to inflation sources. That is exactly the failure fine-tuning must remove.
- **Qwen3-4B doesn't need examples.** It is unchanged.
- **Metric fix:** cited answers that note a gap ("The sources do not say X") are now treated as partial answers, not refusals. All runs were rescored.

**Conclusion:** few-shot is a strong free fix for Qwen3.5-0.8B (the 5-example prompt gives the best citations). But it adds +2.2 s per question on the CPU and causes some false refusals. Fine-tuning can bake the behaviour in with the 0-example prompt, avoiding that time cost.

## 2026-11-25 01:16 — Step 3: new test set `test_v2` (114 items) and dataset generation in progress

**Dataset pipeline** (`datagen/`, all generation by Opus 5.5 agents):
1. `seed_questions.jsonl`: 480 questions, 20 in each of 24 domains, written by an agent. Test-set topics are excluded.
2. `retrieve.py`: the real pipeline (search, extract, BM25), saving the **top 20 passages** per question to `datagen/raw/`. 317 of 480 retrieved so far.
3. `make_label_batches.py`: splits by topic, stratified by domain:
   - test: 1 topic per domain (24 topics)
   - val: 1 topic per domain (24 topics)
   - train: the rest
   
   It writes batch files of 20 topics, or 6 for test topics, which also show sources 6–20.
4. Labelling agents follow `datagen/SPEC.md`. Per topic they write:
   - **seed**: the original question, labelled answerable, partial or unanswerable from sources 1–5
   - **gen**: a new, fully answerable question
   - **hard_neg**: an on-topic question the sources don't answer
   - **partial**: on every 3rd topic, a two-part question with only one part covered
   
   Test topics also record whether sources 6–20 contain the missing answer, for the retry loop.
5. `build_dataset.py` validates every item:
   - citations within 1–5
   - every sentence cited
   - 90 words or fewer, at most 5 sentences
   - exact refusal wording
   - groundedness 40% or higher
   - shares key words with the question
   - not a duplicate or a reserved test question
   
   It adds about 10% scripted **off-topic** unanswerable items (a question paired with another domain's passages), then writes `data/train.jsonl`, `data/val.jsonl` and `eval/data/test_v2.jsonl`.

So far: 12 of 27 batches labelled (all 4 test batches), with **3 rejections out of about 600 items**. A hand spot-check confirmed the answers are grounded and the hard_negs truly unanswerable. Spec clarifications from the pilot: thin coverage, mere mentions, abbreviations. The sentence splitter now handles initials such as "Robert T. Paine".

**`eval/data/test_v2.jsonl` — frozen** (md5 `4b53694843e230d8606746bbc24818be`; `build_dataset.py` no longer rewrites it without `--rebuild-test`):

| Type | Items | Label |
|---|---|---|
| seed | 24 | 22 answerable, 2 partial |
| gen | 24 | answerable |
| partial | 7 | partial |
| hard_neg | 24 | unanswerable (all 24 have the answer in sources 6–20) |
| offtopic_neg | 8 | unanswerable |
| baseline (old set) | 27 | 22 answerable, 5 unanswerable |

**Results on test_v2, on the GPU, with `--normalize-refusal`** (`results/test-v2-0shot/`, `results/test-v2-5shot/`). The type columns show correct answer-or-refuse decisions.

| Model | Examples | Behaviour | Cites | Coverage | Groundedness | Off-topic | seed | gen | partial | **hard_neg** | offtopic | baseline |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Qwen3.5-0.8B | 0 | 94% | 12% | 10% | 82% | 1 | 24/24 | 24/24 | 7/7 | **17/24** | 8/8 | 27/27 |
| Qwen3.5-0.8B | 5 | 76% | 92% | 90% | 68% | 0 | 20/24 | **7/24** | 4/7 | 23/24 | 8/8 | 25/27 |
| Granite-4.0-H-1B | 0 | 86% | 51% | 47% | 74% | **11** | 24/24 | 22/24 | 6/7 | **11/24** | 8/8 | 27/27 |
| Granite-4.0-H-1B | 5 | 79% | 43% | 37% | 79% | 2 | 23/24 | 19/24 | 6/7 | 11/24 | 8/8 | 23/27 |
| Qwen3-4B-2507 | 0 | 99% | 100% | 93% | 74% | 0 | 24/24 | 24/24 | 7/7 | 23/24 | 8/8 | 27/27 |
| Qwen3-4B-2507 | 5 | 98% | 100% | 96% | 77% | 0 | 23/24 | 24/24 | 7/7 | 23/24 | 8/8 | 27/27 |

**Observations**
- **The hard negatives separate the models.** The old test set's unanswerable items (unrelated sources) are solved by everyone. With on-topic sources lacking the answer, Qwen3.5-0.8B answers anyway 7 of 24 times and Granite 13 of 24 times.
- **The 5-example prompt makes the 0.8B over-refuse.** It now refuses 17 of 24 answerable `gen` questions. It trades answering for citing and refusing, so few-shot is not a usable fix on the harder set.
- **New Granite failure: citation-only replies** (e.g. the whole answer is `[4]`). That's 11 of 114 with 0 examples. The off-topic check catches them.
- **Qwen3-4B is near-perfect on behaviour** (1 missed hard_neg), but is still at 4.8 GB RAM on the CPU and about 34 s per answer.
- test_v2 is now the main benchmark for fine-tuning: hard_neg accuracy, citation rate and gen accuracy are the key numbers.

**Next:** finish retrieval and labelling of the 16 remaining train/val batches, build the final `train.jsonl` / `val.jsonl`, then fine-tune Qwen3.5-0.8B (step 5).
