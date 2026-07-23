---
layout: default
title: "Horizon Summary: 2026-07-23 (ZH)"
date: 2026-07-23
lang: zh
---

> 从 95 条内容中筛选出 17 条重要资讯。

---

1. [陶哲轩用 ChatGPT 探索雅可比猜想反例](#item-1) ⭐️ 9.0/10
2. [SkewAdam 将 MoE 优化器内存削减 97%](#item-2) ⭐️ 9.0/10
3. [GigaToken：通过 SIMD 实现千倍加速的 LLM 分词](#item-3) ⭐️ 8.0/10
4. [Bento：整个 PPT 放在一个 HTML 文件中](#item-4) ⭐️ 8.0/10
5. [初创公司的 Postgres 生存指南](#item-5) ⭐️ 8.0/10
6. [面试项目隐藏恶意 Git 钩子](#item-6) ⭐️ 8.0/10
7. [Anthropic 的 Claude Tag 处理 65% 的产品工程 PR](#item-7) ⭐️ 8.0/10
8. [美国财政部因 Moonshot AI 模型蒸馏威胁制裁](#item-8) ⭐️ 8.0/10
9. [OpenAI 基础设施支出达 7500 亿美元](#item-9) ⭐️ 8.0/10
10. [数学家仍未找到最快乘法方法](#item-10) ⭐️ 8.0/10
11. [Vera Rubin NVL72 与 GB200 NVL72：推理总拥有成本与架构对比](#item-11) ⭐️ 8.0/10
12. [Hugging Face 披露 AI 智能体攻击，商业大模型拒绝协助取证](#item-12) ⭐️ 8.0/10
13. [中国科技公司提前招募青少年应对 AI 人才短缺](#item-13) ⭐️ 8.0/10
14. [月之暗面寻求 20 亿美元融资，估值达 300 亿美元](#item-14) ⭐️ 8.0/10
15. [微软考虑接入 DeepSeek 以降低 Copilot Cowork 成本](#item-15) ⭐️ 8.0/10
16. [四大 AI 编程代理曝沙箱逃逸漏洞](#item-16) ⭐️ 8.0/10
17. [特朗普或限制美企使用中国开放权重 AI 模型](#item-17) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [陶哲轩用 ChatGPT 探索雅可比猜想反例](https://chatgpt.com/share/6a5fdc7a-d6f8-83e8-bbea-8deb42cfed56) ⭐️ 9.0/10

陶哲轩分享了一段 ChatGPT 对话，他系统地引导 AI 发现了一个雅可比猜想的反例，展示了先进的 AI 辅助数学推理。 这表明，在专家引导下，大型语言模型可以成为数学研究的强大工具，可能加速发现并让高级推理更普及。 该反例是一个结构化的三元多项式，并非暴力搜索所得；陶哲轩的提示非常具体，使用专业术语和逐步推进的方式从模型中提取有用见解。

hackernews · gmays · 7月22日 17:30 · [社区讨论](https://news.ycombinator.com/item?id=49010345)

**背景**: 雅可比猜想断言：如果一个多项式映射的雅可比行列式是非零常数，则该映射具有多项式逆。该猜想于 1939 年提出，以众多错误证明而闻名。最近有人用 AI 找到了大于 2 维情况的反例，但二维情形仍未解决。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jacobian_conjecture">Jacobian conjecture</a></li>
<li><a href="https://mathworld.wolfram.com/JacobianConjecture.html">Jacobian Conjecture -- from Wolfram MathWorld</a></li>
<li><a href="https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/">A digestion of the Jacobian conjecture counterexample | What's new</a></li>

</ul>
</details>

**社区讨论**: 评论者对陶哲轩的专业提示技巧感到着迷，指出他具体且充满术语的问题是从 AI 获得有用结果的关键。他们还强调反例在结构上有意义，并非暴力搜索所得，这展示了 AI 如何高效地将新知识映射到专家的思维模型中。

**标签**: `#mathematics`, `#AI-assisted research`, `#LLM applications`, `#Jacobian Conjecture`, `#expert prompting`

---

<a id="item-2"></a>
## [SkewAdam 将 MoE 优化器内存削减 97%](https://www.reddit.com/r/MachineLearning/comments/1v38k1m/skewadam_a_tiered_optimizer_that_cuts_moe_state/) ⭐️ 9.0/10

SkewAdam 是一种分层优化器，将混合专家（MoE）模型的优化器状态内存减少了 97.4%，从 50.6 GB 降至 1.29 GB，使得 6.78B 参数的 MoE 模型能够单卡运行在 40GB GPU 上。 这一突破大幅降低了训练大型 MoE 模型的硬件门槛，使得拥有消费级 GPU 的研究人员也能尝试此前仅限于高端集群的架构。 SkewAdam 采用分层状态分配：骨干参数（5%）使用动量加分解二阶矩，专家参数（95%）仅使用分解二阶矩，路由器参数（<0.01%）使用精确二阶矩，同时保持了收敛性和路由器稳定性。

reddit · r/MachineLearning · /u/Kooky-Ad-4124 · 7月22日 07:04

**背景**: 混合专家（MoE）模型使用多个专门的子网络（专家），由路由器激活，从而在不显著增加计算量的情况下扩大模型容量。然而，使用 AdamW 等标准优化器训练 MoE 需要为每个参数存储较大的优化器状态（动量和二阶矩），这常常占据 GPU 内存的主要部分。Adafactor 中使用的分解二阶矩估计通过低秩因子近似二阶矩矩阵来减少内存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@apoorvajain1111/inside-the-sparse-brain-how-mixture-of-experts-moe-makes-llms-smarter-faster-and-greener-205b0fea1416">Inside the Sparse Brain: How Mixture - of - Experts ( MoE )... | Medium</a></li>
<li><a href="https://deepwiki.com/google-deepmind/optax/3.1-standard-optimizers">Standard Optimizers | google-deepmind/optax | DeepWiki</a></li>

</ul>
</details>

**标签**: `#Mixture-of-Experts`, `#Optimizer`, `#Memory Efficiency`, `#Deep Learning`, `#GPU Training`

---

<a id="item-3"></a>
## [GigaToken：通过 SIMD 实现千倍加速的 LLM 分词](https://github.com/marcelroed/gigatoken/) ⭐️ 8.0/10

GigaToken 是一个开源库，通过 SIMD 优化的预分词和缓存技术，实现了约 1000 倍的语言模型分词加速。 分词是 LLM 的关键预处理步骤，这一加速在处理数 TB 训练文本时可大幅节省时间和成本。 加速源于用 SIMD 指令替代基于正则表达式的预分词，并深度优化了预分词映射的缓存，在现代 x86 和 ARM CPU 上表现一致。

hackernews · syrusakbary · 7月22日 17:20 · [社区讨论](https://news.ycombinator.com/item?id=49010167)

**背景**: 分词将原始文本转换为 LLM 可处理的数值令牌。传统分词器依赖正则表达式进行预分词，计算开销大。SIMD（单指令多数据）允许并行处理多个字符，大幅加速这一步骤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/marcelroed/gigatoken/">GitHub - marcelroed/gigatoken: Language model tokenization at GB/s · GitHub</a></li>
<li><a href="https://medium.com/@shashankag14/tokenization-in-large-language-models-llms-0ba0aea6b1d6">Tokenization in Large Language Models (LLMs) | by Shashank Agarwal | Medium</a></li>
<li><a href="https://www.traceloop.com/blog/a-comprehensive-guide-to-tokenizing-text-for-llms">A Comprehensive Guide to Tokenizing Text for LLMs | Traceloop - LLM Application Observability</a></li>

</ul>
</details>

**社区讨论**: 社区称赞这项工作非常出色，指出其对离线预训练数据准备的价值大于推理场景。有人幽默地提到分词通常只占推理时间的不到 0.1%，但承认其对数据预处理有重大影响。

**标签**: `#tokenization`, `#LLM`, `#performance optimization`, `#SIMD`, `#open source`

---

<a id="item-4"></a>
## [Bento：整个 PPT 放在一个 HTML 文件中](https://bento.page/slides/) ⭐️ 8.0/10

Bento 是一个单一的 HTML 文件，提供了完整的幻灯片工具，包括编辑、动画和实时协作，无需安装或云登录。 这种方法挑战了传统的演示软件，提供了一种便携、离线优先且保护隐私的替代方案，任何有浏览器的人都可以共享和编辑。 默认幻灯片约 560 KB，使用加密盲中继进行协作，确保中继无法看到数据。代码在 GitHub 上以 MIT 许可证发布。

hackernews · starfallg · 7月22日 15:19 · [社区讨论](https://news.ycombinator.com/item?id=49008211)

**背景**: 传统的演示工具如 PowerPoint 需要安装且常依赖云存储。Bento 将整个应用、数据和编辑器打包成一个离线可用的 HTML 文件，利用了 reveal.js 和 DecompressionStream 等 Web 技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49008211">Show HN: Bento - An entire PowerPoint in one HTML file (edit+view+data+collab) | Hacker News</a></li>
<li><a href="https://bento.page/">Bento/Suite — the office suite that fits in a file</a></li>
<li><a href="https://github.com/nyblnet/bento">GitHub - nyblnet/bento · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区称赞 Bento 的创新性和潜力，有人认为它会变得更常见。一位用户报告在大量协作编辑时出现冻结，表明在极端负载下存在性能限制。

**标签**: `#single-file web app`, `#presentation tool`, `#offline-first`, `#collaboration`, `#web development`

---

<a id="item-5"></a>
## [初创公司的 Postgres 生存指南](https://hatchet.run/blog/postgres-survival-guide) ⭐️ 8.0/10

一篇针对初创公司的 PostgreSQL 扩展与优化综合指南已发布，涵盖索引、连接池和常见陷阱。 该指南提供实用的可操作建议，帮助初创公司避免代价高昂的数据库错误并高效扩展，满足了初创社区的关键需求。 该指南强调使用 uuidv7 而非 uuid v4、确定性锁排序以防止死锁，以及使用 EXPLAIN (GENERIC_PLAN)进行查询分析。它还建议避免使用 ORM、使用序列主键，并考虑仅追加数据模型。

hackernews · abelanger · 7月22日 12:36 · [社区讨论](https://news.ycombinator.com/item?id=49005787)

**背景**: PostgreSQL 是一种流行的开源关系型数据库，被许多初创公司使用。扩展它需要仔细的索引、连接管理以及对锁定行为的理解。像 pgBouncer 这样的连接池工具有助于高效管理数据库连接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scalegrid.io/blog/postgresql-connection-pooling-part-1-pros-and-cons/">PostgreSQL Connection Pooling : Part 1 - Pros & Cons</a></li>
<li><a href="https://www.freecodecamp.org/news/postgresql-indexing-strategies/">Advanced Indexing Strategies in PostgreSQL</a></li>
<li><a href="https://tembo.io/docs/getting-started/postgres_guides/postgres-indexing-strategies">Postgres indexing strategies | Tembo Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者提供了有价值的修正和补充，例如优先使用 uuidv7 而非 uuid v4、确定性锁排序以及使用 EXPLAIN (GENERIC_PLAN)。一些人指出缺少备份策略等主题，以及 ORM 误用等组织性陷阱。

**标签**: `#PostgreSQL`, `#startups`, `#database optimization`, `#scaling`

---

<a id="item-6"></a>
## [面试项目隐藏恶意 Git 钩子](https://citizendot.github.io/articles/fake-job-interview-git-hook-malware/) ⭐️ 8.0/10

一名开发者发现，一个带回家的面试项目中包含一个恶意 Git 钩子，该钩子静默执行远程负载，揭露了一个针对求职者的复杂骗局。 这种攻击向量利用了求职者对招聘过程的信任，可能危及许多开发者的系统，凸显了社会工程学与技术恶意软件交付相结合的趋势。 恶意 Git 钩子隐藏在.git/hooks 目录中，在 git commit 时执行，检查主机操作系统并从原始 IP 地址下载负载。文章还提到一个类似的骗局，使用 Visual Studio Code 项目，在打开项目时运行自定义代码。

hackernews · CITIZENDOT · 7月22日 20:33 · [社区讨论](https://news.ycombinator.com/item?id=49013036)

**背景**: Git 钩子是在 Git 工作流程的某些节点自动运行的脚本，例如在提交之前。它们存储在.git/hooks 目录中，可用于自动化，但也可能被滥用于恶意目的。骗子开始将恶意软件嵌入带回家的面试项目中，以感染求职者的机器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/xanderselorm/fake-job-offers-are-turning-github-repos-into-a-trap-5fad">Fake Job Offers Are Turning GitHub Repos Into a Trap - DEV Community</a></li>
<li><a href="https://cybertex.io/how-recruitment-scams-target-developers-through-github-test-tasks/">How Recruitment Scams Target Developers via GitHub | Cybertex</a></li>
<li><a href="https://git-scm.com/docs/githooks">Git - githooks Documentation</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了类似经历，一位用户意识到自己在一个更复杂的攻击中被黑，该攻击涉及一场摄像头关闭的虚假面试。其他人指出，使用原始 IP 地址是一个危险信号，并对 VS Code 项目在打开时运行代码表示担忧，这创造了另一个恶意软件传播途径。

**标签**: `#security`, `#malware`, `#social engineering`, `#job scams`, `#git hooks`

---

<a id="item-7"></a>
## [Anthropic 的 Claude Tag 处理 65% 的产品工程 PR](https://simonwillison.net/2026/Jul/21/cat-and-thariq/#atom-everything) ⭐️ 8.0/10

Simon Willison 与 Anthropic 的 Claude Code 团队进行了一场炉边谈话，透露 Claude Tag 现在处理该团队 65% 的产品工程拉取请求。团队还分享说，Claude Code 的系统提示词减少了 80%，并且对于 Fable 5 等模型，在系统提示词中添加示例已不再是最佳实践。 这些指标表明 Anthropic 内部对 AI 编码代理的信任和成熟度正在增长，显示 AI 可以自主处理大部分日常工程工作。从冗长的系统提示词和负面指令的转变，标志着提示高级模型的新范式。 对 Claude Code 的关键更改仍需人工审查，但团队越来越依赖自动化代码审查来处理产品外层。Anthropic 使用内部称为“ant fooding”的吃狗粮流程，并且只发布那些在员工中显示出用户留存率的功能。

rss · Simon Willison · 7月21日 12:54

**背景**: Claude Code 是 Anthropic 的代理式编码工具，位于终端中，帮助开发者更快地将想法转化为代码。Claude Tag 是一个 Slack 集成，允许用户在话题中 @Claude 以获得实时帮助。Fable 5 是 Anthropic 最新的前沿模型，专为自主知识工作和编码而构建。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI)</a></li>
<li><a href="https://claude.com/product/tag">Claude in Slack: Tag @ Claude in any thread | Claude by Anthropic</a></li>
<li><a href="https://docs.anthropic.com/en/docs/claude-code/overview">Claude Code overview - Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude Code`, `#Anthropic`, `#coding agents`, `#AI engineering`

---

<a id="item-8"></a>
## [美国财政部因 Moonshot AI 模型蒸馏威胁制裁](https://techcrunch.com/2026/07/22/treasury-threatens-sanctions-after-white-house-claims-moonshot-distilled-anthropics-fable/) ⭐️ 8.0/10

美国财政部威胁实施制裁，此前白宫指控中国 AI 初创公司 Moonshot 蒸馏了 Anthropic 的 Fable 模型，加剧了围绕中国开源 AI 模型的紧张局势。 这一事件凸显了围绕 AI 模型蒸馏和开源 AI 日益加剧的地缘政治摩擦，可能影响全球 AI 监管以及开源模型的跨境流动。 模型蒸馏涉及将知识从大型模型转移到小型模型，可用于未经授权复制专有模型。白宫声称 Moonshot 未经许可使用了 Anthropic 的 Fable 模型。

rss · TechCrunch AI · 7月22日 20:49

**背景**: 模型蒸馏是一种机器学习技术，其中较小的“学生”模型从较大的“教师”模型中学习，常用于创建高效的部署模型。Moonshot AI 是一家专注于构建 AGI 基础模型的中国初创公司。Anthropic 的 Fable 模型是用于自主知识工作和编码的最先进 AI 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#geopolitics`, `#open-source AI`, `#model distillation`, `#national security`

---

<a id="item-9"></a>
## [OpenAI 基础设施支出达 7500 亿美元](https://techcrunch.com/2026/07/22/openais-ai-spending-spree-has-ballooned-to-750b/) ⭐️ 8.0/10

OpenAI 宣布计划到 2030 年在 AI 基础设施上支出 7500 亿美元，这一数额相当于瑞典的整个国内生产总值。 这笔巨额投资标志着 AI 军备竞赛的急剧升级，可能重塑全球技术基础设施，并影响其他主要参与者的资本配置方式。 这笔支出涵盖到 2030 年的数据中心、计算硬件和能源资源，反映了 OpenAI 对 AI 计算需求持续指数级增长的押注。

rss · TechCrunch AI · 7月22日 16:13

**背景**: 随着 OpenAI、谷歌和微软等公司竞相构建更大规模的模型，AI 基础设施支出一直在快速增长。训练最先进的模型需要大量的专用芯片集群和巨大的电力消耗。7500 亿美元的数字远超此前估计，凸显了前沿 AI 开发的资本密集型特征。

**标签**: `#OpenAI`, `#AI infrastructure`, `#investment`, `#industry trends`

---

<a id="item-10"></a>
## [数学家仍未找到最快乘法方法](https://www.solidot.org/story?sid=84899) ⭐️ 8.0/10

文章探讨了快速乘法算法的历史和现状，从 Karatsuba 的 O(n^1.585)算法到 Harvey 和 van der Hoeven 猜想的最优 O(n log n)算法，但后者尚未得到正式证明。 理解最快的乘法算法是计算复杂性的基本问题，对密码学、数值计算和算法设计都有影响。寻找最优算法的努力持续推动着理论计算机科学的研究。 Karatsuba 算法通过分治法将乘法复杂度降低到 O(n^1.585)，Python 使用混合方法，当数字大于 630 位十进制数时切换到 Karatsuba 算法。Harvey-van der Hoeven 算法实现了 O(n log n)，但仅在数字极大时才能超越 Karatsuba 算法。

rss · Solidot 奇客 · 7月22日 16:52

**背景**: 乘法算法通过操作次数随位数(n)增长的速度来衡量。传统的竖式乘法复杂度为 O(n^2)。1960 年，Anatoly Karatsuba 发现了一种更快的算法，打破了 O(n^2)的壁垒，引发了对更快方法的探索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Karatsuba_algorithm">Karatsuba algorithm</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multiplication_algorithm">Multiplication algorithm - Wikipedia</a></li>
<li><a href="https://stackoverflow.com/questions/70646578/understanding-harvey-van-der-hoeven-2019-algorithm-huge-integer-multiplicatio">Understanding Harvey & van der Hoeven 2019 algorithm ...</a></li>

</ul>
</details>

**标签**: `#algorithms`, `#computational complexity`, `#mathematics`, `#multiplication`, `#computer science`

---

<a id="item-11"></a>
## [Vera Rubin NVL72 与 GB200 NVL72：推理总拥有成本与架构对比](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-vs-gb200-nvl72-inference) ⭐️ 8.0/10

一项详细分析将 NVIDIA 即将推出的 Vera Rubin NVL72 架构与当前的 GB200 NVL72 进行了对比，重点关注推理总拥有成本（TCO）、每瓦性能和每美元性能。Rubin 架构引入了基于 3 位查找表（LUT）的张量核心和 Feynman SM140 设计，有望显著提升推理效率。 这项对比对于 AI 基础设施规划者至关重要，因为它量化了下一代硬件的潜在成本和性能优势。研究结果可能影响大规模 AI 推理部署的采购决策，特别是针对 MoE 和 DeepSeek-R1 等模型。 Vera Rubin NVL72 配备 72 个 Rubin GPU，提供 3.6 exaFLOPS 的 NVFP4 推理性能和 260 TB/s 的 NVLink 6 带宽，而 GB200 NVL72 配备 72 个 Blackwell GPU，在 MoE 工作负载中吞吐量比 AMD MI355X 高出 28 倍。分析还涵盖了 PyTorch、vLLM 和 OpenAI Triton 的软件改进。

rss · Semianalysis · 7月23日 00:47

**背景**: NVIDIA 的 GPU 架构快速演进以满足 AI 需求。GB200 NVL72 是当前配备 72 个 Blackwell GPU 的机架级系统，而即将推出的 Vera Rubin NVL72 集成了 Vera CPU、Rubin GPU、NVLink 6 等组件。3 位 LUT 张量核心是一种新颖的软硬件协同设计，利用查找表实现高效的低比特 LLM 推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.r3con.co.uk/post/nvidia-unveils-vera-rubin-nvl72-ai-supercomputer-with-massive-performance-leap">Nvidia Unveils Vera Rubin NVL 72 AI Supercomputer With Massive...</a></li>
<li><a href="https://blogs.nvidia.com/blog/vera-rubin/">NVIDIA Vera Rubin Driving Performance Per Watt... | NVIDIA Blog</a></li>
<li><a href="https://www.kad8.com/ai/gb200-nvl72-vs-mi355x-why-systems-win-moe-inference/">GB 200 NVL 72 vs MI355X: Why Systems Win MoE Inference · KAD</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#GPU architecture`, `#AI inference`, `#TCO analysis`, `#hardware`

---

<a id="item-12"></a>
## [Hugging Face 披露 AI 智能体攻击，商业大模型拒绝协助取证](https://t.me/zaihuapd/42701) ⭐️ 8.0/10

Hugging Face 披露了 2026 年 7 月的一起安全事件，攻击者利用自主 AI 智能体框架，通过数据集处理流程中的两处代码执行漏洞入侵内部系统，窃取了内部凭证并横向移动至多个集群。 这是首次公开的自主 AI 智能体用于攻破主流机器学习平台的案例，突显了传统防御可能无法捕获的新型 AI 驱动网络攻击。 该智能体在周末期间执行了数万次操作，窃取了部分内部数据集和服务凭证，但面向公众的模型、数据集及 Spaces 未被篡改；Hugging Face 已修复漏洞、轮换受影响凭证。

telegram · zaihuapd · 7月22日 00:46

**背景**: Hugging Face 是托管机器学习模型、数据集和演示应用（Spaces）的领先平台。自主 AI 智能体是由大语言模型驱动的系统，能够独立规划和执行任务。代码执行漏洞允许攻击者在目标系统上运行任意代码。

**标签**: `#AI security`, `#Hugging Face`, `#cyberattack`, `#AI agent`, `#vulnerability`

---

<a id="item-13"></a>
## [中国科技公司提前招募青少年应对 AI 人才短缺](https://restofworld.org/2026/china-tech-recruiting-teenagers-ai-shortage/) ⭐️ 8.0/10

腾讯、字节跳动和吉利等中国科技公司推出了面向青少年的项目，招募年仅 13 岁的学生进行 AI 培训和提前就业，以应对严重的人才短缺。腾讯的营地面向 13 至 18 岁学生，字节跳动的非营利研究中心每年遴选 30 名 16 至 18 岁学生，吉利则在高中毕业后直接招录并提供与大学毕业生同等的薪酬。 这一趋势标志着 AI 人才管道发展的战略转变，可能重塑中国的教育和就业路径。预计到 2030 年 AI 人才缺口将达 500 万，提前招募可能使中国企业在全球 AI 竞赛中获得竞争优势。 数据显示，2026 年 1 至 5 月 AI 岗位供需比为 3.08 比 1，AI 工程职位同比增长 28.4%。AI 公司 MiniMax 表示年龄已非壁垒，更重视原生智慧与学习能力而非传统资历。

telegram · zaihuapd · 7月22日 04:25

**背景**: 随着 AI 人才需求激增，中国科技公司面临严重的 AI 工程师短缺。美国也有类似项目，如 Palantir 的高中实习计划和谷歌的举措，反映了全球早期人才识别的趋势。这些项目旨在建立长期人才池并跟踪学生成长，同时提升企业品牌形象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MiniMax_(company)">MiniMax (company)</a></li>
<li><a href="https://edutimes.com/news/2025/11/202511285559">[Diagnosing the Breakdown of Universities] Palantir ’s “Post-University”...</a></li>

</ul>
</details>

**标签**: `#AI talent`, `#China tech`, `#talent acquisition`, `#education`, `#AI shortage`

---

<a id="item-14"></a>
## [月之暗面寻求 20 亿美元融资，估值达 300 亿美元](https://t.me/zaihuapd/42706) ⭐️ 8.0/10

月之暗面（Moonshot AI）正寻求至多 20 亿美元的新融资，目标估值 300 亿美元，这是其六个月内启动的第三轮融资，4 月年度经常性收入已达 2 亿美元。 估值在六个月内从 40 亿美元飙升至 300 亿美元，凸显了中国对 AI 聊天机器人和大语言模型的强劲需求，也表明月之暗面在全球竞争的雄心。 该公司还在拆除境外架构以筹备香港上市，并推出了面向知识工作者的通用 AI 代理 Kimi Work。

telegram · zaihuapd · 7月22日 05:10

**背景**: 月之暗面于 2023 年 3 月在北京成立，以其 Kimi 聊天机器人和具有行业领先长上下文能力的大语言模型而闻名。年度经常性收入（ARR）是 SaaS 初创公司的关键指标，代表订阅收入的年化价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi ( chatbot ) - Wikipedia</a></li>
<li><a href="https://www.moonshot.ai/">Welcome to Moonshot AI . Our mission is to seek the optimal...</a></li>
<li><a href="https://trythatllm.com/model-family/moonshot-ai">Moonshot AI | Try That LLM</a></li>

</ul>
</details>

**标签**: `#AI`, `#funding`, `#startup`, `#large language models`, `#valuation`

---

<a id="item-15"></a>
## [微软考虑接入 DeepSeek 以降低 Copilot Cowork 成本](https://t.me/zaihuapd/42710) ⭐️ 8.0/10

微软正探索在几周内将经微调的 DeepSeek V4 或其他开源模型接入其企业 AI 工具 Copilot Cowork，作为比现有 Anthropic 和 OpenAI 模型更低价的备选方案。同时，微软宣布 Copilot Cowork 将改为按实际算力使用量收费，不再提供无限量套餐。 此举标志着企业 AI 采用可能发生转变，微软等主要供应商考虑使用开源模型降低成本，这可能会迫使专有模型提供商调整定价。同时，它也反映了 AI 服务中按使用量计费的重要性日益增加，解决了重度用户推高成本的挑战。 DeepSeek 模型将完全托管于 Azure，确保数据不离开微软云，并受企业安全与合规管控。微软高管指出，部分用户每周执行数百项任务，在无限量计划下导致成本剧增，因此需要改变定价模式。

telegram · zaihuapd · 7月22日 07:18

**背景**: DeepSeek V4 是一系列开源混合专家（MoE）模型，包括 DeepSeek-V4-Pro（总参数 1.6 万亿，激活参数 490 亿）和 DeepSeek-V4-Flash（总参数 2840 亿，激活参数 130 亿），在编码和智能体任务方面表现出色，支持 100 万 token 的上下文窗口。Copilot Cowork 是微软为 Microsoft 365 推出的智能体 AI 助手，于 2026 年 6 月正式发布，采用基于 Copilot Credits 的按使用量计费模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://windowsforum.com/threads/copilot-coworks-usage-pricing-why-agentic-ai-needs-a-meter-deepseek-included.428891/">Copilot Cowork ’s Usage Pricing : Why Agentic AI... | Windows Forum</a></li>
<li><a href="https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-overview-copilot-credits">Usage - Based Billing and Cost Management for Copilot Credits</a></li>
<li><a href="https://unsloth.ai/docs/models/deepseek-v4">DeepSeek - V 4 : How to Run Locally | Unsloth Documentation</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#DeepSeek`, `#AI`, `#Enterprise`, `#Cost Optimization`

---

<a id="item-16"></a>
## [四大 AI 编程代理曝沙箱逃逸漏洞](https://www.bleepingcomputer.com/news/security/cursor-codex-gemini-cli-antigravity-hit-by-sandbox-escapes/) ⭐️ 8.0/10

Pillar Security 研究团队披露，Cursor、OpenAI Codex、Google Gemini CLI 和 Antigravity 四款主流 AI 编程代理存在沙箱逃逸漏洞，攻击者可通过开源仓库中的间接提示注入实现任意代码执行。 该漏洞影响数百万使用这些工具的开发者，攻击者通过工作区文件进行间接提示注入，绕过了传统沙箱保护，暴露了 AI 代理安全中的关键盲区。 攻击利用了主机工具（如 Python 解释器、Git）会自动读取并执行 AI 代理生成的工作区文件这一特性，而这些文件并未被沙箱隔离。厂商已发布修复：Cursor 3.0.0、Codex CLI v0.95.0，但 Google 将 Antigravity 的两项漏洞降级处理，认为需要配合社工攻击。

telegram · zaihuapd · 7月22日 08:08

**背景**: 间接提示注入是一种将恶意指令嵌入 AI 代理读取的数据（如 README 文件）中的技术，导致代理违背用户意图行事。沙箱逃逸漏洞允许攻击者突破受限环境，在主机系统上执行代码。此次披露将两者结合，表明即使 AI 代理在沙箱中运行，其写入的文件仍可能被受信任的主机工具执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prepfast.in/topics/ai-agents/prompt-injection/">Prompt Injection ( Direct & Indirect ) — AI Coding Agents Interview...</a></li>
<li><a href="https://devops.com/mozilla-shows-the-danger-of-indirect-prompt-injections-in-ai-coding-agents/">Mozilla Shows the Danger of Indirect Prompt Injections in AI Coding ...</a></li>
<li><a href="https://www.ox.security/blog/the-aftermath-of-cve-2025-4609-critical-sandbox-escape-leaves-1-5m-developers-vulnerable/">The aftermath of CVE-2025-4609: Critical Sandbox Escape Leaves...</a></li>

</ul>
</details>

**标签**: `#AI security`, `#sandbox escape`, `#prompt injection`, `#vulnerability disclosure`, `#developer tools`

---

<a id="item-17"></a>
## [特朗普或限制美企使用中国开放权重 AI 模型](https://t.me/zaihuapd/42715) ⭐️ 8.0/10

据 Axios 报道，特朗普政府正考虑出台新限制措施，以阻止美国企业使用像 Kimi K3 这样物美价廉的中国开放权重 AI 模型，原因是该模型表现强劲。 这一政策转变可能割裂全球 AI 生态，增加美国企业成本，并加速中美 AI 供应链脱钩。 限制措施可能不是硬性封禁，而是通过采购规则、实体清单威胁和舆论压力进行软性封锁。Kimi K3 是一个 2.8 万亿参数、拥有 100 万 token 上下文窗口的开放权重模型。

telegram · zaihuapd · 7月22日 13:30

**背景**: 开放权重模型公开其训练后的参数，允许任何人下载和运行，但与同时包含训练代码和数据的完全开源模型不同。像 Kimi K3 这样的中国开放权重模型近期在性能上已接近美国同类产品，且成本更低。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://promtable.com/glossary/open-weight-model">Open - weight model — Definition , when to use, and... | Promtable</a></li>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-what-we-finally-opened-bonnet-nicolas-pistorio-n3ulf">Open - weight AI : what if we finally opened the bonnet ?</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#geopolitics`, `#open-weight models`, `#Kimi K3`, `#US-China tech`

---