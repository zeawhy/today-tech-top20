---
layout: default
title: "Horizon Summary: 2026-10-06 (ZH)"
date: 2026-10-06
lang: zh
---

> 从 66 条内容中筛选出 9 条重要资讯。

---

1. [2026 年诺贝尔物理学奖授予弗朗西斯·哈尔岑，表彰冰立方中微子观测站](#item-1) ⭐️ 9.0/10
2. [vLLM v0.31.0 强化 DeepSeek-V4.1-Flash 推理并新增快速重启权重缓存](#item-2) ⭐️ 8.0/10
3. [Reflection 发布 501B 开源权重 MoE 模型 Beam](#item-3) ⭐️ 8.0/10
4. [苹果的围墙花园与 AI 智能体和黑客的对决](#item-4) ⭐️ 8.0/10
5. [高通获华为 LogicFolding 芯片专利授权，达成里程碑协议](#item-5) ⭐️ 8.0/10
6. [3 亿参数字节级 Transformer 仅凭合成非语言先验即可在上下文中学习真实语言](#item-6) ⭐️ 8.0/10
7. [用 39 亿局面数据集将 Stockfish 蒸馏进 ResNet/ViT 模型](#item-7) ⭐️ 8.0/10
8. [Sona：单个 Transformer 取代 Yandex Music 的 15+组件推荐系统](#item-8) ⭐️ 8.0/10
9. [OpenAI 将在欧盟为部分 AI 生成文本添加隐形水印](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [2026 年诺贝尔物理学奖授予弗朗西斯·哈尔岑，表彰冰立方中微子观测站](https://www.nobelprize.org/prizes/physics/2026/press-release/) ⭐️ 9.0/10

2026 年 10 月 6 日，瑞典皇家科学院宣布将 2026 年诺贝尔物理学奖授予美国威斯康星大学麦迪逊分校的弗朗西斯·哈尔岑，以表彰他对冰立方中微子观测站的决定性贡献以及发现天体物理起源的高能中微子。哈尔岑于 1988 年首次提出在南极冰层中探测中微子的构想，并领导建成了约一立方公里、布设光传感器的冰立方，该观测站于 2011 年完工，此后陆续捕获到来自宇宙的高能中微子。 该奖项标志着中微子天文学这一新领域的奠基获得认可，该领域利用几乎无质量、极少发生相互作用的粒子来观测宇宙中最高能的过程，而这些过程对光学望远镜而言是不可见的。这也验证了数十年来在南极开展的大规模探测装置建设，并可能推动多信使天文学（与引力波、伽马射线观测并列）获得更多资助与关注。 冰立方由数千个数字光学模块组成，这些模块被布设在南极冰层下 1450 至 2450 米深处的缆绳上，用于探测中微子发生相互作用时产生的带电粒子所发出的切伦科夫辐射。该奖项奖金为 1200 万瑞典克朗；此外，2026 年 2 月宣布的观测站升级是该设施自建成以来的首次重大扩建。

telegram · zaihuapd · 10月6日 09:54

**背景**: 中微子是一种几乎无质量、电中性的基本粒子，极少与物质发生相互作用，因此能够沿直线穿越浩瀚的宇宙距离而不被磁场偏转。中微子天文学通过大型地下或冰下观测站探测这些粒子，与传统的基于光的观测手段形成互补。冰立方建在南极阿蒙森-斯科特站，是此类探测器中规模最大的一个，以一立方公里的清澈南极冰层作为其探测靶体积。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IceCube_Neutrino_Observatory">IceCube Neutrino Observatory</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neutrino_astronomy">Neutrino astronomy</a></li>

</ul>
</details>

**社区讨论**: 评论者对这种在南极冰层中建造探测器的胆识和科幻感表示赞赏，其中一位指出，这类无法在附近冰川先做原型验证的昂贵项目在争取经费时极为困难。还有人提到了哈尔岑关于夸克与轻子的教科书，并感慨在世的诺贝尔奖得主数量之多。

**标签**: `#Nobel Prize`, `#Physics`, `#Neutrino Astronomy`, `#IceCube`, `#Scientific Breakthrough`

---

<a id="item-2"></a>
## [vLLM v0.31.0 强化 DeepSeek-V4.1-Flash 推理并新增快速重启权重缓存](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) ⭐️ 8.0/10

vLLM 发布了 v0.31.0，这是一个包含来自 307 位贡献者的 717 次提交的重大更新，带来了大量 DeepSeek-V4.1-Flash 推理优化，例如采用 NVFP4 压缩 KV 缓存的 FlashMLA mega attention、DeepGEMM 稀疏 MQA logits 以及多种融合内核。该版本还引入了新的 `vllm preload` CLI，通过启动权重缓存守护进程，使量化后的权重在引擎重启期间常驻 GPU 显存，并提供了基于 CRIU 的实验性引擎快照功能。 vLLM 是广泛使用的高性能 LLM 推理引擎，这些优化可以显著降低服务 DeepSeek-V4.1-Flash 等大型模型时的延迟和显存占用。快速重启功能通过缩短引擎重启时间，解决了常见的运维痛点，对生产环境部署和整个 LLM 服务生态都具有重要意义。 该版本包含破坏性变更：按请求的多模态 kwargs 现在需要通过 `--trust-request-mm-kwargs` 启用，`tokenizer_mode="slow"` 被移除，通过 `quantization="fp8"` 进行的在线量化被 `fp8_per_tensor` 简写取代。此外还新增了 `--max-num-active-seqs` 等调度控制，并重构了等待队列，使已持有 KV 块的请求优先被调度。

github · khluu · 10月5日 06:44

**背景**: vLLM 是一个用于 LLM 推理和服务的开源框架，最初由加州大学伯克利分校 Sky Computing Lab 开发，核心是用于高效 KV 缓存内存管理的 PagedAttention。它支持连续批处理、分布式推理、量化和 OpenAI 兼容 API。FlashMLA 是 DeepSeek 优化的多头潜在注意力内核库，NVFP4 是一种 4 位浮点格式，用于压缩 KV 缓存并降低内存带宽。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLLM">VLLM</a></li>
<li><a href="https://github.com/puwei0000/deepseek-ai_FlashMLA">GitHub - puwei0000/deepseek-ai_ FlashMLA : FlashMLA : Efficient...</a></li>
<li><a href="https://www.lmsys.org/">LMSYS Org</a></li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#gpu-kernels`, `#model-serving`, `#release`

---

<a id="item-3"></a>
## [Reflection 发布 501B 开源权重 MoE 模型 Beam](https://reflection.ai/blog/introducing-beam) ⭐️ 8.0/10

Reflection 发布了 Beam，这是一个开源权重的稀疏混合专家（MoE）模型，总参数量 5010 亿，激活参数 230 亿，面向编程、推理和智能体（agentic）任务。该公司表示，Beam 在 23.8 万亿经过筛选的高质量 token 上完成预训练，并在强化学习上投入大量资源以提升其能力。 Beam 为快速发展的开源权重 MoE 领域再添一员，为开发者在编程和智能体场景中提供了闭源前沿模型之外的潜在选择。它的发布也加剧了关于模型来源以及开源权重模型背后的组织能否被信任用于长期产品承诺的争论。 Beam 总参数量为 5010 亿，但每个 token 仅激活 230 亿参数；社区对比指出它没有使用 N-gram 或 PLE 参数，而 DeepSeek V4.1 Flash 总参数量 5520 亿、激活参数 80 亿/160 亿，并带有 1960 亿 N-gram/PLE 参数。Reflection 还引用了一项针对近期热门网格谜题的泛化测试，称 Beam 达到 95.5% 的覆盖率，介于 Opus 5 和另一个模型之间。

hackernews · Philpax · 10月5日 19:16 · [社区讨论](https://news.ycombinator.com/item?id=49969183)

**背景**: 混合专家（MoE）模型将参数拆分为许多专门的子网络（即“专家”），每次输入只激活其中一小部分。这使得稀疏 MoE 模型在推理时比同等总参数量的稠密模型更便宜，但所有参数仍需加载到内存中。开源权重模型会公开训练好的参数，允许他人运行或微调，但训练数据和完整训练配方通常不会公开。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://latenteast.com/insights/moe-total-vs-active-parameters">MoE Total vs Active Parameters , Explained | The Latent East</a></li>
<li><a href="https://localmodel.run/guides/mixture-of-experts">Mixture of experts ( MoE ) explained for local LLMs · localmodel.run</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者欢迎又一个开源权重模型的发布，但对 Reflection 这家组织表示担忧，有人追问模型背后是谁、该公司几个月后是否还会存在。其他人则关注技术对比，指出 Beam 相比 DeepSeek V4.1 Flash 缺少 N-gram/PLE 参数，并讨论了针对近期谜题的泛化测试，该谜题不可能出现在训练数据中。

**标签**: `#open-weight models`, `#mixture-of-experts`, `#large language models`, `#AI research`, `#model release`

---

<a id="item-4"></a>
## [苹果的围墙花园与 AI 智能体和黑客的对决](https://stratechery.com/2026/apple-and-a-hackers-future/) ⭐️ 8.0/10

Ben Thompson 在 Stratechery 的文章中，以一名黑客（据称是 Claude）曝光了他自己暴露在互联网上的 VNC/ARD 设置为例，论证 AI 智能体和黑客正在挑战苹果的围墙花园安全模式。该文章在 Hacker News 上引发了 230 条实质性评论，讨论 AI 智能体的风险容忍度、隐私权衡以及个人安全纪律。 这场辩论凸显了 AI 智能体带来的生产力提升与支撑苹果封闭生态系统的安全假设之间日益紧张的关系，可能影响平台如何设计权限以及用户如何在便利与隐私之间权衡。它也标志着愿意接受更高风险的 AI 原生用户与优先考虑苹果保护模式的用户之间正在出现分化。 案例研究的核心是一个未受保护、对互联网开放的 VNC/ARD 端口，评论者指出这反映出“近乎犯罪的安全意识缺失”；同时，苹果的完全磁盘访问权限以及 Meta 的 Muse AI 智能体发送引用私人消息的未经请求通知，说明 AI 智能体如何使用户同意和数据访问变得复杂。评论者还指出，重度 AI 智能体用户表现出的风险容忍度远超中大型企业所能接受的程度。

hackernews · maguay · 10月5日 10:05 · [社区讨论](https://news.ycombinator.com/item?id=49962857)

**背景**: 苹果的“围墙花园”是一个严格控制的应用生态系统，所有应用都经过严格审查并被沙盒化以保护用户数据，这一模式对普通消费者而言非常成功。VNC（虚拟网络计算）是一种远程桌面协议，如果在没有过滤或加密的情况下暴露在互联网上，攻击者就能完全控制机器。AI 智能体是能够代表用户执行任务的自主软件，通常需要完全磁盘访问等广泛权限，这使传统的安全假设变得复杂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://security.stackexchange.com/questions/193542/remote-access-to-my-home-pc-minimizing-the-risk/193544">vnc - Remote access to my home PC - minimizing the risk ...</a></li>
<li><a href="https://www.datastudios.org/post/apple-macos-full-disk-access-autonomous-ai-agents-security">Apple tightens macOS Full Disk Access as autonomous AI agents ...</a></li>
<li><a href="https://www.technologyreview.com/2021/03/01/1020089/apple-walled-garden-hackers-protected/">How Apple 's locked down security gives... | MIT Technology Review</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者大多认为，将 VNC/ARD 无过滤地暴露在互联网上显示出严重缺乏安全纪律，一些人认为苹果的存在正是为了保护这类用户免于自伤。其他人则争论重度 AI 智能体用户是否对身份盗窃和数据丢失有高得不合理的风险容忍度，以及是否值得为了 AI 驱动的生产力而放弃苹果的保护模式。

**标签**: `#apple`, `#security`, `#ai-agents`, `#privacy`, `#stratechery`

---

<a id="item-5"></a>
## [高通获华为 LogicFolding 芯片专利授权，达成里程碑协议](https://www.bloomberg.com/news/articles/2026-10-05/qualcomm-licenses-patents-on-huawei-s-logicfolding-chip-tech) ⭐️ 8.0/10

2026 年 10 月，高通与华为宣布达成一项为期多年、范围广泛的专利许可协议，涵盖 5G、计算、人工智能和网络等领域；高通还将购买华为部分美国专利，并获得华为 LogicFolding 芯片制造技术相关专利的许可。华为表示，其专利许可协议的累计预期合同价值预计超过 69 亿美元，自 2021 年起其知识产权授权业务已实现正向收入。 这是两家公司首次就 5G 技术达成的专利许可协议，也是华为与高通签署的首个收入为正的协议，标志着半导体知识产权格局的转变——华为从西方技术的主要被许可方转变为先进芯片 IP 的净提供方。这可能增强华为在海外人工智能市场的地位，并重塑美中科技紧张局势在专利许可领域的走向。 LogicFolding 是华为实现其 Tau Scaling 方法的物理架构，通过三维堆叠完整逻辑电路而非将所有逻辑放在单一平面硅层上，目标是在 2031 年前无需 EUV 光刻即可达到 1.4 纳米级芯片密度。不过，高通已否认 LogicFolding 技术包含在协议中的报道，称协议涵盖人工智能、5G 和网络，但不包括 LogicFolding 芯片技术。

hackernews · 0xedb · 10月5日 07:46 · [社区讨论](https://news.ycombinator.com/item?id=49961861)

**背景**: LogicFolding 是一项芯片封装突破，通过垂直堆叠逻辑电路来缩短信号传输距离、降低热量并提高密度，是华为 Tau Scaling 定律在后摩尔定律时代的物理实现。三维芯片堆叠本身并不新鲜——台积电、英特尔和三星都在小芯片和混合键合方面投入巨资——但华为的方法旨在无需 EUV 光刻的情况下实现先进密度，而由于美国出口管制，华为无法获得 EUV 设备。此类专利许可协议使企业能够在地缘政治紧张局势下仍将知识产权变现并进行专利组合交叉许可。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.huawei.com/en/news/2026/10/qualcomm-broad-patent-agreement">Huawei and Qualcomm Announce Broad Patent License Agreement</a></li>
<li><a href="https://www.chinadaily.com.cn/a/202610/05/WS6ac387bae4b06d4aa056167c.html">Huawei and Qualcomm sign landmark patent license agreement ...</a></li>
<li><a href="https://insightsintegration.com/logic-folding-explained-huaweis-chip-packaging-breakthrough-that-could-redefine-the-ai-race/">Logic Folding Explained: Huawei's Chip Packaging Breakthrough...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，关于 LogicFolding 是否真的包含在协议中存在相互矛盾的报道，高通否认了这一说法；其他人则强调 LogicFolding 通过缩短信号路径来降低热量的技术优雅性。一些人提出担忧，华为在美国实体清单上，高通如何能达成此类协议；还有一位评论者引用中国宣传人士的说法，称华为现在从高通获得净收入，标志着技术依赖关系的逆转。

**标签**: `#semiconductors`, `#patent-licensing`, `#Huawei`, `#Qualcomm`, `#US-China-tech`

---

<a id="item-6"></a>
## [3 亿参数字节级 Transformer 仅凭合成非语言先验即可在上下文中学习真实语言](https://www.reddit.com/r/MachineLearning/comments/1wyzhdw/learning_to_learn_a_language_incontext_learning/) ⭐️ 8.0/10

一个 3 亿参数的字节级 Transformer 仅使用由随机采样的循环因果模型生成的合成序列进行训练，却能在权重冻结的情况下完全通过上下文学习预测真实自然语言。在阅读维基百科文本时，其下一字节预测在读完一百万字节后从 8 比特每字节降至 0.9–2.4，覆盖英语、中文、印地语、阿拉伯语、日语和韩语六种语言；同一模型还能在上下文中学会计数、比较数字、近似加法，以及预测素数序列和 Kolakoski 序列等确定性序列。 这项工作将先验拟合网络范式（TabPFN 背后的思想）从表格数据扩展到结构化序列，表明在上下文中学习语言的能力可以源自合成的、非语言的先验，而非语言训练数据。如果这一结论能够推广，可能为数据高效的自适应学习以及理解 Transformer 中上下文学习能力的来源开辟新方向。 该模型在文本上的表现仍远逊于用数万亿 token 训练的经典语言模型，因为它在测试时每种语言最多只看到一百万字节，而且它是字节级模型而非 token 级模型。论文、代码和权重已公开，分别见 arXiv:2610.05879、github.com/cbl/prior-fitted-language-model 和 huggingface.co/lennartcb/pflm1。

reddit · r/MachineLearning · /u/cbl007 · 10月6日 10:50

**背景**: 先验拟合网络（PFN）是一种机器学习范式：模型先在与先验分布对应的合成数据上训练，然后在真实数据上完全通过上下文进行贝叶斯推断，无需更新任何参数；TabPFN 是最著名的例子，将这一思想应用于小型表格数据集。上下文学习指模型在推理时仅凭提示中的示例就能适应新任务，而不进行梯度更新。本文通过定义一种语言先验——每条训练序列都来自随机采样的循环因果模型，使每条序列都成为一种新的合成“语言”——来探究同样的技巧能否用于自然语言。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TabPFN">TabPFN</a></li>
<li><a href="https://chrhenning.com/blog/2026/the-bayesian-story-of-pfns/">The Bayesian Story Behind Prior - Fitted Networks | Christian Henning</a></li>
<li><a href="https://en.wikipedia.org/wiki/In-context_learning">In-context learning</a></li>

</ul>
</details>

**标签**: `#in-context learning`, `#prior-fitted networks`, `#natural language processing`, `#synthetic data`, `#transformers`

---

<a id="item-7"></a>
## [用 39 亿局面数据集将 Stockfish 蒸馏进 ResNet/ViT 模型](https://www.reddit.com/r/MachineLearning/comments/1wxz5qq/distilling_stockfish_on_a_billion_positions_full/) ⭐️ 8.0/10

一位开发者利用 Gigafish 数据集中的 10 亿个局面，将 Stockfish 的价值函数蒸馏进了一个 ResNet/ViT 模型，并在 Hugging Face 上发布了完整的 39 亿局面数据集。该数据集由 37 个月的 Lichess 对局局面构建而成，搜索深度固定为 10。 这项工作表明，学习到的神经网络可以逼近 Stockfish 在限定深度搜索下的价值函数，有望成为 NNUE 式评估的更快替代方案。公开的 39 亿局面数据集也为机器学习和国际象棋社区提供了大规模资源，用于训练和评测新的评估模型。 作者发现，视觉 Transformer 在训练初期理解棋盘的速度较慢，而 CNN 凭借固有的几何归纳偏置在早期学习更快；将两者结合取得了最佳结果。保持搜索深度恒定很重要，因为目标是在固定深度下比 Stockfish 更快地逼近其下方的完整搜索树。

reddit · r/MachineLearning · /u/microscope1024 · 10月5日 04:11

**背景**: Stockfish 是一款免费开源的国际象棋引擎，多年来一直是世界上最强的引擎之一，自 2020 年起它使用可高效更新的神经网络（NNUE）进行评估。知识蒸馏是一种机器学习技术，可将大型模型的知识迁移到较小的模型中，通常是为了降低评估成本或使其能部署在较弱的硬件上。Gigafish 数据集提供了数百万个带有 Stockfish 评估标签的棋局局面，适合用于训练此类蒸馏模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stockfish_NNUE">Stockfish NNUE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation</a></li>
<li><a href="https://huggingface.co/datasets/lukesalamone/gigafish-3.8b-d10">lukesalamone/ gigafish -3.8b-d10 · Datasets at Hugging Face</a></li>

</ul>
</details>

**标签**: `#chess`, `#knowledge-distillation`, `#deep-learning`, `#dataset`, `#stockfish`

---

<a id="item-8"></a>
## [Sona：单个 Transformer 取代 Yandex Music 的 15+组件推荐系统](https://www.reddit.com/r/MachineLearning/comments/1wy4qxm/sona_one_transformer_replaced_our_15_candidate/) ⭐️ 8.0/10

Yandex Music 推出了 Sona，这是一个单一的生成式 Transformer 推荐模型，在生产环境的 A/B 测试中取代了 15+个候选生成器、预排序器和排序器。在智能音箱上进行的为期 7 天、每组 15%用户的测试中，Sona 相比生产对照组实现了+4.53%的活跃用户和+6.30%的总收听时长，两者均在 p < 0.01 水平上显著。 这表明单个端到端生成模型可以在真实生产系统中取代复杂的多阶段推荐级联，有望简化架构并降低工程开销。它为越来越多的证据增添了新内容，证明 LLM 风格的端到端方法可以超越传统的模块化推荐流水线。 Sona 使用历史压缩（History Compression）读取最多 8,192 个事件，将历史分为较早的 6,144 个事件和最近的 2,048 个事件，通过交叉注意力和一个全历史自注意力层交换信息，大致将推理成本减半。一个 7 层堆栈仅对最近的 2,048 个事件运行，解码器和排序模块共享相同的编码器输出，因此编码器每个请求只运行一次；目录覆盖率低于生产堆栈，正在调查中。

reddit · r/MachineLearning · /u/SettingAccording8986 · 10月5日 10:07

**背景**: 传统的生产推荐系统是级联结构：多个候选生成器产生物品，预排序器进行过滤，重型排序器使用数百个工程特征进行打分。Transformer 最初为自然语言处理开发，使用自注意力来建模序列中的关系，近期研究探索使用单个生成式 Transformer 取代这种多阶段流水线。历史压缩是一种技术，通过将更多计算分配给最近事件，来降低对长用户历史进行全注意力计算的二次成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/10/05/yandex-introduces-sona-a-single-generative-recommender-that-replaces-entire-recommendation-cascade/">Yandex Introduces Sona: A Single Generative Recommender That...</a></li>

</ul>
</details>

**标签**: `#recommender-systems`, `#transformers`, `#machine-learning`, `#production-ml`, `#attention-mechanisms`

---

<a id="item-9"></a>
## [OpenAI 将在欧盟为部分 AI 生成文本添加隐形水印](https://openai.com/index/eu-text-provenance/) ⭐️ 8.0/10

OpenAI 宣布，为配合《欧盟人工智能法案》的内容透明要求，未来几周将在欧盟地区符合条件的 ChatGPT 和 Codex 文本输出中加入机器可识别的隐形水印。API 用户也可为部分模型选择开启水印（默认关闭），OpenAI 同时向研究人员和专业机构开放文本水印检测器的申请使用。 这是主要 AI 厂商首次因监管要求而大规模部署文本水印，可能为整个行业如何标注和追溯 AI 生成内容树立先例。它影响欧盟数百万 ChatGPT 用户，也表明内容溯源与透明度正从可选功能变为合规底线。 OpenAI 的水印技术名为 textGrain，它会在模型的用词选择中加入一种不可见的统计信号，检测器则通过寻找该信号来判断一段文本是否带有 OpenAI 水印。检测器目前仅限经批准的研究人员和专业机构使用，API 水印为可选开启而非默认启用。

telegram · zaihuapd · 10月5日 15:25

**背景**: 文本水印的原理是微妙地影响模型对词元（单词或词片）的偏好，嵌入一种读者无法察觉、但匹配工具可以检测到的统计模式。《欧盟人工智能法案》是欧盟全面的 AI 监管法规，要求提供方对 AI 生成或实质性修改的内容进行标注以便识别，其中关键的透明度义务自 2026 年 8 月 2 日起适用。OpenAI 此举是其在文本领域履行这些义务的早期步骤，此前它已在图像和音频方面开展类似的溯源工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/eu-text-provenance/">Our approach to EU text provenance rules | OpenAI</a></li>
<li><a href="https://9to5mac.com/2026/10/05/openai-details-new-text-watermarking-system-for-chatgpt-codex-and-the-api/">OpenAI details new text watermarking system for... - 9to5Mac</a></li>
<li><a href="https://ai-ei.org/ai-transparency/">What does AI transparency require ? - AIEI</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#watermarking`, `#OpenAI`, `#EU AI Act`, `#content provenance`

---