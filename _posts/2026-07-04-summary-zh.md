---
layout: default
title: "Horizon Summary: 2026-07-04 (ZH)"
date: 2026-07-04
lang: zh
---

> 从 51 条内容中筛选出 12 条重要资讯。

---

1. [华为提出“韬定律”：以时间缩微替代几何缩微](#item-1) ⭐️ 9.0/10
2. [Jamesob 的本地运行顶级大模型指南](#item-2) ⭐️ 8.0/10
3. [飞马间谍软件入侵欧盟议会调查员手机](#item-3) ⭐️ 8.0/10
4. [Current AI 发布开源 AI 差距地图](#item-4) ⭐️ 8.0/10
5. [课程创作者报告因 AI 导致销售额下降超 50%](#item-5) ⭐️ 8.0/10
6. [CDD 仅凭 logits 恢复微调数据原文](#item-6) ⭐️ 8.0/10
7. [BaryGraph：将关系嵌入为文档的知识图谱](#item-7) ⭐️ 8.0/10
8. [华为发布 Atlas 350 加速卡，性能达 H20 的 2.87 倍](#item-8) ⭐️ 8.0/10
9. [阿里下令全员卸载 Claude，7 月 10 日生效](#item-9) ⭐️ 8.0/10
10. [华为 Mate 80 Pro 游戏能效超越骁龙 8 Gen3](#item-10) ⭐️ 8.0/10
11. [NASA 发射救援卫星拯救坠落太空望远镜](#item-11) ⭐️ 8.0/10
12. [腾讯阿图因 AI 在 CyberGym 测试中超越 Mythos](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [华为提出“韬定律”：以时间缩微替代几何缩微](https://t.me/zaihuapd/42346) ⭐️ 9.0/10

在近日于上海举行的 2026 国际电路与系统研讨会上，华为发表了“韬定律”，提出以“时间缩微”（τ缩微）替代传统的“几何缩微”作为半导体演进新原则。过去六年，华为已据此设计并量产了 381 款芯片，今年秋季将推出采用逻辑折叠技术的新麒麟芯片。 “韬定律”通过聚焦降低信号传播时延（时间常数）而非缩小晶体管尺寸，为延续摩尔定律提供了潜在路径。这可能重塑半导体产业格局，尤其对那些受限于先进光刻技术的公司意义重大，并有望在 AI、移动和高性能计算领域持续提升性能。 华为预计，到 2031 年，基于“韬定律”的芯片晶体管密度可达 1.4 纳米制程同等水平。即将推出的麒麟芯片采用的逻辑折叠技术并非传统 3D 堆叠，而是一种通过垂直折叠关键路径来降低 RC 延迟和时钟偏斜的设计技术。

telegram · zaihuapd · 7月4日 04:56

**背景**: 摩尔定律预测晶体管密度每两年翻一番，但随着几何缩微日益困难，该定律正逼近物理和经济极限。传统半导体进步依赖于缩小晶体管尺寸（几何缩微）来提升性能和密度。“韬定律”提出了一种范式转变：不再追求晶体管更小，而是通过器件、电路、芯片到系统的多层级协同优化，降低时间常数（τ）——即信号传播时延。这种方法无需极紫外（EUV）光刻技术即可提升晶体管密度和系统性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.thepaper.cn/newsDetail_forward_33228813">究竟｜“韬定律”将如何影响半导体产业演进路径</a></li>
<li><a href="https://article.pchome.net/info/13712.html">华为发表半导体韬定律，提出以时间（τ）缩微替代传统的几何缩微</a></li>
<li><a href="https://www.huxiu.com/article/4861142.html">华为发布"韬定律"半导体新理论 提出以时间缩微替代几何缩微</a></li>

</ul>
</details>

**社区讨论**: 在知乎和虎嗅等平台上的社区评论表达了谨慎乐观，许多人称赞这一创新思路，但也质疑缺乏详细技术规格和独立验证。一些专家指出，逻辑折叠不同于 3D 堆叠，在先进光刻工具受限的背景下，可能成为中国半导体产业的可行路径。

**标签**: `#semiconductor`, `#Moore's Law`, `#Huawei`, `#chip design`, `#hardware innovation`

---

<a id="item-2"></a>
## [Jamesob 的本地运行顶级大模型指南](https://github.com/jamesob/local-llm) ⭐️ 8.0/10

Jamesob 在 GitHub 上发布了一份详尽指南，详细说明了如何构建和本地运行最先进的大语言模型，包括硬件推荐和成本分解。 该指南凸显了本地与云端大模型推理之间的权衡，引发了关于成本效益、性能以及个人和组织可行性的讨论。 该指南的顶级配置使用 4 块 RTX PRO 6000 Blackwell GPU（每块约 1.2 万美元），总价约 5 万至 5.5 万美元，并依赖量化与剪枝技术（如 REAP）来缩小模型规模。

hackernews · livestyle · 7月3日 15:03 · [社区讨论](https://news.ycombinator.com/item?id=48775921)

**背景**: 本地运行大语言模型需要强大的硬件，尤其是大显存的 GPU，以处理数千亿参数的模型。量化通过降低模型精度来适配可用内存，而剪枝则移除不重要的参数。云端 API（如 Claude 或 GPT）提供便捷访问，但会产生持续订阅费用并引发隐私担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/jamesob/local-llm">Jamesob's guide to running SOTA LLMs locally - GitHub</a></li>
<li><a href="https://explainx.ai/blog/running-sota-llms-locally-jamesob-rtx-6000-pro-2026">Jamesob’s Guide to Running SOTA LLMs Locally - explainx.ai</a></li>
<li><a href="https://www.sitepoint.com/local-llms-vs-cloud-api-cost-analysis-2026/">Local LLMs vs Cloud APIs: 2026 Total Cost of Ownership Analysis | SitePoint</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，本地配置仍然极其昂贵，且质量通常低于云服务，有用户提到 4 万美元足以支付 16.8 年的 Claude Opus。其他人则对量化与剪枝的实用性展开辩论，质疑其在基准测试之外的真实性能。

**标签**: `#LLM`, `#local inference`, `#hardware`, `#cost analysis`, `#open source`

---

<a id="item-3"></a>
## [飞马间谍软件入侵欧盟议会调查员手机](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

公民实验室确认，一名参与调查间谍软件的欧洲议会议员在 2022 年和 2023 年多次被飞马间谍软件感染。 这一事件表明，国家支持的监控活动正在针对欧盟机构，破坏民主进程和民选官员的安全。 感染发生在 2022 年 10 月 21 日和 2023 年 3 月 6 日至 7 日，首次感染与针对欧洲的俄罗斯和白俄罗斯流亡记者的活动有关。

hackernews · ledoge · 7月3日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: 飞马是由 NSO 集团开发的强大间谍软件，能够远程入侵移动设备以提取数据和监控通信。公民实验室是研究数字威胁对人权影响的领先研究机构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，其他欧洲议会议员也曾被飞马软件攻击但未产生后果，并质疑为何欧盟议会没有区分工作与个人设备。一些人认为智能手机架构的漏洞使得此类攻击成为可能。

**标签**: `#cybersecurity`, `#surveillance`, `#Pegasus`, `#European Parliament`, `#spyware`

---

<a id="item-4"></a>
## [Current AI 发布开源 AI 差距地图](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI（一家于 2025 年 2 月在巴黎 AI 行动峰会上成立的非营利组织）发布了开源 AI 差距地图 v0.1，索引了 421 个产品，涵盖软件、模型、数据集和硬件，以及 24,400 个未分类的工件。 这份全面的地图提供了开源 AI 生态系统的结构化概览，有助于识别投资和开发方面的差距与机遇，对于推进开源 AI 基础设施至关重要。 该地图详细列出了来自 228 个组织的 266 个软件工具、85 个模型、50 个数据集和 20 个硬件项目，分为三个层次的 14 个类别：模型组件、产品/用户体验和基础设施。底层数据以 MIT 许可证发布在 GitHub 上。

rss · Simon Willison · 7月3日 22:04

**背景**: Current AI 是一个全球性的非营利合作伙伴关系，已获得 4 亿美元的承诺资金，旨在为 AI 构建一个公共选项。差距地图是一个动态的可视化工具，旨在跟踪和分析开源 AI 格局，帮助利益相关者了解资源集中在哪里以及存在哪些差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1</a></li>
<li><a href="https://simonwillison.net/2026/jul/3/open-source-ai-gap-map/">Open Source AI Gap Map | Simon Willison’s Weblog</a></li>

</ul>
</details>

**标签**: `#open source`, `#AI`, `#ecosystem mapping`, `#non-profit`, `#infrastructure`

---

<a id="item-5"></a>
## [课程创作者报告因 AI 导致销售额下降超 50%](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything) ⭐️ 8.0/10

Josh W. Comeau 报告称，他的新课程发布预计销量仅为通常的三分之一，现有课程销售额也大幅下降，多位课程创作者的收入下降了 50%以上。 这标志着开发者教育领域的重大转变，AI 不仅通过提供免费个性化辅导减少了对付费课程的需求，还因就业稳定性担忧抑制了学习意愿，可能重塑整个在线学习行业。 Comeau 提到‘双重打击’：开发者质疑近期内工作是否还存在，以及 LLM 提供个性化辅导，降低了购买课程的动机。他指出 LLM 未经同意或补偿就吞噬了创作者的作品。

rss · Simon Willison · 7月3日 21:25

**背景**: Josh W. Comeau 是一位知名的前端开发者和教育者，创作了关于 React 和 CSS 的热门课程。开发者在线课程市场曾快速增长，但像 ChatGPT 和 Claude 这样的生成式 AI 工具现在提供交互式学习体验，直接与结构化课程竞争。

**标签**: `#AI impact`, `#developer education`, `#course creators`, `#software industry trends`

---

<a id="item-6"></a>
## [CDD 仅凭 logits 恢复微调数据原文](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

研究人员提出了对比解码差异分析（CDD），这是一种灰盒方法，通过对比基础模型和微调模型的 logits 来恢复 LLM 中的逐字微调数据，在 SDF 基准测试中，跨四个模型家族（1B 到 32B 参数）的 19/20 个生物体×模型对上实现了 4+/5 的逐字恢复分数，且无需权重访问。 CDD 暴露了模型构建者面临的重大隐私和知识产权风险，因为它仅通过 logits 访问就能从微调 LLM 中提取逐字训练数据，这比白盒方法的假设弱得多。这一突破还通过揭示微调所学内容增强了模型可解释性。 CDD 使用单一默认配置，无需逐生物体校准或层选择，其性能优于白盒激活差异透镜（ADL）方法，后者在同一基准测试中从未超过 3/5。一个意外发现是，虚构人物“Elena Rodriguez 博士”出现在四个语义无关的微调领域中，追溯发现这是由于 Claude Sonnet 3.6 在生成合成数据时存在偏见。

reddit · r/MachineLearning · /u/CebulkaZapiekana · 7月3日 19:01

**背景**: 模型差异分析旨在识别基础模型与其微调版本之间的变化。先前的工作，激活差异透镜（ADL），需要完全的白盒访问（权重和激活），且仅能恢复模糊的领域级描述。CDD 在灰盒设置下运行，仅需 logits 输出，并能恢复精确文本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tools4all.ai/trends/contrastive-decoding-diffing-recovers-verbatim-finetuning-data">Contrastive Decoding Diffing Recovers Verbatim Finetuning ...</a></li>
<li><a href="https://www.emergentmind.com/papers/2605.25902">CDD: Verbatim Content Recovery via Diffing</a></li>
<li><a href="https://www.machinebrief.com/news/unlocking-ais-hidden-memories-with-contrastive-decoding-9a3m">Unlocking AI's Hidden Memories with Contrastive Decoding</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论内容充实，用户就方法的局限性和潜在防御措施提出了技术问题。作者回应了疑问，指出 CDD 在窄微调模型上效果最佳，而输出扰动等防御措施可能会降低其有效性。总体情绪积极，人们对模型安全的影响感兴趣。

**标签**: `#LLM`, `#model diffing`, `#finetuning`, `#interpretability`, `#security`

---

<a id="item-7"></a>
## [BaryGraph：将关系嵌入为文档的知识图谱](https://www.reddit.com/r/MachineLearning/comments/1un3lsf/barygraph_knowledge_graph_where_every/) ⭐️ 8.0/10

BaryGraph 提出了 BaryEdge，将知识图谱中的每个关系嵌入为拥有自身向量的独立文档，而非表示为节点间的边。它还递归构建 MetaBary 三元组，以发现远距离概念之间的结构桥梁。 该方法解决了平面向量搜索的一个关键局限——将关系视为点邻近的副产品，从而遗漏跨域连接。BaryGraph 通过揭示隐藏的结构相似性，可能显著改进检索增强生成（RAG）和基于图的检索。 BaryEdge 向量计算公式为 bary_vector = normalize(q·v(CM1) + q·v(CM2) + (1−q)·v(type))，其中 q 是连接质量，v(type) 是关系类型的上下文嵌入。该系统在本地运行于 MongoDB Community + mongot 上，使用 nomic-embed-text 处理整个英文维基词典（660 万文档），并提供 MCP 服务器供探测。

reddit · r/MachineLearning · /u/adseipsum · 7月4日 08:24

**背景**: 传统知识图谱将关系表示为连接节点的边，向量搜索通过比较点的嵌入相似度来检索信息。然而，平面向量搜索无法捕捉跨越远距离概念的结构关系。BaryGraph 将关系视为拥有自身嵌入的一等文档，并通过 MetaBary 三元组实现递归抽象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_graph">Knowledge graph - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/mongodb/power-your-ai-application-with-mongodb-vector-search/">Power Your AI Application with MongoDB Vector Search</a></li>
<li><a href="https://www.baeldung.com/cs/ml-knowledge-graphs">How to Build a Knowledge Graph? | Baeldung on Computer Science Guide to Creating Knowledge Graph Visualizations 7 Knowledge Graph Examples of 2026 Knowledge Graphs Knowledge graph - Wikipedia Neo4j LLM Knowledge Graph Builder - Extract Nodes and ...</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论包含实质性的技术评论，对该方法的新颖性和有效性进行了辩论。一些评论者质疑跨域桥梁是否真实或源于模式匹配，而另一些则欣赏其数学严谨性及在 RAG 中的潜力。

**标签**: `#knowledge graph`, `#vector search`, `#RAG`, `#embedding`, `#graph database`

---

<a id="item-8"></a>
## [华为发布 Atlas 350 加速卡，性能达 H20 的 2.87 倍](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

在 2026 年华为中国合作伙伴大会上，华为正式发布并上市搭载全新昇腾 950PR 处理器的 Atlas 350 加速卡，宣称其单卡算力达到英伟达 H20 的 2.87 倍，并支持 FP4 低精度推理。 这一发布标志着华为在 AI 加速器市场迈出重要一步，提供了性能远超受限英伟达 H20 芯片的国产替代方案，可能影响中国及全球的 AI 基础设施选择。 Atlas 350 是国内首款支持 FP4 推理的加速卡，配备 112 GB HBM 内存，单卡可加载 70B 参数模型，大幅降低推理延迟与投资成本。

telegram · zaihuapd · 7月3日 08:35

**背景**: 昇腾 950PR 是华为最新的 AI 推理芯片，专为加速大语言模型推理工作负载（尤其是预填充阶段）而设计。英伟达 H20 是面向中国市场的合规 GPU，性能低于 H100/H200，是中国市场的主要竞争对手。FP4 是一种 4 位浮点格式，能以更低的内存和带宽需求实现高效推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.omniyq.com/en/sys-nd/501.html">Ascend 950 : A Milestone for Domestic AI Compute - Shenzhen Cloud...</a></li>
<li><a href="https://spoonai.me/posts/2026-04-13-huawei-950pr-ai-chip-en">Huawei Ascend 950 PR — 2.8x H20 FP4, and ByteDance... | spoonai</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nvidia_H20">Nvidia H20</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#Huawei`, `#Ascend`, `#accelerator`, `#FP4`

---

<a id="item-9"></a>
## [阿里下令全员卸载 Claude，7 月 10 日生效](https://t.me/zaihuapd/42334) ⭐️ 8.0/10

阿里巴巴内部宣布禁止使用 Anthropic 产品，包括 Claude、Sonnet、Opus 和 Claude Code，要求所有员工在 2025 年 7 月 10 日前卸载。此前 Anthropic 指控阿里在 4 月 22 日至 6 月 5 日期间使用约 2.5 万个虚假账号与 Claude 交互超过 2800 万次。 这标志着中国一家大型科技公司重大政策转变，可能影响中国 AI 模型使用的竞争格局。该禁令还可能加剧美国 Anthropic 与中国企业之间关于安全和滥用的紧张关系。 禁令涵盖所有 Anthropic 产品，包括 Claude 模型（Sonnet、Opus、Fable）和 Claude Code 等 Agent 产品。此前阿里曾报销员工使用 Claude、GPT、Gemini 等外部模型的费用。Anthropic 在指控后收紧了风控策略。

telegram · zaihuapd · 7月3日 13:00

**背景**: Claude 是由美国 AI 安全公司 Anthropic 开发的 AI 助手。Anthropic 使用“宪法 AI”技术训练 Claude 以确保伦理合规。Claude Code 是一个智能编码工具，可以读取代码库、编辑文件和运行命令。阿里的禁令是“反向禁用”——阻止内部使用竞争对手的产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://claude.com/product/overview">The AI for Problem Solvers | Claude by Anthropic</a></li>
<li><a href="https://www.anthropic.com/product/claude-code">Claude Code | Anthropic's agentic coding system \ Anthropic</a></li>

</ul>
</details>

**标签**: `#Alibaba`, `#Claude`, `#Anthropic`, `#AI regulation`, `#corporate policy`

---

<a id="item-10"></a>
## [华为 Mate 80 Pro 游戏能效超越骁龙 8 Gen3](https://www.bilibili.com/video/BV1F7T46wEyT) ⭐️ 8.0/10

极客湾对华为 Mate 80 Pro 系列的评测显示，原生鸿蒙优化使游戏能效超越骁龙 8 Gen3，尽管麒麟 9030 的理论性能仍落后。 这表明深度的软硬件协同可以弥补硬件本身的劣势，可能重塑移动芯片竞争格局，并凸显生态优化的重要性。 麒麟 9030 Pro 采用 9 核 14 线程 CPU 和 6 核马良 935 GPU，晶体管规模约 150 亿。在《原神》最高画质 60 帧下，Mate 80 Pro Max 整机功耗仅 4.9W，能效优于骁龙 8 Gen3。

telegram · zaihuapd · 7月3日 13:27

**背景**: 华为的麒麟芯片历史上一直具有竞争力，但受到美国制裁的限制。HarmonyOS NEXT 是完全自研的操作系统，允许对原生应用进行深度优化，通过软硬芯云协同实现更好的性能和能效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/麒麟9030/66925509">麒麟9030 - 百度百科</a></li>
<li><a href="https://baike.baidu.com/item/麒麟9030+Pro/67025907">麒麟9030 Pro - 百度百科</a></li>
<li><a href="https://www.sohu.com/a/954749456_546984">满血版麒麟9030架构曝光：超大核9宽+GPU 800MHz，Mate80系列却全系“残...</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#chipset`, `#HarmonyOS`, `#gaming`, `#energy efficiency`

---

<a id="item-11"></a>
## [NASA 发射救援卫星拯救坠落太空望远镜](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 8.0/10

NASA 于 2026 年 7 月 3 日发射了 LINK 航天器，与老化的 Swift 太空望远镜会合，并将其轨道抬升约 240 公里，防止其最早在 2026 年 10 月发生失控再入。 此次任务是私人航天器首次尝试抓取并抬升美国政府卫星，展示了在轨服务和太空碎片减缓的关键能力。 由 Katalyst Space Technologies 建造的 LINK 航天器将使用机械臂抓住 Swift，然后通过推进器抬升其轨道。如果成功，Swift 最早可在 2026 年 9 月恢复科学观测。

telegram · zaihuapd · 7月3日 15:43

**背景**: Neil Gehrels Swift 天文台于 2004 年发射，用于探测伽马射线暴等高能宇宙事件。由于太阳活动加剧，其轨道衰减速度快于预期，可能终结其任务。NASA 于 2024 年雇佣 Katalyst 在不到一年内建造救援航天器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spaceeyenews.com/nasa-swift-rescue-mission/">NASA Swift Rescue Mission: A Robot Races to Save... - SpaceEyeNews</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/nasa-successfully-launches-rescue-mission-to-save-swift-space-telescope-from-burning-up-in-earths-atmosphere">NASA launches rescue mission to save Swift space telescope... | Space</a></li>
<li><a href="https://www.science.org/content/article/space-telescope-falling-earth-nasa-racing-rescue-it">A space telescope is falling to Earth. NASA is racing ... - AAAS</a></li>

</ul>
</details>

**标签**: `#space`, `#NASA`, `#satellite servicing`, `#space debris`, `#private space`

---

<a id="item-12"></a>
## [腾讯阿图因 AI 在 CyberGym 测试中超越 Mythos](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 8.0/10

腾讯玄武实验室的阿图因 AI 在 CyberGym 网络安全基准测试中获得 84.0% 的得分，超越 Anthropic 的 Claude Mythos Preview，且消耗预算不到 Mythos 的 0.1%。 这表明可本地部署的开源模型能以极低成本在网络安全领域超越前沿 AI，可能推动高级漏洞发现能力的普及。 阿图因 AI 基于开源模型 GLM-5.1 构建，在 curl、OpenSSL、Python cryptography 等项目中发现了多个 Mythos 未检出的高危逻辑漏洞（最高评分 9.3）。

telegram · zaihuapd · 7月3日 16:12

**背景**: CyberGym 是加州大学伯克利分校推出的网络安全基准测试，用于评估 AI 智能体在真实世界任务中的表现。Claude Mythos 是 Anthropic 的专用网络安全模型，而 GLM-5.1 是 Z.AI 的开源旗舰模型，专为长周期智能体任务设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/cybergym">CyberGym Benchmark Leaderboard | LLM Stats</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.1">GLM-5.1 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mythos_AI">Mythos AI</a></li>

</ul>
</details>

**标签**: `#AI`, `#cybersecurity`, `#benchmark`, `#vulnerability discovery`, `#Tencent`

---