---
layout: default
title: "Horizon Summary: 2026-09-16 (ZH)"
date: 2026-09-16
lang: zh
---

> 从 89 条内容中筛选出 14 条重要资讯。

---

1. [TypeSafe AI 发布 System One 模型与 Jev 类型化推理系统](#item-1) ⭐️ 8.0/10
2. [电子墨水相框聆听鸟鸣并用 19 世纪风格绘制鸟类](#item-2) ⭐️ 8.0/10
3. [黑客入侵 Flock 车牌识别摄像头，暴露未加密数据](#item-3) ⭐️ 8.0/10
4. [Apple Reference Image：加密照片验证新方案](#item-4) ⭐️ 8.0/10
5. [互联网档案馆因 Wayback Machine 遭大规模抓取而增设防护](#item-5) ⭐️ 8.0/10
6. [谷歌发布 Gemini 3.8 Live 与 Live Extended Thinking 语音模型](#item-6) ⭐️ 8.0/10
7. [作者称即便解决纳维-斯托克斯问题，仍看空大语言模型](#item-7) ⭐️ 8.0/10
8. [FPGA 项目重现 3dfx Voodoo 显卡与 90 年代末游戏 PC](#item-8) ⭐️ 8.0/10
9. [SemiAnalysis：Vera Rubin NVL72 智能体推理每美元性能提升 67 倍](#item-9) ⭐️ 8.0/10
10. [SemiAnalysis：端侧与数据中心 AI 推理的经济性对比](#item-10) ⭐️ 8.0/10
11. [Prior Labs 发布 TabPFN-3.5，新的表格基础模型 SOTA](#item-11) ⭐️ 8.0/10
12. [英特尔 CEO：CPU 仅满足五成需求，14A 明年一季度投产，新架构或使推理功耗降至 GPU 的 1/15](#item-12) ⭐️ 8.0/10
13. [Cloudflare 推出新设置：可禁止 AI 训练同时保留搜索收录](#item-13) ⭐️ 8.0/10
14. [新浪云 SAE 永久下线，早期 B 站视频源文件全部消失](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TypeSafe AI 发布 System One 模型与 Jev 类型化推理系统](https://typesafe.ai/blog/introducing-system-one-models-and-jev) ⭐️ 8.0/10

TypeSafe AI 发布了其首个 System One 模型 Jev，这是一类全新的前沿模型，专为做出软件可直接使用的快速结构化决策而构建，返回的是类型化答案和概率，而非自由文本。该公司声称 Jev 的运行速度比通用生成模型快约 200 倍，成本为每百万 token 0.042 美元，目前已开放早期访问。 这标志着从通用文本生成向分类、路由、评分和抽取等狭窄的、输出受限任务的转变，有望让由 LLM 驱动的自动化在生产软件中大幅降低成本和提升速度。它也引发了关于专用类型化推理模型能否取代还是仅补充通用生成模型的争论。 Jev 返回的是类型化决策而非文本，其“零幻觉”的说法实际上是一种狭窄的类型安全保证，而非通用的正确性承诺。据报道，一项独立测试发现了 7 个缺陷中的 6 个，而且与生成模型的速度对比被批评为具有误导性，因为图灵完备的生成模型原则上可以完成 Jev 能做的任何事情。

hackernews · albelfio · 9月15日 19:25 · [社区讨论](https://news.ycombinator.com/item?id=49717558)

**背景**: System One 模型是一类专为做出软件可直接使用的快速结构化决策而构建的 AI 模型，它评估状态并返回类型化答案和概率。Jev 是 TypeSafe 的旗舰模型，也是首个 System One 模型，面向分类、路由、评分和抽取等手写逻辑过于脆弱的任务。结构化输出已成为 LLM 应用中的常见模式，让模型能够为文档抽取、工单分类和智能体路由等任务返回严格的 JSON schema。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://typesafe.ai/">Home - TypeSafe AI</a></li>
<li><a href="https://docs.typesafe.ai/concepts/system-one">System One - TypeSafe AI</a></li>
<li><a href="https://www.orcarouter.ai/blog/jev-typesafe-system-one-what-we-know">Jev : TypeSafe's Decision Model, Speed and Cost Explained</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞这次发布确实有趣且新颖，有人表示 home assistant 演示让价值变得直观，还有人提到家谱匹配是一个真实用例。然而，也有多人质疑其定位和速度对比，认为图灵完备的生成模型可以完成 Jev 能做的任何事情，而 Jev 仅限于结构化输出，因此这种对比具有误导性。

**标签**: `#LLM`, `#structured-output`, `#typed-inference`, `#AI`, `#system-design`

---

<a id="item-2"></a>
## [电子墨水相框聆听鸟鸣并用 19 世纪风格绘制鸟类](https://github.com/arnegiacomo/fugleramme) ⭐️ 8.0/10

开发者 Arne Munthe-Kaas 制作了一个电子墨水相框，它能持续聆听鸟鸣，利用 BirdNET 神经网络识别鸟种，然后以 19 世纪插画风格生成该鸟的图画。这个名为“fugleramme”（挪威语“鸟框”）的项目以 Show HN 形式发布在 Hacker News 上。 该项目展示了如何将低功耗电子墨水硬件与设备端机器学习和生成艺术相结合，在家庭中创造氛围感十足的奇妙体验。它也凸显了开源鸟类监测工具生态的成长，以及嵌入式系统在典型智能家居设备之外的创意潜力。 BirdNET 是一个传统的卷积神经网络，经过训练可从声音中识别超过 3000 种鸟类，而非大语言模型。电子墨水屏仅在图像变化时耗电，因此该相框可用小电池长时间运行，尤其是搭配蓝牙低功耗等低功耗无线技术而非 Wi-Fi 时。

hackernews · arnemunthekaas · 9月15日 12:31 · [社区讨论](https://news.ycombinator.com/item?id=49711544)

**背景**: BirdNET 是康奈尔鸟类学实验室和开姆尼茨工业大学合作的开源研究项目，利用神经网络从音频录音中识别鸟种。电子墨水（e-ink）是一种模拟纸张的显示技术，通过移动带电颜料颗粒成像，仅在内容变化时耗电。生成艺术使用算法（通常是 AI 模型）创作图像；在此项目中，它生成模仿 19 世纪博物学绘画风格的插画。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://jiclcd.com/what-is-e-ink-display-technology/">What Is E - Ink Display Technology ? Complete Guide to E-Paper...</a></li>

</ul>
</details>

**社区讨论**: 评论者非常热情，称该项目“神奇”且是各种想法的完美融合。有人指出 BirdNET 是传统神经网络而非大语言模型；另一位分享了自己的电子墨水项目，并称赞蓝牙低功耗电子墨水驱动的电池续航。还有人链接了相关鸟类项目，并开玩笑说“以鸟类为载体的 IP 传输”终于要实现了。

**标签**: `#e-ink`, `#bird-classification`, `#embedded-systems`, `#generative-art`, `#hardware`

---

<a id="item-3"></a>
## [黑客入侵 Flock 车牌识别摄像头，暴露未加密数据](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 8.0/10

黑客通过物理方式接触了一台 Flock Safety 自动车牌识别（ALPR）摄像头，并提取了其中存储的数据，发现该设备以未加密形式保存日志和图像。对摄像头记录的分析显示，其约 21 天的活动期间拍摄了约 50,200 辆车，生成了约 160 万张图像，典型一天记录约 3,300 辆车，最高达到 4,454 辆。 此次入侵事件凸显出，如果自动车牌识别监控基础设施未得到妥善保护，可能会泄露敏感的位置数据，从而对被记录行踪的公众构成严重的隐私和公民自由担忧。这也加剧了对 Flock Safety 安全实践的审视，并可能加速对 ALPR 系统实施更严格监管的呼声。 该摄像头以未加密方式存储数据，意味着任何有物理接触机会的人都可以直接取走数据，日志覆盖多个时间段，总计约 21 天。此次报道与 404 Media 合作完成，透明度组织 Distributed Denial of Secrets 发布了该摄像头数据的分区镜像。

hackernews · driverdan · 9月16日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49726586)

**背景**: 自动车牌识别（ALPR）是 AI 驱动的摄像头，能够拍摄并分析过往车辆的图像，存储车辆位置、日期和时间等细节；在美国通常称为 ALPR 而非 ANPR。Flock Safety 是此类摄像头的主要供应商，执法机构用它来将车牌与监视名单、被盗车辆数据库和 AMBER 警报进行交叉比对。隐私倡导者长期警告此类系统会生成详细的移动记录，而以往研究已在其他监控设备（包括家庭安全摄像头和追踪器）中发现未加密数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deflock.org/">DeFlock is an open-source project that maps license plate readers ...</a></li>
<li><a href="https://trafficvision.live/blog/flock-cameras">Flock Cameras : What They Are & Can You Watch... | TrafficVision.Live</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automatic_number-plate_recognition">Automatic number- plate recognition - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对数据未加密且可被物理获取表示震惊，有人称他们“对 Flock 说的任何话都零信任”。其他人提到了与 404 Media 的合作以及 Distributed Denial of Secrets 发布分区镜像，还有一位评论者以新罕布什尔州对非命中车牌数据严格的 3 分钟删除规则作对比，指出这与发现的 21 天日志形成反差。

**标签**: `#security`, `#privacy`, `#surveillance`, `#ALPR`, `#data-breach`

---

<a id="item-4"></a>
## [Apple Reference Image：加密照片验证新方案](https://security.apple.com/blog/apple-reference-image/) ⭐️ 8.0/10

Apple 推出了 Apple Reference Image，这是 iPhone 18 Pro 上的一种可选相机模式，利用加密硬件认证生成带有安全时间戳的参考图像，证明相机传感器实际拍摄到的内容。该系统从相机传感器到最终处理建立了一条信任链，为图像添加加密封印，以抵御 AI 生成和编辑的伪造图像。 这是一项具有重大隐私、安全和社会影响的技术进展，因为它可能使身份验证和保险理赔从需要智能手机转变为需要 iPhone。它还引发了更广泛的问题：验证光子是否真正解决了验证事件真相的问题。 该系统依赖闭源组件，并将每张经过验证的“已显影”图像上传到 Apple 的服务器，而且它无法应对重放攻击——即把修改过或 AI 生成的图像显示在高分辨率显示器上再拍摄下来。批评者指出，信任链的许多环节是闭源的，使得正确性假设难以审计。

hackernews · imwally · 9月16日 02:07 · [社区讨论](https://news.ycombinator.com/item?id=49721322)

**背景**: 加密硬件认证是一种安全机制，设备的硬件和固件会生成关于自身状态的加密证明，而不是依赖软件简单地声称完整性。Apple Reference Image 将这一概念应用于摄影，从相机传感器到最终图像建立可验证的信任链，使查看者能够检查照片是否由 iPhone 未经篡改地拍摄。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://security.apple.com/blog/apple-reference-image/">Apple Reference Image: A New Approach for Verified Photography - Apple Security Research</a></li>
<li><a href="https://appleinsider.com/articles/26/09/09/apple-reference-image-is-a-new-way-to-authenticate-iphone-photography">Apple Reference Image is a new way to authenticate iPhone photography</a></li>
<li><a href="https://www.securview.com/ai-security-essentials/hardware-attestation">Hardware Attestation : Definition and Key Concepts</a></li>

</ul>
</details>

**社区讨论**: 评论者认为这一方案很巧妙，但提出了严重担忧：通过拍摄显示器进行重放攻击、信任链的复杂性和闭源性质、强制上传到 Apple 服务器，以及“认证真实”标签可能让人们不加辨别地接受误导性叙事的风险。一些人还警告说，这可能使日常生活从需要智能手机转变为需要 iPhone。

**标签**: `#Apple`, `#cryptography`, `#photo verification`, `#privacy`, `#security`

---

<a id="item-5"></a>
## [互联网档案馆因 Wayback Machine 遭大规模抓取而增设防护](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) ⭐️ 8.0/10

2026 年 9 月 15 日，互联网档案馆宣布 Wayback Machine 遭到一波波高流量自动化流量的冲击，并已部署新的防护措施以维持服务运行。档案馆承认部分防护措施误伤了正常用户，并警告称由于抓取压力，一些网站已经选择退出被存档。 互联网档案馆是记者、研究人员、律师和事实核查人员依赖的关键公共基础设施，因此持续的抓取压力既威胁服务可用性，也威胁历史网络记录的完整性。如果更多网站所有者选择退出存档，Wayback Machine 作为共享公共档案的价值可能会随时间逐渐削弱。 档案馆将这股流量归因于抓取者试图绕过对原始网站的封锁，转而从 Wayback Machine 的副本中提取内容，并指出其反制措施无意中屏蔽了一些真实用户。历史上，网站所有者可以通过 robots.txt 选择退出，一份公开名单显示约有 3800 个网站已明确将自己排除在抓取范围之外。

hackernews · ChrisArchitect · 9月15日 17:52 · [社区讨论](https://news.ycombinator.com/item?id=49716176)

**背景**: Wayback Machine 是互联网档案馆用于长期保存网页快照的工具，让任何人都能查看网站过去的样子，即使网站已经改版或下线。网站所有者传统上可以通过 robots.txt 标准选择退出存档，该标准告诉爬虫可以访问网站的哪些部分。抓取器是规模化采集数据的自动化程序，当它们瞄准 Wayback Machine 时，会消耗普通访客同样需要的带宽和服务器资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/">An Update on Wayback Machine Access | Internet Archive Blogs</a></li>
<li><a href="https://www.digitalinformationworld.com/2026/09/internet-archives-wayback-machine.html">Internet Archive's Wayback Machine Blocks Some Real Users Amid High ...</a></li>
<li><a href="https://www.stefanjudis.com/blog/the-internet-archive-opt-out-itch/">The Internet Archive opt out itch | Stefan Judis Web Development</a></li>

</ul>
</details>

**社区讨论**: 评论者大多称赞互联网档案馆是至关重要的基础设施并呼吁捐款，simonw 则认为这些流量很可能来自试图绕过原始网站封锁的抓取者。一些用户分享了找回丢失内容的个人经历，另一些人则担心礼貌的抓取者会被误伤，或担忧档案馆的长期生存。

**标签**: `#internet-archive`, `#web-scraping`, `#digital-preservation`, `#open-access`, `#infrastructure`

---

<a id="item-6"></a>
## [谷歌发布 Gemini 3.8 Live 与 Live Extended Thinking 语音模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) ⭐️ 8.0/10

谷歌发布了 Gemini 3.8 Live 和 Gemini 3.8 Live Extended Thinking，这是其目前最先进的实时对话模型，专为自然流畅的实时语音交流而打造。其中 Extended Thinking 版本是一款高推理能力的音频到音频模型，专为实时语音交互中的复杂多步问题求解而设计。 此次发布推动了实时、低延迟语音 AI 的发展，让用户能够与模型进行自然的语音对话，同时模型还能在后台处理更复杂的推理任务。这对语音助手的开发者和使用者都很重要，并在 Hacker News 上引发热议，获得 464 分和 309 条评论。 根据 Google DeepMind 的模型卡，Gemini 3.8 Audio 系列模型兼具成本效益与速度，针对实时交互等高频、低延迟任务进行了优化。Extended Thinking 版本则特别推荐用于语音对话中需要更高后台推理能力来完成的复杂多步问题求解场景。

hackernews · leumon · 9月15日 17:38 · [社区讨论](https://news.ycombinator.com/item?id=49715947)

**背景**: Gemini 是谷歌的旗舰级原生多模态 AI 模型系列，能够同时处理文本、音频、图像等多种输入。3.8 代是在此前 3.7 和 3.8 Flash 发布之后推出的，而“Live”这一名称指的是针对实时对话场景而非批量文本生成进行调优的模型。“Extended Thinking”则指模型在作答前投入额外算力进行内部推理的模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-audio/">Gemini 3.8 Audio (Live, Live Extended Thinking) - Model Card — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking">Gemini 3.8 Live Extended Thinking | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评价褒贬不一：一位用户盛赞 Gemini 的南非荷兰语对话与语法辅导是亮点用例，另一位则称此次发布扎实，口音处理出色、声音悦耳、延迟低，而且终于可以在工作区账户上使用。也有人提出批评，一位用户抱怨 Gemini 有时在紧接着的下一条消息中就丢失上下文，还会插入未经请求的产品链接；还有用户质疑，尽管谷歌拥有数据、TPU 和广告资金优势，为何仍落后于竞争对手。

**标签**: `#Gemini`, `#Google`, `#LLM`, `#AI`, `#model release`

---

<a id="item-7"></a>
## [作者称即便解决纳维-斯托克斯问题，仍看空大语言模型](https://dank.systems/posts/2026-09-15-ai-bear.html) ⭐️ 8.0/10

一篇题为《为什么在纳维-斯托克斯之后我仍看空大语言模型》的博客文章认为，即便模型能解决纳维-斯托克斯这类高难度技术问题，也不代表大语言模型具有广泛价值，因为它们缺乏大多数真实商业场景所需的隐性知识和战略思维。该文在 Hacker News 上引发热议，获得 352 分、447 条评论。 该文为“前沿 AI 实验室很快将自动化大部分知识工作”的叙事提供了一个务实的反例，对投资者、正在评估 AI 落地的企业以及判断大语言模型实际适用边界的从业者都有参考价值。它还凸显了基准测试式的技术胜利与现实中定义模糊、杂乱无章的业务问题之间的鸿沟。 作者认为，只有少数几类企业能接受完全自主的大语言模型应用，例如能承受低成本失败的企业（如实习生级别或快速原型类工作），或任务定义狭窄、护栏清晰的企业。评论者引用了一篇 2026 年 4 月的 arXiv 论文（2509.24239v4）：前沿模型在下棋时识别合法走法的准确率不超过 80%，即便被明确告知哪些走法合法，仍会继续请求非法走法。

hackernews · jaykru · 9月15日 17:37 · [社区讨论](https://news.ycombinator.com/item?id=49715927)

**背景**: 纳维-斯托克斯方程描述黏性流体的运动，是空气动力学、气象建模等领域的核心方程；与之相关的“存在性与光滑性”问题是七个千禧年大奖难题之一。2026 年 9 月，OpenAI 宣布了一个据称是该问题的反例，随后引发优先权争议，且尚未得到独立验证。文章讨论的核心概念是“隐性知识”——人类处理定义模糊问题时依赖的、难以言传的经验性知识，而 AI 系统被认为缺乏这种知识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_equations">Navier-Stokes equations</a></li>
<li><a href="https://medium.com/@bruno_7636/the-knowledge-ai-cant-have-why-friction-still-matters-d2a5cebdad06">The Knowledge AI Can’t Have: Why Friction Still Matters | Medium</a></li>
<li><a href="https://aldeiadaponte.com/autonomous-llm-agents-real-world-capabilities-and-current-limits">Autonomous LLM Agents : Real-World Capabilities and Current Limits</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍称赞该文是对大语言模型可实现价值最务实的分析之一，多人认为 AI 缺乏隐性知识和战略思维，并举例说客服 AI 代理上线后因缺乏这些能力而失败。也有人质疑文章关于前沿实验室估值的论断前提，还有评论者批评文章不使用句子首字母大写，阅读起来十分吃力。

**标签**: `#LLM`, `#AI criticism`, `#tacit knowledge`, `#autonomous agents`, `#Hacker News`

---

<a id="item-8"></a>
## [FPGA 项目重现 3dfx Voodoo 显卡与 90 年代末游戏 PC](https://nand2mario.github.io/posts/2026/zsst-voodoo/) ⭐️ 8.0/10

一位开发者在 nand2mario 博客上发布了一个详细项目，在 FPGA 上重现了 3dfx 的 Voodoo Graphics 显卡以及一台完整的 90 年代末游戏 PC。该项目以可编程硬件实现原始 GPU 逻辑，而非通过软件模拟，引发了关于硬件复刻与底层 GPU 内部结构的讨论。 这是复古计算与硬件模拟领域的一项重要成就，表明即便是 90 年代复杂的 3D 加速卡也能在 FPGA 结构中忠实重现。它可能推动对老式 PC 游戏硬件更精确的保存，并加深公众对早期 GPU 内部工作原理的理解。 该项目针对的是 3dfx 最初推出的 Voodoo Graphics 芯片组——3dfx 在 90 年代中期发布的先驱性 3D 加速卡，并搭配了符合时代背景的其余游戏 PC 组件。由于 FPGA 实现将原始设备逻辑直接映射到硬件中，因此能够实现软件模拟器往往难以达到的时序精度。

hackernews · zdw · 9月15日 22:50 · [社区讨论](https://news.ycombinator.com/item?id=49719938)

**背景**: 3dfx Interactive 是一家成立于 1994 年的美国硬件公司，凭借 Voodoo 系列 GPU 开创了消费级 3D 图形先河，为 90 年代末的众多 PC 游戏提供动力，随后在 2000 年代初走向衰落。FPGA 即现场可编程门阵列，是一种在制造后仍可重新配置逻辑的芯片，使爱好者能够在硬件层面而非软件模拟层面重现经典计算机和游戏机。MiSTer 等项目让这种方法在复古游戏中流行起来，而 Voodoo 显卡因其复杂的 3D 流水线而成为尤为雄心勃勃的目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/3dfx">3 dfx - Wikipedia</a></li>
<li><a href="https://emulation.gametechwiki.com/index.php/FPGA">FPGA - Emulation General Wiki</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hardware_emulation">Hardware emulation - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对该项目表示赞赏，并指出 MiSTer 是一个相关的基于 FPGA 的硬件复刻项目；一位用户分享了为购买 Voodoo 3000 PCI 而攒钱的怀旧经历以及随之而来的后悔。另一位评论者指出，近年来关于底层 GPU 内部结构的文章大幅增加，并认为一旦将 GPU 视为一种专用于图形处理、拥有自己指令集和内存的处理器，实现一个 GPU 在概念上就变得相当直接。

**标签**: `#FPGA`, `#retro-computing`, `#hardware-emulation`, `#GPU`, `#Voodoo-Graphics`

---

<a id="item-9"></a>
## [SemiAnalysis：Vera Rubin NVL72 智能体推理每美元性能提升 67 倍](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-agentic-inference) ⭐️ 8.0/10

SemiAnalysis 发布了对 NVIDIA Vera Rubin NVL72 机架级平台的分析，声称其在智能体推理工作负载上实现了每美元 67 倍的性能提升。报告还指出该系统每吉瓦年利润翻倍，并强调 NVIDIA 的“极致协同设计”战略，同时暗示黄仁勋再次“压低”了性能数据。 该分析的重要性在于，它量化了 NVIDIA 机架级协同设计系统如何大幅降低运行智能体 AI 工作负载的成本，而这类工作负载正成为主流生产用例。每吉瓦利润的框架也表明，AI 基础设施的经济性正从单纯的芯片规格转向数据中心级别的效率。 Vera Rubin NVL72 在单个液冷机架中集成了 72 块下一代 Rubin GPU 和 36 颗 Vera CPU，通过 NVLink 6 互连，提供 3.6 exaFLOPS 的 AI 性能和 75TB 内存。67 倍的每美元性能提升这一说法特指智能体推理，即涉及有状态、多轮工作流而非单次模型补全的场景。

rss · Semianalysis · 9月14日 22:08

**背景**: 智能体推理是指 AI 智能体在推理、选择动作、使用工具、回顾先前上下文并更新下一步时所遵循的完整执行路径，这使其成为一种有状态的工作流，不同于简单的单轮推理。NVIDIA 的“极致协同设计”方法将硬件、软件和模型一起优化，以最大化 AI 工厂吞吐量并最小化 token 成本，超越了单纯的芯片峰值规格。Vera Rubin NVL72 是基于第三代 MGX 设计的机架级系统，支持无电缆模块化和快速部署，适用于关键任务 AI 工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">NVIDIA Vera Rubin NVL72 | Co-Designed Infrastructure for Agentic AI</a></li>
<li><a href="https://nhimg.org/glossary/agentic-inference/">What Is Agentic Inference? Definition & Examples</a></li>
<li><a href="https://developer.nvidia.com/blog/building-for-the-rising-complexity-of-agentic-systems-with-extreme-co-design/">Building for the Rising Complexity of Agentic Systems with Extreme ...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI Inference`, `#Hardware Acceleration`, `#Performance Optimization`, `#Agentic AI`

---

<a id="item-10"></a>
## [SemiAnalysis：端侧与数据中心 AI 推理的经济性对比](https://newsletter.semianalysis.com/p/a-brain-too-big-to-carry-on-device) ⭐️ 8.0/10

SemiAnalysis 发布了一篇深度分析文章，对比端侧与数据中心 AI 推理，重点探讨机器人模型、芯片效率、NVIDIA Jetson Thor 与 B300 的总拥有成本（TCO）、部署策略以及网络限制。 该分析对 AI/ML 系统和硬件领域高度相关，可能影响企业决定在何处运行推理工作负载，在边缘设备与数据中心之间权衡延迟、成本和可扩展性。 文章对比了 NVIDIA Jetson Thor（一款机器人计算机，提供高达 2070 FP4 TFLOPS 算力和 128 GB 内存）与 B300 数据中心 GPU（配备 288 GB HBM3e 和 8 TB/s 带宽），强调了在总拥有成本和实时应用网络限制方面的权衡。

rss · Semianalysis · 9月14日 16:37

**背景**: 端侧推理在手机、机器人或汽车等本地硬件上运行 AI 模型，提供低延迟和隐私保护；而数据中心推理则使用强大的云 GPU 处理繁重工作负载。NVIDIA 的 Jetson Thor 专为物理 AI 和机器人设计，而 B300（Blackwell Ultra）则面向数据中心的高内存训练和推理。两者之间的选择涉及性能、成本和网络依赖性的权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/embedded/jetson-modules">Jetson Modules, Support, Ecosystem, and Lineup | NVIDIA Developer</a></li>
<li><a href="https://www.together.ai/gpu/nvidia-hgx-b300">NVIDIA HGX B 300 Cluster Pricing & Specs | Rent HGX B 300 GPUs</a></li>
<li><a href="https://www.etfpedia.wiki/compare/ai-on-device-vs-ai-inference-infrastructure/">AI On - Devices vs AI Inference Infrastructure | ETFpedia</a></li>

</ul>
</details>

**标签**: `#AI inference`, `#edge computing`, `#hardware`, `#robotics`, `#TCO`

---

<a id="item-11"></a>
## [Prior Labs 发布 TabPFN-3.5，新的表格基础模型 SOTA](https://www.reddit.com/r/MachineLearning/comments/1wh4xhy/tabpfn35_is_released_as_the_next_sota_tabular/) ⭐️ 8.0/10

Prior Labs 发布了 TabPFN-3.5，这是一款新的表格基础模型，在 TabArena 和 BeyondArena 两个基准测试上均排名第一，并在高达 100 万行、2 万特征的数据集上达到 SOTA。此次发布包含三个变体：TabPFN-3.5-Fast（alpha 阶段，比基础模型快 6 倍）、TabPFN-3.5-Thinking（通过 API 以计算换精度）以及 TabPFN-3.5-Plus。 表格数据在现实企业级和科学应用中仍占主导地位，因此新的 SOTA 基础模型会直接影响在梯度提升树与深度模型之间做选择的机器学习从业者。尤其在文本丰富、高基数和高维数据上的显著 Elo 提升，表明基础模型正在缩小此前有利于树模型方法的差距。 在 BeyondArena 上，TabPFN-3.5 比此前最强基线高出 250 Elo，比此前总榜领先者高出 150 Elo；而 TabPFN-3.5-Thinking 在 BeyondArena 上比基础模型再高 20 Elo，在 TabArena 上高 44 Elo。Fast 变体仍处于 alpha 阶段，Thinking 变体则只能通过 API 使用。

reddit · r/MachineLearning · /u/tuanacelik · 9月15日 16:18

**背景**: TabPFN 是 Prior Labs 推出的基于 Transformer 的基础模型，利用上下文学习在一次前向传播中解决表格预测问题，而无需针对每个数据集单独训练。TabArena 是一个持续纳入新数据集和模型的“活”基准，用于表格机器学习评测；BeyondArena 则是较新的统一基准，覆盖 142 个精选数据集上的 IID、时序和分组任务。此前的 TabPFN 版本（2.5、2.6、3）均以非商业许可证发布，公开仓库中默认使用 TabPFN-3。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://priorlabs.ai/tabpfn-2">TabPFN | Prior Labs</a></li>
<li><a href="https://github.com/PriorLabs/TabPFN">GitHub - PriorLabs/ TabPFN : TabPFN : Foundation Model for Tabular ...</a></li>
<li><a href="https://arxiv.org/abs/2506.16791">TabArena : A Living Benchmark for Machine Learning on Tabular Data</a></li>

</ul>
</details>

**标签**: `#tabular-data`, `#foundation-models`, `#machine-learning`, `#benchmarking`, `#SOTA`

---

<a id="item-12"></a>
## [英特尔 CEO：CPU 仅满足五成需求，14A 明年一季度投产，新架构或使推理功耗降至 GPU 的 1/15](https://wallstreetcn.com/articles/3781851) ⭐️ 8.0/10

英特尔 CEO 陈立武表示，受 AI 智能体扩张带动，公司目前只能满足前沿客户约 50%的 CPU 需求。他还确认 18A 制程已全面量产，14A 制程将于 2027 年一季度投产，同时英特尔正布局数据流架构、晶圆级扩展和神经形态计算，称相关芯片在特定推理场景下可用 GPU 1/10 至 1/15 的功耗实现同等性能。 CPU 供应短缺表明 AI 驱动的需求正超过英特尔的制造能力，这对构建智能体 AI 系统的云服务商和企业而言是一大隐忧。14A 的时间表以及宣称的 10 至 15 倍推理功耗优势，使英特尔得以与英伟达等以 GPU 为中心的 AI 硬件领导者竞争，若该架构兑现承诺，可能重塑 AI 推理的经济性。 据报道，14A 节点在缺陷密度降低方面领先于 18A，英特尔目标是在 2027 年一季度将 D0 控制在 0.1 至 0.2。所宣称的 1/10 至 1/15 功耗效率仅适用于特定推理场景，且英特尔已承认，如果外部客户不采用 14A，可能彻底放弃先进制造。

telegram · zaihuapd · 9月16日 04:15

**背景**: 英特尔的 18A 和 14A 是以埃为单位的先进制程节点，数字越小通常意味着芯片密度更高、能效更好；18A 是英特尔当前的主力节点，14A 则是下一代继任者。神经形态计算通过人工神经元和事件驱动处理模拟大脑结构以提升能效，而数据流架构则优化数据在芯片中的流动方式，而非单纯依赖原始算力，这对 AI 推理工作负载日益重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/intels-defect-density-minimization-for-its-14a-node-is-currently-tracking-3-4-quarters-ahead-of-the-18a-node-trajectory-indicating-an-earlier-launch/">Intel 's Defect Density Minimization For Its 14 A Node Is Currently...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neuromorphic_computing">Neuromorphic computing</a></li>
<li><a href="https://datacentremagazine.com/news/sambanovas-dataflow-architecture-the-natural-flow-of-ai">SambaNova's Dataflow Architecture : The natural Flow of AI</a></li>

</ul>
</details>

**标签**: `#Intel`, `#semiconductor`, `#AI hardware`, `#inference`, `#process node`

---

<a id="item-13"></a>
## [Cloudflare 推出新设置：可禁止 AI 训练同时保留搜索收录](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/) ⭐️ 8.0/10

9 月 15 日，Cloudflare 宣布推出新的“禁止 AI 训练”设置，允许网站继续被搜索引擎收录，同时阻止同一批爬虫用其内容训练 AI 模型。苹果、谷歌和微软已经遵守或承诺在规定时间内遵守这一设置。 这解决了行业的一大痛点，让内容发布者既能保护自己的内容不被用于 AI 训练，又不必牺牲搜索曝光度，而搜索流量对网站的访问量和收入至关重要。苹果、谷歌和微软的支持标志着网络内容控制和 AI 伦理方面的重大转变，可能影响其他平台处理爬虫权限的方式。 该设置按域名配置；如果网站选择“阻止”，包括混合用途爬虫在内的所有爬虫都会被拦截，搜索收录也会受到影响。Cloudflare 还计划从明年初开始让网站控制其内容被 AI 摘要引用的比例。

telegram · zaihuapd · 9月16日 05:46

**背景**: 网络爬虫是自动扫描网站的机器人，用于为搜索引擎索引内容或为训练 AI 模型收集数据。过去，网站使用 robots.txt 来管理爬虫访问，但 AI 公司通常为训练和搜索使用不同的爬虫，导致很难只阻止其中一种。Cloudflare 的新设置旨在通过网络层面区分训练爬虫和搜索爬虫，从而简化这一过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/">Have it both ways: stay discoverable in search while... | Cloudflare Blog</a></li>
<li><a href="https://www.playwire.com/blog/ai-training-vs-ai-search-crawlers-does-blocking-ai-training-crawlers-hurt-your-ai-referral-traffic">AI Training vs . AI Search Crawlers : Does Blocking AI Training ...</a></li>
<li><a href="https://www.innflows.com/blog/technology/training-bots-vs-search-crawlers-robots-txt">Training Bots vs Search Crawlers : The robots.txt Split</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#AI training`, `#web crawling`, `#search indexing`, `#content control`

---

<a id="item-14"></a>
## [新浪云 SAE 永久下线，早期 B 站视频源文件全部消失](https://tracker.archiveteam.org/sinavideo/#show-all) ⭐️ 8.0/10

2009 年上线的国内首个 PaaS 平台新浪云 SAE 将于 2026 年 9 月 16 日 24 时正式永久下线，所有用户数据将被彻底删除。早期 B 站存储在该平台上的视频源文件随之丢失，目前仍有约 420 TB 历史数据存于新浪云 S3 桶中，Archive Team 发起的分布式归档项目已累计抢救约 680 TB 数据，完成度达 96.26%。 这标志着中国首个 PaaS 云平台的消失，以及一批早期中国互联网视频历史的流失，凸显了商业云存储在长期数字保存方面的脆弱性。同时也说明志愿归档组织在内容被永久删除前抢救濒危网络资料方面正发挥越来越重要的作用。 下线时间定在 2026 年 9 月 16 日 24 时，此后所有用户数据将被不可逆地删除。Archive Team 的抢救行动已保存约 680 TB 数据，完成度 96.26%，但新浪云 S3 桶中仍有约 420 TB 与 B 站相关的数据，与截止时间的赛跑仍在继续。

telegram · zaihuapd · 9月16日 15:00

**背景**: 新浪云 SAE（Sina App Engine）于 2009 年上线，是中国首个 PaaS（平台即服务）产品，让开发者无需管理服务器即可部署和运行 Web 应用，并因低成本、免运维而广受欢迎。如今已是国内主要视频平台的 B 站，早期曾依赖新浪云存储大量视频源文件。Archive Team 是由 Jason Scott 于 2009 年联合创立的志愿数字保存组织，专门复制面临关停风险的在线服务内容，通常通过 Wayback Machine 向公众开放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Archive_Team">Archive Team</a></li>
<li><a href="https://www.sinacloud.com/sae.html">云 应用 SAE - 云 服务 - 云 托管</a></li>
<li><a href="https://cloud.it168.com/a2012/0719/1374/000001374232_all.shtml">十分钟带你快速了解 新 浪 SAE 云 计算平台- 云 计算专区</a></li>

</ul>
</details>

**标签**: `#cloud-computing`, `#digital-preservation`, `#PaaS`, `#Bilibili`, `#Archive Team`

---