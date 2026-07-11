---
layout: default
title: "Horizon Summary: 2026-07-11 (ZH)"
date: 2026-07-11
lang: zh
---

> 从 27 条内容中筛选出 9 条重要资讯。

---

1. [人形机器人完成全球首例活猪腹腔镜手术](#item-1) ⭐️ 9.0/10
2. [SGLang v0.5.15 将 GLM-5.2 在 Blackwell 上提升至 500+ tok/s](#item-2) ⭐️ 8.0/10
3. [相对论主宰重元素化学键](#item-3) ⭐️ 8.0/10
4. [苹果起诉 OpenAI 窃取商业机密](#item-4) ⭐️ 8.0/10
5. [VultronRetriever 模型登顶 MTEB，支持 iPhone 离线问答](#item-5) ⭐️ 8.0/10
6. [SpaceXAI 与 Cursor 联合发布 Grok 4.5，专注编码、法律和金融](#item-6) ⭐️ 8.0/10
7. [U-Boot 引导程序漏洞可在操作系统启动前执行代码](#item-7) ⭐️ 8.0/10
8. [OpenAI 发布 GPT-5.6 系列：Sol、Terra、Luna 三档模型](#item-8) ⭐️ 8.0/10
9. [上海计划 2027 年前实现高质量脑控](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [人形机器人完成全球首例活猪腹腔镜手术](https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/) ⭐️ 9.0/10

外科医生远程操控宇树 G1 人形机器人，在活猪身上完成了全球首例腹腔镜胆囊切除术，结果发表在《自然》期刊。 这一突破表明，低成本通用人形机器人有望在偏远地区、战场或太空等场景中普及微创手术，挑战达芬奇等昂贵专用系统的垄断地位。 宇树 G1 基础款售价 13500 美元，配备灵巧手后约 67000 美元，而达芬奇系统售价在 50 万到数百万美元之间。该机器人高约 1.5 米，重约 27 公斤。

telegram · zaihuapd · 7月11日 02:29

**背景**: 腹腔镜胆囊切除术是一种微创手术，用于切除胆囊，常用于治疗胆结石。达芬奇手术系统是目前机器人辅助手术的标准，但售价高达数十万到数百万美元。宇树 G1 是一款通用人形机器人，设计用于多种任务，并非专门为手术开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unitree_Robotics">Unitree Robotics - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Laparoscopic_cholecystectomy">Laparoscopic cholecystectomy</a></li>
<li><a href="https://en.wikipedia.org/wiki/Da_Vinci_Surgical_System">da Vinci Surgical System - Wikipedia</a></li>

</ul>
</details>

**标签**: `#robotics`, `#surgery`, `#humanoid robot`, `#medical technology`, `#AI`

---

<a id="item-2"></a>
## [SGLang v0.5.15 将 GLM-5.2 在 Blackwell 上提升至 500+ tok/s](https://github.com/sgl-project/sglang/releases/tag/v0.5.15) ⭐️ 8.0/10

SGLang v0.5.15 为 Blackwell GPU 上的 GLM-5.2 引入了重大性能优化，在 8 块 B300 上实现每用户每秒超过 500 个 token，在 4 块 GB300 上达到 450 tok/s。关键改进包括默认启用 Spec V2 投机解码、IndexShare MTP 将草稿步骤成本降低高达 1.9 倍，以及 TopK V2 融合。 这些优化使 SGLang 成为服务于 GLM-5.2 等生产级模型的最快开源 LLM 推理框架之一，直接惠及需要在 NVIDIA Blackwell 硬件上实现低延迟推理的用户。该版本还为投机解码和 MoE 服务设立了新的性能标杆。 Spec V2 通过可 CUDA 图的 DSA 草稿扩展和融合元数据操作实现零开销调度，端到端 TPS 提升 11%。IndexShare MTP 在草稿步骤间重用索引器 top-k，在长上下文下将草稿步骤成本降低高达 1.9 倍。该版本还增加了通过 Exa 的原生网页搜索、默认启用可中断 CUDA Graph，以及支持 Hunyuan 3 和 Qwen3.6 NVFP4 等新模型。

github · Fridge003 · 7月10日 22:58

**背景**: SGLang 是一个开源 LLM 推理框架，专为高性能推理设计。投机解码是一种使用小型草稿模型预测多个 token，再由主模型验证的技术，可降低延迟。GLM-5.2 是 ZAI 推出的 753B 参数混合专家模型，针对长周期任务优化。NVFP4 是 NVIDIA Blackwell GPU 的 4 位量化格式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.sglang.io/docs/advanced_features/speculative_decoding">Speculative Decoding - SGLang Documentation</a></li>
<li><a href="https://www.lmsys.org/blog/2026-06-15-next-generation-speculative-decoding-dflash-v2/">The next generation of speculative decoding: DFlash and Spec V2</a></li>
<li><a href="https://huggingface.co/blog/zai-org/glm-52-blog">GLM-5.2: Built for Long-Horizon Tasks</a></li>

</ul>
</details>

**标签**: `#LLM serving`, `#performance optimization`, `#GPU inference`, `#SGLang`, `#speculative decoding`

---

<a id="item-3"></a>
## [相对论主宰重元素化学键](https://www.brown.edu/news/2026-07-09/chemical-bonds-relativity) ⭐️ 8.0/10

发表在《科学》杂志上的新研究证实，爱因斯坦的相对论支配着重元素的化学键合，为自旋-轨道耦合等相对论效应提供了直接的实验证据。 这项工作加深了我们对汞等重元素为何在室温下呈液态以及黄金为何呈黄色的理解，对材料科学和量子化学具有重要意义。 该研究表明，在重元素中，电子以接近光速的速度运动，导致自旋与轨道耦合——这种相对论效应改变了化学键合。

hackernews · hhs · 7月10日 22:30 · [社区讨论](https://news.ycombinator.com/item?id=48866134)

**背景**: 相对论量子化学考虑了对重元素中接近光速的电子运动的薛定谔方程修正。这些效应解释了汞的低熔点和黄金的颜色等性质，这些无法通过非相对论理论预测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Relativistic_quantum_chemistry">Relativistic quantum chemistry - Wikipedia</a></li>
<li><a href="https://sciencenotes.org/why-is-mercury-a-liquid-at-room-temperature/">Why Is Mercury a Liquid at Room Temperature?</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，化学中的相对论效应此前已有认知（如黄金的颜色），但对新的实验确认表示赞赏。一位用户幽默地提醒不要将其解释用于航天器设计。

**标签**: `#physics`, `#chemistry`, `#relativity`, `#chemical bonding`, `#heavy elements`

---

<a id="item-4"></a>
## [苹果起诉 OpenAI 窃取商业机密](https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/) ⭐️ 8.0/10

苹果已对 OpenAI 提起诉讼，指控这家 AI 公司通过雇佣前苹果员工系统性地窃取商业机密，这些员工将机密信息通过电子邮件发送给自己，并利用这些信息接触苹果的供应商。 这起诉讼可能对 AI 行业产生重大影响，可能为商业机密保护和员工流动设立法律先例，并可能损害 OpenAI 的声誉和硬件合作伙伴关系。 苹果声称 OpenAI 指示新员工不要向苹果透露他们的新工作，并发现了一个发送机密信息的模式，包括一名叫 Tan 的关键员工。OpenAI 据称在接触苹果供应商时使用了苹果的机密硬件信息。

hackernews · stock_toaster · 7月10日 20:47 · [社区讨论](https://news.ycombinator.com/item?id=48865019)

**背景**: 商业机密诉讼在科技行业很常见，但这起案件因两家公司的高知名度和涉嫌系统性的盗窃行为而备受关注。苹果历来积极保护其知识产权，而 OpenAI 则因其数据实践和招聘策略受到批评。

**社区讨论**: 社区评论大多批评 OpenAI，许多人称其行为“确凿”，并认为这可能终结 OpenAI 的硬件野心。一些评论者警告企业不要使用 OpenAI 模型，因为存在知识产权风险，而另一些人指出苹果财力雄厚，不太可能和解，证据开示可能对 OpenAI 造成毁灭性打击。

**标签**: `#Apple`, `#OpenAI`, `#trade secrets`, `#lawsuit`, `#AI ethics`

---

<a id="item-5"></a>
## [VultronRetriever 模型登顶 MTEB，支持 iPhone 离线问答](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

Vultr 在 HuggingFace 上发布了 VultronRetriever 模型系列，在 MTEB 排行榜上每个尺寸类别均排名第一，其中 8B 模型为全球第一。与之前的 9B 类领先模型相比，这些模型的索引存储占用最多减少 16 倍，吞吐量提高 12 倍，并且可以在 iPhone 上完全离线运行问答和文档嵌入。 这一突破使得在智能手机等边缘设备上实现高质量的检索和嵌入成为可能，减少了对云基础设施的依赖。它为检索模型设定了新的效率标准，可能加速离线 AI 应用在移动和物联网环境中的普及。 该系列包括三个模型：VultronRetrieverPrime-8B（全球第一）、Core-4.5B（性能超越两倍大小的模型）和 Flash-0.8B（性能超越五倍大小的模型，离线每分钟可索引多达 60 张图像）。它们采用 Hydra 架构实现后期交互检索，内存仅为同类模型的一半，并且训练数据集具有 0% 跨数据集重复和 0% 评估污染。

reddit · r/MachineLearning · /u/madkimchi · 7月11日 15:22

**背景**: MTEB（大规模文本嵌入基准）是一个广泛使用的排行榜，用于评估文本嵌入和检索模型在各种任务上的表现。后期交互检索（如 ColBERT 模型所推广）将查询和文档编码分离，直到最终匹配步骤，从而实现高效且精确的检索。Hydra 架构是一种新颖的方法，它将后期交互与生成相结合，减少了内存占用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB Leaderboard - a Hugging Face Space by mteb</a></li>
<li><a href="https://weaviate.io/blog/late-interaction-overview">An Overview of Late Interaction Retrieval Models... | Weaviate</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区对这些模型的效率和边缘部署能力表示兴奋，许多人询问关于 Hydra 架构的技术问题以及与现有模型（如 ColBERT）的比较。一些用户对缺乏开源训练代码和可复现性表示担忧，而另一些用户则称赞在索引大小和吞吐量方面的显著改进。

**标签**: `#retrieval`, `#MTEB`, `#edge AI`, `#NLP`, `#HuggingFace`

---

<a id="item-6"></a>
## [SpaceXAI 与 Cursor 联合发布 Grok 4.5，专注编码、法律和金融](https://t.me/zaihuapd/42484) ⭐️ 8.0/10

SpaceXAI 与 Cursor 联合发布了新一代 AI 模型 Grok 4.5，该模型在 Harvey 法律代理基准测试中排名第一，并针对编码、法律和金融服务等任务进行了优化。 这是 SpaceX 以 600 亿美元收购 Cursor 后双方推出的首个联合模型，结合了 SpaceXAI 的规模与 Cursor 的编码专长，可能为专业服务领域的专用 AI 树立新标准。 Grok 4.5 以每秒 80 个 token 的速度运行，声称 token 效率是同类领先模型的两倍，定价为每百万输入 token 2 美元、每百万输出 token 6 美元，缓存输入价格为 0.50 美元。

telegram · zaihuapd · 7月11日 01:44

**背景**: Harvey 是一个开源的法律代理基准测试，包含 24 个实践领域的 1200 多项任务，根据专家编写的评分标准进行评分。Cursor 是一家成立于 2022 年的 AI 编码代理和开发环境公司，近期被 SpaceX 收购。Token 效率指的是每个 token 生成更多有用输出，从而降低每个任务的成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark">Introducing Harvey ’s Legal Agent Benchmark</a></li>
<li><a href="https://byteiota.com/grok-45-ga-token-efficiency-api-guide/">Grok 4.5 Is GA: Token Efficiency Beats the Benchmark Gap</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(company)">Cursor (company) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Grok 4.5`, `#SpaceXAI`, `#Cursor`, `#legal AI`

---

<a id="item-7"></a>
## [U-Boot 引导程序漏洞可在操作系统启动前执行代码](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

Binarly 披露了 U-Boot 的 FIT 签名验证中的六个漏洞，其中两个可导致任意代码执行，四个可造成设备崩溃，影响自 2013.07 版本以来的版本。 这些漏洞允许攻击者绕过启动时的安全检查，在操作系统加载前执行恶意代码，可能破坏固件安全功能并在大量设备上植入持久性恶意软件。 漏洞位于 FIT 镜像签名验证代码中，在验证完成前会处理不受信任的启动镜像。补丁已被 U-Boot 维护者接受，但部署取决于硬件厂商将其集成到固件更新中。

telegram · zaihuapd · 7月11日 08:32

**背景**: U-Boot 是嵌入式设备中广泛使用的开源引导程序，支持带有签名验证的 FIT（扁平镜像树）镜像以实现安全启动。已验证启动机制确保只有经过认证的固件运行，但这些漏洞允许绕过该检查。支持远程固件更新的 BMC（基板管理控制器）尤其面临风险，因为攻击者无需物理接触即可利用漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.u-boot-project.org/en/latest/usage/fit/signature.html">U-Boot FIT Signature Verification</a></li>
<li><a href="https://cybersecuritynews.com/u-boot-fit-signature-verification/">Six U-Boot FIT Signature Verification Flaws Enable Code ...</a></li>

</ul>
</details>

**标签**: `#security`, `#bootloader`, `#U-Boot`, `#firmware`, `#vulnerability`

---

<a id="item-8"></a>
## [OpenAI 发布 GPT-5.6 系列：Sol、Terra、Luna 三档模型](https://t.me/zaihuapd/42497) ⭐️ 8.0/10

OpenAI 正式发布 GPT-5.6 系列，包含三个档次：旗舰级 Sol、平衡型 Terra 和低成本 Luna，并新增 max/ultra 推理、多智能体协作和 Programmatic Tool Calling 等功能。 此次发布大幅优化了性能成本比，使高级 AI 在编程、研究和网络安全等复杂任务中更易用，同时多智能体和工具调用功能支持更自主、高效的流程。 Sol 在 Fable 5 基准测试中比前代高出 13.1 分，而 Luna 的成本仅为 Sol 的五分之一。该系列引入了 Programmatic Tool Calling，允许模型通过代码编排工具，而非逐个 API 往返调用。

telegram · zaihuapd · 7月11日 13:34

**背景**: 大型语言模型（如 GPT）通常通过 API 调用访问，每次工具调用都需要单独往返，对于多步骤任务效率低下。Programmatic Tool Calling 使模型能够编写并执行代码，在一次会话中调用多个工具，从而降低延迟和成本。多智能体协作允许多个 AI 智能体协同完成复杂任务，突破了单一模型的局限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vellum.ai/blog/gpt-5-6-benchmarks-explained">GPT-5.6 Sol vs Terra vs Luna: Which Tier Should You Actually Use?</a></li>
<li><a href="https://www.marktechpost.com/2026/07/09/openai-releases-gpt-5-6-a-three-tier-model-family-with-programmatic-tool-calling/">OpenAI Releases GPT-5.6 (Sol, Terra, Luna): A Three-Tier Model Family With Programmatic Tool Calling in the Responses API - MarkTechPost</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-gpt-5-6-soul-terra-luna-explained">What Is GPT-5.6? OpenAI's Soul, Terra, and Luna Model Tiers Explained | MindStudio</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#AI`, `#large language model`, `#machine learning`

---

<a id="item-9"></a>
## [上海计划 2027 年前实现高质量脑控](https://t.me/zaihuapd/42501) ⭐️ 8.0/10

上海市科学技术委员会印发《上海市脑机接口未来产业培育行动方案（2025-2030 年）》，目标是在 2027 年前实现高质量脑控，半侵入式脑机接口产品在国内率先实现临床应用，侵入式脑机接口研发取得突破。 该政策标志着政府对脑机接口技术的大力支持和投入，可能加速临床采用，并使上海成为神经技术领域的全球领导者。它可能为瘫痪或失语患者带来改变生活的沟通和运动功能恢复。 该计划旨在推动 5 款以上侵入式或半侵入式脑机接口产品完成医疗器械型式检验和临床试验，面向失语、瘫痪等患者实现部分语言和运动功能恢复。行动方案覆盖 2025-2030 年。

telegram · zaihuapd · 7月11日 15:49

**背景**: 脑机接口（BCI）使大脑与外部设备之间能够直接通信。它们分为非侵入式（头皮电极）、半侵入式（电极置于颅骨下但大脑外）和侵入式（电极植入脑组织）。半侵入式 BCI 在信号质量和手术风险之间取得平衡，使其有望早期进入临床应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://paper.people.com.cn/rmrb/pc/content/202607/04/content_30166549.html">无创接入，脑机接口迎来更多可能（院士讲科普·未来产业）</a></li>
<li><a href="https://www.nhsa.gov.cn/art/2025/3/13/art_52_15967.html">nhsa.gov.cn/art/2025/3/13/art_52_15967.html</a></li>
<li><a href="https://www.jfdaily.com/wx/detail.do?id=874565">三家“ 脑 机 接 口 ”头部企业为何出现在上海？｜跟着项目经理看未来产业</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#policy`, `#China`, `#clinical application`, `#neurotechnology`

---