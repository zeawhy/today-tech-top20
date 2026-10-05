---
layout: default
title: "Horizon Summary: 2026-10-05 (ZH)"
date: 2026-10-05
lang: zh
---

> 从 65 条内容中筛选出 11 条重要资讯。

---

1. [2026 年诺贝尔生理学或医学奖授予光遗传学发现](#item-1) ⭐️ 9.0/10
2. [vLLM v0.31.0 发布：优化 DeepSeek-V4.1-Flash 推理并引入快速重启权重缓存](#item-2) ⭐️ 8.0/10
3. [Reflection 发布 501B 开源权重 MoE 模型 Beam](#item-3) ⭐️ 8.0/10
4. [Anthropic 将佛罗里达女子在 Claude 中的日记报告给警方，引发重罪指控](#item-4) ⭐️ 8.0/10
5. [高通获授华为 LogicFolding 芯片专利许可，达成里程碑协议](#item-5) ⭐️ 8.0/10
6. [文章称现有技术已可根除蚊媒疾病](#item-6) ⭐️ 8.0/10
7. [OpenAI 将在欧盟为 ChatGPT 和 Codex 文本添加水印](#item-7) ⭐️ 8.0/10
8. [在 10 亿局面上蒸馏 Stockfish，3.9B 数据集已公开](#item-8) ⭐️ 8.0/10
9. [Yandex Music 的 Sona 用单个 Transformer 取代 15+ 推荐组件](#item-9) ⭐️ 8.0/10
10. [ARC-AGI-3 Kaggle 最高分 30 天内从 7%跃升至 56%](#item-10) ⭐️ 8.0/10
11. [Quad9 拒绝法国 DNS 封锁令，面临每日 58 万欧元罚款](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [2026 年诺贝尔生理学或医学奖授予光遗传学发现](https://www.nobelprize.org/all-nobel-prizes-2026/) ⭐️ 9.0/10

2026 年诺贝尔生理学或医学奖授予卡尔·戴瑟罗特、彼得·赫格曼和格奥尔格·纳格尔，以表彰他们发现光控离子通道并开创光遗传学。该技术可在活体大脑中开启或关闭单个神经细胞的活动，目前已被全球多地实验室用于脑科学研究。 光遗传学是神经科学领域的一次范式转变，使研究人员能够以前所未有的精度控制特定神经元，研究神经回路如何驱动行为、学习、记忆和疾病。此次获得诺贝尔奖凸显了该工具的巨大影响，它已经开始走向临床应用，例如帮助一名失明患者部分恢复视力。 光遗传学的原理是在目标细胞中表达光敏离子通道、泵或酶，从而利用光精确控制生化信号和神经元活动。除了控制单个细胞外，该技术还被用于绘制大脑功能连接图谱，以及研究决策、恐惧记忆、成瘾和进食等行为。

telegram · zaihuapd · 10月5日 09:33

**背景**: 光遗传学是一种利用光来操控神经元或其他细胞活动的生物技术。它依赖于光敏蛋白（如离子通道和离子泵），这些蛋白通过基因工程被导入目标细胞；当光照到这些细胞时，蛋白会改变细胞膜上的离子流动，从而激活或抑制该细胞。这种方法已成为系统神经科学的基础工具，使研究人员能够建立特定神经活动与行为之间的因果联系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Optogenetics">Optogenetics</a></li>
<li><a href="https://en.wikipedia.org/wiki/Karl_Deisseroth">Karl Deisseroth - Wikipedia</a></li>
<li><a href="https://www.downtoearth.org.in/health/2026-medicine-nobel-awarded-for-discoveries-concerning-light-gated-ion-channels-and-optogenetics">2026 Medicine Nobel Prize Honors Pioneers of Optogenetics and...</a></li>

</ul>
</details>

**标签**: `#optogenetics`, `#neuroscience`, `#Nobel Prize`, `#brain research`, `#light-controlled ion channels`

---

<a id="item-2"></a>
## [vLLM v0.31.0 发布：优化 DeepSeek-V4.1-Flash 推理并引入快速重启权重缓存](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) ⭐️ 8.0/10

vLLM 发布了 v0.31.0，这是一个包含 307 位贡献者（其中 96 位新贡献者）提交的 717 个 commit 的大型更新，带来了针对 DeepSeek-V4.1-Flash 的重大推理优化，例如采用 NVFP4 压缩 KV 缓存的 FlashMLA mega attention、DeepGEMM 稀疏 MQA logits 以及融合的 decoder 边界内核。该版本还引入了新的 `vllm preload` CLI，用于启动权重缓存守护进程，使量化后的权重在引擎重启期间常驻 GPU 显存，并提供了基于 CRIU 的实验性引擎快照功能。 vLLM 是使用最广泛的开源高吞吐 LLM 推理与服务引擎之一，因此这些优化会直接影响团队部署 DeepSeek-V4.1-Flash 等大模型时的效率与成本。快速重启权重缓存和快照功能有望大幅缩短生产环境中的冷启动和重启时间，这对自动扩缩容和可靠性都至关重要。 该版本包含多项破坏性变更：按请求传入的多模态 kwargs 现在需要 `--trust-request-mm-kwargs` 才能启用，`tokenizer_mode="slow"` 被移除，`--enable-mamba-fine-grained-prefix-cache` 重命名为 `--enable-mamba-shared-prefix-checkpoint`，通过 `quantization="fp8"` 进行的在线量化被 `fp8_per_tensor` 简写取代。此外还新增了 `--max-num-active-seqs` 和 `--long-prefill-token-threshold` 等调度控制项，并修复了前缀缓存键冲突和过期多模态缓存条目等安全问题。

github · khluu · 10月5日 06:44

**背景**: vLLM 是一个用于大语言模型推理与服务的开源框架，最初由加州大学伯克利分校 Sky Computing Lab 开发，核心是基于 PagedAttention 的 transformer 键值缓存内存管理方法。它支持连续批处理、分布式推理、量化以及兼容 OpenAI 的 API，因此常被用于生产环境的 LLM 服务。DeepSeek-V4.1-Flash 是 DeepSeek 近期推出的模型，基于 45T token 的多模态语料从零训练，采用稀疏注意力并将上下文扩展至 100 万 token，而 FlashMLA 则是 DeepSeek 的优化注意力内核库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLLM">VLLM</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek-V4.1-Flash">DeepSeek-V4.1-Flash</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/ FlashMLA : FlashMLA : Efficient Multi-head...</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#model serving`, `#performance optimization`, `#release`

---

<a id="item-3"></a>
## [Reflection 发布 501B 开源权重 MoE 模型 Beam](https://reflection.ai/blog/introducing-beam) ⭐️ 8.0/10

Reflection 发布了 Beam，这是一个开源权重的稀疏混合专家（MoE）模型，总参数量 5010 亿，激活参数 230 亿，面向编程、推理和智能体（agentic）任务。该模型在 23.8 万亿经过筛选的高质量 token 上完成预训练，并进一步通过强化学习进行调优，Reflection 声称其表现可匹配或超越同规模的开源基础模型。 Beam 为日益被中国实验室主导的开源大模型领域增添了又一个重量级竞争者，其发布也引发了关于西方开源模型是否跟得上步伐的讨论。对开发者和研究者而言，它提供了一个可自行部署和审查的高容量选项，适用于编程和智能体场景。 Beam 采用稀疏 MoE 设计，每个 token 仅激活 5010 亿参数中的 230 亿；根据社区对比，其预训练使用了 28 万亿 token。社区成员 wren6991 将其与 DeepSeek V4.1 Flash 对比，指出 Beam 的激活参数更多（230 亿，对比预填充 80 亿/解码 160 亿），但预训练 token 更少（28 万亿对比 45 万亿），且没有 N-gram/PLE 参数。

hackernews · Philpax · 10月5日 19:16 · [社区讨论](https://news.ycombinator.com/item?id=49969183)

**背景**: 混合专家（MoE）是一种将模型拆分为多个专门子网络（专家）的架构，通过路由器为每个输入只激活少数专家，因此总参数量可以非常大，而激活参数（以及每个 token 的计算量）保持较小。开源权重模型会公开训练好的参数供任何人下载和运行，与仅提供 API 的闭源模型不同。Beam 的 5010 亿/230 亿参数配置使其与 DeepSeek 等前沿开源 MoE 模型处于同一量级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://berges.ai/concepts/mixture-of-experts">What is a mixture-of-experts (MoE) model? Total vs active parameters</a></li>
<li><a href="https://vettedconsumer.com/mixture-of-experts-moe-explained-why-active-parameters-decide-what-runs-on-your-machine/">Mixture-of-Experts (MoE), Explained: Why “ Active Parameters ”...</a></li>

</ul>
</details>

**社区讨论**: 评论者欢迎又一个开源权重模型的发布，但对 Reflection 的泛化能力声明持怀疑态度，Ariarule 指出演示中声称在一个近期病毒式传播的谜题上达到 95.5% 的覆盖率。wren6991 提供了与 DeepSeek V4.1 Flash 的详细规格对比，而 NorwegianDude 认为西方开源模型仍落后于更小的免费中国模型，并希望出现更多竞争和像 Google Gemma 这样的提供方。

**标签**: `#open-weight models`, `#Mixture-of-Experts`, `#large language models`, `#AI research`, `#model release`

---

<a id="item-4"></a>
## [Anthropic 将佛罗里达女子在 Claude 中的日记报告给警方，引发重罪指控](https://www.techspot.com/news/114091-florida-woman-used-claude-diary-anthropic-reported-shoot.html) ⭐️ 8.0/10

佛罗里达州一名女子因使用 Anthropic 的 Claude 聊天机器人写下含有暴力威胁的日记内容，被 Anthropic 报告给警方，随后依据佛罗里达州法规 836.10 被控二级重罪。据 TechSpot 和 Cybernews 报道，这是已知最早由 AI 公司主动将用户对话分享给执法机构的案例之一。 此案引发了关于 AI 监控、用户隐私和言论自由的重大法律与伦理问题，并可能为 AI 公司如何处理潜在威胁内容树立先例。它影响到每一位 AI 聊天机器人用户，因为看似私密的对话可能被监控并报告给当局。 佛罗里达州法规 836.10 规定，发送、发布或传输威胁杀害或伤害他人、实施大规模枪击或恐怖主义的书面或电子记录属于二级重罪，且该通信必须以他人可能看到的方式进行。该女子向当局表示她把 Claude 当作日记使用，此案凸显了 AI 聊天机器人对话可能因严重威胁而被审查并分享给警方。

hackernews · emptybits · 10月5日 05:37 · [社区讨论](https://news.ycombinator.com/item?id=49961057)

**背景**: Anthropic 是一家 AI 安全与研究公司，利用 Constitutional AI 开发了 Claude 聊天机器人，使其安全、准确且可靠。与其他 AI 聊天服务一样，Claude 会收集用户数据，并可能对内容进行过滤或审核，但具体的监控和报告政策并不总是透明的。此事件延续了关于 AI 公司是否应报告表达暴力意图的用户的类似争论，一些批评者认为这等同于监控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybernews.com/ai-news/claude-diary-police/">Claude diary threat : Florida woman reported to police | Cybernews</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>
<li><a href="https://claude.com/">Claude</a></li>

</ul>
</details>

**社区讨论**: 评论者意见严重分歧：一些人认为阅读私人日记并起诉作者是违宪的监控行为，而另一些人则同情 Anthropic，指出不报告潜在枪手也会招致批评。许多人质疑向聊天机器人写日记在法律上是否构成佛罗里达州法律下的传播威胁，还有人建议运行本地开源模型以避免企业监控。

**标签**: `#AI ethics`, `#privacy`, `#surveillance`, `#free speech`, `#legal`

---

<a id="item-5"></a>
## [高通获授华为 LogicFolding 芯片专利许可，达成里程碑协议](https://www.bloomberg.com/news/articles/2026-10-05/qualcomm-licenses-patents-on-huawei-s-logicfolding-chip-tech) ⭐️ 8.0/10

2026 年 10 月 5 日，华为与高通宣布达成一项为期多年、范围广泛的专利交叉许可协议，涵盖 5G、计算、人工智能和网络等领域；高通同时获得华为 LogicFolding 芯片制造技术相关专利的许可，并将购买华为部分美国专利。华为表示，交易完成后其专利许可业务的累计预期合同价值预计超过 69 亿美元，交易尚待监管批准。 这标志着半导体知识产权格局的显著逆转：华为从西方技术的净被许可方，转变为向美国主要芯片厂商授权其芯片制造知识产权的提供方。此举可能重塑 5G 和人工智能领域的专利议价格局，并因华为被列入美国实体清单而具有重大地缘政治影响。 华为声称 LogicFolding 可提升芯片性能，有助于缩小与台积电等领先代工厂的差距，目标是在不使用 EUV 的情况下于 2031 年实现 1.4 纳米级密度；不过 3D 堆叠本身并非全新技术，且该交易仍需获得监管批准。作为协议的一部分，高通将购买华为部分美国专利。

hackernews · 0xedb · 10月5日 07:46 · [社区讨论](https://news.ycombinator.com/item?id=49961861)

**背景**: LogicFolding 是华为的芯片技术，通过堆叠多层晶圆，让信号在层间空间内以更短距离传输，而非横跨单颗芯片，华为称这可降低整体发热。该协议属于交叉许可，即双方互相获得对方专利组合的使用权；自 2021 年以来，华为的知识产权授权业务已实现正向收入。华为仍在美国实体清单上，美国企业与其某些交易受到限制，因此该协议的监管路径格外引人关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tipranks.com/news/qualcomm-stock-rises-after-huawei-logicfolding-chip-deal">Qualcomm Stock Rises after Huawei LogicFolding Chip Deal</a></li>
<li><a href="https://www.buildmvpfast.com/blog/huawei-logicfolding-tau-scaling-chip-breakthrough-2026">Huawei LogicFolding Tau Scaling Chip Breakthrough 2026</a></li>
<li><a href="https://moorinsightsstrategy.com/field-notes/huawei-qualcomms-historic-cross-license-agreement/">Huawei & Qualcomm ’s Historic Cross - License Agreement</a></li>

</ul>
</details>

**社区讨论**: 评论者争论华为是否已从过去的技术购买方转变为向高通收取净收入的一方；也有人质疑在高通受实体清单限制的情况下如何能达成此类协议。有人称赞 LogicFolding 是事后看来显而易见、却能降低发热的创新，还有人好奇爱立信会如何回应，或感叹 5G 领导权竞争格局的变化。

**标签**: `#semiconductors`, `#patents`, `#Huawei`, `#Qualcomm`, `#geopolitics`

---

<a id="item-6"></a>
## [文章称现有技术已可根除蚊媒疾病](https://worksinprogress.co/issue/mosquitoes-are-a-choice/) ⭐️ 8.0/10

《Works in Progress》的一篇文章指出，根除登革热和疟疾等蚊媒疾病的技术其实已经存在，不加以部署是一种主动选择，每年因此付出数百万人的生命代价。文章重点介绍了基因驱动和基于沃尔巴克氏体的方法等已可推广使用的工具。 蚊媒疾病每年导致数十万人死亡，且主要集中在热带地区，因此更广泛地部署这些技术可能挽救数百万人的生命并减轻巨大的经济负担。这场讨论还提出了关于有意改变野生昆虫种群的伦理和监管问题。 文章提到基因驱动技术，利用 CRISPR 将抗寄生虫基因在蚊群中传播，以及沃尔巴克氏体细菌，可降低蚊子传播登革热等病毒的能力。新加坡的沃尔巴克氏体 AlbB 菌株试验显示登革热风险降低了 72%，但监管和生态方面的担忧依然存在。

hackernews · benbreen · 10月4日 18:06 · [社区讨论](https://news.ycombinator.com/item?id=49956290)

**背景**: 基因驱动是一种遗传系统，能确保特定性状几乎被所有后代继承，从而使某种修改在野生种群中迅速传播。沃尔巴克氏体是一种常见细菌，引入蚊子体内后可阻止其传播登革热等病毒。这两种方法都旨在抑制或改造蚊群，而不仅仅依赖杀虫剂和蚊帐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geneconvenevi.org/articles/mosquito-gene-drives-and-the-malaria-eradication-agenda/">Mosquito Gene Drives and the Malaria Eradication Agenda</a></li>
<li><a href="https://www.worldmosquitoprogram.org/en/work/wolbachia-method/how-it-works">How WMP's Wolbachia method works | World Mosquito Program</a></li>
<li><a href="https://www.ocacademy.in/blogs/wolbachia-mosquito-dengue-control-singapore-trial/">Wolbachia mosquito dengue control : A 72% risk reduction</a></li>

</ul>
</details>

**社区讨论**: 评论者大多表示支持，有人称登革热“绝非小事”，还有人认为“没有理由不”部署这项技术。一些人提出了在流行地区自行使用的实际问题，另一些人则将这一情况与结核病相比较——尽管已有治愈方法，但人类的选择仍使该疾病持续存在。

**标签**: `#public health`, `#biotechnology`, `#genetic engineering`, `#mosquito-borne diseases`, `#global health`

---

<a id="item-7"></a>
## [OpenAI 将在欧盟为 ChatGPT 和 Codex 文本添加水印](https://techcrunch.com/2026/10/05/openai-will-start-watermarking-chatgpts-text-in-the-eu/) ⭐️ 8.0/10

OpenAI 宣布，为配合《欧盟人工智能法案》的内容透明要求，将在未来几周内为欧盟地区符合条件的 ChatGPT 和 Codex 文本输出加入机器可识别的隐形水印。API 用户也可为部分模型选择开启水印，但该功能默认关闭；同时 OpenAI 向研究人员和专业机构开放其文本水印检测器的申请使用。 这是主要 AI 供应商首批落实《欧盟人工智能法案》透明度义务的具体举措之一，可能为整个行业如何标记和检测 AI 生成文本树立事实标准。此举将影响欧盟用户、基于 OpenAI API 开发的开发者、依赖 AI 生成内容的企业，以及寻求可执行内容溯源机制的监管机构。 OpenAI 指出，对文本进行编辑会使隐形标记更难被检测到，这与文本水印已知的局限一致，例如内容被改写或翻译后检测器置信度会大幅下降。该水印仅适用于欧盟地区符合条件的输出，且 API 水印为可选开启而非默认启用。

rss · TechCrunch AI · 10月5日 20:36

**背景**: 《欧盟人工智能法案》第 50 条要求特定 AI 系统的提供者通过机器可读的标记方式，使 AI 生成或被操纵的内容可被检测识别，从而标明其为合成内容。文本水印的原理是在大语言模型生成的文本中嵌入隐藏的、可被统计检测的模式，检测器随后可将其识别出来。OpenAI 的 Codex 是其帮助开发者完成修复缺陷、重构代码等任务的编程智能体，因此对其加水印意味着透明度要求从聊天扩展到了代码生成领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.resemble.ai/resources/complete-guide-to-eu-ai-act-watermarking-requirements-for-generative-ai">Complete Guide to EU AI Act Watermarking Requirements for...</a></li>
<li><a href="https://vryse.co/blog/claude-ai-watermarking">Claude AI Watermarking : EU AI Act & Content Rules Explained</a></li>
<li><a href="https://ai.google.dev/responsible/docs/safeguards/synthid">SynthID: Tools for watermarking and detecting LLM- generated Text</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI Act`, `#watermarking`, `#AI regulation`, `#content provenance`

---

<a id="item-8"></a>
## [在 10 亿局面上蒸馏 Stockfish，3.9B 数据集已公开](https://www.reddit.com/r/MachineLearning/comments/1wxz5qq/distilling_stockfish_on_a_billion_positions_full/) ⭐️ 8.0/10

一位开发者使用 Gigafish 数据集中的 10 亿个局面，将 Stockfish 的价值函数蒸馏到一个 ResNet 与 ViT 结合的模型中，并在 Hugging Face 上公开了完整的 39 亿局面数据集。该数据集由 37 个月的 Lichess 对局构建而成，项目特意固定搜索深度，以用神经网络近似深度受限的搜索。 这项工作探索了学习到的函数能否比引擎本身更快地近似 Stockfish 的深度受限搜索，从而可能成为 NNUE 的有力替代方案。公开的 39 亿局面数据集也为国际象棋 AI 社区提供了一个大规模、可直接使用的资源，用于训练和评测评估模型。 作者发现纯视觉 Transformer 理解棋盘的速度非常慢，而 CNN 在训练初期凭借其固有的几何归纳偏置表现更好；将两者结合取得了最佳结果。固定搜索深度是一个刻意的设计选择，目的是让蒸馏出的价值函数近似每个局面下方的完整搜索树。

reddit · r/MachineLearning · /u/microscope1024 · 10月5日 04:11

**背景**: Stockfish 是一款顶尖的开源国际象棋引擎，负责评估局面并选择走法，自采用 NNUE（一种可高效更新的神经网络）以来，它使用一个小型神经网络进行评估。知识蒸馏是将大型或强模型（教师）的知识迁移到较小模型（学生）的过程，这里 Stockfish 充当教师。ResNet 是具有强空间归纳偏置的卷积网络，而视觉 Transformer 将图像作为图块序列处理，必须从数据中学习空间结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Efficiently_updatable_neural_network">Efficiently updatable neural network - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://genmind.ch/posts/ResNet-vs-ViT-Benchmark-Reality-Check/">I Benchmarked ResNet vs ViT on 50K Images. They're Nearly Identical.</a></li>

</ul>
</details>

**标签**: `#chess`, `#distillation`, `#neural-networks`, `#dataset`, `#stockfish`

---

<a id="item-9"></a>
## [Yandex Music 的 Sona 用单个 Transformer 取代 15+ 推荐组件](https://www.reddit.com/r/MachineLearning/comments/1wy4qxm/sona_one_transformer_replaced_our_15_candidate/) ⭐️ 8.0/10

Yandex Music 推出了 Sona，这是一个单一的生成式 Transformer，在智能音箱上的生产 A/B 测试中取代了 15 个以上的候选生成器、预排序器和排序器，相比对照组实现了 +4.53% 的活跃用户和 +6.30% 的总收听时长（p < 0.01）。该模型采用 History Compression 技术，将最多 8,192 个事件拆分为 6,144 个较早事件和 2,048 个近期事件，将推理成本大约减半，同时保留了全注意力的大部分质量。 这是一个罕见的生产环境验证案例，表明单个端到端生成式推荐器可以取代复杂的多阶段级联架构，有可能简化整个行业的推荐系统架构。如果该方法具有通用性，它可以降低大规模推荐系统的工程开销和推理成本。 Sona 最多读取 8,192 个事件，较早的 6,144 个和近期的 2,048 个块通过交叉注意力和一个全历史自注意力层交换信息，之后一个 7 层堆栈仅对近期的 2,048 个事件运行。解码器和排序模块共享同一个编码器输出，因此编码器每次请求只运行一次，但目录覆盖率低于生产堆栈，且该模型尚未全量上线。

reddit · r/MachineLearning · /u/SettingAccording8986 · 10月5日 10:07

**背景**: 传统的生产推荐系统采用多阶段级联：许多候选生成器检索物品，预排序器进行过滤，然后一个重型排序器使用数百个工程特征对幸存者打分。Transformer 最初为序列建模而设计，最近被改造成可以端到端生成推荐的生成式推荐器，但对长用户历史进行全注意力的计算成本很高，因为其成本随序列长度呈二次增长。History Compression 是一种实用的注意力效率技术，它让较早的事件保持可见，同时将昂贵的全注意力限制在较短的近期窗口内。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/10/05/yandex-introduces-sona-a-single-generative-recommender-that-replaces-entire-recommendation-cascade/">Yandex Introduces Sona: A Single Generative Recommender That...</a></li>
<li><a href="https://www.deeplearning.ai/the-batch/more-efficient-transformers">BigBird is an Efficient Attention Mechanism for Transformers</a></li>
<li><a href="https://mbrenndoerfer.com/writing/quadratic-attention-bottleneck-transformers-long-sequences">Quadratic Attention Bottleneck - Interactive</a></li>

</ul>
</details>

**标签**: `#recommender systems`, `#transformer`, `#efficient attention`, `#production ML`, `#A/B testing`

---

<a id="item-10"></a>
## [ARC-AGI-3 Kaggle 最高分 30 天内从 7%跃升至 56%](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 8.0/10

在过去 30 天里，ARC-AGI-3 Kaggle 竞赛的最高分从约 7%飙升至 56%，这些成绩由在严格算力限制下、运行于自定义 harness 中的小型本地模型取得。这意味着这些紧凑、可本地运行的系统如今在一个专门为展示人类优越性而设计的基准测试上，已经超过了普通人类的水平。 ARC-AGI-3 被设计为对灵活、类人推理能力的严苛测试，因此从接近零到超越普通人水平的快速跃升，表明交互式推理基准的饱和速度可能远超预期。这可能重塑 AI 社区衡量 AGI 进展的方式，并引发关于当前基准是否仍能有效区分人类与机器智能的质疑。 Kaggle 参赛者只能使用较小的本地模型，因此 56%这一数字反映的是在严格算力预算下的效率，而非单纯的规模优势。发帖者指出排行榜图片略有滞后，而且众所周知 ARC-AGI-3 的分数会因模型外挂的 harness 不同而大幅波动，这意味着 harness 工程是这些提升的主要因素。

reddit · r/MachineLearning · /u/we_are_mammals · 10月4日 10:24 · [社区讨论](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arcαgi3_scores_on_kaggle_just_went_from_7_to/)

**背景**: ARC-AGI-3 是 ARC Prize 推出的交互式推理基准，要求 AI 智能体探索全新环境、即时推断目标、构建可适应的世界模型，并通过动作-响应循环持续学习。与静态谜题基准不同，它不提供任何指令，智能体必须仅凭观察推断规则和目标，100%的分数意味着智能体能像人类一样高效地通关所有游戏。Kaggle 竞赛属于系统赛道，参赛者必须在严格算力限制下提交高效、专门构建的方法，而整个 ARC Prize 项目还设有 200 万美元的奖金池。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC - AGI - 3</a></li>
<li><a href="https://arcprize.org/leaderboard">ARC Prize - Leaderboard</a></li>
<li><a href="https://www.mindstudio.ai/blog/gpt6-astra-benchmarks-agi-claims">GPT-6 Astra Benchmarks : Do the Numbers Actually Mean AGI ?</a></li>

</ul>
</details>

**标签**: `#ARC-AGI`, `#AI benchmarks`, `#Kaggle`, `#AGI`, `#machine learning`

---

<a id="item-11"></a>
## [Quad9 拒绝法国 DNS 封锁令，面临每日 58 万欧元罚款](https://torrentfreak.com/dns-resolver-quad9-rejects-french-piracy-blocks-weighs-exit-as-bein-seeks-up-to-e580k-a-day/) ⭐️ 8.0/10

瑞士非营利 DNS 服务商 Quad9 拒绝执行法国法院要求其封锁 58 个盗版相关域名的命令，beIN Sports 正寻求对其处以每日最高 58 万欧元（每域名每日 1 万欧元）的罚款。巴黎法院上周四开庭审理此案，预计三周内作出裁决。 此案可能为各国强制 DNS 封锁如何适用于注重隐私的解析器树立全球先例，可能迫使 Quad9 退出法国市场或在全球范围内封锁域名。它凸显了国家版权执法与公共 DNS 服务无国界、以隐私为核心的架构之间日益加剧的紧张关系。 Quad9 表示其从未封锁任何域名，且由于不收集用户数据，无法仅针对法国用户进行地理定位封锁，只能选择全球封锁或退出法国市场。它还批评法国 7 月通过的可实时自动加黑域名的法律「鲁莽且危险」。

telegram · zaihuapd · 10月5日 08:05

**背景**: 像 Quad9 这样的 DNS 解析器将人类可读的域名转换为 IP 地址，在此层面进行封锁是常见的反盗版手段。Quad9 是一家瑞士非营利机构，强调隐私保护，不记录用户查询，这使得针对特定司法管辖区的选择性封锁在技术上难以实现。法国近期扩大了其盗版封锁制度，包括 7 月通过的一项允许对盗版体育流媒体进行自动化实时封锁的法律。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://torrentfreak.com/dns-resolver-quad9-rejects-french-piracy-blocks-weighs-exit-as-bein-seeks-up-to-e580k-a-day/">DNS Resolver Quad9 Rejects French Piracy Blocks ... * TorrentFreak</a></li>
<li><a href="https://quad9.net/">Quad9 | A public and free DNS service for a better security and privacy</a></li>
<li><a href="https://torrentfreak.com/wrong-logo-no-piracy-proof-french-court-rejects-dns-piracy-blocking-bids-250515/">Wrong Logo, No Piracy Proof: French Court Rejects DNS Piracy...</a></li>

</ul>
</details>

**标签**: `#DNS`, `#Internet Censorship`, `#Privacy`, `#Digital Rights`, `#France`

---