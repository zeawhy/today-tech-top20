---
layout: default
title: "Horizon Summary: 2026-07-03 (ZH)"
date: 2026-07-03
lang: zh
---

> 从 41 条内容中筛选出 14 条重要资讯。

---

1. [美国禁止人口普查数据使用差分隐私](#item-1) ⭐️ 9.0/10
2. [弗吉尼亚州禁止出售精确地理位置数据](#item-2) ⭐️ 8.0/10
3. [crustc：将整个 Rust 编译器翻译为 C 语言](#item-3) ⭐️ 8.0/10
4. [Podman v6.0.0 发布：Quadlet 改进与自动数据库迁移](#item-4) ⭐️ 8.0/10
5. [Immich 3.0 发布：自托管照片管理重大更新](#item-5) ⭐️ 8.0/10
6. [Postgres 事务：分布式系统的超能力](#item-6) ⭐️ 8.0/10
7. [理解才能参与：AI 编程协作的关键](#item-7) ⭐️ 8.0/10
8. [ECTC 2026 综述：EMIB-T、定制 HBM、HBM4、微流冷却和光子互连](#item-8) ⭐️ 8.0/10
9. [Hierarchos：232M 参数循环记忆增强模型训练成功](#item-9) ⭐️ 8.0/10
10. [证监会同意宇树科技科创板 IPO 注册](#item-10) ⭐️ 8.0/10
11. [花旗禁用 GPT-5.5，AI 成本飙升](#item-11) ⭐️ 8.0/10
12. [PS3 商店 2027 年关闭，档案员紧急抢救游戏](#item-12) ⭐️ 8.0/10
13. [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](#item-13) ⭐️ 8.0/10
14. [华为发布 Atlas 350 加速卡，性能达 H20 的 2.87 倍](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [美国禁止人口普查数据使用差分隐私](https://scottaaronson.blog/?p=9902) ⭐️ 9.0/10

2026 年 6 月 4 日，美国商务部长发布了 DAO 216-26 号指令，禁止在人口普查局的所有统计产品中使用噪声注入和差分隐私，将披露避免限制为仅使用粗化方法。 该指令移除了人口普查数据中数学上严格的隐私保护，增加了个人重新识别的风险，并可能降低公众对数据发布的信任。 该禁令涵盖了所有形式的噪声注入，包括 2020 年人口普查中使用的差分隐私。只有粗化方法（如四舍五入或分箱）仍被允许用于披露避免。

hackernews · flowercalled · 7月3日 00:01 · [社区讨论](https://news.ycombinator.com/item?id=48768992)

**背景**: 差分隐私是一种数学框架，通过向数据集添加受控噪声来防止个人重新识别，同时保持统计准确性。人口普查局在 2020 年人口普查中采用了该方法以增强隐私保护。批评者认为噪声注入会扭曲小区域数据，而支持者则认为它对现代隐私保护至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bea.gov/help/faq/1490">Why didn’t BEA use noise infusion as its statistical disclosure limitation method in its June 10, 2026, news release on “New Foreign Direct Investment in the United States, 2025’’? | U.S. Bureau of Economic Analysis (BEA)</a></li>
<li><a href="https://desfontain.es/blog/banning-noise.html">Banning noise will be a disaster for statistical data products - Ted is writing things</a></li>
<li><a href="https://www.census.gov/programs-surveys/decennial-census/decade/2020/planning-management/process/disclosure-avoidance/differential-privacy.html">Understanding Differential Privacy</a></li>

</ul>
</details>

**社区讨论**: 评论者对指令背后的政治动机表示困惑，一些人推测这可能是出于对统计方法的意识形态反对。其他人呼吁联系立法者反对该禁令，并指出原帖中缺少直接行动链接。

**标签**: `#privacy`, `#differential privacy`, `#US Census`, `#policy`, `#data security`

---

<a id="item-2"></a>
## [弗吉尼亚州禁止出售精确地理位置数据](https://www.hunton.com/privacy-and-cybersecurity-law-blog/virginia-bans-sale-of-geolocation-data) ⭐️ 8.0/10

2026 年 4 月 13 日，弗吉尼亚州州长阿比盖尔·斯潘伯格签署了 S.B. 388 法案，修订《弗吉尼亚消费者数据保护法》，禁止出售精确地理位置数据，该禁令于 2026 年 7 月 1 日生效。 这使得弗吉尼亚州成为美国第三个禁止出售精确地理位置数据的州，反映了隐私监管的日益增长趋势，可能影响其他州并对数据经纪商和科技公司产生冲击。 该法律将精确地理位置数据定义为识别个人或设备位置精度在 1750 英尺（约 533 米）以内的信息，比联邦定义的 1000 米更为严格。禁令适用于出售此类数据，但公司仍可内部收集和使用。

hackernews · toomuchtodo · 7月2日 21:03 · [社区讨论](https://news.ycombinator.com/item?id=48767347)

**背景**: 精确地理位置数据可能泄露个人敏感信息，如家庭住址、就医记录或政治倾向。许多公司通过移动应用收集此类数据并出售给数据经纪商，引发隐私担忧。《弗吉尼亚消费者数据保护法》已赋予消费者相关权利，此次修订增加了对出售地理位置数据的明确禁令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hunton.com/privacy-and-cybersecurity-law-blog/virginia-bans-sale-of-geolocation-data">Virginia Bans Sale of Geolocation Data</a></li>
<li><a href="https://advocacy.consumerreports.org/press_release/virginia-governor-signs-landmark-location-privacy-bill-into-law/">Virginia Governor signs landmark location privacy bill into law</a></li>
<li><a href="https://www.regulatoryoversight.com/2026/04/virginia-becomes-third-state-to-ban-sale-of-consumers-precise-geolocation-data/">Virginia Becomes Third State to Ban Sale of Consumers' Precise Geolocation Data | Regulatory Oversight</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，禁令仅适用于 1750 英尺以内的精确数据，因此公司仍可出售模糊地理位置数据。其他人则质疑对州外公司的执法问题，并担忧匿名化漏洞——大型科技公司可能声称剥离标识符后的数据不再属于个人信息。

**标签**: `#privacy`, `#geolocation`, `#regulation`, `#data protection`, `#Virginia`

---

<a id="item-3"></a>
## [crustc：将整个 Rust 编译器翻译为 C 语言](https://github.com/FractalFir/crustc) ⭐️ 8.0/10

crustc 项目成功将整个 rustc 编译器翻译为 C 语言，从而能够在没有 LLVM 或 GCC 支持的旧式或小众硬件上进行引导。 这一突破使得 Rust 能够在之前没有 Rust 支持的平台上从源代码引导，极大地扩展了 Rust 的覆盖范围，并通过多样化双重编译（DDC）实现编译器验证。 该项目是已知的第 14 次将 Rust 翻译为 C 的尝试，它在翻译后利用 GCC 的优化能力。C 输出可由任何 C 编译器编译，因此具有高度可移植性。

hackernews · Philpax · 7月2日 22:57 · [社区讨论](https://news.ycombinator.com/item?id=48768464)

**背景**: 引导（bootstrapping）是使用编译器编译自身的过程，这会产生一个先有鸡还是先有蛋的问题：第一个编译器必须用另一种语言编写。Rust 目前依赖 LLVM 作为后端，因此只支持 LLVM 可用的平台。将 Rust 翻译为 C 允许使用任何 C 编译器作为后端，从而在只有 C 编译器的平台上运行 Rust。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/FractalFir/crustc">GitHub - FractalFir/crustc: Entirety of `rustc`, translated to C. · GitHub</a></li>
<li><a href="https://rustc-dev-guide.rust-lang.org/building/bootstrapping/what-bootstrapping-does.html">What Bootstrapping does - Rust Compiler Development Guide</a></li>
<li><a href="https://internals.rust-lang.org/t/impediments-to-transpile-rust-to-c/8112">Impediments to transpile Rust to C? - compiler - Rust Internals</a></li>

</ul>
</details>

**社区讨论**: 社区对这一奉献精神和技术成就印象深刻，评论称赞其为“原创艺术品”，并讨论了诸如用于安全验证的 DDC 等潜在应用。一些用户指出 LLVM 的 C 后端曾经可用但正在恢复，而 crustc 提供了一种更直接的方法。

**标签**: `#rust`, `#compiler`, `#bootstrapping`, `#transpilation`, `#systems-programming`

---

<a id="item-4"></a>
## [Podman v6.0.0 发布：Quadlet 改进与自动数据库迁移](https://blog.podman.io/2026/07/introducing-podman-v6-0-0/) ⭐️ 8.0/10

Podman v6.0.0 引入了从 BoltDB 到 SQLite 的自动迁移，移除了对 BoltDB 的支持，并增强了 Quadlet，新增了如 'podman quadlet list' 等子命令。 这一重大版本巩固了 Podman 作为 Docker 可靠替代品的地位，通过 Quadlet 实现了无缝的 Docker Compose 兼容性和改进的 systemd 集成，惠及 DevOps 和家庭实验室用户。 从 BoltDB 到 SQLite 的自动迁移在系统重启时或通过 'podman system migrate --migrate-db' 命令完成，Quadlet 现在支持列出 quadlet 及其容器。

hackernews · soheilpro · 7月2日 14:23 · [社区讨论](https://news.ycombinator.com/item?id=48762098)

**背景**: Podman 是一个无守护进程的容器引擎，旨在成为 Docker 的直接替代品。Quadlet 允许用户使用 systemd 单元文件声明式管理容器。BoltDB 是旧版数据库后端，现已被 SQLite 取代，以获得更好的性能和可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.podman.io/en/latest/markdown/podman-quadlet.1.html">podman-quadlet — Podman documentation</a></li>
<li><a href="https://docs.podman.io/en/latest/markdown/podman-system-migrate.1.html">podman -system- migrate — Podman documentation</a></li>
<li><a href="https://blog.hofstede.it/podman-58-quadlet-multi-file-install-automatic-sqlite-migration-and-the-road-to-60/">Podman 5.8: Quadlet Multi-File Install, Automatic SQLite Migration ...</a></li>

</ul>
</details>

**社区讨论**: 用户报告了无缝的 Docker Compose 兼容性，并称赞 Quadlet 简化了容器管理。然而，也有人指出与 Docker 存在细微不兼容，可能导致期望 Docker 特定行为的项目出现问题。

**标签**: `#Podman`, `#containers`, `#Docker alternative`, `#release`, `#DevOps`

---

<a id="item-5"></a>
## [Immich 3.0 发布：自托管照片管理重大更新](https://github.com/immich-app/immich/discussions/29439) ⭐️ 8.0/10

自托管 Google Photos 替代品 Immich 3.0 现已发布，带来了新功能和错误修复。该版本包括从移动应用直接上传资产到相册等功能。 此版本巩固了 Immich 作为 Google Photos 领先开源替代品的地位，让用户完全掌控自己的照片和视频数据。它解决了日益增长的隐私担忧，并减少了对云服务的依赖。 此次更新包括在移动应用中直接上传资产到相册的新功能。社区讨论突显了对加密功能的持续关注，但端到端加密尚未实现。

hackernews · hashier · 7月2日 14:13 · [社区讨论](https://news.ycombinator.com/item?id=48761944)

**背景**: Immich 是一个高性能的自托管照片和视频管理解决方案，提供类似 Google Photos 的自动备份、搜索和组织功能。它运行在您自己的服务器上，确保数据隐私和控制。该项目是开源的，并在 GitHub 上积极开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://immich.app/">Immich</a></li>
<li><a href="https://github.com/immich-app/immich">GitHub - immich -app/ immich : High performance self - hosted photo ...</a></li>

</ul>
</details>

**社区讨论**: 社区参与度很高，许多用户称赞 Immich 的质量和易用性。关于加密存在热烈讨论：一些用户希望增加端到端加密以增强隐私，而另一些用户则认为服务器端加密和适当备份对自托管设置已经足够。

**标签**: `#self-hosting`, `#photo management`, `#open source`, `#immich`, `#privacy`

---

<a id="item-6"></a>
## [Postgres 事务：分布式系统的超能力](https://www.dbos.dev/blog/co-locating-workflow-state-with-your-data) ⭐️ 8.0/10

DBOS 的一篇博文指出，通过将工作流步骤与数据库提交对齐，Postgres 事务可以成为分布式系统的超能力，从而简化出站模式等模式。 这种方法通过消除对独立消息队列或外部编排器的需求，降低了架构复杂性，使构建可靠的分布式系统更加容易。 该技术将工作流推进单元与数据库提交单元一一对应，简化了出站模式，但可能导致数据库与工作流逻辑之间的紧耦合。

hackernews · KraftyOne · 7月2日 18:38 · [社区讨论](https://news.ycombinator.com/item?id=48765639)

**背景**: 在分布式系统中，确保数据库更新和消息发送的原子性具有挑战性。事务性出站模式通过在同一事务中将消息存储在数据库中，然后由单独进程发布来解决此问题。Postgres 事务提供 ACID 保证，可用于工作流编排。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://microservices.io/patterns/data/transactional-outbox.html">Microservices Pattern: Pattern: Transactional outbox</a></li>
<li><a href="https://en.wikipedia.org/wiki/Inbox_and_outbox_pattern">Inbox and outbox pattern - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了其中的权衡：一些人赞扬原子性的好处，而另一些人则质疑这是否真正构成了分布式系统，还是仅仅是一个带有互斥锁的集中式数据库。一位评论者指出了紧耦合的问题，但承认在实践中很少需要分离。

**标签**: `#Postgres`, `#distributed systems`, `#workflow orchestration`, `#transactions`, `#outbox pattern`

---

<a id="item-7"></a>
## [理解才能参与：AI 编程协作的关键](https://simonwillison.net/2026/Jul/2/understand-to-participate/#atom-everything) ⭐️ 8.0/10

Simon Willison 强调了 Geoffrey Litt 提出的“理解才能参与”概念，认为这是有效与编程代理协作、避免积累认知债务的关键。 这一概念解决了 AI 辅助编程中的关键挑战：保持开发者的理解以避免认知债务，认知债务会阻碍生产力和代码质量。它为团队与编程代理协作同时保留自身心智模型提供了实用框架。 Geoffrey Litt 在 2026 年 AI 工程师世界博览会上提出了这一观点，认为开发者必须足够深入地理解代码，才能与 AI 代理积极参与创作过程。该演讲已录制，将在 YouTube 上发布。

rss · Simon Willison · 7月2日 17:07

**背景**: 认知债务指的是软件系统中共享理解随时间推移而侵蚀，导致用于推理和安全修改系统的心智模型不足。随着 AI 编程代理生成越来越大的代码变更，开发者面临失去对代码库理解的风险，积累最终必须偿还的认知债务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://margaretstorey.com/blog/2026/02/09/cognitive-debt/">How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt</a></li>
<li><a href="https://getdx.com/blog/cognitive-debt-the-hidden-risk-in-ai-driven-software-development/">Cognitive debt: The hidden risk in AI-driven software development</a></li>
<li><a href="https://arxiv.org/abs/2603.22106">[2603.22106] From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI</a></li>

</ul>
</details>

**标签**: `#AI-assisted coding`, `#cognitive debt`, `#developer experience`, `#software engineering`

---

<a id="item-8"></a>
## [ECTC 2026 综述：EMIB-T、定制 HBM、HBM4、微流冷却和光子互连](https://newsletter.semianalysis.com/p/ectc2026) ⭐️ 8.0/10

在 ECTC 2026 上，Intel、台积电、SK 海力士、三星、美光、Marvell、Lightmatter 和微软展示了半导体封装领域的进展，包括 Intel 的 EMIB-T 路线图、定制 HBM 解决方案、HBM4 封装挑战、微流冷却和光子互连。 这些创新解决了 AI 和高性能计算中的关键瓶颈，如内存带宽、热管理和互连密度，从而支持更强大、更高效的芯片设计。 Intel 的 EMIB-T 支持 HBM4 和 UCIe 接口，而微流冷却通过芯片内的微观通道循环冷却液。光子互连利用光进行数据传输，有望实现更高带宽和更低功耗。

rss · Semianalysis · 7月2日 17:25

**背景**: 像 EMIB（嵌入式多芯片互连桥）这样的先进封装技术通过小型硅桥连接芯片，消除了大型中介层。微流冷却是一种新兴的高功率芯片热管理方法。光子互连用光代替电信号以克服带宽限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/ammhasib_driving-the-future-of-multi-chip-compute-activity-7408764535257317376-dVkb">Intel EMIB - T : Revolutionizing AI and HPC Packaging with... | LinkedIn</a></li>
<li><a href="https://abit.ee/en/hard/intel-introduces-emib-t-revolutionary-multi-die-packaging-technology-with-hbm4-support">Intel Introduces EMIB - T — Revolutionary Multi-Die Packaging...</a></li>
<li><a href="https://medium.com/no-time/microfluidic-cooling-the-silent-revolution-in-high-performance-semiconductor-c713d1089630">Microfluidic Cooling : The Silent Revolution In... | Medium</a></li>

</ul>
</details>

**标签**: `#semiconductor packaging`, `#HBM`, `#photonic interconnects`, `#microfluidic cooling`, `#ECTC`

---

<a id="item-9"></a>
## [Hierarchos：232M 参数循环记忆增强模型训练成功](https://www.reddit.com/r/MachineLearning/comments/1um123n/hierarchos_preliminary_findings_from_a_232m/) ⭐️ 8.0/10

研究人员从头训练了 Hierarchos，一个 232M 参数的循环记忆增强语言模型，结合了 RWKV 骨干网络、层次化循环、可微分槽式长期记忆和确定性后缀自动机，在修复训练-推理不匹配后实现了指令连贯性。 这项工作表明非 Transformer 架构可以在不崩溃的情况下进行大规模训练，为开发具有显式记忆和层次推理的更参数高效模型提供了潜在路径，挑战了 Transformer 在 LLM 中的主导地位。 关键的工程修复包括对齐训练和推理之间的漂移状态重置、在训练期间将长期记忆切换为只读模式，以及限制 RWKV 通道混合和 DeepEmbed 调制中的激活值以防止 NaN 梯度。

reddit · r/MachineLearning · /u/PhysicsDisastrous462 · 7月3日 01:48

**背景**: 目前大多数大语言模型基于 Transformer 架构，使用注意力机制。Hierarchos 探索了 RWKV（一种循环架构）和显式记忆模块等替代方案以提高参数效率。该模型还使用后缀自动机进行精确模式匹配，以及层次化的管理者/工作者循环进行迭代优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2406.19369">Mamba or RWKV : Exploring High-Quality and</a></li>
<li><a href="https://en.wikipedia.org/wiki/Suffix_automaton">Suffix automaton - Wikipedia</a></li>
<li><a href="https://github.com/howard-hou/RWKV-TS">GitHub - howard-hou/ RWKV -TS: RWKV -TS: Beyond Traditional...</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#language model`, `#recurrent architecture`, `#memory augmentation`, `#research`

---

<a id="item-10"></a>
## [证监会同意宇树科技科创板 IPO 注册](https://www.csrc.gov.cn/csrc/c105906/c7642867/content.shtml) ⭐️ 8.0/10

2026 年 7 月 1 日，中国证监会同意宇树科技股份有限公司在科创板首次公开发行股票并上市的注册申请，标志着其上市进程进入关键阶段。 宇树科技是国内领先的机器人独角兽，其成功上市将推动机器人和 AI 生态系统发展，为创新和商业化提供资金支持。 公司须严格按照报送上交所的招股说明书和发行承销方案实施，注册至发行结束期间发生重大事项须及时报告。

telegram · zaihuapd · 7月2日 09:57

**背景**: 宇树科技是知名机器人公司，以 H1 和 R1 等人形机器人闻名。科创板是中国面向科技企业的纳斯达克式板块。IPO 注册批准是上市前的最后监管门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eu.36kr.com/zh/p/3419294583000457">eu.36kr.com/zh/p/3419294583000457</a></li>

</ul>
</details>

**标签**: `#IPO`, `#机器人`, `#科创板`, `#宇树科技`, `#资本市场`

---

<a id="item-11"></a>
## [花旗禁用 GPT-5.5，AI 成本飙升](https://www.404media.co/companies-are-throttling-employees-ai-use-because-its-too-expensive/) ⭐️ 8.0/10

花旗银行自 2026 年 6 月 24 日起完全禁用 GPT-5.5、Claude Opus 4.6/4.7 等先进 AI 模型，理由是这些模型消耗的 AI 积分过高。Atlassian 的 AI 月支出从 500 万美元飙升至超过 1500 万美元，促使公司限制使用并推出成本追踪面板。 这标志着企业面临按用量计费的 AI 成本不可持续的重大行业转变，可能减缓前沿模型的采用。Adobe 和 Amazon 等公司也在收紧 AI 访问权限，预示着企业 AI 策略的广泛调整。 Atlassian 的内部仪表板显示，AI 支出从 2025 年 8 月的 500 万美元飙升至 2026 年 5 月的超过 1500 万美元。Adobe 的无限量 Claude 合同于 2026 年 6 月 30 日到期且未续签。Amazon 此前关闭了鼓励 AI 使用的内部排行榜，员工随后发现了此前未知的 token 使用上限。

telegram · zaihuapd · 7月2日 13:59

**背景**: 许多企业通过按 token 或按请求计费的 API 使用 AI 模型，随着使用规模扩大，成本变得不可预测。GPT-5.5 和 Claude Opus 4.7 等前沿模型能力更强，但每次查询也更昂贵。公司最初鼓励广泛尝试 AI，但随着账单膨胀，现在开始控制成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-opus-4-7">Introducing Claude Opus 4 . 7 \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT-5.5</a></li>

</ul>
</details>

**标签**: `#AI`, `#cost management`, `#enterprise`, `#industry trend`

---

<a id="item-12"></a>
## [PS3 商店 2027 年关闭，档案员紧急抢救游戏](http://no-intro.org/) ⭐️ 8.0/10

索尼宣布将于 2027 年 7 月永久关闭 PS3 和 PS Vita 的 PlayStation 商店，数字档案管理员正紧急备份 PS3 游戏数据。RPCS3 模拟器团队正利用 no-intro.org 数据库协调保存工作。 此次关闭可能导致从未推出实体版的数字 PS3 游戏永久丢失，凸显了数字游戏保存的脆弱性。RPCS3 和 no-intro.org 的参与凸显了社区在保护游戏历史中的作用。 RPCS3 推荐使用 no-intro.org 数据库，该平台记录加密哈希、文件大小和序列号，以追踪哪些游戏已备份。截至 2026 年 4 月，超过 70%的 PS3 游戏可在 RPCS3 上运行，但纯数字游戏仍面临风险。

telegram · zaihuapd · 7月2日 15:04

**背景**: PlayStation 3 于 2006 年发布，通过 PlayStation 商店提供了大量数字游戏。RPCS3 是一款免费开源的模拟器，允许在 PC 上运行 PS3 游戏；no-intro.org 是一个数据库，用于编录 ROM 和数字游戏元数据以进行保存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RPCS3">RPCS3</a></li>
<li><a href="https://no-intro.org/">No - Intro . org</a></li>

</ul>
</details>

**标签**: `#digital preservation`, `#gaming`, `#PS3`, `#RPCS3`, `#no-intro`

---

<a id="item-13"></a>
## [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](https://t.me/zaihuapd/42327) ⭐️ 8.0/10

Anthropic 指控阿里巴巴对其 Claude AI 模型发动了迄今已知最大规模的蒸馏攻击，涉及约 2.5 万个欺诈账户，在 2026 年 4 月 22 日至 6 月 5 日期间进行了超过 2880 万次交互。 此事件凸显了模型蒸馏攻击日益增长的威胁，这种攻击可能削弱 AI 公司的知识产权和竞争优势，并可能促使更严格的监管和全行业的防御措施。 Anthropic 声称此次攻击由阿里巴巴及其 AI 实验室 Qwen 实施，利用蒸馏获得的知识可能用于增强其自身模型。该公司已致信美国参议院银行委员会详细说明这些指控。

telegram · zaihuapd · 7月3日 06:21

**背景**: 模型蒸馏是一种技术，让较小的弱模型从较大、更强的模型的输出中学习，以复制其能力。未经授权使用时，就变成了蒸馏攻击，使竞争对手能够以极低的成本窃取专有 AI 能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks?ref=mlq.ai">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained">AI Model Distillation Attacks : What They Are and Why... | MindStudio</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen_(Alibaba_Cloud)">Qwen (Alibaba Cloud)</a></li>

</ul>
</details>

**标签**: `#AI`, `#security`, `#distillation`, `#Anthropic`, `#Alibaba`

---

<a id="item-14"></a>
## [华为发布 Atlas 350 加速卡，性能达 H20 的 2.87 倍](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

在 2026 年华为中国合作伙伴大会上，华为正式发布并上市了搭载全新昇腾 950PR 处理器的 AI 训练推理加速卡 Atlas 350，其单卡算力达到英伟达 H20 的 2.87 倍，并支持 FP4 低精度推理。 这标志着中国国产 AI 芯片发展的重要一步，可能减少对英伟达硬件的依赖。Atlas 350 对 FP4 的支持和大容量 HBM（112GB）使得单卡即可高效推理 70B 参数等大模型，降低部署成本。 Atlas 350 是国内首款支持 FP4 精度的加速卡，并采用华为自研 HBM（HiBL 1.0），互联带宽是上一代的 2.5 倍。单卡即可加载 70B 参数模型，大幅降低推理延迟与投资成本。

telegram · zaihuapd · 7月3日 08:35

**背景**: FP4 精度是一种低精度格式，可减少内存占用并加速推理，常用于 AI 模型部署。英伟达 H20 是上一代加速器，曾是出口限制前允许在中国销售的最先进英伟达芯片。华为昇腾 950PR 芯片于 2026 年 3 月进入量产，是华为 AI 芯片收入增长的关键驱动力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/markdhirsch_ai-semiconductors-huawei-activity-7441908261555179521-ELQu">Huawei Ascend 950 PR Chip Debuts in China with... | LinkedIn</a></li>
<li><a href="https://www.tradingview.com/news/invezz:f89d2e554094b:0-huawei-ascend-950-chip-demand-surges-after-deepseek-v4-launch/">Huawei Ascend 950 chip demand surges after... — TradingView News</a></li>
<li><a href="https://meyka.com/blog/huawei-targets-12b-ai-chip-revenue-up-60-from-7-5b-in-2025-2605/">Huawei Targets $12B AI Chip Revenue, Up 60% From... | Meyka</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#AI accelerator`, `#hardware`, `#Ascend`, `#deep learning`

---