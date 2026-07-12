---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> 从 31 条内容中筛选出 11 条重要资讯。

---

1. [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](#item-1) ⭐️ 9.0/10
2. [OpenAI 发布 GPT-5.6 系列：Sol、Terra、Luna 三层模型](#item-2) ⭐️ 9.0/10
3. [GPT-5.6 一小时攻克 50 年图论猜想](#item-3) ⭐️ 9.0/10
4. [xAI Grok CLI 默认上传整个代码库及密钥文件](#item-4) ⭐️ 9.0/10
5. [Mesh LLM：通过 iroh P2P 实现分布式 AI 推理](#item-5) ⭐️ 8.0/10
6. [RISCBoy：开源 RISC-V 便携游戏机](#item-6) ⭐️ 8.0/10
7. [UPI 架构与交易流程详解](#item-7) ⭐️ 8.0/10
8. [Zer0Fit MCP 服务器封装 Google TabFM 和 TimesFM 实现零样本机器学习](#item-8) ⭐️ 8.0/10
9. [VultronRetriever 模型登顶 MTEB 排行榜](#item-9) ⭐️ 8.0/10
10. [上海计划 2027 年前实现高质量脑控](#item-10) ⭐️ 8.0/10
11. [苹果起诉 OpenAI 窃取商业机密](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 9.0/10

vLLM v0.25.0 将 Model Runner V2 设为所有稠密模型的默认执行路径，并移除了旧的 PagedAttention 实现。该版本包含来自 232 位贡献者的 558 次提交，新增了对 LLaVA-OneVision-2、GLM-5 等模型的支持，并引入了新的 Streaming Parser Engine。 此版本标志着 vLLM 的重大架构转变，通过标准化 Model Runner V2 提高了性能和模块化。移除 PagedAttention 简化了代码库，而新模型和功能扩展了 vLLM 在生产级 LLM 服务中的适用性。 Model Runner V2 现在支持 EVS、实时嵌入、Mamba 混合模型的前缀缓存，以及带完整 CUDA 图的动态推测解码。Transformers 建模后端现在与原生 vLLM 速度相当，新增模型包括 Unlimited OCR、MOSS-Transcribe-Diarize 和 Hy3。

github · khluu · 7月11日 20:06

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理引擎。Model Runner V2 是重新设计的执行核心，相比原始的 V1 提高了模块化和性能。PagedAttention 是 vLLM 最初的注意力机制，通过分页高效管理 KV 缓存，但已被更新的后端取代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#open source`, `#release`, `#AI/ML`

---

<a id="item-2"></a>
## [OpenAI 发布 GPT-5.6 系列：Sol、Terra、Luna 三层模型](https://t.me/zaihuapd/42497) ⭐️ 9.0/10

OpenAI 正式发布了 GPT-5.6 系列，包含三个层级：Sol（旗舰）、Terra（平衡）和 Luna（高性价比）。该系列引入了 max/ultra 推理、多智能体协作和 Programmatic Tool Calling，在代码、知识工作、设计、科研和网络安全方面有显著提升。 此次发布标志着 OpenAI 模型产品线的重大演进，通过分层定价和能力，用户可以根据任务复杂度选择合适的模型。新的推理和多智能体功能能够更高效地处理复杂多步骤任务，有望降低 token 使用量和成本。 GPT-5.6 Sol 是最强大但最昂贵的层级，Terra 平衡了性能与成本，Luna 针对高并发、低成本场景优化。max 推理模式为单次模型调用分配更多推理工作，而 ultra 模式则使用子智能体并行处理任务。Programmatic Tool Calling 允许模型通过代码编排工具，而非逐个 API 往返调用。

telegram · zaihuapd · 7月11日 13:34

**背景**: OpenAI 的 GPT 系列经历了多个版本的演进，GPT-5.4 将于 7 月 23 日退役，GPT-5.5 仍可使用。新的 GPT-5.6 系列引入了分层命名系统，数字表示代际，而 Sol、Terra 和 Luna 是独立演进的持久层级。这种结构允许用户根据具体用例选择合适的能力和成本水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vellum.ai/blog/gpt-5-6-benchmarks-explained">GPT - 5 . 6 Sol vs Terra vs Luna : Which Tier Should You Actually Use?</a></li>
<li><a href="https://felloai.com/gpt-5-6/">GPT - 5 . 6 Sol , Terra , Luna : What OpenAI Just Shipped</a></li>
<li><a href="https://apidog.com/blog/gpt-5-6-sol-vs-terra-vs-luna/">GPT - 5 . 6 Sol vs Terra vs Luna : which model should you use?</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的早期社区反应强调，GPT-5.6 Sol 结合 Codex 和 Ultra 模式在处理复杂任务时表现“惊人”，用户指出 Max Reasoning 配合聚焦的上下文能获得最佳结果。一些讨论提醒，Ultra 模式将 Sol 从单一模型转变为协调者，可能需要仔细的任务分解。

**标签**: `#OpenAI`, `#GPT-5.6`, `#AI`, `#LLM`, `#announcement`

---

<a id="item-3"></a>
## [GPT-5.6 一小时攻克 50 年图论猜想](https://www.qbitai.com/2026/07/447873.html) ⭐️ 9.0/10

OpenAI 的 GPT-5.6 Sol Ultra 模型在不到一小时内自主证明了循环双覆盖猜想，这是一个存在约 50 年的图论未解问题。该模型通过 64 个并行子代理和一个精心设计的提示词，生成了一份 3 页的 PDF 证明。 这一成就表明，大型语言模型现在能够自主处理长期存在的数学猜想，可能加速数学和理论计算机科学的研究。它也展示了多智能体协作和严谨提示工程在复杂推理任务中的强大能力。 该证明将猜想转化为有限域上的边标号和线性方程组问题，为每条边分配两个标签，使得相同标签的边组成圈。提示词明确了验收标准、定义、边界条件和失败情形，但没有规定固定的解题步骤。

telegram · zaihuapd · 7月12日 03:49

**背景**: 循环双覆盖猜想由 Szekeres（1973 年）和 Seymour（1979 年）独立提出，询问是否每个无桥图都存在一组圈，使得每条边恰好被覆盖两次。这是图论中的一个基本未解问题，与图嵌入和圆形嵌入猜想相关。多智能体 LLM 系统使用多个并行工作的专门智能体，通常带有一个协调器，来处理复杂任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cycle_double_cover_conjecture">Cycle double cover conjecture</a></li>
<li><a href="https://mathworld.wolfram.com/CycleDoubleCoverConjecture.html">Cycle Double Cover Conjecture -- from Wolfram MathWorld</a></li>
<li><a href="https://www.superannotate.com/blog/multi-agent-llms">Multi - agent LLMs in 2026 [+frameworks] | SuperAnnotate</a></li>

</ul>
</details>

**标签**: `#AI`, `#graph theory`, `#LLM`, `#mathematical proof`, `#multi-agent`

---

<a id="item-4"></a>
## [xAI Grok CLI 默认上传整个代码库及密钥文件](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) ⭐️ 9.0/10

安全研究人员发现，xAI 的 Grok Build CLI 工具（版本 0.2.93）会自动将整个代码仓库和 .env 等敏感文件上传到 xAI 服务器，即使明确指示不要读取，隐私开关也无效。 这对使用 xAI 工具的开发者及组织构成严重的安全与隐私风险，可能导致专有代码和凭据被无意泄露。该发现削弱了用户对 xAI 隐私控制的信任，并凸显了 AI 辅助开发工具中更严格数据处理需求的必要性。 该工具通过两个渠道上传代码：文件内容嵌入模型请求并打包上传至 Google Cloud Storage，同时整个仓库以 git bundle 形式上传。测试中，一个被明确指令“不要打开”的文件仍可从上传的 bundle 中恢复，且关闭“改进模型”开关无法阻止上传。

telegram · zaihuapd · 7月12日 04:19

**背景**: Grok Build 是 xAI 推出的命令行工具，允许开发者直接在终端中与 Grok AI 模型交互。Git bundle 是一种将整个 Git 仓库打包成单个文件以便离线传输的格式。该工具的隐私设置包含一个用于选择退出模型改进的开关，但研究人员发现该开关无效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>
<li><a href="https://git-scm.com/docs/git-bundle">Git - git - bundle Documentation</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论可能包含对该问题严重性的技术分析和辩论，一些用户对数据泄露表示担忧，另一些用户则质疑该工具的设计。输入中未提供具体评论。

**标签**: `#security`, `#privacy`, `#AI tools`, `#data exfiltration`, `#xAI`

---

<a id="item-5"></a>
## [Mesh LLM：通过 iroh P2P 实现分布式 AI 推理](https://www.iroh.computer/blog/mesh-llm) ⭐️ 8.0/10

Mesh LLM 是一个新的开源项目，利用 iroh 的点对点网络，在异构设备上实现分布式 LLM 推理，自动将模型拆分到多个节点。 这种方法通过聚合消费级硬件，使大型语言模型的访问更加民主化，可能减少对昂贵云 GPU 的依赖，并实现保护隐私的去中心化 AI 推理。 Mesh LLM 支持三种服务模式：本地执行、路由到已加载模型的对等节点，或通过流水线并行将模型拆分到多个节点。性能数据显示，Qwen 235B MoE 在 2 个节点上达到 16 tok/s。

hackernews · tionis · 7月11日 22:38 · [社区讨论](https://news.ycombinator.com/item?id=48876505)

**背景**: 大型语言模型（LLM）通常需要具有大显存的高端 GPU，这些 GPU 价格昂贵且不普及。分布式推理将模型拆分到多个设备上，但传统方法依赖集中式编排或高速互连。iroh 是一个开源的 Rust 库，用于建立点对点连接，使用基于密钥的寻址而非 IP 地址，从而更容易构建去中心化应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.iroh.computer/blog/mesh-llm">Mesh LLM: distributed AI computing on iroh - Iroh</a></li>
<li><a href="https://github.com/Mesh-LLM/mesh-llm">GitHub - Mesh-LLM/mesh-llm: Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat. · GitHub</a></li>
<li><a href="https://docs.iroh.computer/what-is-iroh">What is iroh? - iroh</a></li>

</ul>
</details>

**社区讨论**: 社区成员表示对将 Mesh LLM 用于小型专用模型而非大型编码 LLM 感兴趣。一位贡献者提到 skippy 引擎负责模型拆分，一些用户对网络延迟表示担忧，但也认可了分享的性能数据。

**标签**: `#distributed computing`, `#LLM inference`, `#peer-to-peer`, `#AI infrastructure`

---

<a id="item-6"></a>
## [RISCBoy：开源 RISC-V 便携游戏机](https://github.com/Wren6991/RISCBoy) ⭐️ 8.0/10

RISCBoy 是一款完全围绕 RISC-V 处理器从头设计的开源便携游戏机，具有可编程扫描线缓冲渲染管线。 该项目展示了使用开源硬件和 RISC-V 构建定制游戏机的可行性，可能激发更多嵌入式游戏领域的爱好者和教育项目。 该游戏机采用扫描线缓冲渲染方式，逐行而非逐像素处理图形，并已在首次 wafer.space 流片中完成设计。

hackernews · mariuz · 7月11日 21:58 · [社区讨论](https://news.ycombinator.com/item?id=48876245)

**背景**: 扫描线渲染是一种每次处理一行像素的技术，与传统帧缓冲方法相比可减少内存带宽。RISC-V 是一种开放指令集架构，允许自定义处理器设计。该项目由 Raspberry Pi 的 ASIC 设计工程师 Luke Wren 创建。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Scanline_rendering">Scanline rendering - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该项目的技术深度，并注意到设计师在 Raspberry Pi 的背景及其之前 PicoDVI 的工作。有人想知道流片后的设计是否实际工作，但总体情绪非常积极。

**标签**: `#RISC-V`, `#open-source hardware`, `#game console`, `#embedded systems`, `#rendering`

---

<a id="item-7"></a>
## [UPI 架构与交易流程详解](https://timeseriesofindia.com/economy/reads/upi-architecture/) ⭐️ 8.0/10

一篇深度文章详细介绍了印度 UPI 支付系统的架构和交易流程，涵盖其规模和技术设计。 这篇文章为处理数十亿笔交易的 UPI 系统提供了宝贵的技术见解，帮助工程师和金融科技专业人士理解其设计和可扩展性。 文章解释了 NPCI 交换机、PSP 和银行的作用，并描述了包括基于意图和二维码支付在内的交易流程。

hackernews · prtk25 · 7月11日 16:33 · [社区讨论](https://news.ycombinator.com/item?id=48873457)

**背景**: UPI（统一支付接口）是由印度国家支付公司（NPCI）开发的实时支付系统。它允许用户将多个银行账户关联到单个移动应用，并进行即时个人对个人和商户支付。UPI 已成为印度主要的数字支付方式，每年处理超过 220 亿笔交易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unified_Payments_Interface">Unified Payments Interface - Wikipedia</a></li>
<li><a href="https://medium.com/@avinashkariya05910/deep-dive-system-design-of-upi-unified-payments-interface-eff3b0334b0d">Deep Dive: System Design of UPI (Unified Payments Interface) | by Avinash Kariya | Medium</a></li>
<li><a href="https://razorpay.com/blog/what-is-upi-and-how-it-works/">What is UPI ?: Unified Payments Interface Features and How UPI Works?</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 UPI 的广泛采用和易用性，有人指出它甚至让老年人也能实现数字化支付。但也有人对系统依赖手机号码和政府控制提出隐私担忧，并与 Visa/Mastercard 进行对比。另一位评论者将 UPI 的平均每秒查询数（约 700）与纳斯达克的 10 万以上进行比较，认为其规模可控。

**标签**: `#UPI`, `#payment systems`, `#architecture`, `#India`, `#fintech`

---

<a id="item-8"></a>
## [Zer0Fit MCP 服务器封装 Google TabFM 和 TimesFM 实现零样本机器学习](https://www.reddit.com/r/MachineLearning/comments/1uue8cc/zer0fit_i_took_googles_new_tabfm_timesfm_ml/) ⭐️ 8.0/10

一名研究生发布了 Zer0Fit，这是一个 MCP 服务器，封装了 Google 的 TabFM 和 TimesFM 基础模型，可通过 Open WebUI 等聊天界面实现零样本分类、回归和时间序列预测。该服务器使用 Docker 本地运行，需要 16GB 以上显存。 该项目通过简单的聊天界面让非专家也能使用 Google 强大的零样本表格和时间序列模型，降低了以往需要大量训练和调优的机器学习任务的门槛。它弥合了大语言模型与传统机器学习模型之间的差距。 Zer0Fit 使用 5 分钟 TTL 动态加载/卸载模型以释放显存，支持 CSV 输入（即将支持 XLS/XLSX/JSON/JSONL），基于 PyTorch（仅 CUDA）。在零样本模式下，Iris 分类准确率达 94.7%，加州房价回归 R² 为 0.91。

reddit · r/MachineLearning · /u/Porespellar · 7月12日 12:32

**背景**: TabFM 是 Google Research 发布的用于表格数据分类和回归的零样本基础模型，TimesFM 是用于时间序列预测的仅解码器基础模型。MCP（模型上下文协议）是一种允许 AI 模型与外部工具和数据源交互的标准。Zer0Fit 实现了一个 MCP 服务器，将这些模型作为工具暴露给大语言模型调用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/">Introducing TabFM: A zero-shot foundation model for tabular data</a></li>
<li><a href="https://github.com/google-research/tabfm">google-research/tabfm - Tabular Foundation Models</a></li>
<li><a href="https://github.com/google-research/timesfm">google -research/ timesfm : TimesFM ( Time Series Foundation Model )...</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区称赞该项目实用且易于使用，许多人表示有兴趣尝试。一些用户讨论了显存需求以及扩展模型支持的潜力。作者积极参与，表示根据兴趣计划增加更多文件格式并进行维护。

**标签**: `#machine learning`, `#MCP server`, `#zero-shot learning`, `#time series`, `#tabular data`

---

<a id="item-9"></a>
## [VultronRetriever 模型登顶 MTEB 排行榜](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

VultronRetriever 模型家族（包括 Prime-8B、Core-4.5B 和 Flash-0.8B）已在 HuggingFace 上发布，在 MTEB 排行榜上各自类别中排名第一，其中 Prime-8B 为全球第一。与之前的 9B 类领先模型相比，这些模型的索引存储占用最多减少 16 倍，吞吐量最高提升 12 倍，并已在 iPhone 上离线运行问答和嵌入演示。 此次发布显著推动了高效检索技术的发展，使得在智能手机等边缘设备上实现高性能嵌入和搜索成为可能。顶尖的 MTEB 分数与大幅降低的资源需求相结合，有望使最先进的检索技术普及到移动和嵌入式应用中。 这些模型采用 Hydra 架构实现后期交互检索，在提供高精度的同时将内存使用量降低多达一半。所有模型均在零跨数据集重复和零评估污染的数据集上训练，并且在私有 MTEB 评估中未显示过拟合。

reddit · r/MachineLearning · /u/madkimchi · 7月11日 15:22

**背景**: 大规模文本嵌入基准（MTEB）是一个标准的公共排行榜，用于评估嵌入模型在检索、分类和聚类等任务上的表现。后期交互检索（由 ColBERT 等模型推广）将查询和文档分别处理，直到最终匹配阶段，从而实现高效且精确的搜索。Hydra 架构是一种结合了检索和生成能力的新方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB Leaderboard - a Hugging Face Space by mteb</a></li>
<li><a href="https://weaviate.io/blog/late-interaction-overview">An Overview of Late Interaction Retrieval Models... | Weaviate</a></li>
<li><a href="https://www.emergentmind.com/topics/hydra-model">Hydra Model: Unified Architectures</a></li>

</ul>
</details>

**标签**: `#retrieval`, `#MTEB`, `#embedding`, `#efficiency`, `#HuggingFace`

---

<a id="item-10"></a>
## [上海计划 2027 年前实现高质量脑控](https://t.me/zaihuapd/42501) ⭐️ 8.0/10

上海市科学技术委员会印发《上海市脑机接口未来产业培育行动方案（2025-2030 年）》，目标是在 2027 年前实现高质量脑控，半侵入式脑机接口产品率先实现临床应用，侵入式脑机接口研发取得突破。 这一政府支持的计划标志着中国对脑机接口技术的强力政策支持，可能加速临床采用，并使上海成为神经技术的全球中心。它可能通过恢复部分运动和语言功能，惠及瘫痪或失语患者。 该计划旨在推动 5 款以上侵入式、半侵入式脑机接口产品完成医疗器械型式检验和临床试验，面向失语、瘫痪等患者实现部分语言和运动功能恢复。

telegram · zaihuapd · 7月11日 15:49

**背景**: 脑机接口（BCI）实现大脑与外部设备之间的直接通信。它们分为非侵入式（如 EEG 帽）、半侵入式（电极置于颅骨下但大脑外）和侵入式（电极直接植入脑组织）。半侵入式 BCI 在信号质量和安全性之间取得平衡，使其在临床应用中具有前景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jjckb.cn/20251207/2391e2555b2d4825bfc88ca71deebceb/c.html">jjckb.cn/20251207/2391e2555b2d4825bfc88ca71deebceb/c.html</a></li>
<li><a href="https://www.dzwww.com/xinwen/guoneixinwen/202603/t20260313_17538328.htm">dzwww.com/xinwen/guoneixinwen/202603/t20260313_17538328.htm</a></li>
<li><a href="https://www.jfdaily.com/wx/detail.do?id=874565">三家“ 脑 机 接 口 ”头部企业为何出现在上海？｜跟着项目经理看未来产业</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#neural technology`, `#medical devices`, `#policy`, `#China`

---

<a id="item-11"></a>
## [苹果起诉 OpenAI 窃取商业机密](https://t.me/zaihuapd/42502) ⭐️ 8.0/10

2026 年 7 月 10 日，苹果在美国加州北区联邦法院起诉 OpenAI、两名前员工（Chang Liu 和 Tang Yew Tan）以及 io Products，指控其系统性窃取与产品设计、制造工艺和供应链信息相关的商业机密，以加速 OpenAI 的硬件业务。 这两大科技巨头之间的高调法律战凸显了 AI 硬件领域日益激烈的竞争，以及企业为获得优势可能采取的手段，可能重塑公司保护知识产权和管理员工流动的方式。 苹果指控 Chang Liu 在离职后保留工作笔记本电脑，并利用漏洞访问苹果的云文件存储；而 Tang Yew Tan 在离职前将供应商信息发送到个人邮箱，并要求求职者携带苹果零部件参加面试。

telegram · zaihuapd · 7月11日 16:29

**背景**: OpenAI 以 GPT-4 等 AI 模型闻名，近年来正扩展至硬件领域，并于 2025 年 5 月收购了由前苹果设计师 Jony Ive 联合创立的 io Products。OpenAI 硬件负责人 Tang Yew Tan 曾在苹果担任副总裁。商业机密诉讼在硅谷并不罕见，但本案因涉及领先 AI 公司而备受关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.yahoo.com/technology/ai/articles/apple-sues-openai-two-former-202836629.html">Apple sues OpenAI , two former employees for trade secrets theft</a></li>
<li><a href="https://www.macrumors.com/2026/07/10/apple-sues-openai/">Apple Sues OpenAI for Stealing Trade Secrets to Build... - MacRumors</a></li>
<li><a href="https://www.theguardian.com/technology/2026/jul/10/apple-sues-openai-trade-secrets">Apple sues OpenAI, alleging artificial intelligence company stole trade ...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#OpenAI`, `#trade secrets`, `#legal`, `#hardware`

---