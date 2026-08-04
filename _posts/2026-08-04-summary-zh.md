---
layout: default
title: "Horizon Summary: 2026-08-04 (ZH)"
date: 2026-08-04
lang: zh
---

> 从 84 条内容中筛选出 14 条重要资讯。

---

1. [DeepSeek V4 Flash 在单块 AMD MI300X 上运行，速度超 150 tok/s](#item-1) ⭐️ 8.0/10
2. [Keyv 及相关 npm 包在 Shai-Hulud 供应链攻击中遭入侵](#item-2) ⭐️ 8.0/10
3. [Xbox 宕机导致光盘游戏无法游玩，数字所有权争议再起](#item-3) ⭐️ 8.0/10
4. [AI 自我改进的支架工程](#item-4) ⭐️ 8.0/10
5. [MiniMax-H3 移植到 MLX，支持 Apple Silicon](#item-5) ⭐️ 8.0/10
6. [LLM 让开源自由变得切实可行](#item-6) ⭐️ 8.0/10
7. [AI 开始大幅削减客服岗位](#item-7) ⭐️ 8.0/10
8. [Kimi K3 架构：压缩记忆、跨深度注意力与潜在路由](#item-8) ⭐️ 8.0/10
9. [呼吁对无可复现代码的机器学习论文进行桌面拒稿](#item-9) ⭐️ 8.0/10
10. [探索性建模：生成模型的第三个预训练轴](#item-10) ⭐️ 8.0/10
11. [华为提出“韬定律”以替代摩尔定律](#item-11) ⭐️ 8.0/10
12. [Cloudflare 弃用第三方安全工具，用每月 58 美元的 AI 处理漏洞](#item-12) ⭐️ 8.0/10
13. [谷歌为 Anthropic 搭建 2000 亿美元华尔街融资机器](#item-13) ⭐️ 8.0/10
14. [中国首部 L3/L4 自动驾驶强制性国标获批，2027 年实施](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek V4 Flash 在单块 AMD MI300X 上运行，速度超 150 tok/s](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐️ 8.0/10

一份技术指南展示了 DeepSeek V4 Flash 在单块 AMD MI300X 加速器上运行，速度超过每秒 150 个 token。该配置将上下文窗口从原来的 1M 缩减至 256k。 这一演示表明，在单块 AMD GPU 上也能实现高性能的 LLM 推理，可能降低硬件成本并扩大先进模型的可及性。它还凸显了上下文长度与硬件需求之间的实际权衡，这对部署决策具有重要意义。 DeepSeek V4 Flash 是一个混合专家模型，总参数 284B，激活参数 13B，原生量化至 MXFP4。MI300X 配备 192GB HBM3 内存，足以在缩减的上下文窗口下运行该模型。

hackernews · zhoutong · 8月4日 10:00 · [社区讨论](https://news.ycombinator.com/item?id=49166386)

**背景**: DeepSeek V4 Flash 是 DeepSeek V4 系列中面向效率优化的版本，设计用于快速推理，支持 1M token 的上下文窗口。AMD MI300X 是一款数据中心 GPU，配备 192GB HBM3 内存，常用于大规模 AI 工作负载。量化技术可减小模型体积和内存占用，从而支持在单个加速器上部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash">DeepSeek V 4 Flash 0423 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://www.techpowerup.com/gpu-specs/radeon-instinct-mi300x.c4179">AMD Radeon Instinct MI300X Specs | TechPowerUp GPU Database</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，MI300X 通常以 8 卡系统而非单卡形式销售，并建议使用 MI350P 作为 PCIe 替代方案，其内存为 144GB。还有人提到了 DwarfStar 等替代方法，并引用了双 MI300X 配置的相关工作，同时有人称赞了为提升速度而缩减上下文窗口这一实际权衡。

**标签**: `#DeepSeek`, `#AMD MI300X`, `#LLM inference`, `#quantization`, `#hardware`

---

<a id="item-2"></a>
## [Keyv 及相关 npm 包在 Shai-Hulud 供应链攻击中遭入侵](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) ⭐️ 8.0/10

供应链攻击已入侵 Keyv npm 包及多个相关包，这是持续的 Shai-Hulud 攻击活动的一部分。该攻击利用 npm 依赖生态系统分发恶意代码。 此次攻击凸显了 npm 生态系统在供应链攻击面前的持续脆弱性，影响了依赖这些包的无数开发者和项目。它强调了加强安全措施和社区意识的紧迫性。 Shai-Hulud 活动此前已入侵数百个 npm 包并窃取开发者凭证。最新事件涉及 Keyv 及其相关包，这些包广泛用于 Node.js 应用中的键值存储。

hackernews · cimi_ · 8月4日 11:01 · [社区讨论](https://news.ycombinator.com/item?id=49166874)

**背景**: 对 npm 包的供应链攻击已成为重大安全隐患，攻击者通过入侵流行包将恶意代码注入下游应用。Shai-Hulud 攻击是近期多个活动之一，此前还有 s1ngularity 攻击和 Josh Junon 维护者被入侵事件。这些攻击常利用安装前或安装后的钩子（hooks）在包安装时执行恶意脚本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack">Shai - Hulud npm Supply Chain Attack | Wiz Blog</a></li>
<li><a href="https://www.securityweek.com/shai-hulud-supply-chain-attack-worm-used-to-steal-secrets-180-npm-packages-hit/">Shai - Hulud Supply Chain Attack : Worm Used to... - SecurityWeek</a></li>
<li><a href="https://www.npmjs.com/package/keyv">keyv - npm</a></li>

</ul>
</details>

**社区讨论**: 社区成员对脆弱的依赖系统表示不满，有人呼吁取消安装前和安装后的钩子。还有人建议实际缓解措施，如设置包的最低发布年龄，同时有人质疑为何在如此大规模的犯罪下无人被捕。

**标签**: `#security`, `#supply chain`, `#npm`, `#open source`, `#dependency management`

---

<a id="item-3"></a>
## [Xbox 宕机导致光盘游戏无法游玩，数字所有权争议再起](https://birchtree.me/blog/xbox-goes-down-you-cant-play-games-you-own-on-disc/) ⭐️ 8.0/10

最近一次持续约 15-16 小时的 Xbox 宕机导致玩家无法启动跨多个主机世代的实体光盘游戏。此次宕机是由后端授权服务故障引起的，而非光盘不可读，暴露了现代主机对 DRM 的依赖。 这一事件凸显了数字所有权的脆弱性，表明即使是实体媒体也可能因服务器端故障而无法使用。它加剧了关于游戏领域真正所有权和离线访问必要性的消费者权利讨论，可能影响未来的法规和行业实践。 此次宕机影响了三代 Xbox 主机，微软将其归因于错误的授权检查。这表明 Xbox 上的光盘游戏仍需在线许可证验证，与实体媒体保证离线游玩的假设相矛盾。

hackernews · surprisetalk · 8月4日 12:01 · [社区讨论](https://news.ycombinator.com/item?id=49167448)

**背景**: 现代游戏主机越来越依赖在线 DRM（数字版权管理）来验证游戏所有权，即使是实体光盘也是如此。这一趋势引发了对所有权侵蚀的担忧，因为如果服务器关闭或出现故障，游戏可能无法游玩。'Stop Killing Games'运动及各国政府的回应凸显了消费者对此类做法日益增长的抵制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech.yahoo.com/gaming/articles/xbox-outage-locked-players-discs-154143617.html">Xbox Outage Locked Players Out of Discs They Own</a></li>
<li><a href="https://windows.gadgethacks.com/news/xbox-outage-blocked-disc-games-why-physical-media-isnt-offline-access/">Xbox Outage Blocked Disc Games: Why Physical Media Isn't ...</a></li>
<li><a href="https://aliteq.com/xbox-outage-physical-discs-stopped-working-explained-2026">Xbox Outage Stopped Physical Discs From Working: What ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了沮丧和怀旧之情，如用户 cautiouscat 感叹永久所有权的丧失，并将其与其他行业实体媒体的衰落相比较。paxys 认为核心问题是所有权权利，而非实体与数字之争，并列出了消费者应享有的具体权利。一些用户还指出，像 PS3 这样的老主机提供了更好的离线与局域网支持，暗示消费者友好功能出现了倒退。

**标签**: `#digital ownership`, `#DRM`, `#gaming`, `#cloud dependency`, `#consumer rights`

---

<a id="item-4"></a>
## [AI 自我改进的支架工程](https://lilianweng.github.io/posts/2026-07-04-harness/) ⭐️ 8.0/10

Lilian Weng 发表了一篇关于自我改进的支架工程的博客文章，讨论了如何优化 AI 代理框架，并引发了关于适应度函数和训练范式的社区讨论。 这篇文章强调了从改进模型权重转向优化周围支架的转变，这可能导致更可靠和高效的 AI 代理。对于寻求在模型能力之外提升代理性能的 AI 工程师和研究人员来说，这具有重要意义。 这篇文章探讨了实际实施挑战，例如定义质量和为代码库构建通用适应度函数。它还涉及新颖的方法，如爬山实验和在 Codex 等工具中使用 AI 支架工程技能。

hackernews · tosh · 8月4日 06:17 · [社区讨论](https://news.ycombinator.com/item?id=49164896)

**背景**: 支架工程是一门专注于构建 AI 系统周围的基础设施、验证循环、护栏和编排系统的学科，将焦点从模型智能转移到系统可靠性。适应度函数源自进化算法，用于衡量候选解决方案与期望结果的接近程度，并正被应用于优化 AI 编码助手和代理支架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://harness-engineering.ai/?trk=article-ssr-frontend-pulse_little-text-block">Home | Harness Engineering</a></li>
<li><a href="https://medium.com/@ravikumar135/harness-engineering-the-new-discipline-powering-reliable-ai-agents-da5a077099a2">Harness Engineering : The New Discipline Powering Reliable AI Agents</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fitness_function">Fitness function - Wikipedia</a></li>
<li><a href="https://www.thinkcode.se/blog/2026/06/24/fitness-functions-for-an-ai-coding-assistant">Fitness Functions for an AI Coding Assistant</a></li>

</ul>
</details>

**社区讨论**: 社区评论表现出热情和实际担忧的混合。一些用户讨论在组织层面实施适应度函数，而另一些用户则分享个人关于支架优化的实验。还有对“Torment Nexus”的幽默引用，以及关于训练权重是否已达到顶峰的辩论，一些人主张为提示和代码建立新的训练范式。

**标签**: `#AI engineering`, `#harness optimization`, `#LLM agents`, `#software engineering`, `#self-improvement`

---

<a id="item-5"></a>
## [MiniMax-H3 移植到 MLX，支持 Apple Silicon](https://simonwillison.net/2026/Aug/4/minimax-h3-mlx/#atom-everything) ⭐️ 8.0/10

一个新的 Python 包 PipeNetwork/minimax-h3-mlx 将 MiniMax 的全模态 MiniMax-H3 模型移植到 MLX，使其能够在 Apple Silicon 上本地运行。Simon Willison 在 M5 Max MacBook Pro 上成功运行了该模型，并根据文本提示生成了带音频的 15 秒视频片段。 这一移植使得开发者能够在 Apple 硬件上使用最先进的全模态生成模型，降低了本地实验和部署的门槛。它凸显了利用 Apple 统一内存架构进行高效 AI 推理的 MLX 移植生态系统的不断壮大。 该模型需要下载约 115 GB 的模型文件，在 M5 Max 上生成视频耗时不到 45 分钟。由于提示词未包含音频指导，生成的音频被描述为“类似语音的垃圾”，但提示指南提供了获得更好结果的说明。

rss · Simon Willison · 8月4日 19:10

**背景**: MLX 是一个针对 Apple silicon 统一内存架构优化的开源数组框架，提供类似 NumPy 的 API，用于高效的机器学习。MiniMax-H3 是一个通用的全模态生成模型，可接受文本、图像、音频和视频输入，并生成最长 15 秒、最高 2K 分辨率、带原生立体声的视频片段。全模态系统使用编码器将多种输入类型转换为通用表示，从而能够跨模态进行统一推理和生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://machinelearning.apple.com/research/exploring-llms-mlx-m5">Exploring LLMs with MLX and the Neural Accelerators in the M5 GPU - Apple Machine Learning Research</a></li>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between Tasks and Modalities - MiniMax Research | MiniMax</a></li>
<li><a href="https://fal.ai/minimax-h3">MiniMax H3 - Open-Weights General-Purpose Multimodal Video Model | fal</a></li>

</ul>
</details>

**标签**: `#MLX`, `#MiniMax-H3`, `#multimodal`, `#Apple Silicon`, `#generative model`

---

<a id="item-6"></a>
## [LLM 让开源自由变得切实可行](https://simonwillison.net/2026/Aug/3/devtools-must-be-open-source-exedev/#atom-everything) ⭐️ 8.0/10

Simon Willison 认为，LLM 降低了阅读和修改开源代码的门槛，使开源最初的承诺更易实现。他现在经常使用 Claude 和 Codex 等 AI 工具来克隆、构建和理解以前因摩擦而回避的代码库。 这一转变可能重振开源参与，因为更多开发者能够为他们使用的项目做出贡献。这也标志着 AI 辅助开发融入日常工作的更广泛趋势，可能提升代码质量和创新。 Willison 提到使用常规 Claude 聊天提示“从 GitHub 克隆 x/y 并告诉我 Z 如何工作”，并使用 Codex 或 Claude Code 来检出和构建项目，视为“零时间投入挑战”。他指出自己尚未习惯性地修改软件，但看到了去年不存在的路径。

rss · Simon Willison · 8月3日 15:30

**背景**: 开源软件赋予用户检查和修改源代码的自由，但实践中，所需的时间和精力往往连专家程序员也望而却步。LLM 通过自动化代码理解和构建过程来减少这种摩擦，使开发者更容易接触不熟悉的代码库。这与“氛围编程”概念一致，即 AI 根据自然语言提示生成代码，也与 AI 辅助编程的更广泛趋势相符。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding - Wikipedia</a></li>
<li><a href="https://ias-research.com/research/research-journal/reading-and-understanding-open-source-code-a-comprehensive-guide">Reading and Understanding Open Source Code: A Comprehensive Guide</a></li>

</ul>
</details>

**社区讨论**: 内容中引用的 Hacker News 讨论可能包含多种观点，但由于未提供评论，无法总结情绪。然而，高分表明社区认为这一见解有价值且及时。

**标签**: `#open source`, `#LLMs`, `#developer tools`, `#AI-assisted development`

---

<a id="item-7"></a>
## [AI 开始大幅削减客服岗位](https://www.solidot.org/story?sid=84994) ⭐️ 8.0/10

包括微软、Uber 和澳大利亚联邦银行在内的大型公司正用 AI 驱动的聊天机器人和电话系统取代客服岗位，导致大量裁员。微软将客服团队从约 5 万人缩减至 4 万人，Uber 削减了 10%的客服岗位。 这一趋势标志着客服就业的范式转变，到 2030 年可能影响全球数百万个工作岗位，尤其是在依赖外包的菲律宾和印度等国。它凸显了生成式 AI 对劳动力日益增长的影响，并引发了对岗位流失的担忧。 联邦银行裁减了数百名客服岗位，每年节省数千万美元。微软销售和服务运营负责人 Judson Althoff 表示，AI 每年为公司节省约 7.5 亿美元的客服成本，但复杂问题仍需人工支持。凯悦酒店去年裁掉了美洲地区三成的内部客服。

rss · Solidot 奇客 · 8月3日 14:22

**背景**: 客服呼叫中心传统上在美国、印度和菲律宾等国雇佣了数百万员工。随着 AI 技术的进步以及高管面临采用新技术的压力，企业日益使用生成式 AI 工具处理客户互动，导致美国客服就业人数下降，并预计外包目的地也将出现减少。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/zh-cn/dynamics-365/products/customer-service">使用生成式 AI 的 Customer Service | Microsoft Dynamics 365</a></li>
<li><a href="https://m.aitntnews.com/newDetail.html?newId=7368">万字长文讲透生成式AI 如何赋能客服</a></li>

</ul>
</details>

**标签**: `#AI`, `#customer service`, `#automation`, `#employment`, `#industry trend`

---

<a id="item-8"></a>
## [Kimi K3 架构：压缩记忆、跨深度注意力与潜在路由](https://newsletter.semianalysis.com/p/kimi-k3-the-manos-the-mythos-the) ⭐️ 8.0/10

SemiAnalysis 发表了对 Kimi K3 架构的深度技术分析，重点介绍了其在压缩记忆、跨深度注意力和潜在专家路由方面的创新。这些机制旨在提升推理效率和性能。 该分析为前沿 AI 架构提供了宝贵见解，可能影响未来大语言模型的设计。理解这些技术对于从事高效大规模模型推理的研究人员和工程师至关重要。 Kimi K3 是一个拥有 2.8 万亿参数、100 万 token 上下文窗口的模型，基于 Kimi Delta Attention 和 Attention Residuals 构建。该架构结合了压缩记忆、跨深度注意力和潜在专家路由，以优化推理性能。

rss · Semianalysis · 8月3日 19:42

**背景**: 大型语言模型在高效扩展上下文长度、深度和宽度方面面临挑战。跨深度注意力等技术允许查询关注早期层的键，改善信息流动。专家混合（MoE）路由，尤其是潜在专家路由，在保持能力的同时减少参数，从而实现更高效的训练和推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.24653">Kimi K3: Open Frontier Intelligence - arXiv.org</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://arxiv.org/pdf/2606.05014">Depth-Attention: Cross-Layer Value Mixing for Language Models</a></li>

</ul>
</details>

**标签**: `#AI architecture`, `#LLM inference`, `#memory compression`, `#attention mechanisms`, `#MoE`

---

<a id="item-9"></a>
## [呼吁对无可复现代码的机器学习论文进行桌面拒稿](https://www.reddit.com/r/MachineLearning/comments/1vei12v/its_time_to_desk_reject_papers_that_dont_include/) ⭐️ 8.0/10

一位审稿人报告称，今年为机器学习主要会议审稿的 12 篇论文中，只有 1 篇提供了完整代码，而 5 篇提供部分代码的论文中有 3 篇存在使结果无效的 bug，因此主张对缺乏可复现代码的论文进行桌面拒稿。 这凸显了机器学习研究中系统性的可复现性危机，代码共享稀少且 bug 可能未被发现，损害了科学诚信。改变审稿政策以惩罚缺失代码的做法，可以激励更好的实践并提高研究质量。 审稿人指出，当前的激励结构鼓励隐藏代码，因为发布代码会增加因 bug 而被拒稿的风险。他们建议施加实际惩罚，如桌面拒稿，以强制将代码共享作为标准要求。

reddit · r/MachineLearning · /u/Flaky-Ambition5900 · 8月3日 16:17

**背景**: 在机器学习研究中，可复现性对于验证结果至关重要，但许多论文因缺乏激励或担心审查而省略代码。像 NeurIPS 和 ICML 这样的会议已开始执行如 AI 水印等政策，但代码共享仍不一致。桌面拒稿是编辑在未经完整同行评审的情况下拒绝论文的决定，通常是因为明显违反投稿要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://byteiota.com/icml-desk-rejects-497-papers-ai-review-trap-explained/">ICML Desk Rejects 497 Papers : AI Review Trap Explained | byteiota</a></li>
<li><a href="https://data-mining.philippe-fournier-viger.com/paper-without-code-non-reproducible-research/">Papers without code (and the problem of non- reproducible research )</a></li>

</ul>
</details>

**标签**: `#reproducibility`, `#machine learning`, `#research practices`, `#peer review`, `#open source`

---

<a id="item-10"></a>
## [探索性建模：生成模型的第三个预训练轴](https://www.reddit.com/r/MachineLearning/comments/1vf6r6f/explorative_modeling_unlocking_a_third/) ⭐️ 8.0/10

Gladstone 等人（2026）的新论文提出了“探索性建模”（XMs），作为除参数和数据之外的第三个预训练轴，并展示了它能够在现有生成模型中实现端到端生成。 这可能通过为扩展生成模型提供新维度，对机器学习领域产生重大影响，有望带来更强大、更高效的模型。它挑战了传统上对参数和数据扩展的关注，开辟了新的研究方向。 论文描述了在预训练期间增加探索的探索性模型（XMs），作为参数和数据的补充轴。该方法据称能实现端到端生成，但提供的资料中尚未给出具体技术细节。

reddit · r/MachineLearning · /u/Benlus · 8月4日 10:42

**背景**: 预训练是机器学习中常见的技术，模型在大规模数据集上训练以学习通用表示，然后可以针对特定任务进行微调。传统上，扩展集中在增加模型参数和训练数据上。这篇论文提出了第三个轴——探索，可能涉及新的训练目标或架构，鼓励模型在学习过程中探索更广泛的可能性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explorative-modeling.github.io/">Explorative Modeling : Unlocking a Third Pretraining Axis and...</a></li>
<li><a href="https://digg.com/tech/mrt8e84i">Paper Frames Exploration as Third Pretraining Axis · Digg</a></li>
<li><a href="https://paperswithcode.co/paper/2607.27372">Explorative Modeling : Unlocking a Third Pretraining Axis and...</a></li>

</ul>
</details>

**标签**: `#pretraining`, `#machine learning`, `#research`, `#generative models`

---

<a id="item-11"></a>
## [华为提出“韬定律”以替代摩尔定律](https://t.me/zaihuapd/42966) ⭐️ 8.0/10

在上海举行的 2026 年 IEEE 国际电路与系统研讨会（ISCAS）上，华为提出了“韬定律”（Tau (τ) Scaling Law），主张以时间（τ）缩微替代几何缩微作为半导体演进的新原则。过去六年，华为已据此设计并量产了 381 款芯片，今年秋季将推出采用逻辑折叠技术的新麒麟手机芯片。 这是中国公司提出的首个新的半导体缩微定律，为摩尔定律逼近物理极限后的发展提供了潜在路径。如果得到验证，它可能重塑全球半导体产业，为传统基于光刻的缩微提供替代方案，并对台积电、英特尔等竞争对手产生影响。 韬定律侧重于降低时间常数，以实现器件、电路、芯片到系统的多层级协同优化。华为预计，到 2031 年，基于该定律的高端芯片晶体管密度可达 1.4 纳米制程同等水平。逻辑折叠作为关键技术，通过垂直堆叠芯片组件来缩短信号传输距离，有望在无需 EUV 光刻的情况下达到台积电第一代 3nm 工艺的性能水平。

telegram · zaihuapd · 8月4日 08:04

**背景**: 摩尔定律预测晶体管密度大约每两年翻一番，几十年来一直推动着半导体行业的发展，但现在正逼近物理极限。传统缩微依赖于晶体管的几何缩小，需要先进的光刻设备。华为的韬定律提出了一种替代方案：时域压缩，即通过降低时间常数（如信号传播延迟）来提升性能，而无需缩小特征尺寸。这种方法利用垂直集成和逻辑折叠来实现性能提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.huawei.com/en/news/2026/5/ieee-iscas-tau-scaling">HUAWEI Presents the Tau (τ) Scaling Law, Enabling ...</a></li>
<li><a href="https://medium.com/newsarticulated/huaweis-tau-τ-scaling-law-explained-how-time-scaling-replaces-moore-s-law-for-breakthrough-eeeb13318a31">HUAWEI’s Tau (τ) Scaling Law Explained: How Time Scaling ...</a></li>
<li><a href="https://www.geeky-gadgets.com/huawei-logic-folding-moores-law/">Huawei Logic Folding : A New Approach to... - Geeky Gadgets</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#Huawei`, `#Moore's Law`, `#chip design`, `#technology`

---

<a id="item-12"></a>
## [Cloudflare 弃用第三方安全工具，用每月 58 美元的 AI 处理漏洞](https://www.theregister.com/security/2026/08/04/cloudflare-has-mostly-ditched-third-party-security-tools-suggests-not-trying-that-at-home/5282600) ⭐️ 8.0/10

Cloudflare 首席安全官 Grant Bourzikas 透露，公司已使用 Anthropic 的 Claude Sonnet 模型自动化处理漏洞赏金报告，每月仅花费 58 美元，而使用 Mythos 等安全专用模型则需每月约 20 万美元。公司还构建了 200 多个自主安全代理，并基本弃用第三方安全工具，改用部分由 AI 辅助编写的自研应用。 这表明利用通用 AI 模型可以大幅降低安全运营成本并提高效率，可能重塑企业对待安全工具的方式。同时，它也凸显了 AI 取代传统软件工具的趋势，以及这对厂商和客户带来的战略影响。 Bourzikas 建议其他公司不要效仿 Cloudflare 的做法，称并非每家银行都该自己开发软件。首席战略官 Stephanie Cohen 将公司裁员 1100 人归因于 AI 驱动的自动化，并透露计划充当 AI 公司与出版商之间的中介，通过微支付实现内容授权。

telegram · zaihuapd · 8月4日 09:24

**背景**: Claude 是 Anthropic 开发的一系列大语言模型，包括 Sonnet 和 Opus 等版本。2026 年，Anthropic 向部分组织发布了安全专用模型 Claude Mythos，随后向公众发布了 Claude Fable。Cloudflare 的做法反映了利用 AI 自动化安全任务的趋势，但也引发了对依赖第三方 AI 模型和就业影响的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Sonnet_4">Claude Sonnet 4</a></li>
<li><a href="https://news.qq.com/rain/a/20260611A000PV00">Mythos模型深度解析：技术跃迁、安全革命与战略博弈</a></li>
<li><a href="https://blog.csdn.net/qq_31142761/article/details/162108207">Claude Mythos 深度拆解：安全专用大模型如何开创“防御性AI“新品类-CS...</a></li>

</ul>
</details>

**标签**: `#AI`, `#security`, `#Cloudflare`, `#vulnerability management`, `#Anthropic`

---

<a id="item-13"></a>
## [谷歌为 Anthropic 搭建 2000 亿美元华尔街融资机器](https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c) ⭐️ 8.0/10

谷歌悄然构建了史上最大规模的基础设施融资架构之一，以向 Anthropic 交付超过 1500 亿美元的 AI 芯片，相关合同总额约 2000 亿美元。这一新颖结构涉及博通、阿波罗、黑石、摩根士丹利及多家加密矿企，由各方分担风险。 这标志着 AI 基础设施融资方式的重大转变，将巨额硬件成本移出资产负债表，实现前所未有的规模。它可能重塑 AI 算力的竞争格局，使 Anthropic 受益，并可能为其他 AI 公司和科技巨头提供范本。 今年 6 月，特殊目的载体 Compute SPV 完成了首批交易，购入约 350 亿美元硬件，约合 1 吉瓦算力和 100 万颗 TPU。该模式借鉴了波音和 GE 的厂商融资玩法，使各方不必将数千亿美元的 AI 硬件计入自家资产负债表。

telegram · zaihuapd · 8月4日 10:52

**背景**: Anthropic 是 Claude 模型系列的开发商，没有信用评级，因此融资结构分散风险：谷歌担保数据中心，博通购买并协助融资芯片，阿波罗和黑石购买硬件后回租给 Anthropic。这种表外融资方式是更广泛趋势的一部分，即通过 SPV 和私人信贷为 AI 基础设施热潮提供资金，类似交易如 Meta 的 3000 亿美元 SPV 融资。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ernestchiang.com/en/posts/2025/off-balance-sheet-ai-how-spvs-are-financing-the-data-center-boom-while-hiding-leverage/">Off-Balance Sheet AI: How SPVs Are Financing the Data Center ...</a></li>
<li><a href="https://finance.biggo.com/news/HvPcsp4BmHHDnbgyVm1I">Google, Broadcom, and Private Equity Giants Forge $35 Billion ...</a></li>
<li><a href="https://tech-insider.org/google-40-billion-anthropic-investment-tpu-compute-2026/">Google's $40B Anthropic Investment: TPU Deal Inside [2026]</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#Google`, `#Anthropic`, `#financing`, `#chips`

---

<a id="item-14"></a>
## [中国首部 L3/L4 自动驾驶强制性国标获批，2027 年实施](https://t.me/zaihuapd/42972) ⭐️ 8.0/10

中国工业和信息化部已完成并报批强制性国家标准《智能网联汽车自动驾驶系统安全要求》（GB 44721—2026），自 6 月 17 日起公示，计划于 2027 年 7 月 1 日实施。该标准引入了 Safety Case 安全档案机制，并对 L3 的人机交接和 L4 的系统自主风险处置提出了具体要求。 这是中国首部针对 L3/L4 自动驾驶的强制性国家标准，标志着监管从“概念松绑”转向“安全硬约束”。它将迫使车企严格论证安全性，可能重塑竞争格局，并加速中国高级别自动驾驶汽车的部署。 该标准适用于 M 类和 N 类车辆中搭载 L3 和 L4 自动驾驶系统的车型。它引入了 Safety Case 机制，要求企业通过“声明—论据—证据”系统性论证安全性，并对 L3 的人机交接和 L4 的系统自主风险处置分别提出了要求。

telegram · zaihuapd · 8月4日 13:06

**背景**: 自动驾驶等级从 L0 到 L5，L3 允许驾驶员在特定条件下脱手，但需要在系统请求时接管；L4 则可在限定场景内无需驾驶员干预运行。Safety Case 是一种用于安全关键行业的结构化论证框架，用于证明系统安全性可接受。中国的新标准旨在为 L3/L4 系统建立统一的安全基线，解决人机交接和系统风险管理的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.globaltimes.cn/page/202608/1367493.shtml">China releases mandatory national standard for autonomous ...</a></li>
<li><a href="https://opengovasia.com/china-sets-national-safety-standard-for-autonomous-driving-systems/">China Sets National Safety Standard for Autonomous Driving ...</a></li>
<li><a href="https://cnevpost.com/2026/08/04/china-sets-safety-baseline-l3-l4-autonomous-driving/">China sets unified safety baseline for L3, L4 autonomous driving</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#regulation`, `#China`, `#safety standard`, `#L3/L4`

---