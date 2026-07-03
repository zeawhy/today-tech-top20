---
layout: default
title: "Horizon Summary: 2026-07-03 (ZH)"
date: 2026-07-03
lang: zh
---

> 从 42 条内容中筛选出 8 条重要资讯。

---

1. [Wordgard：ProseMirror 创建者推出的新富文本编辑器](#item-1) ⭐️ 8.0/10
2. [Crustc：将整个 Rust 编译器翻译为 C 语言](#item-2) ⭐️ 8.0/10
3. [CDD 仅通过 logits 恢复 LLM 微调数据](#item-3) ⭐️ 8.0/10
4. [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](#item-4) ⭐️ 8.0/10
5. [华为发布搭载昇腾 950PR 的 Atlas 350 加速卡](#item-5) ⭐️ 8.0/10
6. [华为 Mate 80 Pro 游戏能效超越骁龙 8 Gen3](#item-6) ⭐️ 8.0/10
7. [NASA 发射救援卫星拯救老化雨燕望远镜](#item-7) ⭐️ 8.0/10
8. [腾讯阿图因 AI 在 CyberGym 测试中击败 Mythos](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Wordgard：ProseMirror 创建者推出的新富文本编辑器](https://wordgard.net/) ⭐️ 8.0/10

Wordgard 是 ProseMirror 创建者发布的一款新的浏览器内富文本编辑器，提供了改进的开发者体验和静态类型支持。 这很重要，因为它提供了 ProseMirror 的现代替代方案，具有更好的 TypeScript 集成，可能简化需要静态类型文档模型的团队的开发工作。 Wordgard 与 ProseMirror 共享许多概念，但并非升级路径；切换需要大量重写。该编辑器专注于开发者体验和静态类型。

hackernews · indy · 7月3日 08:50 · [社区讨论](https://news.ycombinator.com/item?id=48772573)

**背景**: ProseMirror 是一个广泛使用的开源 Web 富文本编辑器框架，但缺乏内置的静态类型支持。Wordgard 旨在通过从头提供静态类型 API 来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prosemirror.net/">ProseMirror</a></li>

</ul>
</details>

**社区讨论**: 社区对新编辑器感到兴奋，许多人称赞其设计和技术深度。一些用户对缺乏从 ProseMirror 的升级路径以及切换所需的工作量表示担忧。

**标签**: `#rich-text editor`, `#ProseMirror`, `#web development`, `#open source`, `#JavaScript`

---

<a id="item-2"></a>
## [Crustc：将整个 Rust 编译器翻译为 C 语言](https://github.com/FractalFir/crustc) ⭐️ 8.0/10

一个名为 crustc 的项目成功将整个 Rust 编译器（rustc）翻译为 C 语言，从而能够在没有 LLVM 或 GCC 支持的平台上进行引导编译。 这一突破显著提升了编译器的可移植性，使 Rust 能够在缺乏 LLVM 或 GCC 后端的旧式或小众硬件上运行，并且通过多样双重编译提供了一种验证官方 Rust 编译器是否存在后门的新方法。 该项目是已知的第 14 次将 Rust 编译为 C 的尝试，它翻译了整个 rustc 代码库，而不仅仅是子集。作者指出，翻译为 C 比翻译为 LLVM IR 更容易，并且让 GCC 进行优化可能带来实用的性能。

hackernews · Philpax · 7月2日 22:57 · [社区讨论](https://news.ycombinator.com/item?id=48768464)

**背景**: Rust 的主要编译器 rustc 使用 LLVM 作为后端，这限制了其对 LLVM 目标平台的支持。从源代码引导编译 Rust 通常需要已有的 Rust 编译器，这为新平台带来了先有鸡还是先有蛋的问题。将 rustc 翻译为 C 打破了这种依赖，因为 C 编译器几乎在所有平台上都可用。

**社区讨论**: 社区对该项目的技术新颖性和奉献精神表示高度赞赏，有评论者称其为“原创艺术品”。几位用户讨论了使用 crustc 进行多样双重编译以测试官方 Rust 编译器中的后门，其他人则提到了 LLVM 的 C 后端被移除后又恢复的历史背景。

**标签**: `#rust`, `#compiler`, `#transpilation`, `#bootstrapping`, `#systems programming`

---

<a id="item-3"></a>
## [CDD 仅通过 logits 恢复 LLM 微调数据](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

研究人员提出了对比解码差异法（CDD），这是一种灰盒方法，仅通过 logits 访问即可从 LLM 中恢复逐字微调数据，无需模型权重或激活值。CDD 在四个模型家族的 20 个生物体-模型对中的 19 对上实现了 4+/5 的逐字恢复分数，优于白盒方法激活差异透镜（ADL）。 这项工作凸显了 LLM 微调中重大的隐私和安全风险，因为它表明只需极少的访问权限即可提取敏感训练数据。同时，它为审计和理解模型在微调过程中学到了什么提供了强大工具，可能提高 AI 系统的透明度。 CDD 无需针对每个模型进行校准、无需选择层、无需探测语料库，在所有实验中使用单一默认配置。一个意外的发现是，在语义无关的微调领域中反复出现名字“Dr. Elena Rodriguez”，这追溯到 Claude Sonnet 3.6 在生成合成数据时对虚构科学家名字的偏好。

reddit · r/MachineLearning · /u/CebulkaZapiekana · 7月3日 19:01

**背景**: 模型差异分析旨在检测微调模型相对于基础模型学到了什么。先前的工作激活差异透镜（ADL）需要完整的权重访问，且只能恢复模糊的领域级描述。CDD 在 logits 分布上操作，使其成为一种灰盒方法，既更易访问又更有效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.25902">Reading the Finetuning Prior: Verbatim Content Recovery via Contrastive ...</a></li>
<li><a href="https://arxiv.org/html/2605.25902v2">Reading the Finetuning Prior: Verbatim Content Recovery via Contrastive ...</a></li>
<li><a href="https://www.machinebrief.com/news/unlocking-ais-hidden-memories-with-contrastive-decoding-9a3m">Unlocking AI's Hidden Memories with Contrastive Decoding</a></li>

</ul>
</details>

**标签**: `#LLM`, `#privacy`, `#model diffing`, `#finetuning`, `#security`

---

<a id="item-4"></a>
## [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](https://t.me/zaihuapd/42327) ⭐️ 8.0/10

Anthropic 指控阿里巴巴利用约 2.5 万个欺诈账户，在 2026 年 4 月 22 日至 6 月 5 日期间与 Claude 进行了超过 2880 万次交互，发动大规模“蒸馏攻击”以窃取其 AI 模型能力。 此事件凸显了 AI 模型安全和知识产权盗窃日益增长的担忧，对中美科技竞争以及先进 AI 技术出口管制的执行具有重大影响。 Anthropic 声称这是针对该公司迄今已知最大规模的蒸馏攻击，涉及阿里巴巴及其 AI 实验室 Qwen。作为回应，阿里巴巴据报道下令员工卸载所有 Anthropic 产品，包括 Claude 模型和 Claude Code，禁令于 2026 年 7 月 10 日生效。

telegram · zaihuapd · 7月3日 06:21

**背景**: 模型蒸馏是一种让较弱模型通过学习较强模型的输出来复制其能力的技术。在未经授权的情况下对专有模型使用该技术构成知识产权盗窃。Anthropic 一直支持出口管制以维持美国在 AI 领域的领先地位，而蒸馏攻击可能通过让外国实体获取先进能力来破坏这些管制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained">AI Model Distillation Attacks: What They Are and Why They Matter | MindStudio</a></li>

</ul>
</details>

**标签**: `#AI security`, `#model distillation`, `#Anthropic`, `#Alibaba`, `#intellectual property`

---

<a id="item-5"></a>
## [华为发布搭载昇腾 950PR 的 Atlas 350 加速卡](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

在华为中国合作伙伴大会 2026 上，华为正式发布并上市了搭载全新昇腾 950PR 处理器的 AI 训练推理加速卡 Atlas 350，声称其算力达到英伟达 H20 的 2.87 倍，并支持 FP4 精度。 这一发布标志着华为在 AI 加速器市场的强势进军，以国产芯片提供更高性能和更低成本挑战英伟达的主导地位，可能重塑中国的 AI 硬件格局。 Atlas 350 配备 112 GB HBM 内存，支持 FP4 低精度推理，单卡可加载 70B 参数模型，显著降低推理延迟和投资成本。

telegram · zaihuapd · 7月3日 08:35

**背景**: 华为昇腾 950PR 芯片基于 SIMD 架构，算力达 1 PFLOPS（FP8）/ 2 PFLOPS（FP4），支持多种数据格式。其定价为 7 万元人民币，约为英伟达 H200 在中国市场报价的三分之一，性能达到其近 80%。该芯片是华为 AI 芯片路线图的一部分，后续还有 950DT、960 等型号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wallstreetcn.com/articles/3755816">华为昇腾AI芯片路线图公布：明年Q1推出昇腾950PR，采用自研HBM</a></li>
<li><a href="https://cloud.tencent.com/developer/article/2652707">昇腾950PR加持！华为Atlas 350上市：算力是H20的3倍-腾讯云开发者社区-腾讯云</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2026893491125467122">华为昇腾950PR正式量产！7万定价打穿英伟达，国产AI芯片终于站起来了 - 知乎</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#Huawei`, `#accelerator`, `#FP4`, `#deep learning`

---

<a id="item-6"></a>
## [华为 Mate 80 Pro 游戏能效超越骁龙 8 Gen3](https://www.bilibili.com/video/BV1F7T46wEyT) ⭐️ 8.0/10

极客湾评测显示，搭载麒麟 9030 芯片的华为 Mate 80 Pro 系列，凭借原生鸿蒙优化，游戏能效超越了骁龙 8 Gen3。 这表明软硬件协同优化可以克服理论硬件劣势，可能重塑移动芯片市场的竞争格局。 麒麟 9030 Pro 采用 9 核 14 线程 CPU 和 6 核马良 935 GPU，晶体管规模约 150 亿。在《原神》最高画质 60 帧下，Mate 80 Pro Max 整机功耗仅 4.9W，能效优于骁龙 8 Gen3。

telegram · zaihuapd · 7月3日 13:27

**背景**: 华为麒麟芯片面临美国制裁，限制了其获取先进制程的能力。鸿蒙是华为专为多设备无缝协同设计的操作系统。该评测凸显了原生应用优化如何弥补硬件局限。

**标签**: `#Huawei`, `#Kirin 9030`, `#HarmonyOS`, `#mobile chips`, `#gaming performance`

---

<a id="item-7"></a>
## [NASA 发射救援卫星拯救老化雨燕望远镜](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 8.0/10

7 月 3 日，NASA 发射了名为 LINK 的私人救援卫星，将与老化的雨燕空间望远镜会合，并将其轨道抬升约 240 公里，防止其最早在今年 10 月坠入大气层。 这次任务标志着私人航天器首次尝试捕获并服务美国政府的无人卫星，可能开启在轨服务和太空碎片减缓的新时代。 LINK 航天器将使用机械臂抓住雨燕望远镜，然后通过推进器缓慢抬升其轨道。如果成功，雨燕最快可于 9 月恢复观测。

telegram · zaihuapd · 7月3日 15:43

**背景**: 雨燕空间望远镜于 2004 年发射，已研究伽马射线暴和其他宇宙现象超过 20 年。由于太阳活动增强，其轨道衰减速度快于预期，威胁到任务寿命。在轨服务——即一艘航天器为另一艘加油或抬升轨道——是一个新兴领域，旨在延长卫星寿命并减少太空碎片。

**标签**: `#space`, `#NASA`, `#satellite servicing`, `#space debris`, `#astronomy`

---

<a id="item-8"></a>
## [腾讯阿图因 AI 在 CyberGym 测试中击败 Mythos](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 8.0/10

腾讯玄武实验室的阿图因 AI 在 CyberGym 网络安全基准测试中获得 84.0%的得分，超过 Anthropic 的 Claude Mythos Preview，且消耗预算不到 Mythos 的 0.1%。它还在 curl、OpenSSL、Python cryptography 等项目中发现了多个 Mythos 未检出的高危漏洞。 这表明开源、低成本的 AI 模型在漏洞检测方面可以超越专有模型，可能推动高级网络安全工具的普及。同时，它也凸显了 AI 在广泛使用的开源软件中发现关键漏洞方面的作用日益增强。 阿图因 AI 基于开源模型 GLM-5.1 构建，可本地部署。它在伯克利 BVI 真实世界漏洞榜单中严重程度排名第 1，总数排名第 5。

telegram · zaihuapd · 7月3日 16:12

**背景**: CyberGym 是由加州大学伯克利分校主导的网络安全基准测试，用于评估 AI 系统的漏洞检测能力。Mythos 是 Anthropic 在“玻璃翼计划”下开发的网络安全 AI 系统。这一对比凸显了开源模型相对于专有模型的效率优势。

**标签**: `#AI`, `#cybersecurity`, `#vulnerability detection`, `#open-source`, `#benchmark`

---