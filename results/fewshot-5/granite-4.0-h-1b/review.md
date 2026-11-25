# Review: granite-4.0-h-1b (fewshot-5)

20 of 27 answers flagged. Full prompts are in `prompts.md`, raw data in `answers.jsonl`.

| Problem | Count |
|---|---|
| no citations | 10 |
| wrong answer/refuse decision | 4 |
| some sentences uncited | 4 |
| low groundedness | 3 |

---

## q003: What is the difference between weather and climate?

Answerable: True

Problems:
- low groundedness 50% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The difference between weather and climate is that weather refers to short-term changes in the atmosphere, while climate refers to atmospheric changes over longer periods of time, usually 30 years or more. [1]
````

---

## q016: What causes inflation in an economy?

Answerable: True

Problems:
- no citations

Answer:

````text
The main causes of inflation in an economy are excess aggregate demand (economic growth too fast) or cost-push factors (supply-side factors such as higher oil prices, shipping costs, and food prices).
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
- no citations

Answer:

````text
The sources state that caffeine affects the brain primarily by blocking adenosine, a chemical messenger that helps regulate sleepiness and alertness. By interfering with this process, caffeine can make people feel more awake, improve attention, and temporarily reduce the perception of fatigue.
````

---

## q005: What are the main symptoms of type 2 diabetes?

Answerable: True

Problems:
- no citations

Answer:

````text
The main symptoms of type 2 diabetes include increased thirst, feeling tired, weight loss, frequent urination, blurred vision, and frequent infections.
````

---

## q000: What causes sleep apnea?

Answerable: True

Problems:
- no citations

Answer:

````text
The causes of sleep apnea depend on the type of sleep apnea. Obstructive sleep apnea (OSA) is caused by conditions that block airflow through the upper airway, such as obesity, a stuffy nose, or anomalies in the shape of the face and neck. Central sleep apnea occurs when the brain fails to send the right signals to control breathing, often as a result of medical conditions that affect the brain and heart.
````

---

## q009: What causes the seasons on Earth?

Answerable: True

Problems:
- no citations

Answer:

````text
The sources indicate that the seasons on Earth are caused by the Earth's axial tilt of approximately 23.5 degrees relative to the plane of its orbit around the Sun. This tilt causes different parts of the Earth to receive varying amounts of sunlight at different times of the year, leading to the seasonal changes we observe.
````

---

## q023: How does a refrigerator keep food cold?

Answerable: True

Problems:
- no citations

Answer:

````text
The basic principle behind how refrigerators keep food cold is the refrigeration cycle, which involves the evaporation and condensation of a refrigerant.
````

---

## q021: How do solar panels generate electricity?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## q020: What is the greenhouse effect?

Answerable: True

Problems:
- no citations

Answer:

````text
The greenhouse effect is a process in Earth's atmosphere where certain gases, known as greenhouse gases, trap heat from the sun and keep the planet's temperature within a range suitable for life. This effect is important for maintaining the balance of the Earth's climate. However, human activities such as burning fossil fuels have caused an increase in the concentration of greenhouse gases, leading to global warming.
````

---

## q004: How does a heat pump work?

Answerable: True

Problems:
- only 67% of sentences cited

Answer:

````text
[1] The sources explain that a heat pump works by transferring heat from one place to another using electricity and refrigerant. In heating mode, it pulls heat from the outdoor air and brings it indoors. In cooling mode, it reverses the process and moves heat out of the home. [2] The sources also describe how a heat pump works, stating that it moves heat from one place to another using electricity and refrigerant, without generating heat itself.
````

---

## q002: Why is the sky blue?

Answerable: True

Problems:
- only 25% of sentences cited

Answer:

````text
The sky is blue because sunlight contains all the colors of the rainbow, but the sky appears blue due to a phenomenon called Rayleigh scattering. When sunlight enters Earth's atmosphere, it is scattered in all directions by the tiny molecules of air. Blue light is scattered more than other colors because it travels as shorter, smaller waves. This is why we see a blue sky most of the time. [1]
````

---

## q006: How do lithium-ion batteries degrade over time?

Answerable: True

Problems:
- no citations

Answer:

````text
Lithium-ion batteries degrade over time due to a combination of chemical and mechanical processes, including solid electrolyte interphase (SEI) growth, lithium plating, cathode dissolution, and mechanical stress from expansion and contraction. The primary accelerants for degradation are high voltage (charging to 100%), high temperature, and high charge/discharge rates. Keeping a battery between 20% and 80% charge and below 30°C can help extend its useful lifespan.
````

---

## q022: What causes earthquakes?

Answerable: True

Problems:
- low groundedness 48% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1] The sources state that earthquakes are caused by the release of built-up stress in the Earth's crust, usually along faults or at the boundaries of tectonic plates. [2] They also mention that earthquakes can be induced by various causes, including impoundment of reservoirs, surface and underground mining, withdrawal of fluids and gas from the subsurface, and injection of fluids into underground formations.
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
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

Raw answer before refusal normalization:

````text
The sources do not contain the answer to the question "How do coral reefs form?".
````

---

## q001: How do vaccines train the immune system?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
[1] How Vaccines Work - Immunology Explained
Vaccines train the immune system to respond to pathogens without the dangerous side-effects of the disease. They do this by providing an antigen for a specific disease that the immune system responds to by producing antibodies.
````

---

## q015: How does the BM25 ranking function score documents?

Answerable: True

Problems:
- no citations

Answer:

````text
The BM25 ranking function scores documents by calculating a numerical score based on the occurrences and importance of query terms within the document. It balances simplicity and effectiveness, making it a popular choice in modern search engines and applications.
````

---

## u003: What year was the Eiffel Tower completed?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The Eiffel Tower was completed in 1889 [1].
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
