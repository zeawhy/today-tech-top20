---
layout: default
title: "Horizon Summary: 2026-08-12 (ZH)"
date: 2026-08-12
lang: zh
---

> 从 85 条内容中筛选出 17 条重要资讯。

---

1. [Qwen 发布 Qwen3.8-2.4T-A95B，一个巨大的 MoE 模型](#item-1) ⭐️ 9.0/10
2. [主要 LLM API 的加密思维链痕迹被窃取](#item-2) ⭐️ 9.0/10
3. [vLLM v0.27.0 新增 Kimi K3、PyTorch 2.13 和深度 FlashAttention 4 支持](#item-3) ⭐️ 8.0/10
4. [DeepSeek V4 Pro 0813：以更低成本实现竞争性能](#item-4) ⭐️ 8.0/10
5. [Tailscale 将数据库损坏追溯到 16 年前的 SQLite WAL 重置错误](#item-5) ⭐️ 8.0/10
6. [AI 正在移除软件工程的中产阶级](#item-6) ⭐️ 8.0/10
7. [数学家分析 LLM 在寻找反例方面的优势](#item-7) ⭐️ 8.0/10
8. [Woxi：用 Rust 重写的开源 Wolfram 语言实现](#item-8) ⭐️ 8.0/10
9. [Meta 发布 Muse Glimmer，一款 30B 开源权重智能体模型](#item-9) ⭐️ 8.0/10
10. [AI 先驱在 Ai4 上就开放与安全展开辩论](#item-10) ⭐️ 8.0/10
11. [General Catalyst 领投成立仅两个月的 River AI 11 亿美元融资](#item-11) ⭐️ 8.0/10
12. [Anthropic 未发布模型在黎曼猜想上取得进展](#item-12) ⭐️ 8.0/10
13. [Adam 的逐坐标缩放破坏旋转不变性与低秩偏置](#item-13) ⭐️ 8.0/10
14. [解耦下降：通过 AMP 校正实现精确的训练-测试误差跟踪](#item-14) ⭐️ 8.0/10
15. [LTX 发布开源视频模型 LTX-2.5，单张 RTX 5090 即可运行](#item-15) ⭐️ 8.0/10
16. [中国前总理朱镕基逝世，享年 98 岁](#item-16) ⭐️ 8.0/10
17. [DeepSeek 发布 V4-Flash API 公测版，Agent 基准测试表现强劲](#item-17) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwen 发布 Qwen3.8-2.4T-A95B，一个巨大的 MoE 模型](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen 发布了 Qwen3.8-2.4T-A95B，这是一个稀疏混合专家模型，总参数达 2.4 万亿，每个 token 激活 950 亿参数。它是 Qwen3.8-Max 的开源权重版本，声称性能介于 Opus 4.8 和 Fable 5 之间。 此次发布将接近前沿的能力带入开源生态系统，可能使顶级 AI 性能更加普及。社区强调，量化版本（例如 1 比特 397GB）可以在消费级硬件上本地部署，这对个人用户来说是一个重要进步。 该模型的词汇量约为 24.8 万，大于其他近期中国模型，如 Kimi K3（约 16.4 万）和 DeepSeek-V4（约 12.9 万）。最初发布 BF16 和 FP8 格式，没有针对 4 比特量化的 QAT，因此可能需要社区量化来减小体积。完整 BF16 模型约 4.9TB，而 1 比特量化版本约 397GB。

hackernews · Philpax · 8月12日 15:01 · [社区讨论](https://news.ycombinator.com/item?id=49273478)

**背景**: 混合专家（MoE）模型每个 token 只激活一部分参数，从而可以在保持推理成本可控的同时拥有巨大的总参数量。量化通过降低权重精度来减小模型大小和内存需求，这对于在有限硬件上部署大型模型至关重要。Qwen 是阿里巴巴开发的一系列大型语言模型，Qwen3.8-Max 是其旗舰模型，具有视觉输入和 1M 上下文长度等额外功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/">Serve Qwen3.8-2.4T-A95B, a 2.4T-Parameter Model, with ...</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.8-2.4t-a95b">Qwen3.8 2.4T A95B - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://forums.developer.nvidia.com/t/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/379956">Serve Qwen3.8-2.4T-A95B, a 2.4T-Parameter Model, with ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论对模型的性能以及通过量化实现本地部署的潜力表示兴奋，一位用户指出 1 比特量化 397GB 使得 Opus 4.5 级别的性能在普通人机器上触手可及。也有人对开源权重版本缺乏视觉支持和 1M 上下文长度表示担忧，并提到由于模型体积大和许可限制带来的服务挑战。

**标签**: `#AI/ML`, `#Large Language Models`, `#Open Source`, `#Model Release`, `#MoE`

---

<a id="item-2"></a>
## [主要 LLM API 的加密思维链痕迹被窃取](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/#atom-everything) ⭐️ 9.0/10

一篇研究论文表明，Anthropic、OpenAI 和 Google 的加密思维链块可以被重放和越狱，以明文形式恢复隐藏的推理痕迹。该攻击利用了同一系列模型共享加密密钥的事实，使得较弱的模型能够解码较强模型的推理。 这一漏洞暴露了主要专有 LLM API 中隐藏的思维链推理，破坏了旨在保护知识产权和防止信息泄露的安全措施。它突显了 API 设计中的关键缺陷，可能对 AI 安全和隐私产生重大影响。 该攻击在 Claude Haiku 4.5 等模型上进行了演示，这是最容易攻击的模型，使用简单的提示来转录推理。论文附录中包含了提取的推理痕迹的详细内容，所有提供商都已确认收到报告并修复了该问题。

rss · Simon Willison · 8月11日 22:40

**背景**: 思维链（CoT）推理是一种 LLM 在生成最终答案之前逐步推理的技术。为了保护知识产权并限制信息泄露，Anthropic、OpenAI 和 Google 等提供商现在将这些痕迹加密并以加密块的形式返回给客户端。论文揭示这些加密块并未得到适当隔离，因为它们可以在会话、用户和模型之间重放，并且较弱的模型可以被越狱以解码它们。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://arxiv.org/abs/2608.09867">[2608.09867] Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://www.explainx.ai/blog/stealing-reasoning-traces-encrypted-cot-vulnerability-august-2026">Stealing Reasoning Traces: The Encrypted Chain-of-Thought ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 和其他论坛上的讨论强调了该漏洞的严重性，许多人对其对 AI 安全和专有 API 可信度的影响表示担忧。一些评论者指出修复可能不完整，未来可能出现类似攻击，而其他人则争论提取隐藏推理的伦理问题。

**标签**: `#LLM`, `#security`, `#chain-of-thought`, `#API`, `#privacy`

---

<a id="item-3"></a>
## [vLLM v0.27.0 新增 Kimi K3、PyTorch 2.13 和深度 FlashAttention 4 支持](https://github.com/vllm-project/vllm/releases/tag/v0.27.0) ⭐️ 8.0/10

vLLM v0.27.0 是一个重要版本，包含来自 242 位贡献者的 561 次提交，新增了对 Kimi K3 模型的完整支持，以及 Qwen3.5、K-EXAONE-2.0-750B-A37B 等新模型，并将 PyTorch 升级到 2.13.0，同时加深了在 SM100 上的 FlashAttention 4 集成。 此版本显著扩展了 vLLM 的模型覆盖范围和性能，特别是对 Kimi K3 等前沿架构的支持，使其成为 AI 推理社区的关键更新。PyTorch 2.13 升级和 FlashAttention 4 增强有望提高大规模部署的效率和降低延迟。 值得注意的技术细节包括对 Kimi K3 的全栈支持（包含 AttnRes 内核和 DeepGEMM）、破坏性的 PyTorch 2.13.0 环境变更，以及在 SM100 上 FlashAttention 4 的 FP8 KV 缓存和 headdim-256 支持。该版本还引入了用于大规模服务的简化容错框架，并初步支持 NVIDIA Rubin (sm_107) 和 ROCm gfx1250。

github · khluu · 8月10日 21:18

**背景**: vLLM 是一个高吞吐、内存高效的 LLM 推理和服务引擎，广泛用于生产环境。Kimi K3 是 Moonshot AI 推出的大型语言模型，采用了 Kimi Delta Attention 和 Attention Residuals 等创新，改善了长上下文处理。FlashAttention 是一系列优化的注意力算法，可减少内存并加速训练和推理。PyTorch 是一个流行的深度学习框架，升级到 2.13 带来了性能和兼容性改进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html">Kimi K3 Architecture Notes | Sebastian Raschka, PhD</a></li>
<li><a href="https://huggingface.co/blog/ResterChed/kimi-k3-model-overview-mxfp4-quantization-open-wei">Kimi K3 Model Overview: 2.8T Parameters, MXFP4 Quantization, and What the Open Weights Mean for the Community</a></li>
<li><a href="https://github.com/deepseek-ai/DeepGEMM">GitHub - deepseek-ai/DeepGEMM: DeepGEMM: clean and efficient ...</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#PyTorch`, `#FlashAttention`, `#AI/ML`

---

<a id="item-4"></a>
## [DeepSeek V4 Pro 0813：以更低成本实现竞争性能](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 8.0/10

DeepSeek 发布了 V4 Pro 0813，这是 V4 Pro 模型的新版本，现已在 OpenRouter 上提供。它提供 1,048,576 token 的上下文窗口，定价为每百万输入 token 0.435 美元，每百万输出 token 0.87 美元。 此次发布意义重大，因为它提供了与 Opus 4.8 等顶级模型相媲美的性能，同时价格便宜约 20 倍，使先进 AI 更加普及。它可能影响 LLM 市场的定价和采用趋势，尤其对成本敏感的开发者与企业。 DeepSeek V4 Pro 0813 是一个大规模混合专家模型，总参数 1.6T，激活参数 49B，支持 1M token 上下文窗口和最大 384,000 token 输出。社区基准测试显示其在 HLE 上无工具/有工具得分为 42.7/60.0，定位介于 DeepSeek V4 Flash 和 Sol 或 Fable 等更强模型之间。

hackernews · explosion-s · 8月12日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=49274600)

**背景**: DeepSeek 是一家以发布高性价比大语言模型而闻名的中国 AI 公司。V4 Pro 系列采用混合专家架构，每个 token 只激活部分参数，从而以较低计算成本实现高性能。OpenRouter 是一个提供多种 AI 模型统一 API 访问的平台，方便用户比较和使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V 4 Pro 0813 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://lmmarketcap.com/model/deepseek-v4-pro-0813">DeepSeek V 4 Pro - Pricing & Benchmarks 2026 | LM Market Cap</a></li>
<li><a href="https://aihubmix.com/model/deepseek-v4-pro-0813">deepseek - v 4 - pro - 0813 - API Pricing & Performance | AIHubMix</a></li>

</ul>
</details>

**社区讨论**: 社区反馈褒贬不一：一些用户报告称，与 GPT-5.6-terra-high 或 Grok 4.6 等替代品相比，DeepSeek V4 Pro 0813 在复杂任务上存在问题，而另一些用户则称赞其成本效益和承担繁重开发任务的能力。一位用户指出，它与 Opus 4.8 竞争，但弱于 Sol 或 Fable，且便宜约 20 倍。

**标签**: `#AI`, `#LLM`, `#DeepSeek`, `#benchmarks`, `#cost-efficiency`

---

<a id="item-5"></a>
## [Tailscale 将数据库损坏追溯到 16 年前的 SQLite WAL 重置错误](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

Tailscale 发布了一篇详细的博客文章，说明他们如何将数据库损坏问题追溯到 16 年前的 SQLite WAL 重置错误，并资助了一个开源 VFS 垫片来帮助隔离竞态条件。该错误发生在两个或多个连接到同一 WAL 模式数据库的连接同时尝试写入或运行检查点时，可能导致数据库文件损坏。 这很重要，因为它凸显了支持 SQLite 等开源项目的价值，并展示了公司如何资助特定的调试工具来解决微妙且长期存在的错误。它还提高了人们对使用受支持的 SQLite 版本以及 WAL 模式下并发访问潜在风险的认识。 该错误记录在 SQLite 的“如何损坏 SQLite 数据库文件”页面上，影响特定范围内的 SQLite 版本；例如，SQLite 3.50.4 受影响，而 3.51.3 则无问题。Tailscale 修补了他们的 SQLite 驱动程序，以便在写事务和 WAL 重置操作重叠时记录警告，并资助开发了一个 VFS 垫片来帮助检测此类竞态。

hackernews · ropbear · 8月12日 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49272832)

**背景**: SQLite 是一种广泛使用的嵌入式数据库，支持预写日志（WAL）模式以提高并发性。WAL 重置错误是一种竞态条件，当多个连接到同一数据库的连接同时尝试写入或检查点时可能发生，导致数据库损坏。Tailscale 在其控制平面中使用 SQLite，尽管遵循了推荐的单一写入者设计，仍遇到了这个微妙的错误。SQLite 中的 VFS（虚拟文件系统）层允许自定义实现来拦截文件操作，这就是垫片能够帮助隔离问题的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL-Reset bug</a></li>
<li><a href="https://www.sqlite.org/howtocorrupt.html">How To Corrupt An SQLite Database File</a></li>
<li><a href="https://sqlite.org/cksumvfs.html">The Checksum VFS Shim - SQLite</a></li>

</ul>
</details>

**社区讨论**: 社区对这篇博文以及 Tailscale 资助开源开发的决定表示赞赏，评论强调了支持 SQLite 的价值和有趣的调试过程。一些用户对导致该错误的特定检查点频率表示好奇，而另一些用户则欣赏其技术深度和公司的透明度。

**标签**: `#SQLite`, `#database`, `#bug`, `#Tailscale`, `#open-source`

---

<a id="item-6"></a>
## [AI 正在移除软件工程的中产阶级](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html) ⭐️ 8.0/10

一篇博客文章认为，AI 通过自动化常规编码任务正在消除软件工程师的中产阶级，同时放大高技能和低技能工程师的影响。文章强调工程师需要保持批判性思维和深度学习。 这很重要，因为它突显了软件工程就业市场的重大转变，可能影响职业发展轨迹和招聘实践。它强调了在 AI 增强的行业中批判性思维和适应性的日益重要性。 文章指出，'糟糕'的工程师现在可以通过 AI 将他们的不良实践在组织中放大十倍，并且从高级工程师到初级编码员的传统交接不再必要。它还警告不要将批判性思维外包给 LLM。

hackernews · florianherrengt · 8月12日 13:20 · [社区讨论](https://news.ycombinator.com/item?id=49271994)

**背景**: 软件工程传统上存在一个层级结构，高级工程师设计解决方案，初级工程师实施。随着 GitHub Copilot 和 OpenAI Codex 等 AI 编码助手的兴起，常规编码任务日益自动化，可能压缩该职业的中层。研究表明，虽然 LLM 可以生成代码，但它们尚不能可靠地维护大型软件系统，这表明人工监督仍然至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2502.20429v2">Impact of AI on Software Engineering Jobs</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2772485925000171">LLMs: A game-changer for software engineers? - ScienceDirect</a></li>
<li><a href="https://arxiv.org/html/2511.06428v1">Walking the Tightrope of LLMs for Software Development: A Practitioners’ Perspective</a></li>

</ul>
</details>

**社区讨论**: 评论者大体同意文章观点，指出 AI 放大了好的和坏的工程实践。一些人强调永远不要将批判性思维外包给 LLM，另一些人则将这一变化比作自动化'StackOverflow 工程师'角色，高级工程师不再需要将编码任务交给初级人员。

**标签**: `#AI`, `#software engineering`, `#future of work`, `#LLM`, `#career impact`

---

<a id="item-7"></a>
## [数学家分析 LLM 在寻找反例方面的优势](https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/) ⭐️ 8.0/10

著名数学家蒂莫西·高尔斯发表了一篇博客文章，分析 LLM 擅长的数学类型，认为它们更擅长寻找反例而非创造优雅的证明。该文章引发了高质量的讨论，共 102 条评论。 这一分析为 LLM 在数学领域的当前能力和局限性提供了宝贵见解，对于指导未来 AI 研究和数学发现应用至关重要。它还强调了 AI 在反例搜索中的潜力，这一任务可能极大地辅助数学研究。 高尔斯指出，LLM 可能更擅长寻找反例而非构建优雅的证明，并讨论了 AI 驱动数学的影响。讨论还涉及测试时扩展，评论指出基于采样的方法（如 AlphaCode）在生成大量候选并筛选方面已显示出成功。

hackernews · ColinWright · 8月12日 10:04 · [社区讨论](https://news.ycombinator.com/item?id=49270022)

**背景**: 大型语言模型（LLM）是在海量文本数据上训练的 AI 系统，能够生成类似人类的文本。在数学领域，它们已被用于证明构建和反例生成，近期研究聚焦于测试时扩展，即在推理时使用更多计算来改善输出。高尔斯是菲尔兹奖得主，他的这篇文章为关于 AI 在数学中作用的持续讨论增添了数学家的视角。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.04001">Test-Time Scaling in Reasoning LLMs: Inference Regimes ...</a></li>
<li><a href="https://arxiv.org/abs/2408.03314">[2408.03314] Scaling LLM Test-Time Compute Optimally can be ... GitHub - testtimescaling/testtimescaling.github.io: "what ... What, How, Where, and How Well? A Survey on Test-Time Scaling ... Scaling Test-Time Compute for Longer Thinking in LLMs ... Scaling LLM Test-Time Compute Optimally Can be More Effective ... Scaling LLM Test-Time Compute Optimally Can be More Effective ...</a></li>
<li><a href="https://arxiv.org/html/2603.19514v1">Learning to Disprove: Formal Counterexample Generation with Large Language Models</a></li>

</ul>
</details>

**社区讨论**: 社区讨论强调这篇文章本质上是在讨论测试时扩展，一位评论者指出像 AlphaCode 这样的基于采样的方法早已显示出成功。另一位评论者同意高尔斯关于 AI 在数学中达到人类水平的标准，强调需要新颖且令人惊讶的证明方法。还有一位评论者鉴于 AI 在并发代码上的困难，好奇其在时序逻辑上的表现。

**标签**: `#LLMs`, `#mathematics`, `#AI research`, `#test-time scaling`, `#proof`

---

<a id="item-8"></a>
## [Woxi：用 Rust 重写的开源 Wolfram 语言实现](https://woxi.ad-si.com/) ⭐️ 8.0/10

Woxi 是一个用 Rust 编写的开源 Wolfram 语言解释器，提供类似 Mathematica 的 GUI（Woxi Studio）、CLI、Jupyter 内核、Python 包、npm 包和 WASM 模块。它拥有毫秒级的启动时间，使其适用于 shell 脚本和单行命令。 该项目为专有的 Wolfram 语言提供了一个免费开源的替代方案，可能降低学生、研究人员和开发者的使用门槛。其可嵌入性和快速启动特性可能扩展该语言在脚本和 Web 应用中的使用，挑战 Mathematica 和 Sage 等商业工具的统治地位。 Woxi 通过约 26,000 个单元测试和 900 个.wls 脚本快照测试来确保一致性。该项目目前专注于修复边缘情况、提升性能和扩大社区；可在 GitHub 上获取并进行贡献和错误报告。

hackernews · adius · 8月12日 10:06 · [社区讨论](https://news.ycombinator.com/item?id=49270040)

**背景**: Wolfram 语言是由 Wolfram Research 开发的专有高级多范式编程语言，以符号计算和基于规则的编程而闻名。它是 Mathematica 背后的语言，Mathematica 是一种广泛使用的计算工具。WebAssembly（WASM）是一种可移植二进制代码的开放标准，能够在网页和其他平台上实现高性能应用，使 Woxi 可以在浏览器中运行。Jupyter 内核是特定于语言的进程，能够在 Jupyter 环境中实现交互式执行，促进数据分析和科学计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wolfram_Language">Wolfram Language</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly - Wikipedia</a></li>
<li><a href="https://docs.jupyter.org/en/stable/projects/kernels.html">Kernels (Programming Languages) — Jupyter Documentation 4.1.1 alpha documentation</a></li>

</ul>
</details>

**社区讨论**: 评论者对该项目表示支持，有人希望它能取代 Sage 成为集成良好的开源 CAS。一位用户用 Woxi Studio 测试了多元微积分可视化，发现它能显示，但不确定是否完全正确。另一位指出该项目六个月前已发布，还有一位新手发现 Woxi 能解决 Sympy 等其他工具无法解决的代数问题，从而对 Wolfram 语言产生了兴趣。

**标签**: `#Wolfram Language`, `#Rust`, `#Open Source`, `#Interpreter`, `#Scientific Computing`

---

<a id="item-9"></a>
## [Meta 发布 Muse Glimmer，一款 30B 开源权重智能体模型](https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/#atom-everything) ⭐️ 8.0/10

Meta 推出了 Muse Glimmer，这是一款 300 亿参数的开源权重多模态模型，采用 Apache 2.0 许可证发布，针对智能体任务完成、可靠工具使用和多步推理进行了优化。该模型支持本地部署，在 LM Studio 上提供 18.16 GB 版本，并支持视觉任务。 此次发布意义重大，因为它提供了一款功能强大且许可证宽松的开源权重模型，使开发者能够在本地运行高级智能体工作流，而无需受到限制性许可的约束。这可能加速本地 AI 应用、工具集成和自主任务自动化方面的创新，惠及更广泛的 AI 生态系统。 Muse Glimmer 是一个从 Muse Spark 蒸馏而来的 300 亿参数模型，支持文本和图像输入，并在 vLLM 上提供服务，具有原生的 Onyx 工具调用和推理解析器。它在 DeepSearch QA、MCP-Atlas、τ-Bench 和 SWE-Bench 等基准测试中表现良好，并且可以在 32 GB 或更高内存的消费级硬件上运行。

rss · Simon Willison · 8月10日 23:56

**背景**: 智能体 AI 指的是能够自主推理、规划并执行复杂任务的系统，通常使用工具和多步工作流。开源权重模型允许开发者在本地运行 AI，确保数据隐私和定制化。Apache 2.0 是一种宽松许可证，允许商业使用和修改，与 Meta 之前的一些许可证不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model">Introducing Muse Glimmer: An Open Agentic Model That Runs on ...</a></li>
<li><a href="https://dev.meta.ai/docs/muse-glimmer">Model API | Muse Glimmer</a></li>
<li><a href="https://build.nvidia.com/meta/muse-glimmer-30b/modelcard">muse-glimmer-30b Model by Meta | NVIDIA NIM</a></li>

</ul>
</details>

**标签**: `#AI`, `#Meta`, `#open-weights`, `#agentic`, `#model release`

---

<a id="item-10"></a>
## [AI 先驱在 Ai4 上就开放与安全展开辩论](https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/) ⭐️ 8.0/10

在拉斯维加斯举行的 Ai4 2026 大会上，杰弗里·辛顿、李飞飞和吴恩达就 AI 监管、开源获取以及美国竞争力展开公开辩论，背景是日益增长的安全担忧。辛顿警告开源模型权重可能被滥用，吴恩达主张开放以推动创新，而李飞飞则提出基于风险的透明度方案。 这场辩论凸显了 AI 先驱之间的重大分歧，可能塑造未来的政策和行业实践。他们在开放与监管上的不同立场将影响政府和企业在创新与安全之间的平衡，进而影响全球 AI 竞争格局。 辛顿区分了传统开源软件与开放权重 AI 模型，警告公开权重可能助长滥用。李飞飞认为 AI 改变的是任务而非整个工作，并建议透明度应根据应用场景和相关风险来决定。此次大会汇聚了来自 20 个行业的 12000 多名参与者和 1000 多名演讲者。

rss · TechCrunch AI · 8月12日 17:51

**背景**: Ai4 大会是 AI 商业和政策领域领导者的年度盛会。杰弗里·辛顿是图灵奖得主，常被称为“AI 教父”；李飞飞是著名的计算机视觉研究者；吴恩达是知名的 AI 教育家和企业家。他们的辩论反映了社会在 AI 安全、开源原则和国家竞争力方面的广泛张力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://iblnews.org/story/the-ai4-2026-conference-showed-the-divergence-shaping-the-public-debate-today">The AI4 2026 Conference Showed the Divergence Shaping the ...</a></li>
<li><a href="https://dedirock.com/blog/debate-over-ai-risks-and-regulation-hinton-fei-fei-li-and-andrew-ng-face-off-at-ai4/">Debate Over AI Risks and Regulation : Hinton , Fei - Fei Li ... - DediRock</a></li>
<li><a href="https://www.forbes.com/sites/ronschmelzer/2026/08/06/hinton-li-ng-ai-jobs-regulation/">Three AI Pioneers Clash Over Jobs, Regulation And The Future Of AI</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#open-source`, `#regulation`, `#AI policy`, `#Geoffrey Hinton`

---

<a id="item-11"></a>
## [General Catalyst 领投成立仅两个月的 River AI 11 亿美元融资](https://techcrunch.com/2026/08/11/general-catalyst-leads-1-1b-round-into-2-month-old-river-ai/) ⭐️ 8.0/10

由 xAI 联合创始人 Igor Babuschkin 共同创立的初创公司 River AI 在成立仅两个月后，获得了由 General Catalyst 领投的 11 亿美元融资。这是 AI 初创公司有史以来规模最大的早期融资之一。 这笔巨额投资表明业界对个人 AI 代理这一快速增长的领域充满信心。像 General Catalyst 这样的知名投资者和 xAI 的关键人物的参与，可能会加速个人 AI 代理的开发和采用，从而可能重塑个人与 AI 的互动方式。 本轮融资由 General Catalyst 领投，未披露其他投资者。River AI 专注于开发个人代理，旨在创建能够代表用户执行任务的 AI 系统。该公司成立仅两个月，这使其成为创纪录的早期融资。

rss · TechCrunch AI · 8月11日 17:41

**背景**: Igor Babuschkin 于 2023 年与 Elon Musk 共同创立了 xAI，并于 2025 年 8 月离开公司，创办了自己的风险投资公司。个人 AI 代理是旨在帮助个人完成日程安排、沟通和信息管理等任务的 AI 系统，通常利用大型语言模型。AI 行业对基于代理的初创公司的投资激增，反映出向更自主的 AI 应用发展的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2025/08/13/elon-musks-xai-loses-co-founder-igor-babuschkin-for-venture-firm.html">Elon Musk's xAI loses co-founder Igor Babuschkin, who's ...</a></li>
<li><a href="https://techcrunch.com/2025/08/13/co-founder-of-elon-musks-xai-departs-the-company/">Co-founder of Elon Musk’s xAI departs the company - TechCrunch</a></li>
<li><a href="https://www.businessinsider.com/xai-cofounder-leaving-learned-2-things-from-elon-musk-babuschkin-2025-8">XAI Cofounder Leaving the Company, Says He Learned 2 Things ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#funding`, `#startups`, `#personal agents`

---

<a id="item-12"></a>
## [Anthropic 未发布模型在黎曼猜想上取得进展](https://techcrunch.com/2026/08/11/an-unreleased-anthropic-model-made-progress-on-one-of-maths-biggest-unsolved-problems/) ⭐️ 8.0/10

据报道，Anthropic 未发布的 AI 模型在黎曼猜想这一 150 多年来未解决的重大数学问题上取得了显著进展。该模型并未完全解决该问题，但取得的进展超出了预期。 这一进展凸显了 AI 模型处理复杂数学问题的能力不断增强，可能加速纯数学领域的研究。同时，它也彰显了 Anthropic 模型在高级推理任务中的竞争优势。 具体模型名称及进展的确切性质尚未披露。黎曼猜想涉及黎曼ζ函数零点的分布，其证明将对数论及相关领域产生深远影响。

rss · TechCrunch AI · 8月11日 16:25

**背景**: 黎曼猜想由伯恩哈德·黎曼于 1859 年首次提出，它断言黎曼ζ函数的所有非平凡零点的实部均为 1/2。这是克莱数学研究所的千禧年大奖难题之一，其解决将对素数的分布产生重大影响。像 Anthropic 的 Claude 这样的 AI 模型越来越多地被用于数学推理，但通常只是辅助而非完全解决此类问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://mathworld.wolfram.com/RiemannHypothesis.html">Riemann Hypothesis -- from Wolfram MathWorld</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-4-5">Introducing Claude Opus 4.5 \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#Anthropic`, `#research`, `#Riemann hypothesis`

---

<a id="item-13"></a>
## [Adam 的逐坐标缩放破坏旋转不变性与低秩偏置](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 8.0/10

一项新研究表明，在因子化模型 W=UV^T 中，Adam 的逐坐标二阶矩破坏了旋转不变性，导致其失去梯度下降（GD）所具有的隐式低秩偏置。在矩阵感知任务上对九种更新规则的实验显示，GD、Muon 和 Shampoo 等旋转不变的优化器保留了该偏置，而 Adam、RMSProp、Lion、signum 和 Adafactor 则失去了它。 这一发现指出了决定优化器是否保留隐式低秩偏置的关键机制——逐坐标缩放的各向异性，这对低秩矩阵恢复和深度学习至关重要。它提示从业者在低秩结构重要的任务中应考虑使用 Muon 等旋转不变的优化器，并可能指导新优化器的设计。 该研究使用一个单参数族将 Adam 的分母从逐坐标插值为单一共享标量，结果显示恢复性能沿此路径单调提升，从而将损害归因于各向异性而非一般的自适应性。Muon 在真正低秩目标上表现精确，但随着谱尾增加退化最快，并在约 4%尾能量处与 GD 交叉；作者还发现，在他们自己的优化器中，从逐坐标裁剪改为全局范数裁剪使恢复误差从 0.347 降至 0.220。

reddit · r/MachineLearning · /u/EtherealGlyph · 8月12日 16:39

**背景**: 在 W=UV^T 这样的因子化模型中，损失对因子的正交旋转具有不变性，而梯度下降尊重这种对称性。Adam 的逐坐标二阶矩估计破坏了这种不变性，因为它依赖于因子表达所用的基。隐式偏置是指优化算法即使没有显式正则化也倾向于收敛到具有某些属性（如低秩）的解。像 Muon 这样使用 Newton-Schulz 正交化的旋转不变优化器保留了这种对称性，从而保留了低秩偏置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/rotational-adam-optimizer">Rotational Adam Optimizer</a></li>
<li><a href="https://kellerjordan.github.io/posts/muon/">Muon: An optimizer for hidden layers in neural networks | Keller Jordan blog</a></li>
<li><a href="https://arxiv.org/html/2604.01472v1">The Newton–Muon Optimizer</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论可能包含关于该发现的技术辩论，一些用户质疑 Adam 是否被公平调参，因为作者预料到诸如“你应该更努力地调 Adam”的反对意见。其他人可能讨论对优化器设计的影响以及 Muon 的意外行为，Muon 在不同设置下既表现出谱简单性偏置又拟合虚假特征。

**标签**: `#optimization`, `#low-rank`, `#implicit bias`, `#Adam`, `#matrix sensing`

---

<a id="item-14"></a>
## [解耦下降：通过 AMP 校正实现精确的训练-测试误差跟踪](https://www.reddit.com/r/MachineLearning/comments/1vlu1se/decoupled_descent_enforcing_exact_traintest_error/) ⭐️ 8.0/10

该论文提出了一种新颖的训练方法——解耦下降（DD），利用近似消息传递（AMP）的 Onsager 校正，确保训练误差在每次参数迭代时渐近等于测试误差，从而解决了全批量梯度下降中的数据重用偏差问题。 这项工作为缓解训练-测试差距提供了理论框架，这是神经网络训练中的基本问题，可能有助于改善泛化性能，并实现有原则的早停或超参数调整。它将高维统计与实际优化联系起来，为训练算法提供了新方向。 该方法在风格化的高斯混合模型和高维 XOR 模型（使用两层网络）上进行了验证，显示出比标准梯度下降更好的训练-测试跟踪效果。该论文为预印本，尚未得到广泛验证；作者计划发布一个兼容 PyTorch 的软件包。

reddit · r/MachineLearning · /u/mlovik1 · 8月11日 21:06

**背景**: 近似消息传递（AMP）是一种用于信号恢复的迭代算法，通过 Onsager 校正来跟踪误差的演变，从而实现精确的渐近分析。在梯度下降中，跨迭代重用相同数据会引入偏差，导致训练误差与测试误差偏离。解耦下降应用 AMP 校正来解耦数据重用效应，确保训练和测试误差对齐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/approximate-message-passing-amp-algorithms">Approximate Message Passing Algorithms</a></li>
<li><a href="https://arxiv.org/abs/2201.07487">[2201.07487] A Concise Tutorial on Approximate Message Passing</a></li>
<li><a href="https://arxiv.org/pdf/2604.27883">Decoupled Descent: Exact Test Error Tracking Via Approximate...</a></li>

</ul>
</details>

**社区讨论**: 作者积极邀请讨论和反馈，表明对社区意见持开放态度。该帖评分较高（8/10），表明反响积极，但内容中未提供具体评论。

**标签**: `#machine learning`, `#generalization`, `#approximate message passing`, `#optimization`, `#theory`

---

<a id="item-15"></a>
## [LTX 发布开源视频模型 LTX-2.5，单张 RTX 5090 即可运行](https://ltx.io/model/ltx-2-5) ⭐️ 8.0/10

LTX 发布了开源视频生成基础模型 LTX-2.5，权重、训练代码和推理管线全部开放。该模型可在单张 RTX 5090 GPU 上本地运行，年收入低于 1000 万美元的公司可免费商用。 此次发布通过允许在消费级硬件上进行本地、私有和可定制的部署，使高质量视频生成更加普及。开放权重允许微调和集成到各种工作流中，可能加速 AI 视频制作的创新，并对专有模型构成挑战。 LTX-2.5 支持文生视频和图生视频，改进了多镜头连贯性和提示词遵循。它引入了新的扩散视频解码器，并使用 Gemma 4 12B 文本编码器；在 98 个提示词的文生视频瑕疵评测中，LTX 2.5 Pro 在十款模型中排名第一。

telegram · zaihuapd · 8月12日 02:15

**背景**: 视频生成模型通常需要大量云端资源，但扩散变换器和高效解码器的最新进展使得在 RTX 5090 等高端 GPU（具有 32GB 显存）上进行本地推理成为可能。像 LTX-2.5 这样的开源模型允许开发者无需依赖外部 API 即可运行、微调和部署视频 AI，从而促进隐私和定制化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ltx.io/model/ltx-2-5">LTX-2.5: LTX's Latest AI Open-Source Foundation Model | LTX</a></li>
<li><a href="https://ltx.io/model/open-source">LTX-2.5 Model Open Source: AI Video Generator</a></li>
<li><a href="https://comfy.org/ltx-2.5">LTX 2.5 on Comfy — Open-Source AI Video Model</a></li>

</ul>
</details>

**标签**: `#video generation`, `#open source`, `#AI model`, `#LTX`, `#diffusion`

---

<a id="item-16"></a>
## [中国前总理朱镕基逝世，享年 98 岁](https://www.news.cn/politics/20260812/4c2c72e299ef4561915d2e507393a81f/c.html) ⭐️ 8.0/10

中国国务院前总理朱镕基因病医治无效，于 2026 年 8 月 12 日在北京逝世，享年 98 岁。中共中央、全国人大常委会、国务院、全国政协发布了官方公告。 朱镕基是中国经济改革和加入世贸组织的关键人物，他的逝世标志着中国政治史上一个时代的结束。他在亚洲金融危机期间的政策以及他在塑造社会主义市场经济体制中的作用，继续影响着中国的经济发展轨迹。 朱镕基 1928 年 10 月生于湖南长沙，1949 年 10 月加入中国共产党。他于 1998 年 3 月出任国务院总理，期间实施积极财政政策和稳健货币政策，坚持人民币不贬值，并主持完成了加入世界贸易组织的谈判。

telegram · zaihuapd · 8月12日 10:11

**背景**: 朱镕基是中国著名的领导人，以在 1990 年代经济改革中的角色而闻名。他在财税、金融、国企、住房和粮食流通等领域的重大改革，帮助建立了社会主义市场经济体制的基本框架。他的总理任期恰逢亚洲金融危机和中国于 2001 年加入世贸组织。

**标签**: `#politics`, `#obituary`, `#China`, `#history`

---

<a id="item-17"></a>
## [DeepSeek 发布 V4-Flash API 公测版，Agent 基准测试表现强劲](https://t.me/zaihuapd/43149) ⭐️ 8.0/10

2026 年 7 月 31 日，DeepSeek 上线了 V4-Flash API 的公测版，其 Agent 能力大幅增强，基准测试成绩超越 V4-Pro-Preview。该模型在 Terminal Bench 2.1 上达到 82.7，在 Cybergym 上达到 76.7，在 DSBench-FullStack 上达到 68.7，在 DSBench-Hard 上达到 59.6。 此次发布标志着 DeepSeek 在智能体 AI 领域的持续发力，在衡量软件工程、网络安全和数据科学等真实世界任务完成能力的基准测试中表现优异。这可能加剧 AI 模型提供商之间的竞争，并为开发者构建自主智能体提供更强大、更高效的选择。 V4-Flash API 原生支持 Responses API 格式，并针对 Codex 进行了专门适配。公告中未完全披露模型的架构和尺寸细节，但基准测试的提升表明其在智能体工作流方面进行了显著优化。

telegram · zaihuapd · 8月12日 15:30

**背景**: Terminal Bench 2.1 是一个用于评估 AI 智能体在容器环境中完成复杂任务（如调试代码和解决安全漏洞）能力的基准测试。Cybergym 评估 AI 智能体在真实世界网络安全漏洞分析方面的表现，而 DSBench 则评估数据科学智能体在真实数据分析和建模任务上的能力。这些基准测试旨在衡量智能体超越简单语言理解的实际任务执行能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tbench.ai/news/terminal-bench-2-1">Terminal-Bench 2.1</a></li>
<li><a href="https://www.cybergym.io/cybergym/">CyberGym: Evaluating AI Agents' Real-World Cybersecurity ...</a></li>
<li><a href="https://github.com/LiqiangJing/DSBench">GitHub - LiqiangJing/DSBench: [ICLR 2025] DSBench: How Far ...</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#API`, `#AI`, `#benchmark`, `#agent`

---