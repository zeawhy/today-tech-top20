---
layout: default
title: "Horizon Summary: 2026-07-09 (EN)"
date: 2026-07-09
lang: en
---

> From 35 items, 11 important content pieces were selected

---

1. [OpenAI Launches GPT-Live with GPT-5.5 Delegation](#item-1) ⭐️ 9.0/10
2. [TypeScript 7.0 Announced with Go Rewrite, Up to 12x Faster](#item-2) ⭐️ 9.0/10
3. [Ant Group Open-Sources LingBot-Video, First MoE Embodied Video Model](#item-3) ⭐️ 9.0/10
4. [John Deere Settles Right-to-Repair with FTC](#item-4) ⭐️ 8.0/10
5. [Microsoft Releases Flint: A Visualization Language for AI Agents](#item-5) ⭐️ 8.0/10
6. [xAI Releases Grok 4.5 with Cost Efficiency](#item-6) ⭐️ 8.0/10
7. [Bun Rewrites in Rust with AI Assistance](#item-7) ⭐️ 8.0/10
8. [Cloudflare and OpenAI Partner to Boost AI Search with Network Data](#item-8) ⭐️ 8.0/10
9. [Researchers identify apps via EM signals with 99% accuracy](#item-9) ⭐️ 8.0/10
10. [DJI EV50 Drone Reaches 8,861m on Mount Everest](#item-10) ⭐️ 8.0/10
11. [China's Supercomputing Internet Core Node Goes Live in Zhengzhou](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Launches GPT-Live with GPT-5.5 Delegation](https://openai.com/index/introducing-gpt-live/) ⭐️ 9.0/10

OpenAI launched GPT-Live on July 8, 2026, a full-duplex voice mode for ChatGPT that can delegate complex queries to GPT-5.5 in the background, enabling more productive and extended conversations. This bridges the gap between voice assistants and frontier AI models, allowing users to have natural, real-time conversations while still accessing top-tier reasoning and tool use. It could redefine how people interact with AI assistants for both casual and professional tasks. GPT-Live uses a full-duplex architecture, meaning it can listen and speak simultaneously, and includes two tiers: GPT-Live-1 (paid) and GPT-Live-1 mini (free). The delegation to GPT-5.5 happens seamlessly in the background, so users are not limited to a less capable voice model.

hackernews · logickkk1 · Jul 8, 17:03 · [Discussion](https://news.ycombinator.com/item?id=48834405)

**Background**: Previous voice modes in ChatGPT and other assistants were often limited to older, less capable models, restricting their usefulness for complex tasks. GPT-5.5, launched in April 2026, is OpenAI's most advanced model, excelling at coding, research, and data analysis. GPT-Live combines the natural interaction of voice with the power of GPT-5.5, addressing a key limitation of earlier voice assistants.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-live/">Introducing GPT-Live | OpenAI</a></li>
<li><a href="https://www.explainx.ai/blog/gpt-live-openai-chatgpt-voice-july-2026">GPT-Live: OpenAI Full-Duplex ChatGPT Voice | explainx.ai Blog</a></li>
<li><a href="https://mer.vin/2026/07/gpt-live-explained-full-duplex-chatgpt-voice-with-gpt-5-5-delegation/">GPT-Live Explained: Full-Duplex ChatGPT Voice With GPT-5.5 ...</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some users with preview access praise the long conversation capability and GPT-5.5 delegation, while others express philosophical concerns about replacing human relationships or note the lack of tool/connector support in voice mode. A blind user highlighted the potential for assistive technology when combined with video and glasses.

**Tags**: `#OpenAI`, `#voice AI`, `#GPT-5.5`, `#AI assistants`, `#product launch`

---

<a id="item-2"></a>
## [TypeScript 7.0 Announced with Go Rewrite, Up to 12x Faster](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 9.0/10

Microsoft announced TypeScript 7.0, a major version featuring a complete rewrite of the compiler in Go, delivering up to 11.9x faster compilation on large codebases like VS Code. This dramatic performance improvement makes TypeScript significantly more practical for large-scale projects, potentially accelerating developer workflows and CI pipelines across the JavaScript ecosystem. The new compiler supports shared-memory multithreading with --checkers and --builders flags to customize parallelism, and a compatibility package allows coexistence with TypeScript 6. However, embedded language toolchains for Vue and Svelte are not yet supported.

hackernews · DanRosenwasser · Jul 8, 16:06 · [Discussion](https://news.ycombinator.com/item?id=48833715)

**Background**: TypeScript is a typed superset of JavaScript that compiles to plain JavaScript. Its previous compiler, tsc, was written in TypeScript itself, which limited performance. The Go-based rewrite, codenamed tsgo, leverages native compilation and multithreading to achieve order-of-magnitude speedups.

<details><summary>References</summary>
<ul>
<li><a href="https://devblogs.microsoft.com/typescript/typescript-native-port/">A 10x Faster TypeScript - TypeScript - devblogs.microsoft.com</a></li>
<li><a href="https://github.com/microsoft/typescript-go">GitHub - microsoft/typescript-go: Staging repo for development of ...</a></li>

</ul>
</details>

**Discussion**: The community reaction is overwhelmingly positive, with many praising the performance gains and the team's ability to maintain two codebases. Some users expressed interest in similar typed language efforts for other ecosystems like PHP, while others humorously anticipated a future Rust rewrite.

**Tags**: `#TypeScript`, `#programming languages`, `#performance`, `#compiler`, `#Microsoft`

---

<a id="item-3"></a>
## [Ant Group Open-Sources LingBot-Video, First MoE Embodied Video Model](https://www.qbitai.com/2026/07/446458.html) ⭐️ 9.0/10

Ant Group's robotics unit, Ant LingBot, has open-sourced LingBot-Video, the world's first Mixture-of-Experts (MoE) based embodied video foundation model, under the Apache 2.0 license. The model achieves 3x inference efficiency over dense models and scores 0.620 on the RBench benchmark, surpassing models like Wan2.6 and Seedance1.5 Pro. This release marks a significant milestone in embodied AI by combining MoE efficiency with video generation for robotics, potentially accelerating research in robot action prediction, simulation data generation, and world models. The open-source nature lowers barriers for the community to build upon state-of-the-art technology. LingBot-Video has 30B total parameters but activates only about 3B per inference, using a DiT+MoE architecture with 128 experts and top-8 routing. It incorporates a multi-reward RL post-training system including physical plausibility, and supports action-to-video generation conditioned on robot actions and hand poses.

telegram · zaihuapd · Jul 9, 04:30

**Background**: MoE (Mixture of Experts) is an AI architecture that uses multiple specialized submodels (experts) and a routing mechanism to activate only a subset for each input, improving efficiency without sacrificing capacity. Embodied video foundation models aim to generate realistic videos of robots performing tasks, serving as world models or policy evaluators. RBench is a benchmark for evaluating robot-oriented video generation across five task domains and four robot embodiments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? | NVIDIA Glossary</a></li>
<li><a href="https://huggingface.co/datasets/DAGroup-PKU/RBench">DAGroup-PKU/RBench · Datasets at Hugging Face</a></li>

</ul>
</details>

**Discussion**: The Reddit community expressed interest but raised critical questions: whether a VLM can reliably judge physical plausibility (risk of Goodhart's law), and whether the model is truly a world model or just a video generator, as no closed-loop robot results were provided. Some noted that while it tops RBench average, reasoning-heavy dimensions still favor closed models, and it ranks second on general T2V in its own evaluation.

**Tags**: `#embodied AI`, `#MoE`, `#video generation`, `#open-source`, `#robotics`

---

<a id="item-4"></a>
## [John Deere Settles Right-to-Repair with FTC](https://apnews.com/article/john-deere-right-to-repair-agriculture-equipment-cb7514ffedb95c130a976af661f2bc02) ⭐️ 8.0/10

John Deere has reached a settlement with the Federal Trade Commission and five states, agreeing to allow farmers and independent repair shops to fix its equipment. The settlement requires Deere to provide diagnostic tools, manuals, and parts for 10 years. This settlement marks a major victory for the right-to-repair movement, potentially setting a precedent for other manufacturers. It empowers farmers to repair their own equipment, reducing costs and downtime, and challenges repair monopolies in agriculture. John Deere must pay $1 million collectively to five states for antitrust enforcement costs and is subject to strict compliance oversight for 10 years. The settlement does not include a monetary fine to the FTC, and the $1 million is relatively small compared to Deere's profits.

hackernews · djoldman · Jul 8, 23:37 · [Discussion](https://news.ycombinator.com/item?id=48838876)

**Background**: The right-to-repair movement advocates for consumers' legal right to maintain, repair, or modify products they own, including farm equipment. Manufacturers like John Deere have historically restricted access to diagnostic tools, software, and parts, forcing farmers to use authorized dealers for repairs. This has led to higher costs and delays for farmers, especially during critical planting and harvest seasons.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Right_to_repair_movement">Right to repair movement</a></li>
<li><a href="https://en.wikipedia.org/wiki/Right_to_repair">Right to repair - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters praised right-to-repair activist Louis Rossmann for his work, and noted that the $1 million fine is trivial compared to Deere's profits. Some expressed frustration that such basic rights require litigation, while others pointed out cognitive dissonance in the tech industry's opposition to repair rights.

**Tags**: `#right-to-repair`, `#consumer rights`, `#antitrust`, `#agriculture`, `#FTC`

---

<a id="item-5"></a>
## [Microsoft Releases Flint: A Visualization Language for AI Agents](https://microsoft.github.io/flint-chart/#/) ⭐️ 8.0/10

Microsoft has open-sourced Flint, a visualization intermediate language that allows AI agents to generate high-quality charts from simple, semantic-type-based specifications, offloading visual decisions to a compiler. Flint addresses a key limitation in current chart DSLs by balancing reliability and expressiveness, enabling AI agents to produce polished visualizations without verbose low-level parameters. This could significantly improve the quality of AI-generated data visualizations in agentic systems. Flint supports 46 chart types and can compile a single specification into multiple industry-standard formats including Vega-Lite, Apache ECharts, and Chart.js. It also provides an MCP server for easy integration with existing agent applications.

hackernews · chenglong-hn · Jul 8, 17:46 · [Discussion](https://news.ycombinator.com/item?id=48834924)

**Background**: Data visualizations are crucial for human-data interaction, but AI agents struggle with current visualization languages: simple specs yield low-quality charts, while detailed specs are verbose and error-prone. An intermediate language (IR) is a representation used internally by compilers to enable optimization and translation between source and target languages. Flint applies this concept to visualization, letting the compiler handle layout and styling decisions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/research/blog/flint-a-visualization-language-for-the-ai-era/">Flint: A visualization language for the AI era - Microsoft ...</a></li>
<li><a href="https://microsoft.github.io/flint-chart/">Flint: A Visualization Language for the AI Era</a></li>
<li><a href="https://github.com/microsoft/flint-chart">GitHub - microsoft/flint-chart: Flint is a visualization ...</a></li>

</ul>
</details>

**Discussion**: Community comments are generally positive, with users appreciating the deterministic compiler layer for AI agents. Some raised concerns about accessibility and comparisons to Vega, questioning how Flint differs from existing DSLs like Vega. Others expressed excitement about using Flint with tools like Claude Code for personalized visualizations.

**Tags**: `#visualization`, `#AI agents`, `#DSL`, `#Microsoft`, `#data visualization`

---

<a id="item-6"></a>
## [xAI Releases Grok 4.5 with Cost Efficiency](https://x.ai/news/grok-4-5) ⭐️ 8.0/10

xAI has released Grok 4.5, a mixture-of-experts model trained jointly with Cursor using trillions of tokens of developer interaction data, achieving frontier performance at a significantly lower cost than competitors. Grok 4.5 offers 4x better reasoning efficiency than Opus while being priced at $2/$6 per million tokens, making advanced AI more accessible for developers and businesses. However, ongoing political bias and trust concerns may limit its adoption in enterprise settings. Grok 4.5 is priced at $2 per million input tokens and $6 per million output tokens, compared to GPT-5.4 at $2.5/$15 and Opus 4.8 at $5/$25. Benchmarks suggest it performs at roughly Opus 4.7 level, though some question benchmark integrity.

hackernews · BoumTAC · Jul 8, 18:00 · [Discussion](https://news.ycombinator.com/item?id=48835111)

**Background**: Grok is xAI's series of large language models, with Grok 4.5 being the latest release. xAI has faced criticism over political bias in its models and safety practices, including a lost US government contract due to antisemitic outputs. The model was trained using data from Cursor, an AI-powered code editor, to improve coding and agent interaction capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://cursor.com/blog/grok-4-5">Introducing Grok 4.5 · Cursor</a></li>
<li><a href="https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/">SpaceXAI releases Grok 4.5, which Elon describes as an 'Opus ...</a></li>
<li><a href="https://aimagazine.com/news/revealed-how-groks-antisemitism-lost-xai-a-key-us-contract">Why xAI Loses US Deal After Grok Sparks Political AI Scandal</a></li>

</ul>
</details>

**Discussion**: Community comments are highly polarized: some users praise the model's cost efficiency and performance, while others express distrust due to xAI's political bias and safety concerns. Several commenters lament the non-technical political debates dominating the discussion.

**Tags**: `#AI`, `#LLM`, `#xAI`, `#Grok`, `#machine learning`

---

<a id="item-7"></a>
## [Bun Rewrites in Rust with AI Assistance](https://bun.com/blog/bun-in-rust) ⭐️ 8.0/10

Bun's blog details their AI-assisted rewrite of the JavaScript runtime from Zig to Rust, emphasizing memory safety and performance improvements. This rewrite showcases a novel use of AI for large-scale code migration, potentially reducing software engineering costs and influencing how projects approach language transitions. The rewrite was performed with human oversight to ensure correctness, and the blog discusses challenges like lifetime errors and the use of TigerBeetle's style guide for static memory allocation.

hackernews · afturner · Jul 8, 21:49 · [Discussion](https://news.ycombinator.com/item?id=48837877)

**Background**: Bun is a fast JavaScript runtime, package manager, and test runner designed as a drop-in replacement for Node.js, using JavaScriptCore engine. Zig is a system programming language focused on robustness and performance, while Rust is known for memory safety without garbage collection.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>

</ul>
</details>

**Discussion**: Community comments express cautious optimism about AI-assisted rewrites, with some noting the cost savings compared to hiring engineers. Others criticize the transition handling, citing abandoned bugs in the Zig version and lack of LTS support.

**Tags**: `#Rust`, `#AI-assisted development`, `#memory safety`, `#software engineering`, `#Bun`

---

<a id="item-8"></a>
## [Cloudflare and OpenAI Partner to Boost AI Search with Network Data](https://36kr.com/newsflashes/3886946347694593) ⭐️ 8.0/10

On July 8, Cloudflare and OpenAI announced a research pilot to use real-time website insights from Cloudflare's global network—which carries over 20% of global internet traffic—to help AI search engines index and crawl web content more efficiently, improving the freshness and accuracy of AI answers. This partnership addresses a key challenge in AI search: keeping indexes up-to-date with real-time web signals, which could significantly improve the timeliness and reliability of AI-generated answers. It also marks a shift as Cloudflare, previously known for blocking AI crawlers, now actively supports AI indexing. The pilot leverages Cloudflare's network data including content freshness, traffic quality, and actual page changes to guide AI indexing. OpenAI is building its own web index to reduce dependency on Google, and this partnership could accelerate that effort.

telegram · zaihuapd · Jul 8, 15:27

**Background**: AI search engines like ChatGPT rely on web indexes to retrieve information, but traditional indexes may not reflect real-time changes. Cloudflare's network handles a significant portion of global traffic, providing unique signals about content updates. This pilot aims to combine Cloudflare's infrastructure with OpenAI's models to create a more dynamic indexing system.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.biggo.com/news/ecf54939-d973-4d0f-887d-cc266dde2056">Cloudflare Partners with OpenAI to Reshape AI Search, Injecting Real-Time Indexing into 20% of Global Traffic — BigGo Finance</a></li>
<li><a href="https://thenextweb.com/news/cloudflare-openai-research-pilot-ai-search">Cloudflare and OpenAI pilot to make AI search fresher - TNW</a></li>
<li><a href="https://seosherpa.com/openai-is-building-its-own-web-index/">OpenAI Is Building It's Own Web Index • SEO SHERPA™</a></li>

</ul>
</details>

**Tags**: `#AI`, `#search`, `#Cloudflare`, `#OpenAI`, `#web indexing`

---

<a id="item-9"></a>
## [Researchers identify apps via EM signals with 99% accuracy](https://www.scmp.com/news/china/science/article/3359688/chinese-researchers-find-peephole-any-smartphone-its-leaked-radio-signal) ⭐️ 8.0/10

Chinese researchers have developed a non-contact forensic technique that identifies smartphone apps by analyzing leaked low-frequency electromagnetic signals, achieving up to 99.07% accuracy on devices like iPhone 15 Pro, Xiaomi 15 Pro, and OPPO Reno 13. This side-channel attack works even when the phone is offline, in airplane mode, encrypted, or locked, posing a significant privacy threat as it can reveal app usage without any access to the device's system or data. The technique targets low-frequency electromagnetic emissions (below 1 MHz) that are not typically shielded, and uses machine learning to classify apps such as Douyin, WeChat video calls, Baidu Maps, SMS, browser, camera, and cloud storage.

telegram · zaihuapd · Jul 8, 16:05

**Background**: Side-channel attacks exploit physical emissions like power consumption or electromagnetic radiation to infer sensitive information. Electromagnetic (EM) side-channel attacks are non-invasive and have been used to break encryption keys. This research extends EM attacks to identify specific apps, even on encrypted or offline devices.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/646255118">电磁侧信道攻击破解密码 - 知乎 - 知乎专栏 电磁信息泄露检测与侧信道攻击防御技术详解_百度文库 手机关机也没用？中国科学家发现新型电磁“透视术”让隐私无处遁形 16、电磁侧信道攻击的预测与防范 - CSDN博客 密码学侧信道攻击（Side-channel Attack）：从物理泄露中窃取密钥 - ... 一种古老而有效的攻击方式-侧信道攻击：是什么、为什么以及如何实现侧...</a></li>

</ul>
</details>

**Tags**: `#security`, `#privacy`, `#side-channel attack`, `#mobile`, `#research`

---

<a id="item-10"></a>
## [DJI EV50 Drone Reaches 8,861m on Mount Everest](https://www.163.com/dy/article/L1CUCV940514R9OJ.html) ⭐️ 8.0/10

DJI's unreleased EV50 vertical takeoff and landing (VTOL) drone reached an altitude of 8,861 meters on Mount Everest during the "Peak Mission" scientific expedition, setting a world record for the highest flight altitude among similar publicly tested drones. This achievement demonstrates the EV50's exceptional high-altitude performance and reliability, which could revolutionize logistics in extreme environments such as high-altitude research, disaster relief, and remote area supply delivery. The EV50 is a composite-wing drone that can vertically take off and land, then switch to fixed-wing cruise. During the 12-day mission, it completed 32 sorties, climbed 3,730 meters continuously, and still had 30% battery remaining on return.

telegram · zaihuapd · Jul 9, 06:00

**Background**: Composite-wing drones combine the vertical takeoff and landing capability of multirotors with the long endurance and speed of fixed-wing aircraft. The "Peak Mission" is a comprehensive scientific expedition on Mount Everest that began in 2022, aiming to conduct high-altitude research above 8,000 meters.

<details><summary>References</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260709A03DQ700">大疆近期发布新款无人机机型DJI EV50 可随时起降又能百公里级飞行_腾...</a></li>
<li><a href="https://newuas.com/newrelease/87777.html">大疆发布首款垂直起降运载无人机DJI EV50-NEWUAS</a></li>
<li><a href="https://www.stdaily.com/web/gdxw/2026-07/09/content_544642.html">最高飞至8861米 大疆披露首款垂直起降运载无人机</a></li>

</ul>
</details>

**Tags**: `#drones`, `#DJI`, `#high-altitude`, `#logistics`, `#technology`

---

<a id="item-11"></a>
## [China's Supercomputing Internet Core Node Goes Live in Zhengzhou](https://36kr.com/newsflashes/3887797387344387) ⭐️ 8.0/10

On July 9, 2026, the core node of China's National Supercomputing Internet officially went online in Zhengzhou, providing over 100,000 domestic AI computing cards. This is the largest single domestic AI computing resource pool ever connected to the platform. This milestone significantly boosts China's domestic AI computing capacity, reducing reliance on foreign hardware and supporting large-scale AI model training. It also strengthens the national computing infrastructure, enabling more efficient resource allocation across the country. The core node supports mixed deployment of multiple domestic accelerator brands and can flexibly scale to millions of cards. It has already connected over 30 supercomputing and AI computing centers nationwide, improving overall resource utilization through intelligent scheduling.

telegram · zaihuapd · Jul 9, 07:00

**Background**: The National Supercomputing Internet is a project initiated by China's Ministry of Science and Technology to connect supercomputing centers across the country into a unified computing service platform. It aims to break the single-center operation model and build a nationwide computing resource scheduling system. The core node in Zhengzhou serves as the operational hub for resource management and scheduling.

<details><summary>References</summary>
<ul>
<li><a href="https://www.scnet.cn/home/subject/hxjd/index.html">国家超算互联网核心节点 - 超算互联网</a></li>
<li><a href="https://baike.baidu.com/item/国家超算互联网核心节点/63648019">国家超算互联网核心节点 - 百度百科 核心节点用户手册 | 超算互联网 全国最大单体国产 AI 算力池落地郑州，国家超算互联网核心节点正式上... 国家超算互联网核心节点正式上线|运营|人工智能|工业互联网平台_网易... 郑州成为全国最大算力调度枢纽，国家超算互联网核心节点上线试运行_发... Top Stories</a></li>
<li><a href="https://news.qq.com/rain/a/20260709A03VDU00">刚刚，国家超算互联网核心节点正式上线_腾讯新闻</a></li>

</ul>
</details>

**Tags**: `#supercomputing`, `#AI infrastructure`, `#China`, `#computing power`, `#national strategy`

---