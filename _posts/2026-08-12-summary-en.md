---
layout: default
title: "Horizon Summary: 2026-08-12 (EN)"
date: 2026-08-12
lang: en
---

> From 85 items, 17 important content pieces were selected

---

1. [Qwen Releases Qwen3.8-2.4T-A95B, a Massive MoE Model](#item-1) ⭐️ 9.0/10
2. [Encrypted Chain-of-Thought Traces Stolen from Major LLM APIs](#item-2) ⭐️ 9.0/10
3. [vLLM v0.27.0 Adds Kimi K3, PyTorch 2.13, and Deep FlashAttention 4](#item-3) ⭐️ 8.0/10
4. [DeepSeek V4 Pro 0813: Competitive Performance at Lower Cost](#item-4) ⭐️ 8.0/10
5. [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](#item-5) ⭐️ 8.0/10
6. [AI Is Removing the Middle Class of Software Engineering](#item-6) ⭐️ 8.0/10
7. [Mathematician Analyzes LLM Strengths in Finding Counterexamples](#item-7) ⭐️ 8.0/10
8. [Woxi: Open-Source Rust Reimplementation of Wolfram Language](#item-8) ⭐️ 8.0/10
9. [Meta Releases Muse Glimmer, a 30B Open-Weights Agentic Model](#item-9) ⭐️ 8.0/10
10. [AI Pioneers Debate Openness vs. Safety at Ai4](#item-10) ⭐️ 8.0/10
11. [General Catalyst leads $1.1B round into 2-month-old River AI](#item-11) ⭐️ 8.0/10
12. [Anthropic's Unreleased Model Advances on Riemann Hypothesis](#item-12) ⭐️ 8.0/10
13. [Adam's Coordinate Scaling Breaks Rotation Invariance and Low-Rank Bias](#item-13) ⭐️ 8.0/10
14. [Decoupled Descent: Exact Train-Test Error Tracking via AMP Corrections](#item-14) ⭐️ 8.0/10
15. [LTX Releases Open-Source Video Model LTX-2.5, Runs on Single RTX 5090](#item-15) ⭐️ 8.0/10
16. [Former Chinese Premier Zhu Rongji Dies at 98](#item-16) ⭐️ 8.0/10
17. [DeepSeek Launches V4-Flash API Public Beta with Strong Agent Benchmarks](#item-17) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwen Releases Qwen3.8-2.4T-A95B, a Massive MoE Model](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen has released Qwen3.8-2.4T-A95B, a sparse mixture-of-experts model with 2.4 trillion total parameters and 95 billion active parameters per token. It is the open-weight variant of Qwen3.8-Max and claims performance between Opus 4.8 and Fable 5. This release brings near-frontier capabilities to the open ecosystem, potentially democratizing access to top-tier AI performance. The community highlights that quantized versions (e.g., 1-bit at 397GB) could enable local deployment on consumer hardware, which is a significant step for individual users. The model has a vocabulary size of about 248k, larger than other recent Chinese models like Kimi K3 (~164k) and DeepSeek-V4 (~129k). It is initially released in BF16 and FP8 formats, with no QAT for 4-bit quantization, meaning community quantization may be needed for smaller sizes. The full BF16 model is about 4.9TB, while a 1-bit quantized version is around 397GB.

hackernews · Philpax · Aug 12, 15:01 · [Discussion](https://news.ycombinator.com/item?id=49273478)

**Background**: Mixture-of-Experts (MoE) models activate only a subset of parameters per token, allowing for massive total parameter counts while keeping inference costs manageable. Quantization reduces model size and memory requirements by lowering the precision of weights, which is crucial for deploying large models on limited hardware. Qwen is a series of large language models developed by Alibaba, and Qwen3.8-Max is its flagship model with additional features like vision input and 1M context length.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/">Serve Qwen3.8-2.4T-A95B, a 2.4T-Parameter Model, with ...</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.8-2.4t-a95b">Qwen3.8 2.4T A95B - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://forums.developer.nvidia.com/t/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/379956">Serve Qwen3.8-2.4T-A95B, a 2.4T-Parameter Model, with ...</a></li>

</ul>
</details>

**Discussion**: Community comments express excitement about the model's performance and the potential for local deployment via quantization, with one user noting the 1-bit quant at 397GB puts Opus 4.5-level performance within reach of a normal person's machine. Some concerns are raised about the lack of vision support and 1M context length in the open-weight version, as well as the serving challenges due to the large size and licensing restrictions.

**Tags**: `#AI/ML`, `#Large Language Models`, `#Open Source`, `#Model Release`, `#MoE`

---

<a id="item-2"></a>
## [Encrypted Chain-of-Thought Traces Stolen from Major LLM APIs](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/#atom-everything) ⭐️ 9.0/10

A research paper demonstrates that encrypted chain-of-thought blocks from Anthropic, OpenAI, and Google can be replayed and jailbroken to recover hidden reasoning traces in plaintext. The attack exploits the fact that models in the same family share encryption keys, allowing weaker models to decode the stronger models' reasoning. This vulnerability exposes hidden chain-of-thought reasoning in major proprietary LLM APIs, undermining the security measures designed to protect intellectual property and prevent information leakage. It highlights a critical flaw in API design that could have significant implications for AI safety and privacy. The attack was demonstrated on models like Claude Haiku 4.5, which was the easiest to attack, using a simple prompt to transcribe the reasoning. The paper includes extensive details of extracted reasoning traces in the appendix, and all providers have acknowledged the report and fixed the issue.

rss · Simon Willison · Aug 11, 22:40

**Background**: Chain-of-thought (CoT) reasoning is a technique where LLMs generate step-by-step reasoning before producing a final answer. To protect intellectual property and limit information leakage, providers like Anthropic, OpenAI, and Google now encrypt these traces and return them to clients as encrypted blocks. The paper reveals that these encrypted blocks are not properly isolated, as they can be replayed across sessions, users, and models, and weaker models can be jailbroken to decode them.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://arxiv.org/abs/2608.09867">[2608.09867] Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://www.explainx.ai/blog/stealing-reasoning-traces-encrypted-cot-vulnerability-august-2026">Stealing Reasoning Traces: The Encrypted Chain-of-Thought ...</a></li>

</ul>
</details>

**Discussion**: The discussion on Hacker News and other forums highlights the severity of the vulnerability, with many expressing concern about the implications for AI safety and the trustworthiness of proprietary APIs. Some commenters note that the fix may not be complete and that similar attacks could emerge in the future, while others debate the ethics of extracting hidden reasoning.

**Tags**: `#LLM`, `#security`, `#chain-of-thought`, `#API`, `#privacy`

---

<a id="item-3"></a>
## [vLLM v0.27.0 Adds Kimi K3, PyTorch 2.13, and Deep FlashAttention 4](https://github.com/vllm-project/vllm/releases/tag/v0.27.0) ⭐️ 8.0/10

vLLM v0.27.0 is a major release with 561 commits from 242 contributors, adding full support for the Kimi K3 model, new models like Qwen3.5 and K-EXAONE-2.0-750B-A37B, and upgrading to PyTorch 2.13.0 with deeper FlashAttention 4 integration on SM100. This release significantly expands vLLM's model coverage and performance, especially for cutting-edge architectures like Kimi K3, making it a key update for the AI inference community. The PyTorch 2.13 upgrade and FlashAttention 4 enhancements promise better efficiency and lower latency for large-scale deployments. Notable technical details include the full-stack Kimi K3 support with AttnRes kernels and DeepGEMM, a breaking PyTorch 2.13.0 environment change, and FlashAttention 4 FP8 KV cache and headdim-256 support on SM100. The release also introduces a simplified fault tolerance framework for large-scale serving and early enablement for NVIDIA Rubin (sm_107) and ROCm gfx1250.

github · khluu · Aug 10, 21:18

**Background**: vLLM is a high-throughput, memory-efficient inference and serving engine for LLMs, widely used in production. Kimi K3 is a large language model from Moonshot AI featuring innovations like Kimi Delta Attention and Attention Residuals, which improve long-context handling. FlashAttention is a series of optimized attention algorithms that reduce memory and speed up training and inference. PyTorch is a popular deep learning framework, and upgrading to 2.13 brings performance and compatibility improvements.

<details><summary>References</summary>
<ul>
<li><a href="https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html">Kimi K3 Architecture Notes | Sebastian Raschka, PhD</a></li>
<li><a href="https://huggingface.co/blog/ResterChed/kimi-k3-model-overview-mxfp4-quantization-open-wei">Kimi K3 Model Overview: 2.8T Parameters, MXFP4 Quantization, and What the Open Weights Mean for the Community</a></li>
<li><a href="https://github.com/deepseek-ai/DeepGEMM">GitHub - deepseek-ai/DeepGEMM: DeepGEMM: clean and efficient ...</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#PyTorch`, `#FlashAttention`, `#AI/ML`

---

<a id="item-4"></a>
## [DeepSeek V4 Pro 0813: Competitive Performance at Lower Cost](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 8.0/10

DeepSeek has released DeepSeek V4 Pro 0813, a new version of its V4 Pro model, now available on OpenRouter. It offers a 1,048,576-token context window and is priced at $0.435 per million input tokens and $0.87 per million output tokens. This release is significant because it delivers performance competitive with top models like Opus 4.8 while being about 20x cheaper, making advanced AI more accessible. It could influence pricing and adoption trends in the LLM market, especially for cost-sensitive developers and enterprises. DeepSeek V4 Pro 0813 is a large-scale mixture-of-experts model with 1.6T total parameters and 49B activated parameters, supporting a 1M-token context window and maximum output of 384,000 tokens. Community benchmarks show it scores 42.7/60.0 on HLE without/with tools, and it is positioned between DeepSeek V4 Flash and stronger models like Sol or Fable.

hackernews · explosion-s · Aug 12, 16:04 · [Discussion](https://news.ycombinator.com/item?id=49274600)

**Background**: DeepSeek is a Chinese AI company known for releasing cost-efficient large language models. The V4 Pro series uses a mixture-of-experts architecture, which activates only a subset of parameters per token, enabling high performance with lower computational cost. OpenRouter is a platform that provides unified API access to various AI models, allowing users to compare and use them easily.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V 4 Pro 0813 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://lmmarketcap.com/model/deepseek-v4-pro-0813">DeepSeek V 4 Pro - Pricing & Benchmarks 2026 | LM Market Cap</a></li>
<li><a href="https://aihubmix.com/model/deepseek-v4-pro-0813">deepseek - v 4 - pro - 0813 - API Pricing & Performance | AIHubMix</a></li>

</ul>
</details>

**Discussion**: Community feedback is mixed: some users report that DeepSeek V4 Pro 0813 has issues with complex tasks compared to alternatives like GPT-5.6-terra-high or Grok 4.6, while others praise its cost-efficiency and capability for heavy development. One user noted it is competitive with Opus 4.8 but weaker than Sol or Fable, and about 20x cheaper.

**Tags**: `#AI`, `#LLM`, `#DeepSeek`, `#benchmarks`, `#cost-efficiency`

---

<a id="item-5"></a>
## [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

Tailscale published a detailed blog post explaining how they traced a database corruption issue to a 16-year-old SQLite WAL-reset bug, and funded an open-source VFS shim to help isolate the race condition. The bug occurs when two or more connections to the same WAL-mode database attempt to write or run a checkpoint simultaneously, potentially corrupting the database file. This is significant because it highlights the value of supporting open-source projects like SQLite, and demonstrates how a company can fund specific debugging tools to solve subtle, long-standing bugs. It also raises awareness about the importance of using supported SQLite versions and the potential risks of concurrent access in WAL mode. The bug is documented on SQLite's 'How To Corrupt An SQLite Database File' page, and it affects SQLite versions in a certain range; for example, SQLite 3.50.4 is affected while 3.51.3 is clean. Tailscale patched their SQLite driver to log a warning when write transactions and WAL-reset operations overlap, and they funded the development of a VFS shim that helps detect such races.

hackernews · ropbear · Aug 12, 14:22 · [Discussion](https://news.ycombinator.com/item?id=49272832)

**Background**: SQLite is a widely used embedded database that supports Write-Ahead Logging (WAL) mode for improved concurrency. The WAL-reset bug is a race condition that can occur when multiple connections to the same database attempt to write or checkpoint simultaneously, leading to database corruption. Tailscale uses SQLite for its control plane, and despite following the recommended single-writer design, they encountered this subtle bug. The VFS (Virtual File System) layer in SQLite allows custom implementations to intercept file operations, which is how the shim was able to help isolate the issue.

<details><summary>References</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL-Reset bug</a></li>
<li><a href="https://www.sqlite.org/howtocorrupt.html">How To Corrupt An SQLite Database File</a></li>
<li><a href="https://sqlite.org/cksumvfs.html">The Checksum VFS Shim - SQLite</a></li>

</ul>
</details>

**Discussion**: The community praised the write-up and Tailscale's decision to fund open-source development, with comments highlighting the value of supporting SQLite and the interesting debugging process. Some users expressed curiosity about the specific checkpointing frequency that led to the bug, while others appreciated the technical depth and the company's transparency.

**Tags**: `#SQLite`, `#database`, `#bug`, `#Tailscale`, `#open-source`

---

<a id="item-6"></a>
## [AI Is Removing the Middle Class of Software Engineering](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html) ⭐️ 8.0/10

A blog post argues that AI is eliminating the middle class of software engineers by automating routine coding tasks, while amplifying the impact of both highly skilled and unskilled engineers. The post emphasizes the need for engineers to retain critical thinking and deep learning. This matters because it highlights a significant shift in the software engineering job market, potentially affecting career trajectories and hiring practices. It underscores the growing importance of critical thinking and adaptability in an AI-augmented industry. The article notes that 'bad' engineers can now amplify their poor practices tenfold across an organization with AI, and that the traditional handoff from senior engineers to junior coders is no longer necessary. It also warns against outsourcing critical thinking to LLMs.

hackernews · florianherrengt · Aug 12, 13:20 · [Discussion](https://news.ycombinator.com/item?id=49271994)

**Background**: Software engineering has traditionally involved a hierarchy where senior engineers design solutions and junior engineers implement them. With the rise of AI coding assistants like GitHub Copilot and OpenAI Codex, routine coding tasks are increasingly automated, potentially compressing the middle tier of the profession. Research suggests that while LLMs can generate code, they are not yet capable of maintaining large software systems reliably, indicating that human oversight remains crucial.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2502.20429v2">Impact of AI on Software Engineering Jobs</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2772485925000171">LLMs: A game-changer for software engineers? - ScienceDirect</a></li>
<li><a href="https://arxiv.org/html/2511.06428v1">Walking the Tightrope of LLMs for Software Development: A Practitioners’ Perspective</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree with the article, noting that AI amplifies both good and bad engineering practices. Some emphasize the importance of never outsourcing critical thinking to LLMs, while others compare the change to automating the 'StackOverflow engineer' role, where seniors no longer need to hand off coding tasks to juniors.

**Tags**: `#AI`, `#software engineering`, `#future of work`, `#LLM`, `#career impact`

---

<a id="item-7"></a>
## [Mathematician Analyzes LLM Strengths in Finding Counterexamples](https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/) ⭐️ 8.0/10

Timothy Gowers, a prominent mathematician, published a blog post analyzing the types of mathematics LLMs excel at, suggesting they are better at finding counterexamples than creating elegant proofs. The post has sparked a high-quality discussion with 102 comments. This analysis provides valuable insights into the current capabilities and limitations of LLMs in mathematics, which is crucial for guiding future AI research and applications in mathematical discovery. It also highlights the potential of AI in counterexample search, a task that could significantly aid mathematical research. Gowers suggests that LLMs may be more adept at finding counterexamples than constructing elegant proofs, and he discusses the implications for AI-driven mathematics. The discussion also touches on test-time scaling, with comments noting that sampling-based approaches like AlphaCode have shown success in generating many candidates and filtering them.

hackernews · ColinWright · Aug 12, 10:04 · [Discussion](https://news.ycombinator.com/item?id=49270022)

**Background**: Large language models (LLMs) are AI systems trained on vast text data, capable of generating human-like text. In mathematics, they have been used for proof construction and counterexample generation, with recent research focusing on test-time scaling, which involves using more computation during inference to improve outputs. This post by Gowers, a Fields Medalist, adds a mathematician's perspective to the ongoing discussion about AI's role in mathematics.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.04001">Test-Time Scaling in Reasoning LLMs: Inference Regimes ...</a></li>
<li><a href="https://arxiv.org/abs/2408.03314">[2408.03314] Scaling LLM Test-Time Compute Optimally can be ... GitHub - testtimescaling/testtimescaling.github.io: "what ... What, How, Where, and How Well? A Survey on Test-Time Scaling ... Scaling Test-Time Compute for Longer Thinking in LLMs ... Scaling LLM Test-Time Compute Optimally Can be More Effective ... Scaling LLM Test-Time Compute Optimally Can be More Effective ...</a></li>
<li><a href="https://arxiv.org/html/2603.19514v1">Learning to Disprove: Formal Counterexample Generation with Large Language Models</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights that the post is essentially about test-time scaling, with one commenter noting that sampling-based methods like AlphaCode have shown early success. Another commenter agrees with Gowers' criterion for human-level AI in mathematics, emphasizing the need for new and surprising proof methods. A third commenter wonders about AI's performance in temporal logic, given difficulties with concurrent code.

**Tags**: `#LLMs`, `#mathematics`, `#AI research`, `#test-time scaling`, `#proof`

---

<a id="item-8"></a>
## [Woxi: Open-Source Rust Reimplementation of Wolfram Language](https://woxi.ad-si.com/) ⭐️ 8.0/10

Woxi is an open-source interpreter for the Wolfram Language written in Rust, offering a Mathematica-like GUI (Woxi Studio), CLI, Jupyter kernel, Python package, npm package, and WASM module. It boasts millisecond-level startup times, making it practical for shell scripts and one-liners. This project provides a free and open-source alternative to the proprietary Wolfram Language, potentially lowering barriers for students, researchers, and developers. Its embeddability and fast startup could expand the language's use in scripting and web applications, challenging the dominance of commercial tools like Mathematica and Sage. Woxi ensures conformance with approximately 26,000 unit tests and 900 .wls script snapshot tests. The project currently focuses on fixing edge cases, improving performance, and growing the community; it is available on GitHub for contributions and bug reports.

hackernews · adius · Aug 12, 10:06 · [Discussion](https://news.ycombinator.com/item?id=49270040)

**Background**: The Wolfram Language is a proprietary, high-level multi-paradigm programming language developed by Wolfram Research, known for symbolic computation and rule-based programming. It is the language behind Mathematica, a widely used computational tool. WebAssembly (WASM) is an open standard for portable binary code that enables high-performance applications on web pages and other platforms, allowing Woxi to run in browsers. Jupyter kernels are language-specific processes that enable interactive execution within Jupyter environments, facilitating data analysis and scientific computing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wolfram_Language">Wolfram Language</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly - Wikipedia</a></li>
<li><a href="https://docs.jupyter.org/en/stable/projects/kernels.html">Kernels (Programming Languages) — Jupyter Documentation 4.1.1 alpha documentation</a></li>

</ul>
</details>

**Discussion**: Commenters expressed support for the project, with some hoping it could replace Sage as a well-integrated open-source CAS. One user tested Woxi Studio with multivariable calculus visualizations and found it able to display them, though unsure of full correctness. Another noted the project was posted six months ago, and a newcomer found Woxi capable of solving algebra problems that Sympy and others couldn't, sparking interest in the Wolfram Language.

**Tags**: `#Wolfram Language`, `#Rust`, `#Open Source`, `#Interpreter`, `#Scientific Computing`

---

<a id="item-9"></a>
## [Meta Releases Muse Glimmer, a 30B Open-Weights Agentic Model](https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/#atom-everything) ⭐️ 8.0/10

Meta has introduced Muse Glimmer, a 30-billion-parameter open-weights multimodal model released under the Apache 2.0 license, optimized for agentic task completion, reliable tool use, and multi-step reasoning. The model is available for local deployment, with an 18.16 GB version on LM Studio and support for vision tasks. This release is significant because it offers a capable open-weights model with a permissive license, enabling developers to run advanced agentic workflows locally without restrictive licensing. It could accelerate innovation in local AI applications, tool integration, and autonomous task automation, benefiting the broader AI ecosystem. Muse Glimmer is a 30B parameter model distilled from Muse Spark, supporting text and image inputs, and is served on vLLM with native Onyx tool-calling and reasoning parsers. It performs well on benchmarks like DeepSearch QA, MCP-Atlas, τ-Bench, and SWE-Bench, and can run on consumer hardware with 32 GB RAM or more.

rss · Simon Willison · Aug 10, 23:56

**Background**: Agentic AI refers to systems that can autonomously reason, plan, and execute complex tasks, often using tools and multi-step workflows. Open-weights models allow developers to run AI locally, ensuring data privacy and customization. Apache 2.0 is a permissive license that permits commercial use and modification, unlike some previous Meta licenses.

<details><summary>References</summary>
<ul>
<li><a href="https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model">Introducing Muse Glimmer: An Open Agentic Model That Runs on ...</a></li>
<li><a href="https://dev.meta.ai/docs/muse-glimmer">Model API | Muse Glimmer</a></li>
<li><a href="https://build.nvidia.com/meta/muse-glimmer-30b/modelcard">muse-glimmer-30b Model by Meta | NVIDIA NIM</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Meta`, `#open-weights`, `#agentic`, `#model release`

---

<a id="item-10"></a>
## [AI Pioneers Debate Openness vs. Safety at Ai4](https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/) ⭐️ 8.0/10

At the Ai4 2026 conference in Las Vegas, Geoffrey Hinton, Fei-Fei Li, and Andrew Ng publicly debated AI regulation, open-source access, and US competitiveness amid rising safety concerns. Hinton warned against open-sourcing model weights, Ng advocated for openness to drive innovation, and Li proposed a risk-based approach to transparency. This debate highlights a critical rift among AI pioneers that could shape future policy and industry practices. Their differing stances on openness and regulation will influence how governments and companies balance innovation with safety, affecting the global AI race. Hinton distinguished between conventional open-source software and open-weight AI models, cautioning that publicizing weights could enable misuse. Li argued that AI changes tasks rather than entire jobs, and suggested transparency should depend on the application and associated risks. The conference featured over 12,000 participants and 1,000 speakers from 20 industries.

rss · TechCrunch AI · Aug 12, 17:51

**Background**: The Ai4 conference is a major annual gathering for AI leaders in business and policy. Geoffrey Hinton is a Turing Award winner often called the 'godfather of AI,' Fei-Fei Li is a renowned computer vision researcher, and Andrew Ng is a prominent AI educator and entrepreneur. Their debate reflects broader societal tensions over AI safety, open-source principles, and national competitiveness.

<details><summary>References</summary>
<ul>
<li><a href="https://iblnews.org/story/the-ai4-2026-conference-showed-the-divergence-shaping-the-public-debate-today">The AI4 2026 Conference Showed the Divergence Shaping the ...</a></li>
<li><a href="https://dedirock.com/blog/debate-over-ai-risks-and-regulation-hinton-fei-fei-li-and-andrew-ng-face-off-at-ai4/">Debate Over AI Risks and Regulation : Hinton , Fei - Fei Li ... - DediRock</a></li>
<li><a href="https://www.forbes.com/sites/ronschmelzer/2026/08/06/hinton-li-ng-ai-jobs-regulation/">Three AI Pioneers Clash Over Jobs, Regulation And The Future Of AI</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#open-source`, `#regulation`, `#AI policy`, `#Geoffrey Hinton`

---

<a id="item-11"></a>
## [General Catalyst leads $1.1B round into 2-month-old River AI](https://techcrunch.com/2026/08/11/general-catalyst-leads-1-1b-round-into-2-month-old-river-ai/) ⭐️ 8.0/10

River AI, a startup co-founded by xAI co-founder Igor Babuschkin, has raised $1.1 billion in a funding round led by General Catalyst, just two months after its founding. This is one of the largest early-stage rounds ever for an AI startup. This massive investment signals strong industry confidence in personal AI agents, a rapidly growing sector. The involvement of a prominent investor like General Catalyst and a key figure from xAI could accelerate the development and adoption of personal AI agents, potentially reshaping how individuals interact with AI. The round was led by General Catalyst, with no other investors disclosed. River AI is focused on developing personal agents, a concept that aims to create AI systems capable of performing tasks on behalf of users. The company is only two months old, making this a record early-stage round.

rss · TechCrunch AI · Aug 11, 17:41

**Background**: Igor Babuschkin co-founded xAI with Elon Musk in 2023 and left the company in August 2025 to launch his own venture. Personal AI agents are AI systems designed to assist individuals with tasks such as scheduling, communication, and information management, often leveraging large language models. The AI industry has seen a surge in funding for agent-based startups, reflecting a broader trend toward more autonomous AI applications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2025/08/13/elon-musks-xai-loses-co-founder-igor-babuschkin-for-venture-firm.html">Elon Musk's xAI loses co-founder Igor Babuschkin, who's ...</a></li>
<li><a href="https://techcrunch.com/2025/08/13/co-founder-of-elon-musks-xai-departs-the-company/">Co-founder of Elon Musk’s xAI departs the company - TechCrunch</a></li>
<li><a href="https://www.businessinsider.com/xai-cofounder-leaving-learned-2-things-from-elon-musk-babuschkin-2025-8">XAI Cofounder Leaving the Company, Says He Learned 2 Things ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#funding`, `#startups`, `#personal agents`

---

<a id="item-12"></a>
## [Anthropic's Unreleased Model Advances on Riemann Hypothesis](https://techcrunch.com/2026/08/11/an-unreleased-anthropic-model-made-progress-on-one-of-maths-biggest-unsolved-problems/) ⭐️ 8.0/10

Anthropic's unreleased AI model reportedly made notable progress on the Riemann hypothesis, a major unsolved problem in mathematics for over 150 years. The model did not solve the problem but achieved more progress than expected. This development highlights the growing capability of AI models to tackle complex mathematical problems, potentially accelerating research in pure mathematics. It also underscores the competitive edge of Anthropic's models in advanced reasoning tasks. The specific model name and the exact nature of the progress have not been disclosed. The Riemann hypothesis concerns the distribution of zeros of the Riemann zeta function, and a proof would have profound implications for number theory and related fields.

rss · TechCrunch AI · Aug 11, 16:25

**Background**: The Riemann hypothesis, first proposed by Bernhard Riemann in 1859, states that all nontrivial zeros of the Riemann zeta function have real part 1/2. It is one of the Clay Mathematics Institute's Millennium Prize Problems, and its resolution would have major consequences for the distribution of prime numbers. AI models like Anthropic's Claude are increasingly being used for mathematical reasoning, though they typically assist rather than fully solve such problems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://mathworld.wolfram.com/RiemannHypothesis.html">Riemann Hypothesis -- from Wolfram MathWorld</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-4-5">Introducing Claude Opus 4.5 \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#mathematics`, `#Anthropic`, `#research`, `#Riemann hypothesis`

---

<a id="item-13"></a>
## [Adam's Coordinate Scaling Breaks Rotation Invariance and Low-Rank Bias](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 8.0/10

A new study demonstrates that Adam's per-coordinate second moment breaks rotation invariance in factored models W=UV^T, causing it to lose the implicit low-rank bias that gradient descent (GD) exhibits. Experiments across nine update rules on matrix sensing show that rotation-invariant optimizers like GD, Muon, and Shampoo preserve the bias, while Adam, RMSProp, Lion, signum, and Adafactor lose it. This finding pinpoints a key mechanism—anisotropy in per-coordinate scaling—that determines whether optimizers retain implicit low-rank bias, which is crucial for low-rank matrix recovery and deep learning. It suggests that practitioners should consider rotation-invariant optimizers like Muon for tasks where low-rank structure is important, and it may guide the design of new optimizers. The study used a one-parameter family that interpolates Adam's denominator from per-coordinate to a single shared scalar, showing recovery improves monotonically along this path, isolating the damage to anisotropy rather than adaptivity in general. Muon showed exact recovery on truly low-rank targets but degraded fastest with added spectral tail, crossing over with GD near 4% tail energy; the author also found that switching from per-coordinate clipping to global norm clipping in their own optimizer reduced recovery error from 0.347 to 0.220.

reddit · r/MachineLearning · /u/EtherealGlyph · Aug 12, 16:39

**Background**: In factored models like W=UV^T, the loss is invariant to orthogonal rotations of the factors, and gradient descent respects this symmetry. Adam's per-coordinate second moment estimate breaks this invariance because it depends on the basis in which the factors are expressed. Implicit bias refers to the tendency of optimization algorithms to converge to solutions with certain properties (e.g., low rank) even without explicit regularization. Rotation-invariant optimizers like Muon, which uses Newton-Schulz orthogonalization, preserve this symmetry and thus retain the low-rank bias.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/rotational-adam-optimizer">Rotational Adam Optimizer</a></li>
<li><a href="https://kellerjordan.github.io/posts/muon/">Muon: An optimizer for hidden layers in neural networks | Keller Jordan blog</a></li>
<li><a href="https://arxiv.org/html/2604.01472v1">The Newton–Muon Optimizer</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely includes technical debate about the findings, with some users questioning whether Adam was tuned fairly, as the author anticipates objections like 'you should have just tuned Adam harder.' Others may discuss the implications for optimizer design and the surprising behavior of Muon, which shows both spectral simplicity bias and spurious feature fitting depending on the setting.

**Tags**: `#optimization`, `#low-rank`, `#implicit bias`, `#Adam`, `#matrix sensing`

---

<a id="item-14"></a>
## [Decoupled Descent: Exact Train-Test Error Tracking via AMP Corrections](https://www.reddit.com/r/MachineLearning/comments/1vlu1se/decoupled_descent_enforcing_exact_traintest_error/) ⭐️ 8.0/10

The paper introduces Decoupled Descent (DD), a novel training method that uses approximate message passing (AMP) Onsager corrections to guarantee that the training error asymptotically equals the test error at each parameter iterate, addressing data reuse bias in full-batch gradient descent. This work provides a theoretical framework to mitigate the train-test gap, a fundamental issue in neural network training, potentially enabling better generalization and principled early stopping or hyperparameter tuning. It bridges high-dimensional statistics and practical optimization, offering a new direction for training algorithms. The method is validated on stylized Gaussian mixture models and a high-dimensional XOR model with a two-layer network, showing improved train-test tracking over standard gradient descent. The paper is a preprint and not yet widely validated; the author plans to release a PyTorch-compatible package.

reddit · r/MachineLearning · /u/mlovik1 · Aug 11, 21:06

**Background**: Approximate Message Passing (AMP) is an iterative algorithm for signal recovery that uses Onsager corrections to track the evolution of errors, enabling exact asymptotic analysis. In gradient descent, reusing the same data across iterations introduces bias, causing training error to diverge from test error. Decoupled Descent applies AMP corrections to decouple the data reuse effect, ensuring train and test errors align.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/approximate-message-passing-amp-algorithms">Approximate Message Passing Algorithms</a></li>
<li><a href="https://arxiv.org/abs/2201.07487">[2201.07487] A Concise Tutorial on Approximate Message Passing</a></li>
<li><a href="https://arxiv.org/pdf/2604.27883">Decoupled Descent: Exact Test Error Tracking Via Approximate...</a></li>

</ul>
</details>

**Discussion**: The author actively invites discussion and feedback, indicating openness to community input. The post has a high score (8/10), suggesting positive reception, though no specific comments are provided in the content.

**Tags**: `#machine learning`, `#generalization`, `#approximate message passing`, `#optimization`, `#theory`

---

<a id="item-15"></a>
## [LTX Releases Open-Source Video Model LTX-2.5, Runs on Single RTX 5090](https://ltx.io/model/ltx-2-5) ⭐️ 8.0/10

LTX has released LTX-2.5, an open-source video generation foundation model with fully open weights, training code, and inference pipeline. It can run locally on a single RTX 5090 GPU and is free for commercial use by companies with annual revenue under $10 million. This release democratizes high-quality video generation by enabling local, private, and customizable deployment on consumer-grade hardware. It could accelerate innovation in AI video production and challenge proprietary models, as open weights allow fine-tuning and integration into diverse workflows. LTX-2.5 supports text-to-video and image-to-video generation, with improved multi-shot coherence and prompt adherence. It introduces a new diffusion video decoder and uses the Gemma 4 12B text encoder; in a 98-prompt text-to-video artifact evaluation, LTX 2.5 Pro ranked first among ten models.

telegram · zaihuapd · Aug 12, 02:15

**Background**: Video generation models typically require massive cloud resources, but recent advances in diffusion transformers and efficient decoders have enabled local inference on high-end GPUs like the RTX 5090, which features 32GB VRAM. Open-source models like LTX-2.5 allow developers to run, fine-tune, and deploy video AI without relying on external APIs, fostering privacy and customization.

<details><summary>References</summary>
<ul>
<li><a href="https://ltx.io/model/ltx-2-5">LTX-2.5: LTX's Latest AI Open-Source Foundation Model | LTX</a></li>
<li><a href="https://ltx.io/model/open-source">LTX-2.5 Model Open Source: AI Video Generator</a></li>
<li><a href="https://comfy.org/ltx-2.5">LTX 2.5 on Comfy — Open-Source AI Video Model</a></li>

</ul>
</details>

**Tags**: `#video generation`, `#open source`, `#AI model`, `#LTX`, `#diffusion`

---

<a id="item-16"></a>
## [Former Chinese Premier Zhu Rongji Dies at 98](https://www.news.cn/politics/20260812/4c2c72e299ef4561915d2e507393a81f/c.html) ⭐️ 8.0/10

Zhu Rongji, former Premier of China's State Council, passed away in Beijing on August 12, 2026, at the age of 98. The official announcement was made by the CPC Central Committee, the NPC Standing Committee, the State Council, and the CPPCC National Committee. Zhu Rongji was a key figure in China's economic reforms and its accession to the WTO, and his passing marks the end of an era in Chinese political history. His policies during the Asian financial crisis and his role in shaping the socialist market economy continue to influence China's economic trajectory. Zhu Rongji was born in October 1928 in Changsha, Hunan, and joined the CPC in October 1949. He served as Premier from March 1998, during which he implemented proactive fiscal and prudent monetary policies, maintained the stability of the RMB, and led negotiations for China's WTO accession.

telegram · zaihuapd · Aug 12, 10:11

**Background**: Zhu Rongji was a prominent Chinese leader known for his role in economic reforms during the 1990s. He is credited with major reforms in fiscal, financial, state-owned enterprise, housing, and grain circulation sectors, which helped establish the basic framework of the socialist market economy. His tenure as Premier coincided with the Asian financial crisis and China's WTO accession in 2001.

**Tags**: `#politics`, `#obituary`, `#China`, `#history`

---

<a id="item-17"></a>
## [DeepSeek Launches V4-Flash API Public Beta with Strong Agent Benchmarks](https://t.me/zaihuapd/43149) ⭐️ 8.0/10

On July 31, 2026, DeepSeek launched the public beta of the V4-Flash API, featuring significantly enhanced agent capabilities and benchmark scores that surpass V4-Pro-Preview. The model achieves 82.7 on Terminal Bench 2.1, 76.7 on Cybergym, 68.7 on DSBench-FullStack, and 59.6 on DSBench-Hard. This release signals DeepSeek's continued push into agentic AI, with strong performance on benchmarks that measure real-world task completion in software engineering, cybersecurity, and data science. It could intensify competition among AI model providers and offer developers a more capable and efficient option for building autonomous agents. The V4-Flash API natively supports the Responses API format and is specifically adapted for Codex. The model's architecture and size details are not fully disclosed in the announcement, but the benchmark improvements suggest significant optimizations for agentic workflows.

telegram · zaihuapd · Aug 12, 15:30

**Background**: Terminal Bench 2.1 is a benchmark for evaluating AI agents' ability to complete complex tasks in container environments, such as debugging code and resolving security vulnerabilities. Cybergym assesses AI agents on real-world cybersecurity vulnerability analysis, while DSBench evaluates data science agents on realistic data analysis and modeling tasks. These benchmarks are designed to measure agent capability beyond simple language understanding, focusing on practical task execution.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tbench.ai/news/terminal-bench-2-1">Terminal-Bench 2.1</a></li>
<li><a href="https://www.cybergym.io/cybergym/">CyberGym: Evaluating AI Agents' Real-World Cybersecurity ...</a></li>
<li><a href="https://github.com/LiqiangJing/DSBench">GitHub - LiqiangJing/DSBench: [ICLR 2025] DSBench: How Far ...</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#API`, `#AI`, `#benchmark`, `#agent`

---