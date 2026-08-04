---
layout: default
title: "Horizon Summary: 2026-08-04 (ZH)"
date: 2026-08-04
lang: zh
---

> 从 78 条内容中筛选出 14 条重要资讯。

---

1. [LLM 奖励专业知识，而非取代它](#item-1) ⭐️ 8.0/10
2. [Swiftlet：在 Mac 上以 4.3GB 内存运行 80B Qwen，在 iPhone 上运行 35B 模型](#item-2) ⭐️ 8.0/10
3. [OpenAI 强调数学与计算机科学领域的十项进展](#item-3) ⭐️ 8.0/10
4. [ComfyUI 日首发支持 MiniMax H3：开放权重、原生音频与 2K 视频](#item-4) ⭐️ 8.0/10
5. [Pandoc 作者回顾文档转换工具二十年历程](#item-5) ⭐️ 8.0/10
6. [Andy Pavlo 加入 ClickHouse 创立 ClickHouse Labs](#item-6) ⭐️ 8.0/10
7. [Jane Street 的 Bonsai：类型安全的 OCaml UI 库](#item-7) ⭐️ 8.0/10
8. [AI 开始大幅削减客服岗位](#item-8) ⭐️ 8.0/10
9. [Kimi K3 架构：压缩记忆、深度注意力与潜在路由](#item-9) ⭐️ 8.0/10
10. [机器学习审稿人呼吁：无复现代码的论文应直接拒稿](#item-10) ⭐️ 8.0/10
11. [美国至少 50 名警员被控滥用车牌摄像头窥探前任](#item-11) ⭐️ 8.0/10
12. [英伟达 CMP 170HX 矿卡被破解，显存解锁至 80GB，价格暴涨](#item-12) ⭐️ 8.0/10
13. [英国要求苹果为加密云备份开后门，仅限英国公民数据](#item-13) ⭐️ 8.0/10
14. [华为提出“韬定律”，以时间缩微引领半导体新路径](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [LLM 奖励专业知识，而非取代它](https://www.seangoedecke.com/llms-reward-expertise/) ⭐️ 8.0/10

文章认为，LLM 不是专业知识的替代品，而是一种放大那些已拥有深厚领域知识的人技能的工具，挑战了 AI 使专业知识过时的流行说法。 这一观点对软件工程社区意义重大，因为它重新定义了 LLM 在开发中的角色，表明对深层专业知识的投资仍然至关重要，并且 LLM 可能扩大专家与新手之间的生产力差距。 文章使用放大镜等类比来说明 LLM 反映了用户自身的知识和交互质量。它强调，在使用 LLM 时，对特定代码库的熟悉程度比一般的软件知识更有价值。

hackernews · MaxMussio · 8月3日 21:13 · [社区讨论](https://news.ycombinator.com/item?id=49161518)

**背景**: 大型语言模型（LLM）如 GPT-4 是经过海量文本数据训练的人工智能系统，能够生成类似人类的文本。在软件工程中，它们被用于代码生成、调试和文档编写，但其有效性取决于用户编写精确提示和评估输出的能力，这需要领域专业知识。

**社区讨论**: 评论者大多同意文章的观点，分享个人轶事支持 LLM 放大现有专业知识的说法。一些人指出这种效果可能存在确认偏差，并呼吁进行正式研究，而另一些人则强调即使新手也能通过简单的提示获得有用的结果，表明情况更为复杂。

**标签**: `#LLM`, `#software engineering`, `#AI tools`, `#expertise`, `#productivity`

---

<a id="item-2"></a>
## [Swiftlet：在 Mac 上以 4.3GB 内存运行 80B Qwen，在 iPhone 上运行 35B 模型](https://github.com/leonickson1/Swiftlet) ⭐️ 8.0/10

一个名为 Swiftlet 的新开源项目展示了在 Mac 上仅用 4.3GB 内存运行 80B 参数的 Qwen 模型，以及在 iPhone 上运行 35B 模型的能力，标志着端侧 AI 的一个重要里程碑。 这一成就突破了消费级硬件的极限，可能使强大的 AI 模型无需依赖云端即可本地运行，从而普及大型语言模型的访问，并增强隐私保护和离线能力。 该项目利用流式权重和高效的内存管理，将大型模型适配到有限的内存中。它基于 TurboFieldfare 等先前工作，并针对 Apple Silicon 进行了优化，在 24-32GB 内存的 Mac 上通过增加 RAM 缓存可能进一步提升速度。

hackernews · leonickson · 8月3日 16:54 · [社区讨论](https://news.ycombinator.com/item?id=49158333)

**背景**: 大型语言模型（LLM）通常需要巨大的 GPU 内存，但量化、混合专家（MoE）和流式权重等技术使其能够在内存有限的设备上运行。Qwen3-Next-80B-A3B 是一个 MoE 模型，总参数 80B 但仅激活 3B，因此更加高效。Apple Silicon 的统一内存架构特别适合此类优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-qwen-qwen3-next-80b-a3b.html">Qwen3 Next 80B A3B - Amazon Bedrock</a></li>
<li><a href="https://qwen.ai/blog?id=4074cca80393150c248e508aa62983f9cb7d27cd&from=research.latest-advancements-list">Qwen</a></li>
<li><a href="https://blog.starmorph.com/blog/apple-silicon-llm-inference-optimization-guide">Apple Silicon LLM Inference Optimization: The Complete Guide ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，用户称赞其进展和实用性。有人指出此前已有类似声明，并引用了 anemll 在 iPhone 上运行 400B 模型的项目。其他人则对端侧 AI 的未来表示兴奋，并计划亲自测试该项目。

**标签**: `#on-device AI`, `#LLM`, `#optimization`, `#Apple Silicon`, `#open source`

---

<a id="item-3"></a>
## [OpenAI 强调数学与计算机科学领域的十项进展](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 8.0/10

OpenAI 发布了一篇题为“数学与理论计算机科学领域的十项进展”的文章，重点介绍了这些领域的最新成就。该文章在 Hacker News 上引发了广泛讨论，获得了 525 个点赞和 804 条评论。 这一公告凸显了 AI 在数学发现中日益重要的作用，可能加速研究进程并改变数学家的研究方式。同时，它也引发了关于 AI 指数级进展在各领域更广泛影响的讨论。 该文章列出了十项具体进展，但所给内容中未提供细节。讨论中包括关于 AI 快速反驳猜想的能力，以及 AI 可能使数学证明更可计算的评论。

hackernews · milkshakes · 8月3日 16:27 · [社区讨论](https://news.ycombinator.com/item?id=49157930)

**背景**: AI 越来越多地被应用于数学和理论计算机科学问题，像 GPT-4 和专用系统等模型辅助定理证明和猜想生成。OpenAI 的这篇文章突出了近期的成功，反映了 AI 正成为研究中有价值工具的趋势，尽管它仍然缺乏人类般的直觉来提出猜想。

**社区讨论**: 社区普遍印象深刻，但对重要性存在分歧。一些人看到指数级进展，认为 AI 的影响不可否认，而另一些人则警告并非所有数学问题都能自动解决。还有引用道格拉斯·亚当斯的幽默，以及指出 AI 能通过人类无法做到的苦力快速反驳猜想。

**标签**: `#AI`, `#Mathematics`, `#Theoretical Computer Science`, `#OpenAI`, `#Research`

---

<a id="item-4"></a>
## [ComfyUI 日首发支持 MiniMax H3：开放权重、原生音频与 2K 视频](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui) ⭐️ 8.0/10

ComfyUI 已为 MiniMax H3 添加了日首发支持。MiniMax H3 是一款开放权重的全模态生成模型，能够生成最高 2K 分辨率、长达 15 秒且带有原生立体声的视频。该模型接受文本、图像、视频和音频作为输入，支持在模型发布当天即可使用。 这意义重大，因为它让 AI/ML 社区能够在流行的流程工具中立即使用下一代开放权重视频模型，支持本地实验和集成。开放权重、原生音频和高分辨率视频生成的结合，可能加速视频合成和多模态 AI 应用的创新。 该模型的调制权重约占总参数的 40%，可以被剪枝并替换为功能等效的查找表，从而在不损失输出质量的情况下将内存占用减少 66%（从 123.6 GB 降至 42.5 GB）。结合动态 VRAM 卸载，这使得 2K 视频模型可以在 RTX 3060 等 GPU 上本地运行。

hackernews · vblanco · 8月3日 13:34 · [社区讨论](https://news.ycombinator.com/item?id=49155629)

**背景**: MiniMax H3 是一个通用的全模态生成模型，能够联合理解文本、图像、视频和音频等多模态上下文。开放权重模型是指核心组件公开发布的 AI 模型，允许任何人下载和使用，但根据许可证可能有限制。ComfyUI 是一个流行的基于节点的 AI 图像和视频生成界面，日首发支持意味着模型在发布当天就集成到该工具中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between ...</a></li>
<li><a href="https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui">MiniMax H3 Day - 0 Support in ComfyUI : Open Weights, Native Audio...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>

</ul>
</details>

**社区讨论**: 社区成员报告了令人印象深刻的结果，一位用户指出在 4070 Ti Super（16 GB VRAM）上生成 10 秒 480p 视频需要 10 分钟，但结果非常出色。另一位用户强调鼠标渲染出奇地好，是当前 SOTA 模型的重大飞跃，但有些片段仍有“AI 平滑”效果。一些用户发现，当偏离正常场景时模型仍存在卡顿，但总体上文本到视频的质量和速度受到称赞。

**标签**: `#AI/ML`, `#Video Generation`, `#Open Weights`, `#ComfyUI`, `#MiniMax`

---

<a id="item-5"></a>
## [Pandoc 作者回顾文档转换工具二十年历程](https://pandoc.org/twenty-years-of-pandoc.html) ⭐️ 8.0/10

Pandoc 的创造者 John MacFarlane 在 Pandoc 官方网站上发表了一篇题为《Pandoc 二十年》的回顾文章，反思了该工具的历史、设计决策以及 Haskell 在其发展中的作用。 Pandoc 是一个广泛使用的开源文档转换工具，这篇回顾文章提供了对其设计理念和演变的宝贵见解。它强调了一个基于基本原则构建的精心设计的工具如何随着时间的推移而变得更加有用，尤其是在人工智能驱动开发快速发展的时代。 文章解释了 Pandoc 的架构，即使用 N 个读取器和 M 个写入器来支持 N×M 种转换，这是其可扩展性的关键。MacFarlane 还指出，最初出于个人兴趣选择 Haskell，导致了高质量但数量较少的贡献者群体。

hackernews · fiddlosopher · 8月3日 15:04 · [社区讨论](https://news.ycombinator.com/item?id=49156750)

**背景**: Pandoc 是一个通用文档转换器，可以在数百种格式之间转换文件，包括 Markdown、HTML、PDF、DOCX 和 EPUB。它基于 Haskell 构建，是 Quarto 等工具的核心引擎。文章回顾了 Pandoc 如何成为最流行的 Haskell 程序之一，支持超过五十种文档格式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pandoc.org/twenty-years-of-pandoc.html">Twenty Years of Pandoc</a></li>
<li><a href="https://hackage.haskell.org/package/pandoc">pandoc: Conversion between markup formats - Hackage Using the pandoc API Haskell Pandoc: a call to arms : r/haskell - Reddit Twenty years of Pandoc | Noise GitHub - adamConnerSax/knit-haskell: Use Pandoc to write ... 24 Days of Hackage: pandoc : r/haskell - Reddit</a></li>
<li><a href="https://servinagrero.github.io/reproducible_research/02-pandoc_and_basics.html">What is Pandoc ? – Reproducible Research with Quarto</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了对 Pandoc 设计和实用性的赞赏。用户分享了个人经验，例如在 bash 脚本中使用 Pandoc 生成网站，以及将其与 Typst 集成以创建 PDF。一些评论者同意 MacFarlane 关于 Haskell 对贡献者文化影响的观察，指出技术选择可以塑造社区动态。

**标签**: `#pandoc`, `#document conversion`, `#Haskell`, `#open source`, `#software history`

---

<a id="item-6"></a>
## [Andy Pavlo 加入 ClickHouse 创立 ClickHouse Labs](https://clickhouse.com/blog/andy-pavlo-joins-clickhouse) ⭐️ 8.0/10

著名数据库研究者、卡内基梅隆大学教授 Andy Pavlo 已加入 ClickHouse，创立新的研究实验室 ClickHouse Labs，旨在弥合数据库研究领域学术界与工业界之间的鸿沟。 此举意义重大，因为它将顶尖学术人才引入开源 OLAP 数据库公司，可能加速数据库技术的创新，并促进更紧密的产学研合作。这也凸显了企业在 AI 之外投资基础基础设施研究的趋势。 ClickHouse Labs 将专注于推进数据库研究，Pavlo 将继续其教育工作，例如广受欢迎的 CMU 系列讲座，可能以赞助形式进行。该实验室旨在解决 OLAP 系统中的挑战，包括存储/计算分离架构以及数据摄入和索引策略。

hackernews · nikolay_sivko · 8月3日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49156011)

**背景**: ClickHouse 是一个开源的列式 OLAP 数据库，以其在实时分析中的高性能而闻名，利用向量化处理和高效的 CPU/内存使用。OLAP 数据库专为跨大型数据集的分析查询而设计，与传统 OLTP 系统形成对比。Pavlo 是数据库领域的知名人物，以其研究和教育贡献而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://clickhouse.com/docs/academic_overview">Architecture overview - ClickHouse Documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Online_analytical_processing">Online analytical processing - Wikipedia</a></li>
<li><a href="https://clickhouse.com/resources/engineering/olap-database">What is an OLAP database?</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了兴奋和支持，用户希望 Pavlo 能倡导资助学术数据库研究，并继续他的系列讲座。一些人讨论了 ClickHouse 等 OLAP 系统与 Trino 的融合趋势，以及这对存储和摄入架构的影响。总体情绪积极，对 AI 之外的企业研究实验室表示赞赏。

**标签**: `#database`, `#ClickHouse`, `#research`, `#industry-academia`, `#OLAP`

---

<a id="item-7"></a>
## [Jane Street 的 Bonsai：类型安全的 OCaml UI 库](https://github.com/janestreet/bonsai) ⭐️ 8.0/10

Jane Street 发布了 Bonsai，这是一个基于 OCaml 的新 UI 库，用于构建高性能、响应式的 Web 应用，现已在 GitHub 和 opam 上可用。它通过在前后端都使用 OCaml，实现了类型安全的全栈开发。 Bonsai 展示了 OCaml 在前端开发中的可行性，可能扩大其在后端系统之外的应用。它提供了一种类型安全的 JavaScript 框架替代方案，可能吸引函数式编程爱好者以及寻求端到端类型安全的公司。 Bonsai 部分灵感来自 Elm，并在 Jane Street 内部用于几乎所有 Web 应用，从公司目录到交易系统监控。它与 Incr_dom 或 React 等增量式框架集成，初始版本为 opam 上的 0.17.0。

hackernews · KolmogorovComp · 8月3日 08:29 · [社区讨论](https://news.ycombinator.com/item?id=49152842)

**背景**: OCaml 是一种通用、多范式的语言，以其强大的静态类型和函数式编程特性而闻名。Bonsai 利用这些特性提供了类型安全的 UI 开发体验，允许开发者在客户端和服务器之间共享类型，减少运行时错误并提高代码可维护性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/janestreet/bonsai">GitHub - janestreet / bonsai : A library for building dynamic webapps...</a></li>
<li><a href="https://opam.ocaml.org/packages/bonsai/bonsai.v0.17.0/">The homepage of opam, a package manager for OCaml</a></li>
<li><a href="https://en.wikipedia.org/wiki/OCaml">OCaml - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区讨论总体积极，用户称赞类型安全的全栈能力，并提到了相关的播客节目。然而，一些用户对库的美观性提出质疑，并询问它与另一个 OCaml 到 JavaScript 工具 Melange 的比较，以及是否会牺牲 JS 生态系统。此外，有用户指出文档链接失效，并询问 DOM 更新机制。

**标签**: `#OCaml`, `#UI framework`, `#full-stack`, `#functional programming`, `#Jane Street`

---

<a id="item-8"></a>
## [AI 开始大幅削减客服岗位](https://www.solidot.org/story?sid=84994) ⭐️ 8.0/10

包括微软、Uber 和澳大利亚联邦银行在内的大型公司正使用 AI 驱动的聊天机器人和自动电话系统来取代人工客服岗位，导致大量裁员。分析师估计到 2030 年，近半客服职位可能受到影响。 这一趋势标志着劳动力市场的重大转变，尤其是在美国、印度和菲律宾等客服行业雇佣数百万人的国家。它凸显了生成式 AI 对白领工作的日益影响，并引发了对岗位流失和劳动力再培训需求的担忧。 联邦银行裁减了数百名客服岗位，每年节省数千万美元。微软将其客服团队从约 5 万人缩减至 4 万人，据 Judson Althoff 称，AI 每年为客服成本节省约 7.5 亿美元。凯悦酒店裁掉了美洲地区三成的内部客服，Uber 则裁减了 10% 的客服岗位以“拥抱 AI”。

rss · Solidot 奇客 · 8月3日 14:22

**背景**: 客服行业传统上是主要的就业领域，许多西方公司将岗位外包给印度和菲律宾等英语国家。生成式 AI 的进步使自动化系统更能处理常规咨询，促使企业采用它们以降低成本和提高效率。然而，复杂问题仍需要人工支持，这一转变预计将持续。

**标签**: `#AI`, `#automation`, `#customer service`, `#employment`, `#generative AI`

---

<a id="item-9"></a>
## [Kimi K3 架构：压缩记忆、深度注意力与潜在路由](https://newsletter.semianalysis.com/p/kimi-k3-the-manos-the-mythos-the) ⭐️ 8.0/10

SemiAnalysis 发布了对 Kimi K3 架构的深度技术解析，详细介绍了压缩记忆、跨深度注意力和潜在专家路由方面的创新。分析强调了这些机制如何提升这一 3T 级开源模型的推理性能。 Kimi K3 代表了前沿的开源 3T 级模型，其架构选择可能影响未来 LLM 的设计。对推理效率和长上下文处理的关注解决了行业关键挑战，可能降低部署成本并催生新应用。 该架构沿序列长度、网络深度和模型宽度三个维度扩展信息流。它使用混合注意力，将 Kimi Delta Attention（KDA）层与 Gated MLA 层结合，并采用潜在专家路由，将路由与隐藏维度解耦以提高效率。

rss · Semianalysis · 8月3日 19:42

**背景**: Kimi K3 是全球首个开源 3T 级模型，在编程、知识工作和推理方面提供前沿性能，并具备原生多模态和 1M 上下文。注意力机制允许模型权衡 token 的重要性，而混合专家（MoE）技术则在不按比例增加计算量的情况下实现扩展。潜在专家路由在专家处理前将 token 投影到低维空间，从而提高效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.24653">Kimi K3: Open Frontier Intelligence - arXiv.org</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://newsletter.semianalysis.com/p/kimi-k3-the-manos-the-mythos-the">Kimi K3, The Manos, The Mythos, The Legendos</a></li>

</ul>
</details>

**标签**: `#AI`, `#architecture`, `#inference`, `#Kimi K3`, `#LLM`

---

<a id="item-10"></a>
## [机器学习审稿人呼吁：无复现代码的论文应直接拒稿](https://www.reddit.com/r/MachineLearning/comments/1vei12v/its_time_to_desk_reject_papers_that_dont_include/) ⭐️ 8.0/10

一位审稿人报告称，今年为机器学习顶级会议审稿的 12 篇论文中，只有 1 篇提供了完整代码，而提供部分代码的 5 篇中有 3 篇存在使结果失效的明显错误。他们认为，会议应直接拒收那些未提供可复现结果代码的论文。 这凸显了机器学习研究中的可复现性危机，隐藏代码损害了科学诚信并浪费了审稿人的精力。如果采纳该政策，将激励作者分享代码，提升对已发表结果的验证和信任。 审稿人指出，7 篇论文未提供代码，4 篇仅提供片段。他们强调，机器学习代码中的小错误可能产生重大影响，而当前的激励机制不鼓励代码共享，因为这会增加因错误而被拒稿的风险。

reddit · r/MachineLearning · /u/Flaky-Ambition5900 · 8月3日 16:17

**背景**: 直接拒稿（desk rejection）是指编辑在同行评审前就拒绝论文，通常是因为明显违反投稿指南。在机器学习中，可复现性需要代码和数据来验证结果，而 AUROC 等指标常用于评估模型性能。代码共享的缺乏是该领域长期存在的问题，许多论文未能提供足够的实现细节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scientific-publishing.webshop.elsevier.com/publication-process/paper-rejection-common-reasons/">Paper Rejection: Common Reasons | Elsevier Language Services</a></li>
<li><a href="https://glassboxmedicine.com/2019/02/23/measuring-performance-auc-auroc/">Measuring Performance: AUC ( AUROC ) – Glass Box Medicine</a></li>

</ul>
</details>

**标签**: `#reproducibility`, `#machine learning`, `#research policy`, `#peer review`, `#open source`

---

<a id="item-11"></a>
## [美国至少 50 名警员被控滥用车牌摄像头窥探前任](https://www.washingtonpost.com/technology/2026/08/02/how-police-officers-used-vast-network-cameras-spy-their-exes/) ⭐️ 8.0/10

《华盛顿邮报》的一项调查显示，美国至少 50 名执法人员被指控或起诉滥用 Flock 等车牌识别系统进行非法监控。其中 26 起案件涉及窥探妻子、女友、前任或心仪女性，46 起使用了 Flock 系统。 这项调查凸显了执法部门部署自动车牌识别系统（ALPR）时存在的系统性隐私和道德问题。它强调了制定更严格法规、加强审计和问责措施以防范监控技术滥用的紧迫性，这些技术在美国正日益普及。 调查发现，佐治亚州警察局长 Michael Steffman 在 2025 年 11 月被捕前，对其前女友 Bakely 及其女儿的车牌进行了约 600 次搜索；他在 2026 年 4 月开庭前自杀身亡。Flock 声称拥有超过 12 万台摄像头，覆盖 6000 多个社区，每月记录 200 亿次车牌扫描，并推出了可选的“审计辅助”功能，而目前只有 13 个州要求审计，至少 8 个州将滥用定为犯罪。

telegram · zaihuapd · 8月3日 09:03

**背景**: 自动车牌识别系统（ALPR）使用摄像头捕捉并记录车牌号码和车辆细节，通常会将数据存储较长时间。Flock Safety 是这类系统的主要供应商，美国各地警察部门广泛采用以协助犯罪调查，但其大规模数据收集引发了隐私担忧。滥用案件涉及警员出于个人原因使用这些系统，例如跟踪心仪对象，而这类行为往往未被法律明确禁止或缺乏充分审计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://edition.cnn.com/2026/07/26/us/flock-cameras-surveillance-abuse">Inside the growing police use and misuse of Flock’s license ...</a></li>
<li><a href="https://ij.org/police-have-reportedly-used-license-plate-readers-to-stalk-romantic-interests-at-least-14-times-in-recent-years/">Police Have Reportedly Used License Plate Readers to Stalk ...</a></li>

</ul>
</details>

**标签**: `#surveillance`, `#privacy`, `#law enforcement`, `#license plate cameras`, `#ethics`

---

<a id="item-12"></a>
## [英伟达 CMP 170HX 矿卡被破解，显存解锁至 80GB，价格暴涨](https://finance.sina.com.cn/tech/roll/2026-08-03/doc-inikzqsf4659769.shtml) ⭐️ 8.0/10

亚利桑那州立大学的研究人员公开了一种破解英伟达 CMP 170HX 矿卡的方法，绕过 OTP 熔丝锁定，将显存最高提升至 80GB，FP32 算力从 0.39 TFLOPS 提升至 94 TFLOPS。该漏洞利用 GPU 安全协处理器（Falcon）中的栈溢出漏洞修改硬件寄存器。 此次解锁将原本受限的矿卡转变为可行的 AI 推理加速器，显著降低了 AI 工作负载的成本门槛。价格从 300-500 元飙升至 3000-4000 元（海外甚至达 1500 美元），反映了高需求，同时也凸显了硬件锁定机制的安全隐患。 该漏洞利用 Falcon 安全协处理器的 DMA 无界溢出漏洞，实现权限提升以修改寄存器。虽然解锁后的卡可在 Windows 和 Linux 下运行 AI 图像生成和大语言模型推理，但长期稳定性和不同批次的解锁上限存在差异，并非所有卡都能达到 80GB。

telegram · zaihuapd · 8月3日 11:29

**背景**: CMP 170HX 是英伟达于 2021 年推出的专用矿卡，基于 GA100 核心（与 A100 相同），但通过 OTP 熔丝在硬件层面限制了算力、显存和 PCIe 功能，此前被认为不可逆转。此次破解表明，即使是硬件级限制也可能被绕过，引发了对 GPU 安全协处理器安全性的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://minerstat.com/hardware/nvidia-cmp-170hx">Nvidia CMP 170HX mining calculator ⛏️ | minerstat</a></li>
<li><a href="https://www.nvidia.com/en-us/cmp/">The NVIDIA CMP HX Professional Crypto Mining Processor</a></li>
<li><a href="https://www.usenix.org/conference/usenixsecurity24/presentation/guo-yanan">GPU Memory Exploitation for Fun and Profit - USENIX</a></li>

</ul>
</details>

**社区讨论**: 国内社区已开始验证解锁方法，有用户报告成功在解锁卡上运行 AI 推理。一些用户对平价 AI 硬件表示兴奋，但也有人提醒注意潜在的不稳定性以及购买可能无法完全解锁的卡的风险。

**标签**: `#hardware security`, `#GPU`, `#Nvidia`, `#AI inference`, `#exploit`

---

<a id="item-13"></a>
## [英国要求苹果为加密云备份开后门，仅限英国公民数据](https://t.me/zaihuapd/42953) ⭐️ 8.0/10

9 月初，英国内政部向苹果发出新的技术能力通知，要求其为加密云备份创建后门，但这次仅针对英国公民的数据。此前 1 月份的通知曾要求全球访问权限，引发了与美国的 diplomatic 紧张关系。 此举可能开创先例，使政府能够强迫科技公司削弱加密，从而可能损害全球用户的隐私和安全。这也凸显了国家安全需求与科技行业对端到端加密承诺之间的持续冲突。 苹果此前在 2 月份因早前的全球要求而从英国撤回了 iCloud 高级数据保护功能。隐私活动人士警告，任何迫使苹果破坏系统安全的尝试都可能危及全球用户的私人信息安全。

telegram · zaihuapd · 8月3日 15:40

**背景**: 英国的《2016 年调查权力法案》（又称“窥探者宪章”）为技术能力通知提供了法律依据，要求公司向执法部门提供特定能力。苹果的高级数据保护使用端到端加密来保护 iCloud 数据，这意味着即使是苹果也无法访问，因此成为政府后门要求的目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Technical_capability_notice">Technical capability notice</a></li>
<li><a href="https://www.gov.uk/government/publications/notices-regime-code-of-practice/notices-regime-code-of-practice-accessible">Notices regime code of practice (accessible) - GOV.UK</a></li>
<li><a href="https://support.apple.com/en-us/108756">How to turn on Advanced Data Protection for iCloud - Apple Support</a></li>

</ul>
</details>

**标签**: `#Apple`, `#UK government`, `#encryption backdoor`, `#privacy`, `#cloud security`

---

<a id="item-14"></a>
## [华为提出“韬定律”，以时间缩微引领半导体新路径](https://t.me/zaihuapd/42966) ⭐️ 8.0/10

在近日于上海举行的 2026 国际电路与系统研讨会（ISCAS）上，华为发表了“韬定律”（τ定律），提出以“时间缩微”替代传统“几何缩微”。华为同时宣布，过去六年已依据该定律设计并量产了 381 款芯片，今年秋季将推出采用逻辑折叠技术的新麒麟芯片。 这一发布意义重大，因为它提出了一种新的缩放原则，有望在摩尔定律逼近物理极限之际延续半导体行业的进步。若得到验证，可能重塑行业战略，并为面临出口限制的企业提供先进芯片制造的另一条路径。 韬定律通过降低时间常数，实现器件、电路、芯片到系统的多层级协同优化。华为预计，到 2031 年，基于该定律的高端芯片晶体管密度可达 1.4 纳米制程同等水平，并计划以开放合作推动产业发展。

telegram · zaihuapd · 8月4日 08:04

**背景**: 摩尔定律预测芯片上的晶体管数量大约每两年翻一番，几十年来一直推动半导体行业进步，但如今因物理极限而放缓。传统的几何缩微（即缩小晶体管尺寸）变得越来越困难和昂贵。韬定律提出通过优化时间相关参数来替代，为不单纯依赖尺寸缩小而持续提升性能提供了新方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.pedaily.cn/202605/564396.shtml">详解华为“ 韬 定 律 ”：对 半 导 体 行业究竟意味着什么？_ 投资界</a></li>
<li><a href="https://m.gelonghui.com/p/4911792">韬 定 律 开启 半 导 体 新周期：四大增量方向梳理</a></li>
<li><a href="https://baike.baidu.com/item/逻辑折叠技术/67870423">逻辑折叠技术_百度百科</a></li>

</ul>
</details>

**社区讨论**: 提供的内容中不包含社区评论，因此无法提供讨论摘要。

**标签**: `#semiconductors`, `#Huawei`, `#Moore's Law`, `#chip design`, `#technology`

---