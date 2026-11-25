# Review: qwen3-4b-instruct-2507 (test-v2-5shot)

17 of 114 answers flagged. Full prompts are in `prompts.md`, raw data in `answers.jsonl`.

| Problem | Count |
|---|---|
| some sentences uncited | 9 |
| low groundedness | 5 |
| too long | 2 |
| wrong answer/refuse decision | 2 |

---

## s0039-partial: How does REM sleep change over the course of the night, and what percentage of total sleep is spent in REM?

Answerable: True

Problems:
- only 67% of sentences cited

Answer:

````text
REM sleep changes over the course of the night as REM episodes generally become longer toward morning [5]. Early sleep contains relatively more deep NREM sleep, while REM episodes increase in duration later in the night [5]. The sources do not specify the percentage of total sleep spent in REM.
````

---

## s0099-partial: How do terraces help prevent soil erosion, and how should farmers build them?

Answerable: True

Problems:
- low groundedness 39% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Terraces help prevent soil erosion by slowing down water flow on hillside farms, allowing more water to reach crops and reducing the force of runoff that can wash away topsoil [1]. They also stabilize the soil, preventing it from being carried away by wind or water [4]. Farmers should build terraces by creating flat, stepped levels on slopes, which can be done through engineering techniques that match the terrain, and they should ensure the terraces are covered with crops or vegetation to further hold the soil in place [1].
````

---

## s0099-seed: What is soil erosion and how can farmers prevent it?

Answerable: True

Problems:
- too long: 6 sentences (limit 5)

Answer:

````text
Soil erosion is the process by which soil is worn away by wind and water, particularly affecting the topsoil that contains essential nutrients for crops [2][4]. It leads to decreased soil fertility, reduced crop yields, and sedimentation in waterways, which can cause flooding [2][4]. Farmers can prevent soil erosion by using soil-friendly agricultural practices such as terraced farming, which slows water flow and stabilizes soil [1]. Growing crops in intercropping systems or agroforestry, where trees and crops are grown together, helps protect the soil [1]. Additionally, alternating deep-rooted and shallow-rooted crops improves soil structure and reduces erosion [1]. Farmers also need financial support to afford anti-erosion measures, which have a median cost of $500 per hectare, as these practices are more cost-effective than land restoration, which can cost up to $2,000 per hectare [1][5].
````

---

## s0128-seed: Why do snowflakes have six sides?

Answerable: True

Problems:
- low groundedness 49% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Snowflakes have six sides because the crystalline structure of ice is six-fold, which is due to the shape of the water molecule [2]. This six-fold symmetry is favored by the conditions in Earth's atmosphere, where water forms hexagonal ice [3]. The hexagonal structure arises because water molecules bond in a way that allows for the most efficient close packing, leading to the formation of six-sided ice crystals [1]. This structure is retained throughout the growth of the snowflake, even as environmental conditions change [4][5].
````

---

## s0150-partial: What unit do professional astronomers mostly use instead of the light-year, and how many light-years is that unit equal to?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
Professional astronomers most commonly use the parsec (pc) instead of the light-year [2]. The sources do not provide the number of light-years equivalent to one parsec.
````

---

## s0216-gen: Do phones store an actual image of my fingerprint?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
No, phones usually do not store an actual image of your fingerprint. Most phones store encrypted mathematical representations instead of real fingerprint images [1]. This means the data is transformed into a unique numeric code for security and privacy [4]. The actual image is not saved in a readable form on the device.
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

## s0273-partial: What is a carbon footprint, and how does carbon offsetting work?

Answerable: True

Problems:
- only 67% of sentences cited

Answer:

````text
A carbon footprint is defined as the total amount of greenhouse gases, such as carbon dioxide (CO2), methane (CH4), nitrous oxide (N2O), and hydrofluorocarbons (HFCs), emitted into the atmosphere, expressed in equivalent tons of CO2, associated with an individual, community, organization, product, service, or event [1][3]. It represents the total amount of greenhouse gases released into the atmosphere as a result of everyday activities like transportation, energy use, diet, and consumption [5]. However, the sources do not explain how carbon offsetting works.
````

---

## s0295-gen: How does adaptive cruise control work?

Answerable: True

Problems:
- low groundedness 59% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Adaptive cruise control works by using a radar sensor in the front of the car to detect traffic ahead and lock onto the vehicle in front [2]. The system then automatically adjusts the speed to maintain a safe distance, slowing down when approaching the vehicle ahead and accelerating when traffic allows [3]. It continuously monitors the vehicle in front and maintains a predetermined following distance [4]. Some advanced systems can also include automatic braking and forward collision warning features [4].
````

---

## s0301-gen: Does the keystone support all the weight of an arch bridge?

Answerable: True

Problems:
- only 75% of sentences cited

Answer:

````text
No, the keystone does not support all the weight of an arch bridge. The completed arch shares the force through the entire ring of voussoirs and transfers it into the supports; the keystone helps close the masonry arch but is not a single load-bearing element carrying everything by itself [3][4]. This misconception is common but misleading when taken literally [3]. Engineers understand that the load is distributed across the entire arch structure, not concentrated on the keystone [4].
````

---

## s0334-gen: Do sunk costs count in opportunity cost?

Answerable: True

Problems:
- only 75% of sentences cited

Answer:

````text
No, sunk costs do not count in opportunity cost because money already spent and unrecoverable cannot be regained by any choice available now. Only the next-best alternative you can still choose belongs in the calculation [2]. This principle applies regardless of whether the cost is monetary or in terms of time or other resources [5]. Sunk costs are irrelevant to future decisions since they cannot be altered by current choices [2].
````

---

## s0351-partial: What are the 4 P's of marketing, and how should a business decide what price to charge?

Answerable: True

Problems:
- only 67% of sentences cited

Answer:

````text
The 4 P's of marketing are product, price, place, and promotion strategy [5]. Price matters in marketing because it shapes how customers see your brand [5]. The sources do not contain information on how a business should decide what price to charge.
````

---

## s0385-gen: Why was Canberra chosen as Australia's capital instead of Sydney or Melbourne?

Answerable: True

Problems:
- low groundedness 56% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Canberra was chosen as Australia's capital as a compromise between Melbourne and Sydney, which were the two main contenders due to political rivalries between the colonies [5]. The decision to construct a new city rather than select one of the existing cities was made to avoid the conflict and provide a neutral location [2]. The site was selected in 1908, and the city was designed to serve as a fair and balanced capital for the new Commonwealth [2]. This compromise ensured that neither Sydney nor Melbourne held a dominant position as the capital [5]. Canberra's central location in the Australian Capital Territory also made it accessible to both major cities [4].
````

---

## s0448-hard_neg: How were participants in the Stanford Prison Experiment assigned to be prisoners or guards?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- only 25% of sentences cited

Answer:

````text
Participants in the Stanford Prison Experiment were assigned to be prisoners or guards through a classified ad placed in the “help wanted” section of the Palo Alto Times, which read: “Male college students needed for psychological study of prison life. $15 per day for 1-2 weeks beginning Aug. 15. For further information & applications, come to Room 248, Jordan Hall, Stanford U.” [3] The students who responded to the ad were then selected and randomly assigned to either the prisoner or guard roles [3].
````

---

## s0462-gen: How does a circuit breaker cut off a circuit when it trips?

Answerable: True

Problems:
- low groundedness 58% (possible outside knowledge or heavy paraphrase)

Answer:

````text
A circuit breaker cuts off a circuit by detecting abnormalities in electrical flow and using an internal spring mechanism to deactivate the circuit by force [3]. This action interrupts the electrical connection to prevent electrical accidents and damage [1]. The mechanism is designed to respond to excessive current or voltage, which results from conditions like overloads or short circuits [3]. When the breaker trips, it physically breaks the circuit to stop the flow of electricity [1]. This process prevents potential fires or equipment damage [2].
````

---

## s0462-partial: What is a ground fault, and how can you test for one?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
A ground fault occurs when electricity finds an unintended path to ground [5]. The sources do not explain how to test for a ground fault.
````

---

## s0462-seed: Why do circuit breakers trip?

Answerable: True

Problems:
- too long: 6 sentences (limit 5)

Answer:

````text
Circuit breakers trip to prevent electrical accidents and damage by cutting off power when abnormalities are detected in a circuit [1]. Common causes include overloaded circuits, short circuits, ground faults, and appliance malfunctions [5]. An overloaded circuit occurs when too many devices draw power simultaneously, exceeding the circuit’s capacity [2][5]. A short circuit happens when a hot wire comes into contact with a neutral wire, causing a surge of electricity [2]. Ground faults occur when electricity finds an unintended path to ground [5]. These conditions trigger the breaker’s protective mechanisms, which then interrupt the electrical flow [5].
````
