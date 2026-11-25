# Review: qwen3.5-0.8b (test-v2-0shot)

79 of 114 answers flagged. Full prompts are in `prompts.md`, raw data in `answers.jsonl`.

| Problem | Count |
|---|---|
| no citations | 71 |
| low groundedness | 11 |
| wrong answer/refuse decision | 7 |
| some sentences uncited | 6 |
| off-topic answer | 1 |

---

## s0004-gen: What warning signs might appear a day or two before a migraine?

Answerable: True

Problems:
- no citations

Answer:

````text
According to the Mayo Clinic source, a day or two before a migraine, one might notice subtle changes such as constipation, mood shifts (from depression to elation), food cravings, neck stiffness, increased urination, fluid retention, and frequent yawning.
````

---

## s0004-seed: What causes migraines and how are they treated?

Answerable: True

Problems:
- no citations
- low groundedness 55% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Migraines are primarily caused by imbalances in brain chemicals, specifically a drop in serotonin and a malfunctioning trigeminal nerve that transmits pain signals to the brain. While doctors believe these chemical imbalances play a key role, they are not entirely sure of the exact cause. Treatment for migraines involves various methods, including lifestyle changes, medication, and behavioral adjustments, though the specific regimen depends on the individual's condition and history.
````

---

## s0039-gen: When was REM sleep first discovered and how did it get its name?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
According to source [2], REM sleep was first discovered in the 1950s when scientists studying sleeping infants noticed distinct periods when their eyes darted quickly from side to side behind closed eyelids. This rapid eye movement earned the sleep stage its name.
````

---

## s0039-partial: How does REM sleep change over the course of the night, and what percentage of total sleep is spent in REM?

Answerable: True

Problems:
- no citations

Answer:

````text
REM sleep changes over the course of the night by becoming longer and more organized toward the morning, reflecting the brain's circadian timing system and sleep-regulating mechanisms. According to the sources, REM sleep is not evenly distributed throughout the night; early sleep contains relatively more deep NREM sleep, while REM episodes generally become longer toward morning.
````

---

## s0039-seed: What happens in the brain during REM sleep?

Answerable: True

Problems:
- no citations

Answer:

````text
During REM sleep, the brain activity ramps up significantly, often leading to vivid dreaming, while most of the body's muscles become temporarily paralyzed. This intense activity is accompanied by rapid eye movements (REM sleep) and a noticeable increase in pulse and breathing.
````

---

## s0047-gen: How does eating a lot of saturated fat affect LDL cholesterol?

Answerable: True

Problems:
- no citations

Answer:

````text
Eating a lot of saturated fat can slow the rate at which LDL particles are cleared from the bloodstream, leaving more circulating in the blood where they contribute to arterial plaque.
````

---

## s0047-hard_neg: How much saturated fat should adults limit themselves to each day?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- only 50% of sentences cited
- low groundedness 33% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The sources provided do not contain a specific numerical limit for how much saturated fat adults should limit themselves to each day. While sources [1], [2], [3], [4], and [5] discuss the health impacts of saturated fat, they do not define a specific daily intake threshold for adults.
````

---

## s0047-seed: What is the difference between saturated and unsaturated fats?

Answerable: True

Problems:
- no citations

Answer:

````text
Saturated fats are characterized by straight carbon chains with no double bonds, which allows them to pack tightly and remain solid at room temperature, whereas unsaturated fats contain one or more double bonds that create kinks, keeping them liquid.
````

---

## s0080-gen: How does parasitism differ from predation?

Answerable: True

Problems:
- no citations

Answer:

````text
Parasitism differs from predation because parasitism involves a benefit to the parasite at the expense of the host, whereas predation typically involves the host being killed and consumed by the predator.
````

---

## s0099-hard_neg: Does reducing tillage help prevent soil erosion?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- only 50% of sentences cited
- low groundedness 42% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The provided sources do not contain information regarding the specific effects of reducing tillage on soil erosion. While sources [1] and [2] mention that terraced farming and agroforestry can help prevent erosion, and sources [3] and [4] discuss the economic and environmental impacts of soil erosion, none of them address the mechanism or benefits of reducing tillage.
````

---

## s0099-partial: How do terraces help prevent soil erosion, and how should farmers build them?

Answerable: True

Problems:
- low groundedness 59% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Terraced farming prevents soil erosion by creating flat surfaces that stop wind and water from washing away topsoil, allowing water to flow more efficiently to crops [1]. Farmers should build these terraces by implementing full crop cover to keep the soil in place and utilizing intercropping systems to manage the land effectively [1].
````

---

## s0099-seed: What is soil erosion and how can farmers prevent it?

Answerable: True

Problems:
- no citations

Answer:

````text
Soil erosion is the process where topsoil is stripped away by wind and water, leading to reduced soil fertility, decreased crop yields, and environmental damage. Farmers can prevent this by implementing terraced farming, intercropping, and agroforestry systems that maintain soil cover and organic matter, while also offering incentives to make these practices financially viable for smallholders.
````

---

## s0109-gen: Why are Old Faithful's eruptions so predictable?

Answerable: True

Problems:
- no citations

Answer:

````text
Old Faithful's eruptions are predictable because their eruptions occur every 60 to 110 minutes, making it one of the most reliable geothermal features in Yellowstone. This regularity is attributed to the relatively simple plumbing system beneath the geyser, which allows for more consistent pressure build-up and release compared to other geysers with complex networks of channels.
````

---

## s0109-seed: How do geysers like Old Faithful work?

Answerable: True

Problems:
- no citations

Answer:

````text
Geysers like Old Faithful work by utilizing groundwater that seeps down through cracks in the Earth's surface and is heated by magma, causing the water to expand and pressurize until it forces its way out through narrow vents.
````

---

## s0128-gen: How does a snowflake start to form?

Answerable: True

Problems:
- no citations

Answer:

````text
Snowflakes begin their existence as a single mote of dust in the atmosphere, where water vapor condenses into microscopic ice crystals. These crystals then grow independently in all directions, eventually developing into the intricate six-sided shapes we observe.
````

---

## s0128-seed: Why do snowflakes have six sides?

Answerable: True

Problems:
- no citations

Answer:

````text
Snowflakes possess six-sided symmetry because the shape of the water molecules is inherently hexagonal, and the environment where they grow creates conditions that favor this specific molecular arrangement.
````

---

## s0150-gen: How long does it take sunlight to reach Earth?

Answerable: True

Problems:
- no citations

Answer:

````text
Light takes approximately 8.3 minutes to travel from the Sun to Earth.
````

---

## s0150-partial: What unit do professional astronomers mostly use instead of the light-year, and how many light-years is that unit equal to?

Answerable: True

Problems:
- no citations

Answer:

````text
Professional astronomers mostly use the parsec (pc) instead of the light-year. One parsec is approximately equal to 3.26156 light-years.
````

---

## s0150-seed: How long is a light-year in kilometres?

Answerable: True

Problems:
- no citations

Answer:

````text
A light-year is approximately 9.46 trillion kilometers.
````

---

## s0167-gen: Who discovered quantum entanglement?

Answerable: True

Problems:
- OFF-TOPIC: answer shares no key words with the question (copied example or wrong passage?)

Answer:

````text
According to source [2], Albert Einstein, Boris Podolsky, and Nathan Rosen described the phenomenon in their 1935 EPR paper.
````

---

## s0167-hard_neg: Who received the 2022 Nobel Prize in Physics for work on quantum entanglement?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- only 50% of sentences cited
- low groundedness 47% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The sources provided do not contain the answer to this question. While sources [1], [2], [3], [4], and [5] discuss quantum entanglement, its history, the 2022 Nobel Prize in Physics, and the recipients of that specific prize are not mentioned in the provided text.
````

---

## s0167-seed: What is quantum entanglement in simple terms?

Answerable: True

Problems:
- no citations

Answer:

````text
Quantum entanglement creates a correlation between particles where measuring one instantly determines the measurement outcome of another, regardless of distance, even before they interact. This phenomenon occurs when particles exist in a shared quantum state where their properties are linked, making it impossible to know the state of one without affecting the other.
````

---

## s0193-gen: What is the difference between Avogadro's number and the Avogadro constant?

Answerable: True

Problems:
- no citations

Answer:

````text
The sources indicate that while the numerical value of Avogadro's number is identical to the Avogadro constant, they represent distinct concepts: the Avogadro number is the specific count of particles in one mole, whereas the Avogadro constant is the physical constant with units (mol⁻¹) that defines the mole.
````

---

## s0193-seed: What is Avogadro's number used for in chemistry?

Answerable: True

Problems:
- no citations

Answer:

````text
Avogadro's number is primarily used as a proportionality factor that links the number of particles in a substance to the amount of matter in moles, enabling chemists to convert between microscopic quantities and macroscopic amounts. It also relates particle counts to mass or volume and interprets mole ratios in chemical equations.
````

---

## s0216-gen: Do phones store an actual image of my fingerprint?

Answerable: True

Problems:
- no citations

Answer:

````text
Phones generally do not store an actual image of your fingerprint; instead, they store encrypted mathematical representations of the unique ridge patterns.
````

---

## s0216-partial: How do ultrasonic fingerprint sensors work, and which phone was the first to use one?

Answerable: True

Problems:
- no citations
- low groundedness 46% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Ultrasonic fingerprint sensors operate by emitting a high-frequency sound wave that reflects off the ridges of the fingerprint, allowing the device to detect the 3D shape of the print. According to the sources, the first phone to use an ultrasonic fingerprint scanner was the Samsung Galaxy S3, which was released in 2011.
````

---

## s0216-seed: How do fingerprint scanners on phones work?

Answerable: True

Problems:
- no citations

Answer:

````text
Smartphone fingerprint scanners utilize optical, capacitive, or ultrasonic technologies to capture and compare unique ridge patterns on a finger. Optical scanners rely on capturing an image of the fingerprint and analyzing light and dark areas to detect ridges, while capacitive and ultrasonic scanners use electrical or sound signals to measure the 3D shape of the ridges. These sensors are designed to function through the phone screen and can be used for mobile payments or access control systems.
````

---

## s0230-gen: What was Alan Turing convicted of in 1952, and what was his sentence?

Answerable: True

Problems:
- no citations

Answer:

````text
Alan Turing was convicted of "gross indecency" in 1952, and he was sentenced to 12 months' probation conditional on undergoing chemical castration via organotherapy.
````

---

## s0230-seed: Who was Alan Turing and what did he contribute to computing?

Answerable: True

Problems:
- no citations
- low groundedness 24% (possible outside knowledge or heavy paraphrase)

Answer:

````text
Alan Turing was a British mathematician and computer scientist who made significant contributions to the field of computing, including the development of the first programmable electronic computer, the ENIAC, and the development of the Turing machine.
````

---

## s0241-gen: What can still be seen about your browsing when a website uses HTTPS?

Answerable: True

Problems:
- no citations

Answer:

````text
The sources indicate that while HTTPS encrypts the connection and protects data, website owners and ISPs can still see what users do on their site and which websites they visit.
````

---

## s0241-seed: How does HTTPS keep websites secure?

Answerable: True

Problems:
- no citations

Answer:

````text
HTTPS keeps websites secure by encrypting data in transit using SSL/TLS encryption, which prevents hackers from intercepting sensitive information like passwords and payment details. Additionally, the protocol verifies the website's identity through a TLS certificate issued by trusted Certificate Authorities (CAs), ensuring that only legitimate websites are accessed.
````

---

## s0273-gen: How much carbon dioxide does the average person produce each year?

Answerable: True

Problems:
- no citations

Answer:

````text
According to the sources, the average person produces about four tons of carbon dioxide each year.
````

---

## s0273-partial: What is a carbon footprint, and how does carbon offsetting work?

Answerable: True

Problems:
- no citations

Answer:

````text
A carbon footprint is defined as the total amount of greenhouse gases emitted into the atmosphere, such as carbon dioxide and methane, associated with an individual, product, or event. Carbon offsetting works by purchasing or donating carbon credits to reduce the amount of carbon dioxide released into the atmosphere, thereby balancing the emissions and helping to limit global warming.
````

---

## s0273-seed: What is a carbon footprint?

Answerable: True

Problems:
- no citations

Answer:

````text
A carbon footprint is defined as the total amount of greenhouse gases emitted into the atmosphere, such as carbon dioxide and methane, associated with an individual, community, or product. It represents the environmental impact of daily activities, including transportation, household consumption, and manufacturing processes.
````

---

## s0295-gen: How does adaptive cruise control work?

Answerable: True

Problems:
- no citations

Answer:

````text
Adaptive cruise control improves upon conventional systems by not only maintaining a preset speed but also automatically keeping a safe distance between the vehicle and the car in front of it. This is achieved using forward-pointed sensors, cameras, or both, which monitor the following vehicle while the system maintains the set speed.
````

---

## s0295-seed: How does cruise control work in a car?

Answerable: True

Problems:
- no citations

Answer:

````text
Cruise control maintains a predetermined speed automatically by using a computer to control throttle input, relieving the driver of the responsibility for speed adjustment. It can be turned off by pressing the brake pedal or clutch, and it is generally not harmful to the engine but may reduce fuel efficiency and wear benefits depending on driving conditions.
````

---

## s0301-gen: Does the keystone support all the weight of an arch bridge?

Answerable: True

Problems:
- only 50% of sentences cited

Answer:

````text
No, the keystone does not support all the weight of an arch bridge. According to source [3], the completed arch transfers force through the entire ring of voussoirs into the supports, whereas the keystone helps close a masonry arch but does not carry the entire load.
````

---

## s0301-seed: How do arch bridges support heavy loads?

Answerable: True

Problems:
- no citations

Answer:

````text
Arch bridges support heavy loads by utilizing the effective load distribution inherent to their curved geometry, which transfers the weight outward along the arch's curve to the supports at both ends. This mechanism allows the bridge to carry heavy loads and span large distances without the need for additional support in the middle.
````

---

## s0334-gen: Do sunk costs count in opportunity cost?

Answerable: True

Problems:
- no citations

Answer:

````text
Sunk costs do not count in opportunity cost because money already spent and unrecoverable cannot be regained by any choice available now. Only the next-best alternative you can still choose belongs in the calculation.
````

---

## s0334-hard_neg: Who developed the concept of opportunity cost?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- only 25% of sentences cited
- low groundedness 13% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The provided sources do not explicitly state the name of the individual who developed the concept of opportunity cost. While sources [1], [2], [3], [4], and [5] define the concept and discuss its application in economics, they do not mention the originator of the theory. Therefore, the answer is not contained within the text.

The sources do not contain the answer.
````

---

## s0334-seed: What is opportunity cost in economics?

Answerable: True

Problems:
- no citations

Answer:

````text
Opportunity cost is defined as the value of the next best alternative that is given up when a choice is made, representing the real cost of a decision.
````

---

## s0351-gen: What are some common types of advertising?

Answerable: True

Problems:
- no citations

Answer:

````text
According to the sources, common types of advertising include contextual ads in search engines, banners on websites, promotional videos, and sponsored content. Additionally, mobile advertising encompasses automated dialers, app download banners, and click-to-call ads. Outdoor advertising refers to billboards, banners on buildings, and branded vehicles placed in heavily trafficked areas.
````

---

## s0351-hard_neg: How does the American Marketing Association define marketing?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- no citations
- low groundedness 20% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The American Marketing Association does not provide a specific definition for "marketing" in its official publications or documents.
````

---

## s0351-partial: What are the 4 P's of marketing, and how should a business decide what price to charge?

Answerable: True

Problems:
- no citations

Answer:

````text
According to the sources, the 4 P's of marketing are Product, Price, Place, and Promotion. A business should decide what price to charge by considering how much it charges for its product, which shapes how customers perceive the brand, where the target audience goes to find information about the product, and how customers discover it.
````

---

## s0351-seed: What is the difference between marketing and advertising?

Answerable: True

Problems:
- no citations

Answer:

````text
Marketing and advertising serve distinct purposes in an organization's efforts to drive sales and engage customers, with marketing determining the overall strategy and advertising deciding where, when, and how that message appears. While marketing encompasses the long-term plan for connecting with customers, advertising is simply one paid method within that broader plan.
````

---

## s0370-gen: How did the printing press help spread the Protestant Reformation?

Answerable: True

Problems:
- no citations

Answer:

````text
The printing press allowed Martin Luther to disseminate his 95 Theses and pamphlets across Germany within two weeks, creating a speed of ideological spread impossible before mass production. This rapid distribution enabled reformist ideas to outrun Catholic Church suppression and transformed European printing specifically into a scalable process that made the Protestant Reformation structurally possible.
````

---

## s0370-hard_neg: How did the printing press affect the use of Latin as a scholarly language?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- no citations
- low groundedness 39% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The printing press fundamentally altered the use of Latin by enabling the rapid dissemination of theological and philosophical works, such as Martin Luther's 95 Theses, which allowed reformist ideas to spread across Europe within two months rather than years. This technological shift facilitated the Protestant Reformation, transforming the scholarly landscape by making complex religious texts accessible to a broader audience and challenging the traditional Catholic monopoly on knowledge.
````

---

## s0370-seed: How did the printing press change Europe?

Answerable: True

Problems:
- no citations
- low groundedness 55% (possible outside knowledge or heavy paraphrase)

Answer:

````text
The printing press fundamentally transformed Europe by enabling the rapid, large-scale production of books, which drastically lowered costs and accelerated the spread of ideas. This technological shift allowed for the Protestant Reformation to begin within two months of Martin Luther's 95 Theses, a speed that was historically impossible before mass printing. Furthermore, the invention of movable type allowed for the creation of the Gutenberg Bible, a masterpiece that survived over 49 years, demonstrating the press's ability to produce high-quality works efficiently.
````

---

## s0385-gen: Why was Canberra chosen as Australia's capital instead of Sydney or Melbourne?

Answerable: True

Problems:
- no citations

Answer:

````text
Canberra was chosen as Australia's capital instead of Sydney or Melbourne because the two major cities were politically rivals, necessitating a compromise to select a single capital city for the new Commonwealth.
````

---

## s0385-seed: What is the capital of Australia?

Answerable: True

Problems:
- no citations

Answer:

````text
The capital of Australia is Canberra, which serves as the seat of the Federation of Australia and has been in place since 1913.
````

---

## s0415-gen: What role did the chorus play in Greek theatre?

Answerable: True

Problems:
- no citations

Answer:

````text
The chorus acted as a collective character, providing commentary, context, and reflections on the events of the play through song and dance.
````

---

## s0415-seed: How did ancient Greek theatre work?

Answerable: True

Problems:
- no citations

Answer:

````text
Ancient Greek theatre functioned as a system that combined architecture, performance, and audience to create a controlled and shared experience, allowing ideas and behaviors to be presented collectively in a public setting.
````

---

## s0425-gen: What were the Cotswold Olimpick Games?

Answerable: True

Problems:
- no citations

Answer:

````text
The Cotswold Olimpick Games were an annual meeting near Chipping Campden, England, organized by the British Olympic Association between 1612 and 1642. They were described as the first stirrings of Britain's Olympic beginnings and were organized by Robert Dover, who later cited them as the first modern Olympic Games.
````

---

## s0425-seed: When were the first modern Olympic Games held?

Answerable: True

Problems:
- no citations

Answer:

````text
The first modern Olympic Games were held in Athens, Greece, in 1896.
````

---

## s0448-gen: Why did Zimbardo end the Stanford Prison Experiment early?

Answerable: True

Problems:
- no citations

Answer:

````text
Zimbardo terminated the experiment early due to ethical concerns regarding the severe distress and abuse experienced by participants, particularly when they demanded to be released from the simulated prison environment. Although he had not initially stopped the study, he was aware of the escalating issues and was only forced to end it after external observer Christina Maslach raised concerns about the participants' well-being.
````

---

## s0448-hard_neg: How were participants in the Stanford Prison Experiment assigned to be prisoners or guards?

Answerable: False

Problems:
- WRONG DECISION: answered an unanswerable question
- no citations

Answer:

````text
Participants were assigned to be prisoners or guards by being placed in a simulated prison environment at Stanford University, where they were subjected to a role-playing scenario designed to test their conformity and behavior under the influence of power dynamics.
````

---

## s0448-seed: What was the Stanford prison experiment?

Answerable: True

Problems:
- no citations

Answer:

````text
The Stanford Prison Experiment was a psychological study conducted by Philip Zimbardo at Stanford University in 1971 where he created a simulated prison environment to observe how individuals would conform to roles of prisoner or guard. The study revealed that the experiment's results were heavily influenced by situational factors and power dynamics rather than inherent personality traits, leading to the early termination of the research due to ethical concerns.
````

---

## s0462-partial: What is a ground fault, and how can you test for one?

Answerable: True

Problems:
- no citations

Answer:

````text
Ground faults occur when electricity finds an unintended path to ground, causing a surge of current that triggers the breaker to trip. To test for a ground fault, you can use a multimeter to check for a high voltage reading across the ground wire, or use a grounded test tool to detect a voltage spike on the ground wire itself.
````

---

## s0462-seed: Why do circuit breakers trip?

Answerable: True

Problems:
- no citations

Answer:

````text
Circuit breakers trip when electrical currents exceed the circuit's capacity, typically due to overloads, ground faults, or other issues that trigger protective mechanisms to prevent electrical accidents.
````

---

## q003: What is the difference between weather and climate?

Answerable: True

Problems:
- no citations

Answer:

````text
Weather refers to short-term changes in the atmosphere, while climate refers to atmospheric changes over longer periods of time, typically defined as 30 years or more.
````

---

## q016: What causes inflation in an economy?

Answerable: True

Problems:
- no citations

Answer:

````text
Inflation is the sustained rise in the general level of prices of goods and services, primarily driven by demand-pull inflation when growing demand outstrips supply, and cost-push inflation when production or input costs rise.
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
- no citations

Answer:

````text
Caffeine primarily works by blocking adenosine receptors, which are natural signals that promote sleepiness and reduce neural activity. By interfering with this process, caffeine can temporarily enhance alertness, focus, and cognitive performance, though its effects are variable and depend on individual factors like sleep habits and dosage.
````

---

## q005: What are the main symptoms of type 2 diabetes?

Answerable: True

Problems:
- no citations

Answer:

````text
Type 2 diabetes is characterized by a lack of insulin production or a failure to respond to it, leading to elevated blood sugar levels. The primary symptoms include increased thirst, frequent urination, fatigue, and weight loss. These symptoms often develop gradually, typically starting in adults over 45, though they can also appear in younger individuals.
````

---

## q000: What causes sleep apnea?

Answerable: True

Problems:
- no citations

Answer:

````text
Sleep apnea is primarily caused by conditions that block airflow through the upper airway during sleep, such as obesity, a stuffy nose, or anatomical anomalies in the face and neck. Central sleep apnea occurs when the brain fails to send the right signals to control breathing, often due to medical conditions affecting the brain and heart. While both types stem from physical or medical factors, the specific cause depends on the type of sleep apnea and the individual's age and lifestyle habits.
````

---

## q009: What causes the seasons on Earth?

Answerable: True

Problems:
- no citations

Answer:

````text
The seasons on Earth are primarily caused by the planet's axial tilt, which is approximately 23.5 degrees relative to its orbital plane. This tilt causes different hemispheres to receive varying amounts of sunlight throughout the year, resulting in the distinct weather patterns we experience.
````

---

## q023: How does a refrigerator keep food cold?

Answerable: True

Problems:
- no citations

Answer:

````text
A refrigerator keeps food cold by continuously transferring heat from its insulated interior to the surrounding room through a complex refrigeration cycle. This process relies on a circulating refrigerant that absorbs heat inside the appliance and releases it outside via coils, a compressor, and an expansion device. By removing heat from the food, the appliance slows down microbial growth and chemical reactions, ensuring the food remains safe and fresh.
````

---

## q021: How do solar panels generate electricity?

Answerable: True

Problems:
- no citations

Answer:

````text
Solar panels generate electricity through the photovoltaic effect, where sunlight excites electrons in silicon cells to create direct current (DC) power. This DC electricity is then converted into alternating current (AC) by an inverter, enabling homes and businesses to use the energy.
````

---

## q020: What is the greenhouse effect?

Answerable: True

Problems:
- no citations

Answer:

````text
The greenhouse effect is the process through which heat is trapped near Earth's surface by substances known as 'greenhouse gases,' helping to maintain a warmer temperature than it would otherwise. This phenomenon occurs when certain gases absorb infrared radiation from the sun and keep the planet's temperature within a range suitable for life, as seen in the atmosphere where sunlight passes through while heat is reflected back into the atmosphere.
````

---

## q004: How does a heat pump work?

Answerable: True

Problems:
- no citations

Answer:

````text
Heat pumps transfer heat from one place to another using electricity and a refrigerant cycle, operating by reversing the direction of the refrigerant flow to move heat between indoor and outdoor air sources.
````

---

## q006: How do lithium-ion batteries degrade over time?

Answerable: True

Problems:
- no citations

Answer:

````text
Lithium-ion batteries degrade over time due to a combination of chemical and mechanical processes, including the growth of the solid electrolyte interphase (SEI), lithium plating, cathode dissolution, and physical stress from expansion and contraction. These mechanisms contribute to a reduction in a cell's performance and capacity, and the primary accelerants for this degradation are high voltage (charging to 100%), high temperature, and high charge/discharge rates.
````

---

## q022: What causes earthquakes?

Answerable: True

Problems:
- no citations

Answer:

````text
Earthquakes are caused by the sudden release of built-up stress in the Earth's crust, typically along faults or at the boundaries of tectonic plates. This stress release sends seismic waves radiating from the point of rupture, traveling through the Earth and shaking the ground. The location within the Earth where the rupture begins is called the focus or hypocenter, and the point directly above the focus on the surface is the epicenter.
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

## q017: How do coral reefs form?

Answerable: True

Problems:
- no citations

Answer:

````text
Coral reefs form when free-swimming coral larvae attach to submerged rocks or hard surfaces along the edges of islands or continents, where they grow and expand to create structures ranging from fringing barriers to atolls.
````

---

## q018: What is the purpose of a VPN?

Answerable: True

Problems:
- no citations

Answer:

````text
A VPN serves as a security tool that encrypts your internet connection and hides your IP address, making it significantly harder for your ISP, advertisers, governments, or hackers to track what you do online. By routing your traffic through a private server in a location of your choice, the server masks your real IP address and wraps your data in encryption, ensuring that even if someone intercepts your connection, they cannot read it.
````

---

## q010: How does photosynthesis convert light into energy?

Answerable: True

Problems:
- no citations

Answer:

````text
Photosynthesis converts light energy into chemical energy by utilizing chlorophyll pigments to capture photons and drive the splitting of water molecules, which releases oxygen and generates chemical fuel. This process occurs in two distinct stages: the first stage involves light-dependent reactions that capture light energy to produce ATP and NADPH, while the second stage uses these products to fix carbon dioxide into sugars.
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
The BM25 ranking function scores documents by calculating a numerical score based on the occurrences of query terms within the document, where each term's contribution is scaled by its inverse document frequency (IDF) and normalized by the document's length. This process involves multiplying the frequency of a term by its rarity factor and adding the results for all terms in the query, with the final score being the sum of these individual contributions.
````

---

## q014: Why do onions make people cry?

Answerable: True

Problems:
- no citations

Answer:

````text
Onions make people cry due to the formation of a volatile chemical compound called lachrymatory factor, which is released when the onion's cells are damaged during cutting. This irritant travels through the air and triggers the eyes to produce tears. To prevent this, one should use a sharp knife to avoid crushing the onion, chill the onion in a bowl of ice water before cutting, and avoid cutting near the root end where the sulfuric acid compounds are highest concentrated.
````
