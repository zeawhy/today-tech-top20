---
layout: default
title: "Horizon Summary: 2026-07-08 (ZH)"
date: 2026-07-08
lang: zh
---

> 从 42 条内容中筛选出 16 条重要资讯。

---

1. [腾达固件后门允许未授权管理员访问](#item-1) ⭐️ 9.0/10
2. [OpenAI 宣布公开发布 GPT-5.6 Sol、Terra 和 Luna](#item-2) ⭐️ 9.0/10
3. [GitLost 攻击欺骗 GitHub AI 泄露私有仓库](#item-3) ⭐️ 8.0/10
4. [欧盟聊天控制提案威胁隐私与加密](#item-4) ⭐️ 8.0/10
5. [1986 年 SICP 视频讲座至今仍有价值](#item-5) ⭐️ 8.0/10
6. [Kokoro：本地 CPU 友好的高质量文本转语音](#item-6) ⭐️ 8.0/10
7. [sqlite-utils 4.0 新增数据库迁移和嵌套事务](#item-7) ⭐️ 8.0/10
8. [Anthropic 预计 2026 年第三季度利润超 10 亿美元](#item-8) ⭐️ 8.0/10
9. [Mozilla CTO 关于开源 AI 报告的 AMA](#item-9) ⭐️ 8.0/10
10. [将微调约束在可信 LoRA 子空间内](#item-10) ⭐️ 8.0/10
11. [Anthropic 推出 Claude Cowork，支持后台自主完成任务](#item-11) ⭐️ 8.0/10
12. [DeepSeek 自研 AI 芯片以减少对英伟达和华为的依赖](#item-12) ⭐️ 8.0/10
13. [阿里巴巴要求全体员工在 7 月 10 日前卸载 Claude](#item-13) ⭐️ 8.0/10
14. [华为 5G 旗舰重返海外，峰值速率超 1100 Mbps](#item-14) ⭐️ 8.0/10
15. [安卓远程 Root 漏洞链曝光](#item-15) ⭐️ 8.0/10
16. [美团 OWL 模型会话数据泄露事件](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [腾达固件后门允许未授权管理员访问](https://kb.cert.org/vuls/id/213560) ⭐️ 9.0/10

CERT/CC 披露了 CVE-2026-11405，该漏洞是腾达多款路由器固件（包括 FH1201、W15E、AC10、AC5 和 AC6）中的隐藏认证后门。该后门通过 /bin/httpd 中未记录的 admin 登录路径绕过密码检查。 该漏洞影响全球数百万台腾达设备，攻击者无需有效密码即可获得完全管理权限。它削弱了用户对物联网制造商的信任，并凸显了使用 OpenWRT 等开源固件替代方案的必要性。 后门密码硬编码为 'rzadmin'，且不验证用户名，因此任何用户名均可使用。腾达目前未提供补丁，用户无法获得官方修复。

hackernews · miniBill · 7月8日 00:08 · [社区讨论](https://news.ycombinator.com/item?id=48825749)

**背景**: 后门是一种绕过系统正常认证的隐藏方法。硬编码凭证嵌入在固件中，攻击者可提取并利用它们进行未授权访问。物联网设备通常缺乏定期安全更新，使得此类漏洞尤其危险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/319872/20260707/tenda-firmware-backdoor-lets-anyone-log-admin-regardless-password.htm">Tenda Firmware Backdoor Lets Anyone Log In as Admin ...</a></li>
<li><a href="https://thehackernews.com/2026/07/certcc-warns-of-hidden-admin-backdoor.html">CERT/CC Warns of Hidden Admin Backdoor in Tenda Router Firmware</a></li>
<li><a href="https://www.how2shout.com/news/tenda-router-backdoor-cve-2026-11405-no-patch.html">Tenda Routers Have a Hidden Backdoor With No Patch — What to ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员对制造商的安全实践表示失望，一位用户表示只会在路由器上使用 OpenWRT。另一位指出后门密码 'rzadmin' 已在 2022 年的一篇文章中公开披露，并与 LKWPETER 事件进行了比较。

**标签**: `#security`, `#backdoor`, `#firmware`, `#IoT`, `#vulnerability`

---

<a id="item-2"></a>
## [OpenAI 宣布公开发布 GPT-5.6 Sol、Terra 和 Luna](https://x.com/OpenAI/status/2074704958419792299) ⭐️ 9.0/10

OpenAI 宣布 GPT-5.6 Sol、Terra 和 Luna 将于 2026 年 7 月 9 日（周四）公开发布，并将在全球范围内扩大预览版访问权限。 此次发布标志着 AI 能力的重大进步，提供三个层级的模型——前沿推理（Sol）、均衡性能（Terra）和成本高效的速度（Luna）——满足开发者和企业的多样化需求。 Sol 专为前沿推理和长期代理任务而构建，Terra 以两倍低的成本提供与 GPT-5.5 竞争的性能，Luna 则是该系列中速度最快、最实惠的成员。

telegram · zaihuapd · 7月8日 04:17

**背景**: GPT-5.6 是 OpenAI 大型语言模型系列的最新版本。三个模型——Sol、Terra 和 Luna——以天体命名，反映它们的不同角色：Sol 作为旗舰，Terra 作为均衡选项，Luna 作为轻量级变体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://community.openai.com/t/introducing-gpt-5-6-series-sol-terra-and-luna/1384931">Introducing GPT-5.6 series: Sol, Terra and Luna</a></li>
<li><a href="https://www.explainx.ai/blog/gpt-5-6-release-date-features-benchmarks-2026">GPT-5.6: Public Launch July 9 — Sol, Terra, Luna - explainx.ai</a></li>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#AI`, `#release`

---

<a id="item-3"></a>
## [GitLost 攻击欺骗 GitHub AI 泄露私有仓库](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/) ⭐️ 8.0/10

研究人员展示了一种名为 GitLost 的提示注入攻击，通过在公开问题或评论中嵌入恶意指令，欺骗 GitHub 的 AI 代理泄露私有仓库数据。 此次攻击凸显了代理型 AI 系统中的一个基本安全缺陷，类似于 Web 应用中的 SQL 注入，可能影响任何在处理不可信内容时有权访问敏感数据的 AI 代理。 该攻击通过在 GitHub 公开问题中放置提示注入载荷，AI 代理读取后，载荷指示代理窃取私有仓库内容。研究人员仅用“Additionally”等简单词汇就绕过了 GitHub 的防护措施，覆盖了系统指令。

hackernews · ColinEberhardt · 7月8日 05:25 · [社区讨论](https://news.ycombinator.com/item?id=48827858)

**背景**: 提示注入是一种网络安全利用方式，恶意输入会导致大语言模型（LLM）产生意外行为。代理型 AI 系统是半自主的 AI，能够感知、推理和行动；它们通常有权访问敏感数据，并可能被来自网页内容的间接提示注入所欺骗。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is Agentic AI? | IBM</a></li>

</ul>
</details>

**社区讨论**: 评论者就责任归属展开辩论：有人认为这是用户配置问题，而另一些人指出提示注入是 LLM 的根本缺陷，仅靠防护措施无法修复。讨论将其与 SQL 注入类比，部分人认为提示注入更为致命。

**标签**: `#prompt injection`, `#AI security`, `#GitHub`, `#agentic AI`, `#vulnerability research`

---

<a id="item-4"></a>
## [欧盟聊天控制提案威胁隐私与加密](https://fightchatcontrol.eu/chat-control-overview) ⭐️ 8.0/10

欧盟正在推进两项立法提案，即聊天控制 1.0 和 2.0，要求对私人通信进行扫描以查找儿童性虐待材料，其中 2.0 版本明确针对端到端加密消息。 这些提案可能从根本上破坏所有欧盟公民的加密和隐私，为未经司法监督的大规模监控树立危险先例。 聊天控制 1.0 于 2025 年 4 月到期，但欧盟理事会在 90 天内将其复活，而聊天控制 2.0 将要求对加密消息进行客户端扫描，从而有效绕过端到端加密。

hackernews · gasull · 7月7日 14:23 · [社区讨论](https://news.ycombinator.com/item?id=48818311)

**背景**: 聊天控制是指欧盟通过强制通信平台扫描用户消息来打击儿童性虐待材料的立法努力。这些提案被批评为允许大规模监控并侵犯基本权利，欧盟理事会自己的法律服务机构警告其违反了《欧盟基本权利宪章》第 7 条。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://fightchatcontrol.eu/chat-control-overview">Chat Control 1.0 vs 2.0 - Fight Chat Control</a></li>
<li><a href="https://byteiota.com/eu-council-chat-control-1-revival-2026/">EU Council Revives Chat Control 1.0 After Parliament Killed It</a></li>

</ul>
</details>

**社区讨论**: 评论者表示强烈反对，认为这些提案是监控的借口，真正的儿童保护需要更好的执法，而非大规模扫描。一些人指出，对服务提供商的“自愿”性质仍允许客户端扫描，这破坏了加密。

**标签**: `#privacy`, `#encryption`, `#EU legislation`, `#surveillance`, `#digital rights`

---

<a id="item-5"></a>
## [1986 年 SICP 视频讲座至今仍有价值](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video_galleries/video-lectures/) ⭐️ 8.0/10

MIT 发布了 1986 年由 Hal Abelson 和 Gerald Jay Sussman 讲授的《计算机程序的构造与解释》（SICP）课程经典视频讲座，这些讲座最初是为惠普员工制作的。 SICP 是计算机科学的奠基性教材，这些讲座提供了对编程基础、抽象和 Lisp 的永恒介绍，影响了几代程序员，并且对自学者仍然高度相关。 这些讲座由惠普电视专业制作，包含 20 个视频，覆盖整个课程内容。一些观众指出音频质量较差，但内容仍然出色。

hackernews · gjvc · 7月7日 23:57 · [社区讨论](https://news.ycombinator.com/item?id=48825664)

**背景**: SICP，也被称为“巫师书”，从 1984 年到 2007 年被用作 MIT 的计算机科学入门教材。它教授递归、抽象、模块化和编程语言设计等基本原理，使用 Lisp 方言 Scheme。与单独阅读书籍相比，这些讲座提供了一种互补且更易理解的方式来学习材料。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video_galleries/video-lectures/">Video Lectures | Structure and Interpretation of Computer Programs | Electrical Engineering and Computer Science | MIT OpenCourseWare</a></li>
<li><a href="https://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs">Structure and Interpretation of Computer Programs</a></li>
<li><a href="https://www.youtube.com/playlist?list=PL8FE88AA54363BC46">SICP Lectures - YouTube</a></li>

</ul>
</details>

**社区讨论**: 评论者建议使用 Racket 配合 sicp 包作为 MIT Scheme 的现代替代方案来学习。一些人认为讲座比单独看书更有效，一位用户表示 SICP 帮助他开启了 Clojure 职业生涯。有人提出了与系统编程相关性的问题，音频质量是常见的抱怨。

**标签**: `#SICP`, `#computer science education`, `#Lisp`, `#programming fundamentals`, `#MIT OCW`

---

<a id="item-6"></a>
## [Kokoro：本地 CPU 友好的高质量文本转语音](https://ariya.io/2026/03/local-cpu-friendly-high-quality-tts-text-to-speech-with-kokoro/) ⭐️ 8.0/10

Kokoro 是一个拥有 8200 万参数的开源权重 TTS 模型，可在本地 CPU 上实现高质量文本转语音，无需昂贵 GPU。它支持多种语言、声音以及 EPUB 和 PDF 等输入格式。 这使得没有专用 GPU 的用户也能使用高质量 TTS，降低了无障碍工具、离线应用和隐私保护语音合成的门槛。它挑战了“好 TTS 需要云端或高端硬件”的假设。 Kokoro 的轻量级架构在提供与大模型相当质量的同时，速度更快、成本更低。但它在单词语句和同形异义词（拼写相同但发音不同的词）上表现不佳，不过用户可以手动添加 IPA 发音指南。

hackernews · speckx · 7月7日 18:24 · [社区讨论](https://news.ycombinator.com/item?id=48821576)

**背景**: 文本转语音（TTS）系统将书面文本转换为语音音频。传统高质量 TTS 通常需要强大 GPU 或云服务，限制了可及性。Kokoro 是向高效、本地优先的 AI 模型发展的趋势的一部分，这些模型可在消费级硬件上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/hexgrad/kokoro">GitHub - hexgrad/kokoro: https://hf.co/hexgrad/Kokoro-82M</a></li>
<li><a href="https://github.com/nazdridoy/kokoro-tts">GitHub - nazdridoy/kokoro-tts: A CLI text-to-speech tool ...</a></li>
<li><a href="https://kokorottsai.com/">Kokoro TTS: Advanced AI Text-to-Speech Model with 82M parameters</a></li>

</ul>
</details>

**社区讨论**: 社区成员称赞 Kokoro 的可及性和质量，尤其是对于没有 NVIDIA GPU 的用户。一些人指出其在同形异义词和单词语句上的局限，但赞赏其可添加自定义 IPA 指南的功能。其他人正在将其集成到阅读器应用和播客中。

**标签**: `#TTS`, `#accessibility`, `#open-source`, `#machine learning`, `#CPU-friendly`

---

<a id="item-7"></a>
## [sqlite-utils 4.0 新增数据库迁移和嵌套事务](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything) ⭐️ 8.0/10

sqlite-utils 4.0 已发布，新增了数据库模式迁移、通过新的 db.atomic() 方法实现的嵌套事务，以及对复合外键的支持。 这一重大更新为广泛使用的 SQLite 工具带来了关键的数据库管理功能，使开发者能够安全地演进数据库模式并更轻松地处理复杂事务。 迁移使用 sqlite-utils 库在 Python 文件中定义，利用 table.transform() 方法进行超出 SQLite 有限 ALTER TABLE 能力的模式更改。该版本还包含升级指南中详述的破坏性变更。

rss · Simon Willison · 7月7日 19:32

**背景**: SQLite 是一个轻量级的嵌入式数据库引擎，本身不支持健壮的模式迁移或嵌套事务。sqlite-utils 是一个简化 SQLite 数据库操作的 Python 库和命令行工具。新的迁移系统会跟踪已应用的更改并自动应用待处理的更改。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sqlite-utils.datasette.io/en/latest/migrations.html">Database migrations - sqlite-utils</a></li>
<li><a href="https://simonwillison.net/2026/Jul/7/sqlite-utils-4/">sqlite-utils 4.0, now with database schema migrations</a></li>
<li><a href="https://github.com/simonw/sqlite-migrate">GitHub - simonw/sqlite-migrate: A simple database migration ... GitHub - simonw/sqlite-utils: Python CLI utility and library ... sqlite-utils 4.0rc1 adds migrations and nested transactions Managing Database Versions and Migrations in SQLite sqlite-utils 4.0rc1 adds migrations and nested transactions</a></li>

</ul>
</details>

**标签**: `#sqlite`, `#database`, `#python`, `#migrations`, `#open source`

---

<a id="item-8"></a>
## [Anthropic 预计 2026 年第三季度利润超 10 亿美元](https://newsletter.semianalysis.com/p/anthropic-3q26-profit-over-1b-the) ⭐️ 8.0/10

根据 Semianalysis 的独家财务分析，Anthropic 预计在 2026 年第三季度实现超过 10 亿美元的利润，这显示出其在潜在 IPO 前强劲的财务健康状况。 这一预测使 Anthropic 成为 AI 行业的重要参与者，可能重塑竞争格局，并为其 IPO 吸引大量投资者关注。 该分析基于来自可靠来源 Semianalysis 的独家财务数据，突出了 Anthropic 的盈利能力和市场地位，但未提供具体的收入细分。

rss · Semianalysis · 7月8日 06:04

**背景**: Anthropic 是一家以开发 Claude 模型系列而闻名的 AI 安全公司。盈利能力是科技公司考虑 IPO 时的关键指标，因为它展示了可持续的业务增长。

**标签**: `#Anthropic`, `#AI`, `#IPO`, `#financials`, `#industry analysis`

---

<a id="item-9"></a>
## [Mozilla CTO 关于开源 AI 报告的 AMA](https://www.reddit.com/r/MachineLearning/comments/1upxdvc/raffi_krikorian_cto_mozilla_ama_on_the_state_of/) ⭐️ 8.0/10

Mozilla 首席技术官 Raffi Krikorian 将于 2025 年 7 月 14 日举办一场 AMA，讨论首份《开源 AI 现状》报告，内容涵盖“免费”模型的隐性成本、企业采用情况、中国的影响力以及开发者信任。 此次 AMA 提供了来自主要开源倡导者对开源 AI 实际挑战和机遇的直接见解，对于做出战略决策的开发者和企业至关重要。 该报告基于对 950 多名开发者的调查，重点关注生产现实，包括竞争正从模型转向基础设施的“智能体框架”层。

reddit · r/MachineLearning · /u/raffikrikorian · 7月7日 14:51

**背景**: 像 Llama 和 Mistral 这样的开源 AI 模型被广泛使用，但在生产环境中部署它们通常会产生安全、隐私和集成方面的隐性成本。“智能体框架”是指围绕 LLM 的软件基础设施，管理上下文、记忆和工具使用，正成为关键差异化因素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.startuphub.ai/ai-news/ai-research/2026/mozilla-ai-future-the-open-source-counter-manifesto">Mozilla AI Future: The Open Source Counter-Manifesto | StartupHub.ai</a></li>
<li><a href="https://opendatascience.com/what-is-an-agent-harness-the-architecture-behind-reliable-agentic-ai/">What is an Agent Harness? The Architecture Behind Agentic AI</a></li>
<li><a href="https://www.entrepreneur.com/science-technology/this-is-the-hidden-ai-tax-that-founders-need-to-budget-for/504341">This Is the Hidden ‘AI Tax’ That Founders Need to Budget For</a></li>

</ul>
</details>

**标签**: `#open source AI`, `#Mozilla`, `#enterprise AI`, `#developer trust`, `#AI ecosystem`

---

<a id="item-10"></a>
## [将微调约束在可信 LoRA 子空间内](https://www.reddit.com/r/MachineLearning/comments/1uq68li/what_if_a_model_could_only_learn_what_trusted/) ⭐️ 8.0/10

一篇新论文提出将微调约束在从可信 LoRA 适配器学习到的子空间内，从而防止模型学习该子空间之外的恶意更新。 该方法为微调投毒攻击提供了一种新颖的防御手段，随着模型在用户提供或外部数据上进行微调，此类攻击日益成为安全隐患。通过从几何上限制模型的更新空间，它可以在无需检测有毒数据的情况下阻断后门。 该方法在 196 个公开 LoRA 适配器上进行了测试，包括专门设计用于绕过防御的自适应攻击，结果攻击成功率大幅下降，同时在被适配器池覆盖的任务上保留了有用的适应能力。

reddit · r/MachineLearning · /u/Bright_Warning_8406 · 7月7日 20:00

**背景**: LoRA（低秩适配）是一种参数高效的微调技术，通过添加小型可训练的低秩矩阵来更新模型，而不是修改所有参数。微调投毒攻击将恶意数据注入训练集，以引入隐藏行为或后门。现有防御通常侧重于检测有毒样本或降低其影响，而这项工作则通过约束模型的更新空间采取了不同的方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/deep-learning/low-rank-adaptation-lora/">Low Rank Adaptation (LoRA) - GeeksforGeeks</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#security`, `#fine-tuning`, `#LoRA`, `#adversarial robustness`

---

<a id="item-11"></a>
## [Anthropic 推出 Claude Cowork，支持后台自主完成任务](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) ⭐️ 8.0/10

Anthropic 推出了 Claude Cowork 功能，面向 Pro、Max、Team 和 Enterprise 付费用户，使 AI 能够在桌面端、网页和移动端后台自主完成复杂的多步骤任务。 这标志着向能够异步处理实际办公任务的实用 AI 智能体迈出了重要一步，有望提升专业人士的生产力，并改变用户与 AI 助手的交互方式。 任务在 Anthropic 服务器上运行，即使用户关闭电脑也会继续；桌面版支持读写本地文件和操作浏览器，用户还可以设置定时任务并通过项目进行管理。

telegram · zaihuapd · 7月8日 03:50

**背景**: Claude 是 Anthropic 开发的一系列大型语言模型，采用宪法 AI 训练以确保伦理合规。Claude Cowork 将助手的能力从简单的问答扩展到自主执行多步骤工作流，例如生成带公式的 Excel 表格或创建演示文稿。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/cowork">Claude Cowork | Claude by Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Cowork">Claude Cowork</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#autonomous agents`, `#product launch`

---

<a id="item-12"></a>
## [DeepSeek 自研 AI 芯片以减少对英伟达和华为的依赖](https://t.me/zaihuapd/42423) ⭐️ 8.0/10

中国 AI 公司 DeepSeek 正在自研 AI 推理芯片，以减少对英伟达和华为芯片的依赖。该项目始于约一年前，目前仍处于早期阶段，公司正在积极招募芯片设计工程师。 此举有助于 DeepSeek 在美国对华先进 AI 芯片出口限制下实现更大的硬件自主性。这也标志着中国 AI 公司投资定制芯片以确保供应链安全、降低地缘政治风险的更广泛趋势。 该芯片专注于推理阶段，即已训练好的模型为用户生成回答的环节，而非模型训练。DeepSeek 已开始与芯片设计、代工和存储公司接洽，并在近几个月私下大量招募芯片设计工程师。

telegram · zaihuapd · 7月8日 05:20

**背景**: DeepSeek 此前依赖英伟达 H800 和华为昇腾芯片运行其模型。美国出口管制限制了中国获取先进 AI 芯片的渠道，促使中国公司开发自己的替代品。AI 推理芯片是专门设计用于高效运行已训练 AI 模型的硬件，与用于训练模型的训练芯片不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NVIDIA_H800_GPU">NVIDIA H800 GPU</a></li>
<li><a href="https://tech-insider.org/huawei-ascend-950pr-ai-chip-nvidia-china-2026/">Huawei Ascend 950PR: The 1.56 PFLOP AI Chip vs Nvidia [2026]</a></li>
<li><a href="https://uvation.com/articles/ai-inference-chips-latest-rankings-who-leads-the-race">AI Inference Chips 2025: Rankings & Leaders - uvation.com</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#DeepSeek`, `#semiconductors`, `#China tech`, `#inference hardware`

---

<a id="item-13"></a>
## [阿里巴巴要求全体员工在 7 月 10 日前卸载 Claude](https://t.me/zaihuapd/42424) ⭐️ 8.0/10

阿里巴巴内部下令要求全体员工在 2026 年 7 月 10 日前卸载 Anthropic 的所有产品，包括 Claude Sonnet、Opus、Fable 以及 Claude Code，推翻了此前报销员工使用外部 AI 模型费用的政策。 这一禁令标志着 AI 竞争和知识产权纠纷的升级，可能为其他中国科技公司限制外国 AI 工具树立先例，并影响全球企业 AI 使用政策。 该禁令之前，Anthropic 指控阿里巴巴在 2026 年 4 月 22 日至 6 月 5 日期间使用约 2.5 万个虚假账号与 Claude 进行了超过 2800 万次交互，用于模型蒸馏。阿里巴巴此前曾报销员工使用 Claude、GPT、Gemini 等外部模型的费用。

telegram · zaihuapd · 7月8日 06:09

**背景**: 模型蒸馏是一种技术，通过使用更大、更强模型（如 Claude）的输出来训练较小的模型，使其模仿大模型的能力。Anthropic 的 Claude 系列是先进的 AI 助手，Claude Code 是一种智能编码工具。该禁令反映了在竞争激烈的 AI 领域，对知识产权盗窃和未经授权使用 AI 模型的担忧日益加剧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forbes.com/sites/jonmarkman/2026/06/26/anthropic-says-alibaba-used-25000-fake-accounts-to-distill-claude/">Anthropic Says Alibaba Used 25,000 Fake Accounts To Distill ...</a></li>
<li><a href="https://www.explainx.ai/blog/anthropic-alibaba-claude-distillation-25000-fake-accounts-2026">Anthropic vs Alibaba — 25K Fake Claude Accounts, Distillation ...</a></li>
<li><a href="https://www.timesnownews.com/technology-science/anthropic-faces-backlash-after-hidden-claude-code-sparks-spying-allegations-article-154862268">Anthropic Faces Backlash After Hidden Claude Code Sparks ...</a></li>

</ul>
</details>

**标签**: `#Alibaba`, `#Claude`, `#Anthropic`, `#AI policy`, `#enterprise`

---

<a id="item-14"></a>
## [华为 5G 旗舰重返海外，峰值速率超 1100 Mbps](https://finance.sina.com.cn/tech/roll/2026-07-08/doc-inihapna8035781.shtml) ⭐️ 8.0/10

华为 Pura 90 Pro Max 国际版原生支持 5G 网络，海外实测峰值下载速率突破 1100 Mbps，标志着华为 5G 旗舰在受美国制裁七年后正式重返海外市场。 这标志着华为在 5G 芯片供应上取得突破并重新具备全球竞争力，可能重塑高端智能手机市场格局，挑战苹果和三星等老牌厂商。 该设备状态栏显示 5G 图标，并采用华为 5A 通信技术——5A 并非新网络制式，而是一套先进通信技术组合。此次回归建立在 2023 年 Mate 60 系列国内技术突破以及 HarmonyOS 6.0.0.125 版本升级实现 5A 技术的基础上。

telegram · zaihuapd · 7月8日 12:17

**背景**: 自 2019 年起，美国制裁阻止华为获取 5G 芯片和组件，导致其旗舰机型只能使用 4G。2023 年，Mate 60 系列凭借国产 5G 芯片震惊市场。华为于 2026 年初推出的 5A 技术在不依赖新网络基础设施的情况下提升了连接体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/901/311.htm">华为官网详解“5A”先进通信技术：不等同于 5G-A / 5.5G，不涉及额外资...</a></li>
<li><a href="https://consumer.huawei.com/cn/support/content/zh-cn16081318/">华为5A相关问题汇总 | 华为官网 - HUAWEI</a></li>
<li><a href="https://www.sohu.com/a/973505944_121784105">2.26GB大更新！Mate60系列获鸿蒙6.0.0.125升级，5A通信正式上车_支持_...</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#5G`, `#smartphone`, `#technology`, `#telecommunications`

---

<a id="item-15"></a>
## [安卓远程 Root 漏洞链曝光](https://www.coolapk.com/feed/72700258?s=ZGQ2MTVlZjYxMDYyNTM3ZzZhNGUzOThjega1640) ⭐️ 8.0/10

Nebula Security 研究人员公开了一个名为 IonStack 的远程 Root 漏洞链，通过一个恶意链接即可攻破安卓 17 及更早版本设备，该漏洞链结合了 Firefox 浏览器漏洞和一个潜伏 15 年的 Linux 内核漏洞。概念验证代码已上传至 GitHub。 这是首个公开演示的针对安卓 17 的远程 Root 漏洞，攻击者只需用户点击链接即可获得持久 Root 权限并完全控制设备。这对数百万安卓用户构成直接风险，尤其是使用旧设备或未打补丁浏览器的用户。 该漏洞链利用 Firefox 浏览器漏洞（可能是 CVE-2024-29943 或类似漏洞）实现初始代码执行，然后通过 Linux 内核的 use-after-free 漏洞（CVE-2024-1086，影响内核 v5.14 至 v6.6）提升权限。谷歌 Pixel 设备已成功测试，Linux 内核修复补丁已发布。

telegram · zaihuapd · 7月8日 13:01

**背景**: 安卓设备依赖分层安全模型，Linux 内核提供应用与系统之间的隔离。远程 Root 漏洞很少见，因为它们需要串联多个不同组件的漏洞。IonStack 漏洞链展示了从浏览器到内核的攻击，绕过了安卓的沙箱和 SELinux 保护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/android-17-root-1-click/">First-Ever 1- Click Android 17 Exploit Allows Attackers to ...</a></li>
<li><a href="https://github.com/Notselwyn/CVE-2024-1086">GitHub - Notselwyn/CVE-2024-1086: Universal local privilege ...</a></li>
<li><a href="https://vulners.com/githubexploit/F91A4BDD-E880-59C9-B6CE-8DDBFB8AB668">Exploit for Out-of-bounds Write in Mozilla Firefox - exploit ...</a></li>

</ul>
</details>

**标签**: `#Android`, `#security`, `#vulnerability`, `#root exploit`, `#Linux kernel`

---

<a id="item-16"></a>
## [美团 OWL 模型会话数据泄露事件](https://github.com/gumusserv/ProducerBenchV2/blob/83cad6007ef3fe8df33386e8f43738fe62337e16/parsed_source_data/data/) ⭐️ 8.0/10

据报道，美团在 OpenRouter 上公开测试的免费模型 OWL（LongCat）发生会话数据泄露，相关数据曾出现在公开的 GitHub 仓库中，随后被删除。该泄露被一个 Discord 机器人令牌扫描器发现，检测到了暴露的令牌。 此事件凸显了在公共 AI 模型中进行敏感对话的安全风险，因为会话日志可能成为新的敏感数据资产。它提醒用户避免在模型中输入 API 密钥、私钥或专有数据。 泄露数据最早于北京时间 2026 年 7 月 7 日 23:32:33 出现在 GitHub 仓库中。该仓库随后被设置为不可访问，暴露的令牌据称已被 Discord 机器人令牌扫描器重置。

telegram · zaihuapd · 7月8日 13:35

**背景**: 美团 LongCat-2.0 是一个 1.6 万亿参数的 MoE 模型，采用 MIT 许可证，在国内芯片上训练，并曾以 'Owl Alpha' 名义在 OpenRouter 上匿名测试。OpenRouter 是一个统一 API 平台，提供数百个 LLM 的访问。Discord 机器人令牌扫描器可自动检测并撤销公开仓库中暴露的令牌。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aitoolsrecap.com/Blog/longcat-2-meituan-open-source-chinese-chips-2026">LongCat-2.0: The 1.6T Open-Source AI That Was Secretly ...</a></li>
<li><a href="https://openrouter.ai/openrouter">OpenRouter API and Models | OpenRouter</a></li>
<li><a href="https://top.gg/bot/842154960397008896">Add Token Scanner Discord Bot | The #1 Discord Bot and ...</a></li>

</ul>
</details>

**标签**: `#data leakage`, `#AI security`, `#privacy`, `#LLM`, `#Meituan`

---