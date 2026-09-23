---
layout: default
title: "Horizon Summary: 2026-09-23 (ZH)"
date: 2026-09-23
lang: zh
---

> 从 95 条内容中筛选出 14 条重要资讯。

---

1. [Anthropic 称 Claude 发现了一种类似 CRISPR 的新型酶系统](#item-1) ⭐️ 9.0/10
2. [Anthropic 与 OpenAI 相继发布 Claude Opus 5.5 与 GPT-6 Sol/Luna，引发价格战](#item-2) ⭐️ 9.0/10
3. [vLLM v0.30.0 发布：新增多款模型、Fast Start 权重缓存与 MXFP8 KV](#item-3) ⭐️ 8.0/10
4. [谷歌发布 Gemini 3.8 语音合成，支持 30 秒克隆声音](#item-4) ⭐️ 8.0/10
5. [用 25 行 Python 实现 Jev：极简 LLM 对数概率分类器](#item-5) ⭐️ 8.0/10
6. [西雅图市议会通过法案禁止食品杂货监控定价](#item-6) ⭐️ 8.0/10
7. [OpenAI 的 GPT-6 Astra 据称破解了长期未解的 Enigma 密文](#item-7) ⭐️ 8.0/10
8. [GPT-6 Astra 展示出驾驶汽车的能力](#item-8) ⭐️ 8.0/10
9. [TypeSafe AI 发布 Jev：一种“System One”决策模型](#item-9) ⭐️ 8.0/10
10. [小米发布 MiMo-V2.6 多模态模型，强化学习成本 350 万美元](#item-10) ⭐️ 8.0/10
11. [中国调查 DeepSeek 与月之暗面涉嫌向 Claude 泄露数据](#item-11) ⭐️ 8.0/10
12. [DeepSeek 本周将向联合国安理会通报 AI 风险](#item-12) ⭐️ 8.0/10
13. [OpenAI 开始有限预览 GPT-5.6 系列：Sol、Terra、Luna](#item-13) ⭐️ 8.0/10
14. [ShinyHunters 声称入侵 FBI 并窃取员工及申请者数据](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 称 Claude 发现了一种类似 CRISPR 的新型酶系统](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) ⭐️ 9.0/10

Anthropic 宣布其 AI 模型 Claude 发现了一种此前未知的酶系统，该酶的基因旁边有一段与 CRISPR 重复序列相似的长重复 DNA 阵列。这一发现以 Anthropic 官方新闻稿的形式发布，而非传统的同行评审期刊投稿或预印本。 CRISPR 重复序列是现代基因编辑药物的基础，因此 AI 发现的类似 CRISPR 的系统可能指向新的基因编辑或生物技术工具。这也引发了关于 AI 公司是否应自行开展并发布前沿科学研究、而非与学术实验室合作的争论。 Anthropic 指出，目前尚不清楚这段重复 DNA 结构的功能，该发现也尚未经过同行评审验证。社区成员还质疑，这一系统究竟是 Claude 自主发现的，还是使用 Claude 的人类发现的。

hackernews · raahelb · 9月23日 18:06 · [社区讨论](https://news.ycombinator.com/item?id=49820134)

**背景**: CRISPR 是存在于细菌和古菌中的一类 DNA 序列，最初是作为异常的重复序列被注意到的，如今已成为基因编辑疗法的基础。AI 驱动的科学发现利用机器学习分析大规模数据集，并找出人类可能难以察觉的模式。Anthropic 一直在拓展科学工具领域，包括面向研究人员的 Claude Science 工作台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-discovers-novel-enzyme-system">Claude discovers a novel enzyme system with CRISPR-like repeats - Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/CRISPR">CRISPR - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists - Anthropic</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：一些人批评 Anthropic 发布的是营销白皮书而非期刊投稿，另一些人则质疑 AI 公司为何要在内部开展这类研究而不与外部合作。还有人指出，对 LLM 而言生物学比数学更难，问题范围已被大幅缩小，不过许多人对这项工作本身表示欢迎。

**标签**: `#AI`, `#CRISPR`, `#scientific discovery`, `#Anthropic`, `#biotechnology`

---

<a id="item-2"></a>
## [Anthropic 与 OpenAI 相继发布 Claude Opus 5.5 与 GPT-6 Sol/Luna，引发价格战](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 9.0/10

Anthropic 发布了 Claude Opus 5.5，大约一小时后 OpenAI 发布了 GPT-6 Sol 和 GPT-6 Luna，其中 GPT-6 Luna 的价格仅为前代 GPT-5.6 Luna 的一半（输入$0.10/百万 token，输出$0.50/百万 token）。Claude Opus 5.5 也同步降价，现为输入$4/百万 token、输出$20/百万 token。 这次同步发布与大幅降价标志着前沿模型厂商之间的价格战进一步升级，显著降低了构建 AI 应用的成本，并可能重塑开发者在生产环境中选用模型的格局。 GPT-6 Luna 以$0.10/$0.50 的价格成为 OpenAI 有史以来最便宜的模型之一，仅弱于能力更低的 GPT-4.1 Nano 和 GPT-5 Nano；GPT-5.6 计划在 11 月涨价 25%，因此 GPT-6 的价格甚至只有促销价的一半。

rss · Simon Willison · 9月22日 23:46

**背景**: Anthropic 和 OpenAI 等前沿 AI 实验室会定期发布新的旗舰大语言模型，而每百万 token 的定价是开发者构建应用时的关键竞争杠杆。Anthropic 的 Claude 系列分为 Haiku、Sonnet 和 Opus 三档，而 OpenAI 的 GPT-6 家族则在现有 Terra 和 Astra 之外新增了 Sol 和 Luna 两个变体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://x.ai/news/grok-4-7">Introducing Grok 4.7 - SpaceXAI</a></li>
<li><a href="https://artificialanalysis.ai/models/claude-opus-5-5">Claude Opus 5 . 5 (max with fallback) - Intelligence... | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 评论者认为 GPT-6 Luna 价格减半是一大进展，有人提到对前代 GPT-5.6 Sol 产生了情感依赖，并担心后继模型虽然技术上更强但用起来不够自然。其他人比较了 Claude Code 与 Codex Pro 订阅的性价比，认为 Codex 在使用额度上胜出，也有人称赞 ChatGPT Plus 在日常任务上几乎无限量。

**标签**: `#AI`, `#LLM`, `#OpenAI`, `#Anthropic`, `#model-releases`

---

<a id="item-3"></a>
## [vLLM v0.30.0 发布：新增多款模型、Fast Start 权重缓存与 MXFP8 KV](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM 发布 v0.30.0，这是一个包含 315 位贡献者（其中 104 位新贡献者）提交的 762 个 commit 的重大版本，新增支持 DeepSeek-V4.1-Flash、DeepSeek-V4-Flash-Vision-Exp、GLM-5.3-Flash、K2-Horizon、Cohere Compass、Bailing V3 VL 和 Nanbeige4.2 等模型。该版本引入了名为 Fast Start 的持久化每 GPU 权重缓存守护进程、SM100 上 DeepSeek-V4.1-Flash 的 MXFP8 KV 存储、Gumbel-max 水印、HiSparse 主机端 KV 分层，以及针对 Qwen3.8-Flash-Next 和 Kimi K3 的大量性能优化。 vLLM 是目前使用最广泛的开源 LLM 推理与服务引擎之一，因此该版本会直接影响大规模部署模型的 AI 基础设施团队。Fast Start 权重缓存和 MXFP8 KV 存储等功能可以显著降低引擎启动时间和 GPU 显存压力，而对众多新模型的支持则使 vLLM 持续跟上开源权重 LLM 的快速演进。 Fast Start 将量化后、按 TP 分片的权重保留在 GPU 显存中，并通过 `--load-format ipc_cache` 以 CUDA IPC 方式映射，目前已覆盖 FP4 检查点和多节点 TP。HiSparse 在 GPU 显存压力下将稀疏 MLA 的 KV 页溢出到锁页主机内存，并从每请求的 GPU 热缓冲区服务 top-k 未命中；Model Runner V2 在 H200 上将图捕获时间从 12 秒降至 2 秒，引擎初始化从 28.9 秒降至 8.2 秒。

github · khluu · 9月22日 05:20

**背景**: vLLM 是一个开源的高吞吐量大语言模型服务引擎，基于 PagedAttention 和连续批处理等技术来最大化 GPU 利用率。KV 缓存指注意力计算过程中存储的键/值张量，其大小往往限制服务器能同时处理的请求数量；将其量化为 MXFP8 等格式可以降低这部分显存占用。FlashMLA 是 DeepSeek 为其基于 MLA 的模型提供的优化注意力内核库，而投机解码则通过小规模草稿模型提出候选 token、再由大模型验证，从而加速生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/stable/configuration/optimization/">Optimization and Tuning - vLLM Documentation</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">FlashMLA</a></li>
<li><a href="https://docs.vllm.ai/en/stable/design/prefix_caching/">Automatic Prefix Caching - vLLM Documentation</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#model serving`, `#release`, `#AI infrastructure`

---

<a id="item-4"></a>
## [谷歌发布 Gemini 3.8 语音合成，支持 30 秒克隆声音](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/) ⭐️ 8.0/10

谷歌发布了 Gemini 3.8 Flash 和 Flash-Lite 文本转语音模型，只需 30 秒的音频样本即可重建一致的声音特征，提供超过 2000 种生产级音色，并支持 100 种语言。该版本内置了同意验证、SynthID 水印和 C2PA 内容凭证，以保护配音人员和开发者。 这标志着谷歌全面拥抱声音克隆技术，而该能力此前已由其他厂商提供，此举可能加速个性化合成语音在有声书、游戏和无障碍工具中的普及。同意验证和水印的加入为符合伦理的语音 AI 部署树立了潜在的行业先例。 该模型针对大批量生产、对话式语音代理和朗读功能进行了优化，并声称在 Hume AI 的语音基准测试中排名第一。声音混音功能被列为即将推出，且该模型在谷歌的消费者、专业消费者和云平台上的可用性各不相同。

hackernews · swolpers · 9月23日 15:29 · [社区讨论](https://news.ycombinator.com/item?id=49817615)

**背景**: 文本转语音（TTS）系统将书面文本转换为语音音频，而近期的 AI 模型已能通过简短样本模仿特定人物的声音。SynthID 是谷歌 DeepMind 的技术，可在 AI 生成内容中嵌入不可见的数字水印；C2PA 则是一项开放标准，通过加密签名的来源元数据记录媒体内容的创建和编辑过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/">Gemini 3.8 text-to-speech says hello</a></li>
<li><a href="https://deepmind.google/models/synthid/">SynthID — Google DeepMind</a></li>
<li><a href="https://c2pa.org/">C2PA</a></li>

</ul>
</details>

**社区讨论**: 评论者批评谷歌在消费者、专业消费者和云平台之间的功能可用性不一致，指出模型在各平台上的能力往往不同。其他人则认为声音克隆如今已足够普遍，谷歌不再犹豫推出该功能；还有人分享了自己的 TTS 实践项目，并对庞大的音色库和精细控制表示欢迎。

**标签**: `#AI`, `#text-to-speech`, `#voice cloning`, `#Google Gemini`, `#Hacker News`

---

<a id="item-5"></a>
## [用 25 行 Python 实现 Jev：极简 LLM 对数概率分类器](https://www.nobodywho.ai/posts/jev-in-25-lines/) ⭐️ 8.0/10

nobodywho.ai 上的一篇博客文章展示了如何仅用 25 行 Python 代码实现 Jev——一种直接从 LLM 的 token 对数概率中提取分类概率的技术。该文章引发了大量讨论（564 分，182 条评论），参与者包括 Redis 的创造者 antirez 等知名实践者。 这一极简实现让强大的分类技术对任何 Python 开发者都触手可及，有望降低目前依赖完整 LLM 文本生成的文本分类任务的成本和延迟。高规格的社区讨论揭示了实际应用中的陷阱和优化技巧，可能影响实践者采用基于对数概率的分类方式。 讨论指出，聊天模型倾向于稀释选择 token 的概率，因为它们被训练来生成散文，因此需要精心设计的系统指令和提示格式。antirez 指出，由于掩码注意力机制，将选项放在文本主体之前可以让 Transformer 使用更多 token 为任务构建状态，重复问题也能改善校准。

hackernews · bashbjorn · 9月23日 07:26 · [社区讨论](https://news.ycombinator.com/item?id=49812769)

**背景**: Jev 是 TypeSafe 提出的一种分类方法，它利用 LLM 的对数概率（logprobs）——即分配给每个 token 的概率的对数——来判断一段文本属于哪个预定义类别，而不是生成自由文本。对数概率来自模型原始 logits 经过 softmax 函数后的结果，为分类提供了自然的置信度分数。这种方法避免了完整文本生成的延迟和成本，同时利用了 LLM 对语言的理解能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jev_(AI_model)">Jev (AI model) - Wikipedia</a></li>
<li><a href="https://www.langchain.com/blog/building-a-harness-with-jev">What Is Jev? A Guide to TypeSafe AI’s System One Model</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为该技术很巧妙，但也提出了重要警告：sigmoid10 指出聊天模型会稀释选择 token 的概率，建议使用清晰的系统指令；antirez 建议将选项放在文本之前并重复任务以改善校准。visarga 分享了一种基于嵌入的替代分类器，使用岭回归在不到一秒内训练完成，并指出 Jev 缺乏领域内训练数据；rcarmo 则描述了在本地 GPU 上用 Gemma 进行原型开发的经验。

**标签**: `#LLM`, `#classification`, `#logprobs`, `#Python`, `#prompt-engineering`

---

<a id="item-6"></a>
## [西雅图市议会通过法案禁止食品杂货监控定价](https://advocacy.consumerreports.org/press_release/seattle-city-council-votes-to-ban-surveillance-pricing-in-sale-of-groceries/) ⭐️ 8.0/10

西雅图市议会投票通过法案，禁止在食品杂货销售中使用监控定价，禁止零售商利用消费者个人数据为食品设定个性化价格。该法案同时允许多种折扣做法，但要求提高折扣透明度，并对消费者画像的使用施加一定限制。 这是美国首批针对监控定价的城市禁令之一，为其他城市和州监管算法个性化定价树立了先例。它可能影响更广泛的消费者保护行动，并促使零售商重新思考食品杂货及其他领域的数据驱动定价策略。 该禁令仅适用于食品杂货，并包含折扣漏洞，允许零售商提供个性化折扣，批评者认为这可能削弱法律初衷。法案还要求提高折扣透明度，并对消费者画像施加一定限制。

hackernews · ortusdux · 9月23日 14:04 · [社区讨论](https://news.ycombinator.com/item?id=49816374)

**背景**: 监控定价是一种动态定价形式，利用消费者的个人数据和行为推断其支付意愿，常导致同一商品对不同人价格不同。它引发了关于算法歧视、消费者隐私和数字红线的担忧，近期多个州已考虑或颁布相关法规。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Surveillance_pricing">Surveillance pricing</a></li>
<li><a href="https://epic.org/issues/consumer-privacy/surveillance-pricing/">Surveillance Pricing – EPIC – Electronic Privacy Information Center</a></li>
<li><a href="https://www.brookings.edu/articles/what-is-dynamic-pricing-and-why-do-consumers-need-better-protections/">What is dynamic pricing, and why do consumers need better protections? | Brookings</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者普遍支持该禁令，但对其适用范围存在争议，有人认为应适用于所有商品和服务，而不仅是食品杂货。其他人则指出折扣漏洞，并呼吁加强隐私保护，例如宪法层面的隐私权。

**标签**: `#privacy`, `#surveillance-pricing`, `#regulation`, `#consumer-protection`, `#algorithmic-fairness`

---

<a id="item-7"></a>
## [OpenAI 的 GPT-6 Astra 据称破解了长期未解的 Enigma 密文](https://www.cryptocellar.org/bgac/the-mvueh-break.html) ⭐️ 8.0/10

据报道，OpenAI 的 GPT-6 Astra 成功解密了一条 82 个字母的 Enigma 加密信息，该信息以指示符 MVUEH 为标识，自 2005 年以来一直列在 Frode Weierud 的 CryptoCellar 研究网站上未被破解。解密后的文本大致为：“请说明行军路线。我在罗森诺，罗森诺。立即通过无线电回复。瓦施布施。” 如果得到验证，这标志着 AI 辅助密码分析的一个重要里程碑，表明大型语言模型能够为解决数十年来人类和计算努力都未能破解的历史密码做出贡献。这也引发了更广泛的争论：当 AI 依赖生成或现有的软件工具来执行实际计算时，它应该获得多少功劳。 该信息的明文包含战地传输中常见的拼写错误，据称解密是通过 GPT-6 Astra 开发用于 Enigma 模拟器的 Python 和 C++软件实现的。怀疑者指出，生成的代码可能大部分并非原创，实际破解过程可能被外包给了该软件，从而引发了对 AI 真正贡献的质疑。

hackernews · sohkamyung · 9月22日 13:52 · [社区讨论](https://news.ycombinator.com/item?id=49801324)

**背景**: Enigma 密码机是二战期间纳粹德国使用的基于转子的加密设备；其密码由艾伦·图灵和布莱切利园的其他人员著名地破解，极大地帮助了盟军的战争努力。尽管取得了这些成功，但由于缺少密钥设置或操作员错误，一些个别信息数十年来一直未被破解。Frode Weierud 的 CryptoCellar 网站维护了一份此类未破解信息的清单，而 MVUEH 信息自 2005 年以来一直在该清单上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mixed-news.com/en/gpt-6-astra-cracks-1941-enigma-message-unsolved-since-2005/">GPT-6 Astra cracks a 1941 Enigma message that had resisted solution since 2005</a></li>
<li><a href="https://news.ycombinator.com/item?id=49801324">OpenAI GPT–6 Astra breaks Enigma message that has resisted solution since 2005 | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cryptanalysis_of_the_Enigma">Cryptanalysis of the Enigma - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者对 GPT-6 Astra 的新颖性和所获功劳表示怀疑，其中一人指出“完全靠自己完成”与 AI 为 Enigma 模拟器开发软件的说法不一致。另一位评论者报告称，Gemini 3.8 Flash 也在约 45 分钟内解决了该信息，表明这项任务对先进模型来说可能并非独一无二的挑战。其他人分享了解密文本，并提到 Veritasium 最近关于 Enigma 的视频，还有人开玩笑说这个解决方案“对战争努力来说有点晚了”。

**标签**: `#AI`, `#cryptography`, `#Enigma`, `#OpenAI`, `#Hacker News`

---

<a id="item-8"></a>
## [GPT-6 Astra 展示出驾驶汽车的能力](https://drivingbench.com/) ⭐️ 8.0/10

OpenAI 于 2026 年 9 月发布的 GPT-6 Astra 在 drivingbench.com 的基准测试中被演示能够驾驶汽车，在 Hacker News 上引发热烈讨论（249 分、213 条评论）。该演示表明，云端交付的大语言模型能够将传感器输入映射为转向和致动器输出，足以完成一段驾驶路线。 这表明基于大语言模型的端到端驾驶最终可能挑战由视觉、3D 地图、车道选择语法和占用网络组成的传统模块化自动驾驶技术栈。如果出现低延迟的开源权重替代方案，可能会重塑自动驾驶系统的构建方式以及谁能构建它们。 核心限制在于延迟：模型太大，无法在本地运行，因此云端往返使得现实世界驾驶目前不可行。评论者还指出 Astra 在视觉和空间推理方面异常强大，这体现在其较高的 ARC 3、SpatialBench 和 ZeroBench 分数上，可能解释了其驾驶能力。

hackernews · plurby · 9月23日 15:14 · [社区讨论](https://news.ycombinator.com/item?id=49817404)

**背景**: GPT-6 Astra 是 OpenAI 于 2026 年 9 月 3 日向获批用户发布的大语言模型，次日全面开放。自动驾驶传统上依赖由摄像头、激光雷达、高精地图和手工设计规划器组成的模块化流水线，而近期 LMDrive、Talk2Drive 等研究探索了将大语言模型用作驾驶智能体。drivingbench.com 的演示测试了通用大语言模型能否直接从传感器数据控制车辆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT - 6 Astra : A new generation of intelligence | OpenAI</a></li>
<li><a href="https://paperswithcode.co/paper/2312.07488">LMDrive: Closed-Loop End - to - End Driving with Large Language ...</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：一位 openpilot 贡献者认为该演示证明大语言模型可以驾驶一段路线，但由于延迟问题在现实世界中绝对行不通；另一些人则表示“苦涩的教训”即将降临自动驾驶，像 Qwen 这样的开源权重低延迟替代方案不会太远。多人称赞 Astra 的视觉和空间推理分数，还有人开玩笑说它接下来能降落飞机或实现社区自动泊车。

**标签**: `#LLM`, `#autonomous driving`, `#GPT-6`, `#AI`, `#self-driving cars`

---

<a id="item-9"></a>
## [TypeSafe AI 发布 Jev：一种“System One”决策模型](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 8.0/10

TypeSafe AI 发布了其首个公开的“System One”模型 Jev，它接收非结构化文本输入，返回类型化的概率输出——包括是/否（Noul）置信度、选项概率分布和数值评分——而不是生成文本。其定价为每百万输入 token 0.042 美元且输出免费，比 OpenAI 的 GPT-5 Nano（每百万 0.05 美元）更便宜，目前已开放早期访问。 Jev 代表了一种全新的模型类别，将 LLM 推理重新定义为类型化的决策函数而非文本生成，使其在垃圾邮件检测、标签推荐、优先级排序和搜索重排等分类任务上速度更快、成本更低。如果这一路线成立，可能会让大量企业自动化工作负载从通用聊天模型转向专用决策模型。 Jev 支持三类问题——Noul（伯努利）是/否置信度、返回选项概率分布的选择题，以及在给定数值区间内返回浮点分数的评分题——并可针对单个“state”文档并行评估多个问题。其自身的“jaggedness”文档指出它在数字、日期和对抗性内容上表现不佳，而且由于只返回浮点数，它无法为决策提供自然语言解释。

rss · Simon Willison · 9月21日 23:09

**背景**: 大多数 LLM 是自回归的：它们一次生成一个 token，这也是输出 token 通常比输入 token 定价更高的原因。TypeSafe AI 将“System One”模型定位为专门用于在软件内部做决策的独立类别，类似于快速、直觉式的“系统 1”思维，而非深思熟虑的推理。结构化输出 API 已经可以强制 LLM 输出合法 JSON，但模型本质上仍在生成文本，其给出的置信度是文字描述，而不是应用程序可以据以分支判断的数值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models & Jev - TypeSafe AI Blog</a></li>
<li><a href="https://www.mindstudio.ai/blog/jev-system-one-model-launch">Jev Explained: Typesafe AI's Non-Autoregressive System-1 Model | MindStudio</a></li>
<li><a href="https://apimaster.ai/blog/jev-vs-llm">Jev vs LLMs: Where a Decision Model Beats Prompting... | APIMaster.AI</a></li>

</ul>
</details>

**社区讨论**: Simon Willison 支持 Maggie Appleton 提出的“决策模型”这一说法，认为它比 TypeSafe 的“System One”命名更好，这场命名之争也表明社区确实在认真讨论。Willison 还表达了一丝不安：Jev 让机器学习进一步走向黑箱系统，因为它只返回一个浮点数，不解释是哪些内容信号促成了该决策。

**标签**: `#LLM`, `#AI/ML`, `#decision-models`, `#inference`, `#model-architecture`

---

<a id="item-10"></a>
## [小米发布 MiMo-V2.6 多模态模型，强化学习成本 350 万美元](https://www.reddit.com/r/MachineLearning/comments/1wn36d4/xiaomi_releases_mimov26_frontier_intelligence_all/) ⭐️ 8.0/10

小米正式发布并开源了 MiMo-V2.6 系列，这是一款前沿多模态 AI 模型，其强化学习训练总成本公开为 350 万美元。此次发布还附带一个实时"benchmaxxing"仪表盘，公开追踪该模型的基准测试表现。 公开具体的 350 万美元强化学习训练成本以及公开的基准测试仪表盘，为通常保密的前沿模型开发带来了罕见的透明度。这可能促使其他实验室公开训练经济性，并为开源社区提供更具成本效益的多模态训练参考。 MiMo-V2.6 已在 Hugging Face 上提供（包括 Flash-RL 变体），推荐采样参数为 temperature=1.0 和 top_p=0.95，同时可通过 AI Studio、MiMo Code、小米 MiMo 桌面端、MiMo 开放平台 API 以及 OpenRouter 访问。据报道，小米的材料专家使用 MiMo-V2.6-Pro 设计了一种新型金属有机框架（MOF），用于吸附 PFAS"永久化学品"。

reddit · r/MachineLearning · /u/we_are_mammals · 9月22日 07:56

**背景**: MiMo 是小米自研的大模型系列，V2.6 侧重于扩大强化学习（RL）规模以实现自我改进。强化学习是一种后训练技术，模型从奖励信号而非标注样本中学习，其计算成本是前沿 AI 支出的主要驱动因素。"Benchmaxxing"指专门针对公开基准测试优化模型以取得高分，因此实时仪表盘会引发外界对报告的性能提升是否真实的审视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo - V 2 . 6 | Xiaomi</a></li>
<li><a href="https://mimo.mi.com/docs/en-US/news/latest/v2-6">Xiaomi MiMo Home</a></li>
<li><a href="https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL">XiaomiMiMo/ MiMo - V 2 . 6 -Flash-RL · Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI`, `#Multimodal`, `#Xiaomi`, `#Model Release`, `#Reinforcement Learning`

---

<a id="item-11"></a>
## [中国调查 DeepSeek 与月之暗面涉嫌向 Claude 泄露数据](https://www.theinformation.com/articles/china-probes-deepseek-moonshot-potential-data-leaks-anthropic) ⭐️ 8.0/10

中国互联网监管机构正在调查 DeepSeek 和月之暗面，起因是两家公司被指将敏感用户数据转发给 Anthropic 的 Claude 模型。此次调查由 Anthropic 于 9 月 10 日发布的 154 页报告引发，该报告指控 7 家中国公司大规模违规使用 Claude，并举例称 DeepSeek 曾把一名警方监控系统开发工程师的请求转发给 Claude。 这是一起罕见的案例：中国监管机构因跨境数据流动问题调查本国 AI 明星企业，可能重塑中国 AI 公司使用外国模型和处理敏感用户数据的方式。这也让 Anthropic 等美国模型提供商面临更大压力，其服务条款和数据处理实践如今处于地缘政治与合规争议的中心。 调查源于 Anthropic 的 154 页报告，该报告点名 7 家中国公司，并特别指称 DeepSeek 将一名开发警方监控系统的工程师的请求转发给了 Claude。调查由中国互联网监管机构进行，涉事公司目前尚未公开回应。

telegram · zaihuapd · 9月22日 14:37

**背景**: DeepSeek 是一家总部位于杭州的 AI 公司，由对冲基金幻方量化（High-Flyer）所有，以发布开放权重的大语言模型而闻名；月之暗面（Moonshot AI）则是一家总部位于北京的 AI 初创公司。Anthropic 是 Claude 系列大语言模型背后的美国公司，Claude 于 2023 年 3 月首次以聊天机器人形式发布。中国 AI 开发者有时会使用 Claude 等外国模型进行数据生成或基准测试等任务，这可能与模型提供商的服务条款以及中国的数据安全法规产生冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#data privacy`, `#DeepSeek`, `#Moonshot AI`, `#Anthropic`

---

<a id="item-12"></a>
## [DeepSeek 本周将向联合国安理会通报 AI 风险](https://t.me/zaihuapd/43989) ⭐️ 8.0/10

两名知情人士称，中国 AI 初创公司 DeepSeek 本周将向由 15 个成员组成的联合国安理会通报人工智能带来的风险，OpenAI 首席执行官 Sam Altman 计划出席周三关于 AI 与国际安全的会议，Anthropic 高层代表预计也将参加。DeepSeek 和月之暗面（Moonshot）等中国 AI 公司受邀发言，但 DeepSeek 创始人梁文锋不打算出席，相关安排仍可能临时变动。 这标志着一个罕见时刻：一家中国 AI 初创公司与美国领先的 AI 实验室同台参与全球治理，凸显 AI 安全已从纯技术议题上升为国际安全的首要议题。这也表明中国 AI 企业的国际地位正在上升，并可能影响未来大国之间全球 AI 规则的谈判走向。 简报定于周三在拥有 15 个成员的安理会举行，议程涵盖 AI 与国际安全；DeepSeek 创始人梁文锋预计不会出席，发言名单仍可能临时变动。DeepSeek 是一家总部位于杭州的开源权重大语言模型开发商，由对冲基金幻方量化（High-Flyer）拥有并出资。

telegram · zaihuapd · 9月22日 17:39

**背景**: 联合国安理会是主要负责维护国际和平与安全的机构，随着人工智能技术快速进步引发滥用和失控担忧，安理会日益关注这一议题。DeepSeek 是一家中国 AI 公司，以发布开源权重大语言模型著称，其 DeepSeek-R1 于 2025 年初成为美国 iOS 应用商店下载量最高的免费应用。Anthropic 是一家美国 AI 安全与研究公司，OpenAI 则是 ChatGPT 的开发者，由 Sam Altman 领导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://news.un.org/en/story/2026/09/1168414">LIVE: OpenAI and Anthropic to brief Security Council as AI ... | UN News</a></li>
<li><a href="https://cointelegraph.com/news/openai-anthropic-to-brief-un-security-council-on-ai-risks">OpenAI and Anthropic CEOs Join UN Security Council AI Briefing</a></li>

</ul>
</details>

**标签**: `#AI governance`, `#DeepSeek`, `#UN Security Council`, `#AI safety`, `#international policy`

---

<a id="item-13"></a>
## [OpenAI 开始有限预览 GPT-5.6 系列：Sol、Terra、Luna](https://t.me/zaihuapd/43990) ⭐️ 8.0/10

OpenAI 已开始有限预览 GPT-5.6 系列，包括旗舰模型 Sol、均衡型 Terra 和低成本 Luna，首批面向少数可信伙伴通过 API 和 Codex 提供。Sol 主打更强的编码、生物和网络安全能力，并新增 max 推理强度和 ultra 模式；Terra 性能接近 GPT-5.5 且便宜约 2 倍，Luna 则定位为最低成本选择。 此次预览表明 OpenAI 持续推进分层模型家族策略，让开发者可以在能力、速度和成本之间权衡，这可能重塑团队为编码智能体和生产负载选择模型的方式。应美国政府要求、仅面向伙伴的发布方式，也凸显出前沿 AI 实验室与监管机构在广泛公开前的日益密切的审查与协调。 三个层级按每 100 万 token 计价：Sol 为输入 $5 / 输出 $30，Terra 为输入 $2.50 / 输出 $15，Luna 为输入 $1 / 输出 $6。OpenAI 未公布参数量或架构描述，且此次预览严格意义上属于闭门测试，计划在未来几周内扩大到 ChatGPT、Codex 和 API。

telegram · zaihuapd · 9月22日 18:04

**背景**: OpenAI 的 GPT 系列是其旗舰大语言模型家族，公司近年来越来越多地以多个规模层级发布模型，让用户根据预算和性能需求进行选择。Codex 是 OpenAI 的一套 AI 驱动的编码智能体，可自动完成软件工程任务，通常也是最早获得新模型的平台之一。有限预览意味着模型仅面向一小批经过审核的伙伴开放，之后才会更广泛地发布，以便 OpenAI 收集反馈并处理安全问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-gpt-5-6-sol-terra-luna-explained">What Is GPT-5.6? OpenAI's Sol, Terra, and Luna Model Tiers Explained | MindStudio</a></li>
<li><a href="https://www.reddit.com/r/codex/comments/1utzi5w/gpt56_sol_vs_terra_vs_luna_my_early_guide_to/">GPT-5.6 Sol vs Terra vs Luna: my early guide to choosing the right model without burning your limits : r/codex - Reddit</a></li>

</ul>
</details>

**社区讨论**: r/codex 上的早期讨论显示，Sol 明显很强但消耗 token 极快，Terra 占用的额度超出预期，一些用户甚至质疑 Terra 是否值得使用。整体情绪是谨慎关注，但对成本和速率限制消耗感到担忧。

**标签**: `#OpenAI`, `#GPT-5.6`, `#AI models`, `#API`, `#Codex`

---

<a id="item-14"></a>
## [ShinyHunters 声称入侵 FBI 并窃取员工及申请者数据](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) ⭐️ 8.0/10

黑客组织 ShinyHunters 声称已入侵多个与美国联邦调查局（FBI）相关的服务，窃取了所有 FBI 员工及求职申请者的数据，并向 404 Media 提供了一份约 5,000 名所谓 FBI 员工的样本。据称样本包含姓名、住址、电话号码以及配偶等家属信息，但 FBI 尚未确认这一说法。 如果数据属实，泄露信息可能被用于跟踪、骚扰甚至威胁 FBI 员工及其家属，并对美国执法和情报系统构成严重的安全与反情报风险。此事也凸显出即便是顶级政府机构也可能通过第三方企业软件被攻破，暴露出公共部门普遍存在的供应链安全漏洞。 据称约 5,000 条记录的样本包含个人及家属信息，被盗数据据称来自最初 PeopleSoft 被攻破后访问的系统，其中据称包括用于存储员工和申请者信息的 FBI AWS GovCloud 环境。FBI 尚未确认此次入侵，因此该说法仍未经证实。

telegram · zaihuapd · 9月23日 05:00

**背景**: ShinyHunters 是一个自 2019 年以来活跃的黑帽犯罪黑客与勒索组织，以大量数据泄露事件以及泄露或出售被盗数据库而闻名。404 Media 是一家独立科技新闻媒体，由前 Motherboard 记者于 2023 年创办。FBI 此前也曾遭遇黑客事件，包括 2021 年有人利用 FBI 邮箱地址发送虚假警告的邮件入侵事件，因此这类说法即便在官方确认前也会受到严肃对待。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ShinyHunters">ShinyHunters - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/404_Media">404 Media - Wikipedia</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/">ShinyHunters claims FBI hack, data theft in PeopleSoft zero-day breach</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#data breach`, `#FBI`, `#ShinyHunters`, `#national security`

---