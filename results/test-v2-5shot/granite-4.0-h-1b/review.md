# Review: granite-4.0-h-1b (test-v2-5shot)

80 of 114 answers flagged. Full prompts are in `prompts.md`, raw data in `answers.jsonl`.

| Problem | Count |
|---|---|
| no citations | 44 |
| wrong answer/refuse decision | 24 |
| low groundedness | 22 |
| some sentences uncited | 8 |
| off-topic answer | 3 |
| too long | 1 |
| cut off | 1 |

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
- low groundedness 27% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1] Migraine - Symptoms and causes - Mayo Clinic
There is no specific medication that can stop a migraine once it starts.
````

---

## s0004-seed: What causes migraines and how are they treated?

Answerable: True

Problems:
- only 21% of sentences cited
- too long: 14 sentences (limit 5)
- cut off at the token limit

Answer:

````text
[1] Migraine - Symptoms and causes - Mayo Clinic
Migraines are often not diagnosed or treated. If you regularly have symptoms of migraines, keep a record of your attacks and how you treated them. Then make an appointment with your healthcare professional to discuss your headaches. [2] Chronic Migraine: What It Is, Causes, Symptoms & Treatment
Because migraines are disruptive and this condition causes them to happen frequently, experts consider chronic migraine a very disabling condition, meaning it keeps you from doing certain things. Migraines aren’t usually dangerous, but they greatly disrupt your life. They also increase your risk of life-threatening conditions like stroke and heart attack. Some migraine symptoms can also look like stroke symptoms. Because of that, chronic migraine needs expert monitoring and treatment. [3] Migraine Causes: Triggers and Risk Factors - WebMD
What Causes Migraines? You know how your migraine headaches start but have no idea why you get them. What makes you more likely than some other people to get these awful headaches? Common Causes of Migraines Doctors aren’t totally sure what causes migraine headaches, but they think imbalances in certain brain chemicals may play a role. The trigeminal nerve in your head runs your eyes and mouth. It also helps you feel sensations in your face and is a major pathway for pain. Your levels of a chemical called serotonin may fall at the start of a migraine, and this nerve can release chemicals called neurotransmitters that travel to your brain and cause pain. Migraine Risk Factors You might be more likely to
````

---

## s0039-gen: When was REM sleep first discovered and how did it get its name?

Answerable: True

Problems:
- no citations

Answer:

````text
REM sleep was first discovered in the 1950s.
````

---

## s0039-partial: How does REM sleep change over the course of the night, and what percentage of total sleep is spent in REM?

Answerable: True

Problems:
- no citations

Answer:

````text
REM sleep becomes longer toward morning, with early sleep containing relatively more deep NREM sleep.
````

---

## s0039-seed: What happens in the brain during REM sleep?

Answerable: True

Problems:
- no citations

Answer:

````text
During REM sleep, the brain activity ramps up, often leading to vivid dreams. Most of the muscles become temporarily paralyzed, and the pulse and breathing slow down.
````

---

## s0047-gen: How does eating a lot of saturated fat affect LDL cholesterol?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
[1] Saturated vs. Unsaturated Fat: What’s the Difference? Saturated fats carry no double bonds between the carbon atoms in their fatty acid chains, which allows them to pack tightly and stay solid at room temperature.
````

---

## s0047-seed: What is the difference between saturated and unsaturated fats?

Answerable: True

Problems:
- no citations

Answer:

````text
Saturated and unsaturated fats differ in their chemical structure, their physical behavior, and, to varying degrees, their effects on your health. Saturated fats carry no double bonds between the carbon atoms in their fatty acid chains, which allows them to pack tightly and stay solid at room temperature. Unsaturated fats have one or more double bonds that introduce kinks in the chain, keeping them liquid.
````

---

## s0080-gen: How does parasitism differ from predation?

Answerable: True

Problems:
- no citations

Answer:

````text
Parasitism differs from predation in that the parasite benefits by exploiting the host, while the host is not necessarily killed in predation.
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
Symbiosis is a close, long-term interaction between organisms of different species. The main types of symbiotic relationships are mutualism, where both organisms benefit; commensalism, where one organism benefits while the other is unaffected; and parasitism, where one organism benefits at the expense of the other.
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

Answer:

````text
[1] The Causes and Effects of Soil Erosion, and How to Prevent It
````

---

## s0099-partial: How do terraces help prevent soil erosion, and how should farmers build them?

Answerable: True

Problems:
- no citations
- low groundedness 43% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Terraces help prevent soil erosion by creating flat surfaces on slopes, which reduces the speed and volume of water flowing over the land. Farmers can build terraces by constructing raised rows of steps or platforms on the slope, using materials like stone, concrete, or soil.
````

---

## s0099-seed: What is soil erosion and how can farmers prevent it?

Answerable: True

Problems:
- no citations

Answer:

````text
Soil erosion is the process of soil being removed from a given area by wind or water. Farmers can prevent soil erosion by using soil-friendly agricultural practices, such as terraced farming, intercropping, and agroforestry systems.
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

Raw answer before refusal normalization:

````text
The sources do not contain information on why Old Faithful's eruptions are so predictable.
````

---

## s0109-seed: How do geysers like Old Faithful work?

Answerable: True

Problems:
- no citations

Answer:

````text
Geysers like Old Faithful work through a unique underground system where groundwater seeps down through cracks in the Earth's surface, coming into contact with hot rocks heated by magma. This heated water becomes superheated and pressurized, eventually finding a pathway to the surface where it erupts as steam and boiling water. The predictability of Old Faithful's eruptions is due to its relatively simple underground plumbing system, allowing for consistent pressure build-up and release.
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

## s0128-seed: Why do snowflakes have six sides?

Answerable: True

Problems:
- no citations

Answer:

````text
The sources explain that snowflakes have six sides due to the shape of the water molecule, which is two hydrogen atoms bonded to one oxygen atom. This hexagonal structure is a result of the crystalline structure of ice, which is also six-fold. The growth of snowflakes is also influenced by the temperature and humidity in the environment, which can cause them to form different shapes.
````

---

## s0150-hard_neg: When was the term light-year first used?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- no citations

Answer:

````text
The term light-year was first used in the late 20th century
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

## s0167-seed: What is quantum entanglement in simple terms?

Answerable: True

Problems:
- no citations

Answer:

````text
Quantum entanglement is a phenomenon where two particles become linked in such a way that the state of one particle instantaneously determines the state of another, regardless of the distance between them. Before measurement, neither particle has a definite state; they exist in superposition, with their properties linked through a shared quantum state.
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
The term "Avogadro's number" was coined by Amedeo Avogadro in 1811.
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

Raw answer before refusal normalization:

````text
The sources do not contain information on whether phones store an actual image of a user's fingerprint.
````

---

## s0216-hard_neg: When did fingerprint scanners first appear on smartphones?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- low groundedness 43% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Fingerprint scanners first appeared on smartphones in 2002, according to [1].
````

---

## s0216-partial: How do ultrasonic fingerprint sensors work, and which phone was the first to use one?

Answerable: True

Problems:
- no citations
- low groundedness 51% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Ultrasonic fingerprint sensors work by emitting ultrasonic waves that bounce off the ridges of a fingerprint. The returning echoes are then analyzed to create a digital image of the fingerprint. The first phone to use ultrasonic fingerprint sensors was the Samsung Galaxy S8, released in 2017.
````

---

## s0216-seed: How do fingerprint scanners on phones work?

Answerable: True

Problems:
- no citations

Answer:

````text
Fingerprint scanners on phones work by capturing an optical image of the user's fingerprint, which is then analyzed using algorithms to detect unique patterns on the surface. This process involves a finite resolution sensor that can detect ridges or marks by analyzing the lightest and darkest areas of the image. The scanner compares the captured fingerprint to encrypted biometric data stored on the device to unlock the phone.
````

---

## s0230-seed: Who was Alan Turing and what did he contribute to computing?

Answerable: True

Problems:
- low groundedness 17% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1] Alan Turing was a British mathematician and computer scientist who made significant contributions to the development of theoretical computer science and to the Allied code-breaking efforts of World War II.
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
- only 50% of sentences cited

Answer:

````text
[1] HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP, the protocol that powers the World Wide Web. It encrypts data in transit, protecting sensitive information like passwords and payment details from interception.
````

---

## s0273-gen: How much carbon dioxide does the average person produce each year?

Answerable: True

Problems:
- low groundedness 38% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1] The average person produces about four tons of carbon dioxide each year [1].
````

---

## s0273-hard_neg: When was the term carbon footprint first used?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- low groundedness 22% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The term "carbon footprint" was first used in 2006, according to the information provided in [1].
````

---

## s0273-partial: What is a carbon footprint, and how does carbon offsetting work?

Answerable: True

Problems:
- no citations

Answer:

````text
A carbon footprint is the total amount of greenhouse gases emitted into the atmosphere, such as carbon dioxide (CO2), methane (CH4), nitrous oxide (N2O), and hydrofluorocarbons (HFCs), associated with an individual, product, person, or event. Carbon offsetting is a way to compensate for these emissions by investing in projects that reduce or remove an equivalent amount of greenhouse gases elsewhere.
````

---

## s0295-seed: How does cruise control work in a car?

Answerable: True

Problems:
- no citations

Answer:

````text
Cruise control works by allowing the driver to set a preset speed, which the system's computer then maintains until the driver adjusts the speed, taps the brake, or disengages the system.
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

## s0301-seed: How do arch bridges support heavy loads?

Answerable: True

Problems:
- no citations

Answer:

````text
Arch bridges support heavy loads through the effective distribution of the load along the curve of the arch to the supports at each end.
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
The concept of opportunity cost was developed by economists, particularly by Alfred Marshall in the late 19th century.
````

---

## s0334-seed: What is opportunity cost in economics?

Answerable: True

Problems:
- no citations

Answer:

````text
Opportunity cost in economics is the value of the next best alternative that is given up when a choice is made. It represents the real cost of a decision, calculated as the value of the alternative that is not chosen.
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

Raw answer before refusal normalization:

````text
The sources provided do not contain information about common types of advertising.
````

---

## s0351-hard_neg: How does the American Marketing Association define marketing?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- low groundedness 27% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The American Marketing Association (AMA) defines marketing as "the stimulation, development, and representation of ideas, goods, and services" [1].
````

---

## s0351-partial: What are the 4 P's of marketing, and how should a business decide what price to charge?

Answerable: True

Problems:
- no citations

Answer:

````text
The 4 P's of marketing are Product, Price, Place, and Promotion. A business should decide what price to charge by considering factors such as the value of the product, competitor pricing, target customer's willingness to pay, and the business's cost structure.
````

---

## s0351-seed: What is the difference between marketing and advertising?

Answerable: True

Problems:
- no citations

Answer:

````text
The difference between marketing and advertising is that marketing is the overall strategy to understand and satisfy customer needs, while advertising is a part of marketing that involves paid placement of a message to promote a product or service.
````

---

## s0370-gen: How did the printing press help spread the Protestant Reformation?

Answerable: True

Problems:
- low groundedness 36% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1] The printing press helped spread the Protestant Reformation by allowing Martin Luther's 95 Theses to be copied and distributed quickly across Europe, making reformist ideas spread faster than traditional methods.
````

---

## s0370-hard_neg: How did the printing press affect the use of Latin as a scholarly language?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- no citations
- low groundedness 36% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The printing press made books more widely available, which helped to standardize the use of Latin as a scholarly language.
````

---

## s0370-seed: How did the printing press change Europe?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
[1] The printing press changed Europe by allowing books to be mass-produced for the first time, drastically reducing the cost of a book by 95% within decades. This triggered an information explosion, leading to the spread of literacy, the Protestant Reformation, and the Scientific Revolution.
````

---

## s0385-gen: Why was Canberra chosen as Australia's capital instead of Sydney or Melbourne?

Answerable: True

Problems:
- low groundedness 36% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1] The sources explain that Canberra was chosen as Australia's capital because it was a compromise between the warring town of Melbourne and Sydney.
````

---

## s0385-seed: What is the capital of Australia?

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

## s0425-hard_neg: Who won the marathon at the 1896 Athens Olympics?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- low groundedness 14% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1] The sources do not contain information about who won the marathon at the 1896 Athens Olympics.
````

---

## s0448-gen: Why did Zimbardo end the Stanford Prison Experiment early?

Answerable: True

Problems:
- no citations

Answer:

````text
Zimbardo ended the Stanford Prison Experiment early due to ethical concerns about the participants' well-being, specifically after Christina Maslach, an external observer, raised issues about the abuse and distress experienced by the participants.
````

---

## s0448-hard_neg: How were participants in the Stanford Prison Experiment assigned to be prisoners or guards?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- no citations

Answer:

````text
Participants were assigned to be either prisoners or guards based on their participation in the Stanford Prison Experiment.
````

---

## s0448-seed: What was the Stanford prison experiment?

Answerable: True

Problems:
- no citations

Answer:

````text
The Stanford prison experiment was a psychological study conducted by Philip Zimbardo in 1971 at Stanford University. Nine college students were placed in a simulated prison environment to observe the effects of perceived power and role-playing on behavior.
````

---

## s0462-gen: How does a circuit breaker cut off a circuit when it trips?

Answerable: True

Problems:
- low groundedness 50% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1] A circuit breaker cuts off a circuit when it trips due to an overload, short circuit, ground fault, or malfunctioning appliance.
````

---

## s0462-partial: What is a ground fault, and how can you test for one?

Answerable: True

Problems:
- low groundedness 32% (possible outside knowledge or heavy paraphrase)

Answer:

````text
[1] A ground fault occurs when an electrical current takes an unintended path to the ground, often through a person or object. [2] To test for a ground fault, you can use a ground fault circuit interrupter (GFCI) tester or a multimeter set to measure continuity.
````

---

## s0462-seed: Why do circuit breakers trip?

Answerable: True

Problems:
- no citations

Answer:

````text
Circuit breakers trip due to various reasons, including short circuitry, grounding faults, arc faults, an overloaded circuit, and a corroded circuit.
````

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
