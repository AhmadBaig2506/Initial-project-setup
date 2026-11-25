# Review: qwen3.5-0.8b (test-v2-5shot)

47 of 114 answers flagged. Full prompts are in `prompts.md`, raw data in `answers.jsonl`.

| Problem | Count |
|---|---|
| wrong answer/refuse decision | 27 |
| low groundedness | 16 |
| no citations | 4 |
| some sentences uncited | 3 |

---

## s0004-gen: What warning signs might appear a day or two before a migraine?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0004-seed: What causes migraines and how are they treated?

Answerable: True

Problems:
- low groundedness 29% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Migraines are caused by imbalances in brain chemicals, specifically a drop in serotonin and a malfunctioning trigeminal nerve that transmits pain signals [3]. They are treated with various medications and lifestyle changes to manage symptoms and prevent recurrence [3].
````

---

## s0039-gen: When was REM sleep first discovered and how did it get its name?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0039-partial: How does REM sleep change over the course of the night, and what percentage of total sleep is spent in REM?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

Raw answer before refusal normalization:

````text
The provided sources do not contain the answer to this question.
````

---

## s0039-seed: What happens in the brain during REM sleep?

Answerable: True

Problems:
- no citations

Answer:

````text
The sources detail that during REM sleep, brain activity ramps up, often leading to vivid dreams, and that most muscles become temporarily paralyzed. However, the text does not explicitly state that REM sleep is the only visible external sign of this activity or that it is the only stage of sleep where dreaming occurs.
````

---

## s0047-gen: How does eating a lot of saturated fat affect LDL cholesterol?

Answerable: True

Problems:
- no citations

Answer:

````text
Saturated fats carry no double bonds, allowing them to pack tightly and stay solid at room temperature, whereas unsaturated fats have one or more double bonds that introduce kinks, keeping them liquid. This structural difference influences how each type affects your blood cholesterol, liver, and inflammatory responses.
````

---

## s0080-gen: How does parasitism differ from predation?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0080-hard_neg: Who first introduced the term symbiosis?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- only 50% of sentences cited
- low groundedness 50% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The provided sources do not contain the answer to the question "Who first introduced the term symbiosis?". While sources [1], [2], [3], and [4] define symbiosis as a close, long-term interaction between organisms of different species and describe the three main types (mutualism, commensalism, and parasitism), they do not mention the specific historical origin or first introduction of the term.
````

---

## s0099-gen: How much do anti-erosion measures cost compared with restoring eroded land?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0099-partial: How do terraces help prevent soil erosion, and how should farmers build them?

Answerable: True

Problems:
- low groundedness 51% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Terraced farming is a primary method to prevent soil erosion by creating flat surfaces that reduce the speed of wind and water movement [1]. Farmers should build these terraces using intercropping systems to ensure full crop cover and manage land effectively [1].
````

---

## s0109-gen: Why are Old Faithful's eruptions so predictable?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0109-seed: How do geysers like Old Faithful work?

Answerable: True

Problems:
- low groundedness 19% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The sources provide a detailed explanation of how geysers work, specifically detailing the process of groundwater seeping through cracks, heating by magma, and creating pressure that forces water and steam to erupt [3].
````

---

## s0128-gen: How does a snowflake start to form?

Answerable: True

Problems:
- low groundedness 59% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Snowflakes form through the process of water vapor in the atmosphere condensing into tiny ice crystals, which then grow rapidly until they reach a size where they can fall to the ground [5].
````

---

## s0128-seed: Why do snowflakes have six sides?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources explain that snowflakes have six-sided symmetry because the shape of the ice crystal is determined by the temperature and humidity of the air, and the environment where they grow impacts their shape. The sources do not explicitly state that snowflakes grow so thin or that corners grow faster than top and bottom faces, though they mention that ice formation favors hexagonal ice in certain atmospheric conditions.
````

---

## s0150-gen: How long does it take sunlight to reach Earth?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0150-partial: What unit do professional astronomers mostly use instead of the light-year, and how many light-years is that unit equal to?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
Professional astronomers mostly use the parsec (pc) instead of the light-year. One parsec is approximately equal to 3.26 light-years [2].
````

---

## s0150-seed: How long is a light-year in kilometres?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0167-gen: Who discovered quantum entanglement?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0216-gen: Do phones store an actual image of my fingerprint?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0216-partial: How do ultrasonic fingerprint sensors work, and which phone was the first to use one?

Answerable: True

Problems:
- low groundedness 41% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Ultrasonic fingerprint sensors operate by measuring the reflected ultrasonic pulse from the ridge patterns on a finger to determine 3D shape, a process that allows them to function through the phone screen [2]. The first phone to use an ultrasonic fingerprint scanner was the iPhone 1, which was released in 2011 [5].
````

---

## s0230-gen: What was Alan Turing convicted of in 1952, and what was his sentence?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0230-seed: Who was Alan Turing and what did he contribute to computing?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0241-gen: What can still be seen about your browsing when a website uses HTTPS?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0241-seed: How does HTTPS keep websites secure?

Answerable: True

Problems:
- low groundedness 45% (possible outside knowledge or heavy paraphrase)

Answer:

````text
HTTPS keeps websites secure by encrypting data in transit using SSL/TLS, preventing hackers from intercepting sensitive information like passwords and payment details [1]. This encryption ensures that sensitive activity remains safe from interception even though the connection is not fully private [4].
````

---

## s0273-gen: How much carbon dioxide does the average person produce each year?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0273-partial: What is a carbon footprint, and how does carbon offsetting work?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
The sources define a carbon footprint as the total amount of greenhouse gases emitted into the atmosphere associated with an individual, community, or product, including emissions from daily activities and transportation [1][2]. While the text explains how to calculate a footprint, it does not detail the mechanism of carbon offsetting.
````

---

## s0295-gen: How does adaptive cruise control work?

Answerable: True

Problems:
- low groundedness 55% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Adaptive cruise control works by using radar sensors to detect traffic ahead and automatically adjusting the vehicle's speed to maintain a safe following distance while keeping the preset target speed [2].
````

---

## s0301-gen: Does the keystone support all the weight of an arch bridge?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0351-gen: What are some common types of advertising?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0351-partial: What are the 4 P's of marketing, and how should a business decide what price to charge?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

Raw answer before refusal normalization:

````text
The provided sources do not contain the answer to the question.
````

---

## s0351-seed: What is the difference between marketing and advertising?

Answerable: True

Problems:
- low groundedness 57% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The sources explicitly state that while marketing and advertising are closely related, they serve distinct purposes and are not interchangeable [1][2]. Marketing determines what a business should say and drives long-term strategy, whereas advertising is a specific paid method used within that plan to share messages [2][5].
````

---

## s0370-seed: How did the printing press change Europe?

Answerable: True

Problems:
- no citations

Answer:

````text
The sources detail the specific mechanics and economic impact of the printing press, such as Gutenberg's mass production of books and the speed of the Protestant Reformation, but they do not explicitly state the overall historical outcome of the printing press on Europe.
````

---

## s0385-gen: Why was Canberra chosen as Australia's capital instead of Sydney or Melbourne?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0415-gen: What role did the chorus play in Greek theatre?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0425-gen: What were the Cotswold Olimpick Games?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0425-seed: When were the first modern Olympic Games held?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0448-gen: Why did Zimbardo end the Stanford Prison Experiment early?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

---

## s0448-seed: What was the Stanford prison experiment?

Answerable: True

Problems:
- low groundedness 29% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The Stanford Prison Experiment was a psychological study where participants were assigned to roles within a simulated prison environment, leading to the development of abusive and authoritarian guard behavior and submissive prisoner behavior [3].
````

---

## s0462-partial: What is a ground fault, and how can you test for one?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

Raw answer before refusal normalization:

````text
The provided sources do not contain the answer to the question.
````

---

## s0462-seed: Why do circuit breakers trip?

Answerable: True

Problems:
- low groundedness 50% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Circuit breakers trip when electrical currents exceed the circuit's capacity, often due to overloads, ground faults, or appliance malfunctions [1][3].
````

---

## q012: How do noise-cancelling headphones work?

Answerable: True

Problems:
- low groundedness 44% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Noise-cancelling headphones work by using active technology to detect ambient sounds and generate an opposing signal that reduces the unwanted noise, while passive isolation provides a physical barrier to block sound waves entirely [2].
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

## q023: How does a refrigerator keep food cold?

Answerable: True

Problems:
- low groundedness 57% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Refrigerators work primarily on the principles of thermodynamics, specifically the refrigeration cycle, where a circulating refrigerant absorbs heat from the interior and releases it outside through coils and a compressor [3]. This continuous process removes heat from the insulated interior, which slows microbial growth and chemical reactions, helping food remain safe and fresh [1].
````

---

## q020: What is the greenhouse effect?

Answerable: True

Problems:
- no citations
- low groundedness 52% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The sources provide definitions and mechanisms for the greenhouse effect, including its role in trapping heat from the sun and maintaining Earth's temperature, as well as specific examples like the Golden Gate Bridge and the greenhouse effect diagram.
````

---

## q006: How do lithium-ion batteries degrade over time?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
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

## q014: Why do onions make people cry?

Answerable: True

Problems:
- low groundedness 44% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The sources indicate that onions cause crying due to the formation of a sulfur-containing chemical called lachrymatory factor when cut or damaged, which irritates the eyes and triggers tear production [1][3]. To prevent this, one should use a sharp knife to avoid crushing the onion, chill it in ice water before cutting, and avoid cutting near the root end where sulfuric compounds are highest concentrated [3].
````
