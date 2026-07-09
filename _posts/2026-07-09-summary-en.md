---
layout: default
title: "Horizon Summary: 2026-07-09 (EN)"
date: 2026-07-09
lang: en
---

> From 40 items, 15 important content pieces were selected

---

1. [TypeScript 7.0 Rewrites Compiler in Go, Boosts Speed 10x](#item-1) ⭐️ 9.0/10
2. [EU Nears Revival of Private Message Scanning Rules](#item-2) ⭐️ 9.0/10
3. [Bun Rewritten from Zig to Rust](#item-3) ⭐️ 9.0/10
4. [John Deere Settles FTC Right-to-Repair Lawsuit](#item-4) ⭐️ 8.0/10
5. [OpenAI on Improving Coding Evaluation Signal](#item-5) ⭐️ 8.0/10
6. [Mistral Unveils Robostral Navigate for Map-Less Navigation](#item-6) ⭐️ 8.0/10
7. [xAI Releases Grok 4.5 with Cursor Data](#item-7) ⭐️ 8.0/10
8. [OpenAI Launches GPT-Live Real-Time Voice Mode](#item-8) ⭐️ 8.0/10
9. [Cloudflare Meerkat: First Production Async Consensus](#item-9) ⭐️ 8.0/10
10. [LingBot-Video: Open-Source Sparse-MoE Video Diffusion Transformer](#item-10) ⭐️ 8.0/10
11. [Alibaba Orders Employees to Uninstall Claude by July 10](#item-11) ⭐️ 8.0/10
12. [Huawei 5G Flagship Returns Overseas, Peak Speed Exceeds 1100 Mbps](#item-12) ⭐️ 8.0/10
13. [Critical Android Remote Root Exploit Chain Disclosed](#item-13) ⭐️ 8.0/10
14. [Meituan's OWL Model Leaks Session Data on OpenRouter](#item-14) ⭐️ 8.0/10
15. [EM Side-Channel Attack Identifies Apps with 99% Accuracy](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TypeScript 7.0 Rewrites Compiler in Go, Boosts Speed 10x](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 9.0/10

Microsoft announced TypeScript 7.0, featuring a complete rewrite of the compiler in Go, achieving 8–12x speed improvements across major codebases like VS Code (11.9x faster) and Sentry (8.9x faster). This dramatic performance improvement makes TypeScript significantly faster for large-scale projects, reducing type-checking times from minutes to seconds, which enhances developer productivity and could accelerate adoption in performance-sensitive environments. The rewrite is still a work in progress and not yet at full feature parity with the original TypeScript compiler; the Go-based compiler is available in a staging repository on GitHub. The speedups were measured on real-world codebases, with the largest gain (11.9x) on the VS Code repository.

hackernews · DanRosenwasser · Jul 8, 16:06 · [Discussion](https://news.ycombinator.com/item?id=48833715)

**Background**: TypeScript is a typed superset of JavaScript that compiles to plain JavaScript. Its original compiler (tsc) was written in JavaScript/TypeScript, which limited performance on large codebases. Go is a compiled language known for its speed and concurrency, making it an ideal choice for rewriting performance-critical compiler components.

<details><summary>References</summary>
<ul>
<li><a href="https://www.devbolt.dev/blog/typescript-7-go-rewrite">TypeScript 7.0: What the Go Rewrite Means for Every Developer</a></li>
<li><a href="https://github.com/microsoft/typescript-go">GitHub - microsoft/typescript-go: Staging repo for ...</a></li>

</ul>
</details>

**Discussion**: The community reacted positively, with many congratulating the team and noting the impressive speedup numbers. Some users discussed the difficulty of maintaining two codebases simultaneously, while others expressed hope for a future Rust rewrite. A few comments highlighted the contrast with other languages that lack TypeScript's type system sophistication.

**Tags**: `#TypeScript`, `#compiler`, `#performance`, `#programming languages`

---

<a id="item-2"></a>
## [EU Nears Revival of Private Message Scanning Rules](https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/) ⭐️ 9.0/10

The European Union is one step away from reviving Regulation (EU) 2021/1232, which would allow providers to voluntarily scan private messages for child sexual abuse material (CSAM), potentially leading to mandatory scanning under Chat Control 2.0. This move threatens end-to-end encryption (E2EE) by enabling client-side scanning, which could undermine privacy for billions of users across Europe and set a precedent for global surveillance. The temporary regulation originally created an exemption to the ePrivacy Directive, and its revival is seen as a stepping stone to Chat Control 2.0, which would mandate scanning and effectively ban E2EE.

hackernews · ggirelli · Jul 8, 16:53 · [Discussion](https://news.ycombinator.com/item?id=48834296)

**Background**: End-to-end encryption (E2EE) ensures that only the sender and intended recipient can read messages, preventing third parties—including service providers—from accessing content. The EU's Chat Control proposals aim to combat CSAM but have sparked debate over privacy and security, with critics arguing that mandatory scanning would break E2EE and enable mass surveillance.

<details><summary>References</summary>
<ul>
<li><a href="https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/">EU now one step away from reviving private message scanning rules</a></li>
<li><a href="https://en.wikipedia.org/wiki/End-to-end_encryption">End-to-end encryption</a></li>
<li><a href="https://closednetwork.io/eu-chat-control-the-fight-to-scan-every-private-message-live-tracker/">EU Chat Control: The Fight to Scan Every Private Message (Live Tracker)</a></li>

</ul>
</details>

**Discussion**: Community comments express strong opposition, with users highlighting the role of organizations like the Internet Watch Foundation in pushing client-side scanning. Some distinguish between voluntary scanning (Chat Control 1.0) and mandatory scanning (Chat Control 2.0), while others question the technical feasibility of bypassing such restrictions with open-source clients and out-of-band key exchange.

**Tags**: `#privacy`, `#encryption`, `#EU regulation`, `#surveillance`, `#cybersecurity`

---

<a id="item-3"></a>
## [Bun Rewritten from Zig to Rust](https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/#atom-everything) ⭐️ 9.0/10

Jarred Sumner announced that Bun, the JavaScript runtime, has been rewritten from Zig to Rust, using AI coding agents to automate much of the port. The rewrite took 11 days and cost approximately $165,000 in API tokens. This rewrite demonstrates that AI-assisted large-scale rewrites are now feasible, challenging the long-held belief that rewrites are too risky. It also highlights Rust's memory safety advantages, which could influence future runtime development. The new Rust version of Bun has been live in Claude Code since June 17, 2026, with 10% faster startup on Linux and no noticeable changes for users. The rewrite used 5.9 billion uncached input tokens and 690 million output tokens.

rss · Simon Willison · Jul 8, 23:57

**Background**: Bun is a fast all-in-one JavaScript runtime, package manager, and test runner, originally written in Zig. Zig is a systems programming language that requires manual memory management, while Rust provides memory safety guarantees through its ownership model and borrow checker. The rewrite was enabled by Bun's extensive TypeScript test suite, which served as a conformance suite for the AI agents.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Memory_safety">Memory safety - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed feelings: some praised the disciplined use of AI and the benefits of Rust's memory safety, while others criticized the abandonment of the Zig version and lack of LTS support. One commenter noted that the rewrite's success reflects poorly on Zig, as it fixed memory leaks and improved stability.

**Tags**: `#Bun`, `#Rust`, `#Zig`, `#runtime`, `#rewrite`

---

<a id="item-4"></a>
## [John Deere Settles FTC Right-to-Repair Lawsuit](https://apnews.com/article/john-deere-right-to-repair-agriculture-equipment-cb7514ffedb95c130a976af661f2bc02) ⭐️ 8.0/10

John Deere has settled a Federal Trade Commission lawsuit, agreeing to provide farmers and independent repair shops with the same diagnostic and repair tools available to its authorized dealers. This settlement sets a legal precedent for the right-to-repair movement in agriculture, potentially influencing similar policies for other industries like automotive and electronics. Deere must pay $1 million collectively to five states for antitrust enforcement costs and will be under strict compliance oversight for 10 years, though critics note the fine is minimal relative to its profits.

hackernews · djoldman · Jul 8, 23:37 · [Discussion](https://news.ycombinator.com/item?id=48838876)

**Background**: The right-to-repair movement advocates for consumers' ability to maintain and repair their own products, countering manufacturer-imposed restrictions on parts, tools, and software. John Deere had long restricted access to diagnostic software and repair manuals, forcing farmers to rely on authorized dealers for repairs.

<details><summary>References</summary>
<ul>
<li><a href="https://apnews.com/article/john-deere-right-to-repair-agriculture-equipment-cb7514ffedb95c130a976af661f2bc02">John Deere owners will get the right to repair their own equipment under a new FTC settlement</a></li>
<li><a href="https://www.usatoday.com/story/money/agriculture/2026/07/08/john-deere-right-to-repair-lawsuit-settled/90850880007/">John Deere settles federal lawsuit over right-to-repair dispute</a></li>
<li><a href="https://pirg.org/resources/john-deere-and-right-to-repair-over-the-years/">John Deere and Right to Repair over the years</a></li>

</ul>
</details>

**Discussion**: Community comments largely celebrate the settlement but criticize the small fine, with one user noting it's a fraction of Deere's profits. Others hope the precedent extends to modern cars, while some highlight the role of activists like Louis Rossmann in advancing right-to-repair.

**Tags**: `#right-to-repair`, `#FTC`, `#agriculture`, `#consumer rights`, `#regulation`

---

<a id="item-5"></a>
## [OpenAI on Improving Coding Evaluation Signal](https://openai.com/index/separating-signal-from-noise-coding-evaluations/) ⭐️ 8.0/10

OpenAI published an analysis of challenges in coding evaluations, including benchmark contamination and cheating, and proposed methods to improve signal quality. This is significant because reliable coding benchmarks are crucial for measuring progress in AI-assisted software development; addressing contamination and cheating helps ensure that reported performance reflects genuine capability. The analysis likely covers issues like test set leakage into training data and adversarial submissions, and suggests techniques such as manual inspection and randomized testing to detect cheating.

hackernews · sk4rekr0w · Jul 8, 21:03 · [Discussion](https://news.ycombinator.com/item?id=48837396)

**Background**: Benchmark contamination occurs when evaluation data inadvertently appears in training sets, inflating scores. Cheating in coding benchmarks includes modifying timeouts, hardware configs, or reward hacking. These issues undermine the validity of AI coding evaluations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.deeplearning.ai/the-batch/the-problem-with-benchmark-contamination-in-ai/">The Problem with Benchmark Contamination in AI</a></li>
<li><a href="https://arxiv.org/abs/2406.04244">[2406.04244] Benchmark Data Contamination of Large Language Models: A Survey</a></li>
<li><a href="https://arxiv.org/abs/2606.07379">[2606.07379] Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests</a></li>

</ul>
</details>

**Discussion**: Commenters noted widespread fake results on Terminal Bench 2 and called for benchmarks that measure efficiency alongside intelligence, e.g., how much a model can accomplish with a fixed API budget. Some argued that flawed benchmarks are inevitable and that the community should move on.

**Tags**: `#AI benchmarks`, `#coding evaluations`, `#OpenAI`, `#machine learning`, `#software engineering`

---

<a id="item-6"></a>
## [Mistral Unveils Robostral Navigate for Map-Less Navigation](https://mistral.ai/news/robostral-navigate/) ⭐️ 8.0/10

Mistral AI has announced Robostral Navigate, an 8-billion-parameter robotics navigation model that enables robots to follow natural language instructions using only a single RGB camera, achieving state-of-the-art results on the R2R-CE benchmark. This model represents a significant step toward map-less navigation, potentially solving the 'kidnapped robot' problem and enabling robots to navigate unfamiliar environments without pre-built maps, which could accelerate adoption in industrial automation and hobbyist robotics. The model is trained entirely in simulation and combines pointing-based navigation with reinforcement learning for continuous improvement. It is not openly available, which limits hobbyist experimentation.

hackernews · ottomengis · Jul 8, 14:09 · [Discussion](https://news.ycombinator.com/item?id=48832212)

**Background**: Traditional robot navigation often relies on pre-built maps of the environment, which can be costly to create and fail when the robot is moved without its knowledge (the 'kidnapped robot' problem). Map-less navigation using vision and language models aims to overcome this by allowing robots to interpret natural language commands and navigate using only visual input. Mistral's model uses a single RGB camera, making it more accessible than systems requiring specialized sensors.

<details><summary>References</summary>
<ul>
<li><a href="https://mistral.ai/news/robostral-navigate/">Robostral Navigate: single-camera AI navigation | Mistral AI</a></li>
<li><a href="https://x.com/MistralAI/status/2074856309438980145">Mistral AI on X: "Announcing Robostral Navigate, our first model for embodied navigation: an 8B robotics navigation model that guides robots to autonomously perform tasks specified with natural language. Single RGB camera. State-of-the-art on R2R-CE. https://t.co/UlmUsXNxhX" / X</a></li>
<li><a href="https://cryptobriefing.com/mistral-robostral-navigate-robotics-model/">Mistral AI unveils Robostral Navigate, an 8B robotics model that could reshape industrial automation investing</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about the map-less navigation capability, with some hoping to integrate it into hobbyist projects like OpenClaw. However, concerns were raised about the lack of open availability and insufficient technical details in the blog post.

**Tags**: `#robotics`, `#AI`, `#navigation`, `#Mistral`, `#deep learning`

---

<a id="item-7"></a>
## [xAI Releases Grok 4.5 with Cursor Data](https://x.ai/news/grok-4-5) ⭐️ 8.0/10

xAI has released Grok 4.5, a cost-efficient model that rivals Opus 4.7 in benchmarks, trained on trillions of tokens of Cursor user interaction data. Grok 4.5's strong performance at a lower price point ($2/$6 per million tokens) could disrupt the AI model market, but community skepticism about political bias and ethics may hinder enterprise adoption. Grok 4.5 is based on a 1.5 trillion parameter V9 foundation model with supplemental training on Cursor data, and is currently in private beta at SpaceX and Tesla. It offers 4x better reasoning efficiency than Opus while being priced at $2/$6 per million tokens.

hackernews · BoumTAC · Jul 8, 18:00 · [Discussion](https://news.ycombinator.com/item?id=48835111)

**Background**: Grok is a series of large language models developed by xAI, Elon Musk's AI company. Cursor is an AI-powered code editor that collects user interaction data for model training when privacy mode is off. The use of real-world coding data from Cursor is seen as a key advantage for improving model capabilities on practical tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://x.ai/news/grok-4-5">Introducing Grok 4.5 | SpaceXAI</a></li>
<li><a href="https://x.com/elonmusk/status/2071184354756477041">Elon Musk on X: "Grok 4.5, based on our 1.5T V9 foundation model, with Cursor data added in supplemental training, is now in private beta at SpaceX & Tesla. Early evals show performance close to, perhaps exceeding Opus. RL is continuing to significantly improve the model, and the Grok Build" / X</a></li>
<li><a href="https://www.axios.com/2026/07/08/spacexai-grok-new-model">Scoop: SpaceXAI launches new model, Grok 4.5</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed sentiments: some users praise the model's cost efficiency and benchmark performance, while others raise concerns about political bias and ethical issues, questioning the trustworthiness of xAI models for business use.

**Tags**: `#AI`, `#LLM`, `#xAI`, `#Grok`, `#benchmarks`

---

<a id="item-8"></a>
## [OpenAI Launches GPT-Live Real-Time Voice Mode](https://openai.com/index/introducing-gpt-live/) ⭐️ 8.0/10

OpenAI has launched GPT-Live, a full-duplex voice mode for ChatGPT that enables real-time, natural conversations and can delegate complex tasks to GPT-5.5 in the background. This marks a significant advancement in AI assistants by removing the latency and turn-taking constraints of previous voice modes, allowing users to have extended, productive conversations while leveraging the latest frontier model for heavy lifting. GPT-Live is built on a full-duplex architecture, meaning it can listen and speak simultaneously, and it can show attentiveness with phrases like 'mhmm' or stay quiet when needed. The feature is rolling out to Go, Plus, Pro, and Free users.

hackernews · logickkk1 · Jul 8, 17:03 · [Discussion](https://news.ycombinator.com/item?id=48834405)

**Background**: Previous voice modes in ChatGPT were half-duplex, requiring the user to finish speaking before the AI responded, which made conversations feel unnatural. GPT-5.5, released in April 2026, is OpenAI's most capable model, excelling at coding, research, and tool use. GPT-Live bridges the gap between a natural voice interface and the power of a frontier model.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-live/">Introducing GPT‑Live - OpenAI</a></li>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT-5.5 | OpenAI</a></li>
<li><a href="https://venturebeat.com/technology/openai-launches-gpt-live-a-full-duplex-voice-upgrade-that-lets-chatgpt-talk-more-like-a-person">OpenAI launches GPT-Live, a full-duplex voice upgrade that ...</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some users praise the natural conversation flow and delegation to GPT-5.5, while others express concerns about AI replacing human relationships. A notable bug was reported where the model interrupts and laughs at unintended moments. Some users also lament the lack of tool/connector support in voice mode.

**Tags**: `#AI`, `#OpenAI`, `#voice assistant`, `#GPT-5.5`, `#real-time`

---

<a id="item-9"></a>
## [Cloudflare Meerkat: First Production Async Consensus](https://blog.cloudflare.com/meerkat-introduction/) ⭐️ 8.0/10

Cloudflare has introduced Meerkat, a globally distributed consensus protocol based on QuePaxa, which is the first production implementation of an asynchronous consensus algorithm that does not rely on timeouts. This marks a significant step in distributed systems, as it offers leaderless asynchronous consensus in production for the first time, potentially improving robustness under adverse network conditions where traditional protocols like Paxos and Raft struggle. Meerkat is based on QuePaxa, which uses randomized asynchronous consensus and hedging instead of timeouts to achieve liveness. However, it requires global consensus for every read operation, which may increase read latency compared to systems with local reads.

hackernews · bobnamob · Jul 8, 13:18 · [Discussion](https://news.ycombinator.com/item?id=48831565)

**Background**: Traditional consensus protocols like Paxos and Raft are partially synchronous, relying on timeouts to ensure liveness. This makes them vulnerable to network delays and leader flapping. Asynchronous consensus protocols like QuePaxa avoid timeouts entirely, guaranteeing progress even under unpredictable delays, but have historically been too inefficient for production use.

<details><summary>References</summary>
<ul>
<li><a href="https://bford.info/pub/os/quepaxa/quepaxa.pdf">QuePaxa: Escaping the Tyranny of Timeouts in Consensus Pasindu Tennage* EPFL</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3600006.3613150">QuePaxa: Escaping the tyranny of timeouts in consensus | Proceedings of the 29th Symposium on Operating Systems Principles</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Meerkat is the first production implementation of an asynchronous consensus algorithm, which is a genuine novelty. Some expressed concern about read latency due to global consensus on every read, while others argued it could be valuable for messy networks where leader-based protocols fail.

**Tags**: `#distributed systems`, `#consensus`, `#asynchronous`, `#Cloudflare`, `#QuePaxa`

---

<a id="item-10"></a>
## [LingBot-Video: Open-Source Sparse-MoE Video Diffusion Transformer](https://www.reddit.com/r/MachineLearning/comments/1ur0bxq/lingbotvideo_sparsemoe_video_diffusion/) ⭐️ 8.0/10

LingBot-Video, a 13B-parameter sparse mixture-of-experts video diffusion transformer with only 1.4B active parameters, has been released as open source with weights, code, and a Diffusers/SGLang stack. It includes reinforcement learning post-training with six rewards, including a physical-plausibility reward graded by a vision-language model, and an action-conditioned world model mode for predicting robot rollouts. This work pushes the boundary of open-source video generation by combining sparse MoE efficiency with RL post-training, and explicitly frames the model as a world model for action planning. It raises critical questions about using VLMs as physics judges and the distinction between video generators and world models, which are central to robotics and embodied AI research. The model uses a single-stream diffusion transformer with DeepSeek-V3-style sparse MoE (128 experts, top-8 routing). It achieves top average on RBench but is second on general text-to-video in its own evaluation, and no closed-loop robot results are provided despite the world model framing.

reddit · r/MachineLearning · /u/Savings-Display5123 · Jul 8, 17:58

**Background**: Sparse mixture-of-experts (MoE) architectures scale model capacity without proportional compute by activating only a subset of parameters per token. DeepSeek-V3 popularized this approach in large language models. Video diffusion transformers generate videos by iteratively denoising latent representations. Goodhart's law warns that when a metric becomes a target, it ceases to be a good measure; using a VLM to judge physical plausibility risks reward hacking.

<details><summary>References</summary>
<ul>
<li><a href="https://machinelearningmastery.com/mixture-of-experts-architecture-in-transformer-models/">Mixture of Experts Architecture in Transformer Models</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://arxiv.org/abs/2412.19437">[2412.19437] DeepSeek-V3 Technical Report - arXiv.org Images DeepSeek-V3: Open Sparse MoE Model - api.emergentmind.com GitHub - RushilJ2603/DeepSeek-V3-Sparse-MoE-Architecture ... Training Pipeline | deepseek-ai/DeepSeek-V3 | DeepWiki DeepSeek V3: Architecture, Benchmarks & Legacy Status</a></li>

</ul>
</details>

**Discussion**: The Reddit community expressed skepticism about using a VLM as a physics judge, citing Goodhart's law and the lack of closed-loop robot validation. Some appreciated the open-source contribution and sparse MoE design, but many questioned whether the model truly qualifies as a world model without physical interaction results.

**Tags**: `#video diffusion`, `#sparse MoE`, `#world model`, `#reinforcement learning`, `#open-source`

---

<a id="item-11"></a>
## [Alibaba Orders Employees to Uninstall Claude by July 10](https://t.me/zaihuapd/42424) ⭐️ 8.0/10

Alibaba has internally ordered all employees to uninstall Anthropic products, including Claude models (Sonnet, Opus, Fable) and Claude Code, effective July 10. This follows Anthropic's allegations that Alibaba used 25,000 fake accounts to interact with Claude over 28 million times between April 22 and June 5. This marks a major corporate policy shift, highlighting growing tensions between US and Chinese AI companies over model security and intellectual property. It could affect how Chinese tech firms access frontier AI models and may lead to stricter usage policies industry-wide. Alibaba previously reimbursed employees for using external models like Claude, GPT, and Gemini. The ban covers all Anthropic products including Sonnet, Opus, Fable models and Claude Code agent tool. Anthropic tightened its risk control policies after the alleged abuse.

telegram · zaihuapd · Jul 8, 06:09

**Background**: Claude is a family of large language models developed by Anthropic, with variants like Sonnet, Opus, and Fable optimized for different tasks. Claude Code is an agentic coding tool that can read codebases, edit files, and run commands. Model distillation involves using a larger model's outputs to train a smaller model, which can infringe on intellectual property if done without authorization.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/sites/jonmarkman/2026/06/26/anthropic-says-alibaba-used-25000-fake-accounts-to-distill-claude/">Anthropic Says Alibaba Used 25,000 Fake Accounts To Distill ...</a></li>
<li><a href="https://www.explainx.ai/blog/anthropic-alibaba-claude-distillation-25000-fake-accounts-2026">Anthropic vs Alibaba — 25K Fake Claude Accounts, Distillation ...</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Alibaba`, `#Claude`, `#Anthropic`, `#corporate policy`

---

<a id="item-12"></a>
## [Huawei 5G Flagship Returns Overseas, Peak Speed Exceeds 1100 Mbps](https://finance.sina.com.cn/tech/roll/2026-07-08/doc-inihapna8035781.shtml) ⭐️ 8.0/10

Huawei's Pura 90 Pro Max international version natively supports 5G, achieving peak download speeds over 1100 Mbps in overseas tests, marking the return of Huawei 5G flagships to global markets after seven years of US sanctions. This signals Huawei's successful technological breakthrough in 5G despite sanctions, potentially reshaping the global high-end smartphone market by offering a competitive alternative to Apple and Samsung. The device runs HarmonyOS 6.0.0.125 and incorporates Huawei's 5A communication technology, which is not a new network standard but represents a 5A-level premium network experience with faster access and lower latency.

telegram · zaihuapd · Jul 8, 12:17

**Background**: Since 2019, US sanctions prevented Huawei from selling 5G phones globally. In 2023, the Mate 60 series broke through technical restrictions, and subsequent software updates like HarmonyOS 6.0.0.125 enabled 5G capabilities. The 5A technology, introduced in late 2025, is a marketing term for Huawei's advanced communication features, distinct from 5G-A or 5.5G.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/0/901/311.htm">华为官网详解“5A”先进通信技术：不等同于 5G-A / 5.5G，不涉及额外资...</a></li>
<li><a href="https://consumer.huawei.com/cn/support/content/zh-cn16081318/">华为5A相关问题汇总 | 华为官网 - HUAWEI</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1995465853668443610">2个多GB的鸿蒙6.0.0.125升级包已到位,有什么亮点？值得冲吗</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#5G`, `#smartphone`, `#technology`, `#telecommunications`

---

<a id="item-13"></a>
## [Critical Android Remote Root Exploit Chain Disclosed](https://www.coolapk.com/feed/72700258?s=ZGQ2MTVlZjYxMDYyNTM3ZzZhNGUzOThjega1640) ⭐️ 8.0/10

Nebula Security disclosed a remote root exploit chain called IonStack that combines a Firefox browser vulnerability and a 15-year-old Linux kernel flaw (CVE-2026-43499, GhostLock) to achieve one-click full device compromise on all Android versions up to 17. This is the first public root exploit chain for Android 17, demonstrating that even fully updated devices are vulnerable to a single malicious URL click, posing a severe threat to billions of Android users worldwide. The exploit chain uses a remote code execution vulnerability in Firefox 151.0.2 and earlier to gain initial access, then escalates to root via the GhostLock kernel flaw; a proof-of-concept has been published on GitHub, but full exploit details are withheld.

telegram · zaihuapd · Jul 8, 13:01

**Background**: Android devices rely on a layered security model, with the Linux kernel as the foundation. A remote root exploit bypasses all layers, giving an attacker full control. The GhostLock vulnerability (CVE-2026-43499) is a use-after-free bug in the kernel's futex subsystem, present since 2011.

<details><summary>References</summary>
<ul>
<li><a href="https://cyberpress.org/ionstack-attack-full-control-android/">IonStack Attack Lets Hackers Gain Full Control of Android ...</a></li>
<li><a href="https://cybersecuritynews.com/android-17-root-1-click/">First-Ever 1- Click Android 17 Exploit Allows Attackers to ...</a></li>
<li><a href="https://threat-modeling.com/cve-2026-43499-ghostlock-linux-kernel-root-container-escape/">CVE-2026-43499 “GhostLock”: 15-Year-Old Linux Kernel Flaw ...</a></li>

</ul>
</details>

**Tags**: `#Android`, `#security`, `#vulnerability`, `#root exploit`, `#Linux kernel`

---

<a id="item-14"></a>
## [Meituan's OWL Model Leaks Session Data on OpenRouter](https://github.com/gumusserv/ProducerBenchV2/blob/83cad6007ef3fe8df33386e8f43738fe62337e16/parsed_source_data/data/) ⭐️ 8.0/10

Meituan's OWL (LongCat) free test model on OpenRouter reportedly leaked session data, with a GitHub repository containing the data now taken private. The leak was discovered by a Discord bot token scanner on July 7, 2026. This incident highlights the security risks of using public LLM models for sensitive data, as session logs can become new sensitive assets. It undermines user trust and underscores the need for stricter data handling policies in AI services. The leaked data was hosted on a GitHub repository that was publicly accessible until it was taken private. A Discord bot token scanner detected exposed tokens and triggered a reset, suggesting that API keys or credentials may have been compromised.

telegram · zaihuapd · Jul 8, 13:35

**Background**: Meituan's LongCat-2.0 is a 1.6 trillion parameter MoE model, MIT-licensed and trained on domestic Chinese chips. OpenRouter is a platform that provides unified API access to hundreds of LLMs. Previous incidents with Google and DeepSeek have also warned that user conversation data may be used for model improvement.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>
<li><a href="https://top.gg/bot/842154960397008896">Add Token Scanner Discord Bot | The #1 Discord Bot and ...</a></li>

</ul>
</details>

**Discussion**: The community expressed concern over the leak, with users on Xiaohongshu sharing screenshots and warning others not to input sensitive information into public models. Some noted that similar risks exist with other providers and called for better transparency.

**Tags**: `#data leak`, `#LLM security`, `#privacy`, `#Meituan`, `#OpenRouter`

---

<a id="item-15"></a>
## [EM Side-Channel Attack Identifies Apps with 99% Accuracy](https://www.scmp.com/news/china/science/article/3359688/chinese-researchers-find-peephole-any-smartphone-its-leaked-radio-signal) ⭐️ 8.0/10

Chinese researchers have developed a non-contact forensic technique that identifies smartphone apps and operations by analyzing leaked low-frequency electromagnetic signals, achieving up to 99.07% accuracy on devices like iPhone 15 Pro, Xiaomi 15 Pro, and OPPO Reno 13. This technique poses a significant privacy and security threat as it works even when the device is offline, in airplane mode, encrypted, or locked, without requiring access to the device's system or stored data. It could be used for surveillance or forensic investigations, raising concerns about mobile device security. The technique targets low-frequency electromagnetic emissions (below 1 MHz) from the device's processor and memory during app execution, using a deep learning model to classify the signals. Tests on three smartphones showed accuracy ranging from 88.7% to 99.07% for apps like Douyin, WeChat video calls, Baidu Maps, SMS, browser, camera, and cloud storage.

telegram · zaihuapd · Jul 8, 16:05

**Background**: Electromagnetic side-channel attacks exploit unintentional EM emissions from electronic devices to extract sensitive information. Unlike traditional side-channel attacks that require physical access or power analysis, this non-contact method can be performed remotely, making it particularly dangerous for mobile security.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Electromagnetic_attack">Electromagnetic attack - Wikipedia</a></li>
<li><a href="https://www.allaboutcircuits.com/technical-articles/em-side-channel-attacks-on-cryptography/">EM Side-Channel Attacks on Cryptography - Technical Articles</a></li>

</ul>
</details>

**Tags**: `#security`, `#privacy`, `#mobile forensics`, `#electromagnetic side-channel`, `#research`

---