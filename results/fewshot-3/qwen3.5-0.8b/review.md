# Review: qwen3.5-0.8b (fewshot-3)

10 of 27 answers flagged. Full prompts are in `prompts.md`, raw data in `answers.jsonl`.

| Problem | Count |
|---|---|
| low groundedness | 8 |
| no citations | 3 |
| some sentences uncited | 1 |

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

## q005: What are the main symptoms of type 2 diabetes?

Answerable: True

Problems:
- low groundedness 55% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The sources provide a detailed breakdown of symptoms, including increased thirst, hunger, fatigue, and frequent urination, as well as specific warning signs like blurry vision and tingling in the hands or feet [1][2][3][4].
````

---

## q000: What causes sleep apnea?

Answerable: True

Problems:
- low groundedness 60% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Sleep apnea is caused by conditions that block airflow through the upper airway during sleep, such as obesity, a stuffy nose, or anomalies in the shape of your face and neck [1]. Central sleep apnea occurs when the brain fails to signal the muscles that control breathing, often as a result of medical conditions that affect the brain and heart [1].
````

---

## q009: What causes the seasons on Earth?

Answerable: True

Problems:
- low groundedness 58% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The sources explicitly state that Earth's axial tilt, not its distance from the Sun, is what drives the seasons [1][2]. This tilt causes different hemispheres to receive varying amounts of sunlight at different times of the year, creating the distinct weather patterns known as seasons [1][2].
````

---

## q023: How does a refrigerator keep food cold?

Answerable: True

Problems:
- low groundedness 59% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Refrigerators work primarily on the principles of thermodynamics, specifically the refrigeration cycle, where a refrigerant absorbs heat from the interior and releases it to the outside [5]. This continuous process removes heat from the insulated interior, which is essential for slowing down microbial growth and chemical reactions that would otherwise cause spoilage [3].
````

---

## q020: What is the greenhouse effect?

Answerable: True

Problems:
- no citations
- low groundedness 44% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The sources provide definitions and mechanisms for the greenhouse effect, including its role in trapping heat from the sun and maintaining Earth's temperature, as well as specific examples like the greenhouse effect diagram and NASA explanations. However, the provided text does not contain a direct definition or explanation of the specific mechanism of the greenhouse effect itself.
````

---

## q006: How do lithium-ion batteries degrade over time?

Answerable: True

Problems:
- no citations

Answer:

````text
The sources detail that lithium-ion batteries degrade due to internal phenomena such as electrolyte reactions, electrode material changes, and side reactions, which reduce performance and capacity. While the text mentions that these processes are unavoidable and accelerate with improper usage, it does not provide specific details on the exact mechanisms or specific chemical reactions that cause the degradation.
````

---

## q017: How do coral reefs form?

Answerable: True

Problems:
- only 50% of sentences cited
- low groundedness 49% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The sources provide a detailed explanation of how coral reefs form, detailing the process of free-swimming larvae attaching to rocks and the development of three major structural shapes like fringing, barrier, and atolls [5]. However, the provided text does not contain information regarding the specific mechanisms of how coral polyps build their structures or the biological processes involved in their formation.
````

---

## q010: How does photosynthesis convert light into energy?

Answerable: True

Problems:
- low groundedness 59% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Photosynthesis converts light energy into chemical energy by using light-dependent reactions to split water molecules and generate ATP and NADPH, which then drive the light-independent reactions to fix carbon dioxide into sugars [2].
````

---

## q014: Why do onions make people cry?

Answerable: True

Problems:
- low groundedness 44% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The sources indicate that onions cause crying due to the formation of a sulfur-containing chemical called lachrymatory factor when cut or damaged, which irritates the eyes and triggers tear production [1][3]. To prevent this, one should use a sharp knife to avoid crushing the onion, chill it in ice water before cutting, and avoid cutting near the root end where sulfuric compounds are highest concentrated [3].
````
