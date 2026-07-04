---
layout: default
title: "Horizon Summary: 2026-07-04 (ZH)"
date: 2026-07-04
lang: zh
---

> 从 48 条内容中筛选出 12 条重要资讯。

---

1. [本地运行 SOTA 大模型指南引发成本讨论](#item-1) ⭐️ 8.0/10
2. [欧盟议会间谍调查成员遭飞马间谍软件入侵](#item-2) ⭐️ 8.0/10
3. [Wordgard：ProseMirror 创建者推出的新富文本编辑器](#item-3) ⭐️ 8.0/10
4. [Ubicloud 倡导 PostgreSQL 使用严格内存过量提交](#item-4) ⭐️ 8.0/10
5. [Current AI 发布开源 AI 差距地图](#item-5) ⭐️ 8.0/10
6. [课程创作者报告收入因 AI 下降超 50%](#item-6) ⭐️ 8.0/10
7. [CDD 仅从 logits 恢复微调数据](#item-7) ⭐️ 8.0/10
8. [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](#item-8) ⭐️ 8.0/10
9. [华为发布 Atlas 350 加速卡，搭载昇腾 950PR，算力达 H20 的 2.87 倍](#item-9) ⭐️ 8.0/10
10. [华为 Mate 80 Pro 游戏能效超越骁龙 8 Gen3](#item-10) ⭐️ 8.0/10
11. [NASA 发射救援卫星拯救老化太空望远镜](#item-11) ⭐️ 8.0/10
12. [腾讯阿图因 AI 在 CyberGym 测试中超越 Mythos](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [本地运行 SOTA 大模型指南引发成本讨论](https://github.com/jamesob/local-llm) ⭐️ 8.0/10

Jamesob 在 GitHub 上发布了一份全面指南，详细介绍了如何构建昂贵的本地设备来运行最先进的大语言模型，包括成本达 4 万美元或更高的配置。 该指南凸显了本地大模型推理的高昂前期成本与用户对隐私、控制权及摆脱云服务依赖的渴望之间的持续矛盾，引发了关于成本效益和可行性的讨论。 指南中的顶级配置包括四块每块 12000 美元的 GPU，总价达 5 万至 5.5 万美元，并依赖量化和剪枝技术将修改后的 GLM-5.2（594B 参数）等模型装入可用显存。

hackernews · livestyle · 7月3日 15:03 · [社区讨论](https://news.ycombinator.com/item?id=48775921)

**背景**: 本地运行大语言模型需要大量硬件资源，尤其是显存，用于加载模型权重和执行推理。量化通过降低模型精度来减少内存占用，而剪枝则移除不重要的参数。基于云的 LLM（如 Claude Opus）以订阅费用提供高性能，但本地设置能提供隐私和离线能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/jamesob/local-llm">GitHub - jamesob/local-llm: Everything I know about running LLMs locally · GitHub</a></li>
<li><a href="https://enji.ai/tech-articles/how-to-switch-from-sota-llms-to-local-oss-llms/">Switching from SOTA to Local OSS LLMs: A Practical Guide</a></li>
<li><a href="https://medium.com/data-science-collective/what-is-the-best-hardware-for-running-local-llms-in-2026-mac-vs-5090-vs-cloud-ff023b660442">What Is The Best Hardware for Running Local LLMs in 2026... | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为，本地设置仍然比云替代方案昂贵得多且质量更低，有人指出 4 万美元足以支付 16.8 年的 Claude Opus 订阅费用。其他人则建议采用中间方案，如 128GB 统一内存系统来运行 DeepSeek V4，并警告量化模型在基准测试之外可能表现不佳。

**标签**: `#LLM`, `#local inference`, `#hardware`, `#cost analysis`, `#open source`

---

<a id="item-2"></a>
## [欧盟议会间谍调查成员遭飞马间谍软件入侵](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

公民实验室调查发现，正在调查间谍软件的欧洲议会议员斯特利奥斯·库洛格卢的 iPhone 在 2022 年和 2023 年至少三次被飞马间谍软件感染。 这表明存在针对欧盟议会议员的协调间谍活动，可能由有权在多个欧洲国家进行监视的国家行为者实施，破坏了民主制度。 2022 年 10 月的首次感染与针对俄罗斯和白俄罗斯流亡记者的飞马行动重叠，表明同一飞马客户跨境操作。同一部手机还包含机密医疗和政府文件。

hackernews · ledoge · 7月3日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: 飞马是由以色列公司 NSO Group 开发的间谍软件，能够通过零点击漏洞远程入侵移动设备。它被多国政府滥用于监视记者、活动家和政治家。公民实验室是多伦多大学的研究小组，专门调查数字威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>
<li><a href="https://citizenlab.ca/">The Citizen Lab - The Citizen Lab</a></li>

</ul>
</details>

**社区讨论**: 评论者争论此次攻击是针对欧盟议会还是希腊国内丑闻，有人指出希腊和其他欧盟国家滥用飞马。还有人质疑欧盟议会缺乏设备分离政策。

**标签**: `#cybersecurity`, `#spyware`, `#Pegasus`, `#EU`, `#espionage`

---

<a id="item-3"></a>
## [Wordgard：ProseMirror 创建者推出的新富文本编辑器](https://wordgard.net/) ⭐️ 8.0/10

Wordgard 是 ProseMirror 创建者 Marijn Haverbeke 发布的一款新的浏览器内富文本编辑器，它提供了一种全新的文档编辑方法，与 ProseMirror 共享概念，但没有升级路径。 这一发布意义重大，因为它来自富文本编辑器领域备受尊敬的创建者，社区正在积极讨论采用没有迁移路径的新编辑器的技术权衡和实际考虑。 Wordgard 与 ProseMirror 共享许多概念，但不向后兼容，这意味着切换需要大量重做。该编辑器专为现代 Web 应用程序设计，强调清晰、语义化的文档模型。

hackernews · indy · 7月3日 08:50 · [社区讨论](https://news.ycombinator.com/item?id=48772573)

**背景**: ProseMirror 是一个经过实战考验的富文本编辑器框架，被 Tiptap 等许多项目使用。它提供了强大的核心，但学习曲线陡峭。由于缺乏 Web 标准，浏览器内富文本编辑器长期以来一直是一个挑战，存在许多解决方案，如 Quill 和 TinyMCE。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prosemirror.net/">ProseMirror</a></li>
<li><a href="https://github.com/prosemirror">ProseMirror · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区对 Wordgard 背后的“为什么”感到好奇，并指出缺乏从 ProseMirror 升级的路径。一些用户对现有编辑器的复杂性表示沮丧，并称赞 Wordgard 的设计，而另一些用户则讨论技术挑战，例如 ProseMirror 的静态类型问题。

**标签**: `#rich-text editor`, `#ProseMirror`, `#web development`, `#open source`, `#WYSIWYG`

---

<a id="item-4"></a>
## [Ubicloud 倡导 PostgreSQL 使用严格内存过量提交](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit) ⭐️ 8.0/10

Ubicloud 发布了一篇博客文章，解释了他们为何对 PostgreSQL 使用严格内存过量提交（vm.overcommit_memory=2）以避免 OOM killer 问题，这是基于他们大规模运营托管 PostgreSQL 的经验。 这很重要，因为 OOM killer 中断是 PostgreSQL 运维人员的常见痛点，严格过量提交提供了一种显著减少这些崩溃的方法，尽管它需要仔细测试，并且可能不适合所有工作负载。 严格过量提交（模式 2）根据 swap + RAM * overcommit_ratio 强制执行 CommitLimit，拒绝超出该限制的分配。Ubicloud 指出，他们最初启用后遇到了故障，但最终发现它有利于稳定性。

hackernews · furkansahin · 7月3日 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48774509)

**背景**: Linux OOM killer 是一种在系统内存耗尽时终止进程的机制。PostgreSQL 可能为查询分配大量内存，因此经常成为目标。内核的默认内存过量提交行为（模式 0 或 1）可能导致过量承诺并随后触发 OOM 终止。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit">PostgreSQL and the OOM Killer: Why We Use Strict Memory ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=48774509">PostgreSQL and the OOM Killer: Why We Use Strict Memory Overcommit | Hacker News</a></li>
<li><a href="https://www.postgresql.org/docs/current/kernel-resources.html">PostgreSQL: Documentation: 18: 18.4. Managing Kernel Resources</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，Linux VM 默认设置被认为有问题，并建议在切换到模式 2 时谨慎，特别是如果已经调整了过量提交比例。Ubicloud 的一位评论者同意技术内容，但认为标题过于强烈，指出严格过量提交在许多场景下可能产生未预料的副作用。

**标签**: `#PostgreSQL`, `#Linux`, `#memory management`, `#OOM killer`, `#database administration`

---

<a id="item-5"></a>
## [Current AI 发布开源 AI 差距地图](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI 是一家于 2025 年 2 月在巴黎人工智能行动峰会上成立的非营利组织，它发布了开源 AI 差距地图 v0.1，索引了 421 个产品，涵盖软件、模型、数据集和硬件，以识别开源 AI 生态系统中的空白。 该地图提供了一次全面且资金充足的系统性尝试，以绘制开源 AI 领域的地图，帮助开发者、研究人员和资助者了解资源缺乏之处以及下一步的投资方向。 该地图详细列出了来自 228 个组织的 266 个软件工具、85 个模型、50 个数据集和 20 个硬件项目，按三个堆栈层的 14 个类别组织；底层数据以 MIT 许可证发布在 GitHub 上。

rss · Simon Willison · 7月3日 22:04

**背景**: Current AI 是一个全球性的非营利合作伙伴关系，已承诺投入 4 亿美元资金，旨在为 AI 构建一个公共选项。差距地图建立在哥伦比亚会议、MOF、Hugging Face 等机构的工作基础上，以绘制开源 AI 堆栈并识别缺失的组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://map.currentai.org/">Current AI – Open Source AI Gap Map</a></li>

</ul>
</details>

**标签**: `#open source`, `#AI`, `#ecosystem mapping`, `#non-profit`, `#infrastructure`

---

<a id="item-6"></a>
## [课程创作者报告收入因 AI 下降超 50%](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything) ⭐️ 8.0/10

知名课程创作者 Josh W. Comeau 报告称，其新课程销量约为正常水平的 1/3，现有课程收入下降超过 50%。他将此归因于 AI 引发的开发者就业不确定性，以及 LLM 取代付费课程的趋势。 多位课程创作者的第一手反馈表明，开发者教育正经历结构性转变——AI 工具降低了付费课程的感知价值，并引发职业不确定性。这凸显了内容创作者面临的更广泛挑战：他们的作品被用于训练 LLM 却未获报酬。 Comeau 推出的第三门课程“Whimsical Animations”销量约为正常水平的 1/3。他指出其他课程创作者也面临类似趋势：收入下降超 50%，用户参与度降低。

rss · Simon Willison · 7月3日 21:25

**背景**: 面向开发者的在线课程曾是许多创作者的重要收入来源，但 GPT-4 等大型语言模型（LLM）的兴起改变了这一格局。LLM 能提供个性化辅导和代码解释，降低了对付费课程的需求。此外，AI 引发的开发者就业不确定性也抑制了学习新技能的投入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mindomax.com/how-llms-generate-educational-content">How LLMs Generate Educational Content</a></li>
<li><a href="https://www.digitaltoday.co.kr/en/view/56971/ai-driven-uncertainty-spreads-expanding-developers-roles-is-key-to-change">AI - driven uncertainty spreads, expanding developers ’ roles is key to...</a></li>

</ul>
</details>

**标签**: `#AI impact`, `#developer education`, `#online courses`, `#LLMs`, `#industry trends`

---

<a id="item-7"></a>
## [CDD 仅从 logits 恢复微调数据](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

研究人员提出了对比解码差异（CDD），该方法仅通过 logits 访问即可从大语言模型中恢复逐字微调数据，无需模型权重或激活。CDD 在四个模型家族的 20 个模型对中的 19 个上达到了 4+/5 的逐字恢复分数，优于之前的白盒方法 Activation Difference Lens（ADL）。 这项工作揭示了大语言模型中一个重大的隐私漏洞，因为它表明仅需最少的访问权限（仅 logits）即可提取微调数据。同时，它展示了由 LLM 生成的合成数据可能留下意外的指纹，引发了对数据泄露和模型审计的担忧。 CDD 使用单一默认配置，无需逐模型校准或层选择，却优于需要完全权重访问的 ADL。一个意外的发现是，虚构名称“Dr. Elena Rodriguez”出现在多个无关的微调领域中，追溯发现这是 Claude Sonnet 3.6 在生成合成数据时偏好的名字。

reddit · r/MachineLearning · /u/CebulkaZapiekana · 7月3日 19:01

**背景**: 模型差异分析旨在识别基础模型与微调版本之间的差异。先前的工作 Activation Difference Lens（ADL）需要白盒访问（权重和激活），且仅能恢复模糊的领域描述。对比解码是一种通过对比两个模型输出来选择 token 的技术；CDD 将这一思想应用于模型差异分析，直接对比 logits。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2510.13900">Narrow Finetuning Leaves Clearly Readable Traces in Activation ...</a></li>
<li><a href="https://arxiv.org/html/2602.10371v1">Simple LLM Baselines are Competitive for Model Diffing</a></li>
<li><a href="https://learnmechinterp.com/topics/finetuning-traces/">Finetuning Traces in Activations | Learn Mechanistic Interpretability</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论中包含关于该方法在更大模型上的适用性以及潜在防御措施的技术问题。一些评论者对隐私影响表示担忧，而另一些则称赞该方法的巧妙之处以及关于合成数据指纹的偶然发现。

**标签**: `#LLM`, `#privacy`, `#model diffing`, `#finetuning`, `#machine learning`

---

<a id="item-8"></a>
## [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](https://t.me/zaihuapd/42327) ⭐️ 8.0/10

Anthropic 指控阿里巴巴通过约 2.5 万个欺诈账户，在 2026 年 4 月 22 日至 6 月 5 日期间与 Claude 模型进行了超过 2880 万次交互，试图非法提取其能力，这是一次大规模的“蒸馏攻击”。 此事件凸显了模型蒸馏攻击对 AI 公司商业模式的日益威胁，这些公司投入巨资训练前沿模型并依赖 API 访问实现盈利。涉及 Qwen 等中国主要 AI 实验室也引发了关于知识产权盗窃和竞争间谍活动的地缘政治担忧。 Anthropic 声称这是针对该公司迄今已知最大规模的蒸馏攻击，涉及阿里巴巴及其 AI 实验室 Qwen。据称，在指控之后，阿里巴巴下令所有员工卸载 Anthropic 产品，包括 Claude Sonnet、Opus、Fable 以及 Claude Code，禁令于 2026 年 7 月 10 日生效。

telegram · zaihuapd · 7月3日 06:21

**背景**: 模型蒸馏是一种让较弱模型通过学习较强模型的输出来复制其能力的技术。蒸馏攻击则通过大量未经授权的 API 查询来提取模型知识，对投入巨资训练前沿模型的 AI 公司构成生存威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude ( AI ) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen_(Alibaba_Cloud)">Qwen (Alibaba Cloud)</a></li>

</ul>
</details>

**标签**: `#AI security`, `#model distillation`, `#Anthropic`, `#Alibaba`, `#geopolitics`

---

<a id="item-9"></a>
## [华为发布 Atlas 350 加速卡，搭载昇腾 950PR，算力达 H20 的 2.87 倍](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

在 2026 年华为中国合作伙伴大会上，华为正式发布并上市了搭载全新昇腾 950PR 处理器的 Atlas 350 AI 加速卡，声称其单卡算力达到英伟达 H20 的 2.87 倍，并支持 FP4 低精度推理。 这意义重大，因为它为中国市场提供了英伟达受限 H20 芯片的高性能国产替代方案，可能减少对美进口 AI 基础设施的依赖。FP4 支持和 112 GB 大容量 HBM 使其在大语言模型推理方面具有竞争力。 Atlas 350 是国内首款支持 FP4 精度的加速卡，其 112 GB HBM 可单卡加载 70B 参数模型。华为声称在向量算力、互联带宽和自研 HBM 方面较前代有显著提升。

telegram · zaihuapd · 7月3日 08:35

**背景**: 英伟达 H20 是为中国市场设计的 GPU，因美国出口限制而性能降低，比 H100/H200 更慢。FP4 是一种低精度浮点格式，通过减少内存带宽和计算需求来加速 AI 推理，但可能影响精度。华为昇腾系列是中国推动国产 AI 芯片独立的关键力量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.omniyq.com/en/sys-nd/501.html">Ascend 950 : A Milestone for Domestic AI Compute - Shenzhen Cloud...</a></li>
<li><a href="https://www.spheron.network/blog/huawei-ascend-950-vs-nvidia-b300-b200-llm-inference-2026/">Huawei Ascend 950 vs NVIDIA B300 and B200 for... | Spheron Blog</a></li>
<li><a href="https://spoonai.me/posts/2026-04-13-huawei-950pr-ai-chip-en">Huawei Ascend 950 PR — 2.8x H20 FP4, and ByteDance... | spoonai</a></li>

</ul>
</details>

**标签**: `#hardware`, `#AI`, `#Huawei`, `#accelerator`, `#semiconductor`

---

<a id="item-10"></a>
## [华为 Mate 80 Pro 游戏能效超越骁龙 8 Gen3](https://www.bilibili.com/video/BV1F7T46wEyT) ⭐️ 8.0/10

极客湾评测显示，搭载麒麟 9030 和 9030 Pro 芯片的华为 Mate 80 Pro 系列，凭借原生鸿蒙优化，游戏能效超越骁龙 8 Gen3。在《原神》极高画质 60 帧下，Mate 80 Pro Max 整机功耗仅 4.9W，能效优于骁龙 8 Gen3。 这表明软硬件协同优化可以克服理论性能劣势，可能重塑移动 SoC 竞争格局。同时凸显华为在自研芯片和鸿蒙生态方面的进展，可能影响消费者选择和行业趋势。 麒麟 9030 Pro 采用 9 核 14 线程 CPU 和 6 核马良 935 GPU，晶体管规模约 150 亿。其 CPU 多核能效介于骁龙 8 Gen2 和 8 Gen3 之间，但实际游戏性能得益于鸿蒙原生应用优化和智能调度。

telegram · zaihuapd · 7月3日 13:27

**背景**: 华为海思麒麟芯片自 2020 年起面临美国制裁，限制了先进制程获取。麒麟 9030 采用 5nm 工艺制造，标志着国内芯片生产的持续进步。鸿蒙是华为专为无缝多设备协同设计的操作系统，原生应用经过优化以充分利用软硬件整合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Kirin_9030">Kirin 9030</a></li>
<li><a href="https://nanoreview.net/en/soc/hisilicon-kirin-9030">HiSilicon Kirin 9030 Pro: specs and benchmarks</a></li>
<li><a href="https://www.ithome.com/0/972/456.htm">华为 Mate 80 Pro 性能解禁：麒麟 9030 Pro GPU 相比 9020 提升 76...</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#Kirin 9030`, `#HarmonyOS`, `#mobile SoC`, `#gaming performance`

---

<a id="item-11"></a>
## [NASA 发射救援卫星拯救老化太空望远镜](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 8.0/10

7 月 3 日，NASA 发射了 LINK 航天器，它将尝试捕获老化的“雨燕”空间望远镜，并将其轨道抬升约 240 公里，以防止其在大气层中烧毁。 此次任务标志着私人航天器首次尝试捕获美国政府卫星，为未来的卫星维修和太空碎片减缓工作开创了先例。 LINK 航天器将使用机械臂抓住望远镜，然后通过推进器缓慢抬升其轨道。如果成功，“雨燕”最快可于 9 月恢复观测。

telegram · zaihuapd · 7月3日 15:43

**背景**: 尼尔·格雷尔斯“雨燕”天文台于 2004 年发射，用于研究伽马射线暴及其他宇宙现象。由于太阳活动加剧，其轨道衰减速度加快，若不干预，最早可能在 2025 年 10 月再入地球大气层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rfi.fr/cn/专栏检索/科技时空/20260630-nasa启动大胆-太空救援-机器人入轨道为20年太空望远镜-续命">NASA启 动 大胆“ 太 空 救援” 机器人入 轨 道 为20... - RFI - 法国国际广播电台</a></li>

</ul>
</details>

**标签**: `#space`, `#NASA`, `#satellite servicing`, `#space debris`, `#astronomy`

---

<a id="item-12"></a>
## [腾讯阿图因 AI 在 CyberGym 测试中超越 Mythos](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 8.0/10

腾讯玄武实验室的阿图因 AI 在加州大学伯克利分校主导的 CyberGym 网络安全基准测试中获得 84.0%的得分，超过了 Anthropic 的 Claude Mythos Preview。该工具基于开源模型 GLM-5.1 构建，消耗的预算不到 Mythos“玻璃翼计划”的 0.1%。 这表明一个可本地部署的开源 AI 在漏洞检测方面能以极低的成本超越前沿模型，可能使高级网络安全能力更加普及。同时，这也凸显了中国 AI 实验室在专业领域日益增长的竞争力。 阿图因 AI 在 curl、OpenSSL、Python cryptography 等项目中发现了多个 Mythos 未检出的高危逻辑漏洞，评分最高达 9.3。在伯克利 BVI 真实世界漏洞榜单中，阿图因 AI 的严重漏洞严重程度排名第 1，总数排名第 5。

telegram · zaihuapd · 7月3日 16:12

**背景**: CyberGym 是一个评估 AI 代理发现和利用真实软件漏洞能力的基准测试。Claude Mythos Preview 是 Anthropic 最先进的网络安全模型，但由于安全担忧尚未公开发布。GLM-5.1 是智谱 AI 开发的开源模型，专为长周期代理任务设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/cybergym">CyberGym Benchmark Leaderboard | LLM Stats</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.1">GLM - 5 . 1 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos_Preview">Claude Mythos Preview</a></li>

</ul>
</details>

**标签**: `#AI`, `#cybersecurity`, `#vulnerability detection`, `#benchmark`, `#open-source`

---