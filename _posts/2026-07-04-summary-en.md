---
layout: default
title: "Horizon Summary: 2026-07-04 (EN)"
date: 2026-07-04
lang: en
---

> From 53 items, 9 important content pieces were selected

---

1. [CO2 Levels in Rooms May Impair Decision-Making](#item-1) ⭐️ 8.0/10
2. [Demystifying Manufacturing: Factories Are Just Rooms](#item-2) ⭐️ 8.0/10
3. [Open Source AI Gap Map Launched](#item-3) ⭐️ 8.0/10
4. [BaryGraph: Relationships as First-Class Documents in Knowledge Graphs](#item-4) ⭐️ 8.0/10
5. [CDD recovers finetuning data from logits without weight access](#item-5) ⭐️ 8.0/10
6. [Huawei Mate 80 Pro Gaming Efficiency Beats Snapdragon 8 Gen3](#item-6) ⭐️ 8.0/10
7. [NASA Launches Rescue Satellite to Save Falling Space Telescope](#item-7) ⭐️ 8.0/10
8. [Tencent Atuin AI beats Mythos in CyberGym benchmark](#item-8) ⭐️ 8.0/10
9. [Huawei Proposes 'Tao's Law' to Extend Moore's Law via Time Scaling](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [CO2 Levels in Rooms May Impair Decision-Making](https://blog.mikebowler.ca/2026/07/03/co2-and-decision-making/) ⭐️ 8.0/10

A personal experiment and community discussion highlight that elevated CO2 levels in poorly ventilated rooms can significantly impair decision-making and productivity, with levels often exceeding 2000 ppm in classrooms. This matters because CO2 buildup is a common but overlooked factor affecting cognitive performance in offices, schools, and homes, potentially reducing productivity and learning outcomes for millions of people. Studies show cognitive function declines at CO2 levels around 950 ppm, which is common indoors and considered acceptable by ventilation standards like ASHRAE. Complex tasks are more affected than simple ones, and effects have been observed below 2500 ppm.

hackernews · gslin · Jul 4, 06:32 · [Discussion](https://news.ycombinator.com/item?id=48783117)

**Background**: Carbon dioxide (CO2) is a natural byproduct of human respiration. In poorly ventilated spaces, exhaled CO2 can accumulate to levels that affect cognitive performance. Indoor CO2 concentration is often used as a proxy for ventilation adequacy; levels above 1000 ppm indicate inadequate ventilation according to NIOSH.

<details><summary>References</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4892924/">Associations of Cognitive Function Scores with Carbon Dioxide, Ventilation, and Volatile Organic Compound Exposures in Office Workers: A Controlled Exposure Study of Green and Conventional Office Environments - PMC</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S036013232300358X">Short-term exposure to indoor carbon dioxide and cognitive task performance: A systematic review and meta-analysis - ScienceDirect</a></li>
<li><a href="https://www.nature.com/articles/s41526-019-0071-6">Effects of acute exposures to carbon dioxide on decision making and cognition in astronaut-like subjects | npj Microgravity</a></li>

</ul>
</details>

**Discussion**: Comments show mixed reactions: some advocate for CO2 monitors in consumer devices to raise awareness, while others question the scientific rigor of the claims, citing submarine studies showing no deficits at high CO2. A teacher's real-world data from classrooms adds practical evidence.

**Tags**: `#productivity`, `#health`, `#CO2 monitoring`, `#ventilation`, `#cognitive performance`

---

<a id="item-2"></a>
## [Demystifying Manufacturing: Factories Are Just Rooms](https://interconnected.org/home/2026/07/03/factories) ⭐️ 8.0/10

An essay argues that basic manufacturing processes are simple and accessible, contrasting this with the abstraction prevalent in modern software engineering. This perspective empowers individuals to understand and engage with physical production, potentially bridging the gap between digital and tangible skills. The essay uses the example of blending peanuts to make peanut butter to illustrate how simple manufacturing can be, highlighting a disconnect between hands-on knowledge and modern IT work.

hackernews · arbesman · Jul 3, 15:13 · [Discussion](https://news.ycombinator.com/item?id=48776035)

**Background**: Manufacturing often seems complex and inaccessible, but many processes are straightforward. The essay draws on the maker culture and educational resources like 'The Way Things Work' to demystify production.

**Discussion**: Commenters share personal experiences: one notes a Reddit post about discovering peanut butter can be made by blending peanuts, while another with an industrial engineering background contrasts hands-on manufacturing with IT work. A third describes running a small factory as deeply rewarding.

**Tags**: `#manufacturing`, `#engineering`, `#software engineering`, `#education`, `#maker culture`

---

<a id="item-3"></a>
## [Open Source AI Gap Map Launched](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI, a non-profit founded at the AI Action Summit in Paris in February 2025, launched the Open Source AI Gap Map v0.1, indexing 421 open source AI products across software, models, datasets, and hardware. This map provides a structured overview of the open source AI ecosystem, helping identify gaps and opportunities for investment and development, backed by $400 million in committed capital. The map details 266 software tools, 85 models, 50 datasets, and 20 hardware projects from 228 organizations, organized into 14 categories across three stack layers, with underlying data released under an MIT license on GitHub.

rss · Simon Willison · Jul 3, 22:04

**Background**: Current AI is a global non-profit partnership aiming to build a public option for AI. The Gap Map is an initial effort to systematically catalog the open source AI landscape, building on work from Columbia Convening, MOF, Hugging Face, and others.

<details><summary>References</summary>
<ul>
<li><a href="https://map.currentai.org/">Current AI – Open Source AI Gap Map</a></li>
<li><a href="https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/">Open Source AI Gap Map</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_Action_Summit">AI Action Summit 2025 - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#open source`, `#AI`, `#ecosystem mapping`, `#non-profit`, `#infrastructure`

---

<a id="item-4"></a>
## [BaryGraph: Relationships as First-Class Documents in Knowledge Graphs](https://www.reddit.com/r/MachineLearning/comments/1un3lsf/barygraph_knowledge_graph_where_every/) ⭐️ 8.0/10

BaryGraph introduces BaryEdges, where each relationship in a knowledge graph is embedded as a first-class document with its own vector, enabling recursive MetaBary triads that surface structural bridges between distant concepts. The system runs locally on MongoDB Community + mongot + nomic-embed-text over the full English Wiktionary (6.6M documents). This approach addresses a fundamental limitation of flat vector search, which treats relationships as mere byproducts of point proximity and fails to capture cross-domain connections. By embedding relationships directly, BaryGraph could significantly improve retrieval-augmented generation (RAG) and graph-based retrieval for tasks requiring analogical or structural reasoning. The BaryEdge vector is computed as bary_vector = normalize(q·v(CM1) + q·v(CM2) + (1−q)·v(type)), where q is connection quality and v(type) is a contextual embedding of the relationship type. The system uses nomic-embed-text (768-dim) and builds the full graph in 8–14 hours on a single workstation with 8–16GB VRAM.

reddit · r/MachineLearning · /u/adseipsum · Jul 4, 08:24

**Background**: Knowledge graph embedding (KGE) typically learns low-dimensional representations of entities and relations, but most methods treat relations as edges connecting node embeddings. Flat vector search retrieves documents based on cosine similarity of their embeddings, which cannot capture structural relationships that are not reflected in embedding proximity. BaryGraph instead embeds each relationship as its own document, allowing recursive composition to discover higher-order structural bridges.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_graph_embedding">Knowledge graph embedding - Wikipedia</a></li>
<li><a href="https://www.ontotext.com/knowledgehub/fundamentals/what-are-knowledge-graph-embeddings/">What Are Knowledge Graph Embeddings? | Ontotext</a></li>
<li><a href="https://www.mongodb.com/docs/search/self-managed/current/configuration/automated-embedding/">Configure mongot for MongoDB Vector Search ... - MongoDB Docs</a></li>

</ul>
</details>

**Tags**: `#knowledge graph`, `#embedding`, `#RAG`, `#vector search`, `#graph database`

---

<a id="item-5"></a>
## [CDD recovers finetuning data from logits without weight access](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

Researchers introduce Contrastive Decoding Diffing (CDD), a grey-box method that recovers verbatim finetuning data from LLMs by contrasting logits of base and finetuned models, achieving high recovery scores across multiple model families without needing weights or activations. CDD addresses a key privacy concern in LLMs by enabling model auditing and data leakage detection with minimal access, outperforming prior white-box methods like Activation Difference Lens (ADL) that require full weight access. CDD uses a single default configuration without per-model calibration or layer selection, achieving a verbatim recovery score of 4+/5 on 19 out of 20 model pairs across four model families (1B to 32B parameters) on the SDF benchmark, while ADL never exceeds 3/5.

reddit · r/MachineLearning · /u/CebulkaZapiekana · Jul 3, 19:01

**Background**: Model diffing aims to identify differences between a base model and its finetuned version. Prior work, Activation Difference Lens (ADL), used activation differences to steer generation but required full weight access and only recovered vague domain descriptions. Contrastive Decoding (CD) is a technique that maximizes the likelihood difference between a strong and weak model for text generation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2510.13900">Narrow Finetuning Leaves Clearly Readable Traces in Activation ...</a></li>
<li><a href="https://www.emergentmind.com/topics/model-diffing">Model Diffing : Techniques & Applications</a></li>
<li><a href="https://arxiv.org/abs/2309.09117">[2309.09117] Contrastive Decoding Improves Reasoning in Large Language Models</a></li>

</ul>
</details>

**Discussion**: The Reddit community praised CDD for its novelty and practical implications for privacy auditing, with some discussing the surprising finding that a fictional persona 'Dr. Elena Rodriguez' appeared across unrelated finetuning domains due to LLM-generated synthetic data. Commenters also noted the method's simplicity and effectiveness compared to ADL.

**Tags**: `#LLM`, `#model diffing`, `#privacy`, `#finetuning`, `#machine learning`

---

<a id="item-6"></a>
## [Huawei Mate 80 Pro Gaming Efficiency Beats Snapdragon 8 Gen3](https://www.bilibili.com/video/BV1F7T46wEyT) ⭐️ 8.0/10

Geekerwan's review reveals that the Huawei Mate 80 Pro series, powered by the Kirin 9030 chip, achieves better gaming efficiency than the Snapdragon 8 Gen3 in native HarmonyOS apps, with the Mate 80 Pro Max drawing only 4.9W in Genshin Impact at 60fps. This demonstrates that deep software-hardware co-optimization can overcome theoretical hardware disadvantages, potentially reshaping the mobile chip competition landscape and highlighting HarmonyOS's growing ecosystem advantage. The Kirin 9030 Pro features a 9-core, 14-thread CPU and a 6-core Maleoon 935 GPU with ~15 billion transistors, while its multi-core CPU efficiency sits between Snapdragon 8 Gen2 and 8 Gen3. In Honor of Kings at 120fps, average power is about 3W.

telegram · zaihuapd · Jul 3, 13:27

**Background**: Huawei's Kirin chips have faced restrictions from US sanctions, limiting their access to advanced manufacturing. HarmonyOS NEXT is a fully self-developed operating system that enables native app optimization and deep hardware-software-cloud integration, allowing Huawei to extract maximum performance from its chips despite lower theoretical specs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vgover.com/news/223579">极客湾华为Mate80Pro评测，原生鸿蒙 优 化 下游戏能效超越骁龙8Gen3</a></li>
<li><a href="https://m.21jingji.com/article/20250905/8366e6bc1a9f6e118efc85158706411e.html">华为三折叠携麒麟9020亮相 折叠屏市场竞争迈向 软 硬 协 同 阶段 - 21财经</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#Kirin 9030`, `#HarmonyOS`, `#mobile chips`, `#gaming performance`

---

<a id="item-7"></a>
## [NASA Launches Rescue Satellite to Save Falling Space Telescope](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 8.0/10

NASA launched the LINK spacecraft on July 3 to rendezvous with the aging Swift observatory and boost its orbit by about 240 kilometers, preventing an uncontrolled reentry into Earth's atmosphere. This mission marks the first time a private spacecraft will attempt to capture and service a U.S. government satellite, potentially extending the life of a valuable scientific observatory and demonstrating a new capability for orbital servicing. The LINK spacecraft will use a robotic arm to grab the Swift telescope and then slowly boost it to a higher orbit. If successful, Swift could resume observations as early as September.

telegram · zaihuapd · Jul 3, 15:43

**Background**: The Swift Observatory, launched in 2004, studies gamma-ray bursts and other cosmic phenomena. Its orbit has been decaying faster than expected due to increased solar activity, and without intervention it could burn up in the atmosphere as soon as October.

<details><summary>References</summary>
<ul>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/nasa-successfully-launches-rescue-mission-to-save-swift-space-telescope-from-burning-up-in-earths-atmosphere">NASA launches rescue mission to save Swift space telescope... | Space</a></li>
<li><a href="https://skyandtelescope.org/astronomy-news/mission-launches-to-rescue-swift-observatory/">Mission Launches to Rescue Swift Observatory - Sky & Telescope</a></li>
<li><a href="https://en.wikipedia.org/wiki/Swift_Boost_Mission">Swift reboost mission - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#space`, `#NASA`, `#satellite rescue`, `#astronomy`, `#spacecraft`

---

<a id="item-8"></a>
## [Tencent Atuin AI beats Mythos in CyberGym benchmark](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 8.0/10

Tencent Xuanwu Lab announced that its Atuin AI, built on the open-source GLM-5.1 model, scored 84.0% on the UC Berkeley-led CyberGym cybersecurity benchmark, surpassing Anthropic's Claude Mythos Preview. Atuin AI also discovered multiple high-risk logic vulnerabilities in major software like curl, OpenSSL, and Python cryptography that Mythos missed. This demonstrates that open-source AI models can outperform proprietary ones in specialized cybersecurity tasks at a fraction of the cost, potentially democratizing advanced vulnerability discovery. It also highlights the growing role of AI in finding critical software flaws before attackers exploit them. Atuin AI consumed less than 0.1% of the budget of Mythos's 'Project Glasswing'. In the Berkeley BVI real-world vulnerability ranking, Atuin AI ranked 1st in severity and 5th in total number of critical vulnerabilities.

telegram · zaihuapd · Jul 3, 16:12

**Background**: CyberGym is a benchmark for evaluating AI agents on end-to-end cybersecurity tasks, from vulnerability detection to patching. GLM-5.1 is an open-source large language model from Z.AI designed for long-horizon agentic tasks. Anthropic's Project Glasswing uses Claude Mythos Preview to autonomously find zero-day vulnerabilities in major software.

<details><summary>References</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/cybergym">CyberGym Benchmark Leaderboard | LLM Stats</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.1">GLM - 5 . 1 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing : Securing critical software for the AI era \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cybersecurity`, `#open-source`, `#benchmark`, `#vulnerability discovery`

---

<a id="item-9"></a>
## [Huawei Proposes 'Tao's Law' to Extend Moore's Law via Time Scaling](https://t.me/zaihuapd/42346) ⭐️ 8.0/10

At the 2026 International Symposium on Circuits and Systems in Shanghai, Huawei unveiled 'Tao's Law,' which replaces geometric scaling with time scaling to extend Moore's Law. The company claims to have designed and mass-produced 381 chips based on this principle over the past six years, and will launch a new Kirin chip using logic folding technology this fall. Tao's Law could represent a paradigm shift in semiconductor scaling, offering a path beyond the physical limits of traditional transistor miniaturization. If validated, it may reduce reliance on extreme ultraviolet lithography and reshape the global chip industry, particularly benefiting companies like Huawei that face export restrictions. The law focuses on reducing time constants through logic folding and multi-layer co-optimization across devices, circuits, chips, and systems. Huawei predicts that by 2031, chips based on Tao's Law could achieve transistor density equivalent to a 1.4nm process.

telegram · zaihuapd · Jul 4, 04:56

**Background**: Moore's Law, which predicts that transistor density doubles approximately every two years, is approaching physical limits due to atomic-scale constraints. Traditional geometric scaling shrinks transistor dimensions, but time scaling instead reduces signal propagation delays to improve performance and density. Logic folding is a design technique that reconfigures circuit layout to shorten critical paths, effectively achieving 3D-like integration without physical stacking.

<details><summary>References</summary>
<ul>
<li><a href="https://www.peopleapp.com/column/30052254360-500007517346">“ 韬 定 律 ”，做 时 间 的朋友_人民日报</a></li>
<li><a href="https://www.msn.com/zh-cn/news/other/究竟-韬定律-将如何影响半导体产业演进路径/ar-AA243zka">究竟｜“ 韬 定 律 ”将如何影响 半 导 体 产业演进路径</a></li>
<li><a href="https://news.qq.com/rain/a/20260527A0AA4G00">news.qq.com/rain/a/20260527A0AA4G00</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#Moore's Law`, `#Huawei`, `#chip design`, `#scaling`

---