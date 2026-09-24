---
layout: default
title: "Horizon Summary: 2026-09-24 (ZH)"
date: 2026-09-24
lang: zh
---

> 从 84 条内容中筛选出 9 条重要资讯。

---

1. [Anthropic 发布 Claude Opus 5.5，OpenAI 推出 GPT-6 Sol 与 Luna，引发新一轮价格战](#item-1) ⭐️ 9.0/10
2. [OpenAI 为 ChatGPT 语音接入插件并启用 GPT-6 模型](#item-2) ⭐️ 9.0/10
3. [vLLM v0.30.0 发布：Fast Start GPU 权重缓存与大量新模型支持](#item-3) ⭐️ 8.0/10
4. [高通为骁龙 X2 笔记本带来上游 Linux 支持](#item-4) ⭐️ 8.0/10
5. [Anthropic 称 Claude 发现具有 CRISPR 样重复序列的新型酶系统](#item-5) ⭐️ 8.0/10
6. [谷歌发布 Gemini 3.8 语音合成，支持 30 秒声音克隆](#item-6) ⭐️ 8.0/10
7. [ClusterMAX 3.0：SemiAnalysis 更新 GPU 云评级系统](#item-7) ⭐️ 8.0/10
8. [Complex KDA 扩展 Kimi Delta Attention 的表达能力](#item-8) ⭐️ 8.0/10
9. [黑客组织 ShinyHunters 声称入侵 FBI，窃取员工及申请者数据](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Opus 5.5，OpenAI 推出 GPT-6 Sol 与 Luna，引发新一轮价格战](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 9.0/10

Anthropic 发布了 Claude Opus 5.5，大约一小时后 OpenAI 发布了 GPT-6 Sol 和 GPT-6 Luna，其中 GPT-6 Luna 的价格仅为 GPT-5.6 对应型号的一半。Claude Opus 5.5 也获得了降价，在典型工作负载下的运行成本比 Opus 5 低 40%。 此次同步发布和大幅降价标志着 AI 模型格局的重大转变，使前沿能力变得更加便宜，并加剧了 Anthropic、OpenAI 和 xAI 之间的竞争。构建应用的开发者将从更低的成本和更强的性能中受益，可能加速整个行业的采用。 GPT-6 Luna 的定价为输入 $0.10/百万 token、输出 $0.50/百万 token，是 OpenAI 有史以来最便宜的模型之一，仅弱于性能较差的 GPT-4.1 Nano 和 GPT-5 Nano。GPT-5.6 计划在 11 月涨价 25%，因此 GPT-6 的价格是这些模型促销价格的一半。

rss · Simon Willison · 9月22日 23:46

**背景**: Claude Opus 5.5 是 Anthropic 自呼吁放缓前沿发展以来的首个发布版本，发布前由 Frontier Design 和 METR 等外部评估机构进行了测试。它在智能体编程和知识工作方面处于领先地位，并由 OpenRouter 上的多个提供商提供服务，包括 Amazon Bedrock、Azure、Google Vertex 和 Anthropic。GPT-6 Sol 和 Luna 是 OpenAI 继 GPT-5.6 系列之后的最新模型，定价表显示了与 xAI（Grok 4.7）等模型的激烈竞争格局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-opus-5.5">Claude Opus 5 . 5 - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://x.ai/news/grok-4-7">Introducing Grok 4.7 - SpaceXAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#OpenAI`, `#Anthropic`, `#pricing`

---

<a id="item-2"></a>
## [OpenAI 为 ChatGPT 语音接入插件并启用 GPT-6 模型](https://x.com/OpenAI/status/2102808325742322002) ⭐️ 9.0/10

OpenAI 宣布 ChatGPT 语音现在可以调用邮箱、日历和 Slack 等插件，并改由名为 Astra、Sol 和 Luna 的新 GPT-6 模型驱动，新版本于今天在全球推出。用户还可以在网页端和移动端的 ChatGPT Work 中通过语音创建文档、演示、网站和表格，或在浏览器中处理复杂任务。 这让 ChatGPT 语音从单纯的对话界面升级为能够实际操作已连接办公工具的智能代理，可能改变知识工作者免提处理邮件、日程和团队沟通的方式。同时将其与 GPT-6 系列和 ChatGPT Work 捆绑，也表明 OpenAI 正把语音打造为其生产力生态的主要入口，而非一个噱头功能。 语音插件覆盖 Gmail、Google Calendar 和 Slack，GPT-6 系列包括 Astra、Sol 和 Luna，据称在早期模型的对齐进展基础上进一步提升。此次更新在全球范围内面向网页端、移动端和桌面端推出，而语音驱动的文件创建功能仅限 ChatGPT Work 用户使用。

telegram · zaihuapd · 9月24日 00:02

**背景**: ChatGPT 语音此前主要充当语音聊天界面，能回答问题、进行对话，但无法直接在第三方应用中执行操作。插件（也称连接器）让助手可以读写邮件、日历等外部服务中的数据，而 ChatGPT Work 是 OpenAI 面向工作场景的产品，用于生成文档、表格和演示文稿。GPT-6 是 GPT-5.x 模型系列的继任者，Astra、Sol 和 Luna 是其命名变体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.androidheadlines.com/2026/09/chatgpt-voice-email-calendar-slack-integration.html">ChatGPT Voice Now Runs Email & Slack Tasks</a></li>
<li><a href="https://blog.laozhang.ai/en/posts/gpt-6-sol-vs-terra-vs-luna-vs-astra">GPT - 6 Sol vs Terra vs Luna vs Astra : Which Model Should You Use?</a></li>
<li><a href="https://help.openai.com/en/articles/20001278-creating-and-editing-documents-spreadsheets-and-presentations-with-chatgpt-work">Creating and editing documents, spreadsheets, and presentations with ChatGPT Work | OpenAI Help Center</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#GPT-6`, `#voice-assistant`, `#plugins`

---

<a id="item-3"></a>
## [vLLM v0.30.0 发布：Fast Start GPU 权重缓存与大量新模型支持](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM 发布了 v0.30.0，这是一个包含 315 位贡献者（其中 104 位是新贡献者）提交的 762 个 commit 的大型版本，新增了对 DeepSeek-V4.1-Flash、DeepSeek-V4-Flash-Vision-Exp、GLM-5.3-Flash、K2-Horizon、Cohere Compass 和 Bailing V3 VL 等模型的支持。该版本最引人注目的特性是 Fast Start：一个常驻的每 GPU 权重缓存守护进程，将量化后、按 TP 分片的权重保存在 GPU 显存中，使引擎重启时可通过 CUDA IPC 直接映射权重（使用 --load-format ipc_cache），而无需从磁盘重新加载。 vLLM 是目前使用最广泛的开源大模型推理与服务引擎之一，其版本发布直接影响生产团队能够部署哪些模型和硬件。Fast Start 以及对新模型和硬件的广泛支持降低了重启延迟并扩展了部署选择，这对运行大规模、多节点或异构推理集群的团队尤为重要。 Fast Start 现在还支持 FP4 检查点和多节点张量并行；该版本还引入了用于稀疏 MLA 解码的 HiSparse 主机端 KV 分层、与投机解码兼容的 Gumbel-max 水印，以及 Model Runner V2 的改进，例如双批次重叠和更快的 CUDA 图捕获（在 H200 上将捕获时间从 12 秒缩短到 2 秒）。量化方面新增了通过 quantization_config.targets 实现的目标在线量化，以及在 SM100/103 上以 FlashInfer CuTeDSL NVFP4 W4A16 取代 Marlin 作为默认方案。

github · khluu · 9月22日 05:20

**背景**: vLLM 是一个用于服务大语言模型的开源引擎，以 PagedAttention 等实现高吞吐推理的技术而闻名。重启推理引擎通常需要从磁盘重新加载并重新量化模型权重，对于大模型来说这可能非常耗时。Fast Start 通过让权重在重启期间常驻 GPU 显存来解决这一问题；而 MXFP8 和 FlashMLA 则是用于加速 DeepSeek 等模型的低精度量化和优化注意力内核技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learnaivisually.com/ai-explained/vllm-0-30-persistent-gpu-weight-cache-cuda-ipc">vLLM 0.30 ships Fast Start — Persistent GPU weight cache via ...</a></li>
<li><a href="https://docs.vllm.ai/en/stable/api/vllm/model_executor/model_loader/weight_cache/daemon/">daemon - vLLM</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">FlashMLA</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#model serving`, `#release`, `#AI/ML systems`

---

<a id="item-4"></a>
## [高通为骁龙 X2 笔记本带来上游 Linux 支持](https://www.qualcomm.com/news/onq/2026/09/snapdragon-summit-agentic-ai-pcs-linux) ⭐️ 8.0/10

高通在骁龙峰会上宣布，骁龙 X2 系列笔记本将获得 Linux 支持，Hexagon NPU 和 Adreno GPU 的核心驱动将向上游主线内核提交。该工作面向骁龙 X2 Elite 及相关型号，OpenBSD/arm64 与 Ubuntu 上已出现早期移植成果。 这对运行 Linux 的 ARM 笔记本意义重大，因为高通上一代骁龙 X Elite 并未兑现 Linux 支持承诺，用户只能依赖 Windows。驱动上游化意味着各发行版可以开箱即用地支持这些设备，为开发者提供了苹果 M 系列和 x86 笔记本之外的可信选择。 该公告明确仅覆盖骁龙 X2 系列笔记本，不包含桌面形态、早期骁龙 X 平台或其他开发板，且就绪程度因 OEM 设计和芯片型号而异。社区报告指出 ARM EL2 现已可用，从而支持 KVM 虚拟化，这与前几代不同；OpenBSD 开发者 Tobias Heider 已提交初步 arm64 支持，使 HP EliteBook X G2q 在 ACPI 模式下实现 USB、键盘和触控板可用。

hackernews · aaronday · 9月23日 22:38 · [社区讨论](https://news.ycombinator.com/item?id=49823582)

**背景**: 骁龙 X2 是高通面向 Windows 笔记本的第二代 ARM 处理器家族，接替骁龙 X Elite 和 X Plus，将高通的 Oryon CPU 核心与 Adreno 集成显卡以及用于端侧 AI 的 Hexagon NPU 结合在一起。Hexagon 是高通用于低功耗 AI 推理的 DSP/NPU 品牌，Adreno 则是其 GPU 产品线，在 Linux 上通常由开源的 Freedreno/Turnip 驱动栈支持。驱动上游化意味着代码被贡献到 Linux 主线内核，而非以厂商专有二进制形式发布，因此各发行版和其他操作系统无需特殊构建即可支持该硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qualcomm_Hexagon">Qualcomm Hexagon - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Adreno">Adreno - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_Qualcomm_Snapdragon_systems_on_chips">List of Qualcomm Snapdragon systems on chips - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者总体热情高涨，有人认为高通的芯片是苹果 M 系列最接近的竞争对手，并优于英特尔和 AMD 的旗舰产品；也有人称此次上游化相比 Chromebook 那种半专有支持是巨大进步。其他人则强调具体进展，包括 OpenBSD/arm64 提交和已确认的 KVM 支持；而持怀疑态度者指出该支持仅限 X2 笔记本，且 x86 在开箱即用的 Linux 体验上仍占优势。

**标签**: `#Linux`, `#ARM`, `#Qualcomm`, `#Snapdragon`, `#Open Source`

---

<a id="item-5"></a>
## [Anthropic 称 Claude 发现具有 CRISPR 样重复序列的新型酶系统](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) ⭐️ 8.0/10

Anthropic 宣布其 AI 模型 Claude 在噬菌体 DNA 中自主发现了一个此前未被描述的酶系统，该酶的基因旁边存在一段类似 CRISPR 阵列的长串联重复序列。这一发现来自 Anthropic 首批 AI 驱动研究项目之一，但该系统的具体功能目前仍不清楚。 如果得到验证，这将是 AI 模型在基因组学领域做出真正科学发现的重要案例，而 CRISPR 等可编程 DNA 修饰系统历来对医学和生物技术产生了巨大影响。这也加剧了关于 AI 系统在研究中的贡献应如何认定以及此类发现应如何验证的争论。 该系统结合的特征此前只在少数其他系统中同时出现过，而这些系统都是可编程的，能够执行切割、复制和粘贴 DNA 等操作。评论者指出，该排列似乎围绕一种已知的逆转录酶（类似 retron）展开，并且这类工具在治疗上的实际瓶颈是递送而非靶向效率。

hackernews · raahelb · 9月23日 18:06 · [社区讨论](https://news.ycombinator.com/item?id=49820134)

**背景**: CRISPR 是细菌的一种免疫系统，利用重复 DNA 阵列和 Cas9 等相关酶来靶向并切割特定 DNA 序列，现已被改造为广泛使用的基因编辑工具。逆转录酶是能将 RNA 逆转录为 DNA 的酶，而 retron 是产生此类酶的细菌遗传元件。Anthropic 是一家 AI 公司，其 Claude 模型属于大语言模型，这条新闻也是利用 AI 辅助酶和蛋白质发现这一更广泛趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-discovers-novel-enzyme-system">Claude discovers a novel enzyme system with CRISPR-like repeats</a></li>
<li><a href="https://thenextweb.com/news/anthropic-claude-enzyme-system-crispr-like-repeats">Anthropic says Claude found a new enzyme system with CRISPR-like repeats</a></li>
<li><a href="https://en.wikipedia.org/wiki/CRISPR">CRISPR - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者总体上对宣传口径持怀疑态度，有人主张更冷静地描述为 Claude 识别出围绕一种已知逆转录酶的此前未描述的基因组排列，并指出治疗用途主要受递送限制。也有人对通过智能体记录重温 AI 发现感到兴奋，并对预印本的方法和提示词感到好奇；还有评论者指出，Anthropic 一边限制 Claude 用于生物工程，一边又宣布与基因编辑相关的发现，颇具讽刺意味。

**标签**: `#AI`, `#CRISPR`, `#genomics`, `#enzyme discovery`, `#Anthropic`

---

<a id="item-6"></a>
## [谷歌发布 Gemini 3.8 语音合成，支持 30 秒声音克隆](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/) ⭐️ 8.0/10

9 月 23 日，谷歌推出 Gemini 3.8 Flash TTS 和 Gemini 3.8 Flash-Lite TTS 两款全新语音合成模型，仅需 30 秒音频样本即可重建一致的声音特征。这些模型正在 Google AI Studio、Gemini API、Gemini Enterprise、Gemini Notebook 和 Google Vids 中陆续上线，并内置了同意验证、SynthID 水印和 C2PA 内容凭证。 声音克隆已足够普及，谷歌愿意在其旗舰语音合成模型中推出该功能，这可能会加速有声书、无障碍工具和企业语音应用的采用。与此同时，此次发布也凸显了谷歌在消费级、专业级和云平台之间日益严重的碎片化问题，并引发了关于同意和合成语音滥用的新伦理问题。 这些模型被定位为谷歌迄今最具表现力的音频生成模型，但各平台的可用性和功能存在差异——例如，与消费级和专业级平台相比，GCP 上的某些多模态功能受到限制。声音复制功能依托同意验证、SynthID 水印和 C2PA 凭证，以保护开发者和配音人才。

hackernews · swolpers · 9月23日 15:29 · [社区讨论](https://news.ycombinator.com/item?id=49817615)

**背景**: 语音合成（TTS）模型将书面文本转换为语音，近期的技术进步使其能够通过简短样本模仿特定人的声音。SynthID 是谷歌 DeepMind 的技术，可在 AI 生成内容中嵌入不可感知的水印，以便日后识别其为合成内容。C2PA（内容来源与真实性联盟）是一项开放标准，通过防篡改元数据记录媒体内容的创建和编辑方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/">Gemini 3.8 Flash TTS and Gemini 3.8 Flash-Lite TTS - The Keyword</a></li>
<li><a href="https://deepmind.google/models/synthid/">SynthID — Google DeepMind</a></li>
<li><a href="https://c2pa.org/">C2PA</a></li>

</ul>
</details>

**社区讨论**: 评论者指出谷歌在消费级、专业级和云平台上的发布不一致，并提到不同平台上模型的能力甚至有所不同。Simon Willison 观察到，声音克隆现已从其他提供商广泛可用，因此谷歌不再犹豫推出该功能；其他人则分享了本地托管有声书制作工具和同人小说广播剧等实际用例。

**标签**: `#text-to-speech`, `#voice-cloning`, `#Google Gemini`, `#AI ethics`, `#platform fragmentation`

---

<a id="item-7"></a>
## [ClusterMAX 3.0：SemiAnalysis 更新 GPU 云评级系统](https://newsletter.semianalysis.com/p/clustermax-30-the-industry-standard) ⭐️ 8.0/10

SemiAnalysis 发布了 ClusterMAX 3.0，这是其 GPU 云服务商行业标准评级系统的最新版本，覆盖全球服务商的可靠性、性能、支持、定价和安全性。此次更新紧随 2026 年 1 月发布的 ClusterMAX 2.0，为 AI/ML 基础设施买家提供了更深入的分析。 ClusterMAX 已成为评估 GPU 云服务商的事实行业基准，其评级影响着 AI 训练和推理基础设施的采购决策。3.0 更新之所以重要，是因为它在 GPU 需求和定价持续变化之际，为企业、新兴云厂商和超大规模云厂商提供了更及时、更全面的服务商比较依据。 ClusterMAX 系统对 80 多家 GPU 云进行评分，涵盖性能、网络、存储、安全、支持和定价，涉及 H100、H200、B200、GB200 NVL72 和 MI300X 等集群。SemiAnalysis 表示，该评级基于独立测试和客户反馈，旨在覆盖按 GPU 数量计约 90% 的 GPU 租赁市场。

rss · Semianalysis · 9月23日 21:20

**背景**: ClusterMAX 是由 SemiAnalysis 创建的评级和排名系统，该公司是一家专注于 GPU 和 AI 基础设施的分析机构，旨在评估租用 GPU 计算资源的体验。该系统于 2025 年首次推出，此后成为比较 GPU 云服务商时被广泛引用的参考。系统从性能、可靠性、支持、定价和安全性等维度评估服务商，帮助买家在由超大规模云厂商、新兴云厂商和 GPU 市场组成的碎片化市场中做出选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.clustermax.ai/">GPU Cloud ClusterMAX™ Rating & Ranking System | SemiAnalysis</a></li>
<li><a href="https://newsletter.semianalysis.com/p/the-gpu-cloud-clustermax-rating-system-how-to-rent-gpus">The GPU Cloud ClusterMAX™ Rating System | How to Rent GPUs</a></li>
<li><a href="https://newsletter.semianalysis.com/p/clustermax-20-the-industry-standard">ClusterMAX™ 2.0: The Industry Standard GPU Cloud Rating System</a></li>

</ul>
</details>

**标签**: `#GPU cloud`, `#cloud computing`, `#AI infrastructure`, `#benchmarking`, `#industry analysis`

---

<a id="item-8"></a>
## [Complex KDA 扩展 Kimi Delta Attention 的表达能力](https://www.reddit.com/r/MachineLearning/comments/1wn5uv9/understanding_and_enhancing_kimi_delta_attention_r/) ⭐️ 8.0/10

一篇新论文分析了 Gated DeltaNet（GDN）与 Kimi Delta Attention（KDA）之间的表达能力差异，指出 KDA 的完整对角门可以充当反射，从而在单步内完成二维旋转，但前提是把门的取值范围扩展到 [-1,1]、把 delta 规则的学习率扩展到 [0,2]，作者将这一变体称为 Complex KDA（CKDA）。实验表明 CKDA 能够学习 S3 和 S4 群任务，在音频续写任务上表现良好，并在语言建模上稳定训练且与标准 KDA 具有竞争力。 这项工作从理论上解释了 KDA 为何比 GDN 更具表达能力，并给出了一种具体且低成本的改进方案（CKDA），扩大了模型可表示的变换类别，可为未来面向长上下文和多模态的线性注意力架构设计提供参考。它还把注意力机制与群论联系起来，为研究者理解序列模型能表示什么、不能表示什么提供了新的视角。 理论表明，CKDA 可以表示任意正交的对角加秩一矩阵，并能跟踪 S3、S4 和 A5 群，但值得注意的是无法跟踪 S5，说明其表达能力存在明确上限。这些收益依赖于把门范围放宽到 [-1,1]、把 delta 规则学习率放宽到 [0,2]，这与标准 KDA 的配置有所不同。

reddit · r/MachineLearning · /u/Yossarian_1234 · 9月22日 10:34

**背景**: Kimi Delta Attention（KDA）是 Kimi Linear 架构中提出的一种线性注意力模块，它在 Gated DeltaNet（GDN）的基础上引入了更细粒度的对角门控；而 GDN 本身通过把 delta 规则与输入相关的门控结合，改进了 Mamba2 的记忆保持与选择性。线性注意力模型的复杂度随上下文长度线性增长而非二次增长，但这种效率的代价是相比完整的成对注意力会损失部分全局上下文建模能力。delta 规则是一种经典的类梯度下降学习规则，根据目标输出与实际输出之差来更新权重，在这里其学习率范围是影响表达能力的关键调节项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.26692">Kimi Linear: An Expressive, Efficient Attention Architecture - arXiv</a></li>
<li><a href="https://arxiv.org/abs/2412.06464">[2412.06464] Gated Delta Networks: Improving Mamba2 with Delta Rule</a></li>
<li><a href="https://en.wikipedia.org/wiki/Delta_rule">Delta rule - Wikipedia</a></li>

</ul>
</details>

**标签**: `#attention mechanisms`, `#deep learning theory`, `#expressivity`, `#Kimi Delta Attention`, `#group theory`

---

<a id="item-9"></a>
## [黑客组织 ShinyHunters 声称入侵 FBI，窃取员工及申请者数据](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) ⭐️ 8.0/10

网络犯罪组织 ShinyHunters 声称已入侵多个与 FBI 相关的服务，窃取了所有 FBI 员工及求职申请者的数据，并提供了一份约 5000 名所谓员工的样本，其中包含姓名、住址、电话号码以及配偶等家属信息。FBI 尚未确认这一说法，404 Media 的报道称该组织据称利用了 Oracle PeopleSoft 的一个新零日漏洞来访问内部系统。 如果数据属实，泄露的个人及家属信息可能被用于跟踪、骚扰甚至威胁 FBI 员工及其家属，对美国执法和情报系统构成严重的安全与反情报风险。这一事件也凸显了 Oracle PeopleSoft 等广泛使用的企业软件如何成为针对政府系统的高价值攻击入口。 据报道，约 5000 条记录的样本包含姓名、住址、电话号码和配偶信息，但被盗数据的完整范围和真实性仍未得到证实。ShinyHunters 据称通过 Oracle PeopleSoft 的一个新零日漏洞获得访问权限，FBI 正在调查这起疑似入侵事件。

telegram · zaihuapd · 9月23日 05:00

**背景**: ShinyHunters 是一个自 2019 年以来活跃的黑帽犯罪黑客和勒索组织，以大规模数据窃取和勒索活动著称。Oracle PeopleSoft 是一款广泛使用的企业资源规划和人力资源软件套件，而零日漏洞是指攻击者可以在补丁发布前利用的此前未知的缺陷。404 Media 是一家由记者独立拥有的科技新闻媒体，曾率先报道过多起重大黑客和网络安全事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ShinyHunters">ShinyHunters - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2026/09/22/hacking-group-shinyhunters-claims-it-breached-the-fbi-stole-agents-and-applicants-data/">Hacking group ShinyHunters claims it breached the FBI, stole ...</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/">ShinyHunters claims FBI hack, data theft in PeopleSoft zero-day breach</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#data breach`, `#FBI`, `#ShinyHunters`, `#national security`

---