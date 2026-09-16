---
layout: default
title: "Horizon Summary: 2026-09-16 (ZH)"
date: 2026-09-16
lang: zh
---

> 从 87 条内容中筛选出 13 条重要资讯。

---

1. [Typesafe.ai 发布 System One 模型与 Jev 快速类型化推理系统](#item-1) ⭐️ 8.0/10
2. [电子墨水相框聆听鸟鸣并绘制 19 世纪风格插画](#item-2) ⭐️ 8.0/10
3. [互联网档案馆因抓取流量激增为 Wayback Machine 增设防护](#item-3) ⭐️ 8.0/10
4. [谷歌发布 Gemini 3.8 Live 与 3.8 Live Extended Thinking](#item-4) ⭐️ 8.0/10
5. [AI 智能体 25 分钟内发现 Baseten 生产环境 GitHub 管理员令牌](#item-5) ⭐️ 8.0/10
6. [前苹果工程师用 LLM 一个月内为 M4 Mac Mini 打造 Linux GPU 驱动](#item-6) ⭐️ 8.0/10
7. [布鲁斯·施奈尔：25 年大规模监控已然失败](#item-7) ⭐️ 8.0/10
8. [SemiAnalysis：Vera Rubin NVL72 智能体推理每美元性能提升 67 倍](#item-8) ⭐️ 8.0/10
9. [4400 万参数三值 LLM 在 CPU 上以 1900 tok/s 运行，仅 19.8 MB](#item-9) ⭐️ 8.0/10
10. [Prior Labs 发布 TabPFN-3.5，新的表格基础模型 SOTA](#item-10) ⭐️ 8.0/10
11. [中国“十五五”规划瞄准先进芯片与开源鸿蒙](#item-11) ⭐️ 8.0/10
12. [美英立法者推动禁止超级智能 AI 的法案](#item-12) ⭐️ 8.0/10
13. [谷歌向全体工程师开放 Anthropic 的 Claude Opus 5](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Typesafe.ai 发布 System One 模型与 Jev 快速类型化推理系统](https://typesafe.ai/blog/introducing-system-one-models-and-jev) ⭐️ 8.0/10

Typesafe.ai 在其博客上发布了 System One 模型和 Jev，这是一个快速类型化推理系统，通过牺牲通用生成能力来换取速度和结构化输出。该发布在 Hacker News 上迅速获得 819 个赞和 270 条评论，显示出社区的高度关注。 这种方法可以显著降低分类和实时决策等结构化输出任务的成本和延迟，使以前不可行的项目变得可行。它还凸显了一种趋势：将前沿大语言模型中的常见用例蒸馏为更小、更快的专用模型。 Jev 专为机器对机器执行而设计，面向合规流程、实时决策和自主代理，并使用 RLCD（可能指基于社区数据的强化学习）进行训练。它只能生成结构化输出，因此无法像图灵完备的代码模型那样进行通用生成。

hackernews · albelfio · 9月15日 19:25 · [社区讨论](https://news.ycombinator.com/item?id=49717558)

**背景**: 类型化推理是指生成符合预定义模式或类型的输出，确保结构有效性而无需后处理。System One 模型是一类新型 AI，专为快速、直觉式推理而设计，与更慢、更审慎的 System Two 思维相对。Typesafe.ai 是一家隐身模式的 AI 实验室，专注于构建可靠的生产级 AI 工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models and Jev</a></li>
<li><a href="https://news.ycombinator.com/item?id=49717558">Introducing System One Models and Jev | Hacker News</a></li>
<li><a href="https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds">Mini-Vibe Check: TypeSafe's Jev Judged Everything I’ve Written in 0.7 Seconds</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，用户称赞其新颖性以及在分类和记忆系统方面的潜力。一些人质疑速度对比具有误导性，指出通用模型可以做任何事情，而 Jev 仅限于结构化输出。其他人则强调蒸馏角度，认为 Typesafe 可以廉价地从前沿大语言模型中提取常见任务并更快地提供服务。

**标签**: `#AI/ML`, `#typed inference`, `#model distillation`, `#structured output`, `#Hacker News`

---

<a id="item-2"></a>
## [电子墨水相框聆听鸟鸣并绘制 19 世纪风格插画](https://github.com/arnegiacomo/fugleramme) ⭐️ 8.0/10

开发者 Arne Munthe-Kaas（arnegiacomo）在 GitHub 上发布了名为“fugleramme”的项目：一个由 ESP32 微控制器和 BirdNET 声音分类模型驱动的电子墨水相框，它能聆听鸟鸣并显示与之匹配的 19 世纪风格插画。该项目以 Show HN 帖子的形式发布，迅速引发了社区的热烈关注。 该项目展示了如何将廉价的微控制器与现有的生物声学 AI 结合，打造出令人愉悦的低功耗环境设备，从而激励其他创客去构建“有魔力”的日常物品。它也凸显了鸟类监测项目的兴起浪潮，以及 BirdNET 作为一种可访问、非大语言模型的神经网络在现实声音分类中的成熟度。 该相框运行在 ESP32 上——这是乐鑫（Espressif）推出的低成本双核 Wi-Fi/蓝牙微控制器，并使用 BirdNET，一个专为声学鸟类识别开发的传统神经网络（并非大语言模型）。电子墨水屏仅在图像变化时消耗电力，因此非常适合这种在检测到新鸟时才偶尔刷新的设备。

hackernews · arnemunthekaas · 9月15日 12:31 · [社区讨论](https://news.ycombinator.com/item?id=49711544)

**背景**: BirdNET 是康奈尔鸟类学实验室与开姆尼茨工业大学联合开发的广泛使用的 AI 系统，能够从录音中识别鸟类物种，并提供免费的手机应用。电子墨水（电子纸）显示屏模仿纸张上的墨水，无需供电即可保持图像，因此常用于低功耗、常显设备。ESP32 是一种常见的创客微控制器，以极低成本提供 Wi-Fi 和蓝牙连接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://en.wikipedia.org/wiki/ESP32">ESP32 - Wikipedia</a></li>
<li><a href="https://jiclcd.com/what-is-e-ink-display-technology/">What Is E - Ink Display Technology ? Complete Guide to E-Paper...</a></li>

</ul>
</details>

**社区讨论**: 评论者热情高涨，有人称其为“HN 上最酷的东西”并称赞其魔力感；其他人指出 BirdNET 是传统神经网络而非大语言模型，分享了自己的电子墨水项目与电池续航计算，并链接了 birdnet-go 等相关鸟类监测项目。

**标签**: `#e-ink`, `#ESP32`, `#bird-classification`, `#hardware`, `#Show HN`

---

<a id="item-3"></a>
## [互联网档案馆因抓取流量激增为 Wayback Machine 增设防护](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) ⭐️ 8.0/10

互联网档案馆于 2026 年 9 月 15 日发布博客更新，表示 Wayback Machine 遭遇了多轮高流量自动化抓取，并已部署新的防护措施以维持服务运行。档案馆认为，这波流量来自试图绕过原始网站访问限制、转而抓取 Wayback Machine 存档副本的爬虫程序。 互联网档案馆被广泛视为数字保存领域的关键公共基础设施，持续的抓取压力会威胁研究人员、记者和普通用户对历史网页的自由、匿名访问。这一事件也凸显了 AI 驱动的数据采集与保存开放网络的非营利服务之间日益加剧的矛盾。 这些防护措施导致服务不稳定，部分用户遇到 HTTP 429 等限流错误；档案馆还指出，由于抓取行为，一些网站已经选择退出存档。社区成员反映在某个网络下被拦截、换一个网络却能正常访问，说明过滤机制至少部分基于 IP 或网络。

hackernews · ChrisArchitect · 9月15日 17:52 · [社区讨论](https://news.ycombinator.com/item?id=49716176)

**背景**: 互联网档案馆是一家非营利数字图书馆，通过 Wayback Machine 保存公共网页的快照，存档页面数量达数千亿。其爬虫会自动采集大部分内容，该服务通常无需登录即可免费使用。高流量抓取工具和商业抓取 API 会产生巨大的请求负载，因此档案馆现在不得不限流或过滤流量以维持在线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Internet_Archive">Internet Archive - Wikipedia</a></li>
<li><a href="https://github.com/sangaline/wayback-machine-scraper">GitHub - sangaline/wayback-machine-scraper: A command-line utility and Scrapy middleware for scraping time series data from Archive.org's Wayback Machine. · GitHub</a></li>
<li><a href="https://www.proxyrack.com/blog/how-to-safely-scrape-data-from-wayback-machine/">How To Safely Scrape Data From Wayback Machine</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者大多赞赏互联网档案馆的韧性和对开放、匿名访问的坚持，有人指出仍可通过 Tor 访问而不必经过中心化网关。也有人建议推出付费捐赠档位以换取更高的速率限制，分享了在某些网络遇到 429 错误而在其他网络正常的困惑经历，并认为从抓取数据中获利的 AI 公司应当向档案馆付费。

**标签**: `#internet-archive`, `#wayback-machine`, `#web-scraping`, `#digital-preservation`, `#infrastructure`

---

<a id="item-4"></a>
## [谷歌发布 Gemini 3.8 Live 与 3.8 Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) ⭐️ 8.0/10

谷歌发布了 Gemini 3.8 Live 和 Gemini 3.8 Live Extended Thinking，称其为迄今最先进的实时对话模型，并于 2026 年 9 月 15 日正式开放使用。Gemini 3.8 Live 提供快速流畅的实时语音对话，支持视觉和语言理解；而 Extended Thinking 版本则在实时语音交互中增加了更强的后台推理能力，用于处理复杂、多步骤的任务。 此次发布让实时语音 AI 更接近自然的人类对话，模型可以在不打断对话的情况下在后台完成推理和工具调用。这对 Gemini Live、Gmail 及其他谷歌产品的用户意义重大，同时也提高了与 OpenAI 等竞争对手实时音频模型之间的竞争门槛。 Gemini 3.8 Live 基于 Gemini 3 Pro 构建，拥有 128K 上下文窗口，支持 97 种语言，音频输出价格为每分钟 0.018 美元。当实时语音交互中需要更强的后台推理来解决复杂、多步骤问题时，官方推荐使用 Extended Thinking 版本。

hackernews · leumon · 9月15日 17:38 · [社区讨论](https://news.ycombinator.com/item?id=49715947)

**背景**: Gemini 是谷歌的旗舰大语言模型系列，其中“Live”系列指的是面向实时语音对话（而非文本聊天）的音频到音频 API 模型。“Extended Thinking”是谷歌对在回答前投入额外算力进行内部推理的模型的称呼，这一模式因专注于推理的 LLM 而流行。这些模型可以在用户持续说话的同时，在后台管理工具调用和视觉上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Gemini 3 . 8 Live & Gemini 3 . 8 Live Extended Thinking</a></li>
<li><a href="https://9to5google.com/2026/09/15/gemini-3-8-live-announced/">Gemini 3 . 8 Live Extended Thinking powers Gemini Live , Gmail</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking">Gemini 3 . 8 Live Extended Thinking | Gemini API | Google AI for...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论总体偏正面：有人称赞它能很好地处理浓重口音、语音悦耳、延迟低，并且终于可以在工作区账户上使用；还有人表示 Gemini 生成的文字是唯一读起来还算舒服的。一位使用小众语言南非荷兰语的用户称其实时聊天和语法教学效果极佳，但也有人质疑 Gemini 何时才能超越 Fable 和 Astra 等对手，还有人批评演示视频中该模型输给了国际象棋中最常见的将杀套路。

**标签**: `#AI`, `#Gemini`, `#Google`, `#LLM`, `#Model Release`

---

<a id="item-5"></a>
## [AI 智能体 25 分钟内发现 Baseten 生产环境 GitHub 管理员令牌](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) ⭐️ 8.0/10

Strix 的 AI 渗透测试智能体在启动扫描后 25 分钟内，发现了一个属于 'basetenbot' 账户的有效 GitHub 个人访问令牌，该令牌对 Baseten 的主要产品仓库、GitOps 集群仓库和 Homebrew tap 拥有管理员和推送权限。该令牌是在智能体找到一个公开的 Baseten 镜像仓库后，从 Docker 构建历史中发现的；Baseten 随后确认该问题为严重级别，将 Harbor 项目设为私有，并在次日轮换了该令牌。 这一事件表明，自主 AI 智能体能够快速发现人类可能忽略的暴露密钥，凸显了在容器构建产物中嵌入凭据的公司所面临的日益严重的供应链安全风险。同时，它也引发了关于此类智能体究竟是渗透测试的根本性变革，还是仅仅将人类本可完成的任务自动化的争论。 泄露的令牌还授予了对其他私有仓库（包括特定客户仓库）的读写权限，并且是在 Docker 构建历史而非源代码中发现的。Baseten 在大约 17 小时内做出响应，确认问题为严重级别，将 Harbor 项目设为私有并轮换了令牌，同时要求 Strix 安全删除他们拉取的镜像。

hackernews · bearsyankees · 9月15日 18:11 · [社区讨论](https://news.ycombinator.com/item?id=49716476)

**背景**: Baseten 是一个 AI 推理平台，用于在生产环境中部署和运行开源、自定义及微调模型。GitHub 个人访问令牌（PAT）是用于向 GitHub API、命令行或集成进行身份验证的密码替代方案，一旦泄露，可能授予广泛的仓库访问权限。Strix 是一款 AI 驱动的渗透测试智能体，能够自主执行侦察、利用和报告，类似于 HackerAI 和 Cyberstrike 等新兴工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.baseten.co/">Inference Platform : Deploy AI models in production | Baseten</a></li>
<li><a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens">Managing your personal access tokens - GitHub Docs</a></li>
<li><a href="https://www.linkedin.com/pulse/man-machine-future-penetration-testing-ai-agents-louis-sin-kpcuc">“Man + Machine: The Future of Penetration Testing with AI Agents ”</a></li>

</ul>
</details>

**社区讨论**: 评论者大多赞扬 Baseten 的迅速响应，但对智能体发现的新颖性存在争议，一些人认为此类智能体的优势在于速度，而非发现人类无法找到的东西。其他人质疑这种未经授权的测试是否合法，而一些人则认为这是 Strix 的有效营销。

**标签**: `#security`, `#AI agents`, `#penetration testing`, `#GitHub`, `#supply chain`

---

<a id="item-6"></a>
## [前苹果工程师用 LLM 一个月内为 M4 Mac Mini 打造 Linux GPU 驱动](https://codyho.dev/blog/gpu-driver/) ⭐️ 8.0/10

一位名叫 Cody Ho 的前苹果工程师与一位名为 Niklas 的合作者，在大约一个月内逆向工程了苹果 AGX GPU 的固件 ABI 和用户空间组件，为 M4 Mac Mini 开发出了一个符合 OpenGL ES 3.0 标准的 Linux GPU 驱动，运行 Minecraft 可达约 200fps。这项工作大量借助了 LLM 辅助，而传统上这类逆向工程通常需要数年时间。 这可能大幅加速 M3、M4 等较新苹果芯片在 Linux 下的 GPU 支持，而这些芯片在 Asahi Linux 下长期缺乏 GPU 加速。同时，它也成为 LLM 辅助逆向工程能否被主流开源项目接受的一个高关注度案例，尤其是考虑到 Asahi Linux 有严格的禁用 AI 政策。 该驱动符合 OpenGL ES 3.0 标准，据称在 M4 Mac Mini 上运行 Minecraft 可达 212fps，但由于 Asahi Linux 的禁用 AI 政策，目前无法被上游合并。作者此前已被 Asahi Linux 封禁，原因是隐瞒了大量使用 LLM 的情况，以及他作为前苹果工程师、与苹果芯片开发人员有直接联系的身份。

hackernews · ADevWithAnIdea · 9月15日 19:30 · [社区讨论](https://news.ycombinator.com/item?id=49717638)

**背景**: Asahi Linux 是一个通过逆向工程苹果芯片硬件、让现代 Mac 运行 Linux 的社区项目，其针对 M1 和 M2 芯片的 GPU 驱动耗费了多年人工努力。苹果的 GPU 内部称为 AGX，其固件 ABI 和用户空间组件没有公开文档，必须逆向工程才能构建开源驱动。LLM 正越来越多地被用于辅助这类底层逆向工程，但包括 Asahi Linux 在内的许多开源项目出于法律和伦理原因禁止 AI 生成的贡献。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://codyho.dev/blog/gpu-driver/">I Came, I Prompted, I Left Part 2: Building a GPU Driver ... — Cody Ho</a></li>
<li><a href="https://asahilinux.org/2022/12/gpu-drivers-now-in-asahi-linux/">Apple GPU drivers now in Asahi Linux - Asahi Linux</a></li>
<li><a href="https://zerohour.day/item/d0b9509c549f79d6c25dd760e89742a7f807263e">Building a Linux GPU Driver for the M4 Mac Mini in One Month</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍称赞这一技术成就，有人称其为 LLM 的最佳用例之一，因为它省去了多年的人工逆向工程。但也有许多人提出伦理和法律方面的担忧：作者的前苹果身份和隐瞒使用 LLM 的行为构成利益冲突，而 Asahi Linux 的禁用 AI 政策很可能阻止上游合并，因此有人预测 AI 辅助的分支将占据主流，而纯粹主义者则继续使用较旧的硬件。

**标签**: `#Linux`, `#GPU driver`, `#Apple Silicon`, `#LLM`, `#Asahi Linux`

---

<a id="item-7"></a>
## [布鲁斯·施奈尔：25 年大规模监控已然失败](https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html) ⭐️ 8.0/10

布鲁斯·施奈尔发表了一篇题为《25 年大规模监控已然足够》的博文，指出四分之一世纪的大规模监控项目未能兑现其承诺的安全收益，反而不断侵蚀公民自由。该文章在 Hacker News 上引发了热烈讨论，获得 812 分和 293 条评论，围绕隐私、去中心化和政策改革展开辩论。 施奈尔是安全与密码学领域最具权威的声音之一，因此他关于大规模监控既无效又有害的论点在政策辩论中具有重要分量。讨论凸显出人们对监控权力日益常态化和扩张的担忧，评论者指出 NSPM-7 可能带来进一步的升级。 施奈尔指出，大规模监控如今已成为执法部门的常规工具，ICE 将其用于移民执法行动，并针对行使第一修正案抗议权利的人士。评论者提议将摄像头网络访问权限限制在地方司法管辖区，并构建易于使用的自托管隐私服务，以利用第一和第四修正案的保护。

hackernews · iamnothere · 9月15日 11:26 · [社区讨论](https://news.ycombinator.com/item?id=49710883)

**背景**: 大规模监控是指对全体人口的通信和行踪数据进行无差别收集与分析，在 9·11 袭击后大幅扩张，并通过 2013 年斯诺登的披露为公众所知。布鲁斯·施奈尔是一位密码学家和公共利益技术专家，他长期以来（包括在其著作《数据与歌利亚》中）主张大规模监控无法可靠地阻止恐怖袭击。评论者提到的 NSPM-7 是一份美国国家安全政策备忘录，批评者认为它将进一步扩大监控权力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html">25 Years of Mass Surveillance Is Enough - Schneier on Security</a></li>
<li><a href="https://www.lawfaremedia.org/article/25-years-of-mass-surveillance-is-enough">25 Years of Mass Surveillance Is Enough | Lawfare</a></li>
<li><a href="https://www.vice.com/en/article/bruce-schneier-mass-surveillance-wont-stop-terror-876/">This Security Expert Thinks Mass Surveillance Doesn't Stop Terror...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多赞同施奈尔的观点，有人引用《道德经》论证限制反而滋生其试图防止的混乱，还有人提议建立受地方管辖的摄像头网络和自托管隐私服务。数人对 NSPM-7 将使大规模监控变得更加压迫表示担忧，还有人警告只有当监控本身成为国家安全隐患时，这一问题才会得到解决。

**标签**: `#surveillance`, `#privacy`, `#security`, `#policy`, `#civil-liberties`

---

<a id="item-8"></a>
## [SemiAnalysis：Vera Rubin NVL72 智能体推理每美元性能提升 67 倍](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-agentic-inference) ⭐️ 8.0/10

SemiAnalysis 发布分析报告称，NVIDIA 的 Vera Rubin NVL72 机架级平台在智能体推理工作负载上实现了每美元 67 倍的性能提升，该结论基于其新推出的 AgentX 基准测试，该测试由 393 个用户自愿提供的 Claude Code 会话构建而成。文章还指出 NVIDIA 在性能宣传上有所保留，并强调每吉瓦年利润翻倍，以及极致协同设计和“买得越多，赚得越多”等主题。 如果这一数据准确，智能体推理每美元性能提升 67 倍将大幅重塑大规模运行 AI 智能体的经济性，影响数据中心运营商、云服务商以及计划大规模部署推理的企业。这也表明硬件设计正越来越多地围绕多轮、有状态的智能体工作负载进行协同优化，而非单次模型补全。 Vera Rubin NVL72 平台在机架级系统中集成了 36 颗 Vera CPU 和 72 颗 Rubin GPU，提供 3.6 exaFLOPS 的 AI 性能和 75TB 内存，基于 NVIDIA 第三代 MGX 设计，支持无电缆模块化和快速部署。AgentX 基准测试是一种基于真实 Claude Code 会话的回放工作负载，旨在捕捉长上下文、多轮编码场景，与固定序列推理基准有所不同。

rss · Semianalysis · 9月14日 22:08

**背景**: 智能体推理指的是 AI 智能体在推理、选择动作、调用工具、回顾先前上下文并更新下一步时所遵循的完整执行路径，是一种有状态的多轮工作流，而非单次模型补全。随着智能体 AI 成为主要的生产用例，MLPerf 和 SemiAnalysis 的 InferenceX/AgentX 等基准测试已被扩展以衡量这些多轮工作负载。NVIDIA 的 Vera Rubin NVL72 是一款面向千兆级训练和推理的机架级 AI 平台，而 SemiAnalysis 是 AI 硬件和推理经济性深度技术分析领域被广泛引用的来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">NVIDIA Vera Rubin NVL72 | Co-Designed Infrastructure for Agentic AI</a></li>
<li><a href="https://servers.asus.com/glossary/What-is-NVIDIA-Vera-Rubin-NVL72">What is NVIDIA Vera Rubin NVL72? | ASUS Servers</a></li>
<li><a href="https://inferencex.semianalysis.com/">Open-Source Agentic Inference Benchmark | InferenceX</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#inference`, `#performance`, `#NVIDIA`, `#agentic AI`

---

<a id="item-9"></a>
## [4400 万参数三值 LLM 在 CPU 上以 1900 tok/s 运行，仅 19.8 MB](https://www.reddit.com/r/MachineLearning/comments/1wgzpli/i_trained_a_44m_parameter_quantized_llm_from/) ⭐️ 8.0/10

一位开发者从零开始训练了 SHADOW-50M，这是一个 4400 万参数的 LLM，在 450 亿 token 上训练，最终以 19.8 MB 的三值权重模型发布，在笔记本 CPU 上运行速度约 1900 tok/s，通过 WebAssembly 在浏览器中约 500 tok/s。它引入了由固定 512 位指纹表示的 73,880 词表（而非训练嵌入），以及一个混合计算电路，可在 token 流内处理算术、日期、单位和排序。 这表明极端量化和架构技巧可以将实用的语言与检索能力压缩到 20 MB 以下，并在普通 CPU 上完全离线运行，这对边缘 AI、隐私保护的端侧推理和 TinyML 应用具有重要意义。它还展示了一种替代工具调用的实用方案，即把确定性计算电路直接嵌入模型的 token 流中。 该模型使用三值{-1,0,+1}权重和 159 KB 的编译内核，基于磁盘的存档以 1 bit（288 字节/token）存储注意力状态，并使用 22 字节/token 的索引，无需向量数据库或嵌入模型。在标准基准上，它不如一个 5180 万参数的 bf16 Llama 风格模型（ARC-Easy 0.307 对 0.435，PIQA 0.570 对 0.600，WikiText-2 困惑度 186 对 165），但在算术、日期和检索任务上表现优异，而更大的模型在这些任务上失败。

reddit · r/MachineLearning · /u/Final-Data-1410 · 9月15日 12:59

**背景**: 三值权重网络将权重量化为{-1, 0, +1}，从而实现无乘法推理和显著的模型压缩，这是在边缘设备上运行 LLM 的关键技术。量化 LLM 通过使用低位表示来降低内存和计算需求，而 WebAssembly 允许此类模型跨平台运行，包括在浏览器标签页中。该项目将这些思路结合起来，把三值权重与基于指纹的词表和确定性计算电路相结合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/ternary-weight-networks-twns">Ternary Weight Networks Overview</a></li>
<li><a href="https://symbl.ai/developers/blog/a-guide-to-quantization-in-llms/">A Guide to Quantization in LLMs | Symbl.ai</a></li>
<li><a href="https://gcore.com/resources/web-assembly-for-ai-inference">WebAssembly for AI Inference</a></li>

</ul>
</details>

**社区讨论**: 社区反响非常积极，原帖获得 360 多个赞和 94 个 GitHub 星标，表明人们对高效微型 LLM 有浓厚兴趣。评论者可能赞赏作者对基准弱点的坦诚以及新颖的检索和计算机制，但也有人可能质疑一个在标准基准上表现不佳的模型的实际用途。

**标签**: `#LLM`, `#Quantization`, `#Edge AI`, `#Efficient Inference`, `#TinyML`

---

<a id="item-10"></a>
## [Prior Labs 发布 TabPFN-3.5，新的表格基础模型 SOTA](https://www.reddit.com/r/MachineLearning/comments/1wh4xhy/tabpfn35_is_released_as_the_next_sota_tabular/) ⭐️ 8.0/10

Prior Labs 发布了 TabPFN-3.5，这是一款新的表格基础模型，在 TabArena 和 BeyondArena 两个基准上都排名第一，并在最多 100 万行、2 万特征的数据集上达到 SOTA。它提供三个变体：TabPFN-3.5-Fast（alpha 版，比基础模型快 6 倍）、TabPFN-3.5-Thinking（通过 API 用算力换取更高精度）以及 TabPFN-3.5-Plus。 表格数据仍是企业和科研场景中最主流的数据格式，但其基础模型进展一直落后于文本和视觉领域，因此这次带有大幅基准提升的新 SOTA 发布，表明表格基础模型正在快速成熟。新增的速度变体和可扩展算力的变体也让这些模型更易于实际部署，将影响依赖 XGBoost 等梯度提升树的数据科学家和机器学习工程师。 在 BeyondArena 上，TabPFN-3.5 在文本丰富、高基数和高度高维的数据上领先，比此前最强基线高出 250 Elo，比此前总榜第一高出 150 Elo。TabPFN-3.5-Thinking 在 BeyondArena 上比基础模型再高 20 Elo，在 TabArena 上高 44 Elo，不过 Fast 变体仍处于 alpha 阶段。

reddit · r/MachineLearning · /u/tuanacelik · 9月15日 16:18

**背景**: TabPFN 是 Prior Labs 开发的、基于 Transformer 的预训练表格数据基础模型；它不需要为每个数据集单独训练模型，而是先生成大量合成表格数据集，再学习在上下文中直接做预测。TabArena 是一个持续纳入新数据集和新模型的“活”基准，用于可靠地比较各种表格机器学习方法；BeyondArena 则是更新的统一基准，覆盖不同规模和维度下的 IID、时序和分组任务。Elo 是借用自国际象棋的相对评分，数值越高表示相对对手的表现越强。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/PriorLabs/tabpfn">PriorLabs/TabPFN - Foundation Model for Tabular Data - GitHub</a></li>
<li><a href="https://arxiv.org/abs/2506.16791">TabArena : A Living Benchmark for Machine Learning on Tabular Data</a></li>
<li><a href="https://www.linkedin.com/posts/probabl_theres-a-new-tabular-ai-benchmark-in-town-activity-7481346525374271488-KtqC">There’s a new tabular AI benchmark in town: BeyondArena Our...</a></li>

</ul>
</details>

**标签**: `#tabular-data`, `#foundation-models`, `#machine-learning`, `#SOTA`, `#benchmarks`

---

<a id="item-11"></a>
## [中国“十五五”规划瞄准先进芯片与开源鸿蒙](https://www.secrss.com/articles/93961) ⭐️ 8.0/10

中国工业和信息化部与国家发展改革委联合印发了《电子信息制造业发展“十五五”规划》，部署了 17 项重点任务。规划提出提高先进制程能力，突破高端手机核心芯片和 PC 高性能芯片，并加强开源鸿蒙等国产操作系统的搭载应用。 该政策设定了到 2030 年营业收入突破 30 万亿元、研发投入强度达到 3.5%的宏伟目标，可能显著重塑中国半导体自给能力和全球供应链。它将直接影响中国及海外的芯片设计商、制造商、操作系统开发商和下游设备厂商。 规划还推进 RISC-V、人工智能芯片和终端以及北斗等领域的发展，同时强调国产操作系统的搭载。不过，这仍是一份战略路线图，未披露具体的资金或执行机制。

telegram · zaihuapd · 9月15日 03:10

**背景**: 开源鸿蒙是华为捐赠给开放原子开源基金会的开源分布式操作系统，构成了鸿蒙操作系统的基础。RISC-V 是一种免费开放的指令集架构，允许定制芯片设计，被视为 ARM 和 x86 等专有架构的替代方案。先进制程（如 7nm、5nm、3nm）指的是能够实现更强大、更高效芯片的尖端半导体制造技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenHarmony">OpenHarmony - Wikipedia</a></li>
<li><a href="https://riscv.org/">Home - RISC - V International</a></li>
<li><a href="https://www.tessolve.com/blogs/7nm-vs-5nm-vs-2nm-how-to-choose-the-right-semiconductor-process-node/">7nm vs 5nm vs 2nm: Choosing the Right Process Node</a></li>

</ul>
</details>

**标签**: `#China policy`, `#semiconductor`, `#OpenHarmony`, `#RISC-V`, `#AI chips`

---

<a id="item-12"></a>
## [美英立法者推动禁止超级智能 AI 的法案](https://t.me/zaihuapd/43832) ⭐️ 8.0/10

美国参议员桑德斯宣布将提出《禁止人工超级智能法案》，禁止开发比人类更聪明的 AI 并暂停其他先进 AI 研究；英国议员索贝尔也在下议院提出据称是 G7 议会中首份相关法案，要求赋予政府监控和限制超级智能“前体”系统的权力。 这标志着 AI 治理努力显著升级，主要西方立法者从安全指南转向直接禁止超级智能系统，可能影响全球 AI 监管和国际条约讨论。 两份法案还要求各自政府推动全球条约，但通过前景渺茫。伯克利教授拉塞尔警告，AI 可能造成“切尔诺贝利级灾难”，如协同破坏金融、通信或电网系统。

telegram · zaihuapd · 9月15日 04:26

**背景**: 超级智能 AI 指的是在推理和决策方面超越人类智能的假想 AI。AI 安全研究者和政策制定者日益呼吁建立有约束力的国际协议，设定红线以防止 AI 能力不受控制地升级，类似欧盟议员贝尼费伊推动全球合作的努力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.euronews.com/video/2026/09/15/eu-has-the-power-to-lead-on-global-treaty-on-ai-says-mep-brando-benifei">Video. EU has 'the power' to lead on ' global treaty on AI ... | Eu...</a></li>
<li><a href="https://www.antoinebuteau.com/lessons-from-yoshua-bengio/">Lessons from Yoshua Bengio | Antoine Buteau</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/what-is-artificial-intelligence-ai/">What is Artificial Intelligence ( AI ) - GeeksforGeeks</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#superintelligence`, `#policy`, `#AI safety`, `#legislation`

---

<a id="item-13"></a>
## [谷歌向全体工程师开放 Anthropic 的 Claude Opus 5](https://www.businessinsider.com/google-finally-lets-all-engineers-use-anthropics-claude-2026-9) ⭐️ 8.0/10

谷歌已向全体工程师开放 Anthropic 的 Claude Opus 5 用于内部开发，但仅限通过其自研的 Antigravity 平台使用。此前谷歌通常禁止大多数员工使用 Claude Code、OpenAI 的 Codex 等外部编程工具，要求他们改用自家的 Gemini。 此举表明，即便拥有自家前沿模型的公司也在 AI 编程工具上感受到竞争压力，同时标志着谷歌的一次显著战略转变——谷歌本身还是 Anthropic 的重要投资者。这可能影响其他大型企业在自研与第三方 AI 编程助手之间的取舍。 Gemini 仍是内部开发的主要模型，Claude 则按每位员工的配额作为补充提供。谷歌今年早些时候宣布计划向 Anthropic 投入最多 400 亿美元，凸显两家公司之间紧密交织的关系。

telegram · zaihuapd · 9月15日 05:31

**背景**: Claude 是 Anthropic 的大语言模型系列，按能力分为 Haiku、Sonnet 和 Opus 三档，其中 Opus 能力最强；Claude Code 是 Anthropic 推出的终端智能体编程工具。Google Antigravity 是谷歌的智能体开发平台，将传统 IDE 演进为“智能体优先”的环境，开发者更多是编排 AI 智能体而非逐行手写代码。谷歌自家的竞争模型是 Gemini，过去一直要求员工在内部工作中使用它。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://antigravity.google/">Google Antigravity</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**标签**: `#AI`, `#Google`, `#Anthropic`, `#Claude`, `#developer-tools`

---