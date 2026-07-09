---
layout: default
title: "Horizon Summary: 2026-07-09 (ZH)"
date: 2026-07-09
lang: zh
---

> 从 40 条内容中筛选出 15 条重要资讯。

---

1. [TypeScript 7.0 用 Go 重写编译器，速度提升 10 倍](#item-1) ⭐️ 9.0/10
2. [欧盟即将重启私密信息扫描法规](#item-2) ⭐️ 9.0/10
3. [Bun 从 Zig 重写为 Rust](#item-3) ⭐️ 9.0/10
4. [约翰迪尔就维修权诉讼与 FTC 达成和解](#item-4) ⭐️ 8.0/10
5. [OpenAI 探讨提升编程评估信号质量](#item-5) ⭐️ 8.0/10
6. [Mistral 发布 Robostral Navigate，实现无地图导航](#item-6) ⭐️ 8.0/10
7. [xAI 发布基于 Cursor 数据的 Grok 4.5](#item-7) ⭐️ 8.0/10
8. [OpenAI 推出 GPT-Live 实时语音模式](#item-8) ⭐️ 8.0/10
9. [Cloudflare Meerkat：首个生产级异步共识协议](#item-9) ⭐️ 8.0/10
10. [LingBot-Video：开源稀疏 MoE 视频扩散 Transformer](#item-10) ⭐️ 8.0/10
11. [阿里下令员工 7 月 10 日前卸载 Claude](#item-11) ⭐️ 8.0/10
12. [华为 5G 旗舰重返海外，峰值速率突破 1100 Mbps](#item-12) ⭐️ 8.0/10
13. [安卓远程 Root 漏洞链曝光](#item-13) ⭐️ 8.0/10
14. [美团 OWL 模型在 OpenRouter 上泄露会话数据](#item-14) ⭐️ 8.0/10
15. [电磁侧信道攻击以 99%准确率识别手机应用](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TypeScript 7.0 用 Go 重写编译器，速度提升 10 倍](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 9.0/10

微软发布了 TypeScript 7.0，其编译器完全用 Go 重写，在 VS Code（快 11.9 倍）和 Sentry（快 8.9 倍）等主要代码库上实现了 8 到 12 倍的速度提升。 这一巨大的性能提升使 TypeScript 在大型项目中的类型检查时间从分钟级缩短到秒级，显著提高了开发效率，并可能加速其在性能敏感环境中的采用。 该重写仍在进行中，尚未完全达到原始 TypeScript 编译器的功能对等；基于 Go 的编译器已在 GitHub 的暂存仓库中提供。速度提升是在真实代码库上测量的，其中 VS Code 仓库的增益最大（11.9 倍）。

hackernews · DanRosenwasser · 7月8日 16:06 · [社区讨论](https://news.ycombinator.com/item?id=48833715)

**背景**: TypeScript 是 JavaScript 的类型化超集，可编译为普通 JavaScript。其原始编译器（tsc）用 JavaScript/TypeScript 编写，在大型代码库上性能受限。Go 是一种以速度和并发性著称的编译型语言，因此成为重写性能关键型编译器组件的理想选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.devbolt.dev/blog/typescript-7-go-rewrite">TypeScript 7.0: What the Go Rewrite Means for Every Developer</a></li>
<li><a href="https://github.com/microsoft/typescript-go">GitHub - microsoft/typescript-go: Staging repo for ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极，许多人祝贺团队并称赞令人印象深刻的加速数据。一些用户讨论了同时维护两个代码库的难度，而另一些人则表达了对未来用 Rust 重写的期待。少数评论强调了与其他缺乏 TypeScript 类型系统复杂性的语言的对比。

**标签**: `#TypeScript`, `#compiler`, `#performance`, `#programming languages`

---

<a id="item-2"></a>
## [欧盟即将重启私密信息扫描法规](https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/) ⭐️ 9.0/10

欧盟距离恢复第 2021/1232 号法规仅一步之遥，该法规允许服务提供商自愿扫描私密信息以查找儿童性虐待材料（CSAM），并可能最终导致在“聊天控制 2.0”下实施强制性扫描。 此举通过启用客户端扫描威胁到端到端加密（E2EE），可能损害欧洲数十亿用户的隐私，并为全球监控开创先例。 该临时法规最初为电子隐私指令设立了豁免，其恢复被视为迈向“聊天控制 2.0”的垫脚石，后者将强制要求扫描并实质上禁止 E2EE。

hackernews · ggirelli · 7月8日 16:53 · [社区讨论](https://news.ycombinator.com/item?id=48834296)

**背景**: 端到端加密（E2EE）确保只有发送者和预期接收者能读取消息，防止包括服务提供商在内的第三方访问内容。欧盟的“聊天控制”提案旨在打击儿童性虐待材料，但引发了关于隐私和安全的辩论，批评者认为强制性扫描将破坏 E2EE 并导致大规模监控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/">EU now one step away from reviving private message scanning rules</a></li>
<li><a href="https://en.wikipedia.org/wiki/End-to-end_encryption">End-to-end encryption</a></li>
<li><a href="https://closednetwork.io/eu-chat-control-the-fight-to-scan-every-private-message-live-tracker/">EU Chat Control: The Fight to Scan Every Private Message (Live Tracker)</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了强烈反对，用户指出互联网观察基金会等组织在推动客户端扫描中的作用。一些人区分了自愿扫描（聊天控制 1.0）和强制扫描（聊天控制 2.0），而另一些人则质疑通过开源客户端和带外密钥交换绕过此类限制的技术可行性。

**标签**: `#privacy`, `#encryption`, `#EU regulation`, `#surveillance`, `#cybersecurity`

---

<a id="item-3"></a>
## [Bun 从 Zig 重写为 Rust](https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/#atom-everything) ⭐️ 9.0/10

Jarred Sumner 宣布，JavaScript 运行时 Bun 已从 Zig 重写为 Rust，并利用 AI 编码代理自动化了大部分移植工作。重写耗时 11 天，API 令牌成本约 16.5 万美元。 这次重写表明，AI 辅助的大规模重写现在变得可行，挑战了长期以来认为重写风险过高的观念。同时，它凸显了 Rust 在内存安全方面的优势，可能影响未来运行时的开发方向。 新的 Rust 版本 Bun 自 2026 年 6 月 17 日起已在 Claude Code 中上线，Linux 上启动速度提升 10%，用户无明显感知。重写使用了 59 亿未缓存输入令牌和 6.9 亿输出令牌。

rss · Simon Willison · 7月8日 23:57

**背景**: Bun 是一个快速的全能 JavaScript 运行时、包管理器和测试运行器，最初用 Zig 编写。Zig 是一种需要手动内存管理的系统编程语言，而 Rust 通过其所有权模型和借用检查器提供内存安全保证。重写得益于 Bun 庞大的 TypeScript 测试套件，该套件为 AI 代理提供了合规性测试基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Memory_safety">Memory safety - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了复杂情绪：一些人称赞了对 AI 的严谨使用以及 Rust 内存安全的好处，而另一些人则批评了对 Zig 版本的放弃和缺乏 LTS 支持。一位评论者指出，重写的成功对 Zig 不利，因为它修复了内存泄漏并提高了稳定性。

**标签**: `#Bun`, `#Rust`, `#Zig`, `#runtime`, `#rewrite`

---

<a id="item-4"></a>
## [约翰迪尔就维修权诉讼与 FTC 达成和解](https://apnews.com/article/john-deere-right-to-repair-agriculture-equipment-cb7514ffedb95c130a976af661f2bc02) ⭐️ 8.0/10

约翰迪尔已就联邦贸易委员会的诉讼达成和解，同意向农民和独立维修店提供与其授权经销商相同的诊断和维修工具。 该和解为农业领域的维修权运动树立了法律先例，可能影响汽车和电子等其他行业的类似政策。 迪尔必须向五个州共同支付 100 万美元的反垄断执法费用，并接受 10 年的严格合规监督，但批评者指出罚款相对于其利润微不足道。

hackernews · djoldman · 7月8日 23:37 · [社区讨论](https://news.ycombinator.com/item?id=48838876)

**背景**: 维修权运动倡导消费者自行维护和修理产品的能力，反对制造商对零件、工具和软件的限制。约翰迪尔长期以来限制诊断软件和维修手册的获取，迫使农民依赖授权经销商进行维修。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apnews.com/article/john-deere-right-to-repair-agriculture-equipment-cb7514ffedb95c130a976af661f2bc02">John Deere owners will get the right to repair their own equipment under a new FTC settlement</a></li>
<li><a href="https://www.usatoday.com/story/money/agriculture/2026/07/08/john-deere-right-to-repair-lawsuit-settled/90850880007/">John Deere settles federal lawsuit over right-to-repair dispute</a></li>
<li><a href="https://pirg.org/resources/john-deere-and-right-to-repair-over-the-years/">John Deere and Right to Repair over the years</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍欢迎这一和解，但批评罚款金额过小，有用户指出这仅占迪尔利润的一小部分。其他人希望这一先例能扩展到现代汽车，同时有人强调路易斯·罗斯曼等活动家在推动维修权方面的作用。

**标签**: `#right-to-repair`, `#FTC`, `#agriculture`, `#consumer rights`, `#regulation`

---

<a id="item-5"></a>
## [OpenAI 探讨提升编程评估信号质量](https://openai.com/index/separating-signal-from-noise-coding-evaluations/) ⭐️ 8.0/10

OpenAI 发布了一篇关于编程评估挑战的分析文章，涉及基准污染和作弊问题，并提出了提升信号质量的方法。 这很重要，因为可靠的编程基准对于衡量 AI 辅助软件开发的进展至关重要；解决污染和作弊问题有助于确保报告的性能反映真实能力。 该分析可能涵盖测试集泄露到训练数据以及对抗性提交等问题，并建议采用人工检查和随机测试等技术来检测作弊。

hackernews · sk4rekr0w · 7月8日 21:03 · [社区讨论](https://news.ycombinator.com/item?id=48837396)

**背景**: 基准污染是指评估数据无意中出现在训练集中，导致分数虚高。编程基准中的作弊行为包括修改超时、硬件配置或奖励黑客攻击。这些问题削弱了 AI 编程评估的有效性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deeplearning.ai/the-batch/the-problem-with-benchmark-contamination-in-ai/">The Problem with Benchmark Contamination in AI</a></li>
<li><a href="https://arxiv.org/abs/2406.04244">[2406.04244] Benchmark Data Contamination of Large Language Models: A Survey</a></li>
<li><a href="https://arxiv.org/abs/2606.07379">[2606.07379] Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 Terminal Bench 2 上存在大量虚假结果，并呼吁基准测试同时衡量效率和智能，例如在固定 API 预算下模型能完成多少任务。一些人认为有缺陷的基准是不可避免的，社区应该向前看。

**标签**: `#AI benchmarks`, `#coding evaluations`, `#OpenAI`, `#machine learning`, `#software engineering`

---

<a id="item-6"></a>
## [Mistral 发布 Robostral Navigate，实现无地图导航](https://mistral.ai/news/robostral-navigate/) ⭐️ 8.0/10

Mistral AI 发布了 Robostral Navigate，这是一个 80 亿参数的机器人导航模型，仅使用单个 RGB 摄像头即可让机器人遵循自然语言指令，在 R2R-CE 基准测试中取得了最先进的结果。 该模型代表了向无地图导航迈出的重要一步，可能解决“绑架机器人”问题，使机器人无需预先构建地图即可在陌生环境中导航，从而加速工业自动化和业余机器人领域的应用。 该模型完全在模拟环境中训练，结合了基于指向的导航和强化学习以实现持续改进。该模型未公开开放，限制了业余爱好者的实验。

hackernews · ottomengis · 7月8日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=48832212)

**背景**: 传统机器人导航通常依赖预先构建的环境地图，这既昂贵，又会在机器人被移动后无法定位（即“绑架机器人”问题）。基于视觉和语言模型的无地图导航旨在克服这一难题，让机器人仅通过视觉输入就能理解自然语言指令并导航。Mistral 的模型仅使用单个 RGB 摄像头，比需要专用传感器的系统更易普及。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mistral.ai/news/robostral-navigate/">Robostral Navigate: single-camera AI navigation | Mistral AI</a></li>
<li><a href="https://x.com/MistralAI/status/2074856309438980145">Mistral AI on X: "Announcing Robostral Navigate, our first model for embodied navigation: an 8B robotics navigation model that guides robots to autonomously perform tasks specified with natural language. Single RGB camera. State-of-the-art on R2R-CE. https://t.co/UlmUsXNxhX" / X</a></li>
<li><a href="https://cryptobriefing.com/mistral-robostral-navigate-robotics-model/">Mistral AI unveils Robostral Navigate, an 8B robotics model that could reshape industrial automation investing</a></li>

</ul>
</details>

**社区讨论**: 评论者对无地图导航能力表示兴奋，有人希望将其集成到 OpenClaw 等业余项目中。但也有评论者担心模型未公开开放，且博客文章缺乏足够的技术细节。

**标签**: `#robotics`, `#AI`, `#navigation`, `#Mistral`, `#deep learning`

---

<a id="item-7"></a>
## [xAI 发布基于 Cursor 数据的 Grok 4.5](https://x.ai/news/grok-4-5) ⭐️ 8.0/10

xAI 发布了 Grok 4.5，这是一款成本高效的模型，在基准测试中与 Opus 4.7 相媲美，该模型使用数万亿个 Cursor 用户交互数据令牌进行训练。 Grok 4.5 以更低的价格（每百万令牌 $2/$6）实现强劲性能，可能颠覆 AI 模型市场，但社区对其政治偏见和伦理问题的怀疑可能阻碍企业采用。 Grok 4.5 基于 1.5 万亿参数的 V9 基础模型，并使用了 Cursor 数据进行补充训练，目前正在 SpaceX 和 Tesla 进行私有测试。其推理效率比 Opus 高 4 倍，定价为每百万令牌 $2/$6。

hackernews · BoumTAC · 7月8日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=48835111)

**背景**: Grok 是 Elon Musk 的 AI 公司 xAI 开发的一系列大型语言模型。Cursor 是一款 AI 驱动的代码编辑器，在隐私模式关闭时会收集用户交互数据用于模型训练。使用来自 Cursor 的真实世界编码数据被视为提升模型在实际任务中能力的关键优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.ai/news/grok-4-5">Introducing Grok 4.5 | SpaceXAI</a></li>
<li><a href="https://x.com/elonmusk/status/2071184354756477041">Elon Musk on X: "Grok 4.5, based on our 1.5T V9 foundation model, with Cursor data added in supplemental training, is now in private beta at SpaceX & Tesla. Early evals show performance close to, perhaps exceeding Opus. RL is continuing to significantly improve the model, and the Grok Build" / X</a></li>
<li><a href="https://www.axios.com/2026/07/08/spacexai-grok-new-model">Scoop: SpaceXAI launches new model, Grok 4.5</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了复杂的情绪：一些用户称赞该模型的成本效率和基准性能，而另一些用户则对政治偏见和伦理问题表示担忧，质疑 xAI 模型在商业用途中的可信度。

**标签**: `#AI`, `#LLM`, `#xAI`, `#Grok`, `#benchmarks`

---

<a id="item-8"></a>
## [OpenAI 推出 GPT-Live 实时语音模式](https://openai.com/index/introducing-gpt-live/) ⭐️ 8.0/10

OpenAI 推出了 GPT-Live，这是一种用于 ChatGPT 的全双工语音模式，支持实时、自然的对话，并能在后台将复杂任务委托给 GPT-5.5。 这标志着 AI 助手的重大进步，消除了以往语音模式的延迟和轮流说话限制，让用户能够进行长时间、高效的对话，同时利用最新的前沿模型处理繁重任务。 GPT-Live 基于全双工架构构建，可以同时听和说，并能用“嗯”等短语表示关注，或在需要时保持安静。该功能正在向 Go、Plus、Pro 和免费用户推出。

hackernews · logickkk1 · 7月8日 17:03 · [社区讨论](https://news.ycombinator.com/item?id=48834405)

**背景**: 之前的 ChatGPT 语音模式是半双工的，需要用户说完后 AI 才能回应，导致对话不自然。GPT-5.5 于 2026 年 4 月发布，是 OpenAI 最强大的模型，擅长编码、研究和工具使用。GPT-Live 弥合了自然语音界面与前沿模型能力之间的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-live/">Introducing GPT‑Live - OpenAI</a></li>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT-5.5 | OpenAI</a></li>
<li><a href="https://venturebeat.com/technology/openai-launches-gpt-live-a-full-duplex-voice-upgrade-that-lets-chatgpt-talk-more-like-a-person">OpenAI launches GPT-Live, a full-duplex voice upgrade that ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一些用户称赞自然的对话流程和委托给 GPT-5.5 的能力，而另一些人则担心 AI 取代人际关系。有用户报告了一个有趣的 bug，即模型会在不适当的时刻打断并大笑。一些用户还抱怨语音模式缺乏工具/连接器支持。

**标签**: `#AI`, `#OpenAI`, `#voice assistant`, `#GPT-5.5`, `#real-time`

---

<a id="item-9"></a>
## [Cloudflare Meerkat：首个生产级异步共识协议](https://blog.cloudflare.com/meerkat-introduction/) ⭐️ 8.0/10

Cloudflare 推出了基于 QuePaxa 的全球分布式共识协议 Meerkat，这是首个不依赖超时的异步共识算法的生产级实现。 这标志着分布式系统的重要进展，首次在生产环境中提供无领导异步共识，有望在传统协议（如 Paxos 和 Raft）难以应对的恶劣网络条件下提升鲁棒性。 Meerkat 基于 QuePaxa，使用随机化异步共识和 hedging 而非超时来保证活性。但每次读操作都需要全局共识，与支持本地读取的系统相比可能增加读延迟。

hackernews · bobnamob · 7月8日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=48831565)

**背景**: 传统共识协议如 Paxos 和 Raft 是部分同步的，依赖超时来保证活性，这使得它们容易受到网络延迟和领导者抖动的影响。像 QuePaxa 这样的异步共识协议完全避免超时，即使在不可预测的延迟下也能保证进展，但历史上效率太低，无法用于生产环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bford.info/pub/os/quepaxa/quepaxa.pdf">QuePaxa: Escaping the Tyranny of Timeouts in Consensus Pasindu Tennage* EPFL</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3600006.3613150">QuePaxa: Escaping the tyranny of timeouts in consensus | Proceedings of the 29th Symposium on Operating Systems Principles</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 Meerkat 是首个生产级异步共识算法实现，具有真正的创新性。一些人担心每次读取都需要全局共识会导致读延迟增加，而另一些人则认为在领导者协议失效的复杂网络中它很有价值。

**标签**: `#distributed systems`, `#consensus`, `#asynchronous`, `#Cloudflare`, `#QuePaxa`

---

<a id="item-10"></a>
## [LingBot-Video：开源稀疏 MoE 视频扩散 Transformer](https://www.reddit.com/r/MachineLearning/comments/1ur0bxq/lingbotvideo_sparsemoe_video_diffusion/) ⭐️ 8.0/10

LingBot-Video 是一个 13B 参数的稀疏混合专家视频扩散 Transformer，仅激活 1.4B 参数，现已开源，包含权重、代码和 Diffusers/SGLang 堆栈。它采用六种奖励的强化学习后训练，其中包括由视觉语言模型评分的物理合理性奖励，并具备动作条件世界模型模式，用于预测机器人 rollout。 这项工作通过将稀疏 MoE 效率与强化学习后训练相结合，推动了开源视频生成的边界，并明确将模型定位为用于动作规划的世界模型。它引发了关于使用 VLM 作为物理评判者以及视频生成器与世界模型之间区别的关键问题，这对机器人学和具身 AI 研究至关重要。 该模型采用单流扩散 Transformer，使用 DeepSeek-V3 风格的稀疏 MoE（128 个专家，top-8 路由）。它在 RBench 上取得平均最高分，但在其自身评估中通用文本到视频任务上排名第二，并且尽管以世界模型为框架，但未提供闭环机器人结果。

reddit · r/MachineLearning · /u/Savings-Display5123 · 7月8日 17:58

**背景**: 稀疏混合专家（MoE）架构通过每个 token 仅激活部分参数，在不成比例增加计算量的情况下扩展模型容量。DeepSeek-V3 在大型语言模型中推广了这种方法。视频扩散 Transformer 通过迭代去噪潜在表示来生成视频。古德哈特定律警告说，当一个指标成为目标时，它就不再是一个好的衡量标准；使用 VLM 来评判物理合理性存在奖励黑客攻击的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://machinelearningmastery.com/mixture-of-experts-architecture-in-transformer-models/">Mixture of Experts Architecture in Transformer Models</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://arxiv.org/abs/2412.19437">[2412.19437] DeepSeek-V3 Technical Report - arXiv.org Images DeepSeek-V3: Open Sparse MoE Model - api.emergentmind.com GitHub - RushilJ2603/DeepSeek-V3-Sparse-MoE-Architecture ... Training Pipeline | deepseek-ai/DeepSeek-V3 | DeepWiki DeepSeek V3: Architecture, Benchmarks & Legacy Status</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区对使用 VLM 作为物理评判者表示怀疑，引用了古德哈特定律以及缺乏闭环机器人验证。一些人赞赏开源贡献和稀疏 MoE 设计，但许多人质疑该模型在没有物理交互结果的情况下是否真正符合世界模型的资格。

**标签**: `#video diffusion`, `#sparse MoE`, `#world model`, `#reinforcement learning`, `#open-source`

---

<a id="item-11"></a>
## [阿里下令员工 7 月 10 日前卸载 Claude](https://t.me/zaihuapd/42424) ⭐️ 8.0/10

阿里巴巴内部下令所有员工卸载 Anthropic 产品，包括 Claude 模型（Sonnet、Opus、Fable）和 Claude Code，禁令于 7 月 10 日生效。此前 Anthropic 指控阿里在 4 月 22 日至 6 月 5 日期间使用约 2.5 万个虚假账号与 Claude 交互超过 2800 万次。 这标志着企业政策的重大转变，凸显了中美 AI 公司在模型安全和知识产权方面的紧张关系加剧。这可能影响中国科技公司获取前沿 AI 模型的方式，并可能导致全行业更严格的使用政策。 阿里巴巴此前曾报销员工使用 Claude、GPT、Gemini 等外部模型的费用。此次禁令涵盖所有 Anthropic 产品，包括 Sonnet、Opus、Fable 模型和 Claude Code 代理工具。Anthropic 在指控后收紧了风控策略。

telegram · zaihuapd · 7月8日 06:09

**背景**: Claude 是 Anthropic 开发的一系列大语言模型，包括针对不同任务优化的 Sonnet、Opus 和 Fable 等变体。Claude Code 是一种代理式编码工具，可以读取代码库、编辑文件和运行命令。模型蒸馏是指利用大型模型的输出来训练小型模型，未经授权进行可能侵犯知识产权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forbes.com/sites/jonmarkman/2026/06/26/anthropic-says-alibaba-used-25000-fake-accounts-to-distill-claude/">Anthropic Says Alibaba Used 25,000 Fake Accounts To Distill ...</a></li>
<li><a href="https://www.explainx.ai/blog/anthropic-alibaba-claude-distillation-25000-fake-accounts-2026">Anthropic vs Alibaba — 25K Fake Claude Accounts, Distillation ...</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#AI`, `#Alibaba`, `#Claude`, `#Anthropic`, `#corporate policy`

---

<a id="item-12"></a>
## [华为 5G 旗舰重返海外，峰值速率突破 1100 Mbps](https://finance.sina.com.cn/tech/roll/2026-07-08/doc-inihapna8035781.shtml) ⭐️ 8.0/10

华为 Pura 90 Pro Max 国际版原生支持 5G 网络，海外实测峰值下载速率突破 1100 Mbps，标志着华为 5G 旗舰在遭受美国制裁七年后正式重返海外市场。 这标志着华为在制裁下成功实现 5G 技术突破，可能通过提供苹果和三星的竞争替代品，重塑全球高端智能手机市场格局。 该设备运行 HarmonyOS 6.0.0.125，并搭载华为 5A 通信技术——5A 并非新的网络制式，而是代表 5A 级优质网络体验，可实现更快接入和更低时延。

telegram · zaihuapd · 7月8日 12:17

**背景**: 自 2019 年起，美国制裁阻止华为在全球销售 5G 手机。2023 年 Mate 60 系列突破技术封锁，后续 HarmonyOS 6.0.0.125 等软件更新实现了 5G 能力。5A 技术于 2025 年底推出，是华为先进通信特性的营销术语，不同于 5G-A 或 5.5G。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/901/311.htm">华为官网详解“5A”先进通信技术：不等同于 5G-A / 5.5G，不涉及额外资...</a></li>
<li><a href="https://consumer.huawei.com/cn/support/content/zh-cn16081318/">华为5A相关问题汇总 | 华为官网 - HUAWEI</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1995465853668443610">2个多GB的鸿蒙6.0.0.125升级包已到位,有什么亮点？值得冲吗</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#5G`, `#smartphone`, `#technology`, `#telecommunications`

---

<a id="item-13"></a>
## [安卓远程 Root 漏洞链曝光](https://www.coolapk.com/feed/72700258?s=ZGQ2MTVlZjYxMDYyNTM3ZzZhNGUzOThjega1640) ⭐️ 8.0/10

Nebula Security 披露了一个名为 IonStack 的远程 Root 漏洞链，该漏洞链结合了 Firefox 浏览器漏洞和一个潜伏 15 年的 Linux 内核漏洞（CVE-2026-43499，GhostLock），可在所有 Android 17 及更早版本上实现一键完全控制设备。 这是首个针对 Android 17 的公开 Root 漏洞链，表明即使是最新更新的设备也可能因点击一个恶意链接而被攻破，对全球数十亿安卓用户构成严重威胁。 该漏洞链利用 Firefox 151.0.2 及更早版本中的远程代码执行漏洞获取初始访问权限，然后通过 GhostLock 内核漏洞提升至 Root 权限；概念验证代码已发布在 GitHub 上，但完整漏洞细节暂未公开。

telegram · zaihuapd · 7月8日 13:01

**背景**: 安卓设备依赖分层安全模型，Linux 内核是其基础。远程 Root 漏洞可以绕过所有安全层，使攻击者获得完全控制权。GhostLock 漏洞（CVE-2026-43499）是内核 futex 子系统中的一个释放后使用漏洞，自 2011 年以来一直存在。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cyberpress.org/ionstack-attack-full-control-android/">IonStack Attack Lets Hackers Gain Full Control of Android ...</a></li>
<li><a href="https://cybersecuritynews.com/android-17-root-1-click/">First-Ever 1- Click Android 17 Exploit Allows Attackers to ...</a></li>
<li><a href="https://threat-modeling.com/cve-2026-43499-ghostlock-linux-kernel-root-container-escape/">CVE-2026-43499 “GhostLock”: 15-Year-Old Linux Kernel Flaw ...</a></li>

</ul>
</details>

**标签**: `#Android`, `#security`, `#vulnerability`, `#root exploit`, `#Linux kernel`

---

<a id="item-14"></a>
## [美团 OWL 模型在 OpenRouter 上泄露会话数据](https://github.com/gumusserv/ProducerBenchV2/blob/83cad6007ef3fe8df33386e8f43738fe62337e16/parsed_source_data/data/) ⭐️ 8.0/10

据报道，美团在 OpenRouter 上的 OWL（LongCat）免费测试模型发生了会话数据泄露，包含数据的 GitHub 仓库现已设为私有。该泄露于 2026 年 7 月 7 日被 Discord 机器人令牌扫描器发现。 此事件凸显了在公共大模型中使用敏感数据的安全风险，因为会话日志可能成为新的敏感资产。它削弱了用户信任，并强调了在 AI 服务中需要更严格的数据处理政策。 泄露的数据曾托管在一个 GitHub 仓库中，该仓库在设为私有之前是公开可访问的。一个 Discord 机器人令牌扫描器检测到暴露的令牌并触发了重置，表明 API 密钥或凭据可能已被泄露。

telegram · zaihuapd · 7月8日 13:35

**背景**: 美团 LongCat-2.0 是一个 1.6 万亿参数的 MoE 模型，采用 MIT 许可，并在国产芯片上训练。OpenRouter 是一个提供统一 API 访问数百个大模型的平台。此前 Google 和 DeepSeek 等公司的事件也警告过，用户对话数据可能被用于模型改进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>
<li><a href="https://top.gg/bot/842154960397008896">Add Token Scanner Discord Bot | The #1 Discord Bot and ...</a></li>

</ul>
</details>

**社区讨论**: 社区对此泄露表示担忧，小红书用户分享截图并警告他人不要在公共模型中输入敏感信息。一些人指出其他提供商也存在类似风险，并呼吁提高透明度。

**标签**: `#data leak`, `#LLM security`, `#privacy`, `#Meituan`, `#OpenRouter`

---

<a id="item-15"></a>
## [电磁侧信道攻击以 99%准确率识别手机应用](https://www.scmp.com/news/china/science/article/3359688/chinese-researchers-find-peephole-any-smartphone-its-leaked-radio-signal) ⭐️ 8.0/10

中国研究人员开发出一种非接触式取证技术，通过分析手机泄漏的低频电磁信号来识别正在使用的应用及操作，在 iPhone 15 Pro、小米 15 Pro 和 OPPO Reno 13 等设备上准确率高达 99.07%。 该技术即使在设备离线、飞行模式、加密或锁定状态下也能工作，无需访问设备系统或存储数据，因此构成重大的隐私和安全威胁。它可能被用于监控或取证调查，引发对移动设备安全的担忧。 该技术针对应用运行时处理器和内存发出的低频电磁辐射（低于 1 MHz），使用深度学习模型对信号进行分类。在三款智能手机上的测试显示，对抖音、微信视频通话、百度地图、短信、浏览器、相机和云存储等应用的识别准确率在 88.7%到 99.07%之间。

telegram · zaihuapd · 7月8日 16:05

**背景**: 电磁侧信道攻击利用电子设备无意中发出的电磁辐射来提取敏感信息。与需要物理接触或电源分析的传统侧信道攻击不同，这种非接触式方法可以远程进行，因此对移动安全尤其危险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Electromagnetic_attack">Electromagnetic attack - Wikipedia</a></li>
<li><a href="https://www.allaboutcircuits.com/technical-articles/em-side-channel-attacks-on-cryptography/">EM Side-Channel Attacks on Cryptography - Technical Articles</a></li>

</ul>
</details>

**标签**: `#security`, `#privacy`, `#mobile forensics`, `#electromagnetic side-channel`, `#research`

---