---
layout: default
title: "Horizon Summary: 2026-07-09 (ZH)"
date: 2026-07-09
lang: zh
---

> 从 36 条内容中筛选出 12 条重要资讯。

---

1. [OpenAI 发布 GPT-5.6，提供三个版本和六种推理等级](#item-1) ⭐️ 9.0/10
2. [Bun 从 Zig 重写为 Rust](#item-2) ⭐️ 9.0/10
3. [TypeScript 7.0 发布：Go 重写带来最高 12 倍速度提升](#item-3) ⭐️ 9.0/10
4. [蚂蚁开源全球首个 MoE 具身视频基模 LingBot-Video](#item-4) ⭐️ 9.0/10
5. [欧盟议会通过程序漏洞批准聊天控制 1.0](#item-5) ⭐️ 8.0/10
6. [Meta 推出 Muse Spark 1.1 并开放付费 API](#item-6) ⭐️ 8.0/10
7. [蜘蛛毒液选择性杀灭瓦螨，不伤蜜蜂](#item-7) ⭐️ 8.0/10
8. [OpenAI 推出 GPT-Live 语音模式，可委托 GPT-5.5 处理复杂任务](#item-8) ⭐️ 8.0/10
9. [Meta 超级智能进展：算力激增、RL 初创公司、建议](#item-9) ⭐️ 8.0/10
10. [大疆 EV50 无人机飞越珠峰 8861 米，创海拔纪录](#item-10) ⭐️ 8.0/10
11. [国家超算互联网核心节点在郑州上线](#item-11) ⭐️ 8.0/10
12. [OpenAI 修订五角大楼合同，禁止国内监控](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-5.6，提供三个版本和六种推理等级](https://openai.com/index/gpt-5-6/) ⭐️ 9.0/10

OpenAI 发布了 GPT-5.6，这是一款新的旗舰模型，提供三个版本（Luna、Terra、Sol）和六种推理努力等级，并在 ARC-AGI-3 基准测试上达到了新的最优水平。 此次发布标志着 AI 推理能力的重大进步，其中 Sol 版本成为首个在 ARC-AGI-3 游戏中获胜的前沿模型，预示着向更适应性和更智能的 AI 智能体迈进。 该模型在三个版本中引入了六种推理努力等级（none、low、medium、high、xhigh、max），其中 Sol 在 ARC-AGI-3 上达到 7.8%。开发者指南强调了改进的意图理解和原始图像尺寸保留。

hackernews · logickkk1 · 7月9日 17:04 · [社区讨论](https://news.ycombinator.com/item?id=48849066)

**背景**: ARC-AGI（人工通用智能抽象与推理语料库）是一个旨在衡量 AI 解决新颖推理任务能力的基准。ARC-AGI-3 是最新的交互式版本，挑战智能体实时适应新环境。之前的 GPT 模型（如 GPT-5.5、GPT-5.4）引入了推理努力等级以平衡成本与性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>

</ul>
</details>

**社区讨论**: 社区成员分享了模型输出的视觉示例（例如不同努力等级下的鹈鹕），并指出 GPT-5.6 Sol 是首个在 ARC-AGI-3 游戏中获胜的前沿模型。一些用户讨论了与其他编码工具（如 Claude Code）的比较，而另一些用户则指出 OpenAI 因竞争对手拒绝回答高级生物学问题而将其排除在基准测试之外。

**标签**: `#OpenAI`, `#GPT-5.6`, `#AI`, `#LLM`, `#ARC-AGI`

---

<a id="item-2"></a>
## [Bun 从 Zig 重写为 Rust](https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/#atom-everything) ⭐️ 9.0/10

Jarred Sumner 宣布 JavaScript 运行时 Bun 已从 Zig 重写为 Rust，新版本自 2025 年 6 月 17 日起已在 Claude Code 中部署。 此次重写解决了 Zig 版本中因混合垃圾回收和手动内存管理而常见的释放后使用、双重释放等内存安全漏洞。同时，它表明借助 AI 编码代理进行大规模重写是可行的，挑战了长期以来“应避免重写”的观念。 此次重写花费了约 16.5 万美元的 API 令牌（59 亿未缓存输入令牌、6.9 亿输出令牌），并利用 TypeScript 测试的一致性套件进行了 11 天的代理工程。Rust 移植版现已用于 Claude Code v2.1.181，在 Linux 上启动速度提升了 10%。

rss · Simon Willison · 7月8日 23:57

**背景**: Bun 是一个 JavaScript 运行时、包管理器和测试运行器，旨在作为 Node.js 的即插即用替代品，使用 JavaScriptCore 而非 V8 引擎。它最初用 Zig 编写，Zig 是一种需要手动内存管理的系统编程语言，当与垃圾回收结合时会导致内存安全漏洞。Rust 是一种内存安全语言，通过其所有权系统和 RAII（资源获取即初始化）模式在编译时防止此类错误。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Memory_safety">Memory safety - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（可能）赞扬了这项工程努力以及使用 AI 代理进行重写，但一些人质疑成本和 LLM 生成代码的长期可维护性。该帖子引发了人们对代理重写可行性的极大兴趣。

**标签**: `#Bun`, `#Rust`, `#Zig`, `#JavaScript runtime`, `#software engineering`

---

<a id="item-3"></a>
## [TypeScript 7.0 发布：Go 重写带来最高 12 倍速度提升](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 9.0/10

微软正式发布 TypeScript 7.0，这是用 Go 语言重写的原生版本，完整构建速度比旧版快 8 到 12 倍，并支持共享内存多线程。用户可通过 npm 安装，主流编辑器通过 LSP 支持新语言服务器。 此版本代表了 TypeScript 工具链的重大范式转变，显著提升了大型代码库上的开发者生产力。Go 重写为 JavaScript 生态中的语言服务器和编译器设定了新的性能基准。 新版本引入了 --checkers 和 --builders 参数以自定义并行度，并提供兼容包实现与 TypeScript 6 并存。但 Vue、Svelte 等嵌入式语言工具链因 API 尚未就绪，目前仍需使用旧版本。

telegram · zaihuapd · 7月9日 04:01

**背景**: TypeScript 是 JavaScript 的超集，增加了静态类型检查，其编译器最初是用 TypeScript 自身编写的。语言服务器协议（LSP）标准化了编辑器与语言服务器之间的通信，支持代码补全、跳转到定义等功能。用 Go 重写编译器可以更好地利用多核处理器并缩短启动时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.devbolt.dev/blog/typescript-7-go-rewrite">TypeScript 7.0: What the Go Rewrite Means for Every Developer</a></li>
<li><a href="https://betterstack.com/community/guides/scaling-nodejs/typescript-7-go-rewrite/">TypeScript 7.0: New Features and the Go-Powered Compiler Rewrite</a></li>

</ul>
</details>

**标签**: `#TypeScript`, `#Programming Languages`, `#Performance`, `#Microsoft`, `#Tooling`

---

<a id="item-4"></a>
## [蚂蚁开源全球首个 MoE 具身视频基模 LingBot-Video](https://www.qbitai.com/2026/07/446458.html) ⭐️ 9.0/10

蚂蚁集团开源了全球首个基于混合专家（MoE）架构的具身视频基础模型 LingBot-Video，采用 Apache 2.0 许可证。该模型在机器人操作评测基准 RBench 上取得最优结果，推理效率是同等规模稠密模型的 3 倍。 此次发布将 MoE 的高效性与机器人视频生成相结合，是具身 AI 领域的重要突破，可加速机器人学习并提升可扩展性。它为研究人员和开发者构建及部署具身 AI 系统降低了门槛。 LingBot-Video 总参数量为 30B，但每次推理仅激活约 3B 参数，采用 DiT+MoE 架构。模型基于 7 万小时具身数据训练，涵盖灵巧操作、机器人移动和第一视角交互，并引入了多维强化学习奖励系统。

telegram · zaihuapd · 7月9日 04:30

**背景**: 混合专家（MoE）是一种 AI 架构，通过多个专用子模型（专家）更高效地处理任务，优于单一稠密模型。扩散变换器（DiT）将变换器与扩散过程结合，用于高质量视频生成。具身 AI 专注于能在物理环境中感知和行动的模型，常用于机器人领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? - NVIDIA</a></li>
<li><a href="https://github.com/facebookresearch/DiT">GitHub - facebookresearch/DiT: Official PyTorch ...</a></li>

</ul>
</details>

**标签**: `#embodied AI`, `#MoE`, `#video generation`, `#open-source`, `#robotics`

---

<a id="item-5"></a>
## [欧盟议会通过程序漏洞批准聊天控制 1.0](https://www.patrick-breyer.de/en/eu-parliament-greenlights-chat-control-1-0-breyer-our-children-lose-out/) ⭐️ 8.0/10

2024 年 7 月 11 日，欧洲议会允许在无嫌疑情况下大规模扫描私人信息（聊天控制 1.0）通过，尽管投票的多数议员反对（314 票反对，276 票赞成，17 票弃权），因为否决动议未能获得所需的 361 票绝对多数。 该决定恢复了美国科技公司在 2028 年前无证扫描私人信息的做法，引发严重的隐私和民主担忧。它还凸显了欧盟立法程序中的操纵行为，可能削弱公众信任。 聊天控制 1.0 允许扫描 Instagram、Discord、Snapchat、Skype、Xbox、Gmail 和 iCloud 等平台上的直接消息，但不影响 WhatsApp 和 Signal 等端到端加密聊天。公共社交媒体帖子和云存储文件此前已可被扫描。

hackernews · rapnie · 7月9日 11:03 · [社区讨论](https://news.ycombinator.com/item?id=48843923)

**背景**: 聊天控制是指欧盟旨在打击儿童性虐待材料（CSAM）的立法，要求科技公司扫描私人通信。第一版聊天控制 1.0 最初于 2021 年自愿达成。专家评估表明，目前没有技术能在不产生高误报率的情况下检测 CSAM，从而影响普通通信。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://www.patrick-breyer.de/en/posts/chat-control/">Chat Control: The EU's CSAM scanner proposal</a></li>
<li><a href="https://www.reddit.com/r/europe/comments/1urnadd/european_parliament_greenlights_chat_control_10/">r/europe on Reddit: European Parliament greenlights Chat Control 1.0, will now become law. 276 In Favour, 314 Against, 17 Abstentians.</a></li>

</ul>
</details>

**社区讨论**: 评论者对程序性伎俩表示愤怒，指出投票在暑假前举行，许多议员缺席。一些人指出 WhatsApp 等端到端加密聊天不受影响，但其他人质疑 WhatsApp 的加密状态。普遍担忧欧盟正走向极权治理。

**标签**: `#privacy`, `#EU legislation`, `#surveillance`, `#democracy`

---

<a id="item-6"></a>
## [Meta 推出 Muse Spark 1.1 并开放付费 API](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) ⭐️ 8.0/10

Meta 发布了 Muse Spark 1.1，这是一个面向智能体任务的多模态推理模型，并首次向企业收取 API 使用费，价格为每百万输入令牌 1.25 美元、每百万输出令牌 4.25 美元。 这标志着 Meta 进入付费 AI 模型市场，以显著更低的价格直接与 OpenAI 和 Anthropic 竞争，可能使智能体 AI 商品化并重塑竞争格局。 该模型专为智能体任务构建，在工具使用方面有重大提升，但社区成员指出，由于在 Terminal-Bench 2.1 评估中覆盖了资源上限，基准测试结果可能无效。

hackernews · ot · 7月9日 14:10 · [社区讨论](https://news.ycombinator.com/item?id=48846184)

**背景**: 智能体 AI 模型旨在自主使用工具并执行多步骤任务。Meta 此前以开放权重形式发布了 Muse Spark，而 Muse Spark 1.1 引入了付费 API 层级，反映出向商业化转变的战略，同时仍提供开放权重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/">Introducing Muse Spark 1.1</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-07-09/meta-starts-charging-for-ai-with-muse-spark-1-1-agentic-model">Meta Starts Charging for AI With Muse Spark 1.1 Agentic Model - Bloomberg</a></li>
<li><a href="https://aiweekly.co/alerts/meta-prices-muse-spark-11-api-at-125425-per-m-tokens">Meta prices Muse Spark 1.1 API at $1.25/$4.25 per M tokens | AI Weekly</a></li>

</ul>
</details>

**社区讨论**: 社区意见分歧：一些人称赞低价和实用集成（例如 Simon Willison 的 LLM 插件），而另一些人则因资源上限违规质疑基准测试有效性，并讨论 Meta 是否应专注于削弱竞争对手而非与之匹敌。

**标签**: `#AI`, `#Meta`, `#agentic model`, `#open source`, `#benchmarking`

---

<a id="item-7"></a>
## [蜘蛛毒液选择性杀灭瓦螨，不伤蜜蜂](https://connectsci.au/news/news-parent/9703/Spider-venom-kills-varroa-mites-without-harming) ⭐️ 8.0/10

研究人员发现蜘蛛毒液能选择性杀灭瓦螨（Varroa destructor），而不伤害蜜蜂，为这一毁灭性害虫提供了新的生物防治方法。 瓦螨是全球最具破坏性的蜜蜂害虫，导致蜂群崩溃和巨大经济损失。一种选择性、对蜜蜂安全的治疗方法可能彻底改变养蜂业，并帮助保护全球授粉。 研究表明蜘蛛毒液成分靶向螨虫特有的离子通道，不影响蜜蜂生理。然而，将实验室结果转化为实用、廉价的蜂箱处理方法仍是一个重大挑战。

hackernews · Jedd · 7月9日 05:14 · [社区讨论](https://news.ycombinator.com/item?id=48841259)

**背景**: 瓦螨是一种外寄生螨虫，以蜜蜂为食并传播致命病毒，若不处理，蜂群常在 2-3 年内崩溃。现有杀螨剂可能伤害蜜蜂或污染蜂蜜，且耐药性日益增加。蜘蛛毒液含有多种毒素，进化出针对特定猎物的能力，使其成为选择性杀虫剂的潜在来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Varroa_mites">Varroa mites</a></li>
<li><a href="https://en.wikipedia.org/wiki/Varroa_destructor">Varroa destructor - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了谨慎乐观，指出实验室成功距离实际应用还很远。一些人强调需要廉价易用的治疗方法，并提到了基于菌丝体的免疫增强等替代方案。其他人质疑对蜜蜂的关注是否忽视了本土蜜蜂的保护。

**标签**: `#biology`, `#agriculture`, `#beekeeping`, `#pest control`, `#venom`

---

<a id="item-8"></a>
## [OpenAI 推出 GPT-Live 语音模式，可委托 GPT-5.5 处理复杂任务](https://simonwillison.net/2026/Jul/8/introducing-gptlive/#atom-everything) ⭐️ 8.0/10

OpenAI 推出了 GPT-Live，这是 ChatGPT 的一种新语音模式模型，能够在保持对话流畅的同时将复杂任务委托给 GPT-5.5。此次升级取代了之前基于 GPT-4o 时代的语音模型，现已向用户推送。 此次升级通过提供更强大、更新的模型，显著提升了 ChatGPT 语音模式的实用性，支持更丰富的头脑风暴和实时辅助。委托机制使得需要网络搜索或深度推理的任务能够无缝处理，而不会中断对话。 GPT-Live 在发布时使用 GPT-5.5 作为其后端前沿模型，并计划在未来更新到更新的模型。之前的语音模式基于 GPT-4o 时代的模型，知识截止于 2024 年，限制了其实用性。预览版中发现了一个 bug，模型会在非玩笑内容时打断并发出笑声，OpenAI 据称已进行了调整。

rss · Simon Willison · 7月8日 23:20

**背景**: ChatGPT 的语音模式允许用户与 AI 助手进行对话，用于语言练习和头脑风暴等任务。之前的模型基于 GPT-4o，知识截止于 2024 年，复杂推理能力较弱。GPT-5.5 于 2026 年 4 月发布，是 OpenAI 最新的前沿模型，推理能力和可靠性更强，GPT-Live 将其用于委托任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT-5.5</a></li>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT-5.5 | OpenAI</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（文章链接）可能包含对此次升级的积极反应，一些用户注意到自然度和能力的提升。关于不恰当笑声的 bug 被提及为一个小烦恼，OpenAI 已解决。

**标签**: `#OpenAI`, `#GPT-Live`, `#voice mode`, `#AI`, `#ChatGPT`

---

<a id="item-9"></a>
## [Meta 超级智能进展：算力激增、RL 初创公司、建议](https://newsletter.semianalysis.com/p/the-future-of-meta-superintelligence) ⭐️ 8.0/10

Meta 的超级智能项目实现了前所未有的激进算力扩展，一家顶级强化学习环境初创公司突然出现，文章还为 Google DeepMind 提供了战略建议。 这标志着 AI 基础设施投资和竞争的重大加速，可能重塑 AI 开发和部署的格局。 算力扩展涉及超过 2000 公里的跨区域扩展，由 Cisco 的'scale-across'网络技术实现，而 RL 环境初创公司是该领域日益增长的供应商之一。

rss · Semianalysis · 7月9日 19:16

**背景**: 超级智能指在多个领域超越人类智能的 AI 系统。强化学习环境是 AI 智能体通过试错学习的模拟世界。'Scale-across'是一种网络方法，通过长距离连接多个数据中心以整合算力资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thecuberesearch.com/cisco-enables-scale-across-ai-environments/">Cisco Enables "Scale-Across" AI environments - theCUBE Research</a></li>
<li><a href="https://alignlist.com/guides/top-40-rl-environments-startups-and-companies">Top 40 RL Environments Startups and Companies in 2026</a></li>
<li><a href="https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out">Tracking Trillions: The Assumptions Shaping the Scale of the ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#superintelligence`, `#compute`, `#Meta`, `#reinforcement learning`

---

<a id="item-10"></a>
## [大疆 EV50 无人机飞越珠峰 8861 米，创海拔纪录](https://www.163.com/dy/article/L1CUCV940514R9OJ.html) ⭐️ 8.0/10

大疆尚未发布的 EV50 垂直起降运载无人机在“巅峰使命”珠峰科考中成功飞越海拔 8861 米，创下同类无人机最高运行海拔世界纪录，并获取了 8000 米以上的大气数据。 这一成就展示了大疆先进的垂直起降技术及其在高原应急物流和气候研究中替代直升机的潜力，为极端环境下的低空货物运输开辟了新可能。 EV50 是一款复合翼无人机，可垂直起降并切换至固定翼巡航。在为期 12 天的任务中，它完成了 32 架次起降，连续爬升 3730 米，返程时仍剩 30%电量。

telegram · zaihuapd · 7月9日 06:00

**背景**: 垂直起降（VTOL）无人机结合了多旋翼的灵活性和固定翼的高效性。EV50 专为在恶劣环境中执行货物运输和科学任务而设计，有效载荷为 50 公斤。大疆计划将该技术用于百公里级货物运输等低空物流场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://laetimes.com/en/news/dji-ev50">Beyond Helicopters: DJI's EV50 Drone Brings Autonomous…</a></li>
<li><a href="https://laetimes.com/en/news/dji-ev50-8861">DJI EV50 Reaches 8,861 Metres Above Sea Level on Mount…</a></li>

</ul>
</details>

**标签**: `#drones`, `#DJI`, `#aviation`, `#technology`, `#record`

---

<a id="item-11"></a>
## [国家超算互联网核心节点在郑州上线](https://36kr.com/newsflashes/3887797387344387) ⭐️ 8.0/10

2026 年 7 月 9 日，国家超算互联网核心节点在郑州正式上线，可提供超过 10 万张国产人工智能算力卡。 这标志着中国国家 AI 计算基础设施的一个重要里程碑，因为它是接入国家超算互联网的最大单体国产 AI 算力资源池，显著提升了国家自主 AI 计算能力。 该节点旨在构建覆盖全国的计算资源统筹调度体系，承担运营管理、资源调度等核心功能，同时整合供需对接、产业孵化等综合服务。

telegram · zaihuapd · 7月9日 07:00

**背景**: 国家超算互联网是科技部于 2023 年 4 月指导启动建设的国家级算力服务平台，旨在整合全国超算、智算等算力资源。国产 AI 算力卡（如华为等厂商的产品）已从“能用”进入“好用”阶段，2025 年国产厂商在中国 AI 加速卡市场占有 41%的份额。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scnet.cn/home/subject/hxjd/index.html">国家超算互联网核心节点 - 超算互联网</a></li>
<li><a href="https://baike.baidu.com/item/国家超算互联网/62902938">国家超算互联网_百度百科</a></li>
<li><a href="https://baike.baidu.com/item/国产算力卡/67727675">国产算力卡_百度百科</a></li>

</ul>
</details>

**标签**: `#supercomputing`, `#AI infrastructure`, `#China`, `#national computing`, `#domestic hardware`

---

<a id="item-12"></a>
## [OpenAI 修订五角大楼合同，禁止国内监控](https://t.me/zaihuapd/42459) ⭐️ 8.0/10

OpenAI 与美国战争部（原国防部）已同意修订其 AI 合同，明确禁止将 AI 系统用于对美国公民的国内监控。该修订由 OpenAI 首席执行官 Sam Altman 主动提出，以回应伦理关切。 此举为军事合同中的 AI 伦理使用树立了先例，回应了公众对大规模监控的担忧。同时，这也使 OpenAI 与因类似问题面临批评的竞争对手 Anthropic 区分开来。 修订后的合同明确禁止使用 AI 对美国公民进行蓄意监控，并禁止利用商业获取的个人身份信息进行追踪或监测。修订条款尚未正式签署。

telegram · zaihuapd · 7月9日 13:22

**背景**: 2025 年 7 月，美国国防部向 OpenAI、Anthropic、Google 和 xAI 分别授予了高达 2 亿美元的合同，以加速 AI 在国家安全领域的应用。Anthropic 的合同后来因其 AI 模型 Claude 可能被用于大规模监控而引发争议，导致纠纷。OpenAI 主动修订合同旨在避免类似的批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/our-agreement-with-the-department-of-war/">Our agreement with the Department of War - OpenAI</a></li>
<li><a href="https://www.bbc.com/news/articles/c3rz1nd0egro">OpenAI changes deal with US military after backlash - BBC</a></li>
<li><a href="https://www.nytimes.com/2026/03/02/technology/openai-pentagon-deal-amended-surveillance.html">OpenAI Amends A.I. Deal With the Pentagon - The New York Times</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#OpenAI`, `#military AI`, `#surveillance`, `#policy`

---