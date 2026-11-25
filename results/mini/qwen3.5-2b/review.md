# Review: qwen3.5-2b (mini)

3 of 5 answers flagged. Full prompts are in `prompts.md`, raw data in `answers.jsonl`.

| Problem | Count |
|---|---|
| low groundedness | 2 |
| refusal not exact | 1 |

---

## m001: What is the difference between a virus and a bacterium?

Answerable: True

Problems:
- low groundedness 46% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Viruses are non-cellular particles that cannot reproduce without a host, whereas bacteria are complete living cells capable of independent growth and division [2]. Bacteria are typically larger, ranging from 0.5 to 5 μm in size, while viruses are much smaller, measuring between 0.02 and 0.2 μm [1]. Antibiotics are effective against bacteria but do not treat viral infections because they target structures bacteria possess that viruses lack [5]. Additionally, bacteria are prokaryotes containing both DNA and RNA, while viruses contain either DNA or RNA but never both [3].
````

---

## m002: How does regenerative braking work in electric cars?

Answerable: True

Problems:
- low groundedness 53% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Regenerative braking works by converting the kinetic energy lost during deceleration into electrical energy, which is then stored in the vehicle's battery [2]. This process utilizes the motor's dual-rotation design, allowing it to act as a generator when the car slows down [2]. The generated electricity is typically displayed on the dashboard speedometer, showing the power produced by the system [4].
````

---

## m004: What is the population of Reykjavik?

Answerable: False

Problems:
- refusal not worded exactly as instructed

Answer:

````text
The provided sources do not contain the answer to the question about the population of Reykjavik.
````
