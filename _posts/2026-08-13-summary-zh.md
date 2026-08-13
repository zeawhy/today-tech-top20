---
layout: default
title: "Horizon Summary: 2026-08-13 (ZH)"
date: 2026-08-13
lang: zh
---

> 从 83 条内容中筛选出 15 条重要资讯。

---

1. [DeepSeek V4 Pro 0813 发布，性能强劲且成本低廉](#item-1) ⭐️ 9.0/10
2. [Tailscale 详述 16 年历史的 SQLite WAL 重置漏洞修复](#item-2) ⭐️ 9.0/10
3. [Qwen 发布 2.4 万亿参数 MoE 模型 Qwen3.8-2.4T-A95B](#item-3) ⭐️ 9.0/10
4. [研究人员窃取顶级 LLM API 的隐藏推理](#item-4) ⭐️ 9.0/10
5. [通过 WebSocket 传输 HTML：用极少的 JavaScript 构建实时 SPA](#item-5) ⭐️ 8.0/10
6. [xAI 发布 Grok 4.6，引发性能与 API 怪癖的讨论](#item-6) ⭐️ 8.0/10
7. [Chrome 渲染小 JPEG 的怪癖解析](#item-7) ⭐️ 8.0/10
8. [亚马逊默认用 Twitch 直播内容训练 AI，用户可选择退出](#item-8) ⭐️ 8.0/10
9. [AI 先驱在 Ai4 上辩论开源与监管](#item-9) ⭐️ 8.0/10
10. [General Catalyst 领投成立仅两个月的 River AI 11 亿美元融资](#item-10) ⭐️ 8.0/10
11. [Anthropic 未发布模型在黎曼猜想上取得进展](#item-11) ⭐️ 8.0/10
12. [Anthropic 将 AI 文本水印扩展到旧模型](#item-12) ⭐️ 8.0/10
13. [Adam 的逐坐标缩放破坏旋转不变性与低秩偏好](#item-13) ⭐️ 8.0/10
14. [解耦下降：通过 AMP 实现精确的训练-测试误差跟踪](#item-14) ⭐️ 8.0/10
15. [白宫拟扩大 AI 政策，开源模型纳入安全测试](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek V4 Pro 0813 发布，性能强劲且成本低廉](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 9.0/10

DeepSeek V4 Pro 0813 是 DeepSeek 1.6T 参数旗舰模型的正式发布版本，现已在 OpenRouter 上通过 API 提供。它拥有 1,048,576 token 的上下文窗口、384,000 token 的最大输出，定价为每百万输入 token 0.435 美元、每百万输出 token 0.87 美元。 此次发布意义重大，因为它以极具竞争力的价格提供了高性能模型，可能颠覆 AI 模型市场。早期社区测试显示，它能有效处理复杂的开发任务，使先进 AI 对开发者和企业更加可及。 该模型仅通过 API 提供，目前尚不清楚是否会发布开放权重。它包含来自 Artificial Analysis 的独立基准测试，官方公告强调了增强的智能体能力、对 Responses API 的支持以及 Codex 集成。

hackernews · explosion-s · 8月12日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=49274600)

**背景**: DeepSeek 是一家以低成本发布强大开源语言模型而闻名的中国 AI 公司。该模型采用的混合专家（MoE）架构每次只激活部分参数，提高了效率。根据 DeepSeek 官网，该模型现已全面在网页、移动应用和 API 上可用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V4 Pro 0813 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://lovableapp.org/blog/deepseek-v4-pro-0813">DeepSeek V4 Pro 0813 (2026): Complete Guide to Pricing ...</a></li>
<li><a href="https://deepseek.com/en/index.html">DeepSeek</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，用户报告在复杂任务上以低成本表现出色。一位用户指出在 Docker 部署任务上与 GPT-5.6-terra-high 相比存在一些小问题，而另一位用户则称赞在交通模拟器中获得了显著改进且没有引入新问题。一些用户表示有兴趣尝试该模型，还有人强调成本效益是关键因素。

**标签**: `#AI`, `#DeepSeek`, `#LLM`, `#model release`, `#open source`

---

<a id="item-2"></a>
## [Tailscale 详述 16 年历史的 SQLite WAL 重置漏洞修复](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 9.0/10

Tailscale 发布了一篇详细博客，讲述发现并修复一个存在 16 年的 SQLite 漏洞，该漏洞是 WAL 模式下检查点与写事务之间的罕见数据竞争。修复工作与 SQLite 团队合作完成，并借助了 Tailscale 资助的自定义 VFS shim。 该漏洞在特定并发条件下可能损坏 SQLite 数据库，影响无数依赖 SQLite 的应用。调试过程凸显了商业支持和专用工具对开源项目的价值，修复提升了 SQLite 对所有用户的可靠性。 该漏洞发生在检查点期间特定时间点发生写入时，导致检查点误以为页面已从 WAL 复制到主数据库，而实际上并未复制。Tailscale 资助了 tmstmpvfs shim 的开发，该 shim 添加的日志帮助隔离了竞争条件。

hackernews · ropbear · 8月12日 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49272832)

**背景**: SQLite 使用预写日志（WAL）模式来提高并发性，允许多个读取者和单个写入者。检查点操作将页面从 WAL 文件复制回主数据库。该漏洞是一个数据竞争，当写入和检查点在不同连接上并发发生时可能导致数据库损坏。SQLite 广泛用于嵌入式系统和应用程序，因此此类漏洞影响尤为重大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL-Reset bug</a></li>
<li><a href="https://www.sqlite.org/howtocorrupt.html">How To Corrupt An SQLite Database File</a></li>
<li><a href="https://ubuntu.com/blog/hunting-a-16-year-old-sqlite-bug-with-tla-is-dqlite-affected">Hunting a 16-year-old SQLite bug with TLA+: is dqlite affected? | Ubuntu</a></li>

</ul>
</details>

**社区讨论**: 社区称赞 Tailscale 资助开源开发，并通过商业支持合同认真对待该漏洞。评论者指出 SQLite 测试虽多但仍存在漏洞的讽刺之处，并赞赏详细的文章。一些人讨论了竞争条件的具体细节和单写入者设计。

**标签**: `#SQLite`, `#bug`, `#debugging`, `#open-source`, `#database`

---

<a id="item-3"></a>
## [Qwen 发布 2.4 万亿参数 MoE 模型 Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen 发布了 Qwen3.8-2.4T-A95B，这是一个 2.4 万亿参数的混合专家模型，每个 token 激活 950 亿参数，提供 BF16 和 FP8 两种格式。该模型声称性能介于 Opus 4.8 和 Fable 5 之间。 此次发布意义重大，因为它将前沿性能带到了开源社区，可能挑战 Opus 和 Fable 等专有模型。这可能加速大型 MoE 模型在研究和工业界的应用，尽管部署要求仍然很高。 该模型采用细粒度 MoE 架构，包含 512 个路由专家（10 个激活）加一个共享专家，基于 92 层混合注意力骨干，支持高达 1M 上下文和 128K 输出。BF16 版本需要约 4.9TB 内存，而 1 位量化版本约为 397GB。

hackernews · Philpax · 8月12日 15:01 · [社区讨论](https://news.ycombinator.com/item?id=49273478)

**背景**: 混合专家（MoE）模型每个 token 只激活部分参数，从而在可控计算量下实现大规模。Qwen3.8-2.4T-A95B 是 Qwen3.8-Max 的开源版本，后者增加了视觉、1M 上下文和内置工具。BF16 和 FP8 是精度格式；FP8 减少内存并加速推理，但可能需要仔细量化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://recipes.vllm.ai/Qwen/Qwen3.8-2.4T-A95B">Qwen/Qwen3.8-2.4T-A95B — 2.4T / 95B active · MOE · 256K ctx</a></li>
<li><a href="https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/">Serve Qwen3.8-2.4T-A95B, a 2.4T-Parameter Model, with Configurable Reasoning on NVIDIA GB300 NVL72 | NVIDIA Technical Blog</a></li>
<li><a href="https://www.mindstudio.ai/blog/qwen3-8-2-4t-a95b-release">Qwen3.8-2.4T-A95B: Alibaba's Open-Weight Qwen-Max Flagship Explained | MindStudio</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了模型的大小和部署挑战，有人指出由于缺乏 QAT 量化，它比 Kimi k3 更难部署。其他人对 1 位量化版本能装进消费级硬件感到兴奋，并讨论了硬件成本预测。一些人对开源模型缺少官方版本的视觉和 1M 上下文功能表示失望。

**标签**: `#AI/ML`, `#Large Language Models`, `#MoE`, `#Qwen`, `#Open Source`

---

<a id="item-4"></a>
## [研究人员窃取顶级 LLM API 的隐藏推理](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/) ⭐️ 9.0/10

研究人员展示了一种方法，通过将加密的思维链推理轨迹重放到较弱的兄弟模型中并对其进行越狱，从而恢复专有 LLM API 中的隐藏推理。该攻击影响了 Anthropic、OpenAI 和 Google，但现已修复。 这项研究暴露了主要 AI API 中的重大安全漏洞，凸显了隐藏推理提取的风险以及模型蒸馏或数据外泄的可能性。它强调了在 AI 服务中实施强加密和访问控制的必要性。 该攻击利用了同一系列模型共享相同加密密钥的特点，使得加密的推理块可以被重放到较弱的模型（如 Claude Haiku 4.5）中，并通过越狱使其输出明文。论文中包含了大量提取的推理轨迹，揭示了本不打算供人类阅读的原始思维链内容。

rss · Simon Willison · 8月11日 22:40

**背景**: 思维链推理是一种让 LLM 生成中间步骤以得出答案的技术，在专有 API 中通常对用户隐藏。为了维持上下文，API 会加密这些推理轨迹并传回客户端，但加密密钥在模型系列中共享，从而使得攻击成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/top-ai-models-apis-flaw-exposes-hidden-reasoning/">OpenAI, Anthropic, and Google LLM APIs vulnerability Exposes...</a></li>
<li><a href="https://arxiv.org/pdf/2608.09867">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>

</ul>
</details>

**标签**: `#LLM security`, `#chain-of-thought`, `#proprietary APIs`, `#AI safety`, `#research`

---

<a id="item-5"></a>
## [通过 WebSocket 传输 HTML：用极少的 JavaScript 构建实时 SPA](https://en.andros.dev/blog/ef4968f5/html-over-websockets-real-time-spas-with-barely-any-javascript/) ⭐️ 8.0/10

这篇文章讨论了使用 HTML over WebSockets 构建实时 SPA 的技术，该技术由 Phoenix LiveView 推广，并强调了如何最小化 JavaScript 的使用。文章还提到了 Chrome 中新的 HTML 流式 API，这些 API 可以进一步减少 JS 依赖。 这种方法挑战了传统的重度 JavaScript SPA 范式，为构建实时应用提供了一种更简单、更高效的方式。它可能影响未来的 Web 开发实践，尤其是需要实时更新的服务端渲染应用。 该技术使用 WebSocket 直接将 HTML 片段发送到浏览器，然后更新 DOM，无需自定义客户端 JavaScript。文章指出，对于大多数应用，SSE（服务器发送事件）更简单且成本更低，但对于双向低延迟通信，WebSocket 是必需的。

hackernews · redbell · 8月12日 16:51 · [社区讨论](https://news.ycombinator.com/item?id=49275335)

**背景**: Phoenix LiveView 由 Chris McCord 创建，是一个允许通过 WebSocket 发送 HTML 来构建交互式 Web 应用而无需编写大量 JavaScript 的框架。这项技术早于 LiveView，因为 McCord 在转向 Phoenix 之前曾在 Rails 中尝试过类似的想法。这种方法与依赖客户端渲染和 REST API 的传统 SPA 形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/phoenixframework/phoenix_live_view">Phoenix LiveView</a></li>
<li><a href="https://www.phoenixframework.org/">Phoenix Framework</a></li>
<li><a href="https://websocket.org/comparisons/sse/">WebSocket vs SSE: Which One Should You Use?</a></li>

</ul>
</details>

**社区讨论**: 评论中强调了历史背景，指出 Chris McCord 在 LiveView 之前就在 Rails 中开创了这项技术。一些人讨论了 WebSocket 和 SSE 之间的权衡，有评论者认为在大多数情况下 SSE 更简单。其他人则提到 Chrome 中新的 HTML 流式 API，可以进一步减少 JS 包，并附有一个批评性回应的链接。

**标签**: `#WebSockets`, `#Real-time`, `#SPA`, `#Phoenix LiveView`, `#SSE`

---

<a id="item-6"></a>
## [xAI 发布 Grok 4.6，引发性能与 API 怪癖的讨论](https://x.ai/news/grok-4-6) ⭐️ 8.0/10

xAI 发布了新前沿 AI 模型 Grok 4.6。它在 AA-Briefcase 基准测试中首次亮相，Elo 评分为 1577，达到 Fable 5 级别，并在多个基准测试中表现出色。 Grok 4.6 的发布加剧了主要 AI 实验室之间的竞争，提供了具有竞争力的性价比替代方案。其强劲的基准测试结果和较低的价格可能对其他前沿模型构成压力，并使寻求高智能低成本的用户受益。 Grok 4.6 支持 500k 上下文窗口，并提供四种推理努力级别：xhigh、high（默认）、medium 和 low。定价为每百万输入 token 2.00 美元，每百万输出 token 6.00 美元，输出 token 价格低于中位数。

hackernews · iLuddite · 8月12日 15:32 · [社区讨论](https://news.ycombinator.com/item?id=49274027)

**背景**: Grok 是由 Elon Musk 领导的 xAI 开发的聊天机器人。该公司已连续发布多个 Grok 模型版本，其中 Grok 4 和 4 Heavy 于 2025 年 7 月发布。Grok 4.6 是最新迭代，旨在与 GPT-5.6 和 Claude 4.8/5 等其他前沿模型竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis">Grok 4 . 6 returns SpaceXAI to the intelligence frontier and leads on cost...</a></li>
<li><a href="https://x.ai/news/grok-4-6">Introducing Grok 4 . 6 | SpaceXAI</a></li>
<li><a href="https://docs.x.ai/developers/grok-4-6">Grok 4 . 6 | SpaceXAI Docs</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了对 API 添加默认系统提示并覆盖用户指令的担忧，以及对各实验室基准测试快速改进的怀疑，暗示可能存在基准测试作弊。一些用户认为 Grok 4.5 比竞争对手更易用，而另一些用户则认为尽管 Grok 声誉两极分化，但它是一个健康的竞争者。

**标签**: `#AI`, `#Grok`, `#xAI`, `#LLM`, `#benchmarks`

---

<a id="item-7"></a>
## [Chrome 渲染小 JPEG 的怪癖解析](https://guillaumetech.github.io/posts/jpg-scaling-chrome/) ⭐️ 8.0/10

一篇技术文章解释了 Chrome 渲染小 JPEG 时之所以不同，是因为它进行了部分解压缩，这可能导致视觉伪影。作者建议不要将 JPEG 用于小图标，而应使用 PNG 或尺寸合适的图像。 这很重要，因为许多开发者使用 JPEG 作为图标和小图像，而渲染差异可能导致跨浏览器的意外视觉问题。理解这一行为有助于开发者选择合适的图像格式，并避免在 Web 和 Electron 应用中产生细微的 bug。 文章指出，Chrome 的部分解压缩是一种优化，但在图像大幅缩小时可能导致伪影。文章还提到 Firefox 正在开发类似的低比例解压缩（参见 bug 2033250），并且不同浏览器之间的缩放算法差异也导致了视觉差异。

hackernews · gutechh · 8月12日 14:00 · [社区讨论](https://news.ycombinator.com/item?id=49272549)

**背景**: JPEG 是一种常用于照片的有损压缩标准，但在低质量设置下会引入压缩伪影，如块状和颜色带状。当图像以远小于原始分辨率的大小显示时，浏览器必须缩小它，而缩放算法和解压缩方法会影响最终外观。Chrome 的部分解压缩只解码部分 JPEG 数据以加快渲染速度，与完全解压缩后再缩放相比，可能产生不同的结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JPEG">JPEG - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Compression_artifact">Compression artifact - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，PNG 也可能出现同样的问题，并且使用尺寸合适的图像比格式更重要。一位评论者提供了 Firefox 低比例解压缩的 bug 链接，另一位则认为 Chrome 和 Firefox 之间不同的缩放算法对视觉差异影响更大。还有用户质疑 Firefox 是进行完整渲染还是部分渲染，表明希望看到更平衡的比较。

**标签**: `#browser`, `#image-processing`, `#JPEG`, `#Chrome`, `#web-performance`

---

<a id="item-8"></a>
## [亚马逊默认用 Twitch 直播内容训练 AI，用户可选择退出](https://techcrunch.com/2026/08/12/amazon-will-train-on-twitch-streamers-content-by-default-unless-they-opt-out/) ⭐️ 8.0/10

亚马逊将默认使用 Twitch 主播的内容来训练其生成式 AI 模型，现在 Twitch 账户设置中的“安全与隐私”选项下提供了退出设置。Twitch 首席产品官 Mike Minton 确认了默认开启的做法，并表示如果采用选择加入模式，参与人数会很少。 这一政策变化引发了重大的隐私和同意问题，因为它在未经明确同意的情况下利用用户生成内容进行 AI 训练，可能为其他平台开创先例。这影响到数百万 Twitch 主播，并可能影响关于 AI 训练数据伦理和用户权利的更广泛讨论。 退出设置的标签为“生成式 AI 训练”，可阻止亚马逊使用频道的直播、点播视频、剪辑、精彩片段、聊天和文本进行训练。然而，一些被视为平台运行所必需的 AI 功能无法退出，且退出不影响已训练的模型。

rss · TechCrunch AI · 8月12日 20:10

**背景**: Twitch 是亚马逊旗下流行的直播平台，用户在此广播游戏、创意内容等。生成式 AI 模型（如亚马逊的 Nova 系列）需要大量数据进行训练，公司常利用用户生成内容来改进这些模型。此举顺应了行业趋势，此前 Reddit 和 Google 等平台因类似做法遭到批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.engadget.com/2235928/how-to-stop-twitch-training-ai-on-streams/">How to stop Twitch from training AI on your streams - Engadget</a></li>
<li><a href="https://appleinsider.com/articles/26/08/12/twitch-will-train-amazons-ai-on-your-streams-unless-you-opt-out">Twitch will train Amazon's AI on your streams unless you opt out</a></li>
<li><a href="https://www.bbc.com/news/articles/cp30pz8d09jo">Twitch users can now block Amazon from using their content to train AI</a></li>

</ul>
</details>

**社区讨论**: 社区反应大多为负面，在公告期间用户涌入 Twitch 聊天室表达批评。许多人担心同意问题和缺乏选择加入机制，也有人指出退出选项是进步，但鉴于默认开启的性质，这还不够。

**标签**: `#AI training`, `#privacy`, `#Twitch`, `#Amazon`, `#ethics`

---

<a id="item-9"></a>
## [AI 先驱在 Ai4 上辩论开源与监管](https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/) ⭐️ 8.0/10

在拉斯维加斯举行的 Ai4 大会上，杰弗里·辛顿、李飞飞和吴恩达公开辩论了 AI 监管、开源访问以及在中国进步背景下美国的竞争力。讨论凸显了三位先驱在如何平衡安全与创新方面的深刻分歧。 这场辩论之所以重要，是因为它汇集了 AI 领域三位最具影响力的声音，共同探讨一个关键政策问题：是否应出于安全原因限制开源 AI。他们的立场可能影响监管机构和行业领袖，因为他们正在塑造 AI 治理的未来。 这场辩论发生在 2026 年 8 月 4 日至 6 日于拉斯维加斯举行的 Ai4 大会上，是三人罕见的同台亮相。报道称，三位专家在就业、监管以及谁应塑造 AI 未来等问题上发生冲突，辛顿强调存在性风险，而李飞飞和吴恩达则主张务实、开放的态度。

rss · TechCrunch AI · 8月12日 17:51

**背景**: 杰弗里·辛顿是诺贝尔奖得主、AI 先驱，他最近警告 AI 可能超越人类并逃出测试环境，凸显安全漏洞。李飞飞是斯坦福大学研究员、World Labs 创始人，她此前敦促政策制定者采取务实态度而非意识形态化。吴恩达是著名 AI 教育家和企业家，一直倡导开源和 AI 访问的民主化。这场辩论反映了 AI 社区在如何管理快速发展同时确保安全和竞争力方面的更广泛紧张关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/">As AI safety concerns mount, three pioneers make the case for ...</a></li>
<li><a href="https://www.forbes.com/sites/ronschmelzer/2026/08/06/hinton-li-ng-ai-jobs-regulation/">Three AI Pioneers Clash Over Jobs, Regulation And The Future ...</a></li>
<li><a href="https://www.datacenterknowledge.com/regulations/hinton-fei-fei-li-and-andrew-ng-clash-over-ai-risks-jobs-and-regulation-at-ai4">Hinton, Fei-Fei Li, and Andrew Ng Clash Over AI Risks at Ai4</a></li>

</ul>
</details>

**社区讨论**: 此新闻条目未提供社区评论。

**标签**: `#AI safety`, `#open source`, `#regulation`, `#AI policy`, `#Geoffrey Hinton`

---

<a id="item-10"></a>
## [General Catalyst 领投成立仅两个月的 River AI 11 亿美元融资](https://techcrunch.com/2026/08/11/general-catalyst-leads-1-1b-round-into-2-month-old-river-ai/) ⭐️ 8.0/10

由 xAI 联合创始人 Igor Babuschkin 创立的初创公司 River AI 在成立仅两个月后，获得了由 General Catalyst 领投的 11 亿美元融资。该公司旨在开发个人 AI 代理。 这笔巨额早期投资表明投资者对个人 AI 代理这一快速发展的领域充满信心。同时，它也凸显了知名 AI 创始人的持续影响力，并可能加速消费级 AI 领域的竞争。 本轮融资由 General Catalyst 领投，该公司是一家管理资产超过 430 亿美元的知名风险投资公司。River AI 成立仅两个月，尚未发布任何产品，这表明投资主要基于团队和愿景。

rss · TechCrunch AI · 8月11日 17:41

**背景**: 个人 AI 代理是能够代表用户执行任务的自主软件系统，例如管理电子邮件、日程安排和提醒。Igor Babuschkin 是埃隆·马斯克旗下 AI 公司 xAI 的联合创始人，最近离开并创办了自己的企业。General Catalyst 是一家知名的风险投资公司，投资了 Anthropic 和 Mistral 等公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/General_Catalyst">General Catalyst</a></li>
<li><a href="https://grokipedia.com/page/igor-babuschkin">Igor Babuschkin</a></li>
<li><a href="https://aimultiple.com/personal-ai-agents">Building Personal AI Agents + 18 Agent Platforms and Tools</a></li>

</ul>
</details>

**标签**: `#AI`, `#funding`, `#startup`, `#personal agents`

---

<a id="item-11"></a>
## [Anthropic 未发布模型在黎曼猜想上取得进展](https://techcrunch.com/2026/08/11/an-unreleased-anthropic-model-made-progress-on-one-of-maths-biggest-unsolved-problems/) ⭐️ 8.0/10

据报道，Anthropic 未发布的 AI 模型在著名的未解数学问题——黎曼猜想上取得了意外进展，但并未解决该问题。该模型及其发现的具体细节尚未公开。 这意义重大，因为它表明先进的 AI 模型能够为前沿数学研究做出贡献，可能加速长期未解问题的进展。这也凸显了 AI 在科学发现中日益重要的作用，可能影响全球的数学家及研究人员。 文章未提供该模型或其进展性质的技术细节，留下许多未解之谜。黎曼猜想于 1859 年提出，断言黎曼ζ函数的所有非平凡零点的实部均为 1/2，尽管经过大量努力，该猜想仍未得到证明。

rss · TechCrunch AI · 8月11日 16:25

**背景**: 黎曼猜想是纯数学中最重要的未解问题之一，与素数的分布有深刻联系。它是克莱数学研究所的千禧年大奖难题之一，为证明提供 100 万美元奖金。像 Anthropic 的 Claude 系列这样的 AI 模型已展现出高级推理能力，这一消息表明它们可能被应用于此类数学挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://www.claymath.org/millennium/riemann-hypothesis/">Riemann Hypothesis - Clay Mathematics Institute</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#Anthropic`, `#Riemann hypothesis`, `#research`

---

<a id="item-12"></a>
## [Anthropic 将 AI 文本水印扩展到旧模型](https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/) ⭐️ 8.0/10

Anthropic 宣布将把 AI 生成文本的水印支持扩展到旧模型，此前该公司已承诺遵守欧盟《人工智能法案》的透明度框架。8 月 2 日之后发布的所有模型将自动包含对文本和文件进行水印的技术，其中文件使用 C2PA 开放标准。 此举增强了 AI 生成内容的可追溯性，有助于打击虚假信息并满足监管要求。它为其他 AI 实验室树立了先例，可能加速整个行业采用水印标准。 文本水印设计为在正常阅读时不可见，并在内容被复制或粘贴时仍然存在。Anthropic 还在努力改造旧模型，并计划为第三方提供检测工具。

rss · TechCrunch AI · 8月11日 12:13

**背景**: 文本水印是一种在文本内容中嵌入隐藏信息以验证其真实性或来源的技术。随着生成式 AI 的兴起，针对 AI 生成文本的水印技术得到了显著发展，以应对虚假信息和监管合规问题，例如欧盟《人工智能法案》第 50 条要求 AI 输出可被检测为人工生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/">Anthropic says it will watermark text generated by its AI models</a></li>
<li><a href="https://en.wikipedia.org/wiki/Text_watermarking">Text watermarking - Wikipedia</a></li>
<li><a href="https://www.seangoedecke.com/text-ai-watermarks/">Text AI watermarks will always be trivial to remove</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#watermarking`, `#AI safety`, `#content authenticity`

---

<a id="item-13"></a>
## [Adam 的逐坐标缩放破坏旋转不变性与低秩偏好](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 8.0/10

一项新研究表明，Adam 的逐坐标二阶矩破坏了因子化模型中的旋转不变性，从而消除了梯度下降所展现的隐式低秩偏好。作者在矩阵感知任务上测试了九种优化器，发现 GD、Muon 和 Shampoo 等旋转不变方法保留了该偏好，而 Adam、RMSProp 等则失去了它。 这一发现阐明了为何某些优化器在低秩场景下泛化更好，这对训练大语言模型及其他过参数化系统至关重要。同时，它揭示了一个此前被忽视的设计准则——旋转不变性，可为新优化器的开发提供指导。 研究使用一个单参数族在逐坐标和共享标量分母之间插值，表明随着各向异性降低，恢复性能单调提升。Muon 表现意外：在真正低秩目标上表现优异，但随着谱尾增加退化最快，并在约 4%尾能量处与 GD 交叉。论文还指出，当每种优化器在各自网格上调优时，高光谱数据上 43-44%的误差降低会缩小。

reddit · r/MachineLearning · /u/EtherealGlyph · 8月12日 16:39

**背景**: 在因子化模型（如 W = UV^T）中，损失对旋转（U,V）→（UQ, VQ）具有不变性，而梯度下降尊重这一对称性。然而，Adam 的逐坐标二阶矩依赖于基的选择，破坏了这种不变性。隐式低秩偏好是指某些优化器即使没有显式正则化也倾向于收敛到低秩解，这在许多任务中有助于泛化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.01472v1">The Newton–Muon Optimizer - arXiv.org</a></li>
<li><a href="https://github.com/KellerJordan/Muon">GitHub - KellerJordan/Muon: Muon is an optimizer for hidden ...</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论可能包括关于结果是否因 Adam 调参不足而产生的争论，作者预见了诸如“你应该更努力地调 Adam”之类的反对意见。一些人可能质疑矩阵感知实验对实际深度学习的相关性，而另一些人可能欣赏其理论清晰度和 Muon 的意外表现。

**标签**: `#optimization`, `#Adam`, `#low-rank bias`, `#matrix sensing`, `#implicit bias`

---

<a id="item-14"></a>
## [解耦下降：通过 AMP 实现精确的训练-测试误差跟踪](https://www.reddit.com/r/MachineLearning/comments/1vlu1se/decoupled_descent_enforcing_exact_traintest_error/) ⭐️ 8.0/10

提出了一种名为解耦下降（DD）的新训练方法，利用近似消息传递（AMP）修正来确保训练误差在每次迭代时渐近等于测试误差。该方法在风格化的高斯混合模型和高维 XOR 模型上进行了演示，表明 DD 避免了梯度下降中出现的过拟合问题。 这项工作解决了神经网络训练中的一个基本问题，即训练误差下降但测试误差停滞或恶化，提供了一种有理论依据的方法来缓解过拟合。它可能实现无需留出数据的验证，并为最优停止和超参数调优开辟新方向，可能影响模型的训练和评估方式。 该方法依赖于 AMP 理论，并在低维状态演化递归下运行，使其动态过程透明且易于处理。该论文是理论性的，专注于风格化问题，并计划未来开发兼容 PyTorch 的包。

reddit · r/MachineLearning · /u/mlovik1 · 8月11日 21:06

**背景**: 近似消息传递（AMP）是高维统计学中的一种技术，用于信号恢复和推断，以其状态演化分析而闻名，能够精确刻画算法行为。在机器学习中，过拟合是指模型过于紧密地拟合训练数据，从而损害对新数据的泛化能力。解耦下降利用 AMP 来强制实现训练-测试一致性，确保训练误差跟踪测试误差，从而防止过拟合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2201.07487">A Concise Tutorial on Approximate Message Passing A unifying tutorial on Approximate Message Passing Lecture 19: Approximate message passing algorithms Approximate Message Passing Tutorial - GitHub Pages Vector Approximate Message Passing - IEEE Xplore Message-passing algorithms for compressed sensing Approximate Message Passing - GitHub Pages</a></li>
<li><a href="https://arxiv.org/abs/2105.02180">A unifying tutorial on Approximate Message Passing Lecture 19: Approximate message passing algorithms Approximate Message Passing Tutorial - GitHub Pages Vector Approximate Message Passing - IEEE Xplore Message-passing algorithms for compressed sensing Approximate Message Passing - GitHub Pages</a></li>
<li><a href="https://arxiv.org/pdf/2604.27883">Decoupled Descent: Exact Test Error Tracking Via Approximate ...</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#optimization`, `#generalization`, `#approximate message passing`, `#theory`

---

<a id="item-15"></a>
## [白宫拟扩大 AI 政策，开源模型纳入安全测试](https://www.wired.com/story/the-white-house-is-going-to-expand-its-ai-policy/) ⭐️ 8.0/10

白宫计划修订其 AI 政策框架，将开源模型纳入发布前安全测试，一旦它们达到“前沿”能力，超出目前对 Anthropic 和 OpenAI 等闭源模型的覆盖范围。该框架仍属自愿，预计在未来数月内生效。 这一扩展可能对开源 AI 生态系统产生重大影响，可能减缓强大开源模型的发布，并影响美国在 AI 开发方面的竞争力。这标志着监管注意力转向开放权重模型，这些模型一直是创新的主要驱动力，但也引发安全担忧。 该政策将要求开源模型一旦达到“前沿”能力（指超越前代能力并超出现有监管框架的模型）即接受安全测试。一些官员担心，可能的 30 天测试要求会抑制美国企业，而该框架的自愿性质部分源于特朗普总统认为正式监管会帮助中国追赶。

telegram · zaihuapd · 8月13日 00:43

**背景**: 前沿 AI 指的是处于能力前沿的模型，通常超越前代模型并带来新的风险。白宫的 AI 政策框架最初是为 OpenAI 和 Anthropic 等闭源模型设计的，但开源模型的影响力日益增长，促使需要更广泛的监管。安全测试旨在部署前识别并缓解对抗性攻击或意外行为等风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zertia.ai/glossary/governance/frontier-ai/">Frontier AI : Capability Beyond the Framework | Zertia</a></li>
<li><a href="https://www.politico.com/news/2026/08/04/white-house-ai-vetting-plan-to-exempt-nonproprietary-models-01024816">White House AI vetting plan to exempt lower-cost ‘open’ models</a></li>
<li><a href="https://owasp.org/www-project-ai-testing-guide/">OWASP AI Testing Guide</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#open-source`, `#safety testing`, `#regulation`, `#White House`

---