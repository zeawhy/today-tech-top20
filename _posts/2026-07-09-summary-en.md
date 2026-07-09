---
layout: default
title: "Horizon Summary: 2026-07-09 (EN)"
date: 2026-07-09
lang: en
---

> From 36 items, 12 important content pieces were selected

---

1. [OpenAI Releases GPT-5.6 with Three Tiers and Six Reasoning Levels](#item-1) ⭐️ 9.0/10
2. [Bun Rewritten from Zig to Rust](#item-2) ⭐️ 9.0/10
3. [TypeScript 7.0 Released with Go Rewrite, Up to 12x Faster](#item-3) ⭐️ 9.0/10
4. [Ant Group Open-Sources LingBot-Video, First MoE Embodied Video Model](#item-4) ⭐️ 9.0/10
5. [EU Parliament Passes Chat Control 1.0 via Procedural Loophole](#item-5) ⭐️ 8.0/10
6. [Meta Launches Muse Spark 1.1 with Paid API](#item-6) ⭐️ 8.0/10
7. [Spider venom selectively kills varroa mites, spares bees](#item-7) ⭐️ 8.0/10
8. [OpenAI Launches GPT-Live Voice Mode with GPT-5.5 Delegation](#item-8) ⭐️ 8.0/10
9. [Meta's Superintelligence Progress: Compute Ramp, RL Startup, Advice](#item-9) ⭐️ 8.0/10
10. [DJI EV50 Drone Reaches 8,861m on Everest, Sets Altitude Record](#item-10) ⭐️ 8.0/10
11. [Zhengzhou Core Node of National Supercomputing Internet Launches](#item-11) ⭐️ 8.0/10
12. [OpenAI Revises Pentagon Contract to Ban Domestic Surveillance](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Releases GPT-5.6 with Three Tiers and Six Reasoning Levels](https://openai.com/index/gpt-5-6/) ⭐️ 9.0/10

OpenAI has released GPT-5.6, a new flagship model available in three tiers (Luna, Terra, Sol) and six reasoning effort levels, achieving a new state-of-the-art on the ARC-AGI-3 benchmark. This release marks a significant advancement in AI reasoning capabilities, with the Sol tier becoming the first frontier model to beat an ARC-AGI-3 game, signaling progress toward more adaptable and intelligent AI agents. The model introduces six reasoning effort levels (none, low, medium, high, xhigh, max) across three tiers, with Sol achieving 7.8% on ARC-AGI-3. The developer guide highlights improved intent understanding and preservation of original image dimensions.

hackernews · logickkk1 · Jul 9, 17:04 · [Discussion](https://news.ycombinator.com/item?id=48849066)

**Background**: ARC-AGI (Abstraction and Reasoning Corpus for Artificial General Intelligence) is a benchmark designed to measure an AI's ability to solve novel reasoning tasks. ARC-AGI-3 is the latest interactive version that challenges agents to adapt to new environments on the fly. Previous GPT models (e.g., GPT-5.5, GPT-5.4) introduced reasoning effort levels to balance cost and performance.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>

</ul>
</details>

**Discussion**: Community members shared visual examples of the model's output (e.g., pelicans at different effort levels) and noted that GPT-5.6 Sol is the first frontier model to beat an ARC-AGI-3 game. Some users discussed comparisons with other coding tools like Claude Code, while others pointed out that OpenAI excluded a competitor from benchmarks due to refusal to answer advanced biology questions.

**Tags**: `#OpenAI`, `#GPT-5.6`, `#AI`, `#LLM`, `#ARC-AGI`

---

<a id="item-2"></a>
## [Bun Rewritten from Zig to Rust](https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/#atom-everything) ⭐️ 9.0/10

Jarred Sumner announced that Bun, the JavaScript runtime, has been rewritten from Zig to Rust, with the new version already deployed in Claude Code since June 17, 2025. This rewrite addresses critical memory safety bugs like use-after-free and double-free, which were common in the Zig version due to mixing garbage collection with manual memory management. It also demonstrates that large-scale rewrites are now feasible with AI coding agents, challenging the long-held belief that rewrites should be avoided. The rewrite cost approximately $165,000 in API tokens (5.9 billion uncached input tokens, 690 million output tokens) and took 11 days of agentic engineering using a conformance suite of TypeScript tests. The Rust port is now used in Claude Code v2.1.181, with 10% faster startup on Linux.

rss · Simon Willison · Jul 8, 23:57

**Background**: Bun is a JavaScript runtime, package manager, and test runner designed as a drop-in replacement for Node.js, using JavaScriptCore instead of V8. It was originally written in Zig, a system programming language that requires manual memory management, which led to memory safety bugs when combined with garbage collection. Rust is a memory-safe language that prevents such bugs at compile time through its ownership system and RAII (Resource Acquisition Is Initialization) pattern.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Memory_safety">Memory safety - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion (likely) praised the engineering effort and the use of AI agents for the rewrite, though some questioned the cost and long-term maintainability of LLM-generated code. The post generated significant interest in the feasibility of agentic rewrites.

**Tags**: `#Bun`, `#Rust`, `#Zig`, `#JavaScript runtime`, `#software engineering`

---

<a id="item-3"></a>
## [TypeScript 7.0 Released with Go Rewrite, Up to 12x Faster](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 9.0/10

Microsoft has officially released TypeScript 7.0, a native version rewritten in Go that delivers 8-12x faster full builds and supports shared-memory multithreading. Users can install it via npm, and major editors support the new language server through LSP. This release represents a major paradigm shift for TypeScript tooling, dramatically improving developer productivity on large codebases. The Go rewrite sets a new performance baseline for language servers and compilers in the JavaScript ecosystem. New --checkers and --builders flags allow customization of parallelism, and a compatibility package enables coexistence with TypeScript 6. However, embedded language toolchains like Vue and Svelte are not yet supported and must still use the older version.

telegram · zaihuapd · Jul 9, 04:01

**Background**: TypeScript is a superset of JavaScript that adds static typing, and its compiler was originally written in TypeScript itself. The Language Server Protocol (LSP) standardizes communication between editors and language servers, enabling features like code completion and go-to-definition. Rewriting the compiler in Go allows better utilization of multi-core processors and faster startup times.

<details><summary>References</summary>
<ul>
<li><a href="https://www.devbolt.dev/blog/typescript-7-go-rewrite">TypeScript 7.0: What the Go Rewrite Means for Every Developer</a></li>
<li><a href="https://betterstack.com/community/guides/scaling-nodejs/typescript-7-go-rewrite/">TypeScript 7.0: New Features and the Go-Powered Compiler Rewrite</a></li>

</ul>
</details>

**Tags**: `#TypeScript`, `#Programming Languages`, `#Performance`, `#Microsoft`, `#Tooling`

---

<a id="item-4"></a>
## [Ant Group Open-Sources LingBot-Video, First MoE Embodied Video Model](https://www.qbitai.com/2026/07/446458.html) ⭐️ 9.0/10

Ant Group's LingBot-Video, the world's first Mixture-of-Experts (MoE) based embodied video foundation model, has been open-sourced under the Apache 2.0 license. It achieves state-of-the-art results on the RBench robot manipulation benchmark with 3x inference efficiency compared to dense models. This release marks a major advance in embodied AI by combining MoE efficiency with video generation for robotics, enabling faster and more scalable robot learning. It lowers the barrier for researchers and developers to build and deploy embodied AI systems. LingBot-Video has 30B total parameters but activates only ~3B per inference, using a DiT+MoE architecture. It was trained on 70,000 hours of embodied data covering dexterous manipulation, robot locomotion, and first-person interaction, with a multi-dimensional reinforcement learning reward system.

telegram · zaihuapd · Jul 9, 04:30

**Background**: Mixture-of-Experts (MoE) is an AI architecture that uses multiple specialized submodels (experts) to handle tasks more efficiently than a single dense model. Diffusion Transformers (DiTs) combine transformers with diffusion processes for high-quality video generation. Embodied AI focuses on models that can perceive and act in physical environments, often for robotics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? - NVIDIA</a></li>
<li><a href="https://github.com/facebookresearch/DiT">GitHub - facebookresearch/DiT: Official PyTorch ...</a></li>

</ul>
</details>

**Tags**: `#embodied AI`, `#MoE`, `#video generation`, `#open-source`, `#robotics`

---

<a id="item-5"></a>
## [EU Parliament Passes Chat Control 1.0 via Procedural Loophole](https://www.patrick-breyer.de/en/eu-parliament-greenlights-chat-control-1-0-breyer-our-children-lose-out/) ⭐️ 8.0/10

On July 11, 2024, the European Parliament allowed the suspicionless mass scanning of private messages (Chat Control 1.0) to pass, despite a majority of voting MEPs opposing it (314 against, 276 in favor, 17 abstentions), because the motion to reject failed to secure the required absolute majority of 361 votes. This decision reinstates warrantless scanning of private messages by US tech companies until 2028, raising serious privacy and democratic concerns. It also highlights procedural manipulation in the EU legislative process, potentially eroding public trust. Chat Control 1.0 allows scanning of direct messages on platforms like Instagram, Discord, Snapchat, Skype, Xbox, Gmail, and iCloud, but does not affect end-to-end encrypted chats such as WhatsApp and Signal. Public social media posts and cloud storage files were already scannable without this law.

hackernews · rapnie · Jul 9, 11:03 · [Discussion](https://news.ycombinator.com/item?id=48843923)

**Background**: Chat Control refers to EU legislation aimed at combating child sexual abuse material (CSAM) by requiring tech companies to scan private communications. The first iteration, Chat Control 1.0, was initially agreed voluntarily in 2021. Expert assessments indicate no current technology can detect CSAM without high false positive rates, affecting ordinary communications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://www.patrick-breyer.de/en/posts/chat-control/">Chat Control: The EU's CSAM scanner proposal</a></li>
<li><a href="https://www.reddit.com/r/europe/comments/1urnadd/european_parliament_greenlights_chat_control_10/">r/europe on Reddit: European Parliament greenlights Chat Control 1.0, will now become law. 276 In Favour, 314 Against, 17 Abstentians.</a></li>

</ul>
</details>

**Discussion**: Commenters expressed outrage over the procedural trick, noting the vote was held just before summer break when many MEPs were absent. Some pointed out that end-to-end encrypted chats like WhatsApp remain unaffected, but others questioned WhatsApp's encryption status. There is widespread concern that the EU is moving toward totalitarian governance.

**Tags**: `#privacy`, `#EU legislation`, `#surveillance`, `#democracy`

---

<a id="item-6"></a>
## [Meta Launches Muse Spark 1.1 with Paid API](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) ⭐️ 8.0/10

Meta introduced Muse Spark 1.1, a multimodal reasoning model for agentic tasks, and for the first time is charging businesses for API access at $1.25 per million input tokens and $4.25 per million output tokens. This marks Meta's entry into the paid AI model market, directly competing with OpenAI and Anthropic at significantly lower prices, potentially commoditizing agentic AI and reshaping the competitive landscape. The model is built for agentic tasks with major gains in tool use, but community members noted that benchmark results may be invalid due to resource cap overrides in Terminal-Bench 2.1 evaluations.

hackernews · ot · Jul 9, 14:10 · [Discussion](https://news.ycombinator.com/item?id=48846184)

**Background**: Agentic AI models are designed to autonomously use tools and perform multi-step tasks. Meta previously released Muse Spark as an open-weight model, but Muse Spark 1.1 introduces a paid API tier, reflecting a strategic shift toward monetization while still offering open weights.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/">Introducing Muse Spark 1.1</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-07-09/meta-starts-charging-for-ai-with-muse-spark-1-1-agentic-model">Meta Starts Charging for AI With Muse Spark 1.1 Agentic Model - Bloomberg</a></li>
<li><a href="https://aiweekly.co/alerts/meta-prices-muse-spark-11-api-at-125425-per-m-tokens">Meta prices Muse Spark 1.1 API at $1.25/$4.25 per M tokens | AI Weekly</a></li>

</ul>
</details>

**Discussion**: The community is divided: some praise the low pricing and practical integration (e.g., Simon Willison's LLM plugin), while others question benchmark validity due to resource cap violations and debate whether Meta should focus on undercutting competitors rather than matching them.

**Tags**: `#AI`, `#Meta`, `#agentic model`, `#open source`, `#benchmarking`

---

<a id="item-7"></a>
## [Spider venom selectively kills varroa mites, spares bees](https://connectsci.au/news/news-parent/9703/Spider-venom-kills-varroa-mites-without-harming) ⭐️ 8.0/10

Researchers have discovered that spider venom can selectively kill Varroa destructor mites without harming honeybees, offering a novel biological approach to a devastating pest. Varroa mites are the most damaging honeybee pest worldwide, causing colony collapse and huge economic losses. A selective, bee-safe treatment could revolutionize beekeeping and help protect global pollination. The study shows that spider venom components target mite-specific ion channels, leaving bee physiology unaffected. However, translating lab results into a practical, affordable hive treatment remains a significant challenge.

hackernews · Jedd · Jul 9, 05:14 · [Discussion](https://news.ycombinator.com/item?id=48841259)

**Background**: Varroa destructor is an external parasitic mite that feeds on honeybees and transmits deadly viruses, often leading to colony collapse within 2-3 years if untreated. Current miticides can harm bees or contaminate honey, and resistance is growing. Spider venoms contain diverse toxins evolved to target specific prey, making them a promising source of selective pesticides.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Varroa_mites">Varroa mites</a></li>
<li><a href="https://en.wikipedia.org/wiki/Varroa_destructor">Varroa destructor - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed cautious optimism, noting that lab success is far from real-world application. Some highlighted the need for affordable, easy-to-use treatments and pointed to alternative approaches like mycelium-based immune boosts. Others questioned whether the focus on honeybees overlooks native bee conservation.

**Tags**: `#biology`, `#agriculture`, `#beekeeping`, `#pest control`, `#venom`

---

<a id="item-8"></a>
## [OpenAI Launches GPT-Live Voice Mode with GPT-5.5 Delegation](https://simonwillison.net/2026/Jul/8/introducing-gptlive/#atom-everything) ⭐️ 8.0/10

OpenAI has introduced GPT-Live, a new voice mode model for ChatGPT that can delegate complex tasks to GPT-5.5 while maintaining conversation flow. The upgrade replaces the previous GPT-4o-era voice model and is rolling out to users now. This upgrade significantly improves the usefulness of ChatGPT's voice mode by providing a more capable and up-to-date model, enabling richer brainstorming and real-time assistance. The delegation mechanism allows seamless handling of tasks requiring web search or deep reasoning without interrupting the conversation. GPT-Live uses GPT-5.5 as its backend frontier model at launch, with plans to update to future models. The previous voice mode was based on a GPT-4o-era model with a 2024 knowledge cutoff, which limited its usefulness. A preview revealed a bug where the model interrupted with laughter at non-jokes, which OpenAI has reportedly tweaked.

rss · Simon Willison · Jul 8, 23:20

**Background**: ChatGPT's voice mode allows users to speak with the AI assistant for tasks like language practice and brainstorming. The previous model was based on GPT-4o, which had a knowledge cutoff in 2024 and was less capable for complex reasoning. GPT-5.5, released in April 2026, is OpenAI's latest frontier model with improved reasoning and reliability, and is used by GPT-Live for delegated tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT-5.5</a></li>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT-5.5 | OpenAI</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion (linked in the article) likely includes positive reactions to the upgrade, with some users noting the improved naturalness and capability. The bug about inappropriate laughter was mentioned as a minor annoyance that OpenAI addressed.

**Tags**: `#OpenAI`, `#GPT-Live`, `#voice mode`, `#AI`, `#ChatGPT`

---

<a id="item-9"></a>
## [Meta's Superintelligence Progress: Compute Ramp, RL Startup, Advice](https://newsletter.semianalysis.com/p/the-future-of-meta-superintelligence) ⭐️ 8.0/10

Meta's superintelligence project has achieved the most aggressive compute scaling ever seen, a top-tier reinforcement learning environment startup has emerged, and the article offers strategic advice for Google DeepMind. This signals a major acceleration in AI infrastructure investment and competition, potentially reshaping the landscape of AI development and deployment. The compute ramp involves scaling across distances over 2000 km, enabled by Cisco's 'scale-across' networking technology, and the RL environment startup is among a growing list of vendors in the space.

rss · Semianalysis · Jul 9, 19:16

**Background**: Superintelligence refers to AI systems that surpass human intelligence across many domains. Reinforcement learning (RL) environments are simulated worlds where AI agents learn through trial and error. 'Scale-across' is a networking approach that connects multiple data centers over long distances to pool compute resources.

<details><summary>References</summary>
<ul>
<li><a href="https://thecuberesearch.com/cisco-enables-scale-across-ai-environments/">Cisco Enables "Scale-Across" AI environments - theCUBE Research</a></li>
<li><a href="https://alignlist.com/guides/top-40-rl-environments-startups-and-companies">Top 40 RL Environments Startups and Companies in 2026</a></li>
<li><a href="https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out">Tracking Trillions: The Assumptions Shaping the Scale of the ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#superintelligence`, `#compute`, `#Meta`, `#reinforcement learning`

---

<a id="item-10"></a>
## [DJI EV50 Drone Reaches 8,861m on Everest, Sets Altitude Record](https://www.163.com/dy/article/L1CUCV940514R9OJ.html) ⭐️ 8.0/10

DJI's unreleased EV50 VTOL cargo drone successfully flew to 8,861 meters above sea level on Mount Everest during the 'Peak Mission' scientific expedition, setting a world record for the highest operating altitude in its class and collecting atmospheric data above 8,000 meters. This achievement demonstrates DJI's advanced VTOL technology and its potential to replace helicopters in high-altitude emergency logistics and climate research, opening new possibilities for low-altitude cargo delivery in extreme environments. The EV50 is a hybrid VTOL drone that takes off vertically and transitions to fixed-wing cruise. Over a 12-day mission, it completed 32 takeoffs and landings, climbed 3,730 meters continuously, and still had 30% battery remaining on return.

telegram · zaihuapd · Jul 9, 06:00

**Background**: VTOL (Vertical Take-Off and Landing) drones combine the flexibility of multi-rotor aircraft with the efficiency of fixed-wing flight. The EV50 is designed for cargo transport and scientific missions in challenging environments, with a payload capacity of 50 kg. DJI aims to use this technology for low-altitude logistics including hundred-kilometer cargo delivery.

<details><summary>References</summary>
<ul>
<li><a href="https://laetimes.com/en/news/dji-ev50">Beyond Helicopters: DJI's EV50 Drone Brings Autonomous…</a></li>
<li><a href="https://laetimes.com/en/news/dji-ev50-8861">DJI EV50 Reaches 8,861 Metres Above Sea Level on Mount…</a></li>

</ul>
</details>

**Tags**: `#drones`, `#DJI`, `#aviation`, `#technology`, `#record`

---

<a id="item-11"></a>
## [Zhengzhou Core Node of National Supercomputing Internet Launches](https://36kr.com/newsflashes/3887797387344387) ⭐️ 8.0/10

On July 9, 2026, the core node of China's National Supercomputing Internet was officially launched in Zhengzhou, providing over 100,000 domestic AI computing cards. This marks a major milestone in China's national AI computing infrastructure, as it is the largest single pool of domestic AI computing resources connected to the National Supercomputing Internet, significantly boosting the country's independent AI computing capacity. The node is designed to build a nationwide computing resource scheduling system, serving core functions such as operation management and resource scheduling, while also integrating supply-demand matching and industry incubation services.

telegram · zaihuapd · Jul 9, 07:00

**Background**: The National Supercomputing Internet is a national-level computing service platform initiated by the Ministry of Science and Technology in April 2023, aiming to integrate supercomputing and intelligent computing resources across China. Domestic AI computing cards, such as those from Huawei and other Chinese manufacturers, have evolved from being merely usable to being effective for large model training, with domestic cards capturing 41% of the Chinese AI accelerator market in 2025.

<details><summary>References</summary>
<ul>
<li><a href="https://www.scnet.cn/home/subject/hxjd/index.html">国家超算互联网核心节点 - 超算互联网</a></li>
<li><a href="https://baike.baidu.com/item/国家超算互联网/62902938">国家超算互联网_百度百科</a></li>
<li><a href="https://baike.baidu.com/item/国产算力卡/67727675">国产算力卡_百度百科</a></li>

</ul>
</details>

**Tags**: `#supercomputing`, `#AI infrastructure`, `#China`, `#national computing`, `#domestic hardware`

---

<a id="item-12"></a>
## [OpenAI Revises Pentagon Contract to Ban Domestic Surveillance](https://t.me/zaihuapd/42459) ⭐️ 8.0/10

OpenAI and the US Department of War (formerly the Department of Defense) have agreed to amend their AI contract to explicitly prohibit the use of AI systems for domestic surveillance of American citizens. The revision was proactively proposed by OpenAI CEO Sam Altman to address ethical concerns. This move sets a precedent for ethical AI use in military contracts, addressing public fears about mass surveillance. It also distinguishes OpenAI from rival Anthropic, which faced backlash over similar issues. The amended contract includes explicit prohibitions on using AI for deliberate surveillance of US citizens and on tracking or monitoring using commercially obtained personally identifiable information. The revised terms have not yet been formally signed.

telegram · zaihuapd · Jul 9, 13:22

**Background**: In July 2025, the US Department of Defense awarded contracts worth up to $200 million each to OpenAI, Anthropic, Google, and xAI to accelerate AI adoption for national security. Anthropic's contract later faced controversy over potential use of its AI model Claude for mass surveillance, leading to a dispute. OpenAI's proactive amendment aims to avoid similar backlash.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/our-agreement-with-the-department-of-war/">Our agreement with the Department of War - OpenAI</a></li>
<li><a href="https://www.bbc.com/news/articles/c3rz1nd0egro">OpenAI changes deal with US military after backlash - BBC</a></li>
<li><a href="https://www.nytimes.com/2026/03/02/technology/openai-pentagon-deal-amended-surveillance.html">OpenAI Amends A.I. Deal With the Pentagon - The New York Times</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#OpenAI`, `#military AI`, `#surveillance`, `#policy`

---