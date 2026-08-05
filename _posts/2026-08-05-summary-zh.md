---
layout: default
title: "Horizon Summary: 2026-08-05 (ZH)"
date: 2026-08-05
lang: zh
---

> 从 91 条内容中筛选出 16 条重要资讯。

---

1. [Gwern 退出写作，启动守护天使 AI 项目](#item-1) ⭐️ 8.0/10
2. [DeepSeek V4 Flash 在单块 AMD MI300X 上运行，速度超 150 tok/s](#item-2) ⭐️ 8.0/10
3. [Keyv 及相关包在活跃的 Shai-Hulud npm 供应链攻击中受损](#item-3) ⭐️ 8.0/10
4. [Oxide Computer 完成 4.45 亿美元 D 轮融资](#item-4) ⭐️ 8.0/10
5. [LLM 0.32 新增推理痕迹、服务端工具与更智能的日志功能](#item-5) ⭐️ 8.0/10
6. [MiniMax-H3 通过 MLX 移植在苹果芯片上运行](#item-6) ⭐️ 8.0/10
7. [开源权重 AI 模型逼近前沿，安全差距扩大](#item-7) ⭐️ 8.0/10
8. [德克萨斯州暂停新建数据中心，因电网压力下令审计](#item-8) ⭐️ 8.0/10
9. [AI 大幅削减客服岗位](#item-9) ⭐️ 8.0/10
10. [Kimi K3：压缩记忆、跨深度注意力与潜在专家路由](#item-10) ⭐️ 8.0/10
11. [无复现代码的论文应被直接拒稿](#item-11) ⭐️ 8.0/10
12. [探索性建模：生成模型的新预训练维度](#item-12) ⭐️ 8.0/10
13. [华为提出“韬定律”，以时间缩微引领半导体新路径](#item-13) ⭐️ 8.0/10
14. [Cloudflare 弃用第三方安全工具，改用每月 58 美元的 AI 处理漏洞](#item-14) ⭐️ 8.0/10
15. [谷歌为 Anthropic 搭建 2000 亿美元华尔街融资机器](#item-15) ⭐️ 8.0/10
16. [我国首部 L3/L4 自动驾驶强制性国标报批](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Gwern 退出写作，启动守护天使 AI 项目](https://twitter.com/gwern/status/2084739205071343837) ⭐️ 8.0/10

Gwern 宣布退出全职写作和匿名身份，启动“守护天使”项目，该项目提出高度个性化的 LLM，模拟用户的价值观以提升生产力并防御 AI 驱动的威胁。该公告通过一条推文发布，链接到他发表在 gwern.net 上的详细文章。 此事意义重大，因为 Gwern 是 AI 社区中备受尊敬的人物，他转向 AI 创业标志着个人构建 AI 工具以对抗企业 AI 对齐的趋势日益增长。该项目挑战了当前的聊天机器人范式，可能影响 AI 助手的开发和使用方式。 “守护天使”提案包括动态评估、主动学习和本地优先 UI 等技术，以创建用户的“数字孪生”。Gwern 强调当前聊天机器人与用户不一致，而与公司所有者一致，他的项目旨在让个人更好地控制其 AI 交互。

hackernews · mattsterett · 8月4日 20:48 · [社区讨论](https://news.ycombinator.com/item?id=49174900)

**背景**: AI 对齐指的是确保 AI 系统按照人类价值观和意图行事的挑战。Gwern 的项目是对大型语言模型（LLM）被优化用于企业利益（如广告和订阅）而非个人用户利益的担忧的回应。“守护天使”AI 的想法受到“上传”思想到数字形式的启发，旨在创建一种增强用户能力而非取代用户的个人 AI。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gwern.net/guardian-angel">Guardian Angels: LLM Personalization for Productivity and ...</a></li>
<li><a href="https://www.devdigest.org/articles/gwerns-guardian-angel-personalized-llms-for-productivity-and-security">Gwern's Guardian Angel: Personalized LLMs for Productivity a</a></li>
<li><a href="https://ecency.com/@crrdlx/gwern-moving-from-writing-to-ai-startup">Gwern moving from writing to AI startup | Ecency</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些人称赞 Gwern 的人性和远见，而另一些人则表示怀疑，称该项目是“一种狂热”，并质疑其对生产力而非自我实现的强调。也有对该项目细节及其潜在影响的好奇。

**标签**: `#AI alignment`, `#pseudonymity`, `#personal AI`, `#Gwern`, `#tech community`

---

<a id="item-2"></a>
## [DeepSeek V4 Flash 在单块 AMD MI300X 上运行，速度超 150 tok/s](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐️ 8.0/10

一个 GitHub 项目展示了在单块 AMD MI300X 加速器上以完整权重运行 DeepSeek V4 Flash，速度超过每秒 150 个 token。上下文窗口从原来的 1M 减少到 256k。 这一成就表明，前沿级 MoE 模型可以在单块高端 GPU 上运行，可能降低硬件成本，并使本地或边缘部署更加可行。它凸显了 AMD MI300X 在大型推理方面的日益增强的能力。 该模型是一个 284B 参数的混合专家模型，激活参数为 13B，原始支持 1M token 上下文。减少到 256k 上下文对于许多编码和智能体任务仍然实用，并且保留了完整权重，没有进行量化。

hackernews · zhoutong · 8月4日 10:00 · [社区讨论](https://news.ycombinator.com/item?id=49166386)

**背景**: DeepSeek V4 Flash 是 DeepSeek V4 系列的轻量级变体，专为编码、工具使用和智能体工作流设计。AMD MI300X 是一款具有 192GB 高带宽内存（HBM）的加速器，适合运行大型模型。每秒 token 数是交互式推理的关键指标，而内存带宽常常限制性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lmstudio.ai/models/deepseek-v4-flash">DeepSeek V4 Flash - lmstudio.ai</a></li>
<li><a href="https://www.orcarouter.ai/blog/deepseek-v4-flash-official-release">DeepSeek V4 Flash: Official Release, Explained - orcarouter.ai</a></li>
<li><a href="https://tokoscope.com/articles/deepseek-v4-flash">DeepSeek V4 Flash: The Fastest Open-Weight Frontier Model in ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，MI300X 通常以 8 卡整机形式销售，难以单独购买，并建议 MI350P 作为 PCIe 替代品，拥有 144GB 内存。一些人指出，像 DwarfStar 这样的先前工作可以在更少内存下运行相同模型，另一些人则赞赏为了高速度而减少上下文窗口的实用权衡。

**标签**: `#DeepSeek`, `#AMD MI300X`, `#LLM inference`, `#hardware`, `#quantization`

---

<a id="item-3"></a>
## [Keyv 及相关包在活跃的 Shai-Hulud npm 供应链攻击中受损](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) ⭐️ 8.0/10

一场活跃的 npm 供应链攻击已攻陷 Keyv 包及其他 400 多个包，Shai-Hulud 蠕虫会窃取凭据并自我传播。该攻击由 JFrog 安全研究团队发现，目前仍在持续。 此次攻击影响了广泛使用的 npm 包，可能危及数千个下游项目并泄露敏感凭据。它凸显了开源依赖生态系统的脆弱性，以及加强供应链安全措施的紧迫性。 Shai-Hulud 蠕虫会将自己发布到每个可写的 npm 包中，并在 GitHub 仓库中植入执行钩子。它窃取凭据，并利用静态和动态分析来逃避检测，且新版本不断出现。

hackernews · cimi_ · 8月4日 11:01 · [社区讨论](https://news.ycombinator.com/item?id=49166874)

**背景**: Shai-Hulud 是一种针对 npm 生态系统的自我复制蠕虫，于 2025 年底首次被发现。它利用被攻陷的包进行传播，通常通过预安装或后安装钩子，并与重大的云原生生态系统入侵有关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.jfrog.com/post/shai-hulud-is-back-august/">Major Shai Hulud campaign strikes npm again, affecting keyv and 400+ packages - JFrog Security Research</a></li>
<li><a href="https://unit42.paloaltonetworks.com/npm-supply-chain-attack/">"Shai-Hulud" Worm Compromises npm Ecosystem in Supply Chain ...</a></li>
<li><a href="https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack">Shai-Hulud 2.0 Supply Chain Attack: 25K+ Repos Exposing Secrets</a></li>

</ul>
</details>

**社区讨论**: 社区成员对此次攻击表示担忧，有人呼吁暂停预安装钩子，也有人推荐使用 devcontainers 或 Packj 等工具进行检测。还有人请求提供 grep 模式以检查本地 node_modules 是否被入侵。

**标签**: `#supply chain`, `#npm`, `#security`, `#open source`, `#dependency`

---

<a id="item-4"></a>
## [Oxide Computer 完成 4.45 亿美元 D 轮融资](https://www.sec.gov/Archives/edgar/data/1795071/000179507126000002/xslFormDX01/primary_doc.xml) ⭐️ 8.0/10

根据最近的 SEC Form D 文件，Oxide Computer Company 已完成 4.45 亿美元的 D 轮融资。此前该公司在 2023 年完成 4400 万美元 A 轮融资，2025 年完成 1 亿美元 B 轮融资，2026 年完成 2 亿美元 C 轮融资。 这笔巨额融资凸显了投资者对 Oxide 机架级硬件和软件方案在本地云基础设施领域的高度信心。这可能加速公司发展，挑战数据中心市场的现有参与者，并可能使寻求超大规模云提供商替代方案的企业受益。 该融资通过 SEC Form D 文件披露，该文件用于 Regulation D 下的豁免发行。Oxide 设计并制造机架级系统，为本地数据中心提供集成的软件和硬件，服务企业和联邦机构。

hackernews · depr · 8月4日 20:13 · [社区讨论](https://news.ycombinator.com/item?id=49174407)

**背景**: Oxide Computer Company 是一家硬件初创公司，由来自 Joyent 和 Amazon 等公司的前工程师创立，包括 Bryan Cantrill 和 Adam Leventhal。该公司旨在提供完整、集成的云平台，让客户可以拥有并在本地运营，与传统云提供商形成对比。Form D 是向 SEC 提交的通知，用于报告豁免证券发行，允许私营公司在无需全面公开注册的情况下筹集资金。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://oxide.computer/press">Press | Oxide Computer Company</a></li>
<li><a href="https://www.linkedin.com/company/oxidecomputer">Oxide Computer Company - LinkedIn</a></li>
<li><a href="https://www.bloomberg.com/profile/company/1776316D:US">Oxide Computer Co - Company Profile and News - Bloomberg Markets</a></li>
<li><a href="https://en.wikipedia.org/wiki/Form_D">Form D - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些人对产品概念和公司进展表示兴奋，而另一些人则对产品可用性和销售响应提出担忧。一位评论者提到，他们提交了销售咨询但从未收到回复，尽管每年在 AWS 上花费 90 万美元；另一位则质疑 Oxide 是否真的向客户发货硬件。

**标签**: `#funding`, `#hardware`, `#startup`, `#Oxide Computer`

---

<a id="item-5"></a>
## [LLM 0.32 新增推理痕迹、服务端工具与更智能的日志功能](https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything) ⭐️ 8.0/10

LLM 0.32 于 2026 年 8 月 4 日发布，为推理模型引入了可见的推理痕迹，支持服务端工具（如 OpenAI 的 CodeInterpreter 和 WebSearch），并重新设计了内容可寻址的 SQLite 日志。它还新增了 GPT-5.6 模型系列，其中 GPT-5.6 Luna 成为新的默认模型，并新增了“llm openai endpoint”命令，用于对任何兼容 OpenAI 的端点执行一次性提示。 此版本通过使推理痕迹可见并支持服务端工具，显著提升了 LLM 这一广泛使用的 CLI 工具的实用性，符合当前 AI 向智能体工作流发展的趋势。日志改进和新的端点命令也简化了开发者和高级用户的工作流程，可能提高采用率和生产力。 默认情况下，推理痕迹会显示到标准错误输出，并可通过-R/--hide-reasoning 标志禁用。llm-anthropic 插件新增了 WebSearch、WebFetch、CodeExecution 和 AnthropicMCP 工具，支持在单个请求中执行 MCP 调用。“llm openai endpoint”命令不记录提示，非常适合一次性交互。

rss · Simon Willison · 8月4日 23:58

**背景**: LLM 是一个 CLI 工具和 Python 库，用于与各种大型语言模型交互，将结果存储在 SQLite 中，并生成嵌入。它支持插件以添加更多模型和工具。OpenAI Responses API 于 2025 年 3 月发布，通过结合聊天补全和高级工具调用能力简化了智能体应用，LLM 0.32 利用了这一点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm.datasette.io/en/stable/">LLM: A CLI utility and Python library for ... - Datasette</a></li>
<li><a href="https://github.com/simonw/llm">GitHub - simonw/llm: Access large language models from the ... llm - a tool for Datasette LLM: A CLI utility and Python library for interacting with ... llm CLI Tool Guide 2026: Run Any LLM From Your Terminal GitHub - sorokinvld/llmcli: Access large language models from ...</a></li>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>

</ul>
</details>

**标签**: `#LLM`, `#CLI`, `#AI`, `#OpenAI`, `#release`

---

<a id="item-6"></a>
## [MiniMax-H3 通过 MLX 移植在苹果芯片上运行](https://simonwillison.net/2026/Aug/4/minimax-h3-mlx/#atom-everything) ⭐️ 8.0/10

Simon Willison 使用 PipeNetwork/minimax-h3-mlx Python 包，在 M5 Max MacBook Pro 上成功运行了 MiniMax 的新型全模态 MiniMax-H3 模型，并根据文本提示生成了带音频的 15 秒视频片段。该模型接受文本、图像、音频和视频输入，可生成高达 2K 分辨率、带原生立体声音频的视频。 这表明尖端的全模态生成模型可以在消费级苹果硬件上本地运行，使开发者无需依赖云端即可使用先进的 AI 视频生成功能。MLX 移植降低了实验门槛，可能加速多模态 AI 在创意和开发工作流程中的采用。 模型下载需要约 115 GB 存储空间，在 M5 Max 上生成视频耗时不到 45 分钟。由于未提供音频相关的提示指导，生成的音频被描述为“奇怪的类似语音的垃圾”，这凸显了遵循提示指南以获得最佳结果的重要性。

rss · Simon Willison · 8月4日 19:10

**背景**: MiniMax-H3 是一个开放权重、通用型的全模态生成模型，能够在统一架构中理解和生成文本、图像、视频和音频。MLX 是 Apple 专为 Apple 芯片设计的高效机器学习数组框架，MLX 移植使得此类模型可以在 Mac 上本地运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between ...</a></li>
<li><a href="https://fal.ai/minimax-h3">MiniMax H3 - Open-Weights General-Purpose Multimodal Video ...</a></li>
<li><a href="https://github.com/ml-explore/mlx">GitHub - ml-explore/mlx: MLX: An array framework for Apple silicon · GitHub</a></li>

</ul>
</details>

**标签**: `#MLX`, `#MiniMax-H3`, `#multimodal`, `#Apple Silicon`, `#video generation`

---

<a id="item-7"></a>
## [开源权重 AI 模型逼近前沿，安全差距扩大](https://techcrunch.com/2026/08/04/open-weight-ai-models-are-catching-up-to-the-frontier-the-safety-gap-remains/) ⭐️ 8.0/10

SaferAI 的一份新报告指出，Z.ai 的开源权重模型 GLM-5.2 正接近前沿 AI 能力，但缺乏必要的安全缓解措施，加剧了人们对治理和监管的担忧。 这一进展凸显了开源权重模型的快速进步与安全及治理框架发展缓慢之间的紧张关系。它可能影响关于如何监管强大开源 AI 系统的政策讨论，进而影响开发者、研究人员及整个 AI 生态系统。 GLM-5.2 由中国的 Z.ai 公司开发，是一款开源权重模型，采用 MIT 或 Apache 2.0 等宽松许可证发布，允许本地或云端部署。SaferAI 报告特别指出，GLM-5.2 接近前沿能力，但缺乏关键安全缓解措施，引发了对潜在滥用的担忧。

rss · TechCrunch AI · 8月4日 20:05

**背景**: 开源权重模型是指公开其学习参数（权重和偏置）的 AI 模型，允许他人下载和使用，修改权限取决于许可证。前沿 AI 指的是最先进的通用模型，通常构建成本高昂且配备广泛的安全措施。GLM 系列（包括 GLM-5.2）是 Z.ai（中国领先的 AI 公司之一）的旗舰开源权重模型系列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>
<li><a href="https://en.wikipedia.org/wiki/Frontier_AI">Frontier AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM-5.2">GLM-5.2</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#open-weight models`, `#frontier AI`, `#governance`, `#GLM-5.2`

---

<a id="item-8"></a>
## [德克萨斯州暂停新建数据中心，因电网压力下令审计](https://techcrunch.com/2026/08/04/texas-halts-new-data-centers-as-governor-calls-for-audits/) ⭐️ 8.0/10

由于电网压力，德克萨斯州已暂停批准新建数据中心，并下令对现有数据中心进行审计，州长格雷格·阿博特宣布了这一决定。这标志着该州此前对数据中心友好的政策发生了重大转变。 此举标志着数据中心扩张的重大转变，凸显了即使在监管宽松的州，电力基础设施也存在限制。这将影响计划建设新设施的科技公司、能源政策和区域规划，并可能为面临类似挑战的其他州树立先例。 在州长格雷格·阿博特指示各机构制定数据中心法规（包括要求数据中心支付基础设施费用并接受筛选程序）之后，暂停和审计措施出台。该州电网因数据中心需求上升而承压，预计到 2030 年需求将增长近两倍。

rss · TechCrunch AI · 8月4日 15:42

**背景**: 数据中心是容纳计算机系统及相关组件的大型设施，消耗大量电力。在美国，数据中心电力需求预计明年将增长 22%，到 2030 年将增长近两倍，给区域电网带来压力并推高成本。德克萨斯州以其宽松的法规和充足的电力供应，一直是数据中心开发商的热门目的地，但快速增长已将电网推向极限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.edgesg.com/2026/01/07/data-centers-are-overwhelming-power-grids-worldwide/">Data Centers Are Overwhelming Power Grids Worldwide</a></li>
<li><a href="https://www.fox7austin.com/news/new-texas-data-center-rules">Texas regulators announce new rules for data centers | FOX 7 Austin</a></li>
<li><a href="https://comptroller.texas.gov/taxes/data-centers/">State Sales Tax Exemption for Qualifying Data Centers and ...</a></li>

</ul>
</details>

**标签**: `#data centers`, `#energy policy`, `#Texas`, `#infrastructure`, `#tech industry`

---

<a id="item-9"></a>
## [AI 大幅削减客服岗位](https://www.solidot.org/story?sid=84994) ⭐️ 8.0/10

澳大利亚联邦银行、微软、Uber 和凯悦酒店等大公司正使用 AI 聊天机器人和自动化电话系统取代人工客服工作，导致大量岗位被裁减。微软将客服团队从约 5 万人缩减至 4 万人，Uber 为“拥抱 AI”裁减了 10%的客服岗位。 这一趋势标志着劳动力市场的重大转变，分析师估计到 2030 年近半客服岗位将受到影响。这对美国、印度和菲律宾等雇用数百万呼叫中心从业者的国家具有广泛影响，也凸显了生成式 AI 在企业运营中的加速应用。 澳大利亚联邦银行裁减了数百名客服，每年节省数千万美元。微软销售和服务运营负责人 Judson Althoff 表示，AI 每年为公司节省约 7.5 亿美元的客服成本，同时指出复杂问题仍需人工支持。凯悦酒店去年裁掉了美洲地区三成的内部客服。

rss · Solidot 奇客 · 8月3日 14:22

**背景**: 客户服务呼叫中心传统上是主要的就业来源，尤其是在印度和菲律宾等国，西方公司曾将支持岗位外包到这些地方。生成式 AI 的进步以及高管面临采用新技术的压力，正促使企业用自动化系统取代人工客服。这一转变是 AI 自动化影响多个就业领域的更广泛趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.commbox.io/the-new-era-of-generative-ai-customer-service-empowering-humans-with-automation/">The New Era of Generative AI Customer Service ... - CommBox</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-in-customer-service">AI in Customer Service | IBM</a></li>

</ul>
</details>

**标签**: `#AI`, `#Customer Service`, `#Employment`, `#Automation`, `#Industry Trends`

---

<a id="item-10"></a>
## [Kimi K3：压缩记忆、跨深度注意力与潜在专家路由](https://newsletter.semianalysis.com/p/kimi-k3-the-manos-the-mythos-the) ⭐️ 8.0/10

SemiAnalysis 发布了对 Kimi K3 架构的深入技术分析，详细介绍了压缩记忆（Kimi Delta Attention）、跨深度注意力和潜在专家路由（LatentMoE）等创新，这些创新提升了推理性能。 该分析对 AI/ML 研究人员和工程师具有高度相关性，因为 Kimi K3 的架构可能为高效 LLM 推理树立新标准，减少内存占用并提升速度。这些创新可能会影响整个行业未来的模型设计和推理优化。 Kimi K3 使用 Kimi Delta Attention (KDA)，这是一种类似于多头潜在注意力 (MLA) 的压缩注意力机制，可大幅减少每个 token 的 KV 缓存占用。LatentMoE 在分派前压缩路由 token，在聚合后解压缩，在 Stable LatentMoE 变体中，上投影（解压缩）操作前应用 RMSNorm。

rss · Semianalysis · 8月3日 19:42

**背景**: 大型语言模型 (LLM) 依赖注意力机制，该机制存储键值 (KV) 缓存，随着上下文长度和内存使用量的增加而增长。像 KDA 这样的压缩注意力减少了这种占用，而跨深度注意力允许层选择性地重用早期表示，改善信息流。在混合专家 (MoE) 模型中，潜在专家路由通过在路由前压缩 token 来减少通信开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wan27.org/blog/kimi-k3-vram-guide">Kimi K3 VRAM Requirements: How Much Memory You Actually Need to Run K3 | Wan 2.7</a></li>
<li><a href="https://vllm.ai/blog/2026-07-27-k3">Kimi K3 Is Here: Efficient Day-0 Support on vLLM | vLLM Blog</a></li>
<li><a href="https://arxiv.org/abs/2606.05014">Depth-Attention: Cross-Layer Value Mixing for Language Models</a></li>

</ul>
</details>

**标签**: `#LLM`, `#architecture`, `#inference`, `#Kimi K3`, `#AI research`

---

<a id="item-11"></a>
## [无复现代码的论文应被直接拒稿](https://www.reddit.com/r/MachineLearning/comments/1vei12v/its_time_to_desk_reject_papers_that_dont_include/) ⭐️ 8.0/10

一位审稿人报告称，今年为机器学习顶会审稿的 12 篇论文中，仅 1 篇提供了完整可运行代码，5 篇提供部分代码的论文中有 3 篇存在使结果失效的明显错误。他们主张强制提交代码，并以直接拒稿作为惩罚。 这凸显了机器学习研究中的可复现性危机，隐藏代码损害了研究质量和信任。强制提交代码可能改变激励，提升验证能力并减少虚假声明，影响研究人员、审稿人及整个 AI 社区。 审稿人指出 12 篇论文中有 7 篇未提供代码，仅 1 篇能运行从输入到 AUROC 的完整流程。他们建议对缺失代码的论文直接拒稿，并指出现有激励促使作者隐藏代码以避免被发现错误。

reddit · r/MachineLearning · /u/Flaky-Ambition5900 · 8月3日 16:17

**背景**: 直接拒稿（desk rejection）指编辑未经同行评审即拒绝稿件，通常因不符合范围或质量标准。AUROC（受试者工作特征曲线下面积）是二分类任务常用的性能指标，范围从 0.5（随机）到 1.0（完美）。可复现性是机器学习领域日益关注的问题，许多论文未共享代码，阻碍了验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Receiver_operating_characteristic">Receiver operating characteristic - Wikipedia</a></li>
<li><a href="https://peerreviewai.org/guides/desk-rejection-prevention">How to Avoid Desk Rejection | PeerReviewAI</a></li>

</ul>
</details>

**标签**: `#reproducibility`, `#machine learning`, `#research practices`, `#peer review`

---

<a id="item-12"></a>
## [探索性建模：生成模型的新预训练维度](https://www.reddit.com/r/MachineLearning/comments/1vf6r6f/explorative_modeling_unlocking_a_third/) ⭐️ 8.0/10

该论文提出“探索性建模”作为除参数和数据之外的第三个预训练维度，模型在生成结果与数据之间探索 K 个候选匹配，并训练最优匹配以避免模式模糊。该方法支持端到端生成，并在图像、视频和语言领域展现出单调的性能提升。 这项工作可能重新定义生成模型的扩展方式，为改进提供新的维度，补充现有的扩展定律。它可能带来跨模态更稳健和准确的生成，影响 AI 的研究和实际应用。 该方法对训练循环而非生成过程进行分解，探索 K 个候选匹配并训练最优匹配。它在连续和离散领域均有效，包括图像、视频和语言，且探索规模的增加单调地提升性能。

reddit · r/MachineLearning · /u/Benlus · 8月4日 10:42

**背景**: 传统生成模型通过增加参数和数据来扩展，但本文引入探索作为第三个维度。该方法解决了模式模糊问题，即模型在多个合理输出上取平均，通过在训练中承诺特定模式来应对。这与提升生成模型保真度和多样性的更广泛趋势相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explorative-modeling.github.io/">Explorative Modeling: Unlocking a Third Pretraining Axis and ...</a></li>
<li><a href="https://arxiv.org/abs/2607.27372">[2607.27372] Explorative Modeling: Unlocking a Third ...</a></li>
<li><a href="https://arxiv.org/html/2607.27372v1">Explorative Modeling: Unlocking a Third Pretraining Axis and ...</a></li>

</ul>
</details>

**标签**: `#pretraining`, `#machine learning`, `#generative models`, `#research`

---

<a id="item-13"></a>
## [华为提出“韬定律”，以时间缩微引领半导体新路径](https://t.me/zaihuapd/42966) ⭐️ 8.0/10

在上海举行的 2026 年国际电路与系统研讨会（ISCAS）上，华为正式提出“韬定律”（τ定律），主张半导体演进从传统的“几何缩微”转向“时间缩微”。华为声称过去六年已据此设计并量产 381 款芯片，今年秋季将推出采用逻辑折叠技术的新麒麟手机芯片。 这一宣布意义重大，因为它提出了摩尔定律（正逼近物理极限）的替代方案，可能重塑全球半导体产业的路线图。若得到验证，它可能减少对极紫外光刻（EUV）的依赖，挑战 ASML 等设备制造商的优势地位，影响竞争格局。 韬定律通过降低时间常数（τ），在器件、电路、芯片和系统层面进行多层级协同优化，并利用逻辑折叠技术对电路拓扑进行三维重构。华为预计，到 2031 年，基于该定律的高端芯片晶体管密度可达 1.4 纳米制程同等水平，并强调以开放合作推动产业发展。

telegram · zaihuapd · 8月4日 08:04

**背景**: 摩尔定律预测集成电路上晶体管密度大约每两年翻一番，数十年来推动了半导体进步，但现在正逼近物理极限。几何缩微（传统上缩小晶体管尺寸的方法）面临漏电增加和制造复杂度提升等挑战。韬定律提出通过优化时间相关参数来替代，可能在不单纯依赖光刻微缩的情况下延续性能提升。逻辑折叠是关键技术之一，它通过三维堆叠电路逻辑路径来缩短信号传输距离，与传统的 Chiplet 封装等 3D 封装技术不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/时间缩微/67842555">时间缩微_百度百科</a></li>
<li><a href="https://www.zhihu.com/question/2042175008198357766">如何评价华为发表的半导体领域新定律“韬（τ）定律”？</a></li>
<li><a href="https://xueqiu.com/1578376429/390887181">华为“韬 (τ)定律”深度研究（半导体产业从“几何缩微”到“时间缩微”的范...</a></li>

</ul>
</details>

**社区讨论**: 知乎和雪球等平台上的社区讨论反应不一。一些人兴奋地认为这可能带来突破，减少对 ASML 的依赖，而另一些人则持怀疑态度，质疑缺乏详细技术数据以及到 2031 年实现 1.4 纳米等效密度的可行性。关于逻辑折叠是否真正区别于先进封装也存在争论，有人澄清它是设计层面的电路拓扑重构，而非简单的芯片堆叠。

**标签**: `#semiconductors`, `#Huawei`, `#Moore's Law`, `#chip design`, `#technology`

---

<a id="item-14"></a>
## [Cloudflare 弃用第三方安全工具，改用每月 58 美元的 AI 处理漏洞](https://www.theregister.com/security/2026/08/04/cloudflare-has-mostly-ditched-third-party-security-tools-suggests-not-trying-that-at-home/5282600) ⭐️ 8.0/10

Cloudflare 首席安全官 Grant Bourzikas 透露，公司已使用 Anthropic 的 Claude Sonnet 模型自动化处理漏洞赏金报告，每月仅花费 58 美元，并已构建 200 多个自主安全代理，基本取代了第三方安全工具。 这标志着向 AI 驱动的安全运营的重大转变，与专用模型（Mythos 每月约 20 万美元）相比成本大幅节省。它凸显了 AI 变革安全工作流程的潜力，但 Cloudflare 建议其他企业不要效仿，因其具备独特的自研能力。 每月 58 美元的费用用于 Claude Sonnet 对漏洞报告进行去重和价值评估，而安全专用模型 Mythos 执行相同任务每月需约 20 万美元。Cloudflare 还构建了 200 多个自主安全代理，并用自研应用（部分由 AI 辅助编写）取代了大多数第三方工具。首席安全官 Bourzikas 提醒，并非每家公司都应自研安全软件。

telegram · zaihuapd · 8月4日 09:24

**背景**: Cloudflare 是一家主要的网络基础设施和安全公司，越来越多地将 AI 集成到其产品中。Claude Sonnet 是 Anthropic 的高性价比大语言模型，而 Mythos 是专注于网络安全、以攻击性安全能力著称的专用模型。该公司的举措反映了使用通用 LLM 处理安全任务的更广泛趋势，例如 GitHub 也使用 Claude Sonnet 进行漏洞分类。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.adwaitx.com/github-ai-taskflow-agent-vulnerability-triage/">GitHub Deploys AI to Triage Vulnerabilities : 30 Flaws Found</a></li>
<li><a href="https://www.speakeasy.com/blog/mythos-security-story/">The Mythos security story is only half told</a></li>
<li><a href="https://www.cloudflare.com/products/agents/">Cloudflare Agents - Build Stateful AI Agents</a></li>

</ul>
</details>

**标签**: `#AI`, `#security`, `#Cloudflare`, `#vulnerability management`, `#automation`

---

<a id="item-15"></a>
## [谷歌为 Anthropic 搭建 2000 亿美元华尔街融资机器](https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c) ⭐️ 8.0/10

谷歌悄然搭建了一个约 2000 亿美元规模的基础设施融资架构，以向 Anthropic 交付超过 1500 亿美元的 AI 芯片。今年 6 月，通过名为 Compute SPV 的特殊目的载体完成的首批交易涉及约 350 亿美元硬件，相当于 1 吉瓦算力和 100 万颗 TPU。 这种新颖的厂商融资模式在多方之间分散风险，使 Anthropic 在无信用评级的情况下也能获得庞大的 AI 算力。这可能重塑 AI 基础设施的融资方式，加速大规模 AI 模型的部署，影响整个 AI 生态系统。 该架构中，谷歌为数据中心提供担保，博通购买并协助融资芯片，阿波罗和黑石购买硬件后回租给 Anthropic。约 80%的合同与芯片直接挂钩，参与方还包括摩根士丹利及多家加密矿企。

telegram · zaihuapd · 8月4日 10:52

**背景**: 厂商融资是一种卖方为买方提供贷款的信用安排，常用于昂贵设备。谷歌的张量处理单元（TPU）是为加速机器学习工作负载而设计的定制 AI 芯片。该模式借鉴了波音和 GE 推销飞机和发动机的厂商融资玩法，使各方都不必把数百亿美元硬件资产压在资产负债表上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nucleuscommercialfinance.com/finance-glossary/vendor-finance/">Vendor Finance | What is Vendor Finance for Business?</a></li>
<li><a href="https://www.linkedin.com/pulse/googles-ai-tpus-secret-engine-powering-revolution-bayonle-akinmurele-wkmuf">Google's AI TPUs : The Secret Engine Powering the AI Revolution</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#Google`, `#Anthropic`, `#financing`, `#chips`

---

<a id="item-16"></a>
## [我国首部 L3/L4 自动驾驶强制性国标报批](https://t.me/zaihuapd/42972) ⭐️ 8.0/10

工信部已完成《智能网联汽车自动驾驶系统安全要求》强制性国家标准报批稿，并于 6 月 17 日起公示，建议 2027 年 7 月 1 日实施。这是我国首部针对 L3 和 L4 级自动驾驶的强制性国家标准。 该标准标志着我国自动驾驶监管从“概念松绑”转向“安全硬约束”，引入 Safety Case 机制，要求企业系统性论证安全性。这将深刻影响车企和技术供应商，迫使其摒弃模糊宣传，采用严格的安全验证实践。 该标准引入了 Safety Case 安全档案机制，要求企业用“声明—论据—证据”结构证明安全性。它还分别对 L3 人机交接（包括驾驶人接管能力监测）和 L4 系统自主风险处置提出要求，并规范人机交互与用户告知，防范误用滥用风险。

telegram · zaihuapd · 8月4日 13:06

**背景**: 自动驾驶按等级分为 L0 至 L5，其中 L3（有条件自动驾驶）和 L4（高度自动驾驶）是系统接管驾驶任务的关键阶段。Safety Case 是一套由证据支持的结构化安全论证体系，用于证明系统在特定环境下运行是可接受安全的，其监管逻辑从“满足条款”转向“自证安全”。中国新标准是全球自动驾驶安全监管进入 Safety Case 时代趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://yfrobotics.github.io/self-driving-handbook-cn/system/safety/">系统安全保障 - 自动驾驶指南 - GitHub Pages</a></li>
<li><a href="https://baike.baidu.com/item/Safety+Case/67871945">Safety Case - 百度百科</a></li>
<li><a href="https://www.autohome.com.cn/news/202608/1316205.html">autohome.com.cn/news/202608/1316205.html</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#regulation`, `#China`, `#safety standard`, `#L3/L4`

---