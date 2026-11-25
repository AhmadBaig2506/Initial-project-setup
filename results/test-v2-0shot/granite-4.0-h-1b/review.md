# Review: granite-4.0-h-1b (test-v2-0shot)

72 of 114 answers flagged. Full prompts are in `prompts.md`, raw data in `answers.jsonl`.

| Problem | Count |
|---|---|
| no citations | 43 |
| low groundedness | 26 |
| wrong answer/refuse decision | 16 |
| off-topic answer | 15 |
| some sentences uncited | 5 |
| too long | 1 |

---

## s0004-gen: What warning signs might appear a day or two before a migraine?

Answerable: True

Problems:
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[4]
````

---

## s0004-hard_neg: What medications can stop a migraine once it starts?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1]
````

---

## s0004-seed: What causes migraines and how are they treated?

Answerable: True

Problems:
- low groundedness 47% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1] Migraines are caused by imbalances in brain chemicals, such as serotonin, and can be triggered by various factors including genetic predisposition, age, and environmental triggers. [2] Migraines are treated by managing symptoms during an attack, which may include pain relief medications, and by addressing underlying causes, such as sleep disorders or depression. [3] Migraines are treated by identifying and avoiding triggers, using over-the-counter or prescription medications, and in some cases, through lifestyle changes or alternative therapies. [4] Migraines are treated by identifying and avoiding triggers, using over-the-counter or prescription medications, and in some cases, through lifestyle changes or alternative therapies.
````

---

## s0039-gen: When was REM sleep first discovered and how did it get its name?

Answerable: True

Problems:
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[2]
````

---

## s0039-hard_neg: How long after falling asleep does the first REM period begin?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1]
````

---

## s0039-partial: How does REM sleep change over the course of the night, and what percentage of total sleep is spent in REM?

Answerable: True

Problems:
- no citations

Answer:

````text
REM sleep becomes longer toward morning, reflecting the brain's sleep-regulating systems and the interaction between sleep pressure and the body's circadian timing system.
````

---

## s0039-seed: What happens in the brain during REM sleep?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
[1] [2] [3] [4] [5]
The brain activity ramps up during REM sleep, leading to vivid dreams. Most of the muscles become temporarily paralyzed.
````

---

## s0047-gen: How does eating a lot of saturated fat affect LDL cholesterol?

Answerable: True

Problems:
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[4]
````

---

## s0047-seed: What is the difference between saturated and unsaturated fats?

Answerable: True

Problems:
- no citations

Answer:

````text
Saturated fats have no double bonds between carbon atoms, allowing them to pack tightly and stay solid at room temperature, while unsaturated fats have one or more double bonds, making them liquid at room temperature.
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

Raw answer before refusal normalization:

````text
The sources do not contain information about the difference between parasitism and predation.
````

---

## s0080-hard_neg: Who first introduced the term symbiosis?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- no citations
- low groundedness 33% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The term "symbiosis" was first introduced by Anton van Leeuwenhoek
````

---

## s0080-seed: What is symbiosis and what are its main types?

Answerable: True

Problems:
- no citations

Answer:

````text
Symbiosis is a close, long-term interaction between organisms of different species. The main types of symbiotic relationships are mutualism, where both organisms benefit, commensalism, where one organism benefits while the other is unaffected, and parasitism, where one organism benefits at the expense of the other.
````

---

## s0099-gen: How much do anti-erosion measures cost compared with restoring eroded land?

Answerable: True

Problems:
- no citations

Answer:

````text
Anti-erosion measures have a median cost of $500 per hectare, while restoring eroded land can cost around $1,500–$2,000 per hectare.
````

---

## s0099-hard_neg: Does reducing tillage help prevent soil erosion?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1]
````

---

## s0099-partial: How do terraces help prevent soil erosion, and how should farmers build them?

Answerable: True

Problems:
- no citations
- low groundedness 38% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Terraces help prevent soil erosion by creating flat surfaces on slopes, allowing water to flow more easily and reducing the impact of raindrops on the soil. Farmers should build terraces by constructing steps or platforms on the slope, using materials like stone, concrete, or soil.
````

---

## s0099-seed: What is soil erosion and how can farmers prevent it?

Answerable: True

Problems:
- no citations

Answer:

````text
Soil erosion is the process of soil being removed from a given area by wind or water, and it can be prevented by using soil-friendly agricultural practices, offering incentives for land management, and implementing erosion-preventative measures.
````

---

## s0109-gen: Why are Old Faithful's eruptions so predictable?

Answerable: True

Problems:
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[4]
````

---

## s0109-seed: How do geysers like Old Faithful work?

Answerable: True

Problems:
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1]
````

---

## s0128-gen: How does a snowflake start to form?

Answerable: True

Problems:
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1]
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

Raw answer before refusal normalization:

````text
The sources do not contain the answer to "How long does it take sunlight to reach Earth?"
````

---

## s0150-hard_neg: When was the term light-year first used?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- no citations

Answer:

````text
The term light-year was first used in the late 20th century.
````

---

## s0150-partial: What unit do professional astronomers mostly use instead of the light-year, and how many light-years is that unit equal to?

Answerable: True

Problems:
- WRONG DECISION: refused an answerable question

Answer:

````text
The sources do not contain the answer.
````

Raw answer before refusal normalization:

````text
The sources do not contain the answer to the question.
````

---

## s0167-hard_neg: Who received the 2022 Nobel Prize in Physics for work on quantum entanglement?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1]
````

---

## s0193-gen: What is the difference between Avogadro's number and the Avogadro constant?

Answerable: True

Problems:
- no citations

Answer:

````text
The difference between Avogadro's number and the Avogadro constant is that Avogadro's number is the numerical value 6.02214076 × 10²³, while the Avogadro constant is that value expressed per mole (Nₐ = 6.02214076 × 10²³ mol⁻¹).
````

---

## s0193-hard_neg: Who coined the term Avogadro's number, and when?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- no citations

Answer:

````text
The term "Avogadro's number" was coined by Amedeo Avogadro.
````

---

## s0216-gen: Do phones store an actual image of my fingerprint?

Answerable: True

Problems:
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1]
````

---

## s0216-hard_neg: When did fingerprint scanners first appear on smartphones?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- no citations
- low groundedness 31% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Fingerprint scanners first appeared on smartphones in the early 2010s, with the first widespread adoption occurring around 2011.
````

---

## s0216-partial: How do ultrasonic fingerprint sensors work, and which phone was the first to use one?

Answerable: True

Problems:
- only 33% of sentences cited
- low groundedness 51% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Ultrasonic fingerprint sensors work by emitting ultrasonic waves that bounce off the ridges of a fingerprint, and then measure the time it takes for the waves to return. This allows the sensor to create a detailed image of the fingerprint. The first phone to use an ultrasonic fingerprint sensor was the Samsung Galaxy S8, released in 2017 [1].
````

---

## s0216-seed: How do fingerprint scanners on phones work?

Answerable: True

Problems:
- no citations

Answer:

````text
Fingerprint scanners on phones work by scanning the unique ridge patterns on a user's finger and comparing them with encrypted biometric data stored on the device. The scanners use optical, capacitive, or ultrasonic technology to capture and analyze the fingerprint data.
````

---

## s0230-gen: What was Alan Turing convicted of in 1952, and what was his sentence?

Answerable: True

Problems:
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1]
````

---

## s0230-seed: Who was Alan Turing and what did he contribute to computing?

Answerable: True

Problems:
- low groundedness 30% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1] Alan Turing was a British mathematician and computer scientist who made significant contributions to computing.
````

---

## s0241-gen: What can still be seen about your browsing when a website uses HTTPS?

Answerable: True

Problems:
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1] [2] [3] [4] [5]
````

---

## s0273-hard_neg: When was the term carbon footprint first used?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- low groundedness 40% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The term "carbon footprint" was first used in [1].
````

---

## s0295-gen: How does adaptive cruise control work?

Answerable: True

Problems:
- low groundedness 35% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1] The sources explain that adaptive cruise control (ACC) works by using sensors to detect the speed and distance of the vehicle ahead, then automatically adjusting the car's speed to maintain a safe following distance.
````

---

## s0295-seed: How does cruise control work in a car?

Answerable: True

Problems:
- too long: 6 sentences (limit 5)

Answer:

````text
[1] Cruise control works by maintaining a preset speed set by the driver. It does this by controlling the throttle input to the engine, accelerating or decelerating as needed to keep the vehicle at the desired speed. [2] Cruise control in a car works by using a system that automatically adjusts the throttle to maintain a set speed. When the driver sets the desired speed, the system engages and maintains that speed until the driver changes it or applies the brakes. [3] Cruise control works by automatically adjusting the throttle to maintain a preset speed. It uses sensors to detect the vehicle's speed and automatically adjusts the throttle to keep the car moving at the set speed, while also monitoring the distance between the car and the one in front. [4] Cruise control works by maintaining a preset speed set by the driver. It does this by controlling the throttle input to the engine, accelerating or decelerating as needed to keep the vehicle at the desired speed. [5] Cruise control works by automatically adjusting the throttle to maintain a set speed. It uses sensors to detect the vehicle's speed and automatically adjusts the throttle to keep the car moving at the set speed, while also monitoring the distance between the car and the one in front.
````

---

## s0301-gen: Does the keystone support all the weight of an arch bridge?

Answerable: True

Problems:
- no citations

Answer:

````text
The keystone supports the weight of an arch bridge, but a completed arch transfers force through the entire ring of voussoirs into the supports.
````

---

## s0301-seed: How do arch bridges support heavy loads?

Answerable: True

Problems:
- no citations

Answer:

````text
Arch bridges support heavy loads through the effective distribution of the load along the curve of the arch to the supports at each end, utilizing the compressive strength of materials like stone, brick, reinforced concrete, and steel.
````

---

## s0334-gen: Do sunk costs count in opportunity cost?

Answerable: True

Problems:
- no citations

Answer:

````text
Sunk costs do not count in opportunity cost, because money already spent and unrecoverable cannot be regained by any choice available now.
````

---

## s0334-hard_neg: Who developed the concept of opportunity cost?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- no citations
- low groundedness 18% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The concept of opportunity cost was developed by economists, particularly by Alfred Marshall and John Bates Clark.
````

---

## s0334-seed: What is opportunity cost in economics?

Answerable: True

Problems:
- no citations

Answer:

````text
Opportunity cost in economics is the value of the next best alternative that is given up when a choice is made. It represents the real cost of a decision, including both explicit and implicit costs.
````

---

## s0351-hard_neg: How does the American Marketing Association define marketing?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- low groundedness 20% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The American Marketing Association defines marketing as "the management process for establishing, growing, maintaining, and satisfying customer relationships through creating, delivering, and communicating superior customer value" [1].
````

---

## s0351-partial: What are the 4 P's of marketing, and how should a business decide what price to charge?

Answerable: True

Problems:
- no citations

Answer:

````text
The 4 P's of marketing are Product, Price, Place, and Promotion. A business should decide what price to charge by considering the value of their product, the competition, and the target customer's willingness to pay.
````

---

## s0351-seed: What is the difference between marketing and advertising?

Answerable: True

Problems:
- no citations

Answer:

````text
The difference between marketing and advertising is that marketing is the overall strategy to understand and satisfy customer needs, while advertising is a part of marketing that involves paid placement of messages to promote a product or service.
````

---

## s0370-gen: How did the printing press help spread the Protestant Reformation?

Answerable: True

Problems:
- no citations

Answer:

````text
The printing press helped spread the Protestant Reformation by allowing Martin Luther's 95 Theses to be copied and distributed rapidly across Europe, making reformist ideas accessible to a wider audience than before.
````

---

## s0370-hard_neg: How did the printing press affect the use of Latin as a scholarly language?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- no citations
- low groundedness 23% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The printing press led to a decline in the use of Latin as a scholarly language, as books became more widely available and accessible in vernacular languages.
````

---

## s0370-seed: How did the printing press change Europe?

Answerable: True

Problems:
- no citations

Answer:

````text
The printing press changed Europe by allowing books to be mass-produced, reducing the cost of a book by 95% within decades. This led to an information explosion, fueling the spread of literacy, the Protestant Reformation, and the Scientific Revolution.
````

---

## s0385-gen: Why was Canberra chosen as Australia's capital instead of Sydney or Melbourne?

Answerable: True

Problems:
- no citations

Answer:

````text
Canberra was chosen as Australia's capital to compromise between the competing cities of Sydney and Melbourne.
````

---

## s0415-gen: What role did the chorus play in Greek theatre?

Answerable: True

Problems:
- no citations

Answer:

````text
The chorus in Greek theatre acted as a collective character, providing commentary, context, and reflections on the events of the play through song and dance.
````

---

## s0415-seed: How did ancient Greek theatre work?

Answerable: True

Problems:
- no citations

Answer:

````text
Ancient Greek theatre worked as a system that combined architecture, performance, and audience to create a controlled and shared experience. It used architectural design and acoustics to project sound naturally across large spaces, with the audience seated in a semicircular arrangement for clear visibility and a shared experience.
````

---

## s0425-gen: What were the Cotswold Olimpick Games?

Answerable: True

Problems:
- no citations

Answer:

````text
The Cotswold Olimpick Games were an annual meeting near Chipping Campden, England, involving various sports, organized by the lawyer Robert Dover between 1612 and 1642.
````

---

## s0448-gen: Why did Zimbardo end the Stanford Prison Experiment early?

Answerable: True

Problems:
- no citations

Answer:

````text
Zimbardo ended the Stanford Prison Experiment early due to ethical concerns about the participants' well-being.
````

---

## s0448-hard_neg: How were participants in the Stanford Prison Experiment assigned to be prisoners or guards?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- no citations

Answer:

````text
Participants in the Stanford Prison Experiment were assigned to be either prisoners or guards.
````

---

## s0448-seed: What was the Stanford prison experiment?

Answerable: True

Problems:
- no citations

Answer:

````text
The Stanford prison experiment was a psychological study conducted by Philip Zimbardo in 1971, where nine college students were placed in a simulated prison environment to observe the effects of power and abuse of authority.
````

---

## s0462-gen: How does a circuit breaker cut off a circuit when it trips?

Answerable: True

Problems:
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1]
````

---

## s0462-partial: What is a ground fault, and how can you test for one?

Answerable: True

Problems:
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)
- low groundedness 0% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1]
````

---

## s0462-seed: Why do circuit breakers trip?

Answerable: True

Problems:
- no citations

Answer:

````text
Circuit breakers trip due to various reasons such as short circuitry, grounding faults, arc faults, an overloaded circuit, and a corroded circuit. They are designed to detect electrical abnormalities and cut off the electrical connection to prevent electrical accidents and damage.
````

---

## q016: What causes inflation in an economy?

Answerable: True

Problems:
- no citations

Answer:

````text
Inflation in an economy is caused by demand-pull inflation, cost-push inflation, built-in inflation, and expectations of inflation.
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
Caffeine affects the brain by blocking adenosine, a chemical messenger that helps regulate sleepiness and alertness, leading to increased alertness, improved attention, and temporary reduction of fatigue.
````

---

## q005: What are the main symptoms of type 2 diabetes?

Answerable: True

Problems:
- no citations

Answer:

````text
The main symptoms of type 2 diabetes include increased thirst, frequent urination, fatigue, blurry vision, and frequent infections.
````

---

## q000: What causes sleep apnea?

Answerable: True

Problems:
- no citations

Answer:

````text
Sleep apnea is caused by conditions that block airflow through the upper airway during sleep, such as the tongue falling backward and blocking the airway (obstructive sleep apnea) or problems with the brain's control of breathing while sleeping (central sleep apnea).
````

---

## q009: What causes the seasons on Earth?

Answerable: True

Problems:
- no citations

Answer:

````text
The sources all agree that the seasons on Earth are caused by the Earth's axial tilt of approximately 23.5 degrees relative to its orbital plane around the Sun.
````

---

## q023: How does a refrigerator keep food cold?

Answerable: True

Problems:
- no citations

Answer:

````text
A refrigerator keeps food cold by continuously transferring heat from its insulated interior to the surrounding room through a repeating refrigeration cycle involving a circulating refrigerant, compressor, condenser, expansion device, and evaporator.
````

---

## q021: How do solar panels generate electricity?

Answerable: True

Problems:
- no citations

Answer:

````text
The sources indicate that solar panels generate electricity through the photovoltaic effect, where sunlight excites electrons in silicon cells, creating direct current (DC) electricity. This DC electricity is then converted into alternating current (AC) by an inverter for use in homes and businesses.
````

---

## q020: What is the greenhouse effect?

Answerable: True

Problems:
- no citations

Answer:

````text
The greenhouse effect is a process in Earth's atmosphere where certain gases, known as greenhouse gases, trap heat from the sun and keep the planet's temperature within a range suitable for life.
````

---

## q002: Why is the sky blue?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
The sky is blue because sunlight contains all colors of the rainbow, and the sky appears blue due to the scattering of light by the Earth's atmosphere. Shorter wavelengths (blue) are scattered more than longer wavelengths (red) [1].
````

---

## q006: How do lithium-ion batteries degrade over time?

Answerable: True

Problems:
- no citations

Answer:

````text
Lithium-ion batteries degrade over time due to a combination of chemical and mechanical processes, including solid electrolyte interphase (SEI) growth, lithium plating, cathode dissolution, and mechanical stress from expansion and contraction.
````

---

## q013: What are the health benefits of regular walking?

Answerable: True

Problems:
- no citations

Answer:

````text
Regular walking can lower blood pressure, improve cognition, promote heart health, reduce rates of chronic disease, and is associated with numerous health benefits, particularly in the context of healthy aging and longevity in the Blue Zones.
````

---

## q022: What causes earthquakes?

Answerable: True

Problems:
- no citations

Answer:

````text
Earthquakes are caused by the release of built-up stress in the Earth's crust, usually along faults or at the boundaries of tectonic plates. This release sends seismic waves radiating from the point of rupture, traveling through the Earth and shaking the ground. (1)
````

---

## q010: How does photosynthesis convert light into energy?

Answerable: True

Problems:
- no citations

Answer:

````text
Photosynthesis converts light into energy through a two-stage process. In the first stage, light-dependent reactions capture light energy and use it to produce hydrogen carrier NADPH and ATP. In the second stage, the light-independent reactions use these products to fix carbon dioxide into organic compounds.
````

---

## q001: How do vaccines train the immune system?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
[1] Vaccines train the immune system to respond to pathogens without the dangerous side-effects of the disease. They do this by providing an antigen for a specific disease that the immune system responds to by producing antibodies.
````

---

## q014: Why do onions make people cry?

Answerable: True

Problems:
- only 33% of sentences cited

Answer:

````text
[1] [2] [3] [4] [5]
Onions make people cry due to the release of a volatile compound called lachrymatory factor when damaged. This chemical irritates the eyes, causing tears to form. Chilling the onion before cutting, using a sharp knife, and running water while cutting can help reduce the tears.
````
