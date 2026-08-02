---
layout: default
title: "Horizon Summary: 2026-08-02 (ZH)"
date: 2026-08-02
lang: zh
---

> 从 74 条内容中筛选出 12 条重要资讯。

---

1. [OpenAI 的 Astra 模型在十项长期数学难题上取得突破](#item-1) ⭐️ 9.0/10
2. [Go 1.27 引入泛型类型别名与自动 HTTP 响应体排空](#item-2) ⭐️ 8.0/10
3. [字节跳动发布 Seedance 2.5 视频生成模型](#item-3) ⭐️ 8.0/10
4. [欧盟责令谷歌向竞争对手开放安卓功能](#item-4) ⭐️ 8.0/10
5. [Lean 内核健全性漏洞 #14576 的事后分析](#item-5) ⭐️ 8.0/10
6. [DeepSeek V4 Flash 0731：性价比最高的智能模型](#item-6) ⭐️ 8.0/10
7. [无状态 MCP 2.0 重燃兴趣，催生新工具](#item-7) ⭐️ 8.0/10
8. [KataGo 研究揭示围棋神经网络如何处理棋盘对称性](#item-8) ⭐️ 8.0/10
9. [用户训练仅编码器 Transformer 预测血糖](#item-9) ⭐️ 8.0/10
10. [VLM 在基准测试中得分高，却抹除临床术语并引入偏见](#item-10) ⭐️ 8.0/10
11. [中国在联合国峰会上向全球南方推广开放权重 AI 模型](#item-11) ⭐️ 8.0/10
12. [微软确认今年推出 Copilot“超级应用”](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 的 Astra 模型在十项长期数学难题上取得突破](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 9.0/10

OpenAI 宣布其下一代模型 Astra 的内部版本在数学和理论计算机科学的十项长期未解决问题上取得了新成果，包括高维球体堆积、非索菲克群的存在性、Connes 刚性猜想的一个反例、算术电路下界、量子并行重复、最近向量问题的难度以及多色 Ramsey 数。模型生成论证的 token 成本约为每个问题 2000 美元，结果已在 Lean 中形式化。 这一里程碑表明 AI 能够为前沿数学研究做出贡献，可能加速发现并改变数学家的研究方式。同时，它也引发了关于作者归属、验证以及 AI 在学术界角色的重要问题，因为这些证明由 AI 生成并由人类形式化。 结果在一篇论文中详细描述，并在 Lean 4 中形式化，仓库（openai/ten-proofs）包含形式化内容。OpenAI 还发布了一份由 LLM 生成的 PDF，重建了推理过程。值得注意的是，每个问题的 token 成本低于 2000 美元，但未披露尝试未成功的问题数量。

telegram · zaihuapd · 8月1日 07:59

**背景**: Lean 是一个开源证明助手，允许对数学证明进行形式化验证，确保正确性。Connes 刚性猜想于 1980 年提出，预测某些 von Neumann 代数完全决定底层群；反例将是一个重大结果。AI 模型 Astra 是 OpenAI 下一代主要模型的内部版本，其在数学中的使用反映了向“大数学”发展的趋势，即人类与 AI 在复杂问题上协作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lean-lang.org/">Lean Programming Language</a></li>
<li><a href="https://www.implicator.ai/openai-astra-10-math-problems-lean-proofs/">OpenAI Says Astra Solved 10 Math Problems With Lean Proofs</a></li>
<li><a href="https://math.ucsd.edu/seminar/connes-rigidity-conjecture">On Connes' rigidity conjecture | Department of Mathematics</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论既有敬畏也有担忧，一些数学家经历了“深蓝”时刻，而另一些人则呼吁对提示词和失败尝试保持透明。总体情绪积极但谨慎，强调需要严格审查。

**标签**: `#AI research`, `#mathematics`, `#OpenAI`, `#formal verification`, `#breakthrough`

---

<a id="item-2"></a>
## [Go 1.27 引入泛型类型别名与自动 HTTP 响应体排空](https://victoriametrics.com/blog/go-1-27/index.html) ⭐️ 8.0/10

Go 1.27 在 VictoriaMetrics 的交互式导览中重点介绍了泛型类型别名和自动 HTTP 响应体排空等主要特性。该版本还修复了 runtime.findnull() 以兼容 Android 上的内存标记扩展（MTE）。 这些变更对 Go 生态系统意义重大，因为它们简化了代码并提升了性能，但自动排空行为可能会微妙地影响依赖旧行为的应用程序。社区的混合反应凸显了在广泛使用的语言中创新与稳定性之间的平衡。 泛型类型别名此前为实验特性，现默认启用，允许别名具有类型参数。自动 HTTP 响应体排空在关闭后最多读取 256KB 或等待 50 毫秒，这可能会在某些情况下导致意外延迟或资源占用。

hackernews · Hixon10 · 8月2日 01:35 · [社区讨论](https://news.ycombinator.com/item?id=49140218)

**背景**: Go 是一种静态类型、编译型编程语言，以其简洁性和强大的标准库而闻名。泛型类型别名允许开发者为泛型类型创建别名，提高代码复用性和可读性。自动 HTTP 响应体排空旨在通过确保响应体被完全读取或关闭来防止连接泄漏，这是 Go 应用程序中 goroutine 泄漏的常见来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://go.dev/blog/alias-names">A description of generic alias types , a planned feature for Go 1 .24</a></li>
<li><a href="https://github.com/golang/go/issues/77370">net/http: drain response body after close #77370 - GitHub</a></li>
<li><a href="https://dev.to/snhacker9/debugging-a-goroutine-leak-caused-by-missing-respbodyclose-in-go-4n6g">Debugging a Goroutine Leak Caused by Missing resp.Body.Close ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论表现出热情与谨慎并存。一些人称赞标准库的改进，而另一些人则对 HTTP 响应排空的静默行为变更表示担忧。一位评论者批评发布说明中使用了“LLM 式用语”，另一位则强调 MTE 修复对 Android 安全性的积极意义。

**标签**: `#Go`, `#programming languages`, `#release`, `#standard library`, `#generics`

---

<a id="item-3"></a>
## [字节跳动发布 Seedance 2.5 视频生成模型](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) ⭐️ 8.0/10

字节跳动正式发布 Seedance 2.5，这是一款新一代视频生成模型，单次可生成最长 30 秒的音视频片段，并支持多轮扩展。该模型引入了 50 个多模态参考、时间戳级编辑控制，以及绿幕、镜头视角控制等增强功能。 此次发布标志着 AI 视频生成领域的重大进步，提供更长、更高质量的输出和更精确的控制，可能对电影制作人和内容创作者产生影响。社区讨论凸显了中国与西方市场需求差异，以及与 MiniMax H3 等开源权重模型的竞争格局。 Seedance 2.5 支持单次生成最长 30 秒，并支持多轮扩展，输入可包含 50 个多模态参考。它还提供时间戳级控制，用于对音频和视频进行精准编辑，并具备绿幕、镜头视角控制等高级功能。

hackernews · njaremko · 8月1日 20:45 · [社区讨论](https://news.ycombinator.com/item?id=49138302)

**背景**: Seedance 是字节跳动的 AI 视频生成模型系列。2.5 版本在之前迭代的基础上，专注于更长、更可控的视频创作。视频生成模型利用深度学习从文本、图像或其他视频创建视频，越来越多地用于创意行业的脚本可视化、原型制作和内容生产。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5">Seedance 2.5 — One-take Creation, Flexible Referencing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Seedance_2.0">Seedance 2.0 - Wikipedia</a></li>
<li><a href="https://www.seeddance.io/models/seedance-2-5">Seedance 2 . 5 Free: Try ByteDance AI Video , No Queue, Instant Results</a></li>

</ul>
</details>

**社区讨论**: 社区评论情绪复杂：有人称赞模型的质量和使用乐趣，也有人担忧成本和伦理问题。一个值得注意的观点是，该模型侧重于动作/高特效镜头，这可能反映了中国与西方市场需求差异。一些用户更倾向于 MiniMax H3 等开源权重替代方案，以获得更好的控制和更低的成本；还有评论者质疑此类生成工具的存在价值，认为其可能造成危害。

**标签**: `#AI`, `#video generation`, `#ByteDance`, `#machine learning`, `#creative tools`

---

<a id="item-4"></a>
## [欧盟责令谷歌向竞争对手开放安卓功能](https://www.openhomefoundation.org/blog/a-big-win-for-android-interoperability/) ⭐️ 8.0/10

欧盟委员会根据《数字市场法案》责令谷歌向第三方开放 11 项安卓功能，其中大部分须在 2027 年 8 月前完成。这包括允许竞争对手的 AI 助手深度集成操作系统，并共享匿名搜索数据。 这一裁决显著挑战了谷歌对安卓的控制，可能促进 AI 和移动服务领域的竞争与创新。它可能为全球如何监管主导平台树立先例，影响开发者、用户以及 OpenAI 等科技巨头。 这 11 项功能包括面向 AI 服务的结构化设备端集成，使其能够与其他应用交互并代表用户执行任务。到 2028 年 8 月，Android 19 需支持多个助手同时监听唤醒词。

hackernews · soheilpro · 7月31日 15:01 · [社区讨论](https://news.ycombinator.com/item?id=49124051)

**背景**: 《数字市场法案》（DMA）是欧盟旨在遏制谷歌等“守门人”平台权力的法规。欧盟委员会 2026 年 7 月的决定明确了谷歌必须如何遵守，涉及安卓互操作性和搜索数据访问。这是确保数字市场公平竞争的更广泛努力的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.remio.ai/post/google-must-open-android-and-search-to-rivals-putting-gemini-s-platform-advantage-at-risk">Google Must Open Android and Search to Rivals, Putting...</a></li>
<li><a href="https://innopanda.com/eu-forces-google-to-open-android-to-rival-ai-agents/">EU Forces Google to Open Android to Rival AI Agents</a></li>
<li><a href="https://windowsforum.com/windows-news.4/google-android-must-open-ai-assistant-access-in-eu-by-july-2027.439760/">Google Android Must Open AI Assistant Access in EU by July 2027</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，赞扬欧盟在追究企业责任方面的作用。一些评论者强调 AI 集成等具体功能，而另一些人则持怀疑态度，指出允许小企业销售修改版安卓设备的核心问题仍未解决。

**标签**: `#Android`, `#Interoperability`, `#Regulation`, `#EU`, `#Digital Markets Act`

---

<a id="item-5"></a>
## [Lean 内核健全性漏洞 #14576 的事后分析](https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/) ⭐️ 8.0/10

发布了一份关于 Lean 内核健全性漏洞 #14576 的详细事后分析，强调了即使是经过验证的系统也存在脆弱性，以及独立检查的必要性。 该漏洞破坏了广泛使用的证明助手 Lean 的核心保证，影响了形式化验证和编程语言理论。它强调了独立内核检查的重要性，以及仅依赖单一实现的局限性。 该漏洞需要两个实现中的两个不同缺陷才能被利用，这意味着使用当前版本进行独立检查仍然有效。事后分析可能讨论了根本原因、修复方法以及对 Lean 生态系统的影响。

hackernews · juhopitk · 8月1日 18:32 · [社区讨论](https://news.ycombinator.com/item?id=49137060)

**背景**: Lean 是一个定理证明器和编程语言，拥有一个小型、可信的内核来检查证明。内核中的健全性漏洞至关重要，因为它们可能导致不健全的证明被接受。独立的内核检查器，例如 Lean4Lean 项目中开发的检查器，通过提供单独的验证路径来帮助降低此类风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2403.14064">[2403.14064] Lean4Lean: Verifying a Typechecker for Lean, in Lean</a></li>
<li><a href="https://news.ycombinator.com/item?id=49137060">Postmortem for Kernel Soundness Bug #14576 | Hacker News</a></li>
<li><a href="https://ammkrn.github.io/type_checking_in_lean4/whats_a_kernel.html">What's a kernel? - Type Checking in Lean 4 - GitHub Pages</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了多种观点：一些人指出，鉴于 Rust 等其他系统也存在类似问题，健全性漏洞并不令人意外；而另一些人则认为，此类漏洞凸显了证明助手背后意识形态的脆弱性。有人建议像 Metamath 这样的替代系统可能更健壮，并呼吁进一步开展独立检查和内核本身验证的工作。

**标签**: `#Lean`, `#formal verification`, `#soundness bug`, `#theorem prover`, `#kernel`

---

<a id="item-6"></a>
## [DeepSeek V4 Flash 0731：性价比最高的智能模型](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek 发布了 DeepSeek-V4-Flash-0731，这是一个拥有 3040 亿参数的模型，智能体能力大幅增强，在 Terminal Bench 2.1 上得分 82.7，在 DeepSWE 上得分 54.4。其定价为每百万输入 token 0.14 美元，每百万输出 token 0.27 美元，被 Artificial Analysis 评为目前性价比最高的智能模型。 此次发布以远低于竞争对手的成本提供了顶级性能，可能通过使先进的智能体能力更容易获得来颠覆 AI 模型市场。这可能会迫使其他提供商降低价格或提高效率，从而使依赖 LLM 的开发者和企业受益。 该模型拥有 1,048,576 个 token 的上下文窗口，支持最多 384K 个输出 token，并支持推理、工具调用和结构化 JSON 输出。它采用 FP4 和 FP8 混合精度以提高效率，并支持三种推理努力模式；但未包含 Jinja 格式的聊天模板，需要使用自定义编码脚本。

rss · Simon Willison · 7月31日 23:59

**背景**: DeepSeek 是一家中国 AI 研究公司，以发布与领先专有模型竞争的开源权重模型而闻名。V4-Flash-0731 是 V4 系列的一部分，该系列包括 Pro 版本和针对成本效率优化的 Flash 版本。Artificial Analysis Intelligence Index 是一个聚合多项测试来衡量模型智能的基准，该模型相对于其成本的强劲表现使其对预算敏感的用户具有吸引力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash | vLLM Recipes</a></li>
<li><a href="https://www.orcarouter.ai/blog/deepseek-v4-flash-official-release">DeepSeek V4 Flash: Official Release, Explained</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论强调了该模型令人印象深刻的性价比，一些用户指出其性能优于像 MiniMax M3 这样更大的模型。然而，一些用户报告在默认推理设置下图像生成结果参差不齐，这表明复杂任务需要更高的推理努力。

**标签**: `#AI`, `#DeepSeek`, `#LLM`, `#model release`, `#cost efficiency`

---

<a id="item-7"></a>
## [无状态 MCP 2.0 重燃兴趣，催生新工具](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 8.0/10

Simon Willison 表示，MCP 2.0（2026-07-28 版 Model Context Protocol 规范）的发布重新点燃了他对该协议的兴趣，促使他构建了三个新工具，包括 mcp-explorer 和 datasette-mcp。新的无状态设计通过消除会话 ID 和多步初始化的需求，简化了客户端和服务器的实现。 此次更新标志着 AI 工具生态系统的一个重要里程碑，使 MCP 对 Web 应用更加易用和可扩展。它可能使开发者从基于终端的代理框架重新转向更易审计和可控的 MCP 工具，尤其是对于较小的模型。 无状态 MCP 使用单个 HTTP 请求，带有 MCP-Protocol-Version 和 Mcp-Method 等头部，取代了之前的两步初始化和调用过程。这减少了服务器端状态管理并提高了可扩展性，但可能会增加请求中的重复数据。

rss · Simon Willison · 7月31日 23:13

**背景**: MCP（Model Context Protocol）是 Anthropic 于 2024 年 11 月推出的开放协议，旨在标准化 LLM 代理访问外部工具和数据的方式。它在 2025 年广受欢迎，但后来被“Skills”和基于终端的方法所掩盖。无状态协议（如 HTTP）不在请求之间保留会话状态，从而提供更好的可见性、可靠性和可扩展性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stateless_protocol">Stateless protocol</a></li>
<li><a href="https://www.linkedin.com/pulse/new-mcp-stateless-here-what-actually-changes-arnold-cartagena-dpcte">The new MCP is stateless . Here is what actually changes.</a></li>

</ul>
</details>

**标签**: `#MCP`, `#AI`, `#LLM`, `#tools`, `#specification`

---

<a id="item-8"></a>
## [KataGo 研究揭示围棋神经网络如何处理棋盘对称性](https://www.reddit.com/r/MachineLearning/comments/1vcrki2/how_symmetric_are_the_insides_of_a_go_network_r/) ⭐️ 8.0/10

KataGo 的维护者发布了一项研究，分析超人级围棋神经网络如何在内部表示棋盘对称性，发现尽管训练时仅使用随机 8 倍数据增强，网络仍能在很大程度上学习与方向无关的概念。该研究包含一个意外发现，并附有代码和教学性文章。 这项研究有助于神经网络的可解释性，特别是对于围棋等棋盘游戏，并可能通过展示对称性如何被隐式学习来影响模型设计。它还提供了对强 AI 系统内部表示的见解，对更广泛的机器学习社区具有价值。 该研究使用开源围棋 AI KataGo，考察其神经网络学习方向不变概念的程度。文章大部分由 AI 生成，但经过了详细的人类指导和反馈，代码链接已附在帖子中。

reddit · r/MachineLearning · /u/icosaplex · 8月1日 16:18

**背景**: 围棋是一种在旋转和反射下完全对称的棋盘游戏，但 KataGo 的神经网络并未强制这种对称性，而是依赖训练期间的随机 8 倍数据增强。本研究探讨网络是否自动学习独立于方向的棋盘表示，这与理解神经网络如何处理对称性普遍相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/lightvector/KataGo/7.2-model-architecture">Model Architecture | lightvector/KataGo | DeepWiki</a></li>
<li><a href="https://github.com/lightvector/KataGo">GitHub - lightvector/KataGo: GTP engine and self-play ... KataGo Distributed Training KataGo - Networks for kata1 KataGo — Grokipedia KataGo/docs/KataGoMethods.md at master · lightvector/KataGo</a></li>
<li><a href="https://medium.com/@youpiter.dr/symmetry-for-data-scientists-how-go-engines-turn-one-position-into-eight-and-you-can-too-30312158da87">Symmetry for Data Scientists: How Go Engines Turn One ...</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#interpretability`, `#Go`, `#neural networks`, `#symmetry`

---

<a id="item-9"></a>
## [用户训练仅编码器 Transformer 预测血糖](https://www.reddit.com/r/MachineLearning/comments/1vc1txc/i_have_trained_a_model_to_predict_my_blood_sugar_p/) ⭐️ 8.0/10

一位 Reddit 用户训练了一个仅编码器的 Transformer，利用过去和未来的餐食/胰岛素数据预测未来 2 小时的血糖水平，并提供了多种模型规模和训练策略。最大的模型约有 1700 万参数，先在模拟器上预训练，再在真实糖尿病数据集上微调。 这展示了 Transformer 模型在个性化健康监测中的实际应用，可能为糖尿病管理提供更准确的血糖预测。它强调了在移动设备上运行此类模型的可行性，有望改善患者的生活质量。 该模型采用 BERT 风格的双向注意力机制，并掩蔽未来的血糖值，结合 DILATE 损失用于中位数预测和分位数损失用于不确定性区间。它在重新参数化到[40, 400] mg/dL 的 Kovatchev 风险空间中运行，并可以自回归方式预测超过 2 小时。

reddit · r/MachineLearning · /u/0xdeadf1sh · 7月31日 20:09

**背景**: 仅编码器的 Transformer，如 BERT，专为表示学习设计，通常用于情感分析等任务。DILATE 损失是一种用于时间序列预测的损失函数，同时优化形状和时间对齐，而分位数损失用于分位数回归以估计不确定性。该模型需要用户输入餐食和胰岛素剂量，这限制了其在未声明场景下的使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/BERT_(language_model)">BERT (language model) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Transformer_(deep_learning)">Transformer (deep learning) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quantile_regression">Quantile regression - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区讨论可能包括关于模型架构、训练数据和实际部署的问题，以及对其局限性的反馈。一些人可能对开源发布和潜在改进感兴趣，而另一些人可能担心数据隐私和泛化能力。

**标签**: `#transformer`, `#health`, `#blood glucose prediction`, `#time series`, `#deep learning`

---

<a id="item-10"></a>
## [VLM 在基准测试中得分高，却抹除临床术语并引入偏见](https://www.reddit.com/r/MachineLearning/comments/1vcipzz/vlms_can_score_well_on_benchmarks_while_silently/) ⭐️ 8.0/10

一篇新论文提出了一个框架，用于衡量视觉语言模型（VLM）在放射学报告生成（RRG）中抹除临床术语和引入偏见术语的问题，揭示当前基准指标会奖励重复、缺乏临床意义的报告。 这很重要，因为高基准分数可能掩盖 AI 生成的医疗报告中的临床重大缺陷，可能导致误诊或漏诊。该框架为医疗应用提供了更准确评估 VLM 的方法，在医疗应用中，精确性和临床相关性至关重要。 论文题为《衡量 VLM 未说出的内容：验证指标掩盖放射学报告生成中的临床术语抹除》，可在 arXiv（2603.01625）上获取。作者观察到 VLM 经常抹除罕见但有临床意义的术语，使报告变得重复且缺乏临床实用性。

reddit · r/MachineLearning · /u/ade17_in · 8月1日 09:27

**背景**: 视觉语言模型（VLM）越来越多地用于自动生成放射学报告，但它们的评估通常依赖于基于参考的指标，如 BLEU 或 ROUGE，这些指标将生成的文本与真实文本进行比较。这些指标可能通过生成重复或通用的模板而被利用，并且它们不会惩罚遗漏临床重要术语的行为。新框架旨在通过直接衡量术语抹除和偏见引入来解决这一差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learnopencv.com/vlm-evaluation-metrics/">The Ultimate Guide To VLM Evaluation Metrics ... | LearnOpenCV</a></li>
<li><a href="https://github.com/mk-runner/Awesome-Radiology-Report-Generation">GitHub - mk-runner/Awesome-Radiology-Report-Generation: paper list, dataset, and tools for radiology report generation · GitHub</a></li>
<li><a href="https://arxiv.org/html/2309.14381">Survey of Social Bias in Vision - Language Models</a></li>

</ul>
</details>

**标签**: `#VLM`, `#evaluation metrics`, `#radiology report generation`, `#bias`, `#clinical AI`

---

<a id="item-11"></a>
## [中国在联合国峰会上向全球南方推广开放权重 AI 模型](https://www.semafor.com/article/07/28/2026/token-diplomacy-how-china-is-shaping-the-worlds-ai-future) ⭐️ 8.0/10

7 月底在日内瓦联合国“智能向善”峰会上，中国派出代表团向巴基斯坦、俄罗斯、赞比亚等国推介其开放权重 AI 模型。阿里云架构师王坚表示，中国 AI 可以像能源一样成为其他国家发展的“基石”。 此举凸显了中国向发展中国家输出 AI 基础设施的战略，与美国闭源模型形成对比。这可能重塑全球 AI 采用和影响力格局，美国对此表示担忧，认为会导致对中国标准和基础设施的依赖。 美国国务院发言人警告称，此举可能导致对中国基础设施和标准的依赖。此次峰会还标志着联合国 AI 治理全球对话首次会议召开，中国支持了首个全球 AI 标准化决议。

telegram · zaihuapd · 8月1日 10:06

**背景**: 开放权重模型是指公开训练参数的 AI 模型，开发者可以微调和部署，而闭源模型仅提供 API 访问。中国一直积极推广其开放权重模型，如阿里的 Qwen 和 DeepSeek，作为美国产品的经济替代品，尤其面向发展中国家。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.zhiding.cn/2025/0401/3164906.shtml">OpenAI 将发布自 2019 年以来首个" 开 放 权 重 " 模 型 --人工智能-至顶网</a></li>
<li><a href="https://wap.miit.gov.cn/xwfb/bldhd/art/2026/art_7b206a82ae3844fd981ff3e42daf0267.html">李乐成率团出席联合国人工智能治理全球对话首次会议等系列活动</a></li>
<li><a href="https://www.neican.ai/insights/aws-bedrock-ai-20250919121005080-1/">开 放 权 重 的云端跃迁：AWS Bedrock 如何 重 塑企业AI的未来格局 | AI内参</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#geopolitics`, `#open-source AI`, `#China`, `#global south`

---

<a id="item-12"></a>
## [微软确认今年推出 Copilot“超级应用”](https://www.theverge.com/tech/972927/microsoft-copilot-super-app-confirmed) ⭐️ 8.0/10

微软 CEO 萨蒂亚·纳德拉在财报电话会议上确认，公司将于今年推出一款 AI“超级应用”，将 Copilot 的聊天、编程和智能体能力整合在一起，同时面向消费者和企业。该应用将整合 Copilot、GitHub Copilot、Copilot Cowork 和 Autopilot 系统等体验。 此举标志着微软的重大战略方向，将其 AI 产品整合到一个平台中，可能重塑用户在工作和个人场景中与 AI 的交互方式。这也加剧了与 OpenAI 的 ChatGPT Work 等其他 AI 超级应用的竞争，可能加速智能体 AI 在日常工作流程中的采用。 纳德拉将 Copilot 描述为从聊天工具演进到“Cowork”再到“Autopilots”，超级应用将在本季度整合这些体验，包括代码功能。微软上季度营收增至 900 亿美元，主要由 AI 和云业务推动，为这一计划提供了财务支持。

telegram · zaihuapd · 8月1日 13:18

**背景**: Copilot 是微软集成在其产品中的 AI 助手，而“Cowork”是 Microsoft 365 中自动化任务和工作流程的功能，“Autopilot”则指自主执行端到端流程的 AI 系统。“超级应用”的概念是指将多种服务整合到一个应用程序中，由微信等应用普及，微软旨在打造类似的 AI 能力中心。这一公告紧随 OpenAI 推出整合 ChatGPT 和 Codex 的 ChatGPT Work 之后，表明 AI 工具整合的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/microsoft-365-copilot/cowork">Copilot Cowork: Automate Tasks and Workflows | Microsoft</a></li>
<li><a href="https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/">Copilot Cowork: A new way of getting work done | Microsoft 365 Blog</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Copilot`, `#AI`, `#Super App`, `#Product News`

---