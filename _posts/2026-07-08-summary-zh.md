---
layout: default
title: "Horizon Summary: 2026-07-08 (ZH)"
date: 2026-07-08
lang: zh
---

> 从 42 条内容中筛选出 15 条重要资讯。

---

1. [MIRA：用于多人火箭联盟的 50 亿参数世界模型](#item-1) ⭐️ 9.0/10
2. [Anthropic 发布 Claude Sonnet 5，代理能力更强](#item-2) ⭐️ 9.0/10
3. [Januscape：潜伏 16 年的 KVM 虚拟机逃逸漏洞影响 Intel 和 AMD](#item-3) ⭐️ 9.0/10
4. [中国拟限制顶尖 AI 模型出口](#item-4) ⭐️ 9.0/10
5. [Kokoro：CPU 友好、高质量的开源 TTS](#item-5) ⭐️ 8.0/10
6. [欧盟聊天控制提案威胁加密通信](#item-6) ⭐️ 8.0/10
7. [微软裁掉 id Software 的 id Tech 引擎团队](#item-7) ⭐️ 8.0/10
8. [sqlite-utils 4.0 引入数据库模式迁移](#item-8) ⭐️ 8.0/10
9. [可微分光线追踪用于无线电传播建模的博士论文](#item-9) ⭐️ 8.0/10
10. [Mozilla CTO Raffi Krikorian 关于开源 AI 报告的 AMA](#item-10) ⭐️ 8.0/10
11. [将微调限制在可信 LoRA 子空间内](#item-11) ⭐️ 8.0/10
12. [中国拟五年投入 2 万亿元建设全国算力网络](#item-12) ⭐️ 8.0/10
13. [new-api 修复计费漏洞：超大参数导致负数扣费](#item-13) ⭐️ 8.0/10
14. [英伟达 Blackwell 晶圆美国制造，封装仍需台湾](#item-14) ⭐️ 8.0/10
15. [DeepSeek 自研 AI 芯片以减少对英伟达和华为的依赖](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [MIRA：用于多人火箭联盟的 50 亿参数世界模型](https://www.reddit.com/r/MachineLearning/comments/1upofuw/mira_multiplayer_interactive_world_models_trained/) ⭐️ 9.0/10

MIRA 是一个在 10000 小时合成火箭联盟数据上训练的 50 亿参数世界模型，能在单个 NVIDIA B200 GPU 上以每秒 20 帧的速度实现 4 人交互式模拟。团队发布了可玩的在线演示、技术报告以及一个 1000 小时的 4 人游戏数据集。 这是迈向多人游戏大规模交互式世界模型的开创性一步，可能改变游戏 AI、模拟和强化学习领域。代码、数据集和模型的开源发布降低了研究人员和开发者在此基础上继续工作的门槛。 该模型在单个 B200 GPU 上为 4 名玩家以 20 fps 运行，B200 基于 NVIDIA Blackwell 架构，拥有 2080 亿个晶体管。训练数据完全合成，使用火箭联盟游戏引擎生成，发布的数据集包含 1000 小时的 4 人游戏数据。

reddit · r/MachineLearning · /u/MasterScrat · 7月7日 07:59

**背景**: AI 中的世界模型是一种机器学习系统，它构建环境的内部表示，并预测环境如何响应动作而变化。合成数据是人工生成而非从真实事件中收集的数据，当真实数据稀缺或昂贵时，常用于训练 AI 模型。B200 GPU 是 NVIDIA 为 AI 工作负载设计的高端加速器，相比前代产品性能显著提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/dgx-b200/">DGX B200: The Foundation for Your AI Factory | NVIDIA</a></li>
<li><a href="https://medium.com/cdrin-cctt/the-power-of-synthetic-data-using-game-engines-to-improve-ai-67e872bab997">The Power of Synthetic Data: Using Game Engines to Improve AI | by CDRIN | CDRIN-CCTT | Medium</a></li>

</ul>
</details>

**标签**: `#world models`, `#reinforcement learning`, `#multiplayer games`, `#large-scale models`, `#open source`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Sonnet 5，代理能力更强](https://t.me/zaihuapd/42404) ⭐️ 9.0/10

Anthropic 发布了 Claude Sonnet 5，称其是迄今代理能力最强的 Sonnet 模型，可自主规划并使用浏览器和终端等工具。该模型即日起面向所有套餐开放，并成为 Free 和 Pro 用户的默认模型。 Claude Sonnet 5 以更低的价格提供了接近 Opus 的性能，使先进的代理 AI 更易于开发者和企业使用。其增强的推理、工具使用和编码能力可能加速 AI 代理在实际工作流程中的采用。 Claude Sonnet 5 在推理、工具使用、编码和知识任务上优于 Sonnet 4.6，性能接近 Opus 4.8。定价为每百万输入 token 2 美元，输出 token 限时优惠截至 2026 年 8 月 31 日。

telegram · zaihuapd · 7月7日 09:02

**背景**: Anthropic 的 Claude 模型系列包括 Opus（能力最强）、Sonnet（平衡型）和 Haiku（快速/廉价）。Sonnet 模型适用于广泛的任务，包括代理工作流，即模型自主规划并使用外部工具执行多步骤操作。新的 Sonnet 5 旨在以低于顶级 Opus 模型的成本提供更强的代理能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-sonnet-5">Introducing Claude Sonnet 5 \ Anthropic</a></li>
<li><a href="https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/">Anthropic launches Claude Sonnet 5 as a cheaper way to run ...</a></li>
<li><a href="https://www.anthropic.com/claude/opus">Claude Opus \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#LLM`, `#Agent`

---

<a id="item-3"></a>
## [Januscape：潜伏 16 年的 KVM 虚拟机逃逸漏洞影响 Intel 和 AMD](https://github.com/V4bel/Januscape) ⭐️ 9.0/10

安全研究员 Hyunwoo Kim 公开了 Januscape（CVE-2026-53359），这是首个同时在 Intel 和 AMD 平台上触发的 KVM/x86 虚拟机逃逸漏洞，其 PoC 可导致宿主机内核崩溃。 该漏洞破坏了云环境中的多租户隔离，恶意客户机可危害宿主机，影响 2010 年至 2026 年的 Linux 内核，并可能实现完全控制宿主机。 该漏洞是 KVM shadow MMU 中的 use-after-free 缺陷，客户机可破坏宿主机的 shadow 页表。另有一个未公开的漏洞利用据称可实现完全宿主机代码执行。

telegram · zaihuapd · 7月7日 10:14

**背景**: KVM（基于内核的虚拟机）是 Linux 的 hypervisor，在旧硬件上使用 shadow MMU 管理客户机内存。Use-after-free 漏洞发生在程序访问已释放的内存时，可能允许攻击者执行任意代码。该漏洞潜伏了 16 年未被发现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html">16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on ...</a></li>
<li><a href="https://www.csoonline.com/article/4194085/16-year-old-kvm-flaw-allows-attackers-to-escape-vms-and-take-over-linux-servers.html">16-year-old KVM flaw allows attackers to escape VMs and take ...</a></li>
<li><a href="https://threat-modeling.com/cve-2026-53359-januscape-linux-kvm-vm-escape-intel-amd/">CVE-2026-53359 'Januscape': 16-Year-Old Linux KVM Guest-to ...</a></li>

</ul>
</details>

**社区讨论**: Telegram 讨论强调了该漏洞的严重性和长期潜伏，一些人担心云服务商的响应速度，并呼吁立即打补丁。

**标签**: `#KVM`, `#VM escape`, `#CVE`, `#Linux kernel`, `#security`

---

<a id="item-4"></a>
## [中国拟限制顶尖 AI 模型出口](https://www.reuters.com/world/beijing-is-looking-curbing-overseas-access-chinas-top-ai-models-sources-say-2026-07-07/) ⭐️ 9.0/10

中国商务部已召集阿里巴巴、字节跳动和智谱 AI 等企业开会，讨论限制最先进的国产 AI 模型（包括尚未发布的模型）向海外提供访问，并可能将 AI 技术泄露列为国家安全犯罪。 这项政策可能通过限制国际社会获取中国尖端 AI 模型，深刻重塑全球 AI 格局，影响主要科技公司，并可能加速全球 AI 生态系统的碎片化。 限制措施仍在商讨中，可能仅适用于未来发布的新模型，最终是否落地尚不确定。会议还讨论了限制境外资本投资国内 AI 初创企业。

telegram · zaihuapd · 7月7日 11:42

**背景**: 中国已快速发展出先进的 AI 模型，如阿里巴巴的通义千问系列、字节跳动的豆包以及智谱 AI 的 GLM 系列。对 AI 模型的出口管制是全球增长趋势，美国已对先进 AI 芯片和模型权重实施限制。此举反映了类似的国家安全和技术领导力担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zglg.work/ai/news/zh/2026-07-07-china-holds-talks-with-alibaba-and-bytedance-on-restricting-ai-model-exports">中国就限制 AI 模型出口与阿里巴巴和字节跳动展开磋商 | zglg.work</a></li>
<li><a href="https://zh.wikipedia.org/wiki/智谱">智谱 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#China`, `#export control`, `#national security`, `#tech policy`

---

<a id="item-5"></a>
## [Kokoro：CPU 友好、高质量的开源 TTS](https://ariya.io/2026/03/local-cpu-friendly-high-quality-tts-text-to-speech-with-kokoro/) ⭐️ 8.0/10

Kokoro 是一个拥有 8200 万个参数的开源文本转语音模型，无需 GPU 即可在 CPU 上高效运行，生成高质量语音。它支持手动添加 IPA 发音指南以纠正同形异义词错误。 这使得没有强大 GPU 的用户也能使用高质量 TTS，为无障碍工具、内容消费等场景普及语音合成。IPA 支持解决了 TTS 准确性的常见痛点。 Kokoro-82M 通过 mlx-audio 针对 Apple Silicon 进行了优化，也能在其他 CPU 上运行。社区成员已基于 Kokoro 构建了 Chrome 扩展和基于 RSS 的播客工作流。

hackernews · speckx · 7月7日 18:24 · [社区讨论](https://news.ycombinator.com/item?id=48821576)

**背景**: 大多数高质量 TTS 模型需要 GPU 进行实时推理，限制了硬件配置较低的用户。Kokoro 是一个开源模型，仅用 8200 万个参数就达到了有竞争力的质量，轻量级到足以在 CPU 上推理。IPA（国际音标）允许精确控制发音，对同形异义词或外来词很有用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Kokoro_TTS">Kokoro TTS</a></li>
<li><a href="https://github.com/nazdridoy/kokoro-tts">GitHub - nazdridoy/kokoro-tts: A CLI text-to-speech tool ...</a></li>

</ul>
</details>

**社区讨论**: 社区反馈非常积极，用户称赞 Kokoro 的质量和 CPU 效率。一些人指出其在单词语音和同形异义词处理上的局限，但 IPA 覆盖功能缓解了这一问题。用户已将 Kokoro 集成到无障碍产品和播客流程中。

**标签**: `#TTS`, `#machine learning`, `#accessibility`, `#open source`, `#CPU`

---

<a id="item-6"></a>
## [欧盟聊天控制提案威胁加密通信](https://fightchatcontrol.eu/chat-control-overview) ⭐️ 8.0/10

欧盟的聊天控制 1.0 和 2.0 提案将强制要求对加密消息进行客户端扫描以检测儿童性虐待材料，这实际上破坏了端到端加密。 如果通过，这些提案将破坏所有欧盟公民的数字隐私和安全，为大规模监控树立危险先例，并削弱全球加密技术。 聊天控制 1.0 允许在 ePrivacy 指令的临时豁免下进行自愿扫描，而聊天控制 2.0 将强制要求扫描。两者都依赖客户端扫描，即在用户设备上加密前或解密后扫描内容。

hackernews · gasull · 7月7日 14:23 · [社区讨论](https://news.ycombinator.com/item?id=48818311)

**背景**: 客户端扫描（CSS）是一种在用户设备上对消息内容在加密前或解密后进行分析的技术，绕过了端到端加密。欧盟的聊天控制提案旨在打击儿童性虐待材料（CSAM），但被隐私倡导者和安全专家广泛批评，认为其制造了漏洞并助长大规模监控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Regulation_to_Prevent_and_Combat_Child_Sexual_Abuse">Chat Control - Wikipedia</a></li>
<li><a href="https://www.eff.org/deeplinks/2026/04/eu-parliament-blocks-mass-scanning-our-chats-whats-next">EU Parliament Blocks Mass-Scanning of Our Chats—What's Next? | Electronic Frontier Foundation</a></li>
<li><a href="https://www.patrick-breyer.de/en/posts/chat-control/">Chat Control: The EU's CSAM scanner proposal</a></li>

</ul>
</details>

**社区讨论**: 评论者表示强烈反对，认为这些提案是广泛的监控权力扩张，而非针对性措施。有人指出，即使自愿扫描（聊天控制 1.0）在法律到期后仍在继续，还有人强调了对婴儿照片等无辜内容的风险。

**标签**: `#privacy`, `#encryption`, `#EU legislation`, `#surveillance`, `#cybersecurity`

---

<a id="item-7"></a>
## [微软裁掉 id Software 的 id Tech 引擎团队](https://gamefromscratch.com/microsoft-fire-idtech-team-at-id-software/) ⭐️ 8.0/10

微软裁掉了 id Software 的整个 id Tech 引擎开发团队，该团队曾开发出用于《毁灭战士：永恒》的 id Tech 7 等标志性引擎。此举实际上终止了 id Software 的内部引擎开发，将重心转向外部引擎如 Unreal Engine 5。 此次裁员标志着游戏引擎市场的重大整合，随着更多工作室放弃自研引擎转向 Unreal Engine 5，竞争和创新将减少。这也引发了对微软收购工作室长期战略的担忧，可能导致游戏开发同质化，并失去独特的技术专长。 id Tech 团队负责开发和维护 id Software 的自研游戏引擎，该引擎曾用于《毁灭战士》、《雷神之锤》和《狂怒》等作品。此次裁员是微软 Xbox 部门更广泛重组的一部分，波及多个工作室。

hackernews · bauc · 7月7日 15:33 · [社区讨论](https://news.ycombinator.com/item?id=48819244)

**背景**: id Software 是一家传奇游戏开发商，由 John Carmack 和 John Romero 于 1991 年创立，以开创第一人称射击游戏和创建 id Tech 引擎系列而闻名。这些引擎曾授权给其他开发者，部分版本已开源。微软于 2021 年收购了 id Software 的母公司 ZeniMax Media。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Id_Tech">id Tech - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Id_Software">id Software - Wikipedia</a></li>
<li><a href="https://www.konvoy.vc/newsletters/the-great-unbundling-of-game-engines">The Great Unbundling of Game Engines - konvoy.vc</a></li>

</ul>
</details>

**社区讨论**: 社区表达了深深的失望和担忧，许多人哀叹 id 引擎专业知识的流失，并警告此举将加强 Epic Games 在游戏引擎领域的垄断地位。一些评论者批评微软的短期削减成本策略，认为这将损害长期创新和工作室文化。

**标签**: `#gaming`, `#game engines`, `#Microsoft`, `#id Software`, `#layoffs`

---

<a id="item-8"></a>
## [sqlite-utils 4.0 引入数据库模式迁移](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything) ⭐️ 8.0/10

sqlite-utils 4.0 于 2026 年 7 月 7 日发布，新增了数据库模式迁移、通过新的 db.atomic() 方法实现的嵌套事务，以及对复合外键的支持。 这一主要版本显著增强了广泛使用的 SQLite Python CLI 和库 sqlite-utils，使开发者无需外部工具即可更轻松地管理模式变更和复杂事务。 迁移通过使用 sqlite-utils Python 库在 Python 文件中定义，利用强大的 table.transform() 方法，该方法实现了 SQLite 推荐的创建新表、复制数据并重命名的模式。该版本还包含升级指南中详述的破坏性变更。

rss · Simon Willison · 7月7日 19:32

**背景**: 模式迁移允许开发者对数据库模式应用一系列变更，同时跟踪哪些已应用。SQLite 的 ALTER TABLE 功能有限，因此像 sqlite-utils 这样的工具提供了增强功能。嵌套事务允许在更大事务内进行原子操作，复合外键则允许引用父表中的多个列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sqlite-utils.datasette.io/en/latest/migrations.html">Database migrations - sqlite-utils</a></li>
<li><a href="https://simonwillison.net/2026/Jul/7/sqlite-utils-4/">sqlite-utils 4.0, now with database schema migrations</a></li>
<li><a href="https://sqlite.org/foreignkeys.html">SQLite Foreign Key Support</a></li>

</ul>
</details>

**标签**: `#sqlite`, `#python`, `#database`, `#migrations`, `#open source`

---

<a id="item-9"></a>
## [可微分光线追踪用于无线电传播建模的博士论文](https://www.reddit.com/r/MachineLearning/comments/1upvkp5/phd_thesis_on_differentiable_ray_tracing_for/) ⭐️ 8.0/10

一篇题为“可微分光线追踪用于无线电传播建模”的博士论文已发布，它将可微分光线追踪与 JAX 等自动微分框架相结合，通过物理环境计算精确梯度，用于无线通信。 这项工作弥合了无线电传播模拟与机器学习之间的鸿沟，支持基于梯度的优化和直接 ML 训练以解决逆问题，这对下一代无线设计（如 6G）至关重要。 论文以自包含教科书形式组织，分为三部分：物理基础、算法核心（包括 GPU 加速路径追踪和不连续性平滑技术）以及实际应用（如信道建模和材料校准）。作者提供开放获取和开源库（如 DiffeRT）。

reddit · r/MachineLearning · /u/jeertmans · 7月7日 13:45

**背景**: 可微分光线追踪通过使渲染管线支持自动微分来扩展传统光线追踪，从而能够计算关于场景参数的梯度。JAX 是一个高性能数值计算库，支持自动微分和 GPU/TPU 加速，常用于机器学习。无线电传播建模模拟无线电波在环境中的传播，对无线网络规划至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://people.csail.mit.edu/tzumao/diffrt/">Differentiable Monte Carlo Ray Tracing through Edge Sampling</a></li>
<li><a href="https://research.nvidia.com/publication/2024-10_learning-radio-environments-differentiable-ray-tracing">Learning Radio Environments by Differentiable Ray Tracing | Research</a></li>
<li><a href="https://github.com/jax-ml/jax">GitHub - jax-ml/jax: Composable transformations of Python+NumPy programs: differentiate, vectorize, JIT to GPU/TPU, and more · GitHub</a></li>

</ul>
</details>

**标签**: `#differentiable ray tracing`, `#radio propagation`, `#automatic differentiation`, `#JAX`, `#wireless communications`

---

<a id="item-10"></a>
## [Mozilla CTO Raffi Krikorian 关于开源 AI 报告的 AMA](https://www.reddit.com/r/MachineLearning/comments/1upxdvc/raffi_krikorian_cto_mozilla_ama_on_the_state_of/) ⭐️ 8.0/10

Mozilla CTO Raffi Krikorian 将于 2025 年 7 月 14 日举办 AMA，讨论首份《开源 AI 现状》报告，涵盖实际成本、企业采用、中国影响力和开发者信任等话题。 此次 AMA 提供了一个难得的机会，可以直接从主要开源倡导者那里了解开源 AI 的实际挑战和机遇，这对于企业采用和开发者信任日益重要。 该报告基于对 950 多名开发者的调查，关注生产现实而非常见叙事。关键主题包括免费模型的“隐性成本”、“代理框架”层以及中国开源模型的影响。

reddit · r/MachineLearning · /u/raffikrikorian · 7月7日 14:51

**背景**: 开源 AI 指源代码公开、允许修改和再分发的 AI 模型和工具。以 Firefox 浏览器闻名的 Mozilla 一直倡导开放和可信的 AI。“代理框架”是包裹 AI 模型以实现类似代理行为的基础设施层，例如管理上下文和外部交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mozilla.org/en-US/foundation/annualreport/2024/article/evolving-together-redefining-mozilla-in-the-ai-era/">Evolving Together: Redefining Mozilla in the AI Era</a></li>
<li><a href="https://www.langchain.com/blog/the-anatomy-of-an-agent-harness">The Anatomy of an Agent Harness</a></li>
<li><a href="https://www.cio.com/article/4140634/the-hidden-tax-on-every-ai-initiative-and-how-to-stop-paying-it.html">The hidden tax on every AI initiative (and how to stop paying ...</a></li>

</ul>
</details>

**标签**: `#open source`, `#AI`, `#Mozilla`, `#enterprise`, `#developer trust`

---

<a id="item-11"></a>
## [将微调限制在可信 LoRA 子空间内](https://www.reddit.com/r/MachineLearning/comments/1uq68li/what_if_a_model_could_only_learn_what_trusted/) ⭐️ 8.0/10

一篇新论文提出将微调更新限制在从可信 LoRA 适配器学习到的子空间内，即使存在中毒数据也能阻止恶意更新。 这种几何防御通过使某些恶意方向在几何上不可达，填补了微调安全性的关键空白，为从用户数据中自适应部署模型提供了实用保障。 该方法在 196 个公开 LoRA 适配器上进行了测试，包括专门设计用于绕过防御的自适应攻击，结果显示攻击成功率大幅下降，同时保留了适配器池覆盖任务上的有用适应能力。

reddit · r/MachineLearning · /u/Bright_Warning_8406 · 7月7日 20:00

**背景**: LoRA（低秩适应）是一种参数高效的微调技术，仅更新少量低秩矩阵，降低计算成本。微调中毒攻击通过操纵训练数据向模型中注入隐藏行为（后门）。现有防御侧重于检测中毒数据或降低其影响，而这项工作通过限制可能更新的空间采取了不同方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/deep-learning/low-rank-adaptation-lora/">Low Rank Adaptation (LoRA) - GeeksforGeeks</a></li>
<li><a href="https://arxiv.org/abs/2402.12168">[2402.12168] Defending Against Weight-Poisoning Backdoor ... Defending Against Weight-Poisoning Backdoor Attacks for ... Data Poisoning Attacks of Fine-Tuning for Large Language ... LLM Poisoning: Detection, Defense, and Prevention Strategies I Poisoned an AI Model to Sell You Software: Fine-Tuning ... GitHub - agw2005/pbp-reproduced: Reproduction of the novel ...</a></li>
<li><a href="https://arxiv.org/pdf/2512.11760">SpectralKrum: A Spectral-Geometric Defense Against Byzantine ...</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#security`, `#LoRA`, `#fine-tuning`, `#adversarial robustness`

---

<a id="item-12"></a>
## [中国拟五年投入 2 万亿元建设全国算力网络](https://t.me/zaihuapd/42399) ⭐️ 8.0/10

中国计划未来五年投入约 2 万亿元（2950 亿美元），建设全国互联数据中心网络，由国有电信企业运营主要设施。该计划优先采用华为等本土供应商的 AI 芯片，目标国产化率至少八成，以减少对英伟达、AMD 等美企的依赖。 这一巨额投资可能重塑全球 AI 硬件供应链和云计算格局，彰显中国追求技术自主的决心。同时，它标志着向整合全国算力资源为统一网络的战略转变，使企业和公共部门更易获得高性能计算。 该计划是北京“六网”基础设施计划的关键一环，旨在整合分散的区域算力资源。中国电信、联通等运营商已推出“token”套餐，将算力像移动数据一样打包销售，为大规模 AI 应用铺路。

telegram · zaihuapd · 7月7日 04:45

**背景**: 中国的“六网”基础设施计划包括算力、能源、交通等网络，以支持数字经济和 AI 发展。全国算力网络又称“东数西算”工程，旨在连接各地数据中心。基于 token 的算力定价是中国电信运营商近期的创新，允许用户按需购买 AI 计算资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gov.cn/lianbo/202605/content_7070126.htm">统筹建设、动态推进“六张网” - 中国政府网</a></li>
<li><a href="https://www.nda.gov.cn/sjj/swdt/mtsy/0616/20260616182702649345771_pc.html">六网织就新未来丨支撑人工智能等高质量发展 算力网开启万亿级投资周期...</a></li>
<li><a href="https://news.qq.com/rain/a/20260518A05V3X00">Token套餐全面上线!三大运营商悉数入局，算力进入“按Token收费”时代_...</a></li>

</ul>
</details>

**标签**: `#China`, `#AI infrastructure`, `#computing network`, `#semiconductors`, `#cloud computing`

---

<a id="item-13"></a>
## [new-api 修复计费漏洞：超大参数导致负数扣费](https://github.com/QuantumNous/new-api/commit/d0bd8aa) ⭐️ 8.0/10

QuantumNous/new-api 项目修复了一个关键计费漏洞：用户可控参数过大时可能触发整数溢出，导致配额计算产生负值，从而出现“反向充值”的效果。 该漏洞可能被攻击者利用来免费获取额度甚至增加余额，对使用 new-api 的服务提供商构成严重财务风险。此次修复加强了输入验证并防止整数溢出，保障了计费系统的完整性。 修复方案对配额相关参数增加了上限校验，并采用饱和运算逻辑，避免结果在转换为整数时回绕为负数。后续提交还补齐了其他入口的边界检查，防止攻击者通过超大数字影响预扣费或结算逻辑。

telegram · zaihuapd · 7月7日 07:26

**背景**: 整数溢出是指算术运算结果超出整数类型的表示范围，导致数值回绕（例如，很大的正数变成负数）。在计费系统中，此类缺陷可被利用来操纵扣费。new-api 是一个开源 API 网关，负责 AI 服务的配额和计费，因此这一修复对生产部署至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.comparitech.com/blog/information-security/integer-overflow-attack/">What is an Integer Overflow Attack (with Examples)? - Comparitech CWE - CWE-190: Integer Overflow or Wraparound (4.20) Understanding & Exploiting Integer Overflow Vulnerabilities ... Vulnerability: Integer Overflow and Underflow - OWASP Foundation NVD - CVE-2025-54091 What is Integer Overflow? Exploits & Impact - blogs.jsmon.sh NVD - CVE-2026-3536</a></li>
<li><a href="https://deepwiki.com/QuantumNous/new-api/2.6-quota-and-billing-system">Quota & Billing System | QuantumNous/new-api | DeepWiki</a></li>
<li><a href="https://deepwiki.com/QuantumNous/new-api/9.2-quota-calculation-and-consumption">Quota Calculation and Consumption | QuantumNous/new-api ...</a></li>

</ul>
</details>

**标签**: `#security`, `#billing`, `#vulnerability`, `#open-source`, `#API`

---

<a id="item-14"></a>
## [英伟达 Blackwell 晶圆美国制造，封装仍需台湾](https://www.tomshardware.com/tech-industry/nvidia-and-intel-tout-chips-built-in-america-but-every-arizona-made-blackwell-die-is-still-packaged-in-taiwan) ⭐️ 8.0/10

英伟达 Blackwell 晶圆已在台积电亚利桑那州 Fab 21 采用定制 4NP 制程量产，但仍需运往台湾完成先进的 CoWoS-L 封装和 HBM 集成。 这凸显了美国半导体供应链的关键瓶颈：尽管晶圆制造已本土化，但先进封装产能预计要到 2028-2029 年才能完备，短期内仍依赖台湾。 晶圆需从亚利桑那州运往约 7000 英里外的台湾进行切割、堆叠和 CoWoS-L 封装。此外，美国目前没有 HBM 生产和封装设施，而这对 AI 加速器至关重要。

telegram · zaihuapd · 7月7日 09:47

**背景**: CoWoS（Chip-on-Wafer-on-Substrate）是一种先进的 2.5D/3D 封装技术，通过硅中介层连接逻辑芯片和 HBM 堆叠。台积电 4NP 制程是为英伟达定制的 5nm 级节点。美国正通过 Amkor、台积电和 SK 海力士建设封装产能，但完整的供应链独立仍需数年。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.csdn.net/u013669912/article/details/143434272">CoWoS 封装 | CoWoS-S / CoWoS-R / CoWoS-L-CSDN博客</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/688119389">RTX 50升级台积电4NP工艺：但其实还是5nm - 知乎</a></li>
<li><a href="https://baike.baidu.com/item/HBM封装/68105001">HBM封装_百度百科</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#supply chain`, `#Nvidia`, `#advanced packaging`, `#geopolitics`

---

<a id="item-15"></a>
## [DeepSeek 自研 AI 芯片以减少对英伟达和华为的依赖](https://www.reuters.com/world/china/chinas-deepseek-developing-its-own-ai-chip-sources-say-2026-07-07/) ⭐️ 8.0/10

DeepSeek 正在开发专注于推理的 AI 芯片，旨在减少对英伟达和华为芯片的依赖。该项目始于约一年前，目前仍处于早期阶段，公司正在招募芯片设计工程师，并与代工厂和存储供应商接洽。 此举标志着 AI 硬件格局的战略性转变，DeepSeek 试图规避限制先进芯片获取的美国出口管制。如果成功，将减少中国对外国芯片制造商的依赖，并加速国内 AI 芯片开发的趋势。 该芯片专为推理阶段设计，即训练好的模型为用户生成回答的环节，而非模型训练。DeepSeek 此前依赖英伟达 H800 和华为昇腾芯片，创始人梁文锋在 2024 年一次罕见采访中承认芯片管制是公司面临的挑战。

telegram · zaihuapd · 7月7日 11:08

**背景**: 自 2018 年以来，美国出口管制限制了中国获取先进半导体及相关技术，影响了像 DeepSeek 这样依赖高性能 AI 芯片的公司。随着 AI 应用普及，推理计算是 AI 需求增长最快的部分，因此专用推理芯片具有战略意义。DeepSeek 此举反映了中国企业将 AI 加速器预算转向国内供应商的更广泛趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/world/china/chinas-deepseek-developing-its-own-ai-chip-sources-say-2026-07-07/">EXCLUSIVE: China's DeepSeek developing its own AI chip ...</a></li>
<li><a href="https://www.usnews.com/news/top-news/articles/2026-07-07/exclusive-chinas-deepseek-developing-its-own-ai-chip-sources-say">Exclusive-China's DeepSeek Developing Its Own AI Chip ...</a></li>
<li><a href="https://www.cryptopolitan.com/deepseek-plans-its-own-inference-chip/">DeepSeek plans its own inference chip, a threat to Nvidia and ...</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#DeepSeek`, `#semiconductors`, `#export controls`, `#inference`

---