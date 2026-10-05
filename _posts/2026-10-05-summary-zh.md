---
layout: default
title: "Horizon Summary: 2026-10-05 (ZH)"
date: 2026-10-05
lang: zh
---

> 从 51 条内容中筛选出 12 条重要资讯。

---

1. [2026 年诺贝尔生理学或医学奖授予光遗传学发现](#item-1) ⭐️ 9.0/10
2. [vLLM v0.31.0 发布：优化 DeepSeek-V4.1-Flash 并新增快速重启](#item-2) ⭐️ 8.0/10
3. [丹麦 CPR 登记系统遭大规模泄露，880 万人个人数据外泄](#item-3) ⭐️ 8.0/10
4. [Strata 让 125B 的 Qwen 3.8 Flash Next 在 RTX 4090 上以 100+ T/s 运行](#item-4) ⭐️ 8.0/10
5. [CedarDB 将原版 Doom 完整移植到 SQL 中运行](#item-5) ⭐️ 8.0/10
6. [在 10 亿棋局上蒸馏 Stockfish 为 ResNet/ViT 模型，并公开 39 亿数据集](#item-6) ⭐️ 8.0/10
7. [Yandex Music 的 Sona 单一 Transformer 取代 15+ 组件推荐流水线](#item-7) ⭐️ 8.0/10
8. [ARC-AGI-3 Kaggle 分数 30 天内从 7%跃升至 56%](#item-8) ⭐️ 8.0/10
9. [SK 电讯就大规模数据泄露致歉，为全体用户免费更换 USIM 卡](#item-9) ⭐️ 8.0/10
10. [Google 发布 VeriHarness 长程任务自验证框架](#item-10) ⭐️ 8.0/10
11. [华为与高通签署涵盖 5G 和人工智能的广泛多年专利协议](#item-11) ⭐️ 8.0/10
12. [Quad9 拒绝法国 DNS 封锁令，面临每日 58 万欧元罚款](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [2026 年诺贝尔生理学或医学奖授予光遗传学发现](https://www.nobelprize.org/all-nobel-prizes-2026/) ⭐️ 9.0/10

2026 年诺贝尔生理学或医学奖授予卡尔·戴瑟罗特、彼得·赫格曼和格奥尔格·纳格尔，以表彰他们发现光控离子通道并开创光遗传学。该技术使研究人员能够利用光在活体大脑中开启或关闭单个神经细胞的活动。 光遗传学通过以前所未有的精确度控制神经元活动，彻底改变了神经科学，目前已被全球实验室用于研究大脑功能和行为。诺贝尔奖的认可凸显了该技术对理解决策、学习、记忆乃至恢复盲人视力的广泛影响。 光遗传学的工作原理是在特定神经元中表达光敏离子通道（如通道视紫红质），从而通过光脉冲实现毫秒级精度的控制。除了基础研究，它已进入临床试验，例如在一名视网膜色素变性患者中部分恢复了视力。

telegram · zaihuapd · 10月5日 09:33

**背景**: 光遗传学是一种利用光来控制活体组织（通常是神经元）的生物学技术，这些细胞经过基因改造以表达光敏离子通道。该方法由戴瑟罗特、赫格曼和纳格尔开创，建立在早期对光响应微生物视紫红质的发现之上。它已成为系统神经科学的基础工具，使研究人员能够因果性地测试特定神经回路如何参与行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Optogenetics">Optogenetics</a></li>
<li><a href="https://en.wikipedia.org/wiki/Karl_Deisseroth">Karl Deisseroth - Wikipedia</a></li>
<li><a href="https://deisseroth.com/">Karl Deisseroth — A timeline of discovery, from light to life</a></li>

</ul>
</details>

**标签**: `#neuroscience`, `#optogenetics`, `#Nobel Prize`, `#research breakthrough`, `#science news`

---

<a id="item-2"></a>
## [vLLM v0.31.0 发布：优化 DeepSeek-V4.1-Flash 并新增快速重启](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) ⭐️ 8.0/10

vLLM 发布了 v0.31.0，这是一次重大更新，包含来自 307 位贡献者（其中 96 位新贡献者）的 717 次提交。该版本为 DeepSeek-V4.1-Flash 带来了大量性能优化，包括将采用 NVFP4 压缩 KV 缓存的 FlashMLA mega attention 设为 SM100 默认配置，同时通过新的 `vllm preload` CLI 提供快速重启能力，使量化后的权重在引擎重启期间常驻 GPU 内存。 作为使用最广泛的开源大模型推理引擎之一，vLLM 的改进直接影响企业部署大模型的效率与成本。针对 DeepSeek-V4.1-Flash 的优化和快速重启功能可以显著降低生产环境的延迟和停机时间，因此该版本对 AI/ML 基础设施社区具有高度相关性。 该版本包含多项破坏性变更：按请求的多模态 kwargs 现在需要通过 `--trust-request-mm-kwargs` 启用，`tokenizer_mode="slow"` 被移除，`--enable-mamba-fine-grained-prefix-cache` 重命名为 `--enable-mamba-shared-prefix-checkpoint`，通过 `quantization="fp8"` 进行的在线量化被 `fp8_per_tensor` 简写取代。此外还新增了 `--max-num-active-seqs` 和 `--long-prefill-token-threshold` 等调度控制，并加强了前缀缓存键和 LoRA 路径的安全性。

github · khluu · 10月5日 06:44

**背景**: vLLM 是一个用于大语言模型推理和服务的开源框架，最初由加州大学伯克利分校 Sky Computing Lab 开发，核心是用于 Transformer KV 缓存的 PagedAttention 内存管理方法。它支持连续批处理、分布式推理、量化以及兼容 OpenAI 的 API。DeepSeek-V4.1-Flash 是 DeepSeek 推出的多模态大语言模型，基于 45T token 语料训练，采用稀疏注意力并将上下文扩展至 100 万 token。FlashMLA 是 DeepSeek 的优化注意力内核库，为其模型提供支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLLM">VLLM</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek-V4.1-Flash">DeepSeek-V4.1-Flash</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/ FlashMLA : FlashMLA : Efficient Multi-head...</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#release`, `#performance optimization`, `#DeepSeek`

---

<a id="item-3"></a>
## [丹麦 CPR 登记系统遭大规模泄露，880 万人个人数据外泄](https://www.cpr.dk/cpr-nyt/nyhedsarkiv/2026/okt/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger) ⭐️ 8.0/10

丹麦国家民事登记系统（CPR）遭遇大规模未经授权的数据泄露，影响约 880 万人的个人信息，涵盖所有在世的丹麦公民、曾在丹麦居住过的外国公民，甚至包括部分已故人员。据称泄露的数据包括 CPR 号码、年龄、性别、家庭关系、实际住址和受保护住址，以及性别变更记录。 这是丹麦历史上规模最大的国家数据泄露事件之一，暴露的敏感身份数据可能被用于身份盗窃、欺诈，以及对受保护住址人群等弱势群体的定向攻击。该事件引发了关于政府数据安全以及欧盟范围内集中式公民登记系统所带来系统性隐私风险的紧迫讨论。 此次泄露影响所有在世的丹麦公民、曾在丹麦居住过的外国公民以及部分已故人员，涉及受保护住址和性别变更记录等高度敏感字段。事件发生前几天，丹麦技术大学（DTU）刚报告了另一起数据泄露，暴露了在校及过往学生、教职员工的 CPR 号码。

hackernews · clan · 10月5日 08:09 · [社区讨论](https://news.ycombinator.com/item?id=49962012)

**背景**: 在丹麦，每位居民都会被分配一个 CPR 号码（中央人口登记号码），这是用于与丹麦政府机构、医疗系统、银行及许多私营机构打交道的民事登记标识符。由于它相当于一把通用身份钥匙，CPR 数据一旦泄露尤为危险——可能被用来冒充个人、开设账户或获取服务。丹麦此前曾因健康和研究数据匿名化不充分而受到批评，目前该国还在讨论“聊天控制”（Chat Control）提案，批评者认为该提案可能削弱整个欧盟的端到端加密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ihcph.kk.dk/registration-guidance/cpr-registration">CPR registration | International House Copenhagen</a></li>
<li><a href="https://www.norden.org/en/info-norden/civil-registration-denmark">Civil registration in Denmark | Nordic cooperation</a></li>
<li><a href="https://international.kk.dk/live/cpr-registration-and-documents/cpr-registration">CPR registration | City of Copenhagen</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对系统性隐私侵蚀的强烈不满，有人表示因担心数据被滥用，现在连看医生或订机票等日常活动都尽量避免。其他人则提到瑞典公开居民数据的模式作为对比，警告丹麦推动的“聊天控制”可能导致欧盟私人对话大规模泄露，并强调此次泄露范围极大——几乎覆盖丹麦全体人口——且与几天前的 DTU 泄露事件时间相近。

**标签**: `#data-breach`, `#privacy`, `#cybersecurity`, `#denmark`, `#identity-theft`

---

<a id="item-4"></a>
## [Strata 让 125B 的 Qwen 3.8 Flash Next 在 RTX 4090 上以 100+ T/s 运行](https://github.com/Niko1221/Strata) ⭐️ 8.0/10

一个名为 Strata 的新开源推理栈，使 125B 参数的 Qwen 3.8 Flash Next 混合专家模型能够在 RTX 4090 等消费级硬件上以每秒超过 100 个 token 的速度运行。不过，一位社区成员的独立测试发现，Strata 在 50 张图像的视觉基准测试中产生的误差中位数为 154.8 像素，而在 llama.cpp 上运行相同的 GGUF 和视觉适配器权重时仅为 46.5 像素。 这具有重要意义，因为它表明超大型混合专家模型可以在消费级 GPU 上以可用速度本地运行，从而可能减少对云端推理的依赖，适用于智能体编程、工具调用和视觉任务。然而，所报告的精度下降凸显了激进量化与输出质量之间的权衡，这对需要可靠结果的技术人员来说非常重要。 Qwen 3.8 Flash Next 总参数量为 125B，但每个 token 仅激活 6B，另有 51B n-gram 嵌入和 4B MTP，被描述为首个基于将支撑 Qwen 4 的架构构建的开源权重模型。社区报告显示，在配备 128GB DDR5 的 RTX 4090 上速度可达 124 T/s，在配备 96GB DDR4 的 R9700 32GB 上约为 60 T/s，甚至在 Ryzen 6600H 核显上也能达到 10 T/s，但与 llama.cpp 相比的精度差距仍令人担忧。

hackernews · snehesht · 10月4日 12:51 · [社区讨论](https://news.ycombinator.com/item?id=49953495)

**背景**: 混合专家（MoE）模型对每个 token 只激活一部分参数，因此可以在保持总参数量非常大的同时，将推理成本控制得接近小得多的模型。量化通过降低模型权重的精度（例如降至 4 位或更低），使大型模型能够装入有限的 GPU 显存，但更激进的量化可能会降低输出质量。Strata 是一个专门为在消费级硬件上运行 Qwen 3.8 Flash Next 而设计的开源推理引擎，而 llama.cpp 是一个广泛使用的推理框架，以其量化支持和精度而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen / Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://github.com/qwenlm/qwen3.8-flash-next">GitHub - QwenLM/ Qwen 3 . 8 - Flash - Next : Qwen 3 . 8 - Flash - Next is the...</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一：一些用户对速度和易用性印象深刻，有人报告在 RTX 4090 上达到 124 T/s，还有人认为它在 R9700 32GB 上具有颠覆性。然而，a11r 对低于 4 位量化可能导致质量下降表示怀疑，Jackson__ 则提供了基准测试，显示在相同权重下 Strata 的误差中位数为 154.8 像素，而 llama.cpp 为 46.5 像素，这给热情泼了冷水。

**标签**: `#LLM inference`, `#quantization`, `#consumer hardware`, `#Qwen`, `#performance benchmarking`

---

<a id="item-5"></a>
## [CedarDB 将原版 Doom 完整移植到 SQL 中运行](https://cedardb.com/blog/sqldoom/) ⭐️ 8.0/10

CedarDB 的开发者将 1993 年原版 Doom 的游戏逻辑和渲染器完全移植为 SQL 查询，在数据库内以约 35 FPS 运行游戏，多人死亡竞赛模式也能正常工作。游戏逻辑约为 5900 行 SQL 代码，比原版 C 实现还要少。 该项目挑战了人们对 SQL 能力边界的常见假设，表明现代 SQL 引擎足以表达像完整游戏引擎这样复杂的有状态逻辑。它引发了关于业务规则和复杂领域逻辑是否也能用 SQL 实现的讨论，这有可能提升企业系统的可维护性和并发能力。 该移植将 SQL 查询规划当作状态机来使用，并通过数据库引擎内的 tic 序列驱动游戏循环；得益于数据模型，死亡竞赛模式几乎无需额外工作即可运行。开发者还探索了编译 SQL 以提升性能，不过在数据库中运行游戏本质上仍是非常规做法。

hackernews · Vaslo · 10月3日 22:14 · [社区讨论](https://news.ycombinator.com/item?id=49948300)

**背景**: Doom 由 id Software 于 1993 年发布，是一款里程碑式的第一人称射击游戏，其引擎架构（id Tech 1）将游戏逻辑与渲染分离，并使用 WAD 文件存储资源。SQL 是查询关系数据库的标准语言，现代数据库引擎支持 PL/SQL、T-SQL 等过程化扩展，增加了循环和分支能力。将 Doom 移植到 SQL 意味着把游戏循环、状态更新和渲染重新实现为数据库查询，而非传统的程序化代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cedardb.com/blog/sqldoom/">We ported the original Doom to SQL | CedarDB</a></li>
<li><a href="https://en.wikipedia.org/wiki/Id_Tech">id Tech - Wikipedia</a></li>
<li><a href="https://vldb.org/pvldb/vol14/p1378-ramachandra.pdf">Procedural Extensions of SQL</a></li>

</ul>
</details>

**社区讨论**: 评论者印象深刻但观点分歧：一些人称赞 SQL 表达复杂逻辑的能力，并分享了 pg_shell、pg_gpt2 等相关项目；另一些人则称其为“工程渎职”，并指出将 SQL 表作为游戏状态真实来源时遇到的死锁和扩展性等实际痛点。总体情绪是对技术壮举的钦佩与对其实用性的怀疑并存。

**标签**: `#SQL`, `#Doom`, `#game development`, `#database`, `#engineering`

---

<a id="item-6"></a>
## [在 10 亿棋局上蒸馏 Stockfish 为 ResNet/ViT 模型，并公开 39 亿数据集](https://www.reddit.com/r/MachineLearning/comments/1wxz5qq/distilling_stockfish_on_a_billion_positions_full/) ⭐️ 8.0/10

一位开发者将 Stockfish 国际象棋引擎的价值函数蒸馏到一个 ResNet 与 ViT 结合的神经网络中，训练使用了 Gigafish 数据集中的 10 亿个棋局。同时，完整的 39 亿棋局数据集已在 Hugging Face 上公开发布，该数据集由 37 个月的 Lichess 对局构建而成。 这项工作表明，神经网络可以比 Stockfish 引擎本身更快地逼近其深度受限搜索的价值函数，有望成为 NNUE 的竞争性替代方案。同时，公开 39 亿棋局数据集也为国际象棋 AI 和知识蒸馏研究提供了宝贵资源。 作者发现，纯视觉 Transformer 理解棋盘的速度较慢，而 CNN 因其固有的几何归纳偏置在训练初期更有效；将两种架构结合取得了最佳效果。保持搜索深度恒定至关重要，因为目标是在固定深度受限搜索下逼近价值函数。

reddit · r/MachineLearning · /u/microscope1024 · 10月5日 04:11

**背景**: Stockfish 是一款免费开源的国际象棋引擎，多年来一直是世界上最强的引擎之一，自 2020 年起它使用高效可更新神经网络（NNUE）进行评估。知识蒸馏是一种将知识从大模型迁移到小模型的技术，通常用于加速评估或在较弱硬件上部署。Gigafish 数据集是从 Lichess 对局中提取的大规模棋局集合，旨在用于训练国际象棋神经网络。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stockfish_NNUE">Stockfish NNUE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation</a></li>
<li><a href="https://huggingface.co/datasets/lukesalamone/gigafish-3.8b-d10">lukesalamone/ gigafish -3.8b-d10 · Datasets at Hugging Face</a></li>

</ul>
</details>

**标签**: `#chess`, `#knowledge-distillation`, `#deep-learning`, `#dataset`, `#stockfish`

---

<a id="item-7"></a>
## [Yandex Music 的 Sona 单一 Transformer 取代 15+ 组件推荐流水线](https://www.reddit.com/r/MachineLearning/comments/1wy4qxm/sona_one_transformer_replaced_our_15_candidate/) ⭐️ 8.0/10

Yandex Music 推出了 Sona，这是一个单一的生成式 Transformer，在 A/B 测试中取代了其生产推荐系统中 15 个以上的候选生成器、预排序器和排序器。在智能音箱上为期 7 天、每组 15% 用户的测试中，Sona 相比生产对照组实现了 +4.53% 的活跃用户和 +6.30% 的总收听时长，两者均在 p < 0.01 水平上显著。 这表明单一的端到端生成模型可以在真实的生产 A/B 测试中取代复杂的多阶段推荐级联，有可能简化架构并降低工程开销。如果长期测试得到验证，它可能会影响整个行业大规模推荐系统的设计方式。 Sona 使用 History Compression 技术读取最多 8,192 个事件，将历史拆分为较早的 6,144 个和最近的 2,048 个事件，通过交叉注意力和一个全历史自注意力层交换信息，大致将推理成本减半。目录覆盖率低于生产系统，团队计划调查原因，长期 A/B 测试正在进行中。

reddit · r/MachineLearning · /u/SettingAccording8986 · 10月5日 10:07

**背景**: 传统的生产推荐系统采用多阶段级联：候选生成器从大目录中检索一部分物品，预排序器进行过滤，重型排序器使用数百个工程特征对最终列表打分。这种设计的存在是因为在几十毫秒内对每次请求的百万级物品进行打分，用单一模型是不可行的。生成式推荐器和高效注意力机制的最新进展使单模型替代方案变得更加实用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/10/05/yandex-introduces-sona-a-single-generative-recommender-that-replaces-entire-recommendation-cascade/">Yandex Introduces Sona: A Single Generative Recommender That...</a></li>
<li><a href="https://preptima.com/questions/machine-learning/recommenders-and-ranking/candidate-generation-then-ranking">Candidate Generation and Ranking | Recommenders — Preptima</a></li>

</ul>
</details>

**标签**: `#recommender systems`, `#transformer`, `#efficient attention`, `#production ML`, `#A/B testing`

---

<a id="item-8"></a>
## [ARC-AGI-3 Kaggle 分数 30 天内从 7%跃升至 56%](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 8.0/10

根据 r/MachineLearning 上的一篇 Reddit 帖子，过去 30 天内，Kaggle ARC-AGI-3 排行榜的最高分数从约 7%上升到 56%，这些成绩由运行在某种 harness（执行框架）中的小型本地模型取得。发帖人指出排行榜截图略有过时，并询问社区如何看待这一快速攀升。 ARC-AGI-3 明确旨在衡量类人的流体智能，并展示人类仍优于机器的地方，因此在 Kaggle 赛道上跃升至 56%意味着这类基准推理任务正以超出预期的速度被攻克。如果小型本地模型都能达到这一水平，就会引发疑问：剩余的差距有多少来自真正的推理能力，又有多少来自 harness 工程和针对基准的调优。 ARC Prize 2026 的 ARC-AGI-3 赛道规则限制参赛者只能使用小型本地模型，因此这些提升来自 harness 设计和智能体脚手架，而非大型前沿模型。ARC-AGI-3 是一个交互式基准，智能体必须在没有指令的情况下探索新环境、即时推断目标并构建可适应的世界模型，每一帧由 4096 个 ASCII 字符组成，具有空间含义而非语义含义。

reddit · r/MachineLearning · /u/we_are_mammals · 10月4日 10:24 · [社区讨论](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arcαgi3_scores_on_kaggle_just_went_from_7_to/)

**背景**: ARC-AGI（Abstraction and Reasoning Corpus for Artificial General Intelligence，通用人工智能抽象与推理语料库）是一系列旨在测试通用推理能力而非记忆知识的基准。ARC-AGI-3 从静态谜题网格转向交互式环境，智能体必须像人类探索陌生游戏那样持续行动、观察和学习。Kaggle 上的 ARC Prize 2026 竞赛设有该赛道，并提供奖金和规则，推动参赛者采用高效的小模型方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC - AGI - 3</a></li>

</ul>
</details>

**社区讨论**: 该 Reddit 帖子内容简短，所提供的内容中并未包含实际评论文字，但其表述引发了讨论：在专为展示人类优势而设计的基准上，harness 中的小型本地模型究竟是真的击败了普通人，还是这一结果只是针对基准的优化。

**标签**: `#ARC-AGI`, `#benchmark`, `#AI`, `#machine learning`, `#Kaggle`

---

<a id="item-9"></a>
## [SK 电讯就大规模数据泄露致歉，为全体用户免费更换 USIM 卡](https://t.me/zaihuapd/44206) ⭐️ 8.0/10

韩国最大电信运营商 SK 电讯（SKT）确认其内部 HSS 服务器遭黑客攻击，导致超过 2500 万用户的敏感数据泄露，包括 IMEI、SN、ICCID、PIN2/PUK2、eID、加密 K 值和私钥等信息。SKT CEO 已公开致歉，并宣布为所有希望更换的 SKT 用户（含其网络下的 MVNO 用户，部分设备除外）免费更换 USIM 卡，同时报销近期已付费更换的用户。 这是近年来规模最大的电信数据泄露事件之一，影响超过 2500 万人，并暴露了可能导致 SIM 卡克隆或身份盗用的关键认证凭证。该事件凸显了核心电信基础设施的脆弱性，并为行业事件响应树立了先例，可能促使其他运营商重新评估其安全措施。 被攻破的 HSS 服务器存储了用于保护用户身份认证的密钥（K 值）和私钥，这些是防止未授权访问的关键。免费更换 USIM 卡旨在通过发放带有新凭证的新卡来降低风险，但部分设备（如某些物联网或较旧型号）可能不符合条件，且如果 IMEI 等其他数据被滥用，用户仍可能面临残余风险。

telegram · zaihuapd · 10月4日 09:02

**背景**: HSS（归属用户服务器）是 4G/5G 网络中的核心数据库，负责管理用户配置文件、认证和安全密钥。USIM 卡是用于 3G/4G/5G 设备的通用用户身份模块，安全存储国际移动用户识别码（IMSI）及相关密钥以进行网络认证。HSS 服务器被攻破尤为严重，因为它可能破坏移动通信的信任根，使攻击者能够冒充用户或拦截通话和数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.p1sec.com/blog/home-subscriber-server-hss">Home Subscriber Server ( HSS ): The Backbone of Modern Telecom ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/USIM_(card)">USIM (card)</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#data breach`, `#telecom`, `#privacy`, `#incident response`

---

<a id="item-10"></a>
## [Google 发布 VeriHarness 长程任务自验证框架](https://arxiv.org/abs/2610.00972v1) ⭐️ 8.0/10

Google 研究团队发布了 VeriHarness，这是一个智能体验证框架，使用生成候选结果的同一模型来执行验证：对存在分歧的主张核查环境证据，对达成共识的主张主动提出挑战，并据此选择、修订或重建最终结果。该框架在 5 个长程任务基准、2 个模型上取得了最高的选择分，经证据驱动修订后，较单次生成平均提升 Gemini 3.5 Flash 6.2 分、Claude Opus 4.8 6.4 分，并公开了约 2.6 万条 rollouts。 这是一个无需训练、即插即用的验证框架，在没有参考答案或评分标准的情况下也能提升长程 LLM 智能体的表现，有望让智能体 AI 在缺乏标准答案的真实多步任务中更加可靠。同时，公开的 2.6 万条 rollouts 也为研究智能体验证与评估提供了宝贵的公开数据集。 VeriHarness 被称为首个面向长程任务的智能体验证框架，无需训练、即插即用，可跨基准和模型使用，依赖分歧消解、共识挑战和证据驱动修订，而非外部评分器。所报告的提升是在 5 个长程任务基准、2 个模型上相对单次生成测得的，框架代码已在 google-research/veriharness 的 GitHub 仓库中公开。

telegram · zaihuapd · 10月4日 13:32

**背景**: 长程任务要求 AI 智能体在延长的步骤序列中做出大量决策，无法通过单次提示或简短交互可靠完成。由于纯生成在长依赖链上容易发生漂移，因此在执行前或执行中进行验证，正日益被视为让智能体保持可靠的一种手段。Rollout 是 LLM 在训练或评估过程中采样生成的轨迹，将其公开可以让研究者系统地分析智能体行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2610.00972">VeriHarness : Scaling Agentic Verification for Long-Horizon Tasks</a></li>
<li><a href="https://huggingface.co/papers/2610.00972">Paper page - VeriHarness : Scaling Agentic Verification for...</a></li>
<li><a href="https://github.com/google-research/veriharness/issues">Issues · google -research/ veriharness · GitHub</a></li>

</ul>
</details>

**标签**: `#LLM`, `#verification`, `#long-horizon tasks`, `#Google`, `#benchmark`

---

<a id="item-11"></a>
## [华为与高通签署涵盖 5G 和人工智能的广泛多年专利协议](https://www.huawei.com/en/news/2026/10/qualcomm-broad-patent-agreement) ⭐️ 8.0/10

华为与高通宣布达成一项为期多年、范围广泛的专利交叉许可协议，涵盖 5G、计算、人工智能和网络等领域；高通还将购买华为部分美国专利，并获得华为逻辑折叠芯片制造技术的专利许可。该交易尚待监管批准，预计将使华为专利许可协议的累计合同价值超过 69 亿美元。 这是两家公司之间首个涵盖 5G 技术的许可协议，标志着全球科技行业格局的重大转变，并可能缓解华为与美国主要芯片厂商之间长期存在的专利紧张关系。这也强化了华为的知识产权变现战略，其知识产权授权业务自 2021 年起已实现正向收入。 该协议涵盖双方在 5G、计算、人工智能和网络领域的专利组合交叉许可，并包括高通收购华为部分美国专利以及获得华为逻辑折叠芯片制造技术的许可。该交易需获得必要的监管批准后方可完成。

telegram · zaihuapd · 10月5日 06:45

**背景**: 专利交叉许可协议允许公司相互使用对方的专利技术，从而避免侵权诉讼，通常能创造协同效应并降低诉讼成本。华为一直在积极将其专利组合变现，而此次与高通——美国主要芯片设计商——达成的协议，标志着其许可范围显著扩展至 5G 和人工智能领域。逻辑折叠芯片制造是华为的一项技术，它在单颗芯片的逻辑层内重构电路拓扑，与先进封装或 3D 堆叠方法不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.shiftdelete.net/huawei-and-qualcomm-sign-landmark-5g-patent-licensing-agreement/">Huawei and Qualcomm Sign Landmark 5 G Patent Licensing Agreement</a></li>
<li><a href="https://www.techzine.eu/news/infrastructure/144742/huawei-and-qualcomm-sign-broad-patent-agreement/">Huawei and Qualcomm sign broad patent agreement - Techzine Global</a></li>
<li><a href="https://www.ithome.com/1/009/852.htm">高通与华为达成 逻 辑 折 叠 芯 片 技 术 相关专利授权，韬定律加速出海 - IT...</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#Qualcomm`, `#patent-licensing`, `#5G`, `#AI`

---

<a id="item-12"></a>
## [Quad9 拒绝法国 DNS 封锁令，面临每日 58 万欧元罚款](https://torrentfreak.com/dns-resolver-quad9-rejects-french-piracy-blocks-weighs-exit-as-bein-seeks-up-to-e580k-a-day/) ⭐️ 8.0/10

瑞士非营利 DNS 服务商 Quad9 拒绝执行法国法院要求其封锁 58 个盗版相关域名的命令，beIN Sports 正寻求按每个域名每日 1 万欧元、合计每日最高 58 万欧元的罚款。巴黎法院上周四开庭审理此案，预计三周内作出裁决。 此案凸显了 DNS 服务商与国家强制审查之间日益加剧的冲突，并可能为 DNS 解析器如何处理特定司法管辖区的封锁要求树立全球先例。Quad9 的原则性立场可能影响其他注重隐私的 DNS 运营商，并塑造互联网治理与数字权利的未来。 Quad9 表示从未封锁过任何域名，且由于不收集用户数据，无法仅针对法国用户执行封锁，因此只能选择全球封锁或退出法国市场。它还批评法国 7 月通过的可实时自动加黑域名的法律「鲁莽且危险」。

telegram · zaihuapd · 10月5日 08:05

**背景**: Quad9 是一家瑞士非营利 DNS 解析器，其创始章程将隐私作为首要目标，因此不记录用户的 IP 地址。DNS 解析器负责将人类可读的域名转换为 IP 地址，而在 DNS 层面进行封锁是执行版权相关网站封锁的常见手段。法国日益推动自动化、实时的域名黑名单机制以打击盗版，尤其是体育赛事直播盗版。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://quad9.net/">Quad 9 | A public and free DNS service for a better security and privacy</a></li>

</ul>
</details>

**标签**: `#DNS`, `#Internet Censorship`, `#Privacy`, `#Digital Rights`, `#France`

---