---
layout: default
title: "Horizon Summary: 2026-07-09 (EN)"
date: 2026-07-09
lang: en
---

> From 33 items, 13 important content pieces were selected

---

1. [EU Parliament Passes Chat Control 1.0, Allowing Warrantless Message Scanning](#item-1) ⭐️ 9.0/10
2. [TypeScript 7.0 Released with Go Rewrite, Up to 12x Faster](#item-2) ⭐️ 9.0/10
3. [Ant Group Open-Sources LingBot-Video, First MoE Embodied Video Model](#item-3) ⭐️ 9.0/10
4. [John Deere Owners Win Right to Repair in FTC Settlement](#item-4) ⭐️ 8.0/10
5. [xAI Releases Grok 4.5 with 4x Efficiency](#item-5) ⭐️ 8.0/10
6. [Microsoft Releases Flint, a Visualization Language for AI Agents](#item-6) ⭐️ 8.0/10
7. [OpenAI Analyzes Flaws in Coding Evaluations](#item-7) ⭐️ 8.0/10
8. [Bun Rewritten from Zig to Rust](#item-8) ⭐️ 8.0/10
9. [OpenAI Introduces GPT-Live Voice Mode with GPT-5.5 Delegation](#item-9) ⭐️ 8.0/10
10. [LineageOS Launches Web-Based Flashing Tool](#item-10) ⭐️ 8.0/10
11. [DJI EV50 Drone Flies to 8,861m on Everest](#item-11) ⭐️ 8.0/10
12. [National Supercomputing Internet Core Node Launches in Zhengzhou](#item-12) ⭐️ 8.0/10
13. [OpenAI and US War Department Revise AI Contract to Ban Citizen Surveillance](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [EU Parliament Passes Chat Control 1.0, Allowing Warrantless Message Scanning](https://www.patrick-breyer.de/en/eu-parliament-greenlights-chat-control-1-0-breyer-our-children-lose-out/) ⭐️ 9.0/10

On July 9, 2026, the European Parliament allowed Chat Control 1.0 to pass, permitting US tech companies to scan private messages without a warrant or prior suspicion, despite having rejected the measure twice in March. This legislation undermines end-to-end encryption and privacy rights, setting a precedent for mass surveillance that could affect all EU citizens and weaken trust in digital communications. The motion to reject the regulation failed to secure the required absolute majority of 361 votes, with 314 against, 276 in favor, 17 abstentions, and 113 absent; the scanning is now permitted until 2028.

hackernews · rapnie · Jul 9, 11:03 · [Discussion](https://news.ycombinator.com/item?id=48843923)

**Background**: Chat Control 1.0, formally the Child Sexual Abuse Regulation (CSAR), was proposed in May 2022 to combat child sexual abuse online by requiring platforms to scan all private communications. Critics argue that no current technology can detect such material without high error rates, leading to false positives and privacy violations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control_1.0">Chat Control 1.0</a></li>
<li><a href="https://www.patrick-breyer.de/en/eu-parliament-greenlights-chat-control-1-0-breyer-our-children-lose-out/">EU Parliament greenlights Chat Control 1.0 – Breyer: "Our children lose out"</a></li>

</ul>
</details>

**Discussion**: Commenters expressed outrage over the parliamentary procedure, noting that the vote was forced under urgency rules just before the summer break, with many MEPs absent. They highlighted that a majority of voting MEPs opposed the measure, but it passed due to the absolute majority requirement for rejection, calling it a democratic failure.

**Tags**: `#privacy`, `#EU legislation`, `#surveillance`, `#encryption`, `#civil liberties`

---

<a id="item-2"></a>
## [TypeScript 7.0 Released with Go Rewrite, Up to 12x Faster](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 9.0/10

Microsoft has officially released TypeScript 7.0, a native version rewritten in Go that achieves 8-12x faster full builds and supports shared-memory multithreading. Users can install it via npm, and editors can use the new language server through LSP. This rewrite marks the most significant performance breakthrough in TypeScript's history, dramatically reducing build times for large codebases. It sets a new standard for compiler performance in the JavaScript ecosystem and may influence other tools to consider native language rewrites. The new version introduces --checkers and --builders flags to customize parallelism, and provides a compatibility package for coexistence with TypeScript 6. However, embedded language toolchains like Vue and Svelte still require the old version due to unfinished API support.

telegram · zaihuapd · Jul 9, 04:01

**Background**: TypeScript is a typed superset of JavaScript that compiles to plain JavaScript. The previous compiler was written in TypeScript itself, which limited performance. By rewriting in Go, a compiled language with efficient concurrency, Microsoft achieved native machine code execution and multithreading, leading to the dramatic speed improvements.

<details><summary>References</summary>
<ul>
<li><a href="https://visualstudiomagazine.com/articles/2026/06/22/typescript-7-0-rc-moves-microsofts-go-rewrite-into-the-mainline-compiler.aspx">TypeScript 7.0 RC Moves Microsoft's Go Rewrite Into the Mainline Compiler -- Visual Studio Magazine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Language_Server_Protocol">Language Server Protocol - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#TypeScript`, `#compiler`, `#performance`, `#Go`, `#Microsoft`

---

<a id="item-3"></a>
## [Ant Group Open-Sources LingBot-Video, First MoE Embodied Video Model](https://www.qbitai.com/2026/07/446458.html) ⭐️ 9.0/10

Ant Group's robotics unit LingBot has open-sourced LingBot-Video, the world's first Mixture-of-Experts (MoE) embodied video generation foundation model, with 30 billion total parameters and 3 billion activated parameters, achieving state-of-the-art results on the RBench benchmark. This model significantly improves inference efficiency (3x faster than dense models of similar scale) and sets a new standard for embodied video generation, enabling more realistic robot simulation and world model research. The open-source release under Apache 2.0 lowers the barrier for researchers and developers in robotics and AI. LingBot-Video uses a DiT+MoE architecture with 128 experts and top-8 routing, and employs a six-reward reinforcement learning post-training that includes a physical-plausibility reward graded by a VLM. The model supports action-to-video prediction from robot action and hand-pose conditions.

telegram · zaihuapd · Jul 9, 04:30

**Background**: Mixture-of-Experts (MoE) is a machine learning approach that divides a model into separate sub-networks (experts), each specializing in different data subsets, and activates only relevant experts per input, improving efficiency. Embodied video generation models aim to produce realistic videos of robots interacting with the physical world, which is crucial for training and evaluating robotic policies without real-world trials.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/mixture-of-experts">What is mixture of experts? | IBM</a></li>
<li><a href="https://arxiv.org/abs/2601.15282">[2601.15282] Rethinking Video Generation Model for the Embodied World</a></li>

</ul>
</details>

**Discussion**: The Reddit community discussion raises critical questions about the physical-plausibility reward being graded by a VLM, suggesting potential Goodhart's law issues, and notes that the model is evaluated only on video quality metrics without closed-loop robot performance numbers, blurring the line between video generation and world models.

**Tags**: `#MoE`, `#embodied AI`, `#video generation`, `#open source`, `#robotics`

---

<a id="item-4"></a>
## [John Deere Owners Win Right to Repair in FTC Settlement](https://apnews.com/article/john-deere-right-to-repair-agriculture-equipment-cb7514ffedb95c130a976af661f2bc02) ⭐️ 8.0/10

John Deere has agreed to a settlement with the FTC and five states, allowing farmers and independent repair shops to repair their own equipment, ending years of restrictive practices. This settlement marks a major victory for the right-to-repair movement, potentially lowering costs for farmers and setting a precedent for other industries like consumer electronics. John Deere must pay $1 million collectively to five states for antitrust enforcement costs and will be subject to strict compliance oversight for 10 years.

hackernews · djoldman · Jul 8, 23:37 · [Discussion](https://news.ycombinator.com/item?id=48838876)

**Background**: The right-to-repair movement advocates for consumers and independent repair shops to have access to parts, tools, and software needed to repair products they own. John Deere had been criticized for using software locks and proprietary tools to prevent farmers from repairing their own tractors.

**Discussion**: Commenters praised Louis Rossmann for his advocacy and noted the fine is small relative to Deere's profits, but the compliance oversight is significant. Some expressed frustration that such basic rights require litigation.

**Tags**: `#right to repair`, `#FTC`, `#consumer rights`, `#regulation`, `#agriculture`

---

<a id="item-5"></a>
## [xAI Releases Grok 4.5 with 4x Efficiency](https://x.ai/news/grok-4-5) ⭐️ 8.0/10

xAI has released Grok 4.5, a new frontier AI model that claims 4x better reasoning efficiency compared to Opus, with competitive pricing at $2/$6 per million tokens. This release intensifies competition in the AI model market, offering a cost-effective alternative to models like GPT-5 and Opus, potentially lowering barriers for enterprise adoption of advanced reasoning capabilities. Grok 4.5 was trained on trillions of tokens of Cursor data, capturing developer-agent interactions, and operates at approximately 80 tokens per second while maintaining advanced reasoning.

hackernews · BoumTAC · Jul 8, 18:00 · [Discussion](https://news.ycombinator.com/item?id=48835111)

**Background**: Grok 4.5 is the latest model from xAI, a company founded by Elon Musk. It competes with models like OpenAI's GPT-5 and Anthropic's Claude Opus. The model supports a reasoning_effort parameter to control thinking time.

<details><summary>References</summary>
<ul>
<li><a href="https://x.ai/news/grok-4-5">Introducing Grok 4.5 | SpaceXAI</a></li>
<li><a href="https://www.digitalapplied.com/blog/grok-4-5-vs-opus-4-8-vs-gpt-5-5-best-frontier-model-2026">Grok 4.5 vs Opus 4.8 vs GPT-5.5: Which Model Wins?</a></li>
<li><a href="https://www.1950.ai/post/grok-4-5-raises-the-bar-for-frontier-ai-with-high-speed-reasoning-token-efficiency-and-real-world">Grok 4.5 Raises the Bar for Frontier AI With High-Speed Reasoning, Token Efficiency, and Real-World Enterprise Automation by Dr. Julie Butenko</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some users praise the model's cost-efficiency and benchmark performance, while others express distrust due to political concerns about xAI's content moderation and Musk's influence.

**Tags**: `#AI`, `#LLM`, `#Grok`, `#xAI`, `#benchmarks`

---

<a id="item-6"></a>
## [Microsoft Releases Flint, a Visualization Language for AI Agents](https://microsoft.github.io/flint-chart/#/) ⭐️ 8.0/10

Microsoft has open-sourced Flint, a visualization intermediate language that allows AI agents to generate high-quality charts from simple, human-editable specifications. Flint abstracts low-level visual decisions and includes a layout optimization engine to produce polished visualizations. Flint addresses a key limitation in AI agent reliability for data visualization by providing a deterministic intermediate layer, reducing the need for agents to make low-level visual decisions. This could improve the quality and consistency of AI-generated charts, benefiting developers and data analysts using agentic systems. Flint uses a semantic-type-based specification and a layout optimization engine to derive low-level details from high-level specs. It also provides an MCP server for easy integration into agent applications, and powers Microsoft's Data Formulator project.

hackernews · chenglong-hn · Jul 8, 17:46 · [Discussion](https://news.ycombinator.com/item?id=48834924)

**Background**: Data visualization languages like Vega are expressive but require explicit low-level details, making them difficult for AI agents to generate reliably. Flint offers a middle ground: a compact, high-level specification that a compiler can expand into detailed charts, similar to how intermediate representations (IR) work in compilers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/research/blog/flint-a-visualization-language-for-the-ai-era/">Flint : A visualization language for the AI era - Microsoft Research</a></li>
<li><a href="https://github.com/microsoft/flint-chart">GitHub - microsoft/ flint -chart: 🪄 Flint is a visualization language ...</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Flint exemplifies an emerging pattern of using deterministic layers (like compilers) in agentic systems. Some compared it to Vega, questioning its advantages, while others raised concerns about accessibility and composability for layered charts.

**Tags**: `#AI agents`, `#data visualization`, `#Microsoft`, `#intermediate language`, `#Hacker News`

---

<a id="item-7"></a>
## [OpenAI Analyzes Flaws in Coding Evaluations](https://openai.com/index/separating-signal-from-noise-coding-evaluations/) ⭐️ 8.0/10

OpenAI published an analysis identifying common flaws in coding evaluations, such as overly strict tests and underspecified prompts, and proposed better benchmarking practices. This matters because flawed benchmarks can mislead the AI community about model capabilities, and improving evaluation practices will lead to more reliable comparisons and progress in AI coding. The analysis covers four flaw types: overly strict tests, underspecified prompts, low-coverage tests, and misleading prompts, and suggests using human judgment to validate benchmarks.

hackernews · sk4rekr0w · Jul 8, 21:03 · [Discussion](https://news.ycombinator.com/item?id=48837396)

**Background**: Coding evaluations are used to measure AI models' ability to write code, but many existing benchmarks contain flaws that can produce misleading results. OpenAI's work aims to improve the reliability of these evaluations.

**Discussion**: Community comments highlight additional issues like efficiency metrics, cheating, and the need for human oversight, with some skepticism about whether benchmarks can ever fully capture real-world software development.

**Tags**: `#AI benchmarks`, `#coding evaluations`, `#software engineering`, `#AI evaluation`

---

<a id="item-8"></a>
## [Bun Rewritten from Zig to Rust](https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/#atom-everything) ⭐️ 8.0/10

Jarred Sumner announced that Bun, the JavaScript runtime, has been rewritten from Zig to Rust, citing memory safety issues. The rewrite was largely automated using AI coding agents and cost approximately $165,000 in API tokens. This rewrite demonstrates that AI-powered coding agents can now enable large-scale rewrites that were previously considered too risky. It also highlights Rust's growing dominance for systems programming where memory safety is critical. The rewrite took 11 days and involved 5.9 billion uncached input tokens and 690 million output tokens. The new Rust-based Bun has been live in Claude Code since June 17, 2026, with 10% faster startup on Linux.

rss · Simon Willison · Jul 8, 23:57

**Background**: Bun is a fast JavaScript runtime and toolkit, originally written in Zig. Memory safety bugs like use-after-free and double-free were common due to mixing garbage collection with manual memory management. Rust's ownership model and Drop trait prevent such bugs at compile time.

**Tags**: `#Bun`, `#Rust`, `#Zig`, `#runtime`, `#rewrite`

---

<a id="item-9"></a>
## [OpenAI Introduces GPT-Live Voice Mode with GPT-5.5 Delegation](https://simonwillison.net/2026/Jul/8/introducing-gptlive/#atom-everything) ⭐️ 8.0/10

OpenAI has launched GPT-Live, a new voice mode model for ChatGPT that can delegate complex tasks to GPT-5.5 while maintaining conversation flow. The model replaces the older GPT-4o era voice model and is available in the iPhone app. This upgrade significantly improves ChatGPT's voice mode capabilities, making it a more useful brainstorming partner with access to a frontier model for heavy lifting. It signals OpenAI's continued investment in conversational AI and multimodal interaction. GPT-Live uses GPT-5.5 as the backend model for tasks requiring web search, deeper reasoning, or complex work, and will be updated as new frontier models are released. The author noted an early bug where the model interrupted with laughter at non-jokes, which OpenAI reportedly tweaked.

rss · Simon Willison · Jul 8, 23:20

**Background**: GPT-5.5 is a large language model released by OpenAI on April 23, 2026, also known by its codename 'Spud'. It achieved notable benchmark scores and has been used in projects like Codex and Patch the Planet. The previous ChatGPT voice mode was based on a GPT-4o era model with a 2024 knowledge cutoff, limiting its usefulness.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT-5.5</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-Live`, `#voice mode`, `#AI`, `#ChatGPT`

---

<a id="item-10"></a>
## [LineageOS Launches Web-Based Flashing Tool](https://www.androidauthority.com/lineageos-summertime-update-2026-3685112/) ⭐️ 8.0/10

LineageOS has officially launched Lineage Flash Tools, a web-based tool that allows users to flash ROMs directly from a browser without installing adb and fastboot locally. The tool supports Fastboot, ADB, and Samsung Odin protocols, and requires a WebUSB-compatible browser like Chrome or Edge. This innovation significantly lowers the barrier to flashing custom ROMs, making the process more accessible to casual users and potentially expanding the LineageOS user base. It also demonstrates the growing adoption of WebUSB technology for device-level operations. The tool cannot fully replace traditional flashing methods and must be used alongside device-specific Wiki installation guides. Additionally, LineageOS updated the Updater app with a Material 3 Expressive interface and confirmed that LineageOS 24 based on Android 17 is under development.

telegram · zaihuapd · Jul 9, 01:46

**Background**: LineageOS is a popular open-source custom ROM for Android devices, offering enhanced features and extended software support. Traditionally, flashing a custom ROM requires installing command-line tools like adb and fastboot, which can be intimidating for beginners. WebUSB allows web applications to communicate with USB devices, enabling browser-based flashing.

**Tags**: `#LineageOS`, `#刷机工具`, `#Android`, `#WebUSB`, `#定制ROM`

---

<a id="item-11"></a>
## [DJI EV50 Drone Flies to 8,861m on Everest](https://www.163.com/dy/article/L1CUCV940514R9OJ.html) ⭐️ 8.0/10

DJI's unreleased EV50 VTOL cargo drone reached 8,861 meters on Mount Everest during the 'Peak Mission' scientific expedition, setting a world record for the highest altitude in public testing of its kind. This achievement demonstrates the drone's high-altitude capability and potential for low-altitude logistics, such as 100-kilometer cargo delivery, which could revolutionize transportation in challenging terrains. The EV50 is a hybrid-wing drone that can vertically take off and land, then switch to fixed-wing cruise. Over 12 days, it completed 32 sorties, climbed 3,730 meters continuously, and still had 30% battery remaining on return.

telegram · zaihuapd · Jul 9, 06:00

**Background**: VTOL (Vertical Take-Off and Landing) drones combine the flexibility of helicopters with the efficiency of fixed-wing aircraft. High-altitude testing on Everest provides valuable data for drone performance in extreme conditions, relevant for logistics and scientific research.

**Tags**: `#drones`, `#DJI`, `#high-altitude`, `#logistics`, `#technology`

---

<a id="item-12"></a>
## [National Supercomputing Internet Core Node Launches in Zhengzhou](https://36kr.com/newsflashes/3887797387344387) ⭐️ 8.0/10

On July 9, 2026, the core node of China's National Supercomputing Internet was officially launched in Zhengzhou, providing over 100,000 domestic AI computing cards. This marks a significant milestone in China's national computing infrastructure, enabling large-scale domestic AI compute resources and supporting the country's strategic AI development goals. The node is the largest single pool of domestic AI computing resources connected to the National Supercomputing Internet platform, and it will handle operations, resource scheduling, and supply-demand integration.

telegram · zaihuapd · Jul 9, 07:00

**Background**: The National Supercomputing Internet is a national initiative to build a unified computing resource scheduling system across China. The Zhengzhou node serves as a core hub for coordinating computing power from various domestic sources, aiming to boost AI and scientific research capabilities.

**Tags**: `#supercomputing`, `#AI infrastructure`, `#China`, `#national strategy`, `#computing resources`

---

<a id="item-13"></a>
## [OpenAI and US War Department Revise AI Contract to Ban Citizen Surveillance](https://t.me/zaihuapd/42459) ⭐️ 8.0/10

OpenAI and the US Department of War (formerly the Department of Defense) have agreed to revise their AI cooperation contract to explicitly prohibit the use of AI systems for surveillance of American citizens, following a proposal by OpenAI CEO Sam Altman. This move sets a precedent for ethical AI use in military contexts, addressing public concerns about mass surveillance and potentially influencing future AI contracts with government agencies. The revised clause specifically prohibits deliberate surveillance of US citizens and the use of commercially obtained personally identifiable information for tracking or monitoring. The contract has not yet been formally signed.

telegram · zaihuapd · Jul 9, 13:22

**Background**: The US Department of War, formerly the Department of Defense, oversees military operations. AI companies like OpenAI and Anthropic have faced scrutiny over potential misuse of their technology in military applications, including surveillance. Anthropic's previous contract with the War Department was suspended due to similar concerns.

**Tags**: `#AI ethics`, `#OpenAI`, `#military AI`, `#surveillance`, `#policy`

---