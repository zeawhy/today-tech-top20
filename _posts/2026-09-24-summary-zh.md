---
layout: default
title: "Horizon Summary: 2026-09-24 (ZH)"
date: 2026-09-24
lang: zh
---

> 从 83 条内容中筛选出 9 条重要资讯。

---

1. [Anthropic 与 OpenAI 一小时内相继发布新前沿模型，引发价格战](#item-1) ⭐️ 9.0/10
2. [OpenAI 为 ChatGPT 语音接入插件并启用 GPT-6 模型](#item-2) ⭐️ 9.0/10
3. [高通为骁龙 X2 系列笔记本芯片带来 Linux 支持](#item-3) ⭐️ 8.0/10
4. [Anthropic 称 Claude 发现类 CRISPR 酶系统](#item-4) ⭐️ 8.0/10
5. [Tailscale 优化用户态 WireGuard 以提升速度](#item-5) ⭐️ 8.0/10
6. [Token 便宜到无需计量：LLM 调用会否比 grep 更便宜？](#item-6) ⭐️ 8.0/10
7. [ClusterMAX 3.0：SemiAnalysis 更新 GPU 云评级标准](#item-7) ⭐️ 8.0/10
8. [Claude Code 云会话正式上线，最高可领 250 美元额度](#item-8) ⭐️ 8.0/10
9. [OpenAI 称苹果 ChatGPT 集成表现不佳，双方合作出现裂痕](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 与 OpenAI 一小时内相继发布新前沿模型，引发价格战](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 9.0/10

2026 年 9 月 22 日，Anthropic 发布了 Claude Opus 5.5，大约一小时后 OpenAI 发布了 GPT-6 Sol 和 GPT-6 Luna。GPT-6 Luna 定价为输入 $0.10/百万 token、输出 $0.50/百万 token，仅为前代 GPT-5.6 Luna 的一半；而 Claude Opus 5.5 在典型工作负载下的运行成本比 Opus 5 低 40%。 两大实验室同时发布新模型并大幅降价，标志着前沿 AI 厂商之间的价格战进一步升级，显著降低了基于最先进模型构建应用的成本。依赖大模型 API 的开发者和企业将是最大受益者，因为能力提升的同时每 token 成本却在下降。 GPT-6 Luna 以 $0.10/$0.50 的定价成为 OpenAI 有史以来最便宜的模型之一，仅弱于能力更差的 GPT-4.1 Nano 和 GPT-5 Nano。GPT-5.6 系列原定于 11 月涨价 25%，这意味着 GPT-6 的价格仅为前代促销价的一半。

rss · Simon Willison · 9月22日 23:46

**背景**: 前沿 AI 模型是 OpenAI、Anthropic、xAI 等实验室提供的最强大语言模型，通常按每百万 token 的输入和输出分别计费。近几个月发布节奏极快——就在前一天，Grok 4.7 和小米的 MiMo v2.6 刚刚亮相——竞争同时推动了能力提升和价格大幅下降。广受关注的 AI 分析师 Simon Willison 一直在密切跟踪这些发布及其定价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5.5 \ Anthropic</a></li>
<li><a href="https://9to5mac.com/2026/09/22/anthropic-upgrades-claude-with-new-opus-5-5-model-details-here/">Anthropic upgrades Claude with new Opus 5.5 model, details here - 9to5Mac</a></li>
<li><a href="https://llm-stats.com/models/grok-4.7">Grok 4 . 7 Benchmarks, Pricing & Context Window</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#OpenAI`, `#Anthropic`, `#pricing`

---

<a id="item-2"></a>
## [OpenAI 为 ChatGPT 语音接入插件并启用 GPT-6 模型](https://x.com/OpenAI/status/2102808325742322002) ⭐️ 9.0/10

OpenAI 宣布 ChatGPT 语音现在可以调用邮箱、日历和 Slack 等插件，并改由全新的 GPT-6 Astra、Sol 和 Luna 模型驱动，新版本于今天在全球推出。用户还可以在网页端和移动端的 ChatGPT Work 中通过语音创建文档、演示、网站和表格，或在浏览器里处理复杂任务。 这标志着 ChatGPT 语音从闲聊工具转变为可在真实办公工具中执行操作的智能代理，可能重塑人们处理邮件、日程和文档创建的方式。同时，这也把 OpenAI 的 GPT-6 系列扩展到更快、更便宜的模型，加剧了与其他 AI 助手及生产力平台的竞争。 GPT-6 Sol 和 Luna 采用了与 GPT-6 Astra 相似的训练方法，将 Astra 在专业工作、事实准确性、编程、计算机操作和一致性方面的进步带到了更快、更实惠的模型中。Work 中的语音功能在网页端和移动端均可使用，如果通话结束时任务仍在运行，它可以在文本模式下继续执行。

telegram · zaihuapd · 9月24日 00:02

**背景**: ChatGPT 语音此前主要聚焦于口语对话，而插件和任务自动化大多局限于文本交互。GPT-6 是 OpenAI 继前几代之后推出的最新模型系列，ChatGPT Work 则是该助手的任务自动化层，用于创建文件和处理多步骤任务。将语音连接到 Gmail、Google 日历和 Slack 等外部应用，使该产品更接近一个完全由语音驱动的 AI 助手。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT‑6 Sol and Luna - OpenAI</a></li>
<li><a href="https://www.digitaltrends.com/computing/chatgpt-voice-can-now-check-your-email-manage-your-calendar-search-slack-and-use-gpt-6/">ChatGPT Voice can now check your email, manage your calendar, search ...</a></li>
<li><a href="https://techcrunch.com/2026/09/23/chatgpt-mobile-app-gets-voice-based-agentic-features/">ChatGPT mobile app gets voice-based agentic features | TechCrunch</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#GPT-6`, `#voice-assistant`, `#plugins`

---

<a id="item-3"></a>
## [高通为骁龙 X2 系列笔记本芯片带来 Linux 支持](https://www.qualcomm.com/news/onq/2026/09/snapdragon-summit-agentic-ai-pcs-linux) ⭐️ 8.0/10

在 2026 年骁龙峰会上，高通宣布其骁龙 X2 系列笔记本处理器将正式支持 Linux，与 Windows 及全新的 Googlebook 平台并列。高通表示正在将 X2 系列的核心驱动（包括 Hexagon NPU 和 Adreno GPU）上游到 Linux 主线，以向开发者和设备厂商开放该平台。 这是 ARM 笔记本生态的一次重要扩展，为 Linux 用户提供了可媲美苹果 M 系列和 x86 笔记本的高性能选择。它可能直接影响开发者和开源爱好者购买 ARM 笔记本的决策，让他们能获得原生的 Linux 体验。 高通特别强调将 Hexagon NPU 和 Adreno GPU 驱动上游到主线，这两者对加速和图形性能至关重要。社区报告还指出，这些芯片现已支持 ARM EL2，从而具备 KVM 虚拟化能力，这与前几代不同；同时 OpenBSD/arm64 支持也已启动，在 HP Elitebook X G2q 上已能在 ACPI 模式下使用 USB、键盘和触控板。

hackernews · aaronday · 9月23日 22:38 · [社区讨论](https://news.ycombinator.com/item?id=49823582)

**背景**: 骁龙 X2 系列是高通第二代面向笔记本的 ARM 处理器家族，接替 2024 年发布的第一代骁龙 X Elite 和 X Plus。上游（upstreaming）指的是将驱动和设备树代码贡献到 Linux 主线内核，使支持随内核本身发布，而不是依赖厂商私有补丁。历史上，ARM 笔记本的 Linux 支持一直较为碎片化，因为厂商往往不提供设备树或上游驱动，导致用户只能依赖 Windows 下的专有驱动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.qualcomm.com/news/onq/2026/09/snapdragon-summit-agentic-ai-pcs-linux">Inside Snapdragon Summit 2026: Agentic AI PCs, Googlebooks and...</a></li>
<li><a href="https://www.gamingonlinux.com/2026/09/qualcomm-announce-snapdragon-x2-series-will-support-linux/">Qualcomm announce Snapdragon X 2 Series will... | GamingOnLinux</a></li>
<li><a href="https://www.theverge.com/news/999664/qualcomm-snapdragon-x2-linux-support-arm">Qualcomm will finally support Linux on Snapdragon X2 chips. | The Verge</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍欢迎这一消息，但强调高通必须为每一款笔记本型号上游设备树支持，因为没有设备树的 ARM 笔记本在 Linux 上几乎无法使用。一些人指出，骁龙 X2 是笔记本形态下最接近苹果 M 系列的竞争对手；还有人提到 OpenBSD 开发者 Tobias Heider 已提交初步的 OpenBSD/arm64 支持，并确认 ARM EL2/KVM 可用。

**标签**: `#Linux`, `#ARM`, `#Qualcomm Snapdragon`, `#Hardware`, `#Open Source`

---

<a id="item-4"></a>
## [Anthropic 称 Claude 发现类 CRISPR 酶系统](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) ⭐️ 8.0/10

Anthropic 宣布其 AI 模型 Claude 在原始 DNA 序列中自主识别出一个带有类 CRISPR 串联重复阵列的新型酶系统，整个过程使用了约 950 个智能体、耗时 21 小时、消耗 2.1 亿个 token，公司科学家仅提供高层方向指导。所有实体实验随后均由人类研究人员在 Anthropic 湾区生物实验室的 BSL-1/2 生物安全条件下完成。 这一声明是 AI 辅助科学发现领域的高调里程碑，表明智能体式大语言模型系统能够比传统依赖文献的工作流程更快地从原始序列数据中找出候选生物结构。它也加剧了一场持续争论：AI 与人类研究者各自应获得多少功劳，以及此类发现能否真正加速生物技术和基因编辑研究。 社区分析更为冷静地认为，这一发现其实是已知的类 retron 逆转录酶出现在此前未描述的基因组排列中，而非全新的酶类别。该工作仅停留在计算层面，而文章“Claude 发现”的表述掩盖了在链接技术报告中才被承认的人类研究者贡献。

hackernews · raahelb · 9月23日 18:06 · [社区讨论](https://news.ycombinator.com/item?id=49820134)

**背景**: CRISPR 是细菌的一种免疫机制，利用重复阵列和 Cas9 等相关蛋白来靶向并切割 DNA，已成为基础性的基因编辑工具。逆转录酶是将 RNA 复制为 DNA 的酶，而 retron 是利用这类酶的细菌遗传元件。Anthropic 的 Claude 是一系列大语言模型，此次声明来自该公司新近成立的生物学研究实验室。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-discovers-novel-enzyme-system">Claude discovers a novel enzyme system \ Anthropic</a></li>
<li><a href="https://mangodeveloper.com/articles/anthropics-ai-lab-found-a-crispr-like-enzyme-system-in-21-hours-but-humans-still-run-the-experiments">Anthropic's AI Lab Found a CRISPR - Like Enzyme System in 21 Hours...</a></li>
<li><a href="https://www.aljazeera.com/economy/2026/9/24/ai-model-claude-discovers-crispr-like-enzyme-system-anthropic-says">AI model Claude discovers CRISPR - like enzyme system ... | Al Jazeera</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分化：一些人赞赏数据科学与领域专业知识融合的新角色，以及通过智能体记录重温发现过程的能力；另一些人则批评“Claude 发现”这种拟人化表述，并指出人类贡献被淡化。一个反复出现的技术反驳是，该结果只是已知逆转录酶处于新的基因组排列中，而且治疗应用的主要瓶颈仍是递送而非核酸酶发现。

**标签**: `#AI for science`, `#CRISPR`, `#Anthropic`, `#bioinformatics`, `#AI-assisted discovery`

---

<a id="item-5"></a>
## [Tailscale 优化用户态 WireGuard 以提升速度](https://tailscale.com/blog/making-tailscale-faster) ⭐️ 8.0/10

Tailscale 发布了一篇博客文章，详细介绍了对其用户态 WireGuard 实现所做的性能优化，旨在提升吞吐量和降低延迟。该文章在 Hacker News 上引发了关于网络速度、内核态与用户态权衡以及 DERP 中继架构的详细讨论。 这些优化可能显著提升 Tailscale 用户的 VPN 性能，尤其是在高带宽场景下，并凸显了用户态与内核态网络之间持续存在的争论。讨论还强调了中继灵活性和 NAT 穿透在网状 VPN 中的重要性。 Tailscale 使用用户态 WireGuard 实现（wireguard-go 的一个分支），以实现跨平台一致性并与其 NAT 穿透和策略层集成。联合创始人 apenwarr 指出，他们的优化曾使 wireguard-go 比内核 WireGuard 更快，而高带宽场景最终可能受益于 DPDK 等用户态框架。

hackernews · yarapavan · 9月23日 17:49 · [社区讨论](https://news.ycombinator.com/item?id=49819880)

**背景**: WireGuard 是一种现代 VPN 协议，可以在 Linux 内核或用户态运行。Tailscale 在 WireGuard 之上构建了网状 VPN，增加了 NAT 穿透、访问控制以及当直接点对点连接失败时用于连接的 DERP 中继服务器。用户态实现提供了灵活性，但通常比基于内核的实现产生更多开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailscale.com/compare/wireguard">WireGuard ® vs. Tailscale | Which is Better for You?</a></li>
<li><a href="https://tailscale.com/docs/reference/derp-servers">DERP servers · Tailscale Docs</a></li>
<li><a href="https://netbird.io/knowledge-hub/tailscale-vs-netbird?ref=faronics">Tailscale vs. NetBird</a></li>

</ul>
</details>

**社区讨论**: 评论者就 Tailscale 的速度限制展开了辩论，一些人认为内核 WireGuard 会更快，而另一些人指出用户态也可以具有竞争力。一个关键担忧是 DERP 中继的灵活性：一位用户希望有更智能的中继路径（例如 a->b->c），而不是总是通过遥远的 DERP 服务器路由。联合创始人 apenwarr 澄清说，内核态与用户态并非简单的权衡，他们的优化在历史上曾优于内核 WireGuard。

**标签**: `#networking`, `#wireguard`, `#tailscale`, `#performance`, `#vpn`

---

<a id="item-6"></a>
## [Token 便宜到无需计量：LLM 调用会否比 grep 更便宜？](https://jyn.dev/tokens-too-cheap-to-meter/) ⭐️ 8.0/10

jyn.dev 上的一篇文章指出，LLM 的 token 正变得极其便宜，调用 GPT-5.6 Luna 的成本仅比一次 grep 调用贵 4 到 5 个数量级，并预测按当前进步速度，LLM 调用很快就会比 grep 等传统工具调用更便宜。该文在 Hacker News 上引发 301 分、206 条评论的热议，讨论这种成本下降能否持续及其对商业模式的影响。 如果 LLM 推理真的比传统工具调用更便宜，可能会从根本上改变软件代理和开发者工具的构建方式，将工作负载从 grep 等确定性工具转向模型驱动的推理。这对 AI 基础设施投资、厂商定价策略以及当前假设未来 token 销售高利润的商业模式可行性都有重大影响。 核心比较对象是一次 grep 调用与一次 GPT-5.6 Luna 调用，作者估计后者目前贵 4 到 5 个数量级；该预测假设成本持续指数级下降。社区成员反驳称效率提升不可能永远持续，并援引斯坦定律，还指出文章忽略了在巨额基础设施投资下的商业模式可行性问题。

hackernews · teoruiz · 9月23日 09:21 · [社区讨论](https://news.ycombinator.com/item?id=49813482)

**背景**: 近年来 LLM 推理成本大幅下降——三年内下降了约 1000 倍，这一趋势有时被称为“LLMflation”——这得益于硬件改进、模型优化和供应商之间的竞争。与此同时，像 grep 这样的传统命令行工具在本地运行几乎免费，因此这一比较凸显了 LLM 经济学的巨大进步以及成本进一步下降可能带来的颠覆性影响。“便宜到无需计量”一词历史上指 1950 年代关于核能会让电力几乎免费的承诺，但该承诺并未如当初所言实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://a16z.com/llmflation-llm-inference-cost/">Welcome to LLMflation - LLM inference cost is going down fast</a></li>
<li><a href="https://themainthread.beehiiv.com/p/llm-token-economics-is-textbook-monopoly-behaviour">LLM Token Economics Is Textbook Monopoly Behaviour</a></li>

</ul>
</details>

**社区讨论**: 评论者大多对文章的推断持怀疑态度：有人援引斯坦定律认为效率提升不会永远持续，有人批评文章忽略了巨额基础设施投资下的商业模式可行性，还有人将“便宜到无需计量”的承诺与 1950 年代核能预测的失败相提并论。其他人则批评讨论中使用的 Artificial Analysis 图表是无意义的综合评分，还有评论者提到奥威尔关于原子弹的先见之明。

**标签**: `#LLM economics`, `#AI infrastructure`, `#cost trends`, `#token pricing`, `#Hacker News discussion`

---

<a id="item-7"></a>
## [ClusterMAX 3.0：SemiAnalysis 更新 GPU 云评级标准](https://newsletter.semianalysis.com/p/clustermax-30-the-industry-standard) ⭐️ 8.0/10

SemiAnalysis 发布了 ClusterMAX 3.0，这是其 GPU 云评级与排名系统的最新版本，从可靠性、性能、支持、定价和安全等维度对 80 多家 GPU 云服务商进行评估。此次更新覆盖基于 NVIDIA H100、H200、B200、GB200 NVL72 以及 AMD MI300X 的集群。 对于需要为 AI 训练和推理选择 GPU 基础设施的组织来说，ClusterMAX 已成为被广泛引用的行业基准，而 3.0 版本的更新在 GPU 云竞争日益激烈之际，为买家提供了更及时、更详细的对比。它帮助 AI/ML 团队和企业在日益拥挤的专业 GPU 云服务商市场中做出更明智的采购决策。 该评级系统从性能、网络、存储、安全、支持和定价等方面对服务商打分，依据的是独立测试和客户反馈，而非厂商提供的数据。SemiAnalysis 声称最初的 ClusterMAX 按 GPU 数量计算覆盖了约 90% 的 GPU 租赁市场，而 3.0 版本进一步扩大了分析的范围和深度。

rss · Semianalysis · 9月23日 21:20

**背景**: ClusterMAX 是由 SemiAnalysis 创建的评级与排名系统，这家研究机构以对半导体、AI 硬件和数据中心基础设施的深度技术分析而闻名。GPU 云是指出租 NVIDIA H100、B200 等高端 GPU 使用权的第三方服务商，这些 GPU 在训练和运行大型 AI 模型方面需求旺盛。由于这些服务商在可靠性、网络和成本方面差异很大，像 ClusterMAX 这样的独立基准评测系统能帮助客户在统一标准下进行比较。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.clustermax.ai/">GPU Cloud ClusterMAX™ Rating & Ranking System | SemiAnalysis</a></li>
<li><a href="https://newsletter.semianalysis.com/p/the-gpu-cloud-clustermax-rating-system-how-to-rent-gpus">The GPU Cloud ClusterMAX™ Rating System | How to Rent GPUs</a></li>
<li><a href="https://newsletter.semianalysis.com/p/clustermax-30-the-industry-standard">ClusterMAX 3.0: The Industry Standard GPU Cloud Rating System...</a></li>

</ul>
</details>

**标签**: `#GPU cloud`, `#cloud computing`, `#AI infrastructure`, `#benchmarking`, `#industry analysis`

---

<a id="item-8"></a>
## [Claude Code 云会话正式上线，最高可领 250 美元额度](https://code.claude.com/docs/en/claude-code-on-the-web) ⭐️ 8.0/10

Anthropic 正式发布 Claude Code 云会话功能，结束研究预览阶段，Pro、Max、Team 及 Enterprise 用户即使合上笔记本，任务仍可在云端继续运行并随时接管。符合条件的订阅用户可通过官方领取页或在 Claude Code 中执行 /claim-credit 命令，一次性领取 Pro 100 美元、Max 250 美元的云端额度。 这是目前使用最广泛的 AI 编程工具之一的重要产品里程碑，使 Claude Code 从局限于终端的助手转变为可从浏览器、手机、桌面应用或终端访问的持久化云服务。这标志着 Anthropic 正推动“常开型”智能体编程工作流，可能改变开发者委派长时间任务的方式，并与其他云端编程智能体展开竞争。 额度仅限用于 Cloud sessions，领取截止时间为太平洋时间 10 月 7 日 23:59，额度有效至 11 月 4 日 23:59；资格需登录后按账号及条款判定，并非所有用户均可领取。Anthropic 支持地区名单目前不含中国大陆、香港和澳门，且云会话需要连接 GitHub，因为每个会话都在独立分支和仓库副本上运行。

telegram · zaihuapd · 9月24日 02:45

**背景**: Claude Code 是 Anthropic 推出的智能体编程工具，能够理解代码库、编辑文件并运行命令，最初以终端中的有限研究预览形式发布。云会话将这一能力扩展到 Anthropic 的基础设施上运行，而非用户本机，因此合上笔记本后任务仍可继续，并可在不同设备间交接。新云会话启动时可运行 setup 脚本，在 Claude Code 启动前安装依赖或配置工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/cloud-environments">Configure cloud environments - Claude Code Docs</a></li>
<li><a href="https://alphasignal.ai/news/anthropic-ships-claude-code-cloud-sessions-so-developers-can-code-without-a">Anthropic Ships Claude Code Cloud Sessions so... | AlphaSignal</a></li>
<li><a href="https://www.anthropic.com/news/claude-3-7-sonnet">Claude 3.7 Sonnet and Claude Code \ Anthropic</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#Anthropic`, `#AI coding tools`, `#cloud development`, `#developer tooling`

---

<a id="item-9"></a>
## [OpenAI 称苹果 ChatGPT 集成表现不佳，双方合作出现裂痕](https://www.ft.com/content/256c4b36-a6c8-49ee-aa15-81cb089b2ced) ⭐️ 8.0/10

在 2026 年 9 月 23 日提交的法庭文件中，OpenAI 表示苹果的 ChatGPT 集成「表现严重不佳」，并对用户缺乏兴趣感到失望。该文件出自埃隆·马斯克的 xAI 提起的反垄断诉讼，同时披露苹果已就商业秘密起诉 OpenAI，并与谷歌合作使用 Gemini 重建 Siri。 这标志着全球两家最具价值的科技公司之间关系严重破裂，法律纠纷以及苹果转向谷歌 Gemini 可能重塑 AI 助手格局。这也凸显出默认设置和用户激活门槛如何决定 AI 分发合作的成败。 2024 年的协议使 ChatGPT 成为 Apple 智能的默认 AI，但该集成默认关闭且需要多步骤激活，OpenAI 将此归咎于采用率低。OpenAI 原本期望借助苹果品牌推广获得「光环效应」并带来更多订阅，但上线一个月内结果就令人失望。

telegram · zaihuapd · 9月24日 05:15

**背景**: Apple 智能是苹果在其设备上推出的一套 AI 功能，2024 年苹果与 OpenAI 合作将 ChatGPT 集成其中。商业秘密诉讼涉及窃取机密信息的指控，而反垄断诉讼则声称某合作关系非法扼杀竞争。苹果转向谷歌 Gemini 重建 Siri，标志着行业 AI 联盟的重新洗牌。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5mac.com/2026/09/23/openai-says-apple-intelligence-users-showed-little-interest-in-chatgpt-integration/">OpenAI says Apple Intelligence users showed little interest... - 9to5Mac</a></li>
<li><a href="https://www.ft.com/content/256c4b36-a6c8-49ee-aa15-81cb089b2ced?syn-25a6b1a6=1">Apple ’s ChatGPT tools ‘dramatically underperformed’, OpenAI claims</a></li>
<li><a href="https://finance.biggo.com/news/cdbc20a5-0293-4436-b2f5-d99b857e10a5">OpenAI Reveals Inside Story of Apple Partnership... — BigGo Finance</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Apple`, `#AI partnerships`, `#legal disputes`, `#Siri`

---