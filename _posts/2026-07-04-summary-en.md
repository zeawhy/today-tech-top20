---
layout: default
title: "Horizon Summary: 2026-07-04 (EN)"
date: 2026-07-04
lang: en
---

> From 48 items, 12 important content pieces were selected

---

1. [Guide to Running SOTA LLMs Locally Sparks Cost Debate](#item-1) ⭐️ 8.0/10
2. [EU Parliament Spy Probe Member Hacked with Pegasus](#item-2) ⭐️ 8.0/10
3. [Wordgard: New Rich-Text Editor from ProseMirror Creator](#item-3) ⭐️ 8.0/10
4. [Ubicloud Advocates Strict Memory Overcommit for PostgreSQL](#item-4) ⭐️ 8.0/10
5. [Current AI Launches Open Source AI Gap Map](#item-5) ⭐️ 8.0/10
6. [Course Creator Reports 50%+ Revenue Drop Due to AI](#item-6) ⭐️ 8.0/10
7. [CDD recovers finetuning data from logits only](#item-7) ⭐️ 8.0/10
8. [Anthropic Accuses Alibaba of Massive Distillation Attack on Claude](#item-8) ⭐️ 8.0/10
9. [Huawei unveils Atlas 350 accelerator with Ascend 950PR, 2.87x H20 compute](#item-9) ⭐️ 8.0/10
10. [Huawei Mate 80 Pro Gaming Efficiency Beats Snapdragon 8 Gen3](#item-10) ⭐️ 8.0/10
11. [NASA Launches Rescue Satellite to Save Aging Space Telescope](#item-11) ⭐️ 8.0/10
12. [Tencent's Atuin AI beats Mythos in CyberGym benchmark](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Guide to Running SOTA LLMs Locally Sparks Cost Debate](https://github.com/jamesob/local-llm) ⭐️ 8.0/10

Jamesob published a comprehensive guide on GitHub detailing how to build expensive local setups for running state-of-the-art large language models, including configurations costing $40,000 or more. This guide highlights the ongoing tension between the high upfront cost of local LLM inference and the desire for privacy, control, and independence from cloud services, sparking debate about cost-effectiveness and feasibility. The guide's top-tier build includes four GPUs at $12,000 each, totaling $50,000–$55,000, and relies on quantization and pruning techniques to fit models like a modified GLM-5.2 with 594B parameters into available VRAM.

hackernews · livestyle · Jul 3, 15:03 · [Discussion](https://news.ycombinator.com/item?id=48775921)

**Background**: Running large language models locally requires significant hardware, especially VRAM, to load model weights and perform inference. Quantization reduces model precision to lower memory usage, while pruning removes less important parameters. Cloud-based LLMs like Claude Opus offer high performance at a subscription cost, but local setups provide privacy and offline capability.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/jamesob/local-llm">GitHub - jamesob/local-llm: Everything I know about running LLMs locally · GitHub</a></li>
<li><a href="https://enji.ai/tech-articles/how-to-switch-from-sota-llms-to-local-oss-llms/">Switching from SOTA to Local OSS LLMs: A Practical Guide</a></li>
<li><a href="https://medium.com/data-science-collective/what-is-the-best-hardware-for-running-local-llms-in-2026-mac-vs-5090-vs-cloud-ff023b660442">What Is The Best Hardware for Running Local LLMs in 2026... | Medium</a></li>

</ul>
</details>

**Discussion**: Commenters widely agree that local setups are still far more expensive and lower quality than cloud alternatives, with one noting that $40,000 could pay for 16.8 years of Claude Opus subscription. Others suggest intermediate options like 128GB unified memory systems for running DeepSeek V4, and warn that quantized models may behave poorly outside benchmarks.

**Tags**: `#LLM`, `#local inference`, `#hardware`, `#cost analysis`, `#open source`

---

<a id="item-2"></a>
## [EU Parliament Spy Probe Member Hacked with Pegasus](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

Citizen Lab investigation found that Stelios Kouloglou, a European Parliament member investigating spyware, had his iPhone infected with Pegasus spyware on at least three occasions in 2022 and 2023. This indicates a coordinated espionage campaign targeting EU parliament members, potentially by a state actor with authorization to spy across multiple European countries, undermining democratic institutions. The first infection in October 2022 overlaps with a Pegasus campaign targeting Russian and Belarusian exiled journalists, suggesting a single Pegasus customer operated across borders. The same phone also contained confidential medical and government documents.

hackernews · ledoge · Jul 3, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48779683)

**Background**: Pegasus is spyware developed by Israeli firm NSO Group, capable of remotely compromising mobile devices via zero-click exploits. It has been widely abused by governments to surveil journalists, activists, and politicians. Citizen Lab is a University of Toronto research group that investigates digital threats.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>
<li><a href="https://citizenlab.ca/">The Citizen Lab - The Citizen Lab</a></li>

</ul>
</details>

**Discussion**: Commenters debated whether the attack was against the EU parliament or a domestic Greek scandal, with some noting that Greece and other EU states have abused Pegasus. Others questioned the lack of device separation policies in the EU parliament.

**Tags**: `#cybersecurity`, `#spyware`, `#Pegasus`, `#EU`, `#espionage`

---

<a id="item-3"></a>
## [Wordgard: New Rich-Text Editor from ProseMirror Creator](https://wordgard.net/) ⭐️ 8.0/10

Wordgard is a new in-browser rich-text editor released by Marijn Haverbeke, the creator of ProseMirror, offering a fresh approach to document editing with shared concepts but no upgrade path from ProseMirror. This release is significant because it comes from a highly respected creator in the rich-text editor space, and the community is actively discussing the technical trade-offs and practical considerations of adopting a new editor without a migration path. Wordgard shares many concepts with ProseMirror but is not backward-compatible, meaning switching requires significant rework. The editor is designed for modern web applications and emphasizes a clean, semantic document model.

hackernews · indy · Jul 3, 08:50 · [Discussion](https://news.ycombinator.com/item?id=48772573)

**Background**: ProseMirror is a battle-tested rich-text editor framework used by many projects like Tiptap. It provides a powerful core but has a steep learning curve. In-browser rich-text editors have long been a challenge due to lack of a web standard, with many solutions like Quill and TinyMCE existing.

<details><summary>References</summary>
<ul>
<li><a href="https://prosemirror.net/">ProseMirror</a></li>
<li><a href="https://github.com/prosemirror">ProseMirror · GitHub</a></li>

</ul>
</details>

**Discussion**: The community is curious about the 'why' behind Wordgard and notes the lack of an upgrade path from ProseMirror. Some users express frustration with the complexity of existing editors and praise Wordgard's design, while others discuss technical challenges like static typing with ProseMirror.

**Tags**: `#rich-text editor`, `#ProseMirror`, `#web development`, `#open source`, `#WYSIWYG`

---

<a id="item-4"></a>
## [Ubicloud Advocates Strict Memory Overcommit for PostgreSQL](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit) ⭐️ 8.0/10

Ubicloud published a blog post explaining why they use strict memory overcommit (vm.overcommit_memory=2) for PostgreSQL to avoid OOM killer issues, based on their experience operating managed PostgreSQL at scale. This matters because OOM killer disruptions are a common pain point for PostgreSQL operators, and strict overcommit offers a way to significantly reduce those crashes, though it requires careful testing and may not suit all workloads. Strict overcommit (mode 2) enforces a CommitLimit based on swap + RAM * overcommit_ratio, refusing allocations that exceed it. Ubicloud notes that they initially ran into failures after enabling it, but eventually found it beneficial for stability.

hackernews · furkansahin · Jul 3, 13:00 · [Discussion](https://news.ycombinator.com/item?id=48774509)

**Background**: The Linux OOM killer is a mechanism that terminates processes when the system runs out of memory. PostgreSQL, which can allocate large amounts of memory for queries, is often a target. The kernel's default memory overcommit behavior (mode 0 or 1) can lead to overcommitment and subsequent OOM kills.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit">PostgreSQL and the OOM Killer: Why We Use Strict Memory ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=48774509">PostgreSQL and the OOM Killer: Why We Use Strict Memory Overcommit | Hacker News</a></li>
<li><a href="https://www.postgresql.org/docs/current/kernel-resources.html">PostgreSQL: Documentation: 18: 18.4. Managing Kernel Resources</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that Linux VM defaults are considered problematic, and caution is advised when switching to mode 2, especially if overcommit ratios have been adjusted. One commenter from Ubicloud agrees with the technical content but feels the title was too strong, noting that strict overcommit may have unanticipated side-effects in many scenarios.

**Tags**: `#PostgreSQL`, `#Linux`, `#memory management`, `#OOM killer`, `#database administration`

---

<a id="item-5"></a>
## [Current AI Launches Open Source AI Gap Map](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI, a non-profit founded at the AI Action Summit in Paris in February 2025, launched the Open Source AI Gap Map v0.1, indexing 421 products across software, models, datasets, and hardware to identify gaps in the open source AI ecosystem. This map provides a comprehensive, well-funded attempt to systematically map the open source AI landscape, helping developers, researchers, and funders understand where resources are lacking and where to invest next. The map details 266 software tools, 85 models, 50 datasets, and 20 hardware projects from 228 organizations, organized into 14 categories across three stack layers; the underlying data is released under an MIT license on GitHub.

rss · Simon Willison · Jul 3, 22:04

**Background**: Current AI is a global non-profit partnership backed by $400 million in committed capital, aiming to build a public option for AI. The Gap Map builds on work from the Columbia Convening, MOF, Hugging Face, and others to map the open source AI stack and identify missing components.

<details><summary>References</summary>
<ul>
<li><a href="https://map.currentai.org/">Current AI – Open Source AI Gap Map</a></li>

</ul>
</details>

**Tags**: `#open source`, `#AI`, `#ecosystem mapping`, `#non-profit`, `#infrastructure`

---

<a id="item-6"></a>
## [Course Creator Reports 50%+ Revenue Drop Due to AI](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything) ⭐️ 8.0/10

Josh W. Comeau, a well-known course creator, reported that sales for his new course are roughly one-third of typical launches, and his existing courses have seen revenue declines of over 50%. He attributes this to AI-driven uncertainty about developer jobs and the replacement of paid courses by LLMs. This firsthand account from multiple course creators signals a structural shift in developer education, as AI tools reduce the perceived value of paid courses and create career uncertainty. It highlights a broader challenge for content creators whose work is used to train LLMs without compensation. Comeau launched his third course, Whimsical Animations, and it is on track to sell roughly one-third as many copies as a typical launch. He notes that other course creators are seeing similar trends, with revenue down 50%+ and fewer people engaging with their content.

rss · Simon Willison · Jul 3, 21:25

**Background**: Online courses for developers have been a significant revenue source for many creators, but the rise of large language models (LLMs) like GPT-4 has changed the landscape. LLMs can provide personalized tutoring and generate code explanations, reducing the need for paid courses. Additionally, AI-driven uncertainty about the future of developer jobs discourages investment in learning new skills.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mindomax.com/how-llms-generate-educational-content">How LLMs Generate Educational Content</a></li>
<li><a href="https://www.digitaltoday.co.kr/en/view/56971/ai-driven-uncertainty-spreads-expanding-developers-roles-is-key-to-change">AI - driven uncertainty spreads, expanding developers ’ roles is key to...</a></li>

</ul>
</details>

**Tags**: `#AI impact`, `#developer education`, `#online courses`, `#LLMs`, `#industry trends`

---

<a id="item-7"></a>
## [CDD recovers finetuning data from logits only](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

Researchers introduce Contrastive Decoding Diffing (CDD), a method that recovers verbatim finetuning data from LLMs using only logit access, without needing model weights or activations. CDD achieves a verbatim recovery score of 4+/5 on 19/20 model pairs across four model families, outperforming the prior whitebox method Activation Difference Lens (ADL). This work highlights a significant privacy vulnerability in LLMs, as it shows that finetuning data can be extracted with minimal access (only logits). It also demonstrates that synthetic data generated by LLMs can leave unintended fingerprints, raising concerns about data leakage and model auditing. CDD uses a single default configuration without per-model calibration or layer selection, yet outperforms ADL which requires full weight access. An unexpected finding was that the fictional name "Dr. Elena Rodriguez" appeared across multiple unrelated finetuning domains, traced back to Claude Sonnet 3.6's preference in synthetic data generation.

reddit · r/MachineLearning · /u/CebulkaZapiekana · Jul 3, 19:01

**Background**: Model diffing aims to identify differences between a base model and a finetuned version. Prior work, Activation Difference Lens (ADL), required whitebox access (weights and activations) and only recovered vague domain descriptions. Contrastive decoding is a technique that selects tokens by contrasting outputs from two models; CDD applies this idea to model diffing by contrasting logits directly.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2510.13900">Narrow Finetuning Leaves Clearly Readable Traces in Activation ...</a></li>
<li><a href="https://arxiv.org/html/2602.10371v1">Simple LLM Baselines are Competitive for Model Diffing</a></li>
<li><a href="https://learnmechinterp.com/topics/finetuning-traces/">Finetuning Traces in Activations | Learn Mechanistic Interpretability</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion includes technical questions about the method's applicability to larger models and potential defenses. Some commenters express concern about privacy implications, while others praise the cleverness of the approach and the serendipitous finding about synthetic data fingerprints.

**Tags**: `#LLM`, `#privacy`, `#model diffing`, `#finetuning`, `#machine learning`

---

<a id="item-8"></a>
## [Anthropic Accuses Alibaba of Massive Distillation Attack on Claude](https://t.me/zaihuapd/42327) ⭐️ 8.0/10

Anthropic has accused Alibaba of orchestrating a massive 'distillation attack' using approximately 25,000 fraudulent accounts to interact with its Claude AI model over 28.8 million times between April 22 and June 5, 2026, in an attempt to extract its capabilities. This incident highlights the growing threat of model distillation attacks to AI companies' business models, as they invest heavily in training frontier models and rely on API access for monetization. The involvement of a major Chinese AI lab like Qwen also raises geopolitical concerns about intellectual property theft and competitive espionage. Anthropic claims this is the largest known distillation attack against the company, involving Alibaba and its AI lab Qwen. Following the accusation, Alibaba reportedly ordered all employees to uninstall Anthropic products, including Claude Sonnet, Opus, Fable, and Claude Code, effective July 10, 2026.

telegram · zaihuapd · Jul 3, 06:21

**Background**: Model distillation is a technique where a weaker model learns from the outputs of a stronger model to replicate its capabilities. Distillation attacks involve unauthorized extraction of a model's knowledge through excessive API queries, posing an existential threat to AI companies that invest heavily in training frontier models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude ( AI ) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen_(Alibaba_Cloud)">Qwen (Alibaba Cloud)</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#model distillation`, `#Anthropic`, `#Alibaba`, `#geopolitics`

---

<a id="item-9"></a>
## [Huawei unveils Atlas 350 accelerator with Ascend 950PR, 2.87x H20 compute](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

At the 2026 Huawei China Partners Conference, Huawei announced and launched the Atlas 350 AI accelerator card powered by the new Ascend 950PR processor, claiming 2.87 times the compute of Nvidia's H20 and support for FP4 low-precision inference. This is significant because it provides a high-performance domestic alternative to Nvidia's restricted H20 chip in China, potentially reducing reliance on U.S. imports for AI infrastructure. The FP4 support and large HBM capacity (112 GB) make it competitive for large language model inference. The Atlas 350 is the first domestic accelerator card to support FP4 precision, and its 112 GB HBM allows single-card loading of 70B-parameter models. Huawei claims improvements in vector compute, interconnect bandwidth, and self-developed HBM over previous generations.

telegram · zaihuapd · Jul 3, 08:35

**Background**: The Nvidia H20 is a GPU designed for the Chinese market with reduced performance due to U.S. export restrictions, making it slower than the H100/H200. FP4 is a low-precision floating-point format that can accelerate AI inference by reducing memory bandwidth and compute requirements, though it may impact accuracy. Huawei's Ascend series is a key player in China's push for domestic AI chip independence.

<details><summary>References</summary>
<ul>
<li><a href="https://www.omniyq.com/en/sys-nd/501.html">Ascend 950 : A Milestone for Domestic AI Compute - Shenzhen Cloud...</a></li>
<li><a href="https://www.spheron.network/blog/huawei-ascend-950-vs-nvidia-b300-b200-llm-inference-2026/">Huawei Ascend 950 vs NVIDIA B300 and B200 for... | Spheron Blog</a></li>
<li><a href="https://spoonai.me/posts/2026-04-13-huawei-950pr-ai-chip-en">Huawei Ascend 950 PR — 2.8x H20 FP4, and ByteDance... | spoonai</a></li>

</ul>
</details>

**Tags**: `#hardware`, `#AI`, `#Huawei`, `#accelerator`, `#semiconductor`

---

<a id="item-10"></a>
## [Huawei Mate 80 Pro Gaming Efficiency Beats Snapdragon 8 Gen3](https://www.bilibili.com/video/BV1F7T46wEyT) ⭐️ 8.0/10

Geekerwan's review reveals that the Huawei Mate 80 Pro series, powered by the Kirin 9030 and 9030 Pro chips, achieves better gaming efficiency than the Snapdragon 8 Gen3, thanks to native HarmonyOS optimizations. In Genshin Impact at max settings 60fps, the Mate 80 Pro Max consumes only 4.9W, outperforming the Snapdragon 8 Gen3 in energy efficiency. This demonstrates that software-hardware co-optimization can overcome theoretical performance disadvantages, potentially reshaping the mobile SoC competitive landscape. It also highlights Huawei's progress in self-developed chips and HarmonyOS ecosystem, which may influence consumer choices and industry trends. The Kirin 9030 Pro features a 9-core, 14-thread CPU and a 6-core Maleoon 935 GPU with approximately 15 billion transistors. Its CPU multi-core efficiency lies between Snapdragon 8 Gen2 and 8 Gen3, but real-world gaming performance benefits from HarmonyOS native app optimizations and intelligent scheduling.

telegram · zaihuapd · Jul 3, 13:27

**Background**: Huawei's HiSilicon Kirin chips have faced US sanctions since 2020, limiting access to advanced fabrication. The Kirin 9030 is manufactured on a 5nm process, marking continued progress in domestic chip production. HarmonyOS is Huawei's proprietary operating system designed for seamless multi-device collaboration, and native apps are optimized to leverage the hardware-software integration.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Kirin_9030">Kirin 9030</a></li>
<li><a href="https://nanoreview.net/en/soc/hisilicon-kirin-9030">HiSilicon Kirin 9030 Pro: specs and benchmarks</a></li>
<li><a href="https://www.ithome.com/0/972/456.htm">华为 Mate 80 Pro 性能解禁：麒麟 9030 Pro GPU 相比 9020 提升 76...</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#Kirin 9030`, `#HarmonyOS`, `#mobile SoC`, `#gaming performance`

---

<a id="item-11"></a>
## [NASA Launches Rescue Satellite to Save Aging Space Telescope](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 8.0/10

On July 3, NASA launched the LINK spacecraft, which will attempt to capture the aging Swift space telescope and boost its orbit by about 240 kilometers to prevent it from burning up in the atmosphere. This mission marks the first time a private spacecraft will attempt to capture a U.S. government satellite, setting a precedent for future satellite servicing and space debris mitigation efforts. The LINK spacecraft will use a robotic arm to grab the telescope and then slowly raise its orbit using thrusters. If successful, Swift could resume observations as early as September.

telegram · zaihuapd · Jul 3, 15:43

**Background**: The Neil Gehrels Swift Observatory, launched in 2004, studies gamma-ray bursts and other cosmic phenomena. Its orbit has been decaying faster due to increased solar activity, and without intervention, it could re-enter Earth's atmosphere as early as October 2025.

<details><summary>References</summary>
<ul>
<li><a href="https://www.rfi.fr/cn/专栏检索/科技时空/20260630-nasa启动大胆-太空救援-机器人入轨道为20年太空望远镜-续命">NASA启 动 大胆“ 太 空 救援” 机器人入 轨 道 为20... - RFI - 法国国际广播电台</a></li>

</ul>
</details>

**Tags**: `#space`, `#NASA`, `#satellite servicing`, `#space debris`, `#astronomy`

---

<a id="item-12"></a>
## [Tencent's Atuin AI beats Mythos in CyberGym benchmark](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 8.0/10

Tencent Xuanwu Lab's Atuin AI achieved a score of 84.0% on the UC Berkeley-led CyberGym cybersecurity benchmark, surpassing Anthropic's Claude Mythos Preview. Atuin AI is built on the open-source GLM-5.1 model and consumed less than 0.1% of Mythos's Project Glasswing budget. This demonstrates that a locally deployable, open-source AI can outperform a frontier model in vulnerability detection at a fraction of the cost, potentially democratizing advanced cybersecurity capabilities. It also highlights the growing competitiveness of Chinese AI labs in specialized domains. Atuin AI discovered multiple high-severity logic vulnerabilities in projects like curl, OpenSSL, and Python cryptography that Mythos missed, with severity scores up to 9.3. On the Berkeley BVI real-world vulnerability list, Atuin AI ranked 1st in severity and 5th in total count.

telegram · zaihuapd · Jul 3, 16:12

**Background**: CyberGym is a benchmark for evaluating AI agents' ability to discover and exploit real-world software vulnerabilities. Claude Mythos Preview is Anthropic's most advanced cybersecurity model, but it remains unreleased to the public due to safety concerns. GLM-5.1 is an open-source model from Z.AI designed for long-horizon agentic tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/cybergym">CyberGym Benchmark Leaderboard | LLM Stats</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.1">GLM - 5 . 1 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos_Preview">Claude Mythos Preview</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cybersecurity`, `#vulnerability detection`, `#benchmark`, `#open-source`

---