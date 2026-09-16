---
layout: default
title: "Horizon Summary: 2026-09-16 (ZH)"
date: 2026-09-16
lang: zh
---

> 从 89 条内容中筛选出 11 条重要资讯。

---

1. [TypeSafe AI 发布 System One 模型与 Jev，专注类型化推理](#item-1) ⭐️ 8.0/10
2. [电子墨水相框聆听鸟鸣并绘制 19 世纪风格插画](#item-2) ⭐️ 8.0/10
3. [Apple Reference Image：为照片真实性提供加密证明](#item-3) ⭐️ 8.0/10
4. [互联网档案馆为应对抓取浪潮给 Wayback Machine 增加防护](#item-4) ⭐️ 8.0/10
5. [谷歌发布 Gemini 3.8 Live 与 Live Extended Thinking](#item-5) ⭐️ 8.0/10
6. [开发者一个月内为 M4 Mac Mini 构建 Linux GPU 驱动](#item-6) ⭐️ 8.0/10
7. [Strix 发现泄露的 GitHub PAT，可获取 Baseten 生产环境 GitHub 管理员权限](#item-7) ⭐️ 8.0/10
8. [Vera Rubin NVL72 智能体推理每美元性能提升 67 倍](#item-8) ⭐️ 8.0/10
9. [SemiAnalysis：机器人“大脑”该放在端侧还是数据中心](#item-9) ⭐️ 8.0/10
10. [Prior Labs 发布 TabPFN-3.5，成为新的表格基础模型 SOTA](#item-10) ⭐️ 8.0/10
11. [低质中文赌场网站暗藏 APT 命令控制基础设施](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TypeSafe AI 发布 System One 模型与 Jev，专注类型化推理](https://typesafe.ai/blog/introducing-system-one-models-and-jev) ⭐️ 8.0/10

TypeSafe AI 是一家由 Diogo Almeida（此前在 OpenAI 为 ChatGPT 构建 RLHF 方法）创立的旧金山实验室，现已结束隐身状态，获得由 DCVC 领投的 4000 万美元种子轮融资，并发布了 System One 模型系列及其首个模型 Jev。Jev 完全跳过文本生成，而是从非结构化输入中返回类型化的概率决策，目前已开放早期访问。 这代表了一种新颖的结构化输出生成方法，用快速类型化推理取代通用文本生成，可能使 LLM 式智能在分类、路由、评分和提取等手写逻辑过于脆弱的任务中变得实用。403 条评论的讨论表明，人们对通用生成与专用类型化推理之间的权衡有着浓厚兴趣。 据 TypeSafe 称，Jev 比 LLM 快 20-200 倍、便宜 40-400 倍，并且由于放弃了字符串生成，它在架构上不可能产生幻觉。然而，这些引人注目的速度和成本优势仍由厂商自行测试，批评者指出 Jev 只能生成结构化输出，无法生成任意代码或文本。

hackernews · albelfio · 9月15日 19:25 · [社区讨论](https://news.ycombinator.com/item?id=49717558)

**背景**: System One 模型是一类专为做出快速、结构化决策而构建的 AI 模型，软件可以直接使用：它们评估状态并返回类型化答案和概率，类似于 LLM 理解自然语言输入，但返回的是类型化决策而非文本。Jev 是 TypeSafe 的旗舰模型，也是首个 System One 模型，使用 RLCD（对比数据强化学习）训练，被定位为前沿智能函数调用：输入非结构化状态，输出类型化概率决策。这与传统 LLM 生成自由文本并可能产生幻觉形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models & Jev - TypeSafe AI Blog</a></li>
<li><a href="https://docs.typesafe.ai/concepts/system-one">System One - TypeSafe AI</a></li>
<li><a href="https://www.explainx.ai/blog/typesafe-ai-jev-system-one-models-launch-2026">Jev by TypeSafe AI: 200x Faster Structured-Output Model (2026 ...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认为这种方法确实有趣且新颖，ymir_e 强调了合同分析，vintermann 提到了家谱匹配作为强有力的用例，尤其看重确定性输出可用于标记低置信度结果以供人工审核。jacobgold 认为标题应改为“Jev：用通用生成换取快速类型化推理”，并质疑速度比较是否具有误导性，因为能输出图灵完备语言代码的生成模型可以做计算机能做的任何事情，而 Jev 只能生成结构化输出。cfowles 表示在看到 Home Assistant 演示后价值才真正体现出来，futurisold 指出将其与契约式设计模式结合可以催生许多新应用。

**标签**: `#LLM`, `#structured-output`, `#typed-inference`, `#AI`, `#typesafe`

---

<a id="item-2"></a>
## [电子墨水相框聆听鸟鸣并绘制 19 世纪风格插画](https://github.com/arnegiacomo/fugleramme) ⭐️ 8.0/10

一位开发者在 GitHub 上发布了名为 fugleramme 的项目，这是一个电子墨水相框，能够持续监听鸟鸣声，使用 BirdNET 分类器识别鸟种，并将每种识别到的鸟以 19 世纪风格插画的形式显示在屏幕上。该 Show HN 帖子获得了 1664 分和 208 条评论，引发了关于嵌入式机器学习和电子墨水项目的热烈讨论。 该项目展示了如何将 BirdNET 等现有开源机器学习模型与低功耗电子墨水硬件结合，创造出令人愉悦的常开环境设备，激励其他开发者探索类似的嵌入式机器学习应用。它也凸显了业余爱好者电子墨水和 ESP32 项目生态的成长，这些项目注重能效和单一用途设计。 BirdNET 是一个专为声学鸟类识别设计的传统卷积神经网络，而非大语言模型，它通过多阶段流程处理原始音频以保证生态识别准确性。电子墨水屏仅在刷新时耗电，因此配合低功耗蓝牙驱动和 2000mAh 电池，类似装置即使每天刷新多次也能单次充电使用数年。

hackernews · arnemunthekaas · 9月15日 12:31 · [社区讨论](https://news.ycombinator.com/item?id=49711544)

**背景**: 电子墨水是一种电子纸显示技术，像纸张一样反射光线，仅在图像变化时耗电，因此非常适合低功耗常开设备。BirdNET 是由康奈尔鸟类学实验室和开姆尼茨理工大学开发的 AI 鸟鸣识别系统，提供免费应用和开源模型。嵌入式机器学习指直接在微控制器等小型低功耗设备上运行机器学习模型，使此类应用无需云连接即可实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://en.wikipedia.org/wiki/E_Ink">E Ink - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Embedded_Machine_Learning">Embedded Machine Learning</a></li>

</ul>
</details>

**社区讨论**: 评论者几乎一致称赞该项目充满魔力且鼓舞人心，有人称这是近期 HN 上最酷的东西。一位评论者澄清 BirdNET 是传统神经网络而非大语言模型，另一位分享了在 FrameOS 上的复刻尝试，还有一位描述了低功耗蓝牙电子墨水装置可单次充电运行数年的经验。

**标签**: `#e-ink`, `#embedded-systems`, `#bird-classification`, `#hardware`, `#machine-learning`

---

<a id="item-3"></a>
## [Apple Reference Image：为照片真实性提供加密证明](https://security.apple.com/blog/apple-reference-image/) ⭐️ 8.0/10

Apple 推出了 Apple Reference Image，这是 iPhone 18 Pro 系列上的一种可选相机模式，通过加密方式证明照片拍摄的是真实事件且未被篡改。该系统在 Apple 安全博客的新文章《Apple Reference Image: A New Approach for Verified Photography》中有详细说明。 这是一项具有重大隐私和安全影响的技术进展，可能将经过验证的摄影从开放行业标准转变为 Apple 控制的专有系统。它可能影响记者、保险和身份验证应用，并引发关于参与正常公民和商业生活是否必须拥有 iPhone 的担忧。 Reference Image 仅适用于 iPhone 18 Pro 的主摄像头，因此使用超广角和长焦摄像头拍摄的照片无法以相同方式验证。该系统要求将每张经过验证的“已显影”图像上传到 Apple 服务器，并依赖许多闭源组件，批评者认为这使信任和审计变得困难。

hackernews · imwally · 9月16日 02:07 · [社区讨论](https://news.ycombinator.com/item?id=49721322)

**背景**: 加密图像溯源旨在通过签名和元数据验证数字图像的来源和编辑历史，类似于由 Adobe、《纽约时报》等支持的 C2PA Content Credentials 标准。Apple 的方法不同之处在于将验证绑定到特定拍摄硬件和 Apple 自己的基础设施，而非开放的跨厂商标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5mac.com/2026/09/15/apple-explains-how-the-iphone-18-pros-new-reference-image-camera-mode-works/">Apple explains how the iPhone 18 Pro’s new Reference Image ...</a></li>
<li><a href="https://www.androidauthority.com/apple-reference-image-vs-android-c2pa-3711734/">Apple claims iPhone 18 Pro's camera is more... - Android Authority</a></li>
<li><a href="https://c2pa.org/">C 2 PA | Verifying Media Content Sources</a></li>

</ul>
</details>

**社区讨论**: 评论者批评激烈：有人指出该系统无法应对重放攻击，即拍摄显示器上经过编辑的图像仍可能获得有效的 Apple Reference 签名。其他人则反对其复杂性、闭源信任要求、强制上传到 Apple 服务器，以及“认证真实”标签可能导致人们不加辨别地接受误导性叙事的风险。

**标签**: `#Apple`, `#photo-verification`, `#cryptography`, `#privacy`, `#security`

---

<a id="item-4"></a>
## [互联网档案馆为应对抓取浪潮给 Wayback Machine 增加防护](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) ⭐️ 8.0/10

互联网档案馆报告称，其 Wayback Machine 遭遇了一波又一波高流量的自动化抓取流量，迫使其部署新的防护措施以维持服务运行。该机构认为，其中大量流量来自试图绕过原始网站封锁、转而抓取存档副本的爬虫。 互联网档案馆是网络保存领域至关重要的公共基础设施，持续的抓取压力威胁着这一被记者、研究人员和维基百科编辑使用的免费开放资源的可用性。如果网站因此选择退出存档，整个网络的历史记录可能会对所有人缩小。 档案馆表示已部署防护措施，但未披露具体细节；服务虽不稳定但仍可访问，包括通过 Tor 匿名访问而无需经过中心化网关。作为对抓取行为的回应，一些网站已经选择退出存档。

hackernews · ChrisArchitect · 9月15日 17:52 · [社区讨论](https://news.ycombinator.com/item?id=49716176)

**背景**: Wayback Machine 是万维网的数字存档服务，由互联网档案馆于 2001 年 10 月 25 日向公众开放；该档案馆是 1996 年由 Brewster Kahle 在旧金山创立的非营利组织。它让用户查看网站的历史快照，截至 2025 年 10 月已存档超过 1 万亿个网页和远超 99 PB 的数据。网络抓取指自动化机器人大规模收集数据，而在 2020 年代中期，大语言模型厂商运营的爬虫成为网络流量的主要来源之一，常使用分布式爬取来规避检测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wayback_Machine">Wayback Machine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Internet_Archive">Internet Archive</a></li>
<li><a href="https://en.wikipedia.org/wiki/Web_scraping">Web scraping - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍称赞互联网档案馆是重要的开放基础设施并呼吁捐款，simonw 认为这些流量很可能来自绕过原始网站封锁的爬虫。其他人分享了找回 2000 年代早期丢失内容的个人经历，还有用户指出工作电脑上持续出现 429 错误而手机却正常，暗示这些防护措施可能对部分合法用户造成不均匀的影响。

**标签**: `#internet-archive`, `#web-scraping`, `#open-access`, `#digital-preservation`, `#infrastructure`

---

<a id="item-5"></a>
## [谷歌发布 Gemini 3.8 Live 与 Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) ⭐️ 8.0/10

谷歌发布了 Gemini 3.8 Live 和 Gemini 3.8 Live Extended Thinking，称其为迄今最先进的实时对话模型，专为自然的实时语音交互打造。其中 Extended Thinking 版本是一款高推理能力的音频到音频模型，以 82.6 分在 Artificial Analysis 的语音到语音质量指数中排名第一。 此次发布将实时语音 AI 推向企业级可靠性，Extended Thinking 模型在智能体任务完成基准上领先（τ-Voice 达 68.6%，Sierra 基准达 35.1%）。这对构建低延迟、高并发语音智能体的开发者和企业意义重大，同时也加剧了与其他前沿模型厂商的竞争。 这些模型主打高性价比和高速度，针对实时对话等高频、低延迟任务进行了优化，属于原生多模态的 Gemini 3 系列。Extended Thinking 版本特别推荐用于实时语音交互中需要更高后台推理能力、解决复杂多步骤问题的场景。

hackernews · leumon · 9月15日 17:38 · [社区讨论](https://news.ycombinator.com/item?id=49715947)

**背景**: Gemini 是谷歌的旗舰多模态 AI 模型系列，其中“Live”系列指的是为实时语音到语音对话（而非纯文本聊天）设计的模型。“Extended Thinking”则指模型在回答前进行额外后台推理的模式，以一定的延迟换取在复杂任务上更高的准确性。此次发布紧随谷歌近期的 Gemini 3.8 Flash 和 3.8 Flash Cyber 之后，延续了 Gemini 3 系列快速迭代的节奏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Gemini 3 . 8 Live & Gemini 3 . 8 Live Extended Thinking</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-audio/">Gemini 3.8 Audio (Live, Live Extended Thinking) - Model Card — Google DeepMind</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking">Gemini 3 . 8 Live Extended Thinking | Gemini API | Google AI for...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论褒贬不一：有人称赞该模型延迟低、语音自然，并且能很好地处理带口音的语音以及像南非荷兰语这样的小众语言；也有人反映存在上下文丢失和未经请求插入产品链接的问题。还有用户质疑，尽管谷歌拥有数据、TPU 硬件和广告资源，为何仍落后于 Fable、Astra 等竞争对手。

**标签**: `#Gemini`, `#Google`, `#AI`, `#LLM`, `#Model Release`

---

<a id="item-6"></a>
## [开发者一个月内为 M4 Mac Mini 构建 Linux GPU 驱动](https://codyho.dev/blog/gpu-driver/) ⭐️ 8.0/10

根据一篇在 Hacker News 上引发广泛讨论的博客文章，一名开发者在大约一个月内为 M4 Mac Mini 构建了一个可用的 Linux GPU 驱动。这一成果之所以引人注目，是因为 M4 属于较新的 Apple Silicon 世代，此前在 Linux 下缺乏 GPU 加速支持。 这可能显著加速 Linux 对较新 Apple Silicon 硬件的支持，而 GPU 加速一直是 M3 及之后芯片的主要痛点。它还引发了关于 LLM 辅助逆向工程能否取代多年人工努力，以及上游项目应如何对待此类贡献的争论。 据报道，该作者因在之前的一次贡献中隐瞒大量使用 LLM，并隐瞒自己是前 Apple 工程师、与 Apple Silicon 开发人员有直接联系，而被 Asahi Linux 封禁。Asahi Linux 有严格的禁止 AI 政策，这很可能使该驱动无法被上游合并进 Linux 内核。

hackernews · ADevWithAnIdea · 9月15日 19:30 · [社区讨论](https://news.ycombinator.com/item?id=49717638)

**背景**: Apple Silicon Mac 使用基于 ARM 的自研芯片，其 GPU 架构没有公开文档，因此 Linux 支持需要逆向工程。Asahi Linux 项目一直主导这一努力，但其 GPU 驱动工作主要针对较旧的 M1 和 M2 世代，并且进展有所放缓。LLM 正越来越多地被用于逆向工程，以帮助理解二进制代码和硬件行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49717638">Building a Linux GPU Driver for the M4 Mac Mini in... | Hacker News</a></li>
<li><a href="https://www.phoronix.com/news/Asahi-Lina-Steps-Down-Linux-GPU">Asahi Lina Pausing Work On Apple GPU Linux Driver Development</a></li>
<li><a href="https://www.linuxencaja.net/en/asahi-lina-pauses-development-of-linux-gpu-driver-for-apple/">Asahi Lina suspends development of Linux GPU driver for Apple</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一成果的速度表示赞叹，并认为这是 LLM 在逆向工程中的一个有力用例，但也有人对作者隐瞒 LLM 使用和前 Apple 员工身份提出伦理担忧。还有人指出，Asahi Linux 的禁止 AI 政策意味着这项工作很可能无法被上游合并，可能导致出现 AI 辅助的分支版本。

**标签**: `#Linux`, `#GPU driver`, `#Apple Silicon`, `#reverse engineering`, `#LLM`

---

<a id="item-7"></a>
## [Strix 发现泄露的 GitHub PAT，可获取 Baseten 生产环境 GitHub 管理员权限](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) ⭐️ 8.0/10

AI 渗透测试平台 Strix 发现了一个泄露的 GitHub 个人访问令牌（PAT）以及一个公开的容器镜像，二者结合可获取 Baseten 生产环境 GitHub 组织的管理员权限。Baseten 确认了该报告，立即吊销了泄露的密钥、移除了公开的 Harbor 容器镜像，并表示日志显示该漏洞从未被利用，也没有客户数据泄露。 这一事件凸显了单个泄露凭证如何可能升级为对公司生产代码仓库的完全管理控制，同时也加剧了关于 AI 智能体是否真正提升了漏洞发现能力，还是仅仅自动化了有动机的人类本就能发现的问题的争论。它还引发了关于在未事先协商的情况下将 AI 安全工具指向潜在供应商时的伦理和交战规则的质疑。 披露时间线显示，Strix 于 7 月 13 日晚上 11:10 报告了活跃的 basetenbot 令牌、公开的 Harbor 项目以及仓库权限；Baseten 次日上午将 Harbor 项目设为私有，但令牌仍然有效，直到 Baseten 安全团队于 7 月 14 日下午 4:34 确认该问题为严重级别并轮换了令牌。Baseten 还要求 Strix 安全删除他们拉取的镜像，社区成员则质疑针对潜在供应商域名运行 Strix 是否事先经过协商。

hackernews · bearsyankees · 9月15日 18:11 · [社区讨论](https://news.ycombinator.com/item?id=49716476)

**背景**: Baseten 是一家 AI 基础设施公司，提供用于在生产环境中部署和扩展开源及自定义 AI 模型的推理平台。GitHub 个人访问令牌（PAT）是一种允许以编程方式访问 GitHub 仓库和组织的凭证；一旦公开泄露，攻击者就可能读取、修改或管理代码及 CI/CD 流水线。Strix 是一款开源 AI 渗透测试工具，使用自主智能体动态运行代码、发现漏洞并通过概念验证进行验证，其理念类似于人工红队测试，但实现了自动化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.baseten.co/">Inference Platform: Deploy AI models in production | Baseten</a></li>
<li><a href="https://github.com/usestrix/strix">GitHub - usestrix/strix: Open-source AI penetration testing ...</a></li>
<li><a href="https://www.csoonline.com/article/4103717/github-action-secrets-arent-secret-anymore-exposed-pats-now-a-direct-path-into-cloud-environments-2.html">GitHub Action Secrets aren’t secret anymore: exposed PATs now a direct path into cloud environments | CSO Online</a></li>

</ul>
</details>

**社区讨论**: Baseten 的 Philip Kiely 确认了协同修复并感谢 Strix 的负责任披露，指出没有发生利用或数据泄露。ivraatiems 等评论者认为 AI 智能体的价值在于速度，而非发现人类找不到的东西；SaucyWrong 则质疑 Strix 是否有权测试潜在供应商，并提出了交战规则方面的担忧。总体情绪是对 Baseten 的响应表示肯定，但对 AI 驱动安全研究的新颖性和伦理持怀疑态度。

**标签**: `#security`, `#vulnerability-disclosure`, `#cloud-security`, `#ai-agents`, `#responsible-disclosure`

---

<a id="item-8"></a>
## [Vera Rubin NVL72 智能体推理每美元性能提升 67 倍](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-agentic-inference) ⭐️ 8.0/10

SemiAnalysis 报告称，NVIDIA 的 Vera Rubin NVL72 机架级平台在智能体推理负载上实现了每美元 67 倍的性能提升，这一结论基于其新推出的 AgentX 基准测试，该测试采用真实智能体编程会话的录制数据。NVIDIA 也援引 SemiAnalysis 的 AgentX 数据指出，在相同智能体负载下，该系统每兆瓦吞吐量比 GB300 NVL72 高出最多 30 倍。 这一说法将 AI 基础设施的经济性衡量标准从原始 FLOPS 转向每吉瓦利润，直接影响数据中心运营商和超大规模云厂商在电力受限条件下的建设规划。如果数据成立，智能体推理的单位有效工作成本将大幅下降，从而推动采购决策转向 NVIDIA 的下一代机架平台。 Vera Rubin NVL72 在第三代 MGX 机架设计中集成了 36 颗 Vera CPU 和 72 颗 Rubin GPU，提供 3.6 exaFLOPS 的 AI 性能和 75TB 内存，并采用无电缆模块化设计以实现快速部署。AgentX 负载保留了真实的上下文增长、工具调用和子智能体派生过程，因此比此前 8k1k、1k1k 等固定序列基准更具代表性。

rss · Semianalysis · 9月14日 22:08

**背景**: 智能体推理指的是 AI 智能体在读取文件、调用工具、反复查看上下文并产生修改时所执行的多步骤工作，而非单次提示-响应交互。SemiAnalysis 的 InferenceX 是一个基于 Apache-2.0 许可证的开源自动化基准测试套件，而 AgentX 是其较新的场景，用智能体编程流量取代了单轮流量。NVIDIA 的 NVL72 机架级系统将 CPU 和 GPU 集成到一个统一单元中，以高效服务超大规模模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/">Up to 30x More Work Per Watt: NVIDIA Vera Rubin NVL72 Sets a New Efficiency Standard for AI Agents</a></li>
<li><a href="https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat">AgentX - InferenceXv3: Does CUDA Moat Hold up in Agentic ...</a></li>
<li><a href="https://servers.asus.com/glossary/What-is-NVIDIA-Vera-Rubin-NVL72">What is NVIDIA Vera Rubin NVL72? | ASUS Servers</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI Hardware`, `#Inference`, `#Performance`, `#Data Center Economics`

---

<a id="item-9"></a>
## [SemiAnalysis：机器人“大脑”该放在端侧还是数据中心](https://newsletter.semianalysis.com/p/a-brain-too-big-to-carry-on-device) ⭐️ 8.0/10

SemiAnalysis 发布了一篇题为《A Brain Too Big to Carry — On-Device vs Datacenter Inference》的深度分析文章，探讨机器人基础模型究竟应该运行在本地端侧芯片上，还是通过无线链路卸载到数据中心的 GPU 上。文章对比了芯片与 DRAM 效率、Jetson Thor 与 B300 的总拥有成本（TCO）、真实部署案例，以及影响这一决策的网络约束。 随着机器人从实验室走向工厂车间和家庭，这一架构选择将决定整个通用机器人行业的硬件成本、延迟与可靠性。分析认为答案取决于机队规模、网络条件以及任务所需的智能程度，这可能会重塑机器人公司设计其计算栈的方式。 对于 96 台机器人的机队，报告的总拥有成本为：端侧 Jetson Thor 每小时 14.97 美元，RTX 6000 Pro 卸载方案每小时 15.61 美元，B300 数据中心推理每小时 18.63 美元。据报道，Boston Dynamics 将其 System 2 规划器卸载到 Google TPU 上，因为数千亿到万亿参数级别的模型太大，无法在机器人本体上运行。

rss · Semianalysis · 9月14日 16:37

**背景**: 机器人基础模型正日益分化为快速反应的“System 1”策略和较慢的审慎“System 2”规划器，这与认知科学中的双过程理论相呼应。与云端语言模型可以灵活扩展算力不同，机器人领域颠覆了这一设计范式：机器人必须在物理世界中行动，面临严格的延迟和安全约束，因此工程师必须决定是搭载沉重的端侧芯片，还是依赖可靠的低延迟网络链路。端侧推理避免了连接风险，但限制了模型规模；而数据中心卸载则能支持更大的模型，代价是带宽、延迟和网络可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/a-brain-too-big-to-carry-on-device">Where Does a Robot Think — On-Device vs Datacenter Inference</a></li>
<li><a href="https://aiweekly.co/alerts/boston-dynamics-runs-robot-brains-on-tpus-rivals-stay-on-jetson">Boston Dynamics runs robot brains on TPUs; rivals stay on Jetson</a></li>
<li><a href="https://news.lavx.hu/article/where-does-a-robot-think-on-device-vs-datacenter-inference">Where Does a Robot Think — On-Device vs Datacenter Inference</a></li>

</ul>
</details>

**标签**: `#AI inference`, `#edge computing`, `#robotics`, `#hardware`, `#TCO`

---

<a id="item-10"></a>
## [Prior Labs 发布 TabPFN-3.5，成为新的表格基础模型 SOTA](https://www.reddit.com/r/MachineLearning/comments/1wh4xhy/tabpfn35_is_released_as_the_next_sota_tabular/) ⭐️ 8.0/10

Prior Labs 发布了 TabPFN-3.5，这是一款新的表格基础模型，在 TabArena 和 BeyondArena 两个基准上都排名第一，并声称在最多 100 万行、2 万特征的表格数据上达到 SOTA。它提供三个版本：TabPFN-3.5-Fast（alpha 版，比基础模型快 6 倍）、TabPFN-3.5-Thinking（仅通过 API 提供，用算力换取更高精度）以及 TabPFN-3.5-Plus。 表格数据仍然是企业和科研场景中最主流的数据格式，因此更强的表格基础模型有望在许多实际流程中直接取代梯度提升树。在 BeyondArena 上比此前最强基线高出 250 Elo，说明基础模型终于开始在此前由树模型主导的、更困难的非 IID 表格任务上具备竞争力。 在 BeyondArena 上，TabPFN-3.5 在文本丰富、高基数和高维数据上领先，比此前的总榜第一高出 150 Elo；而 TabPFN-3.5-Thinking 在 BeyondArena 上比基础模型高 20 Elo，在 TabArena 上高 44 Elo。Fast 版本仍处于 alpha 阶段，Thinking 版本只能通过 API 使用，无法下载权重。

reddit · r/MachineLearning · /u/tuanacelik · 9月15日 16:18

**背景**: TabPFN 是 Prior Labs 推出的基于 Transformer 的基础模型，通过上下文学习在一次前向传播中解决表格预测问题，而不像 XGBoost 或 CatBoost 那样需要针对每个数据集单独训练。TabArena 是一个面向 IID 表格机器学习的“活”基准，会持续加入经过筛选的数据集和实现良好的模型；BeyondArena 则把它扩展到非 IID 场景，涵盖时间序列和分组任务，以及各种数据规模和特征维度。这些排行榜使用 Elo 评分来衡量模型的相对强弱，类似于国际象棋的排名方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/PriorLabs/TabPFN">GitHub - PriorLabs/ TabPFN : TabPFN : Foundation Model for Tabular ...</a></li>
<li><a href="https://arxiv.org/abs/2506.16791">TabArena : A Living Benchmark for Machine Learning on Tabular Data</a></li>
<li><a href="https://aiweekly.co/alerts/beyondarena-finds-trees-still-beat-tabular-fms-off-iid-data">BeyondArena finds trees still beat tabular FMs off-IID data | AI Weekly</a></li>

</ul>
</details>

**标签**: `#tabular-data`, `#foundation-models`, `#machine-learning`, `#benchmarking`, `#SOTA`

---

<a id="item-11"></a>
## [低质中文赌场网站暗藏 APT 命令控制基础设施](https://www.theregister.com/security/2026/09/15/low-quality-casino-sites-conceal-highly-dangerous-threat-actors/5296652) ⭐️ 8.0/10

安全研究人员追踪到约 170 万个中文赌场和成人网站，其中部分被与中国有关联的 APT 组织用作隐蔽的命令控制（C2）基础设施。自 2023 年以来，这些攻击者利用名为“PeckBirdy”的 JScript 框架，将恶意软件的 C2 域名隐藏在低质量赌博网站中，并通过虚假软件更新诱骗用户下载恶意程序。 该技术使攻击者能够将恶意流量混入看似普通的赌博网站访问中，大幅增加防御方检测和归因的难度。它还可能让安全团队将 C2 流量误判为员工违规浏览行为而非实际入侵，从而延误事件响应。 PeckBirdy 是一个用 JScript 实现的脚本框架，可在浏览器、MSHTA、WScript、Classic ASP、Node JS 和.NET ScriptControl 等多种环境中运行，具备利用系统自带程序（LOLBins）的广泛灵活性。由于承载网站与合法赌博网站高度相似，防御方可能将相关流量视为良性或员工违规行为而忽略。

telegram · zaihuapd · 9月16日 07:31

**背景**: 命令控制（C2）基础设施是攻击者在初始入侵后用于与受感染设备保持通信的一整套工具和通道。高级持续性威胁（APT）通常是由技术高超、往往有国家背景的攻击者实施的复杂长期网络攻击。通过将 C2 域名托管在看似无害的赌场网站上，攻击者利用了此类流量常见且很少被审查的特点，使检测和归因都变得更加困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.trendaisecurity.com/en-gb/resources-insights/trendai-security-blog/peckbirdy-script-framework">PeckBirdy : A Versatile Script Framework for LOLBins Exploitation...</a></li>
<li><a href="https://www.scworld.com/brief/peckbirdy-framework-used-by-china-linked-apts-targets-gambling-and-government-entities">PeckBirdy framework used by China-linked APTs targets gambling...</a></li>
<li><a href="https://www.varonis.com/blog/what-is-c2">What is C2? Command and Control Infrastructure Explained</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#APT`, `#malware`, `#threat-intelligence`, `#C2-infrastructure`

---