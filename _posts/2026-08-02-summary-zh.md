---
layout: default
title: "Horizon Summary: 2026-08-02 (ZH)"
date: 2026-08-02
lang: zh
---

> 从 78 条内容中筛选出 12 条重要资讯。

---

1. [OpenAI Astra 在十项长期数学难题上取得突破](#item-1) ⭐️ 9.0/10
2. [字节跳动发布 Seedance 2.5 视频生成模型，具备先进引用功能](#item-2) ⭐️ 8.0/10
3. [谷歌在 RSS 衰落中的角色：历史分析](#item-3) ⭐️ 8.0/10
4. [Ripgrep musl 二进制在大规模搜索时段错误，疑为内核问题](#item-4) ⭐️ 8.0/10
5. [DeepSeek V4-Flash-0731：性价比最高的智能模型](#item-5) ⭐️ 8.0/10
6. [无状态 MCP 重燃兴趣，催生新工具](#item-6) ⭐️ 8.0/10
7. [Reddit 用户训练 Transformer 预测血糖](#item-7) ⭐️ 8.0/10
8. [KataGo 研究揭示围棋神经网络中的对称性学习](#item-8) ⭐️ 8.0/10
9. [VLM 基准高分却抹除临床术语并引入偏见](#item-9) ⭐️ 8.0/10
10. [EA 以 550 亿美元被沙特财团收购，交易将于 8 月 4 日完成](#item-10) ⭐️ 8.0/10
11. [中国在联合国峰会上向全球南方推广开放权重 AI 模型](#item-11) ⭐️ 8.0/10
12. [微软确认今年推出 Copilot“超级应用”](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Astra 在十项长期数学难题上取得突破](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 9.0/10

OpenAI 宣布其下一代模型 Astra 的内部版本在十个长期未解决的数学与理论计算机科学问题上取得了新成果，涵盖高维球体堆积、非索菲克群的存在性、Connes 刚性猜想的反例、算术电路下界、量子并行重复、最近向量问题的硬度以及多色 Ramsey 数等。这些证明已在 Lean 中形式化验证，每个问题的 token 成本约为 2000 美元。 这标志着 AI 驱动数学研究的一个重要里程碑，表明 AI 能够为解决困扰人类数十年的问题做出贡献。它可能加速数学和理论计算机科学的进展，并引发关于归属问题和 AI 在研究中的角色的重要讨论。 这些证明由人类与模型协作整理成论文，并在 Lean 4 中形式化验证，代码可在 openai/ten-proofs 仓库中获取。OpenAI 坦承数学论证由 AI 生成，人类负责整理与形式化，并强调在这一转型期广泛获取的重要性。

telegram · zaihuapd · 8月1日 07:59

**背景**: 所涉及的问题包括高维球体堆积，即寻找 n 维空间中球体的最密排列，以及非索菲克群的存在性，这是 Mikhail Gromov 于 1999 年提出的问题。Connes 刚性猜想涉及某些群是否由其冯·诺依曼代数唯一确定。这些都是数学和理论计算机科学中深奥且长期未解决的开放问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/984/557.htm">均为 10 年以上未解难题：OpenAI...</a></li>
<li><a href="https://www.zhihu.com/question/2066932562694611664">如何评价OpenAI证明Non-Sofic群的存在这个菲奖级成果？是否意味着以数...</a></li>
<li><a href="https://blog.csdn.net/daqianai/article/details/150998305">接吻数 问 题 ：从 球 体 堆 叠到 高 维 空间的数学奥秘-CSDN博客</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论中既有惊叹也有担忧。一些评论者将其与深蓝对国际象棋的影响相提并论，而另一些人则提到数学家们正经历一种“深刻的精神危机”，正如 Kirwin Hampshire 的文章所述。此外，人们也对所使用的提示词感到好奇，并对未提及失败尝试的信息持怀疑态度。

**标签**: `#AI`, `#mathematics`, `#OpenAI`, `#theoretical computer science`, `#formal verification`

---

<a id="item-2"></a>
## [字节跳动发布 Seedance 2.5 视频生成模型，具备先进引用功能](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) ⭐️ 8.0/10

字节跳动发布了其视频生成模型的最新版本 Seedance 2.5，能够单次生成长达 30 秒的高质量片段。该模型支持多模态引用，包括多达 30 张图片、10 个视频和 10 个音频参考，并具备精确的时间戳编辑和同步音频功能。 此次发布标志着 AI 视频生成的重大进步，为电影制作人和创作者提供了前所未有的控制力和质量。该模型对动作和高特效镜头的关注反映了其与中国市场需求的一致性，可能影响全球创意工作流程和竞争格局。 Seedance 2.5 支持多轮视频扩展和黏土渲染控制，允许迭代优化。它还支持自然语言控制和多种参考类型的无缝集成，但社区成员指出其相对缺乏对对话驱动场景的关注。

hackernews · njaremko · 8月1日 20:45 · [社区讨论](https://news.ycombinator.com/item?id=49138302)

**背景**: 字节跳动的 Seedance 系列是一系列 AI 视频生成模型，可将文本和图像输入转换为电影级视频。第一版 Seedance 1.0 已提供 1080p 输出，具有流畅运动和物理真实感。Seedance 2.5 在此基础上增强了引用功能和更长的生成能力，使字节跳动成为竞争激烈的 AI 视频生成市场中的关键参与者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.seedance.tv/seedance-2-5">Seedance 2.5 AI Video Generator — 30s 4K Model Guide</a></li>
<li><a href="https://seeddance.ai/seedance-2-5">Seedance 2.5 — 30s One-Take AI Video with Multimodal ...</a></li>
<li><a href="https://technode.com/2026/07/31/bytedance-launches-seedance-2-5-video-generation-model/">ByteDance launches Seedance 2.5 video-generation model · TechNode</a></li>

</ul>
</details>

**社区讨论**: 社区成员对视频质量印象深刻，有人称这是第一个真正让他们印象深刻的 AI 视频生成。然而，也有人指出该模型更注重动作而非对话，并且存在角色说话后不自然停顿的怪癖。还有人将其与即将推出的开源权重模型如 MiniMax H3 进行比较，后者可能可以在消费级 GPU 上运行。

**标签**: `#AI video generation`, `#ByteDance`, `#Seedance`, `#machine learning`, `#creative tools`

---

<a id="item-3"></a>
## [谷歌在 RSS 衰落中的角色：历史分析](https://openrss.org/blog/how-google-helped-destroy-adoption-of-rss-feeds) ⭐️ 8.0/10

一篇 2023 年发表的文章认为，谷歌的行为，尤其是 2013 年关闭 Google Reader，对 RSS 采用的下降起到了重要作用。这篇文章在 Hacker News 上引发了热烈讨论，获得 401 分和 141 条评论。 这一分析凸显了互联网中心化的更广泛趋势，以及从 RSS 等开放标准向围墙花园的转变。对于关注开放网络健康以及少数科技巨头权力集中的开发者、内容创作者和互联网历史学家来说，这很重要。 文章特别批评了谷歌以“使用率下降”为由关闭 Google Reader，许多人认为这一理由不诚实，因为当时谷歌正在推广 Google+。文章还指出，RSS 在开放网络倡议中仍被广泛使用，支持 RSS 的资源成本极低，Shopify 等平台就是例证。

hackernews · pudgywalsh · 8月1日 18:07 · [社区讨论](https://news.ycombinator.com/item?id=49136821)

**背景**: RSS（简易信息聚合）是一种网络订阅格式，允许用户订阅网站的内容更新。Google Reader 于 2005 年推出，是一款流行的基于网页的 RSS 聚合器，帮助 RSS 成为主流。2013 年其关闭常被视为一个转折点，此后随着社交媒体平台成为主要内容发现工具，RSS 的使用量下降。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Google_Reader">Google Reader — Grokipedia</a></li>
<li><a href="https://modernorange.io/item/39493770">Google helped destroy adoption of RSS feeds (2023) | Modern Orange</a></li>
<li><a href="https://robinrendle.com/notes/rise-and-demise-of-rss/">The Rise and Demise of RSS • Robin Rendle</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对早期互联网的怀念和对谷歌决定的不满，有人称“使用率下降”的借口是假的。其他人则认为中心化网络无论如何都会占据主导地位，而一些人强调 RSS 仍然存在，并鼓励支持它，指出在 Rails 等框架中添加 RSS 订阅很容易。

**标签**: `#RSS`, `#Google`, `#Open Web`, `#Internet History`, `#Centralization`

---

<a id="item-4"></a>
## [Ripgrep musl 二进制在大规模搜索时段错误，疑为内核问题](https://github.com/BurntSushi/ripgrep/issues/3494) ⭐️ 8.0/10

为 x86_64-unknown-linux-musl 构建的 ripgrep 15.2.0 在高并发搜索非常大的目录树时偶尔会因 SIGSEGV 崩溃。崩溃发生在 opendir 调用的 calloc 中，原因是 musl 的 mallocng 分配器中的堆完整性断言失败。 该问题影响广泛使用的命令行工具，并凸显了 musl 默认分配器在多线程工作负载下的深层问题。同时，它暗示可能存在内核缺陷，这对 Linux 上的系统编程和性能具有更广泛的影响。 崩溃是 mallocng 中的完整性断言，由 opendir 的 calloc 调用触发。该问题时有时无，且仅出现在 musl 二进制中，glibc 未受影响。社区分析认为根本原因可能是与内存映射行为相关的内核缺陷。

hackernews · throwaway2037 · 8月1日 12:34 · [社区讨论](https://news.ycombinator.com/item?id=49133889)

**背景**: Ripgrep 是一个快速的递归 grep 工具，使用 Rust 编写，并支持与 musl 静态链接以生成可移植的二进制文件。musl 的默认分配器 mallocng 已知在多线程下存在性能问题，而此缺陷可能因内核交互而加剧。该问题引发了关于分配器选择和内核行为的讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/BurntSushi/ripgrep/issues/3494">x86_64-unknown-linux- musl binaries occasionally segfault during...</a></li>
<li><a href="https://elsolitario.org/en/2026/08/01/ripgrep-musl-segfault-mallocng-heap-en/">Musl Segfault : mallocng Bug Hits Ripgrep 15.2</a></li>
<li><a href="https://sourcefeed.dev/a/that-ripgrep-segfault-is-probably-a-kernel-bug">That ripgrep Segfault Is Probably a Kernel Bug — SourceFeed</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，问题中引用的内核补丁表明该缺陷可能是内核问题，而非 ripgrep 的缺陷。一些用户质疑 ripgrep 为何不更换 musl 的默认分配器，因为其注重速度。还有人建议不要在 HPC 集群文件系统上运行 ripgrep，因为会产生大量小 I/O 开销。

**标签**: `#ripgrep`, `#musl`, `#segfault`, `#allocator`, `#performance`

---

<a id="item-5"></a>
## [DeepSeek V4-Flash-0731：性价比最高的智能模型](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek 发布了 V4-Flash-0731，这是一个拥有 3040 亿参数的模型，智能体能力大幅增强。其定价为每百万输入 token 0.14 美元，每百万输出 token 0.27 美元，Artificial Analysis 将其排在更大的 MiniMax M3 模型之前。 该模型在单位智能上提供了卓越的性价比，可能成为对成本敏感的 AI 应用的首选。其强大的智能体性能可能加速 AI 智能体在生产环境中的采用，加剧模型提供商之间的竞争。 该模型在 Hugging Face 上大小为 167GB，支持可配置的推理强度；Simon Willison 发现默认推理级别效果不佳，但将 reasoning_effort 设为 high 后输出质量大幅提升。它在简单智能体任务上表现与 V4-Pro 相当，并在编程基准测试中取得顶尖成绩。

rss · Simon Willison · 7月31日 23:59

**背景**: DeepSeek 是一家中国 AI 公司，以低成本发布具有竞争力的开放权重模型而闻名。Artificial Analysis 智能指数是一个综合基准，衡量推理、编程等任务的能力，而“每任务成本”指标有助于比较效率。V4-Flash 是 DeepSeek V4 系列的一部分，旨在平衡性能与成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/news/news260424/">DeepSeek V 4 Preview Release | DeepSeek API Docs</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论可能突出了该模型令人印象深刻的性价比和强大的智能体能力，一些用户指出调整推理强度以获得最佳结果的重要性。可能还会讨论这种低价策略的可持续性以及与其他模型的比较。

**标签**: `#AI`, `#DeepSeek`, `#model release`, `#LLM`, `#cost efficiency`

---

<a id="item-6"></a>
## [无状态 MCP 重燃兴趣，催生新工具](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 8.0/10

Simon Willison 讨论了无状态 MCP（MCP 2.0）规范的影响，该规范移除了初始化握手和会话 ID，并介绍了他的新工具 mcp-explorer 和 datasette-mcp。 该规范简化了 MCP 的实现，使开发者更容易构建和扩展 AI 代理工具。它也标志着从基于 shell 的代理框架转向更可审计、更可控的基于工具的方法。 无状态 MCP 使用单个 HTTP 请求，通过 MCP-Protocol-Version 和 Mcp-Method 等头部信息，消除了会话管理的需要。Simon 在一周内构建了三个 MCP 实现，包括用于探测 MCP 服务器的 CLI 工具 mcp-explorer，以及为 Datasette 添加 MCP 服务器的 datasette-mcp。

rss · Simon Willison · 7月31日 23:13

**背景**: MCP（模型上下文协议）是一种向 LLM 驱动的代理暴露工具的标准，由 Anthropic 于 2024 年 11 月推出。它在 2025 年引起了巨大关注，但后来被 Skills（技能）所掩盖，后者允许代理使用终端和 curl。新的无状态 MCP 规范于 2026-07-28 作为候选版本发布，移除了初始化握手和会话 ID，使其更易于实现，更适合可扩展的 Web 应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/mcp-explorer">GitHub - simonw/ mcp - explorer : CLI tool for exploring an MCP server</a></li>
<li><a href="https://github.com/datasette/datasette-mcp">GitHub - datasette/ datasette - mcp : Adds a /-/mcp MCP server to any...</a></li>
<li><a href="https://azukiazusa.dev/en/blog/mcp-stateless/">The 2026-07-28 MCP Specification Becomes Stateless -First</a></li>

</ul>
</details>

**标签**: `#MCP`, `#AI agents`, `#protocol`, `#tools`, `#Simon Willison`

---

<a id="item-7"></a>
## [Reddit 用户训练 Transformer 预测血糖](https://www.reddit.com/r/MachineLearning/comments/1vc1txc/i_have_trained_a_model_to_predict_my_blood_sugar_p/) ⭐️ 8.0/10

一位 Reddit 用户分享了一个项目，他们训练了一个仅编码器的 Transformer，利用过去的血糖、碳水化合物和胰岛素数据以及未来的碳水化合物和胰岛素声明，来预测未来 2 小时的血糖水平。该模型使用了 DILATE 和分位数损失，训练了多种尺寸和变体，最大的模型约有 1700 万参数。 该项目展示了 Transformer 模型在个人健康监测中的新颖应用，可能通过提供个性化血糖预测来改善糖尿病管理。它还展示了 DILATE 损失和不确定性量化等先进技术，可能激发医疗保健时间序列预测的进一步研究。 该模型采用 BERT 风格，具有双向注意力和掩码的未来血糖，上下文窗口可变，为 8-24 小时。它使用 DILATE 损失拟合中位数线，使用分位数损失拟合不确定性带，并通过 Kendall-Gal 混合，所有血糖值均在 Kovatchev 风险空间中。最大的模型有 16 层和 16 个头，预训练耗时约 48 小时，微调不到 10 分钟。

reddit · r/MachineLearning · /u/0xdeadf1sh · 7月31日 20:09

**背景**: 血糖预测对糖尿病管理至关重要，因为它帮助患者预测和预防高血糖或低血糖。Transformer 模型最初为自然语言处理设计，但由于其捕捉长距离依赖的能力，已被改编用于时间序列预测。DILATE 损失是一种可微的损失函数，惩罚时间序列预测中的形状和时间失真，而分位数损失用于分位数回归以估计不确定性区间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1909.09020">Shape and Time Distortion Loss for Training Deep Time Series ... GitHub - vincent-leguen/DILATE: Code for our NeurIPS 2019 ... Shape and Time Distortion Loss for Training Deep Time Series ... vincent-leguen/DILATE | DeepWiki DILATE: Loss for Shape & Time in Forecasting - emergentmind.com DILATE/loss/dilate_loss.py at master · vincent-leguen/DILATE Re: Shape and Time Distortion Loss for Training Deep Time ...</a></li>
<li><a href="https://github.com/vincent-leguen/DILATE">GitHub - vincent-leguen/DILATE: Code for our NeurIPS 2019 ...</a></li>
<li><a href="https://proceedings.neurips.cc/paper_files/paper/2019/file/466accbac9a66b805ba50e42ad715740-Paper.pdf">Shape and Time Distortion Loss for Training Deep Time Series ...</a></li>

</ul>
</details>

**社区讨论**: 未提供社区讨论内容，但根据帖子背景，可能包括关于模型架构、训练数据和实际部署的问题，以及对方法和潜在改进的反馈。

**标签**: `#transformer`, `#health`, `#time-series`, `#blood-glucose`, `#machine-learning`

---

<a id="item-8"></a>
## [KataGo 研究揭示围棋神经网络中的对称性学习](https://www.reddit.com/r/MachineLearning/comments/1vcrki2/how_symmetric_are_the_insides_of_a_go_network_r/) ⭐️ 8.0/10

一项关于开源围棋程序 KataGo 的新可解释性研究，探讨了尽管训练时仅使用随机 8 倍数据增强，其超人类神经网络在多大程度上学习了方向不变的内部表示。该研究发表在 KataGo 研究页面上，揭示了网络对称性学习的意外发现。 这项研究为理解神经网络在复杂领域中如何学习对称性提供了宝贵见解，对改进数据增强策略和模型可解释性具有启示意义。理解对称性学习有助于为游戏和其他结构化任务设计更高效的架构和训练方法。 该研究几乎完全由 AI 驱动，但有人类的详细指导和反馈，并且文章面向非机器学习读者撰写，易于理解。代码已从帖子中链接，研究结果包括一个意外发现，挑战了关于神经网络如何处理方向不变性的假设。

reddit · r/MachineLearning · /u/icosaplex · 8月1日 16:18

**背景**: KataGo 是一个通过自我对弈训练的强大开源围棋引擎，使用带有残差块、策略头和价值头的卷积神经网络。围棋规则在旋转和反射下是对称的，但模型并未强制这种对称性，而是依靠随机数据增强让网络接触所有方向。本研究探讨网络是学习方向不变的内部表示，还是为每个方向分别记忆模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/lightvector/KataGo/7.2-model-architecture">Model Architecture | lightvector/ KataGo | DeepWiki</a></li>
<li><a href="https://katagotraining.org/">KataGo Distributed Training</a></li>

</ul>
</details>

**标签**: `#interpretability`, `#neural networks`, `#Go`, `#symmetry`, `#data augmentation`

---

<a id="item-9"></a>
## [VLM 基准高分却抹除临床术语并引入偏见](https://www.reddit.com/r/MachineLearning/comments/1vcipzz/vlms_can_score_well_on_benchmarks_while_silently/) ⭐️ 8.0/10

一篇新论文揭示，视觉语言模型（VLM）在标准放射学报告生成基准上可以获得高分，同时却悄悄抹除有临床意义的术语并引入有偏见的内容。作者提出了一个包含两个新指标（CAD 和 WAE）的框架来衡量这些问题。 这一发现至关重要，因为它表明临床 AI 的常规评估指标可能具有误导性，可能导致放射学报告生成系统的不安全部署。它强调了重新设计评估协议的必要性，以优先考虑临床效用和偏见检测。 该论文引入了两个新指标：临床缩写删除（CAD）和词级属性擦除（WAE），用于审计常规指标无法发现的语义擦除和新出现的偏见。研究表明，解码策略和指标选择共同混淆了放射学报告生成的评估。

reddit · r/MachineLearning · /u/ade17_in · 8月1日 09:27

**背景**: 放射学报告生成（RRG）旨在将医学图像自动转换为可操作的临床文本，减少文档负担并支持诊断决策。VLM 使 RRG 在临床工作流程中更加可行，但标准的文本相似性指标往往奖励重复模板，并且未能惩罚遗漏罕见但临床重要的术语。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2603.01625">Measuring What VLMs Don't Say: Validation Metrics Hide ...</a></li>
<li><a href="https://arxiv.org/html/2603.01625v1">Measuring What VLMs Don’t Say: Validation Metrics Hide ...</a></li>
<li><a href="https://www.aimodels.fyi/papers/arxiv/measuring-what-vlms-dont-say-validation-metrics">Measuring What VLMs Don't Say: Validation Metrics Hide ...</a></li>

</ul>
</details>

**标签**: `#VLM`, `#Radiology Report Generation`, `#Evaluation Metrics`, `#Bias`, `#Medical AI`

---

<a id="item-10"></a>
## [EA 以 550 亿美元被沙特财团收购，交易将于 8 月 4 日完成](https://www.gamersky.com/news/202607/2180618.shtml) ⭐️ 8.0/10

艺电（EA）宣布，由沙特公共投资基金（PIF）牵头，联合银湖资本和 Affinity Partners 组成的财团对其的收购已获得所有监管批准，预计将于 2026 年 8 月 4 日正式完成。这笔 550 亿美元的交易将使 EA 成为一家私营公司，其财务数据将不再对外公开。 此次收购是游戏史上第二大收购案，仅次于 2023 年微软以 754 亿美元收购动视暴雪。这凸显了沙特在游戏行业的激进布局，并可能重塑竞争格局，因为 EA 的《FIFA》和《战地》等主要系列将归主权财富基金所有。 该财团由 PIF、银湖资本和 Affinity Partners 组成。PIF 近年来持续增持多家游戏公司股份，并已全资收购了 Scopely 和 Niantic 等开发商。交易预计于 2026 年 8 月 4 日完成，之后 EA 将成为私营公司。

telegram · zaihuapd · 8月1日 09:10

**背景**: 沙特公共投资基金是一家主权财富基金，管理资产约 6500 亿美元，目标是在未来几年内超过 1 万亿美元。该基金一直大力投资游戏行业，作为其“2030 愿景”经济多元化战略的一部分。银湖资本是一家全球科技投资公司，管理资产和承诺资本合计约 1020 亿美元；Affinity Partners 则是 2021 年在迈阿密成立的私募股权公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://english.indianews.in/tech-auto/from-riyadh-to-silicon-valley-how-ea-became-the-jewel-of-saudi-arabias-gaming-vision-840036/">From Riyadh to Silicon Valley: How EA became the jewel of Saudi ...</a></li>
<li><a href="https://www.wral.com/saudi-arabia-s-public-investment-fund-just-reshaped-pro-golf-it-s-not-stopping-there/20899678/">Saudi Arabia’s Public Investment Fund just reshaped pro golf.</a></li>
<li><a href="https://www.silverlake.com/">We are Silver Lake</a></li>

</ul>
</details>

**标签**: `#EA`, `#acquisition`, `#gaming industry`, `#Saudi PIF`, `#M&A`

---

<a id="item-11"></a>
## [中国在联合国峰会上向全球南方推广开放权重 AI 模型](https://www.semafor.com/article/07/28/2026/token-diplomacy-how-china-is-shaping-the-worlds-ai-future) ⭐️ 8.0/10

7 月底在日内瓦联合国“智能向善”峰会上，中国代表团向巴基斯坦、俄罗斯、赞比亚等发展中国家推介中国的开放权重 AI 模型。阿里云架构师王坚表示，中国 AI 可以像能源一样成为其他国家发展的“基石”。 此举凸显了中国“词元外交”战略，以更低成本提供开放权重模型，以塑造全球 AI 基础设施和标准，与美国闭源模型形成对比。这可能深刻影响 AI 治理和地缘政治力量格局，尤其是在全球南方。 美国前沿实验室和特朗普政府官员明显缺席此次峰会。美国国务院发言人警告称，此举“将导致对中国基础设施和标准的依赖”。

telegram · zaihuapd · 8月1日 10:06

**背景**: 开放权重 AI 模型允许用户访问和修改模型的权重，相比通常通过 API 访问的闭源模型，提供了更大的灵活性和更低的长期成本。中国的“词元外交”指的是其向发展中国家输出 AI 能力（如词元，即 AI 处理单元）的战略，类似于传统的基础设施出口（如港口和铁路）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.semafor.com/article/07/28/2026/token-diplomacy-how-china-is-shaping-the-worlds-ai-future">Token diplomacy : How China is shaping the world’s AI future | Semafor</a></li>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-models-why-every-enterprise-should-paying-misra-gi2qc">Open - Weight AI Models : Why Every Enterprise Should Be Paying...</a></li>
<li><a href="https://www.diplomacy.edu/topics/ai-and-diplomacy/">AI DIPLOMACY : geo-politics, topics and tools in 2026 | Diplo</a></li>

</ul>
</details>

**标签**: `#AI geopolitics`, `#open-source AI`, `#China`, `#global south`, `#AI policy`

---

<a id="item-12"></a>
## [微软确认今年推出 Copilot“超级应用”](https://www.theverge.com/tech/972927/microsoft-copilot-super-app-confirmed) ⭐️ 8.0/10

微软 CEO 萨蒂亚·纳德拉在财报电话会议上确认，公司将于今年推出一款 AI“超级应用”，将 Copilot 的聊天、编程和智能体能力整合在一起，面向消费者和企业用户。该应用将把 Copilot 聊天、GitHub Copilot、Copilot Cowork 和 Autopilot 合并到一个平台中。 此举标志着微软在整合其 AI 产品方面的战略推进，可能为 AI 工具的打包和交付方式树立先例。通过为多样化的 AI 任务提供单一入口，它可能重塑用户工作流程，影响个人开发者和企业客户。 该超级应用将合并 Copilot 聊天、GitHub Copilot、Copilot Cowork 和 Autopilot，覆盖消费者和商业场景。微软上季度营收增至 900 亿美元，主要由 AI 和云业务推动，为这一举措提供了财务支持。

telegram · zaihuapd · 8月1日 13:18

**背景**: 微软一直在将 Copilot 从简单的聊天机器人发展为更高级的功能，如 Cowork（协作式 AI）和 Autopilot（自主智能体）。超级应用的概念旨在通过提供统一平台来解决客户对 AI 工具碎片化的不满。这顺应了类似趋势，OpenAI 最近也推出了整合 ChatGPT 和 Codex 的 ChatGPT Work 应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pjX2ZHa0VSSFFLeENQU20xQml5Z0FQAQ?hl=en-US&gl=US&ceid=US:en">Google News - Microsoft develops super app to consolidate Copilot ...</a></li>
<li><a href="https://www.aiplanetx.com/p/microsoft-copilot-super-app">Microsoft 's Copilot Super App</a></li>
<li><a href="https://overcentral.com/en/copilot-super-app/">Microsoft Confirms Copilot Super App Launch This Year</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Copilot`, `#AI`, `#Super App`, `#Product Announcement`

---