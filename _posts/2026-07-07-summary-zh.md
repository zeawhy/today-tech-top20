---
layout: default
title: "Horizon Summary: 2026-07-07 (ZH)"
date: 2026-07-07
lang: zh
---

> 从 38 条内容中筛选出 15 条重要资讯。

---

1. [欧盟议会推进聊天控制法案二读](#item-1) ⭐️ 9.0/10
2. [MIRA：用于火箭联盟的 50 亿参数多人世界模型](#item-2) ⭐️ 9.0/10
3. [Anthropic 发布 Claude Sonnet 5，代理能力更强](#item-3) ⭐️ 9.0/10
4. [Januscape：潜伏 16 年的 KVM 虚拟机逃逸漏洞影响 Intel 和 AMD](#item-4) ⭐️ 9.0/10
5. [微软裁掉 id Software 引擎团队](#item-5) ⭐️ 8.0/10
6. [sqlite-utils 4.0 新增数据库模式迁移功能](#item-6) ⭐️ 8.0/10
7. [腾讯发布 Hy3：295B MoE 模型，采用 Apache 2.0 许可](#item-7) ⭐️ 8.0/10
8. [英伟达债务支持推动 AI 基础设施三要素](#item-8) ⭐️ 8.0/10
9. [可微分光线追踪用于无线电传播建模的博士论文](#item-9) ⭐️ 8.0/10
10. [Mozilla CTO 就开源 AI 报告举行 AMA](#item-10) ⭐️ 8.0/10
11. [马斯克解散 xAI，更名为 SpaceXAI](#item-11) ⭐️ 8.0/10
12. [中国拟投 2 万亿元建设全国算力网络](#item-12) ⭐️ 8.0/10
13. [Windows 11 漏洞可吞噬高达 513 GB 存储空间](#item-13) ⭐️ 8.0/10
14. [DeepSeek 自研 AI 芯片以减少对英伟达和华为的依赖](#item-14) ⭐️ 8.0/10
15. [中国拟限制顶尖 AI 模型出口](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [欧盟议会推进聊天控制法案二读](https://www.heise.de/en/news/Showdown-in-Strasbourg-The-unexpected-return-of-Chat-Control-1-0-11356680.html) ⭐️ 9.0/10

欧盟议会在二读中通过了聊天控制法案的第一轮，利用程序性策略可能绕过反对意见，并为大规模监控开创先例。 这一进展威胁全球数字隐私和加密，因为该法律可能强制扫描私人信息，影响所有欧盟公民，并可能在其他地区引发类似法规。 在二读中，修正案需要绝对多数 361 票，而另一方只需出席议员的简单多数，这给支持者带来了战术优势，因为许多议员已在暑假前离开。

hackernews · miroljub · 7月7日 15:16 · [社区讨论](https://news.ycombinator.com/item?id=48819008)

**背景**: 聊天控制指欧盟立法，要求消息平台扫描私人通信中的非法内容，如儿童性虐待材料。批评者认为这破坏了端到端加密和隐私权，欧洲法院此前已裁定大规模监控措施违法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.flokinet.is/2025/10/09/eu-chat-control-mass-surveillance-law/">EU Chat Control : A dangerous step towards mass surveillance</a></li>
<li><a href="https://aiespionage.net/cybersecurity/eu-council-forces-chat-control-via-fast-track/">EU Council Forces Chat Control Via Fast-track - AI Espionage</a></li>
<li><a href="https://www.politico.eu/article/data-retention-europe-mass-surveillance/">Europe's state of mass surveillance - Politico.eu</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了强烈反对，强调程序操纵和民主担忧。用户指出，该策略利用了暑假前出席率低的情况，并警告非欧盟国家也可能采用类似的监控法律。

**标签**: `#privacy`, `#EU legislation`, `#surveillance`, `#encryption`, `#politics`

---

<a id="item-2"></a>
## [MIRA：用于火箭联盟的 50 亿参数多人世界模型](https://www.reddit.com/r/MachineLearning/comments/1upofuw/mira_multiplayer_interactive_world_models_trained/) ⭐️ 9.0/10

General Intuition、Kyutai 和 Epic Games 发布了 MIRA，这是一个基于 10,000 小时合成火箭联盟数据训练的 50 亿参数多人交互世界模型，能够在单个 NVIDIA B200 GPU 上以 20 FPS 模拟 4 人游戏。 MIRA 是首个针对高度动态、复杂物理环境的多人世界模型，实现了实时交互模拟，可能推动游戏 AI、强化学习和多智能体系统研究。 该模型采用潜在扩散架构，根据所有四名玩家的动作生成视频帧，团队还发布了可玩演示、技术报告和 1,000 小时的四人游戏数据集。

reddit · r/MachineLearning · /u/MasterScrat · 7月7日 07:59

**背景**: 世界模型是一种神经网络，能从数据中学习模拟环境动态，使智能体能够进行规划和推理。火箭联盟是一款快节奏的车辆足球游戏，具有复杂的物理特性，是交互式模拟的挑战性测试平台。B200 是 NVIDIA 的 Blackwell GPU，拥有 2080 亿个晶体管和 FP4 Tensor Core，专为 AI 推理和训练设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/mira-wm/mira">MIRA: Multiplayer Interactive World Models with ... - GitHub</a></li>
<li><a href="https://arxiv.org/abs/2607.05352">[2607.05352] Multiplayer Interactive World Models with ...</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/dgx-b200/">DGX B200: The Foundation for Your AI Factory | NVIDIA</a></li>

</ul>
</details>

**标签**: `#world models`, `#reinforcement learning`, `#multiplayer simulation`, `#Rocket League`, `#open-source`

---

<a id="item-3"></a>
## [Anthropic 发布 Claude Sonnet 5，代理能力更强](https://t.me/zaihuapd/42404) ⭐️ 9.0/10

Anthropic 发布了 Claude Sonnet 5，称其是迄今代理能力最强的 Sonnet 模型，能够规划、使用浏览器和终端等工具并自主运行。它在推理、工具使用、编码和知识工作上优于 Sonnet 4.6，性能接近 Opus 4.8，但价格更低。 此次发布标志着高性能代理 AI 变得更易获取和负担得起，可能加速 AI 代理在实际工作流程中的采用。具有竞争力的定价和增强的能力可能促使其他 AI 提供商改进其产品。 Claude Sonnet 5 即日起面向所有套餐开放，并成为 Free 和 Pro 层的默认模型。在 Claude Platform 上，截至 2026 年 8 月 31 日的限时价格为每百万输入 token 2 美元、每百万输出 token 10 美元，API 模型标识为 claude-sonnet-4-5。

telegram · zaihuapd · 7月7日 09:02

**背景**: Anthropic 的 Claude 模型系列包括 Sonnet（中端，平衡速度和能力）和 Opus（高端，能力最强）。代理 AI 指能够自主规划并使用工具执行任务的模型。Sonnet 5 基于 Sonnet 4.6 的混合推理方法，在代理场景中降低了不良行为率，安全性有所提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-sonnet-5">Introducing Claude Sonnet 5 \ Anthropic</a></li>
<li><a href="https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/">Anthropic launches Claude Sonnet 5 as a cheaper way to run agents | TechCrunch</a></li>
<li><a href="https://claude.com/pricing">Plans & Pricing | Claude by Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#LLM`, `#agentic AI`

---

<a id="item-4"></a>
## [Januscape：潜伏 16 年的 KVM 虚拟机逃逸漏洞影响 Intel 和 AMD](https://github.com/V4bel/Januscape) ⭐️ 9.0/10

安全研究人员公开了 Januscape（CVE-2026-53359），这是首个同时影响 Intel 和 AMD 平台的 KVM/x86 虚拟机逃逸漏洞，并发布了概念验证代码。该漏洞是 shadow MMU 中的 use-after-free 缺陷，允许客户机崩溃或逃逸至宿主机内核。 该漏洞打破了多租户 KVM 宿主机的隔离边界，威胁到云服务提供商及所有使用 KVM 虚拟化的环境。其长达 16 年的潜伏期和跨平台影响使其成为有史以来最重大的 KVM 安全问题之一。 该漏洞存在于 KVM 在 Intel 和 AMD 平台上共享的 shadow MMU 代码中，影响范围从 2010 年持续到 2026 年 6 月。它曾被用作 Google kvmCTF 竞赛中的 0-day 攻击，在 RHEL 等发行版中，本地普通用户还可利用该漏洞提权至 root。

telegram · zaihuapd · 7月7日 10:14

**背景**: KVM（基于内核的虚拟机）是 Linux 内核模块，可将宿主机转变为虚拟机监控器，允许多个虚拟机（客户机）运行。shadow MMU 是管理客户机内存地址转换的组件；use-after-free 漏洞发生在程序访问已释放的内存时，可能允许攻击者破坏数据或执行任意代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/V4bel/Januscape">GitHub - V4bel/Januscape</a></li>
<li><a href="https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html">16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel...</a></li>
<li><a href="https://threat-modeling.com/cve-2026-53359-januscape-linux-kvm-vm-escape-intel-amd/">CVE-2026-53359 'Januscape': 16-Year-Old Linux KVM Guest-to ...</a></li>

</ul>
</details>

**标签**: `#security`, `#virtualization`, `#KVM`, `#vulnerability`, `#cloud`

---

<a id="item-5"></a>
## [微软裁掉 id Software 引擎团队](https://gamefromscratch.com/microsoft-fire-idtech-team-at-id-software/) ⭐️ 8.0/10

微软裁掉了 id Software 整个 idTech 引擎团队，实质上终止了内部专有引擎 idTech 的开发，标志着转向使用 Unreal Engine 等第三方引擎。 此举进一步巩固了 Epic Games 旗下 Unreal Engine 在游戏引擎市场的垄断地位，减少了竞争，可能抑制创新。同时，这也引发了对 id Software 开源遗产保护的担忧，因为许多经典 idTech 引擎此前已由 John Carmack 开源。 裁员涉及负责 idTech 引擎的团队，该引擎曾驱动《毁灭战士》和《雷神之锤》等系列。微软尚未正式回应，但此举与游戏发行商放弃自研引擎、转向广泛采用的第三方解决方案的总体趋势一致。

hackernews · bauc · 7月7日 15:33 · [社区讨论](https://news.ycombinator.com/item?id=48819244)

**背景**: id Software 是传奇游戏开发商，以 idTech 等引擎开创了第一人称射击游戏。历史上，id 联合创始人 John Carmack 曾将许多引擎以 GPL 协议开源，促进了技术共享文化。idTech 引擎曾用于内部开发及外部授权，例如《狂怒》和《德军总部：新秩序》。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Id_tech_5_engine">Id tech 5 engine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Id_Software">id Software - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了失望，有人称这是将垄断拱手让给 Epic Games 的企业失误。还有人建议微软应开源最新的 idTech 引擎以纪念 Carmack 的遗产。少数怀疑者指出，文章缺乏整个引擎团队被裁的具体证据。

**标签**: `#game engines`, `#Microsoft`, `#id Software`, `#industry consolidation`, `#open source`

---

<a id="item-6"></a>
## [sqlite-utils 4.0 新增数据库模式迁移功能](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything) ⭐️ 8.0/10

sqlite-utils 4.0 是自 2020 年以来的首个大版本更新，新增了数据库模式迁移、通过新的 db.atomic() 方法实现的嵌套事务，以及对复合外键的支持。 此版本显著增强了 sqlite-utils 作为 SQLite 数据库管理工具的能力，使得安全地应用模式变更并跟踪迁移历史变得更加容易，这对生产数据库至关重要。 迁移使用 sqlite-utils 库在 Python 文件中定义，利用强大的 table.transform() 方法，该方法实现了 SQLite 推荐的创建临时表、复制数据并重命名的模式。此版本还包含升级指南中详述的破坏性变更。

rss · Simon Willison · 7月7日 19:32

**背景**: sqlite-utils 是一个用于创建和操作 SQLite 数据库的 Python 库和命令行工具。模式迁移允许开发者对数据库模式变更进行版本控制并增量应用，这是 sqlite-utils 之前缺失的功能。SQLite 的 ALTER TABLE 功能有限，因此 table.transform() 通过用所需模式重建表来提供一种变通方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sqlite-utils.datasette.io/en/latest/migrations.html">Database migrations - sqlite - utils</a></li>
<li><a href="https://deepwiki.com/simonw/sqlite-utils/3.5-schema-modification">Schema Modification | simonw/ sqlite - utils | DeepWiki</a></li>
<li><a href="https://www.sqlite.org/foreignkeys.html">SQLite Foreign Key Support</a></li>

</ul>
</details>

**标签**: `#sqlite`, `#python`, `#database`, `#migrations`, `#open source`

---

<a id="item-7"></a>
## [腾讯发布 Hy3：295B MoE 模型，采用 Apache 2.0 许可](https://simonwillison.net/2026/Jul/6/hy3/#atom-everything) ⭐️ 8.0/10

腾讯发布了 Hy3，一个 295B 参数的混合专家（MoE）模型，具有 21B 活跃参数，采用 Apache 2.0 许可证。该模型性能优于同类尺寸模型，并可媲美参数规模大 2-5 倍的旗舰开源模型。 此次发布通过提供一个高效且许可宽松的模型，与规模大得多的专有系统竞争，显著推动了开源 AI 的发展。它降低了开发者和研究人员获取最先进语言模型能力的门槛。 完整模型在 Hugging Face 上为 598GB，FP8 量化版本为 300GB，支持 256K 上下文长度。该模型在 OpenRouter 上免费提供至 2026 年 7 月 21 日。

rss · Simon Willison · 7月6日 23:57

**背景**: 混合专家（MoE）是一种架构，每次输入仅激活部分参数，从而以较低计算成本实现高容量。多令牌预测（MTP）是一种技术，模型同时预测多个未来令牌，提高训练效率和推理速度。FP8 量化通过以 8 位浮点格式存储权重来减小模型大小和内存使用，使部署更加实用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/deepseek-ai/DeepSeek-V3/4.4-multi-token-prediction-(mtp)">Multi-Token Prediction ( MTP ) | deepseek-ai/DeepSeek-V3 | DeepWiki</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#large language model`, `#Mixture-of-Experts`, `#Tencent`

---

<a id="item-8"></a>
## [英伟达债务支持推动 AI 基础设施三要素](https://newsletter.semianalysis.com/p/nvidia-gpu-debt-backstop-unleashes) ⭐️ 8.0/10

英伟达正通过债务支持策略推动 Neocloud 和 AI 基础设施的发展，预计到 2029 年 AI 债务将超过 7 万亿美元。 这一金融创新拓宽了 AI 算力的获取渠道，可能重塑云计算格局并加速各行业对 AI 的采用。 “三要素”包括资本、承购协议和数据中心容量；英伟达的支持帮助 Neocloud 获得资金和超大规模合同之外的承购需求。

rss · Semianalysis · 7月6日 21:53

**背景**: Neocloud 是 GPU 即服务提供商，为 AI 工作负载提供高性能计算，区别于传统的基于 CPU 的云服务。它们在获得融资和数据中心空间方面面临挑战，英伟达的支持旨在缓解这些问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/nvidia-gpu-debt-backstop-unleashes">Nvidia GPU Debt Backstop Unleashes the AI Project Trinity: Capital, Offtake and Datacenters</a></li>
<li><a href="https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-evolution-of-neoclouds-and-their-next-moves">Neoclouds’ challenges and next moves | McKinsey</a></li>
<li><a href="https://www.zayo.com/resources/what-neoclouds-are-and-why-they-matter-to-enterprises/">What Neoclouds Are and Why They Matter to Enterprises - Zayo</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论可能讨论 AI 债务的规模以及这种融资模式的可持续性，一些人质疑债务泡沫的风险。

**标签**: `#Nvidia`, `#AI infrastructure`, `#cloud computing`, `#AI financing`, `#datacenters`

---

<a id="item-9"></a>
## [可微分光线追踪用于无线电传播建模的博士论文](https://www.reddit.com/r/MachineLearning/comments/1upvkp5/phd_thesis_on_differentiable_ray_tracing_for/) ⭐️ 8.0/10

一篇博士论文提出了用于无线电传播建模的可微分光线追踪，通过 JAX 集成自动微分，计算物理环境中的精确梯度，从而解决逆问题并训练机器学习模型。 这项工作将无线电传播模拟与机器学习联系起来，为下一代无线设计（如 6G）提供了新工具，其中精确的信道建模和优化至关重要。 论文以教科书形式组织，分为三部分：物理基础、算法核心（包括 GPU 加速路径追踪和不连续性平滑技术）以及实际应用（如信道建模和材料校准）。

reddit · r/MachineLearning · /u/jeertmans · 7月7日 13:45

**背景**: 无线电传播建模预测无线电波在环境中的传播方式，对无线网络规划至关重要。可微分光线追踪扩展了传统光线追踪，允许通过模拟计算梯度，从而实现优化和机器学习集成。JAX 是一个支持自动微分的高性能数值计算库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/jeertmans/DiffeRT2d">GitHub - jeertmans/DiffeRT2d: 2D Toolbox for Differentiable ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Radio_propagation">Radio propagation - Wikipedia</a></li>
<li><a href="https://docs.jax.dev/en/latest/automatic-differentiation.html">Automatic differentiation — JAX documentation</a></li>

</ul>
</details>

**社区讨论**: 作者参与了技术讨论，强调了使用 jaxtyping、equinox 和 optimistix 等 JAX 包，并对 Patrick Kidger 的启发表示感谢。社区对 JAX 中的可微分模拟和光线追踪表现出兴趣。

**标签**: `#differentiable ray tracing`, `#radio propagation`, `#automatic differentiation`, `#machine learning`, `#wireless communications`

---

<a id="item-10"></a>
## [Mozilla CTO 就开源 AI 报告举行 AMA](https://www.reddit.com/r/MachineLearning/comments/1upxdvc/raffi_krikorian_cto_mozilla_ama_on_the_state_of/) ⭐️ 8.0/10

Mozilla 首席技术官 Raffi Krikorian 将于 2026 年 7 月 14 日主持一场 AMA，讨论首份《开源 AI 现状》报告，内容涵盖隐性成本、企业采用、中国效应和开发者信任。 这场 AMA 提供了一个难得的机会，可以直接听取主要开源倡导者关于部署开源 AI 的实际挑战，这可能影响企业战略和开发者工具选择。 该报告基于对 950 多名开发者的调查，将于 2026 年 7 月 14 日发布。关键主题包括“免费”模型的隐性成本、中国效应，以及“智能体框架”概念——真正的竞争现在已转移到这一层面。

reddit · r/MachineLearning · /u/raffikrikorian · 7月7日 14:51

**背景**: 像 Llama 和 Mistral 这样的开源 AI 模型已经流行起来，但在生产环境中运行它们通常会产生基础设施和维护方面的隐性成本。“智能体框架”指的是围绕模型的一层工具和编排，它决定了模型的行为，差异化正越来越多地发生在这个层面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.startuphub.ai/ai-news/ai-research/2026/mozilla-ai-future-the-open-source-counter-manifesto">Mozilla AI Future: The Open Source Counter-Manifesto | StartupHub.ai</a></li>
<li><a href="https://betanews.com/article/state-of-mozilla-report-outlines-an-alternative-vision-for-ai/">State of Mozilla report outlines an alternative vision for AI - BetaNews</a></li>
<li><a href="https://www.linkedin.com/pulse/what-agentic-harness-why-serious-ai-builders-need-one-sharma-9k41e">What Is an Agentic Harness - And Why Serious AI Builders Need One</a></li>

</ul>
</details>

**标签**: `#open source AI`, `#Mozilla`, `#enterprise AI`, `#developer trust`, `#AI costs`

---

<a id="item-11"></a>
## [马斯克解散 xAI，更名为 SpaceXAI](https://x.com/i/status/2074214064746832060) ⭐️ 8.0/10

埃隆·马斯克宣布解散独立公司 xAI，将其更名为 SpaceXAI 并并入 SpaceX。这一变化首次出现在与 Anthropic 的计算合作公告中，该公司自称 SpaceXAI。 此次重组将马斯克的 AI 工作整合到 SpaceX 旗下，可能加速 AI 在太空探索及其他 SpaceX 项目中的发展。这也标志着 AI 行业格局的重大转变，一家重要的独立 AI 初创公司成为航天公司的子公司。 SpaceXAI 保留了 xAI 的旗舰产品，包括 Grok 聊天机器人和社交网络 X（2025 年 3 月收购），以及 Colossus 超级计算机和数据中心业务。SpaceX 于 2026 年 2 月完成收购，此前 xAI 是一家成立于 2023 年的独立公司。

telegram · zaihuapd · 7月7日 02:30

**背景**: xAI 由埃隆·马斯克于 2023 年创立，是一家专注于构建人工智能以加速科学发现的 AI 公司。其旗舰产品 Grok 是一个与社交网络 X 集成的生成式 AI 聊天机器人。解散并更名为 SpaceXAI 反映了马斯克将其 AI 企业集中到 SpaceX 内部的战略，利用 AI 实现与太空相关的目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/XAI_(company)">XAI (company)</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceXAI">SpaceXAI</a></li>
<li><a href="https://x.ai/company">Company: Accelerating Scientific Discovery | SpaceXAI</a></li>

</ul>
</details>

**标签**: `#Elon Musk`, `#xAI`, `#SpaceX`, `#AI`, `#corporate restructuring`

---

<a id="item-12"></a>
## [中国拟投 2 万亿元建设全国算力网络](https://t.me/zaihuapd/42399) ⭐️ 8.0/10

中国计划未来五年投入约 2 万亿元（2950 亿美元），建设全国互联数据中心网络，优先采用华为等本土供应商的 AI 芯片，以减少对英伟达、AMD 等美企的依赖。 这一巨额投资凸显了中国在 AI 基础设施上实现自主的战略决心，可能重塑全球半导体和云计算格局。该计划旨在将分散的区域算力资源整合为统一网络，让企业和公共部门更易获得高性能计算。 该计划是北京“六网”基础设施计划的关键一环，要求 AI 芯片国产化率至少达到 80%。中国电信、联通等国有电信运营商已推出“token 套餐”，把算力像移动数据一样打包销售，为大规模 AI 应用铺路。

telegram · zaihuapd · 7月7日 04:45

**背景**: 中国的“六网”计划涵盖水网、电网、算力网、新型通信网、地下管网和物流网，旨在构建现代化基础设施体系。算力网部分旨在通过高速网络连接全国数据中心，实现资源高效共享。基于 token 的算力定价是一种新兴模式，将计算资源抽象为可计量单位，类似于数据套餐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gov.cn/lianbo/202605/content_7070126.htm">统筹建设、动态推进“六张网” - 中国政府网</a></li>
<li><a href="https://www.sohu.com/a/994678899_122316869">7万亿新基建工程全面启动：国家发改委详解"六张网"投资战略</a></li>
<li><a href="https://news.cctv.com/2026/07/05/ARTIaXH4SWCOXlyO3gvy610Z260705.shtml">“六张网”构建现代化基础设施体系_新闻频道_央视网 (cctv.com)</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#China tech policy`, `#semiconductors`, `#cloud computing`, `#national strategy`

---

<a id="item-13"></a>
## [Windows 11 漏洞可吞噬高达 513 GB 存储空间](https://www.windowslatest.com/2026/07/06/microsoft-admits-a-windows-11-bug-is-eating-up-to-500gb-of-storage-verify-if-you-are-affected/) ⭐️ 8.0/10

微软已确认 Windows 11 的 Capability Access Manager 存在一个漏洞，导致 CapabilityAccessManager.db-wal 文件膨胀至 513 GB。修复程序预计将在 2026 年 7 月累积更新中推出，2026 年 6 月已发布可选预览更新 KB5095093。 该漏洞会静默消耗大量磁盘空间，影响众多 Windows 11 用户，可能导致系统变慢或空间不足错误。此问题凸显了系统服务中数据库日志管理的重要性。 该漏洞涉及 Capability Access Manager 数据库的预写日志（WAL）文件，该文件未能合并回主数据库。停止 Capability Access Manager 服务（camsvc）可暂时阻止文件增长，但可能导致 Wi-Fi/网络问题。

telegram · zaihuapd · 7月7日 06:34

**背景**: Capability Access Manager 用于记录哪些应用使用了摄像头、麦克风和位置等隐私敏感功能。它使用 SQLite 数据库并采用 WAL 模式，更改首先写入 .wal 文件以提高性能和崩溃安全性。正常情况下，.wal 文件会定期检查点合并到主数据库中，但一个漏洞阻止了检查点操作，导致文件无限增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/answers/questions/5815087/capabilityaccessmanager-is-devouring-my-hard-drive">CapabilityAccessManager is devouring my hard drive ...</a></li>
<li><a href="https://techcommunity.microsoft.com/discussions/windows11/fix-for-capabilityaccessmanager-db-wal-growing-huge-in-windows-11/4524594">Fix for CapabilityAccessManager.db-wal Growing Huge in ...</a></li>
<li><a href="https://www.thewindowsclub.com/capability-access-manager-taking-up-storage-in-windows-11">Capability Access Manager taking up storage in Windows 11</a></li>

</ul>
</details>

**标签**: `#Windows 11`, `#bug`, `#storage`, `#Microsoft`, `#privacy`

---

<a id="item-14"></a>
## [DeepSeek 自研 AI 芯片以减少对英伟达和华为的依赖](https://www.reuters.com/world/china/chinas-deepseek-developing-its-own-ai-chip-sources-say-2026-07-07/) ⭐️ 8.0/10

中国 AI 初创公司 DeepSeek 正在自研专注于推理任务的 AI 芯片，旨在减少对英伟达和华为芯片的依赖。该计划始于约一年前，目前仍处于早期阶段，DeepSeek 正在招募芯片设计工程师，并与代工厂和存储公司接洽。 此举可能重塑中国的 AI 硬件格局，因为 DeepSeek 试图规避美国对先进英伟达芯片的出口管制。如果成功，将减少对国内外供应商的依赖，可能加速中国半导体自给自足的进程。 该芯片专为推理阶段设计，即训练好的模型为用户生成回答的环节，而非模型训练。DeepSeek 此前依赖英伟达 H800 和华为昇腾芯片，创始人梁文锋在 2024 年一次罕见采访中承认芯片管制是公司面临的挑战。

telegram · zaihuapd · 7月7日 11:08

**背景**: 自 2022 年 10 月以来，美国出口管制限制了中国公司获取英伟达顶级 GPU 以及 SK 海力士、美光和三星的高带宽内存（HBM）堆栈。英伟达曾为中国市场推出降级版芯片如 A800 和 H800，但这些后来也被限制。华为昇腾系列已成为国内替代方案，但性能差距依然存在。随着 AI 应用规模化，推理芯片变得越来越重要，推理阶段的计算成本积累最快。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/world/china/chinas-deepseek-developing-its-own-ai-chip-sources-say-2026-07-07/">EXCLUSIVE: China's DeepSeek developing its own AI chip ...</a></li>
<li><a href="https://www.usnews.com/news/top-news/articles/2026-07-07/exclusive-chinas-deepseek-developing-its-own-ai-chip-sources-say">Exclusive-China's DeepSeek Developing Its Own AI Chip ...</a></li>
<li><a href="https://www.edgen.tech/news/post/deepseek-builds-inference-chip-in-7b-push-to-cut-nvidia-reliance">DeepSeek builds inference chip in $7B push to cut Nvidia reliance</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#DeepSeek`, `#semiconductors`, `#China tech`, `#export controls`

---

<a id="item-15"></a>
## [中国拟限制顶尖 AI 模型出口](https://www.reuters.com/world/beijing-is-looking-curbing-overseas-access-chinas-top-ai-models-sources-say-2026-07-07/) ⭐️ 8.0/10

中国商务部已召集阿里巴巴、字节跳动和智谱 AI 等企业开会，讨论限制国内最先进 AI 模型（包括尚未发布的模型）向海外提供访问。 此举可能重塑全球 AI 格局，限制中国 AI 模型的可用性，可能加速中美 AI 生态系统的脱钩。 限制可能仅适用于未来发布的模型，仍在讨论中，最终政策尚未确定。会议还考虑将 AI 技术泄露列为国家安全犯罪，并限制外资投资中国 AI 初创企业。

telegram · zaihuapd · 7月7日 11:42

**背景**: 中国一直在快速发展 AI 能力，智谱 AI 等公司已开发出与 OpenAI 竞争的大模型。美国已对华实施先进 AI 芯片出口管制，中国的这一举措可能是保护其技术资产的对应措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.voachinese.com/a/china-ai-ecosystem-20250215/7975051.html">一文了解 中 国 AI 江湖的核心玩家及美 中 AI 竞逐格局 | 美 国 之音</a></li>
<li><a href="https://www.bbc.com/zhongwen/articles/c99n7x5jrygo/simp">人工智能：从聊天机器人到玩具， AI ... - BBC News 中 文</a></li>

</ul>
</details>

**标签**: `#AI`, `#regulation`, `#China`, `#technology policy`, `#export control`

---