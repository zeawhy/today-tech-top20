---
layout: default
title: "Horizon Summary: 2026-09-17 (ZH)"
date: 2026-09-17
lang: zh
---

> 从 87 条内容中筛选出 12 条重要资讯。

---

1. [AWS 承认中东设施遭伊朗袭击后部分数据永久丢失](#item-1) ⭐️ 9.0/10
2. [Nvidia 宣布支持用 Rust 原生编写 CUDA GPU 内核](#item-2) ⭐️ 8.0/10
3. [小米发布 MiMo 2.6 实时后训练仪表盘](#item-3) ⭐️ 8.0/10
4. [电子墨水相框聆听鸟鸣并用 19 世纪插画风格绘制鸟类](#item-4) ⭐️ 8.0/10
5. [DeepMind 成立政策研究所，力图主导 AI 治理方向](#item-5) ⭐️ 8.0/10
6. [黑客曝光 Flock 监控摄像头中的硬编码凭证漏洞](#item-6) ⭐️ 8.0/10
7. [TMLR 就 10 篇被直接拒稿论文质询作者本人](#item-7) ⭐️ 8.0/10
8. [GoBench 用 9x9 围棋对抗 KataGo 来评测大语言模型](#item-8) ⭐️ 8.0/10
9. [Prior Labs 发布 TabPFN-3.5，新的表格基础模型 SOTA](#item-9) ⭐️ 8.0/10
10. [阶跃星辰发布 StepAudio 3 Music：用自然语言生成完整歌曲](#item-10) ⭐️ 8.0/10
11. [新浪云 SAE 永久下线，早期 B 站视频源文件随之消失](#item-11) ⭐️ 8.0/10
12. [美光发布全球首款 512GB DDR5 RDIMM，计划 2027 年量产](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AWS 承认中东设施遭伊朗袭击后部分数据永久丢失](https://www.wsj.com/world/middle-east/aws-says-it-cant-restore-some-data-from-mideast-facilities-struck-by-iran-ddcb7e5d) ⭐️ 9.0/10

AWS 已承认，其位于中东、遭伊朗袭击的设施中存储的部分客户数据无法恢复，这是超大规模云服务商罕见地承认永久性数据丢失。这一披露直接推翻了 AWS 高层此前公开的保证，即单个数据中心被摧毁也不会被用户察觉，因为系统具备冗余。 这一事件动摇了人们长期以来的假设，即超大规模云冗余能够保证数据即使在极端地缘政治事件中也能存活，迫使云架构师和业务连续性规划者重新思考多区域和多云策略。它还凸显了数据驻留法律如何将数据困在脆弱地区，使客户没有可行的恢复途径。 受影响的区域似乎是 me-south-1（巴林）和 me-central-1（阿联酋），社区报告显示可用区自 2026 年初以来一直处于宕机状态。AWS 标准的 S3 持久性保证为 11 个 9（99.999999999%），仅适用于区域内的硬件故障，而不适用于整个区域的物理摧毁，也不适用于因驻留限制而无法复制出去的数据。

hackernews · berkeleyjunk · 9月15日 21:41 · [社区讨论](https://news.ycombinator.com/item?id=49719249)

**背景**: 云冗余通常涉及跨多个可用区或地理区域复制数据，以便一个位置的中断不会导致数据丢失。数据驻留法律（如阿联酋的法律）要求某些数据必须在本国境内存储和处理，这可能阻止数据复制到其他区域。云合同中的不可抗力条款（如 AWS 第 11.3 条）免除提供商因超出其合理控制范围的事件（包括战争和天灾）而导致故障的责任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_residency">Data residency</a></li>
<li><a href="https://en.wikipedia.org/wiki/Force_majeure">Force majeure</a></li>
<li><a href="https://www.akamai.com/glossary/what-is-cloud-redundancy">What Is Redundancy in Cloud Computing? | Akamai</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了 AWS 早先声称炸毁一个数据中心不会被察觉与当前承认永久丢失之间的矛盾。许多人指出阿联酋的数据驻留要求是阻止复制的关键因素，还有人引用不可抗力条款和 11 个 9 的持久性保证作为客户承担风险的证据。总体情绪是对 AWS 此前的宣传持批评态度，并对云弹性的现实局限感到担忧。

**标签**: `#AWS`, `#cloud infrastructure`, `#data loss`, `#geopolitics`, `#disaster recovery`

---

<a id="item-2"></a>
## [Nvidia 宣布支持用 Rust 原生编写 CUDA GPU 内核](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/) ⭐️ 8.0/10

Nvidia 在官方开发者博客上发布了介绍 CUDA Rust 的文章，提供两条用 Rust 原生编写 GPU 内核的技术路线。这是 Nvidia 首次官方认可 Rust 作为 CUDA 内核开发的一等语言，打破了长期以来只能用 C++ 编写 GPU 代码的惯例。 这对 Rust 和 GPU 计算社区都是一次重大转变，因为 Rust 的内存安全保证有望减少 GPU 代码中一大类常见错误。这也表明 Nvidia 正在回应开发者对更安全、更现代工具的需求，同时进一步巩固 CUDA 生态的主导地位。 公告描述了两条在 Rust 中编写 CUDA 内核的不同路线，但博客文章的语气被批评像 AI 生成的营销文案，而非 Nvidia 以往的技术写作风格。社区成员还将其与 Rust-GPU、vectorware 等现有项目以及 Triton 等 DSL 进行了比较。

hackernews · nonmaskable · 9月16日 11:15 · [社区讨论](https://news.ycombinator.com/item?id=49724881)

**背景**: CUDA 是 Nvidia 专有的并行计算平台，内核（kernel）是程序员编写、运行在 GPU 上的函数。过去编写 CUDA 内核必须使用 C++，这使代码库与 Nvidia 硬件深度绑定，难以移植。Rust 是一门以编译期内存安全著称的系统编程语言，Rust-GPU 等项目多年来一直在探索用 Rust 编写 GPU 代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rust-gpu.github.io/rust-gpu/book/">Introduction - Rust GPU Dev Guide</a></li>
<li><a href="https://www.javacodegeeks.com/2026/09/cuda-and-the-vendor-lock-in-problem-in-gpu-programming.html">CUDA and the Vendor Lock-In Problem in GPU Programming</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：有人欢迎任何能让可靠 GPU 编程更轻松的工具，也有人强烈批评 CUDA 的专有性质及其造成的厂商锁定。一些人指出博客文章听起来像 AI 写的，还有人提到 Hugging Face 的 Candle crate 和 vectorware 等相关工作，作为评判此次公告的参照。

**标签**: `#Rust`, `#GPU`, `#CUDA`, `#Nvidia`, `#Programming Languages`

---

<a id="item-3"></a>
## [小米发布 MiMo 2.6 实时后训练仪表盘](https://mimo.xiaomi.com/rl/) ⭐️ 8.0/10

小米在 mimo.xiaomi.com/rl/ 上线了一个公开的实时仪表盘，展示 MiMo 2.6 模型的后训练与强化学习进展。该仪表盘实时公开训练运行情况和强化学习环境评分，这在前沿 AI 开发中属于罕见的透明化举措。 通过公开后训练和强化学习进展，小米树立了一个先例，可能促使其他实验室——尤其是拥有接近前沿模型的团队——披露更多训练细节。这种透明度可能改变社区评估模型质量和可信度的方式，并强化小米在开源 AI 生态中的地位。 该仪表盘聚焦于后训练阶段，包括监督微调和强化学习，而非最初的预训练。社区成员指出，此前的 MiMo-V2.5-Pro 在 DeepSWE 1.1 上仅得分 19%，而 Fable、Kimi K3 和 Astra 等竞品得分在 69% 至 74% 之间，这表明 MiMo 2.6 正力求在编程和推理基准上实现大幅跃升。

hackernews · krackers · 9月16日 20:09 · [社区讨论](https://news.ycombinator.com/item?id=49732270)

**背景**: MiMo 是小米开发的一系列大语言模型，于 2025 年 4 月首次发布 MiMo-7B 模型，目前通过 API 向开发者提供服务。后训练是大规模预训练之后的阶段，通过监督微调（SFT）和强化学习（RL）等技术使模型对齐人类偏好并提升推理能力。在机器人和游戏 AI 研究中，强化学习训练的实时仪表盘很常见，但为前沿规模的语言模型公开发布此类仪表盘则十分罕见，标志着开放程度达到了新水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xiaomi_MiMo">Xiaomi MiMo - Wikipedia</a></li>
<li><a href="https://pytorch.org/blog/a-primer-on-llm-post-training/">A Primer on LLM Post-Training - PyTorch</a></li>
<li><a href="https://huggingface.co/blog/karina-zadorozhny/guide-to-llm-post-training-algorithms">A Guide to Reinforcement Learning Post-Training for LLMs: PPO, DPO, GRPO, and Beyond</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极，用户称赞 MiMo 2.5 在软件工程任务中的性价比和高质量，并赞赏小米仪表盘的透明度。一些评论者将此视为对 OpenAI 和 Anthropic 等闭源实验室的竞争威胁，另一些人则分享了基准对比，显示 MiMo 2.6 相较前代可能有显著提升。

**标签**: `#AI`, `#machine-learning`, `#open-source`, `#model-training`, `#transparency`

---

<a id="item-4"></a>
## [电子墨水相框聆听鸟鸣并用 19 世纪插画风格绘制鸟类](https://github.com/arnegiacomo/fugleramme) ⭐️ 8.0/10

开发者 Arne Munthe-Kaas（arnegiacomo）在 GitHub 上发布了一个名为“fugleramme”的项目，它将电子墨水显示屏、ESP32 微控制器和 BirdNET 神经网络结合起来，用于检测鸟鸣并将识别出的鸟种渲染成 19 世纪风格的插画。该项目以“Show HN”形式发布在 Hacker News 上，迅速获得 240 条评论和 8.0/10 的评分。 该项目是趣味性跨学科工程的杰出范例，融合了嵌入式硬件、生物声学 AI 和生成式插画，展示了廉价微控制器与开源模型如何将日常自然观察变成一种充满魔力的环境体验。它也凸显了 ESP32 加电子墨水 DIY 设备生态的成长，以及基于 BirdNET 的鸟类监测工具的流行。 其分类器是 BirdNET，一种用于声学鸟类识别的传统卷积神经网络，而非大语言模型；电子墨水屏因其类纸、低功耗的特性被选用，适合常开的环境设备。项目托管在 github.com/arnegiacomo/fugleramme，并与 2026 年 5 月一篇题为“Avian Visitors”的相关 HN 帖子相互参照。

hackernews · arnemunthekaas · 9月15日 12:31 · [社区讨论](https://news.ycombinator.com/item?id=49711544)

**背景**: BirdNET 是由康奈尔鸟类学实验室和开姆尼茨工业大学开发的 AI 系统，能够从声音录音中识别鸟种，被广泛用于生态研究和消费级应用。电子墨水（e-ink）显示屏看起来像纸张，静态显示时几乎不耗电，在以低成本 Wi-Fi/蓝牙微控制器 ESP32 为核心的 DIY 项目中很受欢迎。该项目正处于这两股趋势的交汇处，并增加了一个生成式插画层，将检测到的鸟种转化为 19 世纪风格的图画。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://www.howtogeek.com/esp32-e-ink-display-projects-weekend-may-29-jun-1/">5 ESP32-powered E-Ink display projects to make this weekend ...</a></li>

</ul>
</details>

**社区讨论**: 评论者热情高涨，有人称其为“HN 上最酷的东西”，并称赞它将各种想法融合成某种充满魔力的东西；其他人则澄清 BirdNET 是传统神经网络而非大语言模型，分享了自己的 ESP32/电子墨水项目及电池续航计算，并提到近期涌现的鸟类相关项目（如 birdnet-go）。一位挪威评论者称该作品是开发者的“纯粹艺术”。

**标签**: `#e-ink`, `#birdnet`, `#esp32`, `#hardware`, `#creative-coding`

---

<a id="item-5"></a>
## [DeepMind 成立政策研究所，力图主导 AI 治理方向](https://institute.deepmind.com/) ⭐️ 8.0/10

DeepMind 成立了 DeepMind Institute，这是一个内部政策智库，发布了关于推理透明度、面向 AGI 的经济政策以及新乌托邦主义原则的立场文件。该发布迅速在 Hacker News 上引发审视，用户质疑其对 AGI 时间线的表述，并指出许多热门链接是由同一个仅注册 11 天的账号提交的。 一家领先的 AI 实验室直接介入政策辩论，可能影响监管走向、劳动力市场保障以及 AI 利润的分配方式，从而波及政府、劳动者和竞争对手。这也引发了疑问：由企业资助的研究能否在治理讨论中保持中立声音。 该研究所的经济政策文章提出了从轻微到重大破坏的三种影响情景：在较轻微情景下建议扩大失业保险和劳动所得税抵免（EITC），在更严重情景下则强调分享 AI 利润或持有其所有权，并建议用 AI 评估器来衡量政策有效性。其 AGI 表述声称当今系统正接近人脑级别的认知能力，这一说法遭到评论者的强烈质疑。

hackernews · vertigoruntime · 9月16日 14:32 · [社区讨论](https://news.ycombinator.com/item?id=49727659)

**背景**: DeepMind 是谷歌旗下的 AI 研究实验室，以 AlphaGo 和 AlphaFold 等系统闻名，而 AGI 指的是假设中具备人脑全部认知能力的 AI。政策研究所是研究和建议治理方案的机构，AI 实验室近年来纷纷设立自己的研究所来影响监管。随着模型能力增强，围绕 AGI 时间线和 AI 经济影响的争论日益激烈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://institute.deepmind.com/">DeepMind Institute</a></li>
<li><a href="https://gsas.harvard.edu/news/how-ai-might-impact-economy-and-what-government-could-do-about-it">How AI Might Impact the Economy—and What Government Could Do ...</a></li>
<li><a href="https://skynetcountdown.com/agi-timeline">AGI Timeline 2026: Expert Predictions Tracker | Skynet Countdown</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：有人称赞其经济政策文章合理且论证充分，也有人指责该研究所是推动议程的内部智库，并夸大了 AGI 说法。多名用户指出疑似“水军”行为，称许多热门链接来自同一个仅注册 11 天的账号，还有人批评网站文字对比度过低、灰得难以阅读。

**标签**: `#AI policy`, `#DeepMind`, `#AGI`, `#AI governance`, `#economics`

---

<a id="item-6"></a>
## [黑客曝光 Flock 监控摄像头中的硬编码凭证漏洞](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 8.0/10

安全研究员 Micah Lee 发布调查结果，显示 Flock Safety 的车牌识别（ALPR）监控摄像头中存在硬编码 API 密钥和明文凭证，攻击者只要获得物理接触即可提取敏感数据。该披露与 404 Media 合作完成，Distributed Denial of Secrets 已公开摄像头分区镜像。 Flock 在全美 49 个州的 6000 多个社区运营，每月进行超过 200 亿次车辆扫描，因此这些漏洞可能使庞大的监控网络面临未授权访问风险。该事件对处理敏感执法数据的公司的安全实践提出了严重质疑。 硬编码的 API 密钥可用于请求以明文存储的凭证，可能获得对 Flock 服务器的访问权限；但目前尚不清楚攻击者以摄像头身份认证后能做什么。Flock 的漏洞披露政策因在研究人员需要与设备交互或下载数据时设置例外条款而受到批评。

hackernews · driverdan · 9月16日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49726586)

**背景**: Flock Safety 是一家制造自动车牌识别（ALPR）摄像头并运营全国性网络的公司，该网络与警察部门共享车辆数据。ALPR 摄像头拍摄过往车辆图像，并利用机器学习识别车牌，Flock 还在扩展视频流和 AI 驱动的自然语言搜索功能。硬编码凭证是直接嵌入源代码或固件中的密钥，攻击者很容易从物理设备中提取。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://www.aclu.org/news/privacy-technology/tracking-alpr-cameras/flock-roundup">Flock’s Aggressive Expansions Go Far Beyond Simple Driver Surveillance | American Civil Liberties Union</a></li>
<li><a href="https://blogs.jsmon.sh/what-is-hardcoded-api-keys-in-mobile-apps-ways-to-exploit-examples-and-impact/">Hardcoded API Keys in Mobile Apps: Risks & Fixes</a></li>

</ul>
</details>

**社区讨论**: 评论者强烈批评 Flock，称硬编码凭证是无能的表现，并认为该公司的漏洞披露政策只是做样子，并非真正为了解漏洞。多人指出，在公共场所使用现成硬件和软件使本地物理接触成为真实威胁，还有评论者强调设备上的数据甚至没有适当加密。

**标签**: `#security`, `#vulnerability-disclosure`, `#surveillance`, `#IoT`, `#privacy`

---

<a id="item-7"></a>
## [TMLR 就 10 篇被直接拒稿论文质询作者本人](https://www.reddit.com/r/MachineLearning/comments/1wid67h/tmlr_reached_out_to_the_authors_of_10_papers/) ⭐️ 8.0/10

TMLR 的联合主编联系了 10 篇即将被直接拒稿（desk rejection）论文的作者，要求他们解释自己提交的论文，结果令人担忧：1 篇被作者主动撤稿，1 位作者称因其他事务无法参与，1 位约好会议却未出席，3 位作者无法回答关于论文的基本问题，3 位能回答高层思路但在技术细节上遇到困难，只有 1 位回答了全部问题——但面试者仍在该论文中发现了一个重大缺陷。 这一实验表明，相当一部分投稿可能并非由提交者本人真正撰写，暗示可能存在 AI 生成论文或论文工厂（paper mill）行为，并对机器学习出版领域的同行评审诚信和作者身份核验提出了严峻问题。 此次调查仅覆盖 10 篇被直接拒稿的投稿，样本量小且具有自选择性；而直接拒稿本身仅适用于明显情形，例如未匿名、未使用未经修改的 TMLR 样式文件，或与已发表/在审工作明显重叠。

reddit · r/MachineLearning · /u/hihey54 · 9月16日 23:20

**背景**: TMLR（Transactions on Machine Learning Research）是一本采用公开评审的机器学习期刊，评审意见对外公开，并通过直接拒稿在送审前筛除违反基本格式或原创性规则的投稿。学术作者身份通常意味着对研究做出真实的智力贡献，而它也是招聘、晋升和终身教职评定的主要依据，因此期刊越来越担心出现列名作者无法解释自己研究的情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jmlr.org/tmlr/ae-guide.html">TMLR guidelines for action editors</a></li>
<li><a href="https://en.wikipedia.org/wiki/Academic_authorship">Academic authorship - Wikipedia</a></li>
<li><a href="https://phdflow.ai/guides/tmlr-explained">TMLR explained: a differently shaped bar, not a lower one</a></li>

</ul>
</details>

**标签**: `#peer-review`, `#academic-publishing`, `#research-integrity`, `#machine-learning`, `#AI-ethics`

---

<a id="item-8"></a>
## [GoBench 用 9x9 围棋对抗 KataGo 来评测大语言模型](https://www.reddit.com/r/MachineLearning/comments/1wi68jg/gobench_evaluating_llms_on_the_game_of_go_r/) ⭐️ 8.0/10

GoBench 是一个新的基准测试，让大语言模型在 9x9 围棋对局中与从随机水平到超人水平的 KataGo 对手阶梯进行较量。作者报告称，GPT-6 Astra 的最高配置达到 2500 Elo，远低于最强 KataGo 的 4400 Elo；而在提供编程工具并允许两小时准备的情况下，Codex 配合 Astra 可达到 3560 Elo。 该基准测试显示其与 ARC-AGI 2 存在强相关性（r=0.83），说明围棋表现可能可以作为通用推理能力的代理指标，而且该基准远未饱和，为未来模型留下了很大提升空间。这为研究者提供了一个新的开源工具，用于在文本基准趋于饱和之后继续衡量大语言模型的推理进展。 该评测使用 9x9 围棋而非完整的 19x19 棋盘，并且只要基准尚未饱和，排行榜就会持续更新。作者公开了排行榜、代码和论文，并指出工具使用和准备时间能显著提升模型的 Elo 分数。

reddit · r/MachineLearning · /u/Roland31415 · 9月16日 18:54

**背景**: KataGo 是一款免费开源的计算机围棋引擎，通过深度神经网络和高级搜索进行自我对弈训练，能够达到超人水平。Elo 是一种最初为国际象棋开发的评分系统，也被用于围棋中量化相对棋力，数值越高表示棋手越强。ARC-AGI 2 是一个旨在压力测试最先进 AI 推理系统并追踪 AGI 进展的基准测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/KataGo">KataGo - Wikipedia</a></li>
<li><a href="https://arcprize.org/arc-agi/2">ARC-AGI-2</a></li>
<li><a href="https://en.wikipedia.org/wiki/Elo_rating_system">Elo rating system - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM evaluation`, `#benchmark`, `#Go`, `#reasoning`, `#AI`

---

<a id="item-9"></a>
## [Prior Labs 发布 TabPFN-3.5，新的表格基础模型 SOTA](https://www.reddit.com/r/MachineLearning/comments/1wh4xhy/tabpfn35_is_released_as_the_next_sota_tabular/) ⭐️ 8.0/10

Prior Labs 发布了 TabPFN-3.5，这是一款新的表格基础模型，目前在 TabArena 和 BeyondArena 两个基准测试上均排名第一，支持最多 100 万行数据和 2 万个特征。此次发布包含三个变体：TabPFN-3.5-Fast（alpha 阶段，比基础模型快 6 倍）、TabPFN-3.5-Thinking（通过 API 提供，用计算量换取更高精度）以及 TabPFN-3.5-Plus。 这是表格基础模型领域一项重要的 SOTA 进展。长期以来，梯度提升树在该领域占据主导地位，而基础模型在非独立同分布（off-IID）数据上一直难以与之匹敌。BeyondArena 上大幅的 Elo 提升表明，基础模型正在缩小在文本丰富、高基数和高维表格数据上的差距，这可能会改变从业者处理表格机器学习的方式。 在 BeyondArena 上，TabPFN-3.5 在文本丰富、高基数和高维数据上领先，比之前最强基线高出 250 Elo，比之前的总体领先者高出 150 Elo。TabPFN-3.5-Thinking 在 BeyondArena 上比基础模型提升 20 Elo，在 TabArena 上提升 44 Elo，而 Fast 变体仍处于 alpha 阶段。

reddit · r/MachineLearning · /u/tuanacelik · 9月15日 16:18

**背景**: TabPFN 是一款面向中小规模表格数据的基础模型，由 Hollmann、Müller、Purucker 等人在 2025 年发表于 Nature 的论文中提出，旨在无需针对特定数据集训练即可做出准确预测。TabArena 是一个持续维护的表格机器学习“活”基准，统一了预处理和评估流程；而 BeyondArena 则将评估扩展到 IID 数据之外，涵盖时间序列和分组任务，覆盖广泛的数据集规模和特征维度。Elo 是一种相对评分系统，最初用于国际象棋，此处用于跨基准任务比较模型性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-024-08328-6">Accurate predictions on small data with a tabular foundation model | Nature</a></li>
<li><a href="https://arxiv.org/abs/2506.16791">[2506.16791] TabArena: A Living Benchmark for Machine Learning on Tabular Data</a></li>
<li><a href="https://aiweekly.co/alerts/beyondarena-finds-trees-still-beat-tabular-fms-off-iid-data">BeyondArena finds trees still beat tabular FMs off-IID data | AI Weekly</a></li>

</ul>
</details>

**标签**: `#tabular-data`, `#foundation-models`, `#machine-learning`, `#benchmarking`, `#SOTA`

---

<a id="item-10"></a>
## [阶跃星辰发布 StepAudio 3 Music：用自然语言生成完整歌曲](https://static.stepfun.com/blog/stepaudio3/music/) ⭐️ 8.0/10

阶跃星辰发布了 AI 音乐生成模型 StepAudio 3 Music，能够根据自然语言描述直接生成完整的 48 kHz 立体声歌曲。该模型采用 MoE 架构与 AR + DiT 范式，并通过 ABC-COT 技术先将创作意图转化为歌曲结构规划，再进行音频合成，在 Audiobox 与 MuQ-Similarity 评测中均取得 SOTA。 这标志着 AI 音乐生成领域的一次显著进步，因为该模型声称通过让用户用自然语言指定风格、人声、情绪、乐器、调性和速度，兼顾了音乐质量与可控性。它面向短视频配乐、词曲 Demo 和游戏主题曲等实际场景，在这些场景中，快速且可定制的整曲生成具有很高价值。 该模型输出完整的 48 kHz 立体声音频，并使用 ABC-COT 技术在生成前根据自然语言规划歌曲结构，在 Audiobox 与 MuQ-Similarity 评测中处于领先。不过，官方公告未披露模型规模、训练数据、延迟、许可或公开可用性等细节，因此其 SOTA 声明仍有待独立验证。

telegram · zaihuapd · 9月16日 08:48

**背景**: 混合专家（MoE）是一种深度学习架构，每次输入只激活部分专门的子网络（即“专家”），从而提升大模型的效率与扩展性。AR + DiT 将自回归（AR）序列建模与扩散 Transformer（DiT）结合，后者是一种基于序列的生成架构，已在现代图像与音频生成中大量取代 U-Net 设计。ABC-COT 似乎是阶跃星辰提出的一种类思维链规划方法，在合成音频之前将用户的自然语言需求转化为明确的歌曲结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.architectureandgovernance.com/applications-technology/mixture-of-experts-moe-architecture-a-deep-dive-and-comparison-of-top-open-source-offerings/">Mixture of Experts ( MoE ) Architecture : A Deep Dive and Comparison...</a></li>
<li><a href="https://blog.bako.co/deconstructing-the-diffusion-transformer-paradigm">Deconstructing the Diffusion Transformer ( DiT ) Paradigm - BAKO Blog</a></li>
<li><a href="https://www.lmsys.org/blog/2026-08-05-glmImage-optimization/">Full-Stack Performance Optimization of AR + DiT in... - LMSYS Org</a></li>

</ul>
</details>

**标签**: `#AI music generation`, `#MoE`, `#AR+DiT`, `#natural language processing`, `#audio synthesis`

---

<a id="item-11"></a>
## [新浪云 SAE 永久下线，早期 B 站视频源文件随之消失](https://tracker.archiveteam.org/sinavideo/#show-all) ⭐️ 8.0/10

2009 年上线的国内首个 PaaS 平台新浪云 SAE 将于 2026 年 9 月 16 日 24 时正式永久下线，所有用户数据将被彻底删除。仍存放在新浪云 S3 桶中约 420 TB 的早期 B 站视频源文件将随之消失，而 Archive Team 的分布式归档项目已抢救约 680 TB 数据，完成度达 96.26%。 这标志着国内首个公有 PaaS 平台在运营近 17 年后彻底退出历史舞台，也意味着中国早期互联网视频历史可能永久丢失。它凸显了云平台关停可能悄无声息地摧毁文化遗产，也凸显了志愿者数字保存行动的关键作用。 新浪云于 2026 年 6 月 10 日向用户发送服务终止通知，确认 2026 年 9 月 16 日下线。Archive Team 的抢救行动是一个分布式志愿者项目，一旦平台下线，剩余 3.74% 的数据可能永久丢失。

telegram · zaihuapd · 9月16日 15:00

**背景**: 新浪云 SAE（前身 Sina App Engine）于 2009 年上线，是中国最早的公有云服务商之一，专注 PaaS 领域，提供网站、存储、数据库、缓存、队列、安全等服务，拥有近百万开发者和上万家企业用户。PaaS（平台即服务）让开发者无需管理底层服务器即可部署和运行应用，SAE 因此以低成本和免运维成为大量开发者的首选。Archive Team 是由 Jason Scott 于 2009 年联合创立的志愿者组织，专门抢救濒危在线服务上的内容，此前曾保存过 GeoCities、Yahoo! Video、Google Video 和 TwitPic 等。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wanyr.com/2026/06/新浪云（sae）宣布9月16日永久关停：国内首家paas平台17.html">新浪云（SAE）宣布9月16日永久关停：国内首家PaaS平台17年历程落幕</a></li>
<li><a href="https://en.wikipedia.org/wiki/Archive_Team">Archive Team</a></li>
<li><a href="https://sae.sinacloud.com/">网站连接 - 新浪云计算</a></li>

</ul>
</details>

**标签**: `#cloud-computing`, `#digital-preservation`, `#PaaS`, `#Bilibili`, `#data-loss`

---

<a id="item-12"></a>
## [美光发布全球首款 512GB DDR5 RDIMM，计划 2027 年量产](https://videocardz.com/newz/micron-says-worlds-first-512gb-ddr5-module-will-be-production-ready-for-2027) ⭐️ 8.0/10

美光宣布推出全球首款面向服务器的 512GB DDR5 RDIMM，速率最高可达 9200 MT/s，并采用 3D 堆叠 DRAM 芯片。该公司表示该模组将于 2027 年具备量产条件，AMD 和 Intel 正在为未来服务器平台进行验证。 这标志着数据中心内存密度的重大突破，24 根模组即可为单台服务器提供 12TB 内存，使更大的 AI/ML 模型和内存数据库能在更少的系统上运行。单根模组功耗降低超过 60%，也有助于缓解高密度服务器部署日益增长的能源成本。 每根 512GB 模组功耗为 16W，而四根 128GB 模组达到相同容量时功耗为 44.2W，降幅超过 60%。该模组采用 3D 堆叠 DRAM，正由 AMD 和 Intel 验证，但预计要到 2027 年才能量产。

telegram · zaihuapd · 9月16日 16:15

**背景**: DDR5 RDIMM 是服务器中使用的带寄存器 DIMM 规格，寄存器芯片对地址和命令信号进行缓冲，以提高稳定性并支持更高容量。3D 堆叠 DRAM 是指将多个 DRAM 裸片垂直堆叠，并通过硅通孔（TSV）连接，这一技术因高带宽内存（HBM）而普及，可在小尺寸内提升密度和带宽。美光将这一技术应用于标准 RDIMM 模组值得关注，因为它将类似 HBM 的密度带入了传统服务器内存插槽。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/micron-crams-512-gb-memory-into-single-ddr5-stick-next-gen-intel-amd-servers/">Micron Crams 512 GB Memory Into A Single DDR5 Stick, Pushing...</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#DDR5`, `#memory`, `#server hardware`, `#Micron`, `#3D stacking`

---