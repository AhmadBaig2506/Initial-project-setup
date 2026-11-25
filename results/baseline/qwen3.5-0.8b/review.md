# Review: qwen3.5-0.8b (baseline)

26 of 27 answers flagged. Full prompts are in `prompts.md`, raw data in `answers.jsonl`.

| Problem | Count |
|---|---|
| no citations | 20 |
| refusal not exact | 5 |
| some sentences uncited | 1 |

---

## q003: What is the difference between weather and climate?

Answerable: True

Problems:
- no citations

Answer:

````text
According to the sources, weather refers to short-term changes in the atmosphere, while climate refers to atmospheric changes over longer periods of time, typically defined as 30 years or more.
````

---

## q016: What causes inflation in an economy?

Answerable: True

Problems:
- no citations

Answer:

````text
Inflation is the sustained rise in the general level of prices of goods and services, primarily driven by demand-pull inflation when growing demand outstrips supply, and cost-push inflation when production or input costs rise significantly.
````

---

## q012: How do noise-cancelling headphones work?

Answerable: True

Problems:
- no citations

Answer:

````text
Noise-cancelling headphones function by utilizing two complementary technologies: passive isolation, which provides a physical barrier to block external sound waves, and active noise cancellation, which employs microphones and digital processing to detect ambient noise and generate an opposing signal to cancel it out.
````

---

## q019: How does caffeine affect the brain?

Answerable: True

Problems:
- only 75% of sentences cited

Answer:

````text
Caffeine primarily works by blocking adenosine receptors, which are natural sleep-promoting signals that reduce neural activity and fatigue [3]. While this mechanism can temporarily enhance alertness and concentration, it does not universally improve all aspects of cognitive performance, such as memory or complex reasoning [1]. Furthermore, habitual use can lead to tolerance and sleep disruption, potentially undermining long-term cognitive function [5]. Therefore, the effects of caffeine depend on individual factors like dosage, timing, and sleep habits.
````

---

## q005: What are the main symptoms of type 2 diabetes?

Answerable: True

Problems:
- no citations

Answer:

````text
Type 2 diabetes is characterized by a lack of insulin production or a failure to respond to it, leading to elevated blood glucose levels. The primary symptoms include increased thirst, frequent urination, fatigue, and weight loss. These symptoms often develop gradually, typically starting in adults over 45, though they can also appear in younger individuals.
````

---

## q000: What causes sleep apnea?

Answerable: True

Problems:
- no citations

Answer:

````text
Sleep apnea is caused by conditions that block airflow through the upper airway during sleep, such as obesity, a stuffy nose, or anatomical anomalies in the face and neck. Central sleep apnea occurs when the brain fails to send the right signals to control breathing, often due to medical conditions affecting the brain and heart. While both types stem from physical or medical factors, the specific cause depends on the type of sleep apnea and the underlying condition.
````

---

## q009: What causes the seasons on Earth?

Answerable: True

Problems:
- no citations

Answer:

````text
The seasons on Earth are primarily caused by the planet's axial tilt, which is approximately 23.5 degrees relative to its orbital plane. This tilt causes different hemispheres to receive varying amounts of sunlight throughout the year, resulting in the distinct weather patterns known as seasons.
````

---

## q023: How does a refrigerator keep food cold?

Answerable: True

Problems:
- no citations

Answer:

````text
A refrigerator keeps food cold by continuously transferring heat from its insulated interior to the surrounding room through a repeating refrigeration cycle. This process relies on a circulating refrigerant that absorbs heat inside the appliance and releases it outside via coils, a compressor, and an expansion device. By removing heat from the food, the system slows down microbial growth and chemical reactions, ensuring the food remains safe and fresh.
````

---

## q021: How do solar panels generate electricity?

Answerable: True

Problems:
- no citations

Answer:

````text
Solar panels generate electricity through the photovoltaic effect, where sunlight excites electrons in silicon cells to create direct current (DC) power. This DC electricity is then converted into alternating current (AC) by an inverter, enabling homes and businesses to use the generated energy.
````

---

## q020: What is the greenhouse effect?

Answerable: True

Problems:
- no citations

Answer:

````text
The greenhouse effect is the process through which heat is trapped near Earth's surface by substances known as 'greenhouse gases,' helping to maintain a warmer temperature than it would otherwise. This phenomenon occurs when certain gases absorb infrared radiation from the sun, causing the Earth's surface to warm up, which is essential for life on the planet.
````

---

## u002: How many moons does Neptune have?

Answerable: False

Problems:
- refusal not worded exactly as instructed

Answer:

````text
The sources provided do not contain information regarding the number of moons Neptune has.
````

---

## u004: What is the capital city of Mongolia?

Answerable: False

Problems:
- refusal not worded exactly as instructed

Answer:

````text
The provided sources do not contain information regarding the capital city of Mongolia.
````

---

## q004: How does a heat pump work?

Answerable: True

Problems:
- no citations

Answer:

````text
Heat pumps transfer heat from one place to another using electricity and a refrigerant cycle, operating by reversing the direction of the refrigerant flow to move heat between indoor and outdoor air sources. Unlike traditional furnaces that generate heat through combustion, heat pumps do not produce thermal energy themselves but move it, making them highly efficient and suitable for both heating and cooling.
````

---

## u000: Who won the 1998 FIFA World Cup?

Answerable: False

Problems:
- refusal not worded exactly as instructed

Answer:

````text
The sources provided do not contain information regarding the winner of the 1998 FIFA World Cup.
````

---

## q006: How do lithium-ion batteries degrade over time?

Answerable: True

Problems:
- no citations

Answer:

````text
Lithium-ion batteries degrade primarily through a combination of chemical and mechanical processes, including the growth of solid electrolyte interphase (SEI), lithium plating, cathode dissolution, and physical stress from expansion and contraction. These mechanisms occur continuously whether the battery is used or not, and they accelerate significantly under conditions such as high voltage, high temperature, and rapid charge/discharge rates.
````

---

## q013: What are the health benefits of regular walking?

Answerable: True

Problems:
- no citations

Answer:

````text
Walking offers multiple significant health benefits, including the reduction of chronic disease, improved cognitive function, and enhanced heart health. It also supports healthy aging by promoting bone health, reducing the risk of falls, and improving overall well-being through regular physical activity.
````

---

## q022: What causes earthquakes?

Answerable: True

Problems:
- no citations

Answer:

````text
Earthquakes are caused by the sudden release of built-up stress in the Earth's crust, typically along faults or at the boundaries of tectonic plates. This stress release sends seismic waves radiating from the point of rupture, traveling through the Earth and shaking the ground.
````

---

## q011: What is quantization in machine learning models?

Answerable: True

Problems:
- no citations

Answer:

````text
Quantization is a data compression technique that reduces the precision of machine learning models by converting floating-point data to lower-precision formats like integers, thereby optimizing inference speed, reducing computational demands, and improving energy efficiency on resource-constrained devices.
````

---

## u005: Who wrote the novel Pride and Prejudice?

Answerable: False

Problems:
- refusal not worded exactly as instructed

Answer:

````text
The provided sources do not contain information regarding the author of the novel *Pride and Prejudice*.
````

---

## q017: How do coral reefs form?

Answerable: True

Problems:
- no citations

Answer:

````text
Coral reefs form from the growth of hard, stony coral larvae that attach to submerged rocks or hard surfaces along the edges of islands or continents. As these corals grow and expand, they develop into three major characteristic structures: fringing reefs, barrier reefs, or atolls. Fringing reefs project seaward directly from the shore, while barrier reefs border shorelines at a greater distance and are separated by lagoons.
````

---

## q018: What is the purpose of a VPN?

Answerable: True

Problems:
- no citations

Answer:

````text
A VPN serves as a security tool that encrypts your internet connection and hides your IP address, making it significantly harder for your ISP, advertisers, or hackers to track what you do online. By routing your traffic through a private server in a location of your choice, the server masks your real IP address and wraps your data in encryption, ensuring that even if someone intercepts your connection, they cannot read it.
````

---

## q010: How does photosynthesis convert light into energy?

Answerable: True

Problems:
- no citations

Answer:

````text
Photosynthesis converts light energy into chemical energy by utilizing chlorophyll pigments to capture photons and drive the splitting of water molecules, which releases oxygen and generates chemical fuel. This process occurs in two distinct stages: the light-dependent reactions capture energy to produce ATP and NADPH, while the light-independent reactions use these products to fix carbon dioxide into sugars.
````

---

## q001: How do vaccines train the immune system?

Answerable: True

Problems:
- no citations

Answer:

````text
Vaccines train the immune system by providing a specific antigen that triggers the production of antibodies and the activation of memory cells, allowing the body to recognize and respond to pathogens without the dangerous side effects of the disease itself.
````

---

## q015: How does the BM25 ranking function score documents?

Answerable: True

Problems:
- no citations

Answer:

````text
The BM25 ranking function scores documents by calculating a numerical score based on the occurrences of query terms within the document, where each term's contribution is scaled by its inverse document frequency (IDF) and normalized by the document's length. This process involves multiplying the frequency of a term by its rarity factor and adding the results for all terms in the query.
````

---

## u003: What year was the Eiffel Tower completed?

Answerable: False

Problems:
- refusal not worded exactly as instructed

Answer:

````text
The provided sources do not contain information regarding the completion year of the Eiffel Tower.
````

---

## q014: Why do onions make people cry?

Answerable: True

Problems:
- no citations

Answer:

````text
Onions make people cry due to the formation of a volatile chemical compound called lachrymatory factor, which is released when the onion's cells are damaged during cutting. This irritant travels through the air and triggers the eyes to produce tears. To prevent this, one should use a sharp knife to avoid crushing the onion, chill the onion in a bowl of ice water before cutting, and avoid cutting near the root end where the sulfuric compounds are highest concentrated.
````
