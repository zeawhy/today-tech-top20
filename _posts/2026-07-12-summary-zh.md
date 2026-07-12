---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> 从 30 条内容中筛选出 8 条重要资讯。

---

1. [OpenAI 发布 GPT-5.6 系列，旗舰模型 Sol 登场](#item-1) ⭐️ 9.0/10
2. [GPT-5.6 一小时攻克 50 年图论猜想](#item-2) ⭐️ 9.0/10
3. [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](#item-3) ⭐️ 8.0/10
4. [VultronRetriever 模型登顶 MTEB 排行榜](#item-4) ⭐️ 8.0/10
5. [U-Boot 引导程序曝 6 个漏洞，可启动时执行代码](#item-5) ⭐️ 8.0/10
6. [上海计划 2027 年前实现高质量脑控](#item-6) ⭐️ 8.0/10
7. [苹果起诉 OpenAI 窃取商业机密以推进硬件业务](#item-7) ⭐️ 8.0/10
8. [xAI Grok CLI 默认上传整个代码库及密钥文件](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-5.6 系列，旗舰模型 Sol 登场](https://t.me/zaihuapd/42497) ⭐️ 9.0/10

OpenAI 正式发布 GPT-5.6 系列，推出三个模型：Sol（旗舰级，能力最强）、Terra（平衡性能与成本）和 Luna（面向高并发低成本场景）。该系列在代码生成、知识工作、设计、科研和网络安全方面有显著提升，并引入了 max/ultra 推理、多智能体协作和 Programmatic Tool Calling 等新功能。 此次发布标志着 AI 在成本效率和能力上的范式转变，能够以更少的 token 和更低的成本完成复杂任务。多层级模型策略让开发者可以根据需求选择智能与价格的平衡，而多智能体协作和 Programmatic Tool Calling 等高级功能为更自主、高效的 AI 工作流铺平了道路。 GPT-5.6 Sol 是 GPT-5.6 端点的默认模型，提供最高智能。Programmatic Tool Calling 允许模型编写并执行 JavaScript 来协调单个请求中的工具调用，减少往返次数和 token 消耗。多智能体协作使多个 AI 智能体能够协同处理复杂的多步骤任务。

telegram · zaihuapd · 7月11日 13:34

**背景**: OpenAI 的 GPT 系列从 GPT-3 发展到 GPT-4，再到现在的 GPT-5.6，每一代都在推理能力、上下文长度和任务完成度上有所提升。新系列引入了类似其他 AI 提供商的分层模型阵容，让用户可以根据成本或能力进行优化。Programmatic Tool Calling 是一种技术，模型通过编写代码以编程方式调用工具，相比传统的往返式工具调用，能减少延迟和 token 成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://codingfleet.com/blog/gpt-5-6-sol-vs-terra-vs-luna/">GPT‑5.6 Sol vs Terra vs Luna: Which Model Should You Use?</a></li>
<li><a href="https://www.elser.ai/blog/gpt-5-6-sol-vs-terra-vs-luna-which-model-should-you-use">GPT-5.6 Sol vs Terra vs Luna: Which Model Should You Use?</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling">Programmatic Tool Calling | OpenAI API</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#AI models`, `#machine learning`, `#cost optimization`

---

<a id="item-2"></a>
## [GPT-5.6 一小时攻克 50 年图论猜想](https://www.qbitai.com/2026/07/447873.html) ⭐️ 9.0/10

OpenAI 的 GPT-5.6 Sol Ultra 使用 64 个并行子代理，在不到一小时内自主证明了图论中存在 50 年的循环双覆盖猜想，并生成了 3 页 PDF 证明。OpenAI 同时公布了所使用的完整提示词。 这表明大语言模型现在能够自主解决长期未解的数学猜想，可能加速数学和理论计算机科学的研究。同时展示了先进的多智能体推理和验证能力。 该猜想断言每个无桥图都存在一组圈，使得每条边恰好被覆盖两次。GPT-5.6 将问题转化为有限域上的边标号和线性方程组求解，使用 64 个子代理并行工作，并设有独立验证检查。

telegram · zaihuapd · 7月12日 03:49

**背景**: 循环双覆盖猜想由 Szekeres（1973）和 Seymour（1979）独立提出，是图论中的一个重要未解问题。桥是指删除后会使图不连通的边；该猜想仅适用于无桥图。此前使用传统数学方法的尝试未能给出完整证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cycle_double_cover_conjecture">Cycle double cover conjecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bridge_(graph_theory)">Bridge (graph theory)</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#graph theory`, `#OpenAI`, `#reasoning`

---

<a id="item-3"></a>
## [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 8.0/10

vLLM v0.25.0 将 Model Runner V2 设为所有稠密模型的默认执行路径，移除了旧版 PagedAttention，并新增了 LLaVA-OneVision-2、GLM-5 等模型，以及流式解析引擎和通用推测解码。 此版本标志着 vLLM 架构的重大转变，通过移除旧组件提升了性能和模块化，同时简化了代码库。它还扩展了模型支持并引入了新功能，惠及更广泛的 LLM 服务生态系统。 Model Runner V2 现在支持 EVS、实时嵌入、Mamba 混合模型的前缀缓存，以及带完整 CUDA 图的动态推测解码。Transformers 建模后端现在与原生 vLLM 速度相当，此版本包含来自 232 位贡献者的 558 次提交。

github · khluu · 7月11日 20:06

**背景**: vLLM 是一个开源的大语言模型推理和服务引擎，使用 PagedAttention 实现高效内存管理。Model Runner V2 是重新设计的执行核心，解决了 V1 中的设计缺陷，提供了更好的模块化和性能。PagedAttention 是 vLLM 最初实现高吞吐量的注意力机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#open source`, `#release`, `#performance`

---

<a id="item-4"></a>
## [VultronRetriever 模型登顶 MTEB 排行榜](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

VultronRetriever 系列检索模型已在 HuggingFace 上发布，在 MTEB 排行榜上取得第一名，索引存储占用最多减少 16 倍，吞吐量提升 12 倍，并且可以在 iPhone 上完全离线运行。 这一突破使得在边缘设备上实现最先进的检索成为可能，显著降低了离线问答和文档嵌入等应用的基础设施成本和延迟。 该系列包括三个模型：Prime-8B（全球第一）、Core-4.5B（性能超越两倍大小的模型）和 Flash-0.8B（性能超越五倍大小的模型，离线每分钟索引 60 张图像）。它们采用 Hydra 架构实现后期交互检索和生成，内存占用仅为同类模型的一半。

reddit · r/MachineLearning · /u/madkimchi · 7月11日 15:22

**背景**: MTEB 排行榜是评估嵌入模型在检索等任务上性能的标准基准。后期交互检索（如 ColBERT）通过计算 token 级别的相似度实现更高精度。Hydra 架构将检索和生成统一到单个模型中，降低了内存和系统复杂度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB Leaderboard - a Hugging Face Space by mteb</a></li>
<li><a href="https://arxiv.org/abs/2603.28554">[2603.28554] Hydra: Unifying Document Retrieval and ...</a></li>
<li><a href="https://weaviate.io/blog/late-interaction-overview">An Overview of Late Interaction Retrieval Models: ColBERT, ColPali, and ColQwen | Weaviate</a></li>

</ul>
</details>

**标签**: `#retrieval`, `#MTEB`, `#edge AI`, `#embedding`, `#NLP`

---

<a id="item-5"></a>
## [U-Boot 引导程序曝 6 个漏洞，可启动时执行代码](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

Binarly 披露了 U-Boot 的 FIT 签名验证中的六个漏洞，包括两个严重远程代码执行漏洞（BRLY-2026-037 至 BRLY-2026-042），影响自 2013.07 版本以来的所有版本。 这些漏洞允许攻击者绕过签名检查，在操作系统启动前执行恶意代码，从而实现难以检测的固件攻击。漏洞影响从嵌入式系统到服务器的数百万台设备。 六个漏洞中，两个可实现任意代码执行，四个可导致拒绝服务崩溃。补丁已被 U-Boot 维护者接受，但设备厂商需将其集成到固件更新中；已停止支持的设备可能永远无法修复。

telegram · zaihuapd · 7月11日 08:32

**背景**: U-Boot 是广泛使用的嵌入式设备开源引导程序，负责加载操作系统。FIT（Flattened Image Tree）是一种用于打包内核、设备树等镜像并附带加密签名以确保完整性的格式。漏洞位于签名验证代码中，允许攻击者构造绕过验证的恶意 FIT 镜像。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/">New U-Boot flaws could enable stealthy firmware attacks</a></li>
<li><a href="https://cybersecuritynews.com/u-boot-fit-signature-verification/">Six U - Boot FIT Signature Verification Flaws Enable Code Execution...</a></li>
<li><a href="https://thehackernews.com/2026/07/six-new-u-boot-flaws-could-let.html">Six New U-Boot Flaws Could Let Malicious Images Crash Devices ...</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#bootloader`, `#firmware`, `#U-Boot`

---

<a id="item-6"></a>
## [上海计划 2027 年前实现高质量脑控](https://t.me/zaihuapd/42501) ⭐️ 8.0/10

上海市科学技术委员会印发了《上海市脑机接口未来产业培育行动方案（2025-2030 年）》，目标是到 2027 年实现高质量脑控，半侵入式脑机接口产品在国内率先实现临床应用，侵入式脑机接口研发取得突破。 该政策表明中国政府对脑机接口技术的大力支持，可能加速脑机接口设备在医疗康复领域的开发和临床应用，例如帮助瘫痪或失语患者恢复部分语言和运动功能。 该计划目标是到 2027 年推动 5 款以上侵入式和半侵入式脑机接口产品完成医疗器械型式检验和临床试验，面向失语、瘫痪等患者实现部分语言和运动功能恢复。半侵入式脑机接口植入头骨下但不进入脑组织，在信号质量和安全性之间取得平衡。

telegram · zaihuapd · 7月11日 15:49

**背景**: 脑机接口（BCI）实现大脑与外部设备之间的直接通信。它们分为侵入式（电极植入脑组织）、半侵入式（电极置于头骨下但不在脑内）和非侵入式（头皮电极）。侵入式 BCI 信号质量最高但存在手术风险，非侵入式更安全但信号分辨率较低。中国近期开展了首例侵入式脑机接口临床试验，成为第二个进入该阶段的国家。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/脑机接口">脑机接口 - 维基百科，自由的百科全书</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/699343201">侵入式、半侵入式、非侵入式脑机接口，具体应该怎么选 - 知乎</a></li>
<li><a href="https://www.cas.cn/syky/202506/t20250614_5073157.shtml">我国侵入式脑机接口进入临床试验阶段----中国科学院</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#neurotechnology`, `#policy`, `#China`, `#medical AI`

---

<a id="item-7"></a>
## [苹果起诉 OpenAI 窃取商业机密以推进硬件业务](https://t.me/zaihuapd/42502) ⭐️ 8.0/10

2026 年 7 月 10 日，苹果在美国加州北区联邦法院起诉 OpenAI、两名前员工及 io Products，指控其系统性窃取与产品设计、制造工艺及供应链相关的商业机密，以加速 OpenAI 的消费级硬件研发。 这起诉讼加剧了全球两家最具价值科技公司之间的紧张关系，可能影响 OpenAI 的硬件雄心，并为 AI 公司如何从苹果等成熟硬件领导者处招募人才树立先例。 苹果指控前员工 Chang Liu 在离职后仍访问内部网络并下载数十份硬件文件；OpenAI 硬件负责人 Tang Yew Tan 在离职前将供应商信息发送至个人邮箱，并要求求职者携带苹果零部件参加面试。诉讼还称，超过 40 名前苹果员工现任职于 OpenAI 的硬件部门。

telegram · zaihuapd · 7月11日 16:29

**背景**: OpenAI 以 ChatGPT 闻名，近年来正扩展至硬件领域，于 2025 年 5 月收购了由前苹果设计总监 Jony Ive 联合创立的 io Products。诉讼称，OpenAI 的硬件业务建立在窃取的苹果机密之上，包括未发布产品的细节和制造工艺。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.macrumors.com/2026/07/10/apple-sues-openai/">Apple Sues OpenAI for Stealing Trade Secrets to Build AI Hardware</a></li>
<li><a href="https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/">Apple sues OpenAI, accuses ex-employees of stealing trade secrets</a></li>
<li><a href="https://www.nytimes.com/2026/07/10/technology/apple-openai-lawsuit.html">Apple Sues OpenAI, Accusing It of Stealing Company Secrets</a></li>

</ul>
</details>

**标签**: `#Apple`, `#OpenAI`, `#trade secrets`, `#lawsuit`, `#hardware`

---

<a id="item-8"></a>
## [xAI Grok CLI 默认上传整个代码库及密钥文件](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) ⭐️ 8.0/10

安全研究人员发现，xAI 的 Grok Build CLI 工具（版本 0.2.93）默认将整个代码仓库和 .env 等敏感文件上传至 xAI 服务器，且无法有效关闭。 这对开发者构成严重的隐私和安全风险，专有代码和凭据可能在未经同意的情况下泄露，削弱对 AI 辅助开发工具的信任。 该工具通过两个渠道上传代码：文件内容嵌入模型请求，同时以 git bundle 形式打包上传至 Google Cloud Storage；关闭“改进模型”开关无法阻止上传。

telegram · zaihuapd · 7月12日 04:19

**背景**: Grok CLI 是一个命令行界面工具，用于访问 xAI 的 Grok AI 模型。Git bundle 是一种将整个 Git 仓库打包成单个文件以便传输的格式。Google Cloud Storage 是一种云端对象存储服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Grok_CLI">Grok CLI</a></li>
<li><a href="https://git-scm.com/docs/git-bundle">Git - git-bundle Documentation</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论可能对默认上传数据的行为表示强烈担忧，许多用户质疑 xAI 的透明度，并呼吁立即修复或提供退出选项。

**标签**: `#security`, `#privacy`, `#xAI`, `#CLI`, `#data leakage`

---