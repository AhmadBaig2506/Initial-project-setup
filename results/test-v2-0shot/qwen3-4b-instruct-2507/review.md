# Review: qwen3-4b-instruct-2507 (test-v2-0shot)

20 of 114 answers flagged. Full prompts are in `prompts.md`, raw data in `answers.jsonl`.

| Problem | Count |
|---|---|
| some sentences uncited | 12 |
| low groundedness | 11 |
| wrong answer/refuse decision | 1 |
| too long | 1 |

---

## s0004-seed: What causes migraines and how are they treated?

Answerable: True

Problems:
- low groundedness 54% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The exact cause of migraines is not fully understood, but imbalances in certain brain chemicals, such as serotonin, and activation of the trigeminal nerve, which carries sensations from the head to the brain, may play a role [3]. Family history, age, and personal triggers like stress or certain foods can increase the likelihood of migraines [3][5]. Migraines are typically treated with medications that relieve symptoms during an attack, such as pain relievers or triptans, and preventive treatments may be used for frequent or chronic cases [1][2]. A healthcare provider diagnoses migraines through a physical and neurological exam, medical history review, and sometimes imaging or blood tests to rule out other conditions [5]. Treatment plans are personalized based on symptom patterns and individual risk factors [1][5].
````

---

## s0039-gen: When was REM sleep first discovered and how did it get its name?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
REM sleep was first discovered in the 1950s, when scientists studying sleeping infants noticed distinct periods when their eyes darted quickly from side to side behind closed eyelids. These rapid eye movements earned REM sleep its name [2].
````

---

## s0039-partial: How does REM sleep change over the course of the night, and what percentage of total sleep is spent in REM?

Answerable: True

Problems:
- only 67% of sentences cited

Answer:

````text
REM sleep episodes generally become longer toward morning, and REM sleep is not distributed evenly throughout the night [5]. Early sleep contains relatively more deep NREM sleep, while REM episodes increase in duration as the night progresses [5]. However, the sources do not specify the percentage of total sleep spent in REM.
````

---

## s0099-partial: How do terraces help prevent soil erosion, and how should farmers build them?

Answerable: True

Problems:
- low groundedness 42% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Terraces help prevent soil erosion by slowing down water flow on hillside farms, allowing more water to reach crops and reducing the force of runoff that can wash away topsoil [1]. They also stabilize the soil, preventing it from being carried away by wind or water [4]. Farmers should build terraces by creating flat, stepped levels on slopes, which can be done through manual labor or with simple engineering tools, and ensure the terraces are properly aligned with the slope to maximize effectiveness [1]. These terraces should be combined with full crop cover, such as through intercropping or agroforestry, to further protect the soil [1].
````

---

## s0150-partial: What unit do professional astronomers mostly use instead of the light-year, and how many light-years is that unit equal to?

Answerable: True

Problems:
- only 25% of sentences cited
- low groundedness 30% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Professional astronomers mostly use the parsec (pc) instead of the light-year [2]. However, the provided sources do not state how many light-years a parsec is equal to. Therefore, the exact conversion is not available in the sources. The sources do not contain the answer.
````

---

## s0216-gen: Do phones store an actual image of my fingerprint?

Answerable: True

Problems:
- only 75% of sentences cited

Answer:

````text
No, phones usually do not store an actual image of your fingerprint. Most phones store encrypted mathematical representations instead of real fingerprint images [1]. This means the data is transformed into a unique numeric code for security and privacy [4]. The actual image is not saved in a readable form on the device [1].
````

---

## s0216-partial: How do ultrasonic fingerprint sensors work, and which phone was the first to use one?

Answerable: True

Problems:
- only 67% of sentences cited

Answer:

````text
Ultrasonic fingerprint sensors work by sending ultrasonic pulses to the finger and measuring the reflected pulse to understand the 3D shape of the ridges in the fingerprint, similar to how bats and dolphins use echolocation [2]. This technology can even work through the phone screen and is generally considered safer than other types [1][2]. The sources do not specify which phone was the first to use an ultrasonic fingerprint sensor.
````

---

## s0230-seed: Who was Alan Turing and what did he contribute to computing?

Answerable: True

Problems:
- only 50% of sentences cited
- low groundedness 31% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The sources provided do not contain information about who Alan Turing was or his contributions to computing. While they discuss his role in the war effort and his conviction for homosexuality, they do not address his contributions to computing. [1][3][4][5]
````

---

## s0273-partial: What is a carbon footprint, and how does carbon offsetting work?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
A carbon footprint is defined as the total amount of greenhouse gases, such as carbon dioxide (CO₂) and methane (CH₄), emitted into the atmosphere as a result of an individual, organization, product, or event [1][3]. It is measured in equivalent tons of CO₂ and represents the total greenhouse gas emissions associated with daily activities like transportation, energy use, and consumption [1][3]. However, the provided sources do not explain how carbon offsetting works. The sources do not contain the answer.
````

---

## s0301-gen: Does the keystone support all the weight of an arch bridge?

Answerable: True

Problems:
- only 75% of sentences cited

Answer:

````text
No, the keystone does not support all the weight of an arch bridge. The completed arch shares the force through the entire ring of voussoirs, and the keystone helps close the masonry arch but is not a single load-bearing element carrying everything by itself [3][4]. Engineers understand that the load is distributed across the entire arch structure, not concentrated on the keystone [2]. Therefore, the keystone's role is structural and stabilizing, not load-bearing in the sense of supporting all the weight [4].
````

---

## s0334-gen: Do sunk costs count in opportunity cost?

Answerable: True

Problems:
- only 67% of sentences cited

Answer:

````text
No, sunk costs do not count in opportunity cost because money already spent and unrecoverable cannot be regained by any choice available now. Only the next-best alternative you can still choose belongs in the calculation [2]. This principle ensures that opportunity cost focuses on future, forgone alternatives rather than past expenditures [5].
````

---

## s0351-partial: What are the 4 P's of marketing, and how should a business decide what price to charge?

Answerable: True

Problems:
- only 50% of sentences cited
- low groundedness 40% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The 4 P's of marketing are product, price, place, and promotion strategy [5]. Price is determined by how customers perceive the brand and is influenced by market conditions, competition, and the value offered [5]. However, the sources do not provide specific guidance on how a business should decide what price to charge. The sources do not contain the answer.
````

---

## s0370-seed: How did the printing press change Europe?

Answerable: True

Problems:
- low groundedness 60% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The printing press changed Europe by drastically reducing the cost of books, enabling mass production and an information explosion [1]. This led to increased literacy, the rapid spread of Protestant Reformation ideas—such as Martin Luther's 95 Theses, which were distributed widely within weeks— and fueled the Scientific Revolution [1][3]. The press allowed reformist ideas to spread faster than traditional Church methods could suppress them, fundamentally altering religious and intellectual life [3]. Gutenberg himself never profited from his invention, highlighting the disconnect between technological innovation and personal gain [1][2].
````

---

## s0385-gen: Why was Canberra chosen as Australia's capital instead of Sydney or Melbourne?

Answerable: True

Problems:
- low groundedness 54% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Canberra was chosen as Australia's capital instead of Sydney or Melbourne because of political rivalries between the two cities, and a compromise was needed to avoid further conflict [5]. The decision to construct a new capital city was made to resolve the dispute between Sydney and Melbourne, which both had strong claims to being the capital [2]. The site of Canberra was selected in 1908 as a neutral location between the two major cities [2]. This compromise allowed for a fair and balanced capital that was not tied to either Sydney or Melbourne [3]. Canberra's central location in the Australian Capital Territory also provided equitable access to all parts of the country [4].
````

---

## s0415-gen: What role did the chorus play in Greek theatre?

Answerable: True

Problems:
- low groundedness 52% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The chorus played a role as a collective character, providing commentary, context, and reflections on the events of the play through song and dance [4]. It helped to contextualize the action, offer moral insights, and engage the audience in the narrative [4]. The chorus also served as a unifying element, reinforcing shared perspectives and aligning audience attention during performances [3].
````

---

## s0448-hard_neg: How were participants in the Stanford Prison Experiment assigned to be prisoners or guards?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- low groundedness 48% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The participants in the Stanford Prison Experiment were assigned to be prisoners or guards through a classified ad placed by Philip Zimbardo in the “help wanted” section of the Palo Alto Times, which advertised “Male college students needed for psychological study of prison life” [3]. The ad invited male college students to apply for a study on prison life, and after selection, participants were randomly assigned to either the prisoner or guard roles [3]. This random assignment was intended to study the influence of situational factors on behavior rather than individual personality traits [4].
````

---

## s0462-gen: How does a circuit breaker cut off a circuit when it trips?

Answerable: True

Problems:
- low groundedness 57% (possible outside knowledge or heavy paraphrase)

Answer:

````text
A circuit breaker cuts off a circuit by detecting abnormalities in electrical flow and using an internal spring mechanism to deactivate the circuit by force [3]. This action interrupts the electrical connection to prevent electrical accidents and damage [1]. The mechanism is triggered when the electrical current exceeds the safe limit, causing a sudden reduction in resistance that leads to high current and voltage, which activates the breaker [3]. This process ensures the circuit is safely disconnected from power [1].
````

---

## s0462-partial: What is a ground fault, and how can you test for one?

Answerable: True

Problems:
- only 67% of sentences cited
- low groundedness 43% (possible outside knowledge or heavy paraphrase)

Answer:

````text
A ground fault occurs when electricity finds an unintended path to ground, which is one of the common reasons circuit breakers trip [5]. Ground faults can be identified by symptoms such as flickering lights or a tingling sensation, but the sources do not provide specific instructions or methods for testing for a ground fault [5][4]. Therefore, the sources do not contain the answer.
````

---

## s0462-seed: Why do circuit breakers trip?

Answerable: True

Problems:
- too long: 6 sentences (limit 5)

Answer:

````text
Circuit breakers trip to prevent electrical accidents and damage by cutting off power when abnormalities are detected in the circuit [1]. Common causes include overloaded circuits, short circuits, ground faults, and appliance malfunctions [5]. An overloaded circuit occurs when too many devices draw power simultaneously, exceeding the circuit’s capacity [2][5]. Short circuits happen when a hot wire comes into contact with a neutral wire, causing a surge of electricity [2]. Ground faults occur when electricity finds an unintended path to ground [5]. These conditions trigger the breaker’s protective mechanisms, which then interrupt the electrical flow [5].
````

---

## q010: How does photosynthesis convert light into energy?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
Photosynthesis converts light into energy through a two-stage process that occurs in chloroplasts. In the first stage, light-dependent reactions capture light energy and use it to split water molecules, releasing oxygen and generating ATP and NADPH. In the second stage, light-independent reactions use ATP and NADPH to fix carbon dioxide into organic compounds like glucose [2][5]. This process involves chlorophyll and accessory pigments that absorb light, particularly in the red and blue wavelengths, to drive the conversion of light energy into stored chemical energy [2].
````
