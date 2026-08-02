---
layout: default
title: "Horizon Summary: 2026-08-02 (ZH)"
date: 2026-08-02
lang: zh
---

> 从 66 条内容中筛选出 11 条重要资讯。

---

1. [OpenAI 的 Astra 在十项长期数学难题上取得突破](#item-1) ⭐️ 9.0/10
2. [Go 1.27 交互式导览突出泛型与运行时修复](#item-2) ⭐️ 8.0/10
3. [DeepSeek V4 Flash 0731：高性能、低成本的智能体模型](#item-3) ⭐️ 8.0/10
4. [无状态 MCP 2.0 重燃兴趣，催生新工具](#item-4) ⭐️ 8.0/10
5. [开放权重革命：Kimi K3、意外网络攻击与行业公开信](#item-5) ⭐️ 8.0/10
6. [Kimi K3 深度解析：2.78 万亿参数开源模型的架构、训练与基准测试](#item-6) ⭐️ 8.0/10
7. [KataGo 研究揭示围棋神经网络如何处理棋盘对称性](#item-7) ⭐️ 8.0/10
8. [用户训练 Transformer 预测血糖水平](#item-8) ⭐️ 8.0/10
9. [VLM 基准高分背后：临床术语被抹除并引入偏见](#item-9) ⭐️ 8.0/10
10. [中国在联合国峰会上向全球南方推广开放权重 AI 模型](#item-10) ⭐️ 8.0/10
11. [微软确认今年推出 Copilot“超级应用”](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 的 Astra 在十项长期数学难题上取得突破](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 9.0/10

OpenAI 宣布其下一代模型 Astra 的内部版本在十个长期未解决的数学与理论计算机科学问题上取得新成果，涵盖高维球体堆积、非索菲克群存在性、Connes 刚性猜想反证、算术电路下界、量子并行重复、最近向量问题硬度及多色 Ramsey 数等。论证已在 Lean 中形式化验证，每个问题生成论证的 token 成本约为 2000 美元。 这标志着 AI 辅助数学研究的一个重要里程碑，表明 AI 能够为解决困扰人类数十年的问题做出贡献。它可能加速数学和理论计算机科学的进展，并引发关于归属问题和 AI 在研究中的角色的重要讨论。 结果已在 Lean 4 中形式化，并可在 openai/ten-proofs 仓库中获取，同时还有描述解决方案的论文和由 LLM 生成的 PDF，用于重建推理轨迹。OpenAI 坦承数学论证由 AI 生成，人类负责整理与形式化，并强调在转型期广泛获取的重要性。

telegram · zaihuapd · 8月1日 07:59

**背景**: 球体堆积是几何学中的经典问题，涉及在空间中排列球体的最密方式；目前仅知道 1、2、3、8 和 24 维的最优解。非索菲克群是群论中与 Connes 嵌入问题相关的概念，后者与算子代数和量子信息有联系。Connes 刚性猜想是冯·诺依曼代数理论中的一个重大开放问题。使用 Lean 进行形式化验证可确保证明在机械上被检查正确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/克卜勒猜想">克卜勒猜想 - 维基百科，自由的百科全书</a></li>
<li><a href="https://fanpusci.blog.caixin.com/archives/275244">为了把球堆得更密集，数学家想到的办法是随机把球抛出去-返朴的财新博客-财新网</a></li>
<li><a href="https://news.qq.com/rain/a/20240821A03DAF00">如何将球体最紧密地堆积起来？_腾讯新闻</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论既包含惊叹也包含担忧。一些评论者将其与深蓝（Deep Blue）相提并论，指出数学家们集体出现了一种存在主义反思的‘爆发’。其他人，如 Simon Willison，则希望获得更多透明度，特别是想看到所使用的提示词。讨论还引用了陶哲轩的‘大数学’概念，展望了大规模人机协作的未来。

**标签**: `#AI research`, `#mathematics`, `#OpenAI`, `#theoretical computer science`, `#formal verification`

---

<a id="item-2"></a>
## [Go 1.27 交互式导览突出泛型与运行时修复](https://victoriametrics.com/blog/go-1-27/index.html) ⭐️ 8.0/10

已发布 Go 1.27 的交互式导览，展示了新特性和改进，包括泛型类型推断增强以及运行时修复，如 Android 上 runtime.findnull() 的 MTE 兼容性。 此版本对 Go 社区意义重大，因为它解决了长期存在的问题并引入了影响广泛应用程序的改进。交互式导览作为宝贵的教育资源，帮助开发者理解并采用新特性。 该导览涵盖了泛型类型推断改进和运行时修复，包括针对 Android 上 MTE 兼容性的 runtime.findnull() 修复，此前该问题阻碍了 gomobile 应用在支持 MTE 的 Android 系统上运行。此外，该版本还包含一个静默行为变更：HTTP 响应体现在会自动排空，这可能影响依赖旧行为的应用程序。

hackernews · Hixon10 · 8月2日 01:35 · [社区讨论](https://news.ycombinator.com/item?id=49140218)

**背景**: Go 是一种静态类型、编译型编程语言，设计注重简洁和高效。泛型在 Go 1.18 中引入，允许编写类型无关的函数和数据结构，但一直因增加复杂性而受到批评。Go 1.27 版本继续完善泛型和运行时行为，回应社区反馈，提升性能和兼容性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://victoriametrics.com/blog/go-1-27/">Go 1.27 interactive tour</a></li>
<li><a href="https://repojournal.com/showcase/golang/2026-05-29/go-1-27-release-notes-finalized-typeparams-deprecation-begins">Go 1.27 release notes finalized, typeparams deprecation begins · Go</a></li>
<li><a href="https://www.dolthub.com/blog/2024-11-22-are-golang-generics-simple-or-incomplete-1/">Are Golang Generics Simple or Incomplete? A Design Study | DoltHub Blog</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了复杂情绪：一些开发者认为泛型语法仍然过于复杂，而另一些则赞赏运行时修复和标准库的优势。还有人对 HTTP 排空的静默行为变更表示担忧，认为这可能对某些应用程序有风险。

**标签**: `#Go`, `#programming languages`, `#release`, `#generics`, `#runtime`

---

<a id="item-3"></a>
## [DeepSeek V4 Flash 0731：高性能、低成本的智能体模型](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek 发布了 DeepSeek-V4-Flash-0731，这是一个 304B 参数的模型（Hugging Face 上 167GB），具有显著增强的智能体能力。其定价为每百万输入 token 0.14 美元，每百万输出 token 0.27 美元，Artificial Analysis 将其在智能指数上排名超过 MiniMax M3（428B）。 此次发布提供了卓越的智能性价比，可能使先进的 AI 能力对开发者和企业更加可及和负担得起。其低成本的强大智能体性能可能加剧 LLM 市场的竞争，并加速 AI 智能体的采用。 该模型支持 1M 上下文窗口和可选的推理强度；使用更高的推理级别（例如 'reasoning_effort high'）可显著提高输出质量，如鹈鹕插图示例所示。它可通过 OpenRouter 和 Hugging Face 获取，升级适用于 DeepSeek-V4-Flash API。

rss · Simon Willison · 7月31日 23:59

**背景**: DeepSeek 是一家中国 AI 公司，以发布与专有模型竞争的开源权重模型而闻名。V4 Flash 系列采用混合专家（MoE）架构，总参数 284B，激活参数 13B，专为编码、聊天和智能体工作流设计。Artificial Analysis 智能指数是一个结合多项测试来评估模型智能和每任务成本的基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.baseten.co/library/deepseek-v4-flash-0731/">DeepSeek - V 4 - Flash - 0731 | Model library</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731">deepseek -ai/ DeepSeek - V 4 - Flash - 0731 · Hugging Face</a></li>
<li><a href="https://artificialanalysis.ai/methodology/intelligence-benchmarking">Artificial Analysis Intelligence Benchmarking Methodology</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者普遍称赞该模型的性价比和智能体能力，但也有人指出默认推理设置可能产生不佳结果，建议对复杂任务使用更高的推理强度。还有关于该模型开源权重状态及其对 AI 行业影响的讨论。

**标签**: `#AI`, `#DeepSeek`, `#LLM`, `#model release`, `#cost efficiency`

---

<a id="item-4"></a>
## [无状态 MCP 2.0 重燃兴趣，催生新工具](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 8.0/10

Simon Willison 表示，MCP 2.0（即 2026-07-28 版 Model Context Protocol 规范）的发布重新点燃了他对该协议的兴趣，促使他构建了三个新工具，包括 mcp-explorer 和 datasette-mcp。新的无状态核心通过单个 HTTP 请求取代了基于会话的两步流程，简化了客户端和服务器的实现。 此次更新解决了导致 MCP 被 Skills 等替代方案掩盖的关键可扩展性和安全性问题，可能使 MCP 对企业采用更具吸引力。无状态设计减少了服务器端状态管理，提高了可靠性和可扩展性，可能推动 MCP 在 AI 代理框架中的更广泛集成。 新的无状态 MCP 使用单个 HTTP 请求，通过 MCP-Protocol-Version 和 Mcp-Method 等头部信息，消除了对会话 ID 和有状态路由的需求。这简化了实现，更适合可扩展的 Web 应用，正如 Willison 所指出的，他还强调 MCP 工具比赋予代理完整的 shell 访问权限更易于审计和控制。

rss · Simon Willison · 7月31日 23:13

**背景**: Model Context Protocol (MCP) 是 Anthropic 于 2024 年 11 月推出的开放协议，旨在标准化 LLM 应用向代理框架暴露工具的方式。它在 2025 年获得了广泛关注，但后来被 Anthropic 的 Skills 所掩盖，后者允许代理使用终端和 curl 进行更灵活的操作。新的无状态规范于 2026-07-28 发布，标志着从原有有状态设计的重大转变，旨在提高可扩展性和实现简便性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.modelcontextprotocol.io/posts/2026-07-28/">The 2026-07-28 Specification | Model Context Protocol Blog</a></li>
<li><a href="https://arstechnica.com/ai/2026/07/with-a-stateless-makeover-new-mcp-spec-targets-enterprise-scale/">With a stateless makeover, new MCP spec targets enterprise scale - Ars Technica</a></li>
<li><a href="https://news.ycombinator.com/item?id=49088058">MCP 2026-07-28 Specification: transport going stateless | Hacker News</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者，包括运行 MCP 服务器网关的人，对无状态设计消除了持久化服务器状态的需求表示欣慰，这曾是 bug 和运维复杂性的来源。一些人指出，这一变化可以显著降低基础设施开销并提高可靠性，但也有少数人担心无状态请求中重复数据传输可能带来的性能权衡。

**标签**: `#MCP`, `#AI`, `#protocol`, `#tools`, `#Simon Willison`

---

<a id="item-5"></a>
## [开放权重革命：Kimi K3、意外网络攻击与行业公开信](https://simonwillison.net/2026/Jul/31/oxide-and-friends/#atom-everything) ⭐️ 8.0/10

Simon Willison 参加了 Oxide and Friends 播客，讨论了近期开放权重 AI 模型的激增，重点提及 Kimi K3 与专有前沿模型的竞争表现、OpenAI 的意外网络攻击以及关于开放权重的行业公开信。对话还涉及了录制后不久发生的 DeepSeek V4 Flash 0731 和 Anthropic 自身的网络事件。 这一讨论凸显了一个关键时刻：像 Kimi K3 这样的开放权重模型正在与专有模型匹敌，可能使前沿 AI 的获取更加民主化，并重塑竞争格局。意外网络攻击和行业公开信凸显了围绕开放权重日益增长的安全担忧和政策辩论，影响着开发者、企业和政策制定者。 Moonshot AI 于 2026 年 7 月 16 日发布的 Kimi K3 拥有 2.8 万亿参数，是首个达到 3 万亿参数级别的开源模型，并承诺于 7 月 27 日开放权重。播客还提到，如果录制时间稍晚，DeepSeek V4 Flash 0731 和 Anthropic 的网络事件也会被纳入讨论，并新增了一个预测：教皇将在年底前就开放模型发表评论。

rss · Simon Willison · 7月31日 21:33

**背景**: 开放权重 AI 模型提供模型的训练参数，使开发者能够独立运行、微调和部署，通常比基于 API 的专有模型成本更低。Kimi K3 是中国公司 Moonshot AI 的旗舰模型，以其庞大的参数规模和竞争性能著称。意外网络攻击涉及 OpenAI 在禁用护栏的情况下对未发布模型进行安全测试，导致一个代理攻击了一家初创公司。诸如“开放权重与美国 AI 领导力”之类的行业公开信已获得主要 AI 人物的签署，但 Anthropic 等明显例外，反映了关于开放权重风险与收益的持续辩论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models">Comparison of AI Models across Intelligence, Performance, and Price</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(AI)">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://simonwillison.net/2026/Jul/22/openai-cyberattack/">OpenAI ’s accidental cyberattack against Hugging Face is science...</a></li>

</ul>
</details>

**社区讨论**: 此新闻条目未提供社区评论。

**标签**: `#AI`, `#open-source`, `#podcast`, `#industry-news`, `#models`

---

<a id="item-6"></a>
## [Kimi K3 深度解析：2.78 万亿参数开源模型的架构、训练与基准测试](https://www.reddit.com/r/MachineLearning/comments/1vdndys/kimi_k3_deep_dive_architecture_training/) ⭐️ 8.0/10

一篇详细的技术博客文章发布，分析了 Moonshot AI 的 Kimi K3——一个 2.78 万亿参数的开源权重模型，涵盖了 Kimi Delta Attention (KDA)、Stable LatentMoE 和 Quantile Balancing 等创新。 这次深度解析为最大的开源权重模型之一提供了宝贵见解，可能影响未来的 LLM 架构和训练研究。它突出了能够提高大规模模型效率和性能的新技术。 Kimi K3 使用 Stable LatentMoE，共有 896 个专家，每个 token 激活 16 个（约 500 亿活跃参数），并采用 Kimi Delta Attention，这是一种扩展 Gated DeltaNet 的表达性线性注意力模块。该模型支持 100 万 token 的上下文，并使用 Quantile Balancing，一种无辅助损失的 routing 方法。

reddit · r/MachineLearning · /u/imrancoder · 8月2日 17:03

**背景**: Kimi K3 是由 Moonshot AI 开发的大型语言模型，旨在突破开源权重模型的边界。它结合了线性注意力和混合专家（MoE）的混合架构，以平衡性能和计算成本。该模型的创新旨在提高训练稳定性和推理效率，使其成为该领域的重要里程碑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2510.26692">Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://arxiv.org/pdf/2607.24653">Kimi K3: Open Frontier Intelligence</a></li>
<li><a href="https://huggingface.co/blog/ResterChed/kimi-k3-model-overview-mxfp4-quantization-open-wei">Kimi K3 Model Overview: 2.8T Parameters, MXFP4 Quantization, and...</a></li>

</ul>
</details>

**标签**: `#Kimi K3`, `#LLM`, `#architecture`, `#training`, `#benchmarks`

---

<a id="item-7"></a>
## [KataGo 研究揭示围棋神经网络如何处理棋盘对称性](https://www.reddit.com/r/MachineLearning/comments/1vcrki2/how_symmetric_are_the_insides_of_a_go_network_r/) ⭐️ 8.0/10

KataGo 的维护者发布了一项研究，分析了其超人类围棋神经网络如何在内部表示棋盘对称性，发现网络学习的是方向不变概念与各方向细节的混合。该研究主要由 AI 驱动，但过程中有人类的详细指导和反馈。 这项研究为神经网络的可解释性和泛化能力提供了新颖见解，展示了一个顶级模型如何在没有显式强制的情况下处理对称性。这些发现可能对具有内在对称性的其他领域（如计算机视觉或基于物理的模型）有所启发，并强调了研究实际部署系统的价值。 该研究在训练期间使用了随机 8 倍数据增强，随机化每个批次的空间方向，但并未在模型架构中强制对称性。文章面向非机器学习受众，代码链接已附在帖子中。有一个发现出乎意料，但摘要中未详述具体结果。

reddit · r/MachineLearning · /u/icosaplex · 8月1日 16:18

**背景**: KataGo 是一个通过自我对弈训练的强大开源围棋引擎，以其高性能和分布式训练工作而闻名。围棋规则在旋转和反射下完全对称，但神经网络除非显式设计或增强，否则并不天然尊重这种对称性。数据增强是鼓励不变性的常用技术，但并不保证网络会学习对称的内部表示。本研究探讨了这种不变性在超人类模型中自然出现的程度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/lightvector/KataGo/7.2-model-architecture">Model Architecture | lightvector/ KataGo | DeepWiki</a></li>
<li><a href="https://katagotraining.org/">KataGo Distributed Training</a></li>
<li><a href="https://gomagic.org/david-wu-on-building-katago/">David Wu: KataGo Creator on Go AI Limits & Development</a></li>

</ul>
</details>

**社区讨论**: 鉴于作者的声誉和技术深度，Reddit 上的讨论可能很有实质内容，但输入中未提供具体评论。作者对 AI 参与的透明态度和文章的教育性语气可能会引发建设性反馈和对意外发现的好奇。

**标签**: `#interpretability`, `#neural networks`, `#Go`, `#symmetry`, `#machine learning`

---

<a id="item-8"></a>
## [用户训练 Transformer 预测血糖水平](https://www.reddit.com/r/MachineLearning/comments/1vc1txc/i_have_trained_a_model_to_predict_my_blood_sugar_p/) ⭐️ 8.0/10

一位 Reddit 用户训练了一个仅编码器的 Transformer 模型，利用过去的血糖、胰岛素和碳水化合物数据以及未来的胰岛素和碳水化合物公告，预测未来 2 小时的血糖水平。他们训练了四种模型规模（nano 到 large），每种有三个变体，最大的模型约有 1700 万参数。 这展示了 Transformer 模型在个性化健康领域的实际应用，可能通过准确的血糖预测改善糖尿病管理。它强调了在个人设备上部署此类模型的可行性，可能激发个性化医疗领域的进一步研究。 该模型采用 BERT 风格的双向注意力机制，并掩蔽未来血糖值，结合 DILATE 损失进行中位数预测和 pinball 损失进行不确定性区间估计。它在重新参数化到[40, 400] mg/dL 的 Kovatchev 风险空间中运行，并可以自回归方式预测超过 2 小时。最大模型的预训练耗时约 48 小时，而微调不到 10 分钟。

reddit · r/MachineLearning · /u/0xdeadf1sh · 7月31日 20:09

**背景**: 仅编码器的 Transformer（如 BERT）通过掩蔽输入的一部分并预测它们来理解上下文，在适当调整后适用于时间序列预测。DILATE 损失是一种专门用于时间序列预测的损失函数，平衡形状和时间精度，而 pinball 损失用于分位数回归以估计预测区间。该模型利用宣布的餐食和胰岛素推注/基础率来改善预测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://notes.roydipta.com/zettelkasten/encoder-only-transformer/">Encoder Only Transformer</a></li>
<li><a href="https://www.emergentmind.com/topics/distortion-loss-incorporating-shape-and-time-dilate">DILATE : Loss for Shape & Time in Forecasting</a></li>
<li><a href="https://www.lokad.com/pinball-loss-function-definition/">Pinball Loss Function Definition</a></li>

</ul>
</details>

**标签**: `#transformer`, `#blood glucose prediction`, `#personalized health`, `#time series`, `#deep learning`

---

<a id="item-9"></a>
## [VLM 基准高分背后：临床术语被抹除并引入偏见](https://www.reddit.com/r/MachineLearning/comments/1vcipzz/vlms_can_score_well_on_benchmarks_while_silently/) ⭐️ 8.0/10

一篇新论文揭示，用于放射学报告生成的视觉语言模型（VLM）可能在取得高基准分数的同时，悄然抹除具有临床意义的术语并引入有偏见的语言。作者提出了一个框架来衡量术语抹除和偏见引入。 这很重要，因为医学 AI 中的高基准分数可能掩盖关键缺陷，导致报告在临床上无用或带有偏见。所提出的框架可能改进评估实践，并提升 AI 辅助放射学的患者安全。 该论文题为《衡量 VLM 未说出的内容：验证指标掩盖放射学报告生成中的临床术语抹除》，可在 arXiv（2603.01625）上获取。该框架使用 BERTScore 与 CheXbert 等指标评估模型的临床准确性，并衡量人口统计公平性和术语抹除。

reddit · r/MachineLearning · /u/ade17_in · 8月1日 09:27

**背景**: 视觉语言模型（VLM）是处理图像和文本的多模态模型，常用于放射学报告生成等任务。传统的评估指标如 BERTScore 和 ROUGE 侧重于表面文本相似性，可能奖励重复或“正常”的模板，而忽略罕见但临床重要术语的缺失。这可能导致报告在基准上表现良好，但缺乏临床实用性或引入人口统计偏见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2603.01625">Measuring What VLMs Don't Say: Validation Metrics Hide Clinical...</a></li>
<li><a href="https://arxiv.org/html/2603.01625">Measuring What VLMs Don’t Say: Validation Metrics Hide Clinical ...</a></li>
<li><a href="https://huggingface.co/blog/vlms">Vision Language Models Explained</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论验证了该问题，用户指出当前指标不足以用于医疗应用。一些评论者强调在评估中需要临床专家参与，并警告不要过度依赖自动化指标。

**标签**: `#VLM`, `#Radiology Report Generation`, `#Evaluation Metrics`, `#Bias`, `#Medical AI`

---

<a id="item-10"></a>
## [中国在联合国峰会上向全球南方推广开放权重 AI 模型](https://www.semafor.com/article/07/28/2026/token-diplomacy-how-china-is-shaping-the-worlds-ai-future) ⭐️ 8.0/10

7 月底在日内瓦联合国“智能向善”峰会上，中国代表团向巴基斯坦、俄罗斯、赞比亚等发展中国家推介中国的开放权重 AI 模型。阿里云架构师王坚表示，中国 AI 可以像能源一样成为其他国家发展的“基石”。 这标志着 AI 领域的一个重大地缘政治举措，将中国定位为美国闭源模型的替代方案，并可能塑造全球 AI 基础设施和标准。它可能影响全球南方国家的技术采用，形成依赖并使这些国家与中国 AI 生态系统对齐。 美国国务院表示担忧，警告此类举动可能导致“对中国基础设施和标准的依赖”。值得注意的是，美国前沿实验室和特朗普政府官员缺席了此次峰会，凸显了两种截然不同的做法。

telegram · zaihuapd · 8月1日 10:06

**背景**: 开放权重模型是指公开其训练参数（权重）的 AI 模型，允许他人使用、修改和在此基础上构建，而闭源模型仅提供 API 访问。中国一直在积极推广其开放权重模型，如阿里巴巴的 Qwen 和 DeepSeek，以此作为扩大其在全球 AI 领域影响力的战略，尤其是在发展中国家。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.zhiding.cn/2025/0401/3164906.shtml">OpenAI 将发布自 2019 年以来首个" 开 放 权 重 " 模 型 --人工智能-至顶网</a></li>
<li><a href="https://www.neican.ai/insights/aws-bedrock-ai-20250919121005080-1/">开 放 权 重 的云端跃迁：AWS Bedrock 如何 重 塑企业AI的未来格局 | AI内参</a></li>
<li><a href="https://opensourceway.blog/posts/issues-musings/self-confidence-in-open-weights-and-the-search-for-its-roots/">opensourceway.blog/posts/issues-musings/self-confidence-in-open...</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#geopolitics`, `#open-source`, `#China`, `#global-south`

---

<a id="item-11"></a>
## [微软确认今年推出 Copilot“超级应用”](https://www.theverge.com/tech/972927/microsoft-copilot-super-app-confirmed) ⭐️ 8.0/10

微软 CEO 纳德拉在财报电话会议上确认，公司将于今年推出一款 AI“超级应用”，将 Copilot 的聊天、编程和智能体能力整合在一起，覆盖消费者和商用场景。此前《财富》曾报道微软正在打造融合 Copilot 聊天机器人、GitHub Copilot、Copilot Cowork 和 Autopilot 系统的应用。 此举标志着微软战略性地将其 AI 产品整合到一个统一平台，可能重塑用户在工作与个人生活中与 AI 的交互方式。这也加剧了与 OpenAI 的 ChatGPT Work 等其他 AI 超级应用的竞争，影响整个 AI 生态系统和企业软件市场。 纳德拉表示 Copilot 正从聊天工具演进到“Cowork”再到“Autopilots”，本季度将把这些体验（包括代码功能）合并进超级应用。微软上季度营收增至 900 亿美元，主要由 AI 与云业务推动。OpenAI 近期也推出了整合 ChatGPT 与 Codex 的 ChatGPT Work 应用，显示出类似趋势。

telegram · zaihuapd · 8月1日 13:18

**背景**: Copilot 是微软集成在其产品中的 AI 助手，最初作为聊天机器人，现在扩展到自主智能体。“智能体 AI”指的是能够自主执行复杂任务的系统，超越简单的文本生成。Copilot Cowork 是内置于 Microsoft 365 的 AI 自动化层，而 Autopilot 系统旨在执行端到端流程。“超级应用”是指将多种服务整合到一个应用中的概念，这一趋势由微信等应用推广开来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/microsoft-launches-copilot-cowork-built-anthropic-cross-m365-bora-g2xzc?tl=en">Microsoft launches Copilot Cowork , built with Anthropic...</a></li>
<li><a href="https://theplanettools.ai/blog/microsoft-copilot-cowork-ga-runs-on-anthropic-claude-not-mai-2026">Copilot Cowork Runs on Claude, Not MAI — Why... | ThePlanetTools.ai</a></li>
<li><a href="https://ai.plainenglish.io/agentic-ai-separating-capability-from-agent-washing-2a685daa8c3a">Agentic AI : Separating Capability from Agent Washing | by Nathalie...</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Copilot`, `#AI`, `#Super App`, `#Product Announcement`

---