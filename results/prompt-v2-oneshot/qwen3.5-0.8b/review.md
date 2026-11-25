# Review: qwen3.5-0.8b (prompt-v2-oneshot)

9 of 27 answers flagged. Full prompts are in `prompts.md`, raw data in `answers.jsonl`.

| Problem | Count |
|---|---|
| no citations | 6 |
| some sentences uncited | 1 |
| wrong answer/refuse decision | 1 |
| low groundedness | 1 |

---

## q012: How do noise-cancelling headphones work?

Answerable: True

Problems:
- no citations

Answer:

````text
Noise-cancelling headphones rely on two technologies working together: passive isolation and active noise cancellation. Passive isolation comes from the headphone's physical design, including ear cups, padding, and a secure fit that helps block outside sound. Active noise cancellation adds an electronic layer, using microphones to detect ambient noise and digital processing to generate an opposing signal that reduces what you hear. Together, these technologies make noise cancelling headphones especially effective at lowering steady background noise while creating a quieter, more focused listening experience.
````

---

## q000: What causes sleep apnea?

Answerable: True

Problems:
- no citations

Answer:

````text
Sleep apnea is caused by a combination of physical and medical factors that interfere with normal breathing during sleep, including conditions that block airflow or affect the brain's control of breathing.
````

---

## q009: What causes the seasons on Earth?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
The sources indicate that seasons on Earth are primarily caused by the Earth's axial tilt relative to its orbit around the Sun, rather than its distance from the Sun. This tilt causes different hemispheres to receive varying amounts of sunlight at different times of the year, creating the distinct weather patterns known as seasons [1][2].
````

---

## q004: How does a heat pump work?

Answerable: True

Problems:
- no citations

Answer:

````text
Heat pumps work by transferring heat from one place to another using electricity and a refrigerant, rather than generating heat through combustion. In heating mode, they pull heat from the outdoor air and bring it inside, while in cooling mode, they reverse the process to move heat out of the home. This process allows them to achieve efficiency ratings of 300% to 500% compared to traditional furnaces that generate heat directly.
````

---

## q002: Why is the sky blue?

Answerable: True

Problems:
- no citations

Answer:

````text
The sources indicate that the sky is blue due to the scattering of sunlight by air molecules, where shorter wavelengths (blue/violet) are scattered more than longer wavelengths (red), and that Earth's atmosphere reflects this scattered light.
````

---

## q006: How do lithium-ion batteries degrade over time?

Answerable: True

Problems:
- no citations

Answer:

````text
The sources indicate that lithium-ion batteries degrade primarily through chemical and mechanical processes, including the growth of solid electrolyte interphase (SEI), lithium plating, cathode dissolution, and mechanical stress from expansion and contraction. These mechanisms are accelerated by high voltage, high temperature, and high charge/discharge rates. Additionally, the sources note that while lithium-ion batteries are inherently prone to degradation, they are not unalterable and can be mitigated through proper operation and maintenance.
````

---

## q017: How do coral reefs form?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## q001: How do vaccines train the immune system?

Answerable: True

Problems:
- low groundedness 36% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Vaccines train the immune system by providing a safe antigen that induces strong immune responses without causing disease, allowing the body to recognize and fight pathogens more effectively than natural infection [2].
````

---

## q014: Why do onions make people cry?

Answerable: True

Problems:
- no citations

Answer:

````text
The sources indicate that onions cause people to cry due to the formation of a sulfur-containing chemical called lachrymatory factor when cut or damaged, which travels through the air and irritates the eyes. This chemical reaction is triggered by the damage to onion cells, which releases volatile compounds that react with water to create the irritant.
````
