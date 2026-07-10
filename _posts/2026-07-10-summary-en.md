---
layout: default
title: "Horizon Summary: 2026-07-10 (EN)"
date: 2026-07-10
lang: en
---

> From 38 items, 10 important content pieces were selected

---

1. [EU Parliament Passes Chat Control 1.0](#item-1) ⭐️ 9.0/10
2. [OpenAI Releases GPT-5.6 with Three Sizes](#item-2) ⭐️ 9.0/10
3. [TypeScript 7.0 Released with Go Rewrite, Up to 12x Faster](#item-3) ⭐️ 9.0/10
4. [Ant Group Open-Sources LingBot-Video, First MoE Embodied Video Model](#item-4) ⭐️ 9.0/10
5. [Postgres rewritten in Rust passes 100% regression tests](#item-5) ⭐️ 8.0/10
6. [Meta Launches Muse Spark 1.1 Agentic AI Model](#item-6) ⭐️ 8.0/10
7. [Meta Superintelligence Progress: RL Startup, Compute Ramp](#item-7) ⭐️ 8.0/10
8. [DJI EV50 Flies Over Mount Everest at 8,861 Meters](#item-8) ⭐️ 8.0/10
9. [Zhengzhou Core Node of National Supercomputing Internet Launched](#item-9) ⭐️ 8.0/10
10. [OpenAI and US War Department Ban AI for Domestic Surveillance](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [EU Parliament Passes Chat Control 1.0](https://www.patrick-breyer.de/en/eu-parliament-greenlights-chat-control-1-0-breyer-our-children-lose-out/) ⭐️ 9.0/10

The EU Parliament passed Chat Control 1.0 on July 9, 2025, allowing mass scanning of private messages without a warrant, despite 314 MEPs voting against it, because the motion to reject failed to reach the required absolute majority of 361 votes. This decision marks a major shift in EU digital policy, enabling warrantless mass surveillance of private communications on platforms like Instagram, Discord, and Gmail, which threatens encryption and privacy rights for 450 million EU citizens. The regulation, also known as the Child Sexual Abuse Regulation (CSAR), was passed using a procedural tactic: a vote held just before summer break, with the default being acceptance unless an absolute majority of all MEPs voted to reject. The scanning permission is valid until 2028.

hackernews · rapnie · Jul 9, 11:03 · [Discussion](https://news.ycombinator.com/item?id=48843923)

**Background**: Chat Control is an EU regulation proposed in May 2022 aimed at combating child sexual abuse online by requiring platforms to scan private messages. Critics argue it undermines end-to-end encryption and privacy, as it allows scanning without judicial oversight. The Parliament had rejected similar measures twice in March 2025 before this vote.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://fightchatcontrol.eu/chat-control-overview">Chat Control 1.0 vs 2.0 - Fight Chat Control</a></li>
<li><a href="https://www.techtimes.com/articles/320010/20260709/eu-parliament-passes-chat-control-default-314-meps-couldnt-block-scanning-law.htm">EU Parliament Passes Chat Control by Default: 314 MEPs Couldn ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed outrage at the procedural manipulation, noting that the vote was scheduled just before summer break to reduce attendance, and that the default acceptance rule allowed passage despite majority opposition. Some warned this could erode trust in the EU as a democratic institution.

**Tags**: `#privacy`, `#EU regulation`, `#surveillance`, `#encryption`, `#digital rights`

---

<a id="item-2"></a>
## [OpenAI Releases GPT-5.6 with Three Sizes](https://openai.com/index/gpt-5-6/) ⭐️ 9.0/10

OpenAI released GPT-5.6, a new frontier model available in three sizes: Luna, Terra, and Sol, with Sol achieving a state-of-the-art score of 7.8% on the ARC-AGI-3 benchmark. GPT-5.6 is the first verified frontier model to beat an ARC-AGI-3 game, marking progress toward agentic intelligence and general reasoning. Its improved intent understanding and image handling could enhance developer workflows and user experiences. Pricing per 1M tokens is Luna $1/$6, Terra $2.50/$15, Sol $5/$30, comparable to Claude Opus and Fable 5. The model also introduces better intent understanding and preserves original image dimensions.

hackernews · logickkk1 · Jul 9, 17:04 · [Discussion](https://news.ycombinator.com/item?id=48849066)

**Background**: Frontier models are the most advanced general-purpose AI models, trained on massive computational budgets and capable of exceeding state-of-the-art across multiple domains. ARC-AGI-3 is an interactive benchmark that tests an agent's ability to explore, infer goals, and plan in novel environments without explicit instructions.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://arxiv.org/abs/2603.24621">ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence Announcing ARC-AGI-3 - ARC Prize ARC-AGI-3: The New Interactive Reasoning Benchmark - DataCamp GPT 5.6 Sol Tops ARC-AGI 3 With 7.8%, Becomes First Model To ... Exclusive: This new benchmark could expose AI’s biggest ...</a></li>
<li><a href="https://www.datacamp.com/blog/frontier-models">Frontier Models Explained: What Defines the Cutting Edge of AI | DataCamp</a></li>

</ul>
</details>

**Discussion**: Community comments highlight Sol's high cost due to subagent delegation, with some users noting it can be 'disastrously expensive.' Others compare GPT-5.6 to Claude Code and discuss the model's performance on benchmarks like GeneBench and LifeSciBench.

**Tags**: `#AI`, `#OpenAI`, `#GPT-5.6`, `#ARC-AGI`, `#LLM`

---

<a id="item-3"></a>
## [TypeScript 7.0 Released with Go Rewrite, Up to 12x Faster](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 9.0/10

Microsoft has officially released TypeScript 7.0, featuring a native compiler rewritten in Go that delivers 8-12x faster builds and supports shared-memory multi-threading. Users can install it via npm, and editors can use the new language server through LSP. This major performance improvement dramatically reduces build times for large TypeScript codebases, boosting developer productivity. The shift to Go also signals a new direction for TypeScript tooling, potentially influencing the broader JavaScript ecosystem. New --checkers and --builders flags allow customizing parallelism, and a compatibility package enables coexistence with TypeScript 6. However, embedded language toolchains like Vue and Svelte are not yet supported and must continue using the older version.

telegram · zaihuapd · Jul 9, 04:01

**Background**: TypeScript is a typed superset of JavaScript that compiles to plain JavaScript. The previous compiler was written in TypeScript itself, which could be slow on large projects. The Go rewrite leverages native performance and multi-threading to significantly speed up type-checking and compilation.

<details><summary>References</summary>
<ul>
<li><a href="https://betterstack.com/community/guides/scaling-nodejs/typescript-7-go-rewrite/">TypeScript 7.0: New Features and the Go-Powered Compiler Rewrite | Better Stack Community</a></li>
<li><a href="https://www.digitalapplied.com/blog/typescript-7-0-rc-go-native-compiler-2026-upgrade-guide">TypeScript 7.0 RC: The Go-Native Compiler Has Landed</a></li>

</ul>
</details>

**Tags**: `#TypeScript`, `#Microsoft`, `#compiler`, `#performance`, `#programming languages`

---

<a id="item-4"></a>
## [Ant Group Open-Sources LingBot-Video, First MoE Embodied Video Model](https://www.qbitai.com/2026/07/446458.html) ⭐️ 9.0/10

Ant Group's LingBot-Video, the world's first Mixture-of-Experts (MoE) based embodied video generation foundation model, has been open-sourced under the Apache 2.0 license. The model achieves 3x inference efficiency compared to dense models of similar scale, with 30B total parameters but only 3B activated during generation. This release significantly advances embodied AI by providing an efficient, open-source video foundation model tailored for robotics, enabling better action prediction, simulation data generation, and world model research. The MoE architecture reduces computational costs, making advanced embodied video generation more accessible to the research community. LingBot-Video uses a DiT+MoE design and was trained on a 70,000-hour embodied data engine covering dexterous manipulation, robot locomotion, and first-person interaction. It introduces a multi-dimensional reinforcement learning reward system focusing on physical plausibility and task completion, and scored 0.620 on the RBench benchmark, surpassing models like Wan2.6, Seedance1.5 Pro, and Cosmos3 Super.

telegram · zaihuapd · Jul 9, 04:30

**Background**: Mixture-of-Experts (MoE) is an AI architecture that uses multiple specialized submodels (experts) activated via a routing mechanism, enabling larger model capacity with lower inference cost. Embodied video generation models produce videos that capture perception, reasoning, and action in the physical world, crucial for robotics. DiT (Diffusion Transformer) combines diffusion models with transformer architectures for high-quality video generation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? - NVIDIA</a></li>
<li><a href="https://arxiv.org/abs/2601.15282">[2601.15282] Rethinking Video Generation Model for the Embodied World</a></li>

</ul>
</details>

**Tags**: `#MoE`, `#embodied AI`, `#video generation`, `#robotics`, `#open source`

---

<a id="item-5"></a>
## [Postgres rewritten in Rust passes 100% regression tests](https://github.com/malisper/pgrust) ⭐️ 8.0/10

A project called pgrust has rewritten PostgreSQL in Rust using LLMs, and now passes 100% of the official Postgres regression tests. The author is working on a new version incorporating additional techniques. This demonstrates the potential of LLMs for large-scale code rewriting and rearchitecting legacy systems, though it also raises questions about code quality, reviewability, and licensing. The project could influence future database development and AI-assisted software engineering. The project generated 7101 commits in less than a month, making traditional code review impractical. The license was changed from the PostgreSQL license to AGPL, which may raise compatibility concerns.

hackernews · SweetSoftPillow · Jul 9, 06:18 · [Discussion](https://news.ycombinator.com/item?id=48841676)

**Background**: PostgreSQL is a 30-year-old open-source relational database with a comprehensive regression test suite. Rust is a systems programming language known for memory safety and performance. LLMs (large language models) are AI models that can generate code, and their use for rewriting entire codebases is a novel approach.

<details><summary>References</summary>
<ul>
<li><a href="https://www.postgresql.org/docs/current/regress.html">PostgreSQL: Documentation: 18: Chapter 31. Regression Tests</a></li>
<li><a href="https://arxiv.org/abs/2505.16339">[2505.16339] Rethinking Code Review Workflows with LLM Assistance: An ...</a></li>

</ul>
</details>

**Discussion**: The community is impressed by the achievement but concerned about reviewability, with one comment noting that 7101 commits in a month makes traditional review infeasible. Others suggest testing approaches like mirroring queries to compare behavior. The license change to AGPL also sparked debate about compatibility with the original PostgreSQL license.

**Tags**: `#Postgres`, `#Rust`, `#LLM`, `#Database`, `#AI-assisted development`

---

<a id="item-6"></a>
## [Meta Launches Muse Spark 1.1 Agentic AI Model](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) ⭐️ 8.0/10

Meta has released Muse Spark 1.1, a multimodal reasoning model designed for agentic tasks, now available via API with a 1M-token context window and significant improvements in tool use, coding, and computer use. This release marks Meta's entry into the competitive agentic AI space, offering a frontier-tier model at aggressive pricing ($1.25/$4.5 per million tokens), potentially disrupting the market dominated by OpenAI and Anthropic. The model uses a multi-agent thinking approach for superior performance, but community members have questioned the validity of its Terminal-Bench 2.1 results due to resource cap overrides. Pricing includes $0.15 per million cached input tokens.

hackernews · ot · Jul 9, 14:10 · [Discussion](https://news.ycombinator.com/item?id=48846184)

**Background**: Agentic AI models are designed to autonomously perform tasks using tools, code, and computer interactions. Muse Spark 1.1 is built on Meta's Superintelligence Labs' research, following the earlier Muse Spark model, and is positioned as a competitor to models like GPT-5.4 and Claude Opus 4.6.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/">Introducing Muse Spark 1.1</a></li>
<li><a href="https://www.datacamp.com/blog/muse-spark-1-1">Muse Spark 1.1: Meta's Agentic Model and API | DataCamp</a></li>
<li><a href="https://llm-stats.com/models/muse-spark">Muse Spark Benchmarks, Pricing & Context Window</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: some praise the low pricing and open-weight strategy, while others criticize benchmark methodology and question whether Meta can sustain this approach. A developer created an LLM plugin for easy terminal access.

**Tags**: `#AI`, `#Meta`, `#agentic model`, `#open source`, `#benchmark`

---

<a id="item-7"></a>
## [Meta Superintelligence Progress: RL Startup, Compute Ramp](https://newsletter.semianalysis.com/p/the-future-of-meta-superintelligence) ⭐️ 8.0/10

Meta's superintelligence initiative has spawned a top-tier reinforcement learning environment startup, initiated the most aggressive compute ramp ever seen with 2000km+ scale-across networking, and offered strategic advice to Google DeepMind. These developments signal a major acceleration in AI infrastructure and RL research, potentially reshaping the competitive landscape among leading AI labs and driving new standards for distributed computing. The compute ramp involves scale-across networking connecting data centers over 2000km, a new paradigm beyond traditional scale-up and scale-out. The RL environment startup is described as 'top tier' and emerged rapidly.

rss · Semianalysis · Jul 9, 19:16

**Background**: Reinforcement learning environments are simulated worlds where AI agents learn through trial and error. Scale-across networking is a third pillar of AI computing that links geographically distributed data centers into a single supercomputer, enabling massive training clusters. Meta has been investing heavily in AI superintelligence, competing with Google DeepMind and OpenAI.

<details><summary>References</summary>
<ul>
<li><a href="https://alignlist.com/guides/top-40-rl-environments-startups-and-companies">Top 40 RL Environments Startups and Companies in 2026</a></li>
<li><a href="https://www.naddod.com/blog/a-complete-guide-to-scale-across-the-third-pillar-of-ai-computing">What Is Scale-Across? A Complete Guide to the “Third Pillar ...</a></li>
<li><a href="https://drivenets.com/blog/hybrid-scaling-scale-up-scale-out-and-scale-across-gain-new-meaning/">Scale-Up, Scale-Out, and Scale-Across Gain New Meaning</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Meta`, `#superintelligence`, `#reinforcement learning`, `#compute`

---

<a id="item-8"></a>
## [DJI EV50 Flies Over Mount Everest at 8,861 Meters](https://www.163.com/dy/article/L1CUCV940514R9OJ.html) ⭐️ 8.0/10

DJI's unreleased EV50 vertical takeoff and landing cargo drone successfully flew over Mount Everest at 8,861 meters, setting a world record for the highest flight altitude in its class and collecting atmospheric data above 8,000 meters. This achievement demonstrates DJI's technical leadership in high-altitude UAV operations and opens new possibilities for cargo delivery and scientific research in extreme environments. The data collected above 8,000 meters is valuable for atmospheric science and climate studies. The EV50 is a hybrid-wing drone that can take off and land vertically, then transition to fixed-wing cruise. During the 12-day mission, it completed 32 takeoffs and landings, climbed a cumulative 3,730 meters, and still had 30% battery remaining on return.

telegram · zaihuapd · Jul 9, 06:00

**Background**: The DJI EV50 is the company's first vertical takeoff and landing cargo drone, designed for long-range logistics. Hybrid-wing drones combine the vertical takeoff/landing capability of multirotors with the efficiency of fixed-wing aircraft, making them suitable for missions requiring both flexibility and range. Mount Everest's extreme altitude and thin air pose significant challenges for drone flight.

<details><summary>References</summary>
<ul>
<li><a href="https://newuas.com/newrelease/87777.html">大疆发布首款垂直起降运载无人机DJI EV50-NEWUAS</a></li>
<li><a href="https://finance.sina.com.cn/tech/discovery/2026-07-09/doc-inihfihu7575250.shtml">大疆发布首款垂直起降运载无人机DJI EV50：航程150公里 最大载重50千...</a></li>
<li><a href="https://news.qq.com/rain/a/20260709A03DQ700">大疆近期发布新款无人机机型DJI EV50 可随时起降又能百公里级飞行_腾...</a></li>

</ul>
</details>

**Tags**: `#DJI`, `#drone`, `#high-altitude`, `#UAV`, `#Mount Everest`

---

<a id="item-9"></a>
## [Zhengzhou Core Node of National Supercomputing Internet Launched](https://36kr.com/newsflashes/3887797387344387) ⭐️ 8.0/10

On July 9, 2026, the core node of China's National Supercomputing Internet was officially launched in Zhengzhou, providing over 100,000 domestic AI computing cards. This is the largest single pool of domestic AI computing resources connected to the platform since its launch. This milestone significantly boosts China's domestic AI computing capacity, reducing reliance on foreign chips and supporting large-scale AI model training. It strengthens national computing infrastructure for scientific research, industrial simulation, and digital economy development. The core node is responsible for operations management and resource scheduling across the national network, integrating supply-demand matching and industry incubation services. It was announced at the 2026 Henan Artificial Intelligence Conference.

telegram · zaihuapd · Jul 9, 07:00

**Background**: The National Supercomputing Internet is a project initiated by China's Ministry of Science and Technology to connect supercomputing centers nationwide into a unified computing network. It aims to enable efficient resource sharing and scheduling, supporting high-performance computing and AI applications. Domestic AI computing cards, such as Huawei Ascend and Cambricon, are developed by Chinese companies to replace foreign GPUs like NVIDIA's.

<details><summary>References</summary>
<ul>
<li><a href="https://www.scnet.cn/home/internet/index.html">超算互联网 - scnet.cn</a></li>
<li><a href="https://baike.baidu.com/item/国家超算互联网/62902938">国家超算互联网 - 百度百科 国家超算互联网 - 高性能计算服务与 AI 服务平台 - AIHub 超算互联网 - 百度百科 国家超算互联网平台上线 - 中国政府网 国家超算互联网用户规模破百万 - 中国政府网 国家超算互联网正式上线 DeepSeek，全民可用！国家队强势助力！</a></li>
<li><a href="https://baike.baidu.com/item/国产算力卡/67727675">国产算力卡 - 百度百科</a></li>

</ul>
</details>

**Tags**: `#supercomputing`, `#AI infrastructure`, `#China`, `#national computing`, `#domestic chips`

---

<a id="item-10"></a>
## [OpenAI and US War Department Ban AI for Domestic Surveillance](https://t.me/zaihuapd/42459) ⭐️ 8.0/10

OpenAI and the US Department of War have agreed to amend their AI cooperation contract to explicitly prohibit the use of AI systems for domestic surveillance of American citizens, a move proposed by OpenAI CEO Sam Altman. This sets a precedent for ethical AI use in government contracts, addressing public concerns about mass surveillance and potentially influencing future agreements between AI companies and defense agencies. The revised clauses specifically ban intentional surveillance of US citizens and prohibit tracking or monitoring using commercially obtained personally identifiable information; the agreement has not yet been formally signed.

telegram · zaihuapd · Jul 9, 13:22

**Background**: The US Department of War, formerly the Department of Defense, has been expanding AI partnerships with tech companies. Earlier, Anthropic's similar agreement with the department was suspended due to disputes over AI use in autonomous weapons and surveillance. OpenAI's proactive stance aims to differentiate itself by emphasizing safety and ethics.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/our-agreement-with-the-department-of-war/">Our agreement with the Department of War - OpenAI</a></li>
<li><a href="https://www.nytimes.com/2026/02/27/technology/openai-agreement-pentagon-ai.html">OpenAI Reaches A.I. Agreement With Defense Dept. After ...</a></li>
<li><a href="https://techcrunch.com/2026/02/28/openais-sam-altman-announces-pentagon-deal-with-technical-safeguards/">OpenAI’s Sam Altman announces Pentagon deal with ‘technical ...</a></li>

</ul>
</details>

**Tags**: `#AI Ethics`, `#Government Policy`, `#Surveillance`, `#OpenAI`

---