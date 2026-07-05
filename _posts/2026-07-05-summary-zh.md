---
layout: default
title: "Horizon Summary: 2026-07-05 (ZH)"
date: 2026-07-05
lang: zh
---

> 从 39 条内容中筛选出 10 条重要资讯。

---

1. [F-Droid 将 Google ADV 定性为恶意软件，已预装于 40 亿设备](#item-1) ⭐️ 9.0/10
2. [Shadcn/UI 默认组件从 Radix 切换到 Base UI](#item-2) ⭐️ 8.0/10
3. [GPT-5.5 Codex 516 Token 推理聚类导致性能下降](#item-3) ⭐️ 8.0/10
4. [sqlite-utils 4.0rc2：Claude Fable 发现关键漏洞](#item-4) ⭐️ 8.0/10
5. [新 Claude 模型工具调用模式遵守更差](#item-5) ⭐️ 8.0/10
6. [能力门控：基于内部置信信号控制工具使用](#item-6) ⭐️ 8.0/10
7. [USAF：在消费级 GPU 上对 MoE 模型进行稀疏微调](#item-7) ⭐️ 8.0/10
8. [iOS 27 将推出 Trust Insights 反诈功能](#item-8) ⭐️ 8.0/10
9. [卫报调查：OpenAI 从未实地考察英国星际之门核心选址](#item-9) ⭐️ 8.0/10
10. [复旦期末考：学生出题难倒 AI，仅 4 人得零分](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [F-Droid 将 Google ADV 定性为恶意软件，已预装于 40 亿设备](https://f-droid.org/2026/07/01/adv-malware.html) ⭐️ 9.0/10

F-Droid 正式将 Google 的 Android 开发者验证（ADV）定性为恶意软件，称其是一个拥有 root 权限且无法移除的系统进程，已预装在约 40 亿台安卓设备上。自 2026 年 9 月 30 日起，ADV 将在巴西、印尼、新加坡和泰国首批激活，阻止用户安装未经 Google 批准的软件。 此举威胁到安卓生态系统的开放性和用户自由，可能使 Google 能够阻止任何未经批准的软件，包括广告拦截器和自由开源软件。它已引发 EFF、FSF、ACLU 等数字权利组织的广泛反对，并可能为平台控制开创先例。 F-Droid 指出，Google 在开发者服务条款中刻意不对“恶意软件”下定义，从而可任意将不喜欢的软件归类。尽管已有数十万人联署反对、超过 70 个组织签署公开信谴责，Google 仍在推进全球推广，计划于 2027 年及以后实施。

telegram · zaihuapd · 7月5日 00:41

**背景**: F-Droid 是一个免费开源的安卓应用商店，仅托管自由开源软件。Google Play Protect 是内置的安全服务，用于扫描应用。ADV 是 Google 引入的新系统进程，作为额外的安全层，但批评者认为它赋予 Google 对用户安装软件的过度控制，损害了安卓的开放性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.android.com/developer-verification">Android developer verification | Android Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/F-Droid">F-Droid</a></li>

</ul>
</details>

**标签**: `#Android`, `#malware`, `#F-Droid`, `#Google`, `#digital rights`

---

<a id="item-2"></a>
## [Shadcn/UI 默认组件从 Radix 切换到 Base UI](https://ui.shadcn.com/docs/changelog) ⭐️ 8.0/10

Shadcn/UI 已将其默认组件库从 Radix UI 切换为 Base UI，后者是由 Radix、Floating UI 和 Material UI 的创建者开发的新无样式组件库。 这一转变影响了数千个使用 Shadcn/UI 的项目，并引发了关于迁移策略（包括使用 codemods 与 LLM）以及复制粘贴方法可维护性的讨论。 Base UI 是一个无样式、无头组件库，提供对样式和可访问性的完全控制，与 Radix 类似但 API 不同。这一变化反映了 Shadcn/UI 的持续演进和社区反馈。

hackernews · dabinat · 7月5日 04:46 · [社区讨论](https://news.ycombinator.com/item?id=48791328)

**背景**: Shadcn/UI 是一个流行的可复用 React 组件集合，基于 Radix UI 和 Tailwind CSS 构建，通过 CLI 分发以实现完全代码所有权。Radix UI 是一个专注于可访问性的低级无样式组件库。Base UI 来自同一团队，以全新方法提供类似理念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ui.shadcn.com/docs">Introduction - shadcn/ui</a></li>
<li><a href="https://base-ui.com/">Unstyled UI components for accessible design systems · Base UI</a></li>
<li><a href="https://github.com/mui/base-ui">GitHub - mui/base-ui: Unstyled UI components for building accessible web apps and design systems. From the creators of Radix, Floating UI, and Material UI. · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了复杂情绪：一些人认为复制粘贴方法带来了升级挑战，而另一些人则欢迎摆脱过度设计的解决方案。关于使用 LLM 而非传统 codemods 进行迁移也存在争论。

**标签**: `#UI Libraries`, `#React`, `#Frontend Development`, `#Open Source`

---

<a id="item-3"></a>
## [GPT-5.5 Codex 516 Token 推理聚类导致性能下降](https://github.com/openai/codex/issues/30364) ⭐️ 8.0/10

用户报告称，GPT-5.5 Codex 的推理 token 聚类在恰好 516 个 token 时会导致性能下降和错误答案，社区提供了可复现该问题的脚本。 该 bug 影响广泛使用的 AI 编码工具，可能影响依赖 Codex 进行代码生成和推理任务的众多开发者，并引发对静默服务端更改的担忧。 聚类发生在 516 的倍数 token 处（516、1034、1552），当模型恰好停在 516 个 token 时，通常返回错误结果；使用更多 token（6000-8000）则能得到正确答案。

hackernews · maille · 7月4日 21:51 · [社区讨论](https://news.ycombinator.com/item?id=48789428)

**背景**: GPT-5.5 Codex 是 OpenAI 于 2026 年发布的最新专注编码的模型，是 GPT-5.3 Codex 的升级版。推理 token 是模型在生成最终答案前用于思考问题的内部 token。Token 聚类指模型不成比例地停在特定 token 数量，表明自适应思考机制存在 bug。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/gpt-5-5-codex-reasoning-token-clustering-bug-2026">GPT-5.5 Codex 516- Token Bug: Evidence and Theories... | explainx.ai</a></li>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT - 5 . 5 | OpenAI</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍负面，用户报告每日质量下降并转向 Claude 等替代品。有人将其与 4 月 Claude Code 的类似回归问题相提并论，也有人建议使用本地模型以避免服务端更改。

**标签**: `#AI`, `#LLM`, `#Codex`, `#bug`, `#performance`

---

<a id="item-4"></a>
## [sqlite-utils 4.0rc2：Claude Fable 发现关键漏洞](https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/#atom-everything) ⭐️ 8.0/10

Simon Willison 使用 Claude Fable 审查 sqlite-utils 4.0rc1，发现了五个发布阻塞漏洞，其中包括 delete_where() 中的数据丢失漏洞。经过 37 次提示和 34 次提交，修复后发布了 sqlite-utils 4.0rc2。 这展示了 AI 辅助代码审查如何在重大发布前捕获细微但影响严重的漏洞，提升软件质量并减少紧急补丁的需求。同时，它展示了一种将 LLM 集成到开源维护中的实用工作流程。 发现的最严重漏洞是 Table.delete_where() 从未提交，导致连接处于中毒状态，后续写入操作被静默丢失。审查花费了约 149.25 美元的 Claude API 使用费，整个过程涉及 37 次提示和 34 次提交，跨越 30 个文件。

rss · Simon Willison · 7月5日 01:00

**背景**: sqlite-utils 是一个用于操作 SQLite 数据库的 Python 库和 CLI 工具。语义化版本控制（SemVer）使用三位版本号（主版本号.次版本号.修订号），其中破坏性变更需要增加主版本号。Claude Fable 是 Anthropic 为复杂编码任务设计的高级 AI 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/sqlite-utils">GitHub - simonw/sqlite-utils: Python CLI utility and library for ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable">Claude Fable</a></li>
<li><a href="https://en.wikipedia.org/wiki/SemVer">SemVer</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#open source`, `#Python`, `#sqlite-utils`, `#Claude`

---

<a id="item-5"></a>
## [新 Claude 模型工具调用模式遵守更差](https://simonwillison.net/2026/Jul/4/better-models-worse-tools/#atom-everything) ⭐️ 8.0/10

Armin Ronacher 于 2026 年 7 月 4 日报道，包括 Opus 4.8 和 Sonnet 5 在内的新 Claude 模型有时会生成带有额外虚构字段的无效工具调用参数，导致 Pi 的编辑工具拒绝这些调用。旧版 Claude 模型未出现此退化。 这种退化削弱了依赖精确工具调用模式的 AI 编码代理的可靠性，影响了使用 Pi 等第三方工具链的开发者。它凸显了模型针对特定工具的训练与通用工具使用之间的张力。 额外字段由模型虚构，可能包括'new_text_x'、'type'、'in_file'或'closeenough'等键。据报道，在 Claude 的 API 中启用严格模式可解决部分用户的问题。

rss · Simon Willison · 7月4日 22:53

**背景**: 像 Claude 这样的大语言模型（LLM）可以被赋予工具定义，并期望输出符合 JSON 模式的调用。Pi 是一个使用自定义编辑工具的编码工具链；Claude Code 有其内置的编辑工具。新模型可能通过强化学习训练，倾向于 Claude Code 的内部工具格式，导致在使用不同模式时虚构字段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/">Better Models: Worse Tools | Armin Ronacher's Thoughts and ...</a></li>
<li><a href="https://github.com/earendil-works/pi/issues/6278">New Claude models work poorly with the current Pi 's edit tool , failing...</a></li>
<li><a href="https://chatforest.com/builders-log/opus-4-8-sonnet-5-tool-schema-hallucination-strict-mode-fix-builder-guide/">Better Models, Worse Tools: Opus 4.8 and Sonnet 5 Hallucinate ...</a></li>

</ul>
</details>

**社区讨论**: 问题追踪器（GitHub issue #6278）上的社区讨论显示，开发者确认了该问题并分享了额外字段的示例。一些用户建议启用严格模式作为变通方案，而另一些用户则争论第三方工具是否应适应模型特定的怪癖。

**标签**: `#LLM`, `#tool calling`, `#AI reliability`, `#Claude`, `#regression`

---

<a id="item-6"></a>
## [能力门控：基于内部置信信号控制工具使用](https://www.reddit.com/r/MachineLearning/comments/1unw5un/competence_gate_gating_tooluse_on_a_small_models/) ⭐️ 8.0/10

一个 10MB 的 LoRA 适配器，通过内部置信信号控制 Qwen3.5-4B 的工具使用，提升了错误检测能力并减少了幻觉。它可在 Apple Silicon 上通过 MLX 本地运行，也可通过 GGUF 在 llama.cpp/Ollama 上运行。 该方法解决了小型语言模型的一个关键局限：无法准确表达置信度，导致过度自信的错误回答。通过基于内部信号控制工具使用，它减少了幻觉，并保护隐私数据不被泄露到公共搜索引擎。 该门控在错误检测上比基础模型的工具调用提升了 0.46 的 d′值，门控标记而基础模型未标记的案例中 87%确实是错误答案。双信号版本将发送到公共搜索的私人查询从 22%降低到 10%。

reddit · r/MachineLearning · /u/Synthium- · 7月5日 07:49

**背景**: LoRA（低秩适应）是一种参数高效的微调方法，向冻结的基础模型添加小型可训练适配器，以最小的开销实现任务特定定制。内部置信信号指模型隐藏状态激活中与其确定性相关的信号，这些信号比模型口头表达的置信度更可靠。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/learn/llm-course/chapter11/4">LoRA (Low-Rank Adaptation) · Hugging Face</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-4B">Qwen/Qwen3.5-4B · Hugging Face</a></li>
<li><a href="https://arxiv.org/abs/2604.22271">[2604.22271] How LLMs Detect and Correct Their Own Errors ...</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#LLM`, `#tool use`, `#confidence calibration`, `#open source`

---

<a id="item-7"></a>
## [USAF：在消费级 GPU 上对 MoE 模型进行稀疏微调](https://www.reddit.com/r/MachineLearning/comments/1unl62q/if_your_gpu_can_run_inference_it_should_be_able/) ⭐️ 8.0/10

一种名为 USAF（超稀疏自适应微调）的新开源方法，使得之前只能运行推理的 GPU 也能对混合专家（MoE）模型进行微调，已在 12GB AMD RX 6750 XT 上使用 Qwen3-30B-A3B 得到验证。 这一突破大幅降低了微调大型 MoE 模型的硬件门槛，使拥有消费级 GPU 的研究人员和爱好者能够定制最先进的模型，而无需昂贵的云或企业级硬件。 USAF 在 12GB GPU 上仅训练 48 亿参数中的 2600 万（稀疏专家权重和路由器），而全量微调需要超过 120GB。它是唯一能在 AMD GPU 上工作的方法，也是唯一同时训练专家权重和路由器的方法。

reddit · r/MachineLearning · /u/tsuyu122 · 7月4日 21:56

**背景**: 混合专家（MoE）模型使用多个由路由器激活的专门子网络（专家），从而在降低推理成本的同时实现大模型容量。然而，微调此类模型通常需要巨大的 GPU 内存，因为所有参数都会被更新。像 USAF 这样的稀疏微调方法仅更新一小部分参数，从而大幅降低内存需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/tsuyu122/usaf/blob/master/README.md">usaf/README.md at master · tsuyu122/usaf · GitHub</a></li>
<li><a href="https://github.com/tsuyu122/usaf/blob/master">GitHub - tsuyu122/usaf</a></li>

</ul>
</details>

**标签**: `#fine-tuning`, `#MoE`, `#sparse training`, `#open source`, `#GPU`

---

<a id="item-8"></a>
## [iOS 27 将推出 Trust Insights 反诈功能](https://www.cultofmac.com/news/ios-27-trust-insights-feature) ⭐️ 8.0/10

Apple 宣布为 iOS 27 推出 Trust Insights，这是一个新的设备端反诈框架，通过分析用户操作模式、时机、上下文和传感器数据，检测被诈骗分子诱导的转账或改账户等行为。 这标志着移动设备主动防诈迈出重要一步，利用保护隐私的设备端 AI 来保护用户免受社会工程诈骗，同时不泄露个人数据。 该功能不会读取信息、邮件或照片内容；原始数据会立即删除，仅向服务器发送单一输出值。开发者需主动接入才能将 Trust Insights 集成到应用中。

telegram · zaihuapd · 7月4日 14:30

**背景**: 社会工程诈骗（诈骗分子诱骗用户进行转账或更改账户凭证等操作）日益猖獗。传统的反诈措施通常依赖服务器端分析或用户举报，往往为时已晚。Trust Insights 利用设备端机器学习实时检测可疑行为，在用户完成诈骗者要求的操作前增加一层保护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=jY-_rqz_VEM">WWDC26: Meet Trust Insights | Apple - YouTube</a></li>
<li><a href="https://www.ithinkdiff.com/ios-27-trust-insights-scam-detection-framework/">iOS 27 Adds Trust Insights to Detect Scams Before They Happen</a></li>
<li><a href="https://www.newsy-today.com/real-time-social-engineering-detection-how-trust-insights-stops-fraud-before-it-starts/">Real-Time Social Engineering Detection: How Trust Insights Stops...</a></li>

</ul>
</details>

**标签**: `#iOS`, `#security`, `#anti-fraud`, `#privacy`, `#Apple`

---

<a id="item-9"></a>
## [卫报调查：OpenAI 从未实地考察英国星际之门核心选址](https://www.theguardian.com/technology/2026/jul/04/openai-apparent-failure-visit-key-site-questions-stargate-uk-project) ⭐️ 8.0/10

《卫报》调查发现，OpenAI 从未实地造访位于北泰恩赛德 Cobalt Park 的拟建数据中心选址，当地官员也从未与 OpenAI 或其合作伙伴 Nscale 会面。该项目于 2025 年 9 月作为英美 AI 合作旗舰工程高调宣布，但已于 2026 年 4 月因监管和能源成本问题暂停。 调查结果表明，300 亿美元的 Stargate UK 承诺可能只是一场公关噱头，而非真实投资，这削弱了人们对重大 AI 基础设施公告的信任，并引发了对政府科技合作透明度的质疑。 Stargate UK 项目于 2025 年 9 月宣布，合作伙伴包括 Nvidia 和 Nscale，计划在英格兰东北部建设大型数据中心。该项目于 2026 年 4 月暂停，当地保守党议员表示项目落地“看起来极不可能”。

telegram · zaihuapd · 7月5日 05:09

**背景**: Stargate UK 是 OpenAI 全球 Stargate 计划的一部分，旨在建设大规模 AI 基础设施。该项目被宣传为英国 AI 机遇行动计划的关键组成部分，承诺为敏感 AI 工作负载提供本地算力。Cobalt Park 是英国最大的商业园区之一，但 OpenAI 从未派代表前往该选址。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-stargate-uk/">Introducing Stargate UK - OpenAI</a></li>
<li><a href="https://www.bbc.com/news/articles/clyd032ej70o">OpenAI pauses UK data centre deal over energy costs and ... - BBC</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Stargate`, `#AI infrastructure`, `#investigative journalism`, `#UK`

---

<a id="item-10"></a>
## [复旦期末考：学生出题难倒 AI，仅 4 人得零分](https://mp.weixin.qq.com/s/d53O-6mVFZqMa_Sti1yEPw) ⭐️ 8.0/10

复旦大学“数据挖掘技术”课程将期末考试改为“人考 AI”：51 名学生各出 10 道有唯一答案的计算题来难倒三个 AI 模型，结果仅有 4 人能让任一模型得零分，最强模型 Claude 未被完全考倒。 这种创新考核方式将重点从死记硬背转向评估 AI 输出，反映了 AI 能力提升下教育改革的必要性。它凸显了一种新范式：学生学习如何指挥和评判 AI，为 AI 融合的职场做好准备。 考试涉及三个未具名的 AI 模型，其中 Claude 最为稳健。全班平均分 85.7 分（满分 100），意味着大多数学生成功在某道题上难倒了至少一个模型，但只有四人让某个模型整张试卷得零分。

telegram · zaihuapd · 7月5日 08:40

**背景**: 随着 AI 能轻松解决传统算法和记忆类问题，这类考试正变得过时。由肖仰华教授讲授的这门课程代表了向培养学生批判性思维、评估能力和创造性解决问题的转变——这些是 AI 难以复制的技能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/overview">Models overview - Claude Platform Docs</a></li>
<li><a href="https://www.science.org/doi/10.1126/science.aec5115">Generative AI use and misuse call for assessment reform in higher education | Science</a></li>
<li><a href="https://www.unesco.org/en/articles/whats-worth-measuring-future-assessment-ai-age">What's worth measuring? The future of assessment in the AI age</a></li>

</ul>
</details>

**标签**: `#AI in Education`, `#Assessment Reform`, `#LLM Evaluation`, `#Pedagogy`, `#AI Safety`

---