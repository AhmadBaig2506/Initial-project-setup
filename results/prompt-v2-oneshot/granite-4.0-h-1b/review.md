# Review: granite-4.0-h-1b (prompt-v2-oneshot)

15 of 27 answers flagged. Full prompts are in `prompts.md`, raw data in `answers.jsonl`.

| Problem | Count |
|---|---|
| no citations | 9 |
| some sentences uncited | 3 |
| low groundedness | 2 |
| off-topic answer | 1 |
| wrong answer/refuse decision | 1 |

---

## q016: What causes inflation in an economy?

Answerable: True

Problems:
- no citations

Answer:

````text
Inflation in an economy is caused by excess aggregate demand (economic growth too fast) or cost-push factors (supply-side factors such as higher oil prices, shipping costs, and food prices).
````

---

## q012: How do noise-cancelling headphones work?

Answerable: True

Problems:
- no citations

Answer:

````text
Noise-cancelling headphones work by using two technologies: passive isolation and active noise cancellation. Passive isolation comes from the headphone's physical design, including ear cups, padding, and a secure fit that helps block outside sound. Active noise cancellation adds an electronic layer, using microphones to detect ambient noise and digital processing to generate an opposing signal that reduces what you hear. Together, these technologies make noise-cancelling headphones especially effective at lowering steady background noise while creating a quieter, more focused listening experience.
````

---

## q019: How does caffeine affect the brain?

Answerable: True

Problems:
- low groundedness 42% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1] Caffeine affects the brain primarily by blocking adenosine, a chemical messenger that helps regulate sleepiness and alertness.
````

---

## q000: What causes sleep apnea?

Answerable: True

Problems:
- no citations

Answer:

````text
Sleep apnea is caused by conditions that block airflow through the upper airway during sleep, such as obesity, a stuffy nose, or anomalies in the shape of the face and neck.
````

---

## q009: What causes the seasons on Earth?

Answerable: True

Problems:
- no citations

Answer:

````text
The sources indicate that the seasons on Earth are caused by the Earth's axial tilt of approximately 23.5 degrees, which causes different parts of the planet to receive varying amounts of sunlight throughout the year.
````

---

## q020: What is the greenhouse effect?

Answerable: True

Problems:
- no citations

Answer:

````text
The greenhouse effect is a process in Earth's atmosphere where certain gases, such as carbon dioxide, methane, and water vapor, trap heat from the sun, keeping the planet's temperature within a range suitable for life.
````

---

## q004: How does a heat pump work?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
[1] A heat pump works by transferring heat from one place to another using electricity and refrigerant. It does not generate heat, but instead moves it from the outside to the inside of a building.
````

---

## q002: Why is the sky blue?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
The sky is blue because sunlight is scattered in all directions by the tiny molecules of air in Earth's atmosphere, and blue light is scattered more than other colors because it travels as shorter, smaller waves. This is why we see a blue sky most of the time [1].
````

---

## q006: How do lithium-ion batteries degrade over time?

Answerable: True

Problems:
- no citations

Answer:

````text
Lithium-ion batteries degrade over time due to a combination of chemical and mechanical processes, including solid electrolyte interphase (SEI) growth, lithium plating, cathode dissolution, and mechanical stress from expansion and contraction. The primary accelerants for degradation are high voltage, high temperature, and high charge/discharge rates.
````

---

## q022: What causes earthquakes?

Answerable: True

Problems:
- no citations

Answer:

````text
Earthquakes are caused by the release of built-up stress in the Earth's crust, usually along faults or at the boundaries of tectonic plates.
````

---

## q011: What is quantization in machine learning models?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
[1] Quantization Tutorial in TensorFlow for ML Models
In machine learning, deploying models on resource-constrained devices is becoming more important. Quantization is one of the key techniques used to optimize models for efficient deployment without sacrificing much accuracy.
````

---

## q017: How do coral reefs form?

Answerable: True

Problems:
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1] Ocean tides are caused mainly by the Moon's gravity pulling on Earth's oceans [1]. The Sun also contributes, and when the Sun and Moon line up, their combined pull creates larger spring tides [2].
````

---

## q010: How does photosynthesis convert light into energy?

Answerable: True

Problems:
- no citations

Answer:

````text
Photosynthesis converts light into energy through the light-dependent reactions, which capture light energy and use it to produce hydrogen carrier NADPH and ATP, and the light-independent reactions, which use these products to fix carbon dioxide into organic compounds.
````

---

## q001: How do vaccines train the immune system?

Answerable: True

Problems:
- no citations

Answer:

````text
Vaccines train the immune system by providing an antigen for a specific disease that the immune system responds to by producing antibodies.
````

---

## q014: Why do onions make people cry?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````
