---
layout: default
title: "Horizon Summary: 2026-09-22 (ZH)"
date: 2026-09-22
lang: zh
---

> 从 102 条内容中筛选出 16 条重要资讯。

---

1. [阿里巴巴在云栖大会正式发布 Qwen 4](#item-1) ⭐️ 9.0/10
2. [vLLM v0.30.0 发布：新增 Fast Start 权重缓存与多款新模型支持](#item-2) ⭐️ 8.0/10
3. [GPT-6 Astra 协助破解自 2005 年以来未解的恩尼格玛密文](#item-3) ⭐️ 8.0/10
4. [gzip 能充当语言模型吗？](#item-4) ⭐️ 8.0/10
5. [小米发布 MiMo v2.6 开源权重 MoE 模型系列](#item-5) ⭐️ 8.0/10
6. [Bryan Cantrill 剖析 Sun Microsystems 的战略失误](#item-6) ⭐️ 8.0/10
7. [博主反对使用大语言模型生成书面内容](#item-7) ⭐️ 8.0/10
8. [文章称 AI 没有智慧，过度依赖会让人丧失判断力](#item-8) ⭐️ 8.0/10
9. [TypeSafe AI 发布 Jev：一种“系统一”决策模型](#item-9) ⭐️ 8.0/10
10. [OpenAI 成立数学顾问小组，其 AI 已解决 100 多个开放问题](#item-10) ⭐️ 8.0/10
11. [阿里巴巴计划 5 至 10 万亿参数 AI 模型，发布真武 V900 芯片](#item-11) ⭐️ 8.0/10
12. [phantom-kv 通过可热插拔的 18MB KV 缓存库解除 LLM 审查](#item-12) ⭐️ 8.0/10
13. [25 位菲尔兹奖得主警告 AI 或与数学研究目标错位](#item-13) ⭐️ 8.0/10
14. [阿里发布真武 V900，宣称算力达 M890 三倍](#item-14) ⭐️ 8.0/10
15. [DeepSeek 与清华发布 DSec 沙箱平台，每日服务 300 万个沙箱](#item-15) ⭐️ 8.0/10
16. [中国调查 DeepSeek 与月之暗面数据泄露问题](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [阿里巴巴在云栖大会正式发布 Qwen 4](https://www.reddit.com/r/LocalLLaMA/comments/1wmxfjs/qwen_4_announced_at_apsara_conference/) ⭐️ 9.0/10

阿里巴巴在云栖大会上正式发布了 Qwen 4，推出了其开源大语言模型系列的新一代版本。该消息由 r/LocalLLaMA 社区成员分享，引起了本地 AI 爱好者的广泛关注。 Qwen 是使用最广泛的开源权重大模型系列之一，新一代版本的发布可能重塑开源模型格局，为开发者提供比闭源模型更具竞争力的选择。依赖开源权重进行本地部署的用户和企业将直接受到影响。 该 Reddit 帖子内容简短，主要链接到一张来自大会的图片，因此参数规模、基准测试成绩和许可条款等具体技术细节尚未公布。此次发布符合阿里巴巴每年在杭州云栖大会上发布 Qwen 模型的惯例。

reddit · r/LocalLLaMA · /u/Salah_H_Hasan · 9月22日 02:45

**背景**: Qwen（又称通义千问）是阿里云开发的一系列以开源权重为主的大语言模型和小语言模型。该系列凭借出色的性能和宽松的许可协议在开源社区广受欢迎，例如 Qwen-72B 在多项任务上超越了 LLaMA2-70B。云栖大会是阿里云每年在杭州举办的旗舰技术峰会，用于展示其最新的 AI 和云计算创新成果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://www.alibabacloud.com/en/apsara-conference/2026-about?_p_lc=1">2026 About Apsara Conference – Alibaba Cloud</a></li>
<li><a href="https://github.com/QwenLM/qwen">GitHub - QwenLM/Qwen: The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud. · GitHub</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#LLM`, `#Alibaba`, `#open-source`, `#AI announcement`

---

<a id="item-2"></a>
## [vLLM v0.30.0 发布：新增 Fast Start 权重缓存与多款新模型支持](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM 发布了 v0.30.0 版本，这是一次重大更新，包含来自 315 位贡献者（其中 104 位是新贡献者）的 762 次提交，新增了对 DeepSeek-V4.1-Flash、DeepSeek-V4-Flash-Vision-Exp、GLM-5.3-Flash、K2-Horizon、Cohere Compass、Bailing V3 VL 和 Nanbeige4.2 等模型的支持。该版本还引入了名为 Fast Start 的常驻式每 GPU 权重缓存守护进程、Gumbel-max 水印、HiSparse 主机端 KV 分层，以及大量性能与量化优化。 vLLM 是目前使用最广泛的开源大模型推理与服务引擎之一，其版本发布直接影响生产级 AI 基础设施的部署方式。Fast Start 和 HiSparse 等功能针对的是两个最主要的运维痛点——引擎重启缓慢以及长上下文解码时的 GPU 显存压力，这对任何大规模运行大模型的团队都至关重要。 Fast Start 将量化后、按张量并行分片的权重常驻在 GPU 显存中，并通过 CUDA IPC 以 `--load-format ipc_cache` 方式重新映射，而不再从磁盘重新加载，目前还覆盖了 FP4 检查点和多节点张量并行。其他值得注意的细节包括：在 SM100 上通过 FlashMLA 为 DeepSeek-V4.1-Flash 提供 MXFP8 KV 存储、带 AVX512/AMX 稀疏 MLA 内核的 DeepSeek-V4 CPU 后端，以及 Model Runner V2 的改动使 H200 上的 CUDA 图捕获时间从 12 秒降至 2 秒、引擎初始化从 28.9 秒降至 8.2 秒。

github · khluu · 9月22日 05:20

**背景**: vLLM 是一个用于大语言模型推理与服务的开源框架，最初由加州大学伯克利分校 Sky Computing Lab 开发，其核心是 PagedAttention——一种针对 Transformer 键值缓存的内存管理方法。它支持连续批处理、分布式推理、量化和 OpenAI 兼容 API，已成为最活跃的开源 AI 项目之一。FlashMLA 是 DeepSeek 开发的优化多头潜在注意力内核库，而 MXFP8 是一种块浮点格式，通过让一组数值共享同一个指数来节省内存和计算量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLLM">VLLM</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/FlashMLA: FlashMLA: Efficient Multi-head Latent Attention Kernels · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/MXFP8">MXFP8</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#model serving`, `#release`, `#AI infrastructure`

---

<a id="item-3"></a>
## [GPT-6 Astra 协助破解自 2005 年以来未解的恩尼格玛密文](https://www.cryptocellar.org/bgac/the-mvueh-break.html) ⭐️ 8.0/10

据报道，OpenAI 的 GPT-6 Astra 协助研究员 Leffer 破解了一条自 2005 年以来一直未能解密的顽固恩尼格玛密文，这被描述为一次为期两天的合作。突破之所以可能，是因为该密文使用了与当天其他通信完全不同的密钥，原始转录存在错误，而且左侧转子在第 72 个字母处发生了罕见的翻转，使标准的已知明文攻击失效。 这一案例表明，像 GPT-6 Astra 这样的大语言模型正越来越多地被用于艰难的密码学和历史谜题，可能改变研究人员解决长期未解问题的方式。它也引发了更广泛的争论：AI 能力不断增强，密码分析等领域的人类专业知识是否正在变得可被替代。 实际解密出的信息大致为：“请说明行军路线。我在 Rosenow，Rosenow。立即用无线电回复。Waschbusch。”原始德文密文中存在多处拼写错误。该密文使用了不寻常的密钥，加上第 72 个字母处罕见的转子翻转，解释了它为何近二十年未被破解；而且这次解密是研究员 Leffer 与 Astra 的合作成果，并非 AI 完全自主完成。

hackernews · sohkamyung · 9月22日 13:52 · [社区讨论](https://news.ycombinator.com/item?id=49801324)

**背景**: 恩尼格玛机是二战期间德军广泛使用的转子密码设备；尽管它曾被认为不可破解，但由艾伦·图灵领导的布莱切利园盟军密码分析人员利用程序漏洞和操作员失误解密了大量信息。然而，由于异常的密钥设置、转录错误或罕见的转子行为，一些个别密文数十年来一直未能破解。GPT-6 Astra 是 OpenAI 于 2026 年 9 月发布的最强大语言模型，专为复杂推理、编程和研究任务设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Enigma_machine">Enigma machine - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cryptanalysis_of_the_Enigma">Cryptanalysis of the Enigma - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT - 6 Astra - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者纠正了耸动的标题，指出该密文是在 Astra 的“大力帮助”下破解的，而非 AI 独立完成，并强调了其长期未被破解的技术原因：独特的密钥、转录错误以及第 72 个字母处罕见的转子翻转。一些人对 AI 让即使最聪明的人类也变得可替代感到不安，另一些人则提到 Veritasium 最近关于恩尼格玛的视频，并质疑 2005 年这一日期的意义。

**标签**: `#AI`, `#cryptography`, `#Enigma`, `#OpenAI`, `#GPT-6`

---

<a id="item-4"></a>
## [gzip 能充当语言模型吗？](https://nathan.rs/posts/gzip-lm/) ⭐️ 8.0/10

nathan.rs 上的一篇文章探讨了 gzip 压缩算法能否充当语言模型，在 Hacker News 上引发了 307 分、120 条评论的热烈讨论。文章探讨了基于压缩的分类方法及其与语言建模研究的概念联系。 这很重要，因为它将信息论与机器学习联系起来，展示了经典压缩工具如何近似语言建模任务，并为大型神经模型提供了一种低资源替代方案。它还凸显了压缩与预测之间支撑现代 AI 研究的深层理论联系。 社区成员指出，gzip 可以通过将测试文件与特定主题的语料一起压缩并选择输出最小的那个来进行文本分类，这一技术最早由怀卡托大学的 Witten 团队开创。批评者指出，生成续写文本的搜索空间太大，无法进行有意义的探索，因此结果只能给出 gzip 作为合理性检验器的能力下界。

hackernews · networked · 9月22日 06:08 · [社区讨论](https://news.ycombinator.com/item?id=49797323)

**背景**: gzip 是 1992 年发布的广泛使用的压缩工具，基于结合 LZ77 和霍夫曼编码的 DEFLATE 算法。语言模型是预测自然语言序列的计算模型，而谷歌的《Language Modeling Is Compression》等近期研究表明，压缩与预测在数学上是等价的。基于压缩的分类使用归一化压缩距离来衡量文件之间的相似性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gzip">gzip - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Language_modeling">Language modeling</a></li>
<li><a href="https://github.com/ranfysvalle02/compressed-classification">GitHub - ranfysvalle02/ compressed - classification · GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了实用的 gzip 分类示例，并引用了相关研究，包括谷歌的《Language Modeling Is Compression》论文和吉布斯随机性-压缩命题。一些人对有限的搜索空间表示担忧，而另一些人则幽默地指出 Winrar 比 OpenAI 更赚钱。

**标签**: `#compression`, `#language-modeling`, `#gzip`, `#information-theory`, `#machine-learning`

---

<a id="item-5"></a>
## [小米发布 MiMo v2.6 开源权重 MoE 模型系列](https://mimo.xiaomi.com/mimo-v2-6) ⭐️ 8.0/10

小米 MiMo 团队于 9 月 22 日发布并开源 MiMo-V2.6 系列，包括 Flash（总参数 309B / 激活 15B）和 Pro（总参数 1.02T / 激活 42B）两个模型，均已在 Hugging Face 上线。此次发布还罕见地公开了实时训练仪表盘和详细技术报告，涵盖训练方法及 7000 多个强化学习环境。 这是一家大型消费电子公司发布的重要开源权重模型，将万亿参数规模带入开放生态，加剧了中国 AI 实验室之间的竞争。其透明的训练方法为开源模型的文档记录和共享树立了更高标准。 模型采用混合专家（MoE）架构，Pro 总参数达 1.02T 但仅激活 42B，并在编程、视觉和 CFT 任务中使用了 75 万条强化学习轨迹进行训练。社区基准显示 MiMo-V2.6-Pro 在 Terminal Bench 4.0 上得分 34.9，明显落后于 GPT 6 Astra 的 59.6 等领先闭源模型。

hackernews · volf_ · 9月21日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=49792730)

**背景**: 混合专家（MoE）是一种让每个输入只经过模型部分参数的架构，使模型总规模可以极大扩展，同时保持单 token 计算量可控。开源权重模型指训练后的参数可公开下载，但未必包含训练数据或代码。小米 MiMo 团队是该公司专门的 AI 研究部门，此次发布延续了此前的 MiMo 版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo-V2.6 | Xiaomi</a></li>
<li><a href="https://www.kucoin.com/news/flash/xiaomi-releases-mimo-v2-6-with-trillion-parameter-models-and-7-000-rl-environments">Xiaomi Releases MiMo-V2.6 with Trillion-Parameter Models and 7,000+ RL Environments | KuCoin</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞小米的透明度，尤其是实时训练仪表盘作为学习工具的价值，也有人就能源瓶颈展开中美 AI 竞赛的讨论。部分用户对基准测试表示怀疑，还有人分享了 Hugging Face 模型卡和测试输出的链接。

**标签**: `#LLM`, `#open-weights`, `#Mixture-of-Experts`, `#AI-research`, `#Xiaomi`

---

<a id="item-6"></a>
## [Bryan Cantrill 剖析 Sun Microsystems 的战略失误](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) ⭐️ 8.0/10

前 Sun Microsystems 工程师、DTrace 共同创造者 Bryan Cantrill 在其个人博客上发表了一篇题为《What Sun got wrong》的回顾性文章，剖析了导致该公司衰落的一系列战略与技术失误。该文章在 Hacker News 上引发了热烈讨论，获得 653 分和 375 条评论，众多行业资深人士分享了各自的经历与观点。 Sun Microsystems 是 20 世纪 80 年代和 90 年代最具影响力的计算公司之一，其衰落为商业战略、技术商品化以及忽视市场变化的危险提供了持久的教训。Cantrill 的内部视角加上社区讨论，为当今面临类似竞争压力的工程师和创业者提供了宝贵的洞见。 Cantrill 曾在 Sun Microsystems 工作，并在 Oracle 收购 Sun 后加入 Oracle，他与 Adam Leventhal 和 Mike Shapiro 共同开发了面向生产系统的动态追踪框架 DTrace。社区讨论指出了具体的失误，例如 2002 年短暂取消 Solaris 的 x86 版本，以及 2002 年因服务器数量披露问题未能与 Google 达成交易。

hackernews · chmaynard · 9月21日 14:03 · [社区讨论](https://news.ycombinator.com/item?id=49787436)

**背景**: Sun Microsystems 是一家成立于 1982 年的美国科技公司，开发和销售计算机、硬件及软件，以其 SPARC 工作站、Solaris 操作系统和 Java 平台而闻名。该公司于 2010 年被 Oracle 收购，结束了其作为独立公司的历史。Bryan Cantrill 是一位软件工程师，因在 Sun 和 Oracle 的工作而知名，目前是 Oxide Computer Company 的联合创始人兼 CTO。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sun_Microsystems">Sun Microsystems - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bryan_Cantrill">Bryan Cantrill - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Bryan_Cantrill">Bryan Cantrill</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为 Sun 的工程技术非常出色，但商业执行很差，有人指出 Sun“从未真正对经营企业感兴趣”，更在意打造出色的技术。其他人则分享了具体的抱怨，例如与 Dell 相比痛苦的企业销售流程，并指出了取消 Solaris x86 版本、未能与 Google 达成交易等具体战略错误。还有人将其与当今高估值科技股相提并论，警告类似的泡沫动态。

**标签**: `#Sun Microsystems`, `#computing history`, `#business strategy`, `#Hacker News`, `#technology industry`

---

<a id="item-7"></a>
## [博主反对使用大语言模型生成书面内容](https://blog.colinbreck.com/i-dont-want-to-read-what-you-didnt-write/) ⭐️ 8.0/10

Colin Breck 发表了一篇题为《我不想读不是你写的东西》的博客文章，认为使用大语言模型生成书面内容会破坏真实沟通，该文章在 Hacker News 上引发了热烈讨论，获得 904 分和 382 条评论。 随着大语言模型深入融入软件工程工作流，这场争论触及团队如何撰写设计文档、拉取请求描述和技术沟通，引发了关于信任、信息传递以及人类作者身份价值的思考。 评论者提出了一个信息论论点：写作是将语义信息从一个大脑传递到另一个大脑，大语言模型无法填补作者从未提供的语义比特；还有人指出，AI 生成的拉取请求描述已变得极其冗长，审阅者面对 20 行的改动却被迫阅读数页文字。

hackernews · mooreds · 9月21日 22:30 · [社区讨论](https://news.ycombinator.com/item?id=49794330)

**背景**: 像 ChatGPT 和 Claude 这样的大语言模型（LLM）可以按需生成流畅文本，越来越多地被用于起草文档、摘要和代码审查评论。这引发了关于 AI 生成写作是否真正传达作者意图，还是仅仅产生听起来合理的填充内容的争论，如今甚至出现了以“AI 人性化”为卖点的工具，让这类文本听起来更自然。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alphaxiv.org/overview/2309.11210">Speak While You Think: Streaming Speech Synthesis During Text ...</a></li>
<li><a href="https://notegpt.io/ai-humanizer">Free AI Humanizer – 100% Human Text & No Sign-up, Unlimited</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论总体上认同文章观点：一位评论者从信息论角度指出，大语言模型无法提供作者从未拥有的语义信息；另一位则抱怨 AI 生成的拉取请求描述如今臃肿不堪，审阅者根本无法跳过不读。也有持相反意见的评论者认为，只要作者仔细校对并反复改写，直到文本真正传达出想要表达的信息，大语言模型仍可作为梳理思路的有用陪练。

**标签**: `#AI`, `#Writing`, `#LLM`, `#Communication`, `#Software Engineering`

---

<a id="item-8"></a>
## [文章称 AI 没有智慧，过度依赖会让人丧失判断力](https://alexn.org/blog/2026/09/22/ai-has-no-wisdom-and-neither-will-you/) ⭐️ 8.0/10

一篇题为《AI 没有智慧，你也不会有》的博客文章认为，AI 系统并不具备真正的智慧，而过度依赖它的人类可能会因此丧失自己的智慧。该文在 Hacker News 上引发了 430 条评论的热议（获得 308 分），讨论集中在 AI 在知识工作和软件开发中的局限性。 这场讨论触及了 AI/ML 和软件工程社区日益增长的担忧：将认知任务外包给 AI，可能会随着时间推移侵蚀机构知识和人类专业技能。其重要性在于，业界正在快速采用 AI 编码代理和助手，而这对技能发展和代码可维护性的长期影响仍不明确。 评论者指出，代码可维护性和良好架构缺乏良好的可量化指标，因此很难证明 AI 辅助开发是否降低了质量。一位拥有 20 年经验的评论者描述了自己使用 Claude、Kiro、Qwen Coder 和 Cursor 在两周内构建了一个类似 MongoDB 的数据库，随后又花了更长时间学习关系代数和数据库设计并重构内部实现。

hackernews · dimonomid · 9月22日 12:11 · [社区讨论](https://news.ycombinator.com/item?id=49799965)

**背景**: 文章标题暗含的观点是：智慧不同于知识或模式匹配——它需要判断力、经验和情境理解，而当前 AI 模型并不具备这些。Hacker News 是一个广受欢迎的技术论坛，工程师和研究人员常在此讨论行业趋势，430 条评论、308 分的帖子意味着参与度异常高。这场讨论反映了人们对 AI 在取代或增强人类认知工作方面角色的更广泛焦虑。

**社区讨论**: 评论者意见分歧：一些人警告说，将智慧积累外包给 AI 会导致机构知识缓慢衰退，并将其与制造业外包相类比。另一些人则认为，只要正确引导，AI 编码代理也能产出可维护的代码；还有一位评论者预测，未来 5 到 10 年内，大多数人类开发者将不再亲手编写任何一行代码。

**标签**: `#AI`, `#wisdom`, `#software-engineering`, `#institutional-knowledge`, `#Hacker-News`

---

<a id="item-9"></a>
## [TypeSafe AI 发布 Jev：一种“系统一”决策模型](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 8.0/10

TypeSafe AI 发布了 Jev，这是其新一类“系统一”模型（也被称为决策模型）的首个实例：它接受文本输入，但不生成文本，而是返回带类型的概率化输出——针对是/否问题的浮点数、选项概率分布以及评分，并附带置信度。首个模型定价仅为每百万输入 token 0.042 美元，输出不收费，比 OpenAI 的 GPT-5 Nano 更便宜。 这引入了一种新范式，将 LLM 重新定义为决策函数而非对话式文本生成器，可能显著改变 AI 在分类、排序和软件自动化任务中的应用方式。由于它速度极快且成本极低，可能降低将 AI 决策直接嵌入生产系统的成本门槛。 Jev 支持三类问题：返回 0–1 置信度的“Noul”（伯努利）是/否问题、返回所提供选项概率分布的选项问题，以及返回数值区间内浮点分数的评分问题；这些问题会针对同一个“状态”对象并行评估。一个值得注意的局限是，Jev 是纯粹的黑箱——只返回数字，不提供任何解释或理由，这在诸如求职者排名等高风险用途中引发了对隐藏偏见的担忧。

rss · Simon Willison · 9月21日 23:09

**背景**: 传统大语言模型逐 token 生成文本，并按输入和输出 token 计费，其中输出通常更贵。TypeSafe AI 将 Jev 定位为面向机器原生自动化的“前沿智能函数调用”：输入非结构化状态，输出带类型的概率化决策。“系统一”这一名称与更慢、更具审慎推理的“系统二”相对，而“决策模型”这一替代叫法则强调它在垃圾邮件检测、打标签、优先级排序和搜索重排等分类式任务中的作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models & Jev - TypeSafe AI Blog</a></li>
<li><a href="https://www.requesty.ai/blog/typesafe-jev-explained">TypeSafe Jev explained: how it works, LLM differences and... | Requesty</a></li>
<li><a href="https://mchromiak.github.io/articles/2026/Sep/17/Jev-Typed-Decisions-for-Enterprise-AI/">Jev: Typed decisions for enterprise AI - Michał Chromiak's blog</a></li>

</ul>
</details>

**社区讨论**: 备受尊敬的评论者 Simon Willison 认为“决策模型”这一框架有助于理解 Jev 的适用场景，尤其是分类和搜索重排，但他也对它进一步退化为黑箱机器学习表示不安。他警告偏见问题应被置于首位，并希望没有人用 Jev 来给求职者排名，因为那个浮点数可能掩盖看不见的偏见。

**标签**: `#LLM`, `#AI Models`, `#Decision Models`, `#TypeSafe AI`, `#Probabilistic Inference`

---

<a id="item-10"></a>
## [OpenAI 成立数学顾问小组，其 AI 已解决 100 多个开放问题](https://techcrunch.com/2026/09/21/openai-forms-math-advisory-group-as-its-ai-resolves-more-than-100-open-problems/) ⭐️ 8.0/10

OpenAI 成立了一个独立的“数学与人工智能顾问小组”，用于指导新兴 AI 成果的评审与对外沟通，此前其 AI 系统已解决 100 多个开放数学问题。该小组明确无权放缓或改变 OpenAI 正在进行的数学研究方向。 这标志着 AI 驱动数学发现的一个重要里程碑，可能改变数学研究的开展与验证方式。同时它也引发了治理层面的问题：由谁评审和发布 AI 生成的数学成果，这会影响数学家、AI 研究者以及更广泛的科学界。 该顾问小组是独立的，可以提出建议但无法替公司做决策，也无权放缓或改变 OpenAI 的数学研究。此次公告发布之际，OpenAI 的 AI 系统据称已解决 100 多个开放问题，但具体是哪些问题以及验证方式在现有内容中并未详述。

rss · TechCrunch AI · 9月21日 20:15

**背景**: 自动定理证明是自动推理的一个子领域，由计算机程序尝试证明数学定理，Lean、Coq、Isabelle 和 Mizar 等系统常被用作证明助手。近年来，AI 模型越来越多地应用于数学领域，从简单解题逐步走向生成并验证原创数学成果。OpenAI 的顾问小组旨在与数学界建立正式桥梁，使 AI 产出的成果得到负责任的评审与传播。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/advisory-group-on-mathematics-and-ai/">Advisory Group on Mathematics and Artificial Intelligence | OpenAI</a></li>
<li><a href="https://kingy.ai/blog/openai-math-advisory-group-control/">OpenAI ’s Math Advisory Group : Who Controls Mathematics ?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving</a></li>

</ul>
</details>

**社区讨论**: 围绕这一公告的评论普遍持怀疑态度，观察者指出该顾问小组只能提建议、无法替公司决策，一些数学家也反对被当作 AI 的评测基准。主要担忧在于该小组缺乏真正放缓或改变 OpenAI 研究的权力，使其监督作用在很大程度上只是象征性的。

**标签**: `#OpenAI`, `#AI for Mathematics`, `#Automated Theorem Proving`, `#AI Research`, `#Mathematical Discovery`

---

<a id="item-11"></a>
## [阿里巴巴计划 5 至 10 万亿参数 AI 模型，发布真武 V900 芯片](https://www.reddit.com/r/LocalLLaMA/comments/1wmyh9z/alibaba_plans_ai_model_with_5_trillion_to_10/) ⭐️ 8.0/10

在 9 月 22 日于杭州举行的年度云栖大会上，阿里巴巴 CEO 吴泳铭宣布计划训练一个参数规模达 5 至 10 万亿的 AI 模型，并发布了自研的新一代 AI 芯片真武 V900，该芯片同时面向训练和推理。公司还表示，目标是到 2032 年运营超过 20 吉瓦的全球数据中心容量。 如果这一计划得以实现，5 至 10 万亿参数的模型将成为史上规模最大的模型之一，推动 AI 扩展的前沿，而阿里巴巴的自研芯片则有助于在出口管制趋紧的背景下减少对英伟达的依赖。极致的模型规模与自研硬件的结合，表明中国云厂商正在构建全栈 AI 生态以参与全球竞争。 据报道，真武 V900 的性能是上一代的三倍，计划于 2027 年第一季度量产，新一代服务器 CPU 则计划于 2027 年第三季度推出。阿里巴巴尚未披露该 5 至 10 万亿参数模型的训练时间表、成本，以及是否会公开模型权重。

reddit · r/LocalLLaMA · /u/tengo_harambe · 9月22日 03:35

**背景**: 参数是神经网络在训练过程中学习到的内部数值权重，参数规模越大通常能力越强，但缩放定律显示收益递减且成本上升。阿里巴巴的 Qwen 系列模型（包括已预览的 2.4 万亿参数 Qwen3.8-Max）已成为广泛使用的开放权重模型，是西方模型之外的重要选择。真武 V900 由阿里巴巴旗下平头哥半导体设计，顺应了中国科技公司开发国产 AI 加速器、以应对美国先进芯片出口限制的整体趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/alibaba-ai-model-zhenwu-v900-chip/">Alibaba plans AI model with 5 -10 trillion parameters , unveils Zhenwu...</a></li>
<li><a href="https://www.cnbc.com/2026/09/22/alibaba-ai-alibabacloud-zhenwu-v900-.html">Alibaba shares jump as new AI chip , data center buildout plans unveiled</a></li>
<li><a href="https://www.trendforce.com/news/2026/09/22/news-alibaba-unveils-ai-chip-zhenwu-v900-for-1q27-mass-production-maps-out-new-server-cpus-for-3q27/">[News] Alibaba Unveils AI Chip Zhenwu V900 for 1Q27 Mass...</a></li>

</ul>
</details>

**标签**: `#AI`, `#large language models`, `#Alibaba`, `#AI chips`, `#scaling`

---

<a id="item-12"></a>
## [phantom-kv 通过可热插拔的 18MB KV 缓存库解除 LLM 审查](https://www.reddit.com/r/LocalLLaMA/comments/1wms904/uncensor_an_llm_without_touching_weights_inject_a/) ⭐️ 8.0/10

一位开发者发布了 phantom-kv，这是一种拒绝移除系统，它把一小段训练好的键/值张量库（约 18MB）作为上下文直接注入模型的 KV 缓存，而不修改任何模型权重。由于该“移植”只存在于输入通道中，它可以按请求卸载，使基础模型保持字节级一致，并支持可热插拔的能力模式，例如防御性的“蓝药丸”和攻击性的“红药丸”。 这把“去审查”从永久性的检查点修改重新定义为按请求、可热插拔的能力模式，可能让同一套权重无需重新刷写或重新量化就能服务多种部署角色。它还绕开了此前方法的脆弱性，例如权重空间的 abliteration 和激活空间投影——前者会永久提交修改，后者会在启动时修补模型的信号路径。 该移植是离线针对模型自身目标训练的（对有害提示予以配合，对无害提示保持行为），并避免了单一的一维拒绝方向假设、前向传播钩子以及针对新架构的逐次重建。用 8B 评判模型进行的自我审计发现：词汇层面的拒绝抑制指标会高估合规性；在长会话中该移植会以约 2–4k token 的半衰期衰减（可通过实测的再注入节奏缓解）；回答仍保留法律/伦理框架。

reddit · r/LocalLLaMA · /u/Anony6666 · 9月21日 22:55

**背景**: KV 缓存是注意力机制在推理时作为先前上下文读取的键/值张量记忆，因此向其中注入内容会通过与对话历史相同的通道影响模型。此前的拒绝移除方法包括 abliteration（从权重矩阵中投影掉拒绝方向）和激活空间投影（在运行时按 token、按层减去拒绝方向）。phantom-kv 则以数兆字节的缓存内容而非新检查点的形式发布，作者将其定位为部署可控的模式，而非越狱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/abliteration">Abliteration in LLMs: Removing Refusal Behavior</a></li>
<li><a href="https://www.lesswrong.com/posts/jGuXSZgv6qfdhMCuJ/refusal-in-llms-is-mediated-by-a-single-direction">Refusal in LLMs is mediated by a single direction - LessWrong</a></li>
<li><a href="https://toytag.net/posts/efficient-llm/">Efficient Large Language Model Inference · @toytag.net</a></li>

</ul>
</details>

**标签**: `#LLM`, `#uncensoring`, `#KV-cache`, `#refusal-removal`, `#local-llama`

---

<a id="item-13"></a>
## [25 位菲尔兹奖得主警告 AI 或与数学研究目标错位](https://t.me/zaihuapd/43973) ⭐️ 8.0/10

包括陶哲轩、邓煜在内的 25 位菲尔兹奖得主发表联合声明，警告将 AI 快速用于解决数学问题可能导致 AI 发展目标与数学研究目标“严重错位”。声明认为，把数学解题作为衡量 AI 能力的基准，可能损害数学研究和整个学术生态。 这份声明由全球最顶尖的数学家联署，分量非同寻常，可能影响高校、期刊和资助机构如何评估 AI 生成的数学成果。它还提出了一个更广泛的问题：为基准表现而优化 AI，是否会扭曲其所应用领域的目标。 声明强调，数学研究的核心是形成概念理解和新洞见，而非单纯获得答案，并警告 AI 批量生成成果可能压缩验证、交流和引用前人成果的时间，同时引发署名和抄袭等问题。声明也承认 AI 有望提升研究效率，其影响取决于人们如何使用这项技术。

telegram · zaihuapd · 9月22日 03:00

**背景**: 菲尔兹奖由国际数学联盟每四年颁发一次，授予不超过四位 40 岁以下的数学家，常被称为“数学界的诺贝尔奖”；截至 2026 年共有 68 人获奖。近年来，大型语言模型在解决数学问题上的能力显著提升，引发了关于这种基准表现是否代表真正数学理解的争论。这份联合声明反映了数学界对 AI 在研究伦理、出版和学术署名中作用的日益担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fields_Medal">Fields Medal</a></li>
<li><a href="https://otontechnology.com/leiden-declaration-ai-mathematics-ethics/">Leiden Declaration Demands AI Transparency in Mathematics</a></li>
<li><a href="https://www.allscientificjournal.com/assets/archives/2026/vol11issue2/11055.pdf">The impact of AI on mathematical research</a></li>

</ul>
</details>

**标签**: `#AI`, `#Mathematics`, `#Research Ethics`, `#Academic Publishing`, `#Fields Medal`

---

<a id="item-14"></a>
## [阿里发布真武 V900，宣称算力达 M890 三倍](https://finance.sina.com.cn/stock/bxjj/2026-09-22/doc-inissitf7048094.shtml) ⭐️ 8.0/10

在 2026 云栖大会上，阿里平头哥发布了真武 V900，这是一款训推一体的 AI 芯片，被其称为最强国产 AI 芯片，宣称算力提升至前代真武 M890 的 3 倍，单一集群可扩展至 50 万卡。CEO 吴泳铭还表示，自研 M890 超节点已支撑 2 万亿参数大模型推理，本季度将规模化上架阿里云。 这一发布表明中国国产 AI 芯片生态正快速成熟，足以挑战英伟达在中国市场受限的地位；Bernstein Research 预测 2026 年华为将占据中国 AI 芯片市场 50% 的份额，而英伟达的份额将萎缩至约 8%。如果 V900 的宣称能够兑现，中国云厂商将有望在不依赖受出口限制的国外硬件的情况下，训练和部署前沿规模的大模型。 据 IT 之家现场报道，真武 V900 支持 216GB 显存和 1200GB/s 的片间带宽，但 V900 及后续 J900 的完整规格尚未公开。所有性能数据均来自厂商，尚未经过独立基准测试；阿里还设定了雄心勃勃的目标：训练 5 至 10 万亿参数的 Qwen 模型，并到 2032 年使阿里云全球数据中心规模超过 20GW。

telegram · zaihuapd · 9月22日 03:30

**背景**: 平头哥是阿里巴巴旗下的自研半导体设计部门，真武系列是其面向训练和推理的 AI 加速器产品线。“超节点”指的是将大量加速器紧密互联、作为单一大型计算单元运行的集群设计，英伟达通过 NVL72 等系统推广了这一概念，华为等中国厂商也在以 CloudMatrix 384 跟进。中国推动 AI 芯片自研，很大程度上是因为美国出口管制限制了对英伟达顶级 GPU 的获取，使国产替代方案具有重要战略意义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/1/005/602.htm">最强国产 AI 芯 片 阿里 平 头 哥 真 武 V 900 ...</a></li>
<li><a href="https://tech.ifeng.com/c/8tHMSnuzdDJ">真 武 M890只是开胃菜！阿里 平 头 哥 首曝路线图： V 900 +J900两年两代</a></li>
<li><a href="https://www.chip37.com/m/article/20260922-3032.shtml">chip37.com/m/article/20260922-3032.shtml</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#Alibaba`, `#semiconductor`, `#AI infrastructure`, `#cloud computing`

---

<a id="item-15"></a>
## [DeepSeek 与清华发布 DSec 沙箱平台，每日服务 300 万个沙箱](https://arxiv.org/abs/2609.22978) ⭐️ 8.0/10

DeepSeek-AI 与清华大学联合发布了《DeepSeek Elastic Compute（DSec）》技术报告，公开了支撑大规模智能体训练与评测的沙箱基础设施。DSec 通过统一 SDK 提供 FnCall、容器、Firecracker microVM 和完整 VM 四种后端，每天服务约 300 万个沙箱实例，峰值并发超过 38 万。 智能体训练与强化学习越来越依赖海量隔离执行环境，DSec 展示了如何构建可支撑这一规模的生产级沙箱平台。其架构选择与性能数据为构建智能体训练基础设施的团队提供了具体参考，也进一步体现了 DeepSeek 在模型之外对开放系统工作的投入。 单个生产单元约使用 160 个节点，沙箱创建速度超过每秒 5000 个，单节点可高密度承载 3200 个容器或 800 个 microVM。平台基于 3FS 分布式文件系统按需加载 EROFS 镜像，而非全量拉取 Docker 镜像，使任务完成时间快 1.7 倍、磁盘写入减少 57%，内存共享与回收机制还使峰值内存占用下降约 40%。

telegram · zaihuapd · 9月22日 04:45

**背景**: 沙箱是用于安全运行不可信代码的隔离执行环境，智能体训练框架需要海量沙箱来让模型与工具、操作系统和软件任务交互。Firecracker 是一种轻量级虚拟化技术，可创建启动快、内存开销低的 microVM；EROFS 是一种面向压缩和高效 I/O 优化的只读 Linux 文件系统。3FS 是 DeepSeek 自研的面向 AI 训练与推理的高性能分布式文件系统，DSec 将这些组件整合为统一平台，并将有状态的 rollout 执行与可抢占的 GPU 训练解耦。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://firecracker-microvm.github.io/">Firecracker</a></li>
<li><a href="https://en.wikipedia.org/wiki/EROFS">EROFS - Wikipedia</a></li>
<li><a href="https://medium.com/@drishabh521/deepseek-ai-unveils-fire-flyer-file-system-3fs-a-high-performance-distributed-file-system-for-1dac7e4b8d21">DeepSeek AI Unveils Fire-Flyer File System ( 3 FS )... | Medium</a></li>

</ul>
</details>

**标签**: `#agent-training`, `#sandbox-infrastructure`, `#systems`, `#reinforcement-learning`, `#DeepSeek`

---

<a id="item-16"></a>
## [中国调查 DeepSeek 与月之暗面数据泄露问题](https://www.theinformation.com/articles/china-probes-deepseek-moonshot-potential-data-leaks-anthropic) ⭐️ 8.0/10

中国互联网监管机构正在调查 DeepSeek 和月之暗面，起因是 Anthropic 于 9 月 10 日发布报告，指控 7 家中国公司大规模违规使用其 Claude 模型。Anthropic 的 154 页报告特别举例称，DeepSeek 曾把一名警方监控系统开发工程师的请求转发给 Claude。 此次调查凸显了中国 AI 开发者与外国模型提供商之间日益紧张的关系，可能改变中国企业获取海外 AI 服务的方式。这也表明北京正在严肃对待数据隐私和跨境数据流动问题，可能给中国两家最知名的 AI 初创公司带来监管后果。 Anthropic 的报告点名了 7 家中国公司并提供了具体案例，包括 DeepSeek 将一名警方监控工程师的请求转发给 Claude。调查由中国互联网监管机构进行，但目前尚未公布正式指控或处罚。

telegram · zaihuapd · 9月22日 14:37

**背景**: DeepSeek 是一家总部位于杭州的 AI 公司，由对冲基金幻方量化所有，以其开放权重的大语言模型闻名。月之暗面（Moonshot AI）是另一家中国主要 AI 初创公司。Anthropic 是一家美国 AI 安全公司，开发了 Claude 系列大语言模型，全球开发者通过 API 广泛使用该模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://www.moonshot.ai/">Welcome to Moonshot AI . Our mission is to seek the optimal...</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#data privacy`, `#DeepSeek`, `#Moonshot AI`, `#Anthropic`

---