---
layout: default
title: "Horizon Summary: 2026-09-21 (ZH)"
date: 2026-09-21
lang: zh
---

> 从 79 条内容中筛选出 8 条重要资讯。

---

1. [OpenAI 成立数学顾问组，其 AI 已解决 100 多个开放问题](#item-1) ⭐️ 9.0/10
2. [小米发布 MiMo v2.6 开源权重模型系列](#item-2) ⭐️ 8.0/10
3. [NASA/ESA 火星采样返回任务被取消](#item-3) ⭐️ 8.0/10
4. [Bryan Cantrill 反思 Sun Microsystems 的战略失误](#item-4) ⭐️ 8.0/10
5. [Cloudflare Python Workers 正式全面可用](#item-5) ⭐️ 8.0/10
6. [《冥界狂想曲》1996 年谜题设计文档重现网络](#item-6) ⭐️ 8.0/10
7. [月之暗面就 Kimi K3 向微软、亚马逊、谷歌寻求最高 30% 收入分成](#item-7) ⭐️ 8.0/10
8. [苹果发布首款 2 纳米芯片 M6 及四芯片架构 M5 Ultra](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 成立数学顾问组，其 AI 已解决 100 多个开放问题](https://techcrunch.com/2026/09/21/openai-forms-math-advisory-group-as-its-ai-resolves-more-than-100-open-problems/) ⭐️ 9.0/10

OpenAI 宣布成立一个独立的“数学与人工智能顾问组”，负责指导对 AI 新产生的数学成果进行评审与对外沟通。与此同时，据报道 OpenAI 的 AI 系统已解决 100 多个开放数学问题，但该顾问组无权放缓或改变 OpenAI 的研究方向。 如果 AI 系统确实解决了 100 多个开放数学问题，这将是自动推理与定理证明领域的重大里程碑，把讨论从“AI 能否推理”推进到“AI 能否产出经得起形式化验证的发现”。成立顾问组也引发了治理层面的问题：谁来验证和控制这些成果，尤其是该小组只能提供建议、无法约束 OpenAI 的研究议程。 该顾问组被描述为独立机构，专注于对 AI 成果的评审与沟通，但它明确无权替公司做决策，也无法放缓或改变 OpenAI 的数学研究。关于已解决 100 多个问题的说法在现有内容中并未给出细节，这些主张仍需独立验证和形式化证明检查。

rss · TechCrunch AI · 9月21日 20:15

**背景**: 自动定理证明与 AI 辅助数学近年来发展迅速，相关系统已能用 Lean 等形式化语言生成可机器验证的证明。竞争对手也有类似动作：据报道 Google DeepMind 的 Aletheia 解决了 Erdős 问题集中的 13 个开放问题，谷歌研究人员也攻克了若干 Erdős 问题。OpenAI 同样在学术推广上投入，包括推出 ChatGPT for Academic Researchers 计划，为 10 万名科学家和数学家提供免费访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/advisory-group-on-mathematics-and-ai/">Advisory Group on Mathematics and Artificial Intelligence | OpenAI</a></li>
<li><a href="https://kingy.ai/blog/openai-math-advisory-group-control/">OpenAI’s Math Advisory Group: Who Controls Mathematics?</a></li>
<li><a href="https://creati.ai/ai-news/2026-02-08/google-deepmind-ai-solves-erdos-problems/">Google DeepMind's AI Solves 13 Erdős Mathematical Problems ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#OpenAI`, `#research`, `#AI safety`

---

<a id="item-2"></a>
## [小米发布 MiMo v2.6 开源权重模型系列](https://mimo.xiaomi.com/mimo-v2-6) ⭐️ 8.0/10

小米发布了 MiMo v2.6 开源权重大语言模型系列，包含 Flash 和 Pro 两个版本，并罕见地公开了训练过程，包括实时强化学习训练仪表盘和详尽的技术报告。Flash 模型总参数量为 309B、激活参数 15B，Pro 模型则达到 1.02T 总参数、42B 激活参数。 此次发布因公开训练方法而格外引人注目，这在商业 AI 实验室中十分罕见，对研究社区具有重要价值。同时，它也壮大了日益增多的高性价比中国开源权重模型阵营，这些模型正越来越具竞争力，可与美国模型一较高下。 Flash 版本总参数量 309B、激活参数 15B，Pro 版本总参数量 1.02T、激活参数 42B，两者均以强化学习训练后的检查点形式在 Hugging Face 上发布。在 Terminal Bench 4.0 等基准测试中，MiMo-V2.6-Pro 得分为 34.9，Flash 为 28.8，落后于 GPT 6 Astra 和 Claude Fable 5.1 等模型。

hackernews · volf_ · 9月21日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=49792730)

**背景**: 小米 MiMo 是小米开发的大语言模型系列，最初于 2025 年 4 月以 MiMo-7B 模型发布。开源权重模型允许任何人下载并在本地运行，但开放程度各有不同——有些仅发布权重，有些还会公开训练数据和代码。强化学习（RL）是一种让模型从奖励信号中学习的训练技术，小米通过实时仪表盘公开追踪了这一过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xiaomi_MiMo">Xiaomi MiMo - Wikipedia</a></li>
<li><a href="https://www.reddit.com/r/LocalLLaMA/comments/1wi9ebm/xiaomi_mimo_26_live_training_dashboard/">Xiaomi MiMo 2.6 Live Training Dashboard : r/LocalLLaMA - Reddit</a></li>
<li><a href="https://huggingface.co/XiaomiMiMo">XiaomiMiMo (Xiaomi MiMo) - Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞小米的透明度，有人指出实时训练仪表盘是极佳的学习工具，技术报告也异常详尽。其他人则强调中国模型的高性价比是主要吸引力，但也有人对基准测试的可靠性表示怀疑，质疑某些模型超越其他模型的结果。

**标签**: `#LLM`, `#open-weights`, `#Xiaomi`, `#AI-research`, `#benchmarks`

---

<a id="item-3"></a>
## [NASA/ESA 火星采样返回任务被取消](https://www.science.org/content/article/nasa-s-mars-sample-return-mission-dead) ⭐️ 8.0/10

NASA 与 ESA 合作的火星采样返回（MSR）任务已被取消，这项 2022 年批准的多任务计划原本旨在取回 NASA“毅力号”火星车在杰泽罗陨石坑采集的岩石和土壤样本。取消决定还一并撤销了原计划用于接收和封存样本的样本接收设施。 这是行星科学的一次重大挫折，因为返回地球的火星样本可以用远比任何火星车搭载设备更强大的仪器进行分析，尤其是用于寻找潜在的生物特征。此举也改变了国际太空探索格局，使中国的天问三号成为最主要的火星采样返回计划。 “毅力号”共携带 43 个采样管前往火星，其中 38 个用于采集样本，5 个为“见证管”用于记录采样系统的洁净度，并且它已经存放了 10 个备份样本管组成的样本库。此次取消由美国国会在 2026 年 1 月推动，NASA 和 ESA 目前都没有计划替代的取回任务。

hackernews · Muhammad523 · 9月21日 19:14 · [社区讨论](https://news.ycombinator.com/item?id=49791939)

**背景**: 火星采样返回任务是指从火星采集岩石和尘土并带回地球，从而能够进行比火星车搭载传感器更深入的分析，尤其是判断火星是否曾经存在生命。NASA 与 ESA 的 MSR 计划于 2022 年获批，用于取回“毅力号”采集的样本，而该火星车一直将这些样本存放在火星表面。人们也曾担心返回样本可能对地球生物圈造成反向污染，不过这种风险通常被认为很低。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mars_sample-return_mission">Mars sample - return mission - Wikipedia</a></li>
<li><a href="https://science.nasa.gov/mission/mars-2020-perseverance/mars-rock-samples/">Mars Rock Samples - NASA Science</a></li>
<li><a href="https://www.techtimes.com/articles/323332/20260806/china-announces-only-mars-sample-receiving-lab-earth-after-nasa-cancels-plans.htm">China Announces Only Mars Sample Receiving Lab on Earth After...</a></li>

</ul>
</details>

**社区讨论**: 评论者对杰泽罗陨石坑中可能含有生物特征的样本或许永远无法返回表示惋惜，并提到计划在 2028 年发射窗口实施的中国天问三号任务可能成为替代方案。一位曾参与 ExoMars“罗莎琳德·富兰克林”号火星车工作的评论者表示，该任务也一再推迟到 2028 年；还有人质疑为何“毅力号”要钻取岩芯却只是把它们留在地面上，等待一个尚未明确的未来任务。

**标签**: `#space exploration`, `#NASA`, `#Mars Sample Return`, `#planetary science`, `#international competition`

---

<a id="item-4"></a>
## [Bryan Cantrill 反思 Sun Microsystems 的战略失误](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) ⭐️ 8.0/10

前 Sun Microsystems 工程师、DTrace 共同创造者 Bryan Cantrill 发表了一篇题为《What Sun got wrong》的回顾性博客文章，分析了导致该公司衰落的各种战略和技术失误。这篇文章在 Hacker News 上引发了热烈讨论，获得 427 分和 241 条评论，众多行业资深人士分享了关于 Sun 销售实践和战略失误的第一手经历。 Sun 的崩溃仍然是科技史上最具启发性的案例之一，它展示了一家占主导地位的垂直整合厂商如何被商品化的 x86 硬件和开源 Linux 颠覆。这场讨论为当今科技行业提供了教训，评论者将其与特斯拉和 SpaceX 等当前高估值公司进行了类比。 评论者指出了具体的失误：Sun 在 2002 年短暂取消了 x86 平台上的 Solaris，因服务器数量保密问题未能在 2002 年与 Google 达成交易，并且缺乏可信的新客户入门路径——新客户更倾向于在 x86 和 Linux 上开发。一位评论者提到 Sun 的股价从互联网泡沫顶峰的 70 美元在几个月内跌至 7 美元，另一位则回忆说 Sun 和 DEC 的销售流程——需要现场会议和无休止的报价修改——比 Dell 繁重得多。

hackernews · chmaynard · 9月21日 14:03 · [社区讨论](https://news.ycombinator.com/item?id=49787436)

**背景**: Sun Microsystems 是一家美国科技公司，存在于 1982 年至 2010 年，开发和销售计算机、服务器以及 Solaris 操作系统，并以其 SPARC 处理器架构而闻名。Bryan Cantrill 曾在 Sun 工作，后来在 Oracle 收购 Sun 后加入 Oracle，并共同开发了 DTrace——一个用于生产系统的动态追踪框架。Sun 的股价在 2001 年下跌了 51%，2002 年又下跌了 76%，该公司最终于 2010 年被 Oracle 收购。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sun_Microsystems">Sun Microsystems - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bryan_Cantrill">Bryan Cantrill - Wikipedia</a></li>
<li><a href="https://medium.com/@noahbean3396/the-history-of-sun-microsystems-d6ef7248be23">The History of Sun Microsystems - Medium</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论充满了第一手视角：一位评论者描述了从 Sun 或 DEC 购买硬件相比 Dell 的痛苦销售体验；另一位列举了 Sun 的具体失误，包括取消 x86 上的 Solaris 以及未能与 Google 达成交易；还有一位提到在 Sun 股价跌至 7 美元前以 70 美元卖出，并将其与当今高市盈率的 AI 股票相类比。其他人则强调 Sun 缺乏可信的新客户入门路径，并分享了在大学使用 Sun 瘦客户机的怀旧记忆。

**标签**: `#Sun Microsystems`, `#tech history`, `#business strategy`, `#Hacker News`, `#systems engineering`

---

<a id="item-5"></a>
## [Cloudflare Python Workers 正式全面可用](https://blog.cloudflare.com/python-workers-ga/) ⭐️ 8.0/10

Cloudflare 宣布 Python Workers 正式全面可用（GA），开发者现在可以在其基于 WebAssembly 的无服务器边缘运行时中运行 Python 代码，并获得了更好的包支持。此次 GA 版本建立在早期预览版基础上，通过 PEP 783（PyEmscripten）实现了标准化的打包方式，并向上游贡献代码，使 Requests 等 HTTP 客户端能够直接通过 JavaScript 的 fetch API 发起请求。 这对无服务器 Python 来说是一个重要的里程碑，因为 Python 是最流行的语言之一，但历来难以在边缘/无服务器环境中高效运行。它为 Python 开发者提供了一条通往 Cloudflare 全球边缘网络的一流路径，可能重塑 Python Web 应用和 API 的部署方式。 该运行时基于 Pyodide（CPython 移植到 WebAssembly/Emscripten 的版本），包支持现已通过 PEP 783 实现标准化。社区成员指出，冷启动性能和部分架构限制仍是待解问题，而 urllib3 对 Pyodide/Emscripten 及 JSPI 支持的上游工作主要由外部贡献者完成。

hackernews · torutofu · 9月21日 13:38 · [社区讨论](https://news.ycombinator.com/item?id=49787142)

**背景**: Cloudflare Workers 是 Cloudflare 于 2017 年推出的无服务器平台，可在其边缘网络上运行代码，开发者无需管理基础设施。Python Workers 以 WebAssembly（一种最初为浏览器设计的可移植二进制格式）而非原生代码的方式执行 Python。Pyodide 是一个将 CPython 移植到 WebAssembly 的开源项目，使 NumPy、pandas 等 Python 包能够在这些受限环境中运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/pyodide/pyodide">GitHub - pyodide/pyodide: Pyodide is a Python distribution ... Pyodide — Version 314.1.0.dev0 Home - Pyodide About Us - Pyodide pyodide | Pyodide is a Python distribution for the browser ... Pyodide - GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cloudflare">Cloudflare - Wikipedia</a></li>
<li><a href="https://pyodide.org/">Pyodide — Version 314.0.7</a></li>

</ul>
</details>

**社区讨论**: 评论总体积极，Wasmer 的 Syrus Akbary 称赞 Cloudflare 在包支持方面的进展，同时指出仍存在架构方面的担忧。一位 urllib3 维护者澄清，上游的 Pyodide/Emscripten 和 JSPI 贡献的资金是提供给外部贡献者而非维护者；其他人则询问冷启动性能，并希望 Go 语言也能获得类似支持。

**标签**: `#Cloudflare Workers`, `#Python`, `#WebAssembly`, `#Serverless`, `#Pyodide`

---

<a id="item-6"></a>
## [《冥界狂想曲》1996 年谜题设计文档重现网络](http://gameshelf.jmac.org/2008/11/13/GrimPuzzleDoc_small.pdf) ⭐️ 8.0/10

由 Tim Schafer 撰写的《冥界狂想曲》1996 年原始谜题设计文档以 72 页 PDF 的形式在 Hacker News 上被分享。文档详细描述了游戏中每一个谜题及其解法，并穿插了 Schafer 标志性的玩笑和旁注。 这份文档是一份罕见的资料，能让人深入了解史上最受喜爱的冒险游戏之一的创作过程。对于研究经典 LucasArts 冒险游戏如何构建的游戏设计师和编剧来说，它尤其珍贵。 文档揭示了 LucasArts 的谜题设计哲学：从小型环境中的简单线性谜题开始，逐渐过渡到大型区域中可任意顺序解决的较难并行谜题。它还包含标注了每个地点所有出场角色的位置地图，以及一个俏皮的请求——请读者将“喜悦的泪水”限制在一个小方框内。

hackernews · kelseyfrog · 9月21日 05:55 · [社区讨论](https://news.ycombinator.com/item?id=49783495)

**背景**: 《冥界狂想曲》是 1998 年由 Tim Schafer 执导、LucasArts 开发的冒险游戏，背景设定在受黑色电影启发的亡灵之地。Tim Schafer 是著名的美国游戏设计师，后来创立了 Double Fine Productions。谜题设计文档是内部规划资料，概述每个谜题及其解法，这份文档由 Schafer 于 2008 年公开发布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grim_Fandango">Grim Fandango - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tim_Schafer">Tim Schafer - Wikipedia</a></li>
<li><a href="https://simonfairbairn.com/useful-adventure-game-resources-puzzle-documents/">Useful Adventure Game Resources: Puzzle Documents Puzzle Design in Adventure Games - DiVA Design a Puzzle Adventure Game in Unreal Engine | Unreal ... GitHub - brycecovert/adventure-game-designer-handbook: A ... Designing and Integrating Puzzles in Action-Adventure Games</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了怀旧的个人故事，有人回忆小时候因封面艺术而购买该游戏，有人则把它介绍给了自己的儿子。许多人称赞 Schafer 的编剧才华和文档中迷人的个性，也有人指出，在当今注重效率的行业里，这样精心制作的内部文档可能会被视为浪费时间。

**标签**: `#game-design`, `#adventure-games`, `#grim-fandango`, `#tim-schafer`, `#design-document`

---

<a id="item-7"></a>
## [月之暗面就 Kimi K3 向微软、亚马逊、谷歌寻求最高 30% 收入分成](https://t.me/zaihuapd/43950) ⭐️ 8.0/10

据消息人士透露，月之暗面正就 Kimi K3 模型与微软、亚马逊、谷歌谈判收入分成，初期寻求最高 30% 的分成比例。若谈判成功，这将是中国 AI 公司与美国云巨头之间的首个大型模型收入分成协议，但目前谈判仍处早期，核心细节未定，各方均拒绝置评。 这将成为中国 AI 公司与美国云厂商之间的首个大型收入分成协议，表明美国云市场平台越来越需要引入顶级国际模型以保持竞争力。这也意味着开源权重模型的商业化路径正在转变，从单纯的自托管转向借助超大规模云平台进行分发。 Kimi K3 于 2026 年 7 月发布，总参数达 2.8 万亿，是全球首个开源 3T 级模型，截至 6 月中旬其年度经常性收入已突破 3 亿美元。由于 2.8 万亿参数使大多数企业难以自行部署，主要云厂商成为其触达企业客户的主要渠道。

telegram · zaihuapd · 9月21日 06:44

**背景**: 月之暗面是一家中国公司，开发了 Kimi 聊天机器人及其系列大语言模型。Kimi K3 是一款开放权重、原生多模态的混合专家模型，基于 Kimi Delta Attention 与 Attention Residuals 构建，支持 1,048,576 token 的上下文窗口。开放权重模型可自由下载，但其庞大的体量往往使企业依赖云厂商来托管和提供服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(AI)">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://github.com/MoonshotAI/Kimi-K3">GitHub - MoonshotAI/Kimi-K3: Open Frontier Intelligence</a></li>
<li><a href="https://meyka.com/blog/moonshot-ai-negotiates-revenue-sharing-deals-with-microsoft-amazon-and-google-2608/">Moonshot AI Negotiates Revenue - Sharing Deals With... | Meyka</a></li>

</ul>
</details>

**标签**: `#AI`, `#business`, `#cloud-computing`, `#Moonshot-AI`, `#Kimi-K3`

---

<a id="item-8"></a>
## [苹果发布首款 2 纳米芯片 M6 及四芯片架构 M5 Ultra](https://t.me/zaihuapd/43965) ⭐️ 8.0/10

苹果发布了其首款采用 2 纳米制程的芯片 M6，首发搭载于新款 Mac mini，配备 12 核 CPU、12 核 GPU、双 16 核神经网络引擎，统一内存带宽最高 170GB/s。同时，苹果在新款 Mac Studio 中推出 M5 Ultra，这是 M 系列首款四芯片架构芯片，最高 36 核 CPU、80 核 GPU、512GB 内存，统一内存带宽达 1.2TB/s。 M6 标志着苹果向 2 纳米节点过渡，有望带来显著的每瓦性能提升，并使其芯片在笔记本和台式机领域保持对竞争对手的领先。M5 Ultra 的四芯片设计进一步推高了苹果高端台式机的性能上限，直接面向 3D 渲染、视频制作和本地 AI 推理等专业工作负载。 M5 Ultra 的 1.2TB/s 内存带宽比 M3 Ultra 高出 50%，是苹果迄今最强的芯片。M6 的 2 纳米制程相比上一代 3 纳米预计能带来更高性能或更低功耗，不过实际设备跑分尚未公布。

telegram · zaihuapd · 9月21日 16:32

**背景**: “2 纳米制程”指的是继 3 纳米之后的半导体制造节点，这个数字是营销术语而非物理尺寸，通常能带来更高的晶体管密度和更好的能效。苹果的 M 系列芯片采用统一内存架构，即 CPU、GPU 和神经网络引擎共享同一内存池，从而减少数据复制和延迟。M5 Ultra 的四芯片设计通过苹果的 UltraFusion 封装技术连接四块芯片裸片，实际上是将两个双裸片的 M5 Max 芯片组合成一个系统级芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://applescoop.org/story/m5-ultra-quad-die-architecture-explained">M5 Ultra Explained: How Apple’s First Quad - Die Chip Actually Works</a></li>
<li><a href="https://www.xda-developers.com/apple-silicon-unified-memory/">What is Unified Memory and how does it work on Apple Silicon?</a></li>

</ul>
</details>

**标签**: `#Apple Silicon`, `#hardware`, `#chips`, `#2nm process`, `#Mac`

---