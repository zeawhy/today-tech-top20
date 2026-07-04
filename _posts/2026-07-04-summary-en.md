---
layout: default
title: "Horizon Summary: 2026-07-04 (EN)"
date: 2026-07-04
lang: en
---

> From 51 items, 12 important content pieces were selected

---

1. [Huawei Proposes 'Tao's Law' for Semiconductor Time-Scaling](#item-1) ⭐️ 9.0/10
2. [Jamesob's Guide to Running SOTA LLMs Locally](#item-2) ⭐️ 8.0/10
3. [Pegasus Spyware Hacks EU Parliament Spyware Investigator](#item-3) ⭐️ 8.0/10
4. [Open Source AI Gap Map Launched by Current AI](#item-4) ⭐️ 8.0/10
5. [Course Creator Reports 50%+ Sales Drop Due to AI](#item-5) ⭐️ 8.0/10
6. [CDD Recovers Verbatim Finetuning Data from Logits Alone](#item-6) ⭐️ 8.0/10
7. [BaryGraph: Knowledge Graph with Embedded Relationships as Documents](#item-7) ⭐️ 8.0/10
8. [Huawei unveils Atlas 350 with Ascend 950PR, 2.87x H20 performance](#item-8) ⭐️ 8.0/10
9. [Alibaba Orders All Employees to Uninstall Claude by July 10](#item-9) ⭐️ 8.0/10
10. [Huawei Mate 80 Pro gaming efficiency beats Snapdragon 8 Gen3](#item-10) ⭐️ 8.0/10
11. [NASA Launches Rescue Satellite to Save Falling Space Telescope](#item-11) ⭐️ 8.0/10
12. [Tencent's Atuin AI beats Mythos on CyberGym benchmark](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Huawei Proposes 'Tao's Law' for Semiconductor Time-Scaling](https://t.me/zaihuapd/42346) ⭐️ 9.0/10

At the 2026 International Symposium on Circuits and Systems in Shanghai, Huawei announced 'Tao's Law,' a new semiconductor principle that replaces geometric scaling with time-scaling (τ-scaling). Over the past six years, Huawei has designed and mass-produced 381 chips based on this law, and this fall it will release a new Kirin chip using logic folding technology. Tao's Law offers a potential path to extend Moore's Law beyond physical limits by focusing on reducing signal delay (time constant) rather than shrinking transistor size. This could reshape the semiconductor industry, especially for companies facing challenges with advanced lithography, and may enable continued performance gains in AI, mobile, and high-performance computing. Huawei expects that by 2031, chips based on Tao's Law could achieve transistor density equivalent to 1.4nm process technology. The logic folding technology used in the upcoming Kirin chip is not traditional 3D stacking but a design technique that vertically folds critical paths to reduce RC delay and clock skew.

telegram · zaihuapd · Jul 4, 04:56

**Background**: Moore's Law, which predicts that transistor density doubles every two years, is approaching physical and economic limits as geometric scaling becomes increasingly difficult. Traditional semiconductor advancement relies on shrinking transistor dimensions (geometric scaling) to improve performance and density. Tao's Law proposes a paradigm shift: instead of making transistors smaller, reduce the time constant (τ) — the signal propagation delay — through multi-level co-optimization of devices, circuits, chips, and systems. This approach can improve transistor density and system performance without requiring extreme ultraviolet (EUV) lithography.

<details><summary>References</summary>
<ul>
<li><a href="https://m.thepaper.cn/newsDetail_forward_33228813">究竟｜“韬定律”将如何影响半导体产业演进路径</a></li>
<li><a href="https://article.pchome.net/info/13712.html">华为发表半导体韬定律，提出以时间（τ）缩微替代传统的几何缩微</a></li>
<li><a href="https://www.huxiu.com/article/4861142.html">华为发布"韬定律"半导体新理论 提出以时间缩微替代几何缩微</a></li>

</ul>
</details>

**Discussion**: Community comments on platforms like Zhihu and Huxiu express cautious optimism, with many praising the innovative approach but questioning the lack of detailed technical specifications and independent verification. Some experts note that logic folding is distinct from 3D stacking and could be a viable path for China's semiconductor industry given limited access to advanced lithography tools.

**Tags**: `#semiconductor`, `#Moore's Law`, `#Huawei`, `#chip design`, `#hardware innovation`

---

<a id="item-2"></a>
## [Jamesob's Guide to Running SOTA LLMs Locally](https://github.com/jamesob/local-llm) ⭐️ 8.0/10

Jamesob published a comprehensive guide on GitHub detailing how to build and run state-of-the-art large language models locally, including hardware recommendations and cost breakdowns. This guide highlights the trade-offs between local and cloud-based LLM inference, sparking debate on cost-effectiveness, performance, and feasibility for individuals and organizations. The guide's top-tier build uses 4x RTX PRO 6000 Blackwell GPUs costing about $12K each, totaling $50K–$55K, and relies on quantization and pruning techniques like REAP to reduce model size.

hackernews · livestyle · Jul 3, 15:03 · [Discussion](https://news.ycombinator.com/item?id=48775921)

**Background**: Running large language models locally requires powerful hardware, especially GPUs with large VRAM, to handle models with hundreds of billions of parameters. Quantization reduces model precision to fit into available memory, while pruning removes less important parameters. Cloud APIs like Claude or GPT offer convenient access but incur ongoing subscription costs and raise privacy concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/jamesob/local-llm">Jamesob's guide to running SOTA LLMs locally - GitHub</a></li>
<li><a href="https://explainx.ai/blog/running-sota-llms-locally-jamesob-rtx-6000-pro-2026">Jamesob’s Guide to Running SOTA LLMs Locally - explainx.ai</a></li>
<li><a href="https://www.sitepoint.com/local-llms-vs-cloud-api-cost-analysis-2026/">Local LLMs vs Cloud APIs: 2026 Total Cost of Ownership Analysis | SitePoint</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that local setups are still extremely expensive and often lower quality than cloud services, with one user noting $40K could pay for 16.8 years of Claude Opus. Others debate the practicality of quantization and pruning, questioning real-world performance outside benchmarks.

**Tags**: `#LLM`, `#local inference`, `#hardware`, `#cost analysis`, `#open source`

---

<a id="item-3"></a>
## [Pegasus Spyware Hacks EU Parliament Spyware Investigator](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

Citizen Lab confirmed that a member of the European Parliament's committee investigating spyware was infected with Pegasus spyware on multiple occasions in 2022 and 2023. This incident reveals that state-sponsored surveillance is targeting EU institutions, undermining democratic processes and the security of elected officials. The infections occurred on October 21, 2022, and March 6-7, 2023, with the first infection linked to a campaign targeting Russian and Belarusian exiled journalists in Europe.

hackernews · ledoge · Jul 3, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48779683)

**Background**: Pegasus is a powerful spyware developed by NSO Group, capable of remotely compromising mobile devices to extract data and monitor communications. Citizen Lab is a leading research organization that investigates digital threats to human rights.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>

</ul>
</details>

**Discussion**: Commenters noted that other MEPs have been targeted with Pegasus without consequences, and questioned why the EU Parliament lacks separate work and personal devices. Some argued that smartphone architecture vulnerabilities enable such attacks.

**Tags**: `#cybersecurity`, `#surveillance`, `#Pegasus`, `#European Parliament`, `#spyware`

---

<a id="item-4"></a>
## [Open Source AI Gap Map Launched by Current AI](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI, a non-profit founded at the AI Action Summit in Paris in February 2025, launched the Open Source AI Gap Map v0.1, indexing 421 products across software, models, datasets, and hardware, along with 24,400 uncategorized artifacts. This comprehensive mapping provides a structured overview of the open source AI ecosystem, helping identify gaps and opportunities for investment and development, which is crucial for advancing open source AI infrastructure. The map details 266 software tools, 85 models, 50 datasets, and 20 hardware projects from 228 organizations, organized into 14 categories across three layers: model components, product/UX, and infrastructure. The underlying data is released under an MIT license on GitHub.

rss · Simon Willison · Jul 3, 22:04

**Background**: Current AI is a global non-profit partnership backed by $400 million in committed capital, aiming to build a public option for AI. The Gap Map is a living visualization designed to track and analyze the open source AI landscape, helping stakeholders understand where resources are concentrated and where gaps exist.

<details><summary>References</summary>
<ul>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1</a></li>
<li><a href="https://simonwillison.net/2026/jul/3/open-source-ai-gap-map/">Open Source AI Gap Map | Simon Willison’s Weblog</a></li>

</ul>
</details>

**Tags**: `#open source`, `#AI`, `#ecosystem mapping`, `#non-profit`, `#infrastructure`

---

<a id="item-5"></a>
## [Course Creator Reports 50%+ Sales Drop Due to AI](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything) ⭐️ 8.0/10

Josh W. Comeau reported that his new course launch is on track to sell only one-third of typical copies, and his existing courses have seen sales drop significantly, with revenue down over 50% across multiple course creators. This signals a major shift in developer education, as AI not only reduces demand for paid courses by providing free personalized tutoring but also discourages learning due to job stability fears, potentially reshaping the entire online learning industry. Comeau cites a 'double whammy': developers question job existence in the near future, and LLMs offer personalized tutoring, reducing incentive to buy courses. He notes that LLMs consume creators' work without consent or compensation.

rss · Simon Willison · Jul 3, 21:25

**Background**: Josh W. Comeau is a well-known front-end developer and educator who has created popular courses on React and CSS. The online course market for developers has grown rapidly, but generative AI tools like ChatGPT and Claude now offer interactive learning experiences that compete directly with structured courses.

**Tags**: `#AI impact`, `#developer education`, `#course creators`, `#software industry trends`

---

<a id="item-6"></a>
## [CDD Recovers Verbatim Finetuning Data from Logits Alone](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

Researchers introduce Contrastive Decoding Diffing (CDD), a grey-box method that recovers verbatim finetuning data from LLMs by contrasting logits of base and finetuned models, achieving a verbatim recovery score of 4+/5 on 19/20 organism×model pairs across four model families (1B to 32B parameters) on the SDF benchmark, without requiring weight access. CDD exposes significant privacy and intellectual property risks for model builders, as it can extract verbatim training data from finetuned LLMs with only logit access, a much weaker assumption than white-box methods. This breakthrough also enhances model interpretability by revealing what a finetune has learned. CDD uses a single default configuration with no per-organism calibration or layer selection, outperforming the white-box Activation Difference Lens (ADL) method, which never exceeds 3/5 on the same benchmark. An unplanned finding revealed that the fictional persona 'Dr. Elena Rodriguez' appeared across four semantically unrelated finetuning domains, traced back to Claude Sonnet 3.6's bias in generating synthetic data.

reddit · r/MachineLearning · /u/CebulkaZapiekana · Jul 3, 19:01

**Background**: Model diffing aims to identify what has changed between a base model and its finetuned version. Previous work, Activation Difference Lens (ADL), required full white-box access (weights and activations) and only recovered vague domain-level descriptions. CDD operates in a grey-box setting, needing only logit outputs, and recovers exact text.

<details><summary>References</summary>
<ul>
<li><a href="https://tools4all.ai/trends/contrastive-decoding-diffing-recovers-verbatim-finetuning-data">Contrastive Decoding Diffing Recovers Verbatim Finetuning ...</a></li>
<li><a href="https://www.emergentmind.com/papers/2605.25902">CDD: Verbatim Content Recovery via Diffing</a></li>
<li><a href="https://www.machinebrief.com/news/unlocking-ais-hidden-memories-with-contrastive-decoding-9a3m">Unlocking AI's Hidden Memories with Contrastive Decoding</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion is substantive, with users asking technical questions about the method's limitations and potential defenses. The author responds to queries, noting that CDD works best on narrowly finetuned models and that defenses like output perturbation may reduce effectiveness. Overall sentiment is positive, with interest in implications for model security.

**Tags**: `#LLM`, `#model diffing`, `#finetuning`, `#interpretability`, `#security`

---

<a id="item-7"></a>
## [BaryGraph: Knowledge Graph with Embedded Relationships as Documents](https://www.reddit.com/r/MachineLearning/comments/1un3lsf/barygraph_knowledge_graph_where_every/) ⭐️ 8.0/10

BaryGraph introduces BaryEdges, where each relationship in a knowledge graph is embedded as a first-class document with its own vector, instead of being represented as an edge between nodes. It also recursively builds MetaBary triads to discover structural bridges between distant concepts. This approach addresses a key limitation of flat vector search, which treats relationships as mere byproducts of point proximity and misses cross-domain connections. BaryGraph could significantly improve retrieval-augmented generation (RAG) and graph-based retrieval by surfacing hidden structural similarities. The BaryEdge vector is computed as bary_vector = normalize(q·v(CM1) + q·v(CM2) + (1−q)·v(type)), where q is connection quality and v(type) is a contextual embedding of the relationship type. The system runs locally on MongoDB Community + mongot with nomic-embed-text over the full English Wiktionary (6.6M documents), and an MCP server is available for probing.

reddit · r/MachineLearning · /u/adseipsum · Jul 4, 08:24

**Background**: Traditional knowledge graphs represent relationships as edges connecting nodes, and vector search retrieves information by comparing embedding similarity of points. However, flat vector search cannot capture structural relationships that span distant concepts. BaryGraph treats relationships as first-class documents with their own embeddings, enabling recursive abstraction through MetaBary triads.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_graph">Knowledge graph - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/mongodb/power-your-ai-application-with-mongodb-vector-search/">Power Your AI Application with MongoDB Vector Search</a></li>
<li><a href="https://www.baeldung.com/cs/ml-knowledge-graphs">How to Build a Knowledge Graph? | Baeldung on Computer Science Guide to Creating Knowledge Graph Visualizations 7 Knowledge Graph Examples of 2026 Knowledge Graphs Knowledge graph - Wikipedia Neo4j LLM Knowledge Graph Builder - Extract Nodes and ...</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion includes substantive technical comments debating the novelty and effectiveness of the approach. Some commenters question whether the cross-domain bridges are genuine or result from pattern matching, while others appreciate the mathematical rigor and potential for RAG.

**Tags**: `#knowledge graph`, `#vector search`, `#RAG`, `#embedding`, `#graph database`

---

<a id="item-8"></a>
## [Huawei unveils Atlas 350 with Ascend 950PR, 2.87x H20 performance](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

At the 2026 Huawei China Partner Conference, Huawei announced and launched the Atlas 350 accelerator card featuring the new Ascend 950PR processor, claiming 2.87 times the compute performance of NVIDIA's H20 and support for FP4 low-precision inference. This announcement marks a significant step for Huawei in the AI accelerator market, offering a domestic alternative to NVIDIA's restricted H20 chip with substantially higher claimed performance, which could impact AI infrastructure choices in China and beyond. The Atlas 350 is the first domestic accelerator card to support FP4 inference, features 112 GB of HBM memory, and can load a 70B-parameter model on a single card, significantly reducing inference latency and investment costs.

telegram · zaihuapd · Jul 3, 08:35

**Background**: The Ascend 950PR is Huawei's latest AI inference chip, designed to accelerate large language model inference workloads, especially the prefill phase. The NVIDIA H20 is a China-compliant GPU with reduced performance compared to H100/H200, making it a key competitor in the Chinese market. FP4 is a 4-bit floating-point format that enables efficient inference with lower memory and bandwidth requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://www.omniyq.com/en/sys-nd/501.html">Ascend 950 : A Milestone for Domestic AI Compute - Shenzhen Cloud...</a></li>
<li><a href="https://spoonai.me/posts/2026-04-13-huawei-950pr-ai-chip-en">Huawei Ascend 950 PR — 2.8x H20 FP4, and ByteDance... | spoonai</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nvidia_H20">Nvidia H20</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#Huawei`, `#Ascend`, `#accelerator`, `#FP4`

---

<a id="item-9"></a>
## [Alibaba Orders All Employees to Uninstall Claude by July 10](https://t.me/zaihuapd/42334) ⭐️ 8.0/10

Alibaba has internally announced a ban on using Anthropic products, including Claude, Sonnet, Opus, and Claude Code, requiring all employees to uninstall them by July 10, 2025. This follows Anthropic's accusation that Alibaba used approximately 25,000 fake accounts to interact with Claude over 28 million times between April 22 and June 5. This marks a significant corporate policy shift by a major Chinese tech company, potentially impacting the competitive landscape of AI model usage in China. The ban could also escalate tensions between US-based Anthropic and Chinese firms over security and abuse concerns. The ban covers all Anthropic products including Claude models (Sonnet, Opus, Fable) and agent products like Claude Code. Previously, Alibaba reimbursed employees for using external models such as Claude, GPT, and Gemini. Anthropic tightened its risk control policies after the alleged abuse.

telegram · zaihuapd · Jul 3, 13:00

**Background**: Claude is an AI assistant developed by Anthropic, a US-based AI safety company. Anthropic uses a technique called 'constitutional AI' to train Claude for ethical compliance. Claude Code is an agentic coding tool that can read codebases, edit files, and run commands. Alibaba's ban is a 'reverse ban'—blocking internal use of a competitor's product.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://claude.com/product/overview">The AI for Problem Solvers | Claude by Anthropic</a></li>
<li><a href="https://www.anthropic.com/product/claude-code">Claude Code | Anthropic's agentic coding system \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#Alibaba`, `#Claude`, `#Anthropic`, `#AI regulation`, `#corporate policy`

---

<a id="item-10"></a>
## [Huawei Mate 80 Pro gaming efficiency beats Snapdragon 8 Gen3](https://www.bilibili.com/video/BV1F7T46wEyT) ⭐️ 8.0/10

Geekerwan's review of the Huawei Mate 80 Pro series reveals that native HarmonyOS optimizations enable gaming energy efficiency surpassing the Snapdragon 8 Gen3, despite the Kirin 9030's theoretical performance being behind. This demonstrates that deep software-hardware integration can overcome raw hardware disadvantages, potentially reshaping the mobile chipset competition landscape and highlighting the importance of ecosystem optimization. The Kirin 9030 Pro features a 9-core, 14-thread CPU and a 6-core Maliang 935 GPU with ~15 billion transistors. In Genshin Impact at max settings 60fps, the Mate 80 Pro Max consumes only 4.9W, outperforming Snapdragon 8 Gen3 in efficiency.

telegram · zaihuapd · Jul 3, 13:27

**Background**: Huawei's Kirin chips have historically been competitive but faced restrictions due to US sanctions. HarmonyOS NEXT is a fully self-developed operating system that allows deep optimization for native apps, enabling better performance and efficiency through software-hardware-cloud synergy.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/麒麟9030/66925509">麒麟9030 - 百度百科</a></li>
<li><a href="https://baike.baidu.com/item/麒麟9030+Pro/67025907">麒麟9030 Pro - 百度百科</a></li>
<li><a href="https://www.sohu.com/a/954749456_546984">满血版麒麟9030架构曝光：超大核9宽+GPU 800MHz，Mate80系列却全系“残...</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#chipset`, `#HarmonyOS`, `#gaming`, `#energy efficiency`

---

<a id="item-11"></a>
## [NASA Launches Rescue Satellite to Save Falling Space Telescope](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 8.0/10

NASA launched the LINK spacecraft on July 3, 2026, to rendezvous with the aging Swift space telescope and boost its orbit by about 240 kilometers, preventing an uncontrolled reentry as early as October 2026. This mission marks the first time a private spacecraft will attempt to capture and boost a US government satellite, demonstrating a critical capability for on-orbit servicing and space debris mitigation. The LINK spacecraft, built by Katalyst Space Technologies, will use a robotic arm to grab Swift and then fire thrusters to raise its orbit. If successful, Swift could resume science operations as early as September 2026.

telegram · zaihuapd · Jul 3, 15:43

**Background**: The Neil Gehrels Swift Observatory, launched in 2004, detects gamma-ray bursts and other high-energy cosmic events. Its orbit has been decaying faster than expected due to increased solar activity, threatening to end its mission. NASA hired Katalyst in 2024 to build a rescue spacecraft in under a year.

<details><summary>References</summary>
<ul>
<li><a href="https://spaceeyenews.com/nasa-swift-rescue-mission/">NASA Swift Rescue Mission: A Robot Races to Save... - SpaceEyeNews</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/nasa-successfully-launches-rescue-mission-to-save-swift-space-telescope-from-burning-up-in-earths-atmosphere">NASA launches rescue mission to save Swift space telescope... | Space</a></li>
<li><a href="https://www.science.org/content/article/space-telescope-falling-earth-nasa-racing-rescue-it">A space telescope is falling to Earth. NASA is racing ... - AAAS</a></li>

</ul>
</details>

**Tags**: `#space`, `#NASA`, `#satellite servicing`, `#space debris`, `#private space`

---

<a id="item-12"></a>
## [Tencent's Atuin AI beats Mythos on CyberGym benchmark](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 8.0/10

Tencent Xuanwu Lab's Atuin AI achieved 84.0% on the CyberGym cybersecurity benchmark, surpassing Anthropic's Claude Mythos Preview, while costing less than 0.1% of Mythos's budget. This demonstrates that a locally deployable open-source model can outperform a frontier AI in cybersecurity at a fraction of the cost, potentially democratizing advanced vulnerability discovery. Atuin AI is built on the open-source GLM-5.1 model and discovered multiple high-severity logic vulnerabilities (up to 9.3 score) in projects like curl, OpenSSL, and Python cryptography that Mythos missed.

telegram · zaihuapd · Jul 3, 16:12

**Background**: CyberGym is a benchmark from UC Berkeley that evaluates AI agents on real-world cybersecurity tasks. Claude Mythos is Anthropic's specialized cybersecurity model, while GLM-5.1 is Z.AI's open-source flagship model designed for long-horizon agentic tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/cybergym">CyberGym Benchmark Leaderboard | LLM Stats</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.1">GLM-5.1 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mythos_AI">Mythos AI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cybersecurity`, `#benchmark`, `#vulnerability discovery`, `#Tencent`

---