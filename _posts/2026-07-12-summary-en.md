---
layout: default
title: "Horizon Summary: 2026-07-12 (EN)"
date: 2026-07-12
lang: en
---

> From 31 items, 11 important content pieces were selected

---

1. [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](#item-1) ⭐️ 9.0/10
2. [OpenAI Releases GPT-5.6 Series with Sol, Terra, Luna Tiers](#item-2) ⭐️ 9.0/10
3. [GPT-5.6 Sol Ultra Proves 50-Year-Old Graph Conjecture in Under 1 Hour](#item-3) ⭐️ 9.0/10
4. [xAI Grok CLI Uploads Entire Codebase and Secrets by Default](#item-4) ⭐️ 9.0/10
5. [Mesh LLM: Distributed AI Inference via iroh P2P](#item-5) ⭐️ 8.0/10
6. [RISCBoy: Open-Source RISC-V Portable Game Console](#item-6) ⭐️ 8.0/10
7. [UPI Architecture and Transaction Flow Explained](#item-7) ⭐️ 8.0/10
8. [Zer0Fit MCP Server Wraps Google's TabFM & TimesFM for Zero-Shot ML](#item-8) ⭐️ 8.0/10
9. [VultronRetriever Models Top MTEB Leaderboard](#item-9) ⭐️ 8.0/10
10. [Shanghai Aims for High-Quality Brain Control by 2027](#item-10) ⭐️ 8.0/10
11. [Apple Sues OpenAI for Trade Secret Theft](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 9.0/10

vLLM v0.25.0 makes Model Runner V2 the default execution path for all dense models and removes the legacy PagedAttention implementation. The release includes 558 commits from 232 contributors, new model support (e.g., LLaVA-OneVision-2, GLM-5), and a new Streaming Parser Engine. This release marks a major architectural shift in vLLM, improving performance and modularity by standardizing on Model Runner V2. The removal of PagedAttention simplifies the codebase, while new models and features expand vLLM's applicability in production LLM serving. Model Runner V2 now supports EVS, realtime embeddings, prefix caching for Mamba hybrid models, and dynamic speculative decoding with full CUDA graphs. The Transformers modeling backend is now as fast as native vLLM, and new models include Unlimited OCR, MOSS-Transcribe-Diarize, and Hy3.

github · khluu · Jul 11, 20:06

**Background**: vLLM is an open-source high-throughput LLM inference engine. Model Runner V2 is a redesigned execution core that improves modularity and performance over the original V1. PagedAttention was vLLM's original attention mechanism that managed KV cache efficiently using paging, but has been superseded by newer backends.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#open source`, `#release`, `#AI/ML`

---

<a id="item-2"></a>
## [OpenAI Releases GPT-5.6 Series with Sol, Terra, Luna Tiers](https://t.me/zaihuapd/42497) ⭐️ 9.0/10

OpenAI has officially released the GPT-5.6 series, featuring three tiers: Sol (flagship), Terra (balanced), and Luna (cost-efficient). The series introduces max/ultra reasoning, multi-agent collaboration, and Programmatic Tool Calling, with significant improvements in code, knowledge work, design, research, and cybersecurity. This release marks a major evolution in OpenAI's model lineup, offering tiered pricing and capabilities that allow users to match model cost to task complexity. The new reasoning and multi-agent features enable more efficient handling of complex, multi-step tasks, potentially reducing token usage and cost. GPT-5.6 Sol is the most powerful and expensive tier, Terra offers a balance of performance and cost, and Luna is optimized for high-concurrency, low-cost scenarios. The max reasoning effort allocates more reasoning work to a single model invocation, while ultra mode uses sub-agents to parallelize tasks. Programmatic Tool Calling allows models to orchestrate tools via code rather than individual API round-trips.

telegram · zaihuapd · Jul 11, 13:34

**Background**: OpenAI's GPT series has evolved through multiple versions, with GPT-5.4 retiring on July 23 and GPT-5.5 remaining available. The new GPT-5.6 series introduces a tiered naming system where the number indicates the generation, while Sol, Terra, and Luna are durable tiers that advance independently. This structure allows users to choose the appropriate level of capability and cost for their specific use case.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vellum.ai/blog/gpt-5-6-benchmarks-explained">GPT - 5 . 6 Sol vs Terra vs Luna : Which Tier Should You Actually Use?</a></li>
<li><a href="https://felloai.com/gpt-5-6/">GPT - 5 . 6 Sol , Terra , Luna : What OpenAI Just Shipped</a></li>
<li><a href="https://apidog.com/blog/gpt-5-6-sol-vs-terra-vs-luna/">GPT - 5 . 6 Sol vs Terra vs Luna : which model should you use?</a></li>

</ul>
</details>

**Discussion**: Early community reactions on Reddit highlight that GPT-5.6 Sol with Codex and Ultra Mode is considered 'insane' for complex tasks, with users noting that Max Reasoning paired with focused context yields the best results. Some discussions caution that Ultra Mode changes Sol from a single model into a coordinator, which may require careful task decomposition.

**Tags**: `#OpenAI`, `#GPT-5.6`, `#AI`, `#LLM`, `#announcement`

---

<a id="item-3"></a>
## [GPT-5.6 Sol Ultra Proves 50-Year-Old Graph Conjecture in Under 1 Hour](https://www.qbitai.com/2026/07/447873.html) ⭐️ 9.0/10

OpenAI's GPT-5.6 Sol Ultra model autonomously proved the cycle double cover conjecture, a 50-year-old open problem in graph theory, in less than one hour. The model generated a 3-page PDF proof using 64 parallel sub-agents and a carefully designed prompt. This achievement demonstrates that large language models can now tackle long-standing mathematical conjectures autonomously, potentially accelerating research in mathematics and theoretical computer science. It also showcases the power of multi-agent collaboration and rigorous prompt engineering for complex reasoning tasks. The proof transformed the conjecture into a finite field edge labeling problem with linear equations, assigning two labels per edge so that edges with the same label form cycles. The prompt specified verification criteria, definitions, boundary conditions, and failure cases, but did not prescribe fixed solution steps.

telegram · zaihuapd · Jul 12, 03:49

**Background**: The cycle double cover conjecture, posed independently by Szekeres (1973) and Seymour (1979), asks whether every bridgeless graph has a collection of cycles that together cover each edge exactly twice. It is a fundamental open problem in graph theory, related to graph embeddings and the circular embedding conjecture. Multi-agent LLM systems use multiple specialized agents working in parallel, often with an orchestrator, to tackle complex tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cycle_double_cover_conjecture">Cycle double cover conjecture</a></li>
<li><a href="https://mathworld.wolfram.com/CycleDoubleCoverConjecture.html">Cycle Double Cover Conjecture -- from Wolfram MathWorld</a></li>
<li><a href="https://www.superannotate.com/blog/multi-agent-llms">Multi - agent LLMs in 2026 [+frameworks] | SuperAnnotate</a></li>

</ul>
</details>

**Tags**: `#AI`, `#graph theory`, `#LLM`, `#mathematical proof`, `#multi-agent`

---

<a id="item-4"></a>
## [xAI Grok CLI Uploads Entire Codebase and Secrets by Default](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) ⭐️ 9.0/10

Security researchers discovered that xAI's Grok Build CLI tool (version 0.2.93) automatically uploads entire code repositories and sensitive files like .env to xAI servers, even when explicitly instructed not to, and the privacy toggle is ineffective. This poses a severe security and privacy risk for developers and organizations using xAI tools, as it can lead to unintentional data exfiltration of proprietary code and credentials. The finding undermines trust in xAI's privacy controls and highlights the need for stricter data handling in AI-assisted development tools. The tool uploads code via two channels: file contents are embedded in model requests and also packaged to Google Cloud Storage, while the entire repository is uploaded as a git bundle. In tests, a file explicitly instructed not to be opened was still recoverable from the uploaded bundle, and disabling the 'improve model' toggle did not stop the upload.

telegram · zaihuapd · Jul 12, 04:19

**Background**: Grok Build is a command-line tool by xAI that allows developers to interact with Grok AI models directly from the terminal. Git bundle is a file format that packages an entire Git repository into a single file for offline transfer. The tool's privacy settings include a toggle to opt out of model improvement, but researchers found it ineffective.

<details><summary>References</summary>
<ul>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>
<li><a href="https://git-scm.com/docs/git-bundle">Git - git - bundle Documentation</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely includes technical analysis and debate about the severity of the issue, with some users expressing concern over data exfiltration and others questioning the tool's design. No specific comments were provided in the input.

**Tags**: `#security`, `#privacy`, `#AI tools`, `#data exfiltration`, `#xAI`

---

<a id="item-5"></a>
## [Mesh LLM: Distributed AI Inference via iroh P2P](https://www.iroh.computer/blog/mesh-llm) ⭐️ 8.0/10

Mesh LLM is a new open-source project that enables distributed LLM inference across heterogeneous devices using iroh's peer-to-peer networking, automatically splitting models across multiple nodes. This approach democratizes access to large language models by pooling consumer-grade hardware, potentially reducing reliance on expensive cloud GPUs and enabling privacy-preserving, decentralized AI inference. Mesh LLM supports three serving modes: local execution, routing to a peer with the model loaded, or splitting the model across multiple nodes via pipeline parallelism. Performance data shows 16 tok/s for Qwen 235B MoE across 2 nodes.

hackernews · tionis · Jul 11, 22:38 · [Discussion](https://news.ycombinator.com/item?id=48876505)

**Background**: Large language models (LLMs) typically require high-end GPUs with large VRAM, which are expensive and not widely available. Distributed inference splits the model across multiple devices, but traditional approaches rely on centralized orchestration or high-speed interconnects. iroh is an open-source Rust library for peer-to-peer connections that uses key-based addressing instead of IP addresses, making it easier to build decentralized applications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.iroh.computer/blog/mesh-llm">Mesh LLM: distributed AI computing on iroh - Iroh</a></li>
<li><a href="https://github.com/Mesh-LLM/mesh-llm">GitHub - Mesh-LLM/mesh-llm: Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat. · GitHub</a></li>
<li><a href="https://docs.iroh.computer/what-is-iroh">What is iroh? - iroh</a></li>

</ul>
</details>

**Discussion**: Community members expressed interest in using Mesh LLM for small, purpose-built models rather than large coding LLMs. A contributor noted that the skippy engine handles model splitting, and some users raised concerns about network latency but acknowledged the performance numbers shared.

**Tags**: `#distributed computing`, `#LLM inference`, `#peer-to-peer`, `#AI infrastructure`

---

<a id="item-6"></a>
## [RISCBoy: Open-Source RISC-V Portable Game Console](https://github.com/Wren6991/RISCBoy) ⭐️ 8.0/10

RISCBoy is an open-source portable game console designed from scratch around a RISC-V processor, featuring a programmable scanline-buffer rendering pipeline. This project demonstrates the feasibility of building a custom game console using open-source hardware and RISC-V, potentially inspiring more hobbyist and educational projects in embedded gaming. The console uses a scanline-buffer rendering approach, which processes graphics row-by-row rather than pixel-by-pixel, and was taped out on the first wafer.space run.

hackernews · mariuz · Jul 11, 21:58 · [Discussion](https://news.ycombinator.com/item?id=48876245)

**Background**: Scanline rendering is a technique that processes one horizontal line of pixels at a time, reducing memory bandwidth compared to traditional framebuffer methods. RISC-V is an open instruction set architecture that allows custom processor designs. The project is created by Luke Wren, an ASIC design engineer at Raspberry Pi.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Scanline_rendering">Scanline rendering - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters praised the project's technical depth and noted the designer's background at Raspberry Pi and his previous work on PicoDVI. Some wondered if the taped-out design actually worked, but overall sentiment was highly positive.

**Tags**: `#RISC-V`, `#open-source hardware`, `#game console`, `#embedded systems`, `#rendering`

---

<a id="item-7"></a>
## [UPI Architecture and Transaction Flow Explained](https://timeseriesofindia.com/economy/reads/upi-architecture/) ⭐️ 8.0/10

An in-depth article details the architecture and transaction flow of India's UPI payment system, covering its scale and technical design. This article provides valuable technical insight into UPI, a system processing billions of transactions, helping engineers and fintech professionals understand its design and scalability. The article explains the roles of NPCI switch, PSPs, and banks, and describes the transaction flow including intent-based and QR code payments.

hackernews · prtk25 · Jul 11, 16:33 · [Discussion](https://news.ycombinator.com/item?id=48873457)

**Background**: UPI (Unified Payments Interface) is a real-time payment system developed by the National Payments Corporation of India (NPCI). It allows users to link multiple bank accounts to a single mobile app and make instant peer-to-peer and merchant payments. UPI has become the dominant digital payment method in India, processing over 22 billion transactions annually.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unified_Payments_Interface">Unified Payments Interface - Wikipedia</a></li>
<li><a href="https://medium.com/@avinashkariya05910/deep-dive-system-design-of-upi-unified-payments-interface-eff3b0334b0d">Deep Dive: System Design of UPI (Unified Payments Interface) | by Avinash Kariya | Medium</a></li>
<li><a href="https://razorpay.com/blog/what-is-upi-and-how-it-works/">What is UPI ?: Unified Payments Interface Features and How UPI Works?</a></li>

</ul>
</details>

**Discussion**: Commenters praised UPI's widespread adoption and ease of use, with one noting it enabled even elderly people to go digital. However, privacy concerns were raised about the system's reliance on phone numbers and government control, contrasting with Visa/Mastercard. Another commenter compared UPI's peak QPS (~700 average) favorably to Nasdaq's 100k+ QPS, suggesting the scale is manageable.

**Tags**: `#UPI`, `#payment systems`, `#architecture`, `#India`, `#fintech`

---

<a id="item-8"></a>
## [Zer0Fit MCP Server Wraps Google's TabFM & TimesFM for Zero-Shot ML](https://www.reddit.com/r/MachineLearning/comments/1uue8cc/zer0fit_i_took_googles_new_tabfm_timesfm_ml/) ⭐️ 8.0/10

A grad student released Zer0Fit, an MCP server that wraps Google's TabFM and TimesFM foundation models, enabling zero-shot classification, regression, and time-series forecasting via a chat interface like Open WebUI. The server runs locally with Docker and requires 16GB+ VRAM. This project makes Google's powerful zero-shot tabular and time-series models accessible to non-experts through a simple chat interface, lowering the barrier for ML tasks that previously required extensive training and tuning. It bridges the gap between large language models and traditional ML models. Zer0Fit dynamically loads/unloads models with a 5-minute TTL to free VRAM, supports CSV input (XLS/XLSX/JSON/JSONL coming soon), and is PyTorch-based (CUDA only). It achieved 94.7% accuracy on Iris classification and R² of 0.91 on California housing regression in zero-shot mode.

reddit · r/MachineLearning · /u/Porespellar · Jul 12, 12:32

**Background**: TabFM is a zero-shot foundation model for tabular data classification and regression, while TimesFM is a decoder-only foundation model for time-series forecasting, both released by Google Research. MCP (Model Context Protocol) is a standard that allows AI models to interact with external tools and data sources. Zer0Fit implements an MCP server that exposes these models as tools for LLMs to call.

<details><summary>References</summary>
<ul>
<li><a href="https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/">Introducing TabFM: A zero-shot foundation model for tabular data</a></li>
<li><a href="https://github.com/google-research/tabfm">google-research/tabfm - Tabular Foundation Models</a></li>
<li><a href="https://github.com/google-research/timesfm">google -research/ timesfm : TimesFM ( Time Series Foundation Model )...</a></li>

</ul>
</details>

**Discussion**: The Reddit community praised the project for its practical utility and ease of use, with many expressing interest in trying it out. Some users discussed the VRAM requirements and potential for expanding model support. The author actively engaged, noting plans for additional file formats and maintenance based on interest.

**Tags**: `#machine learning`, `#MCP server`, `#zero-shot learning`, `#time series`, `#tabular data`

---

<a id="item-9"></a>
## [VultronRetriever Models Top MTEB Leaderboard](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

VultronRetriever family of models, including Prime-8B, Core-4.5B, and Flash-0.8B, have been released on HuggingFace, achieving #1 in their respective classes on the MTEB leaderboard, with Prime-8B as the global #1. The models demonstrate up to 16x smaller index storage and 12x higher throughput compared to previous 9B-class leaders, and were shown running offline Q&A and embedding on an iPhone. This release significantly advances efficient retrieval, enabling high-performance embedding and search on edge devices like smartphones. The combination of top MTEB scores with drastically reduced resource requirements could democratize access to state-of-the-art retrieval for mobile and embedded applications. The models use the Hydra Architecture for late interaction retrieval, which provides high precision while reducing memory usage by up to half. All models were trained on datasets with 0% cross-dataset duplication and 0% evaluation contamination, and show no overfitting on private MTEB evaluations.

reddit · r/MachineLearning · /u/madkimchi · Jul 11, 15:22

**Background**: The Massive Text Embedding Benchmark (MTEB) is a standard public leaderboard for evaluating embedding models across tasks like retrieval, classification, and clustering. Late interaction retrieval, popularized by models like ColBERT, processes queries and documents separately until the final matching stage, enabling efficient and precise search. The Hydra Architecture is a novel approach that combines retrieval and generation capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB Leaderboard - a Hugging Face Space by mteb</a></li>
<li><a href="https://weaviate.io/blog/late-interaction-overview">An Overview of Late Interaction Retrieval Models... | Weaviate</a></li>
<li><a href="https://www.emergentmind.com/topics/hydra-model">Hydra Model: Unified Architectures</a></li>

</ul>
</details>

**Tags**: `#retrieval`, `#MTEB`, `#embedding`, `#efficiency`, `#HuggingFace`

---

<a id="item-10"></a>
## [Shanghai Aims for High-Quality Brain Control by 2027](https://t.me/zaihuapd/42501) ⭐️ 8.0/10

Shanghai's Science and Technology Commission released the 'Shanghai Brain-Computer Interface Future Industry Cultivation Action Plan (2025-2030)', targeting high-quality brain control by 2027, with semi-invasive BCI products leading clinical applications and breakthroughs in invasive BCI. This government-backed plan signals strong policy support for BCI technology in China, potentially accelerating clinical adoption and positioning Shanghai as a global hub for neural technology. It could benefit patients with paralysis or aphasia by restoring partial motor and language functions. The plan aims to have five or more invasive and semi-invasive BCI products complete medical device type testing and clinical trials, targeting restoration of partial language and motor functions for patients with aphasia or paralysis.

telegram · zaihuapd · Jul 11, 15:49

**Background**: Brain-computer interfaces (BCIs) enable direct communication between the brain and external devices. They are categorized into non-invasive (e.g., EEG caps), semi-invasive (electrodes placed under the skull but outside the brain), and invasive (electrodes implanted directly into brain tissue). Semi-invasive BCIs offer a balance between signal quality and safety, making them promising for clinical use.

<details><summary>References</summary>
<ul>
<li><a href="https://www.jjckb.cn/20251207/2391e2555b2d4825bfc88ca71deebceb/c.html">jjckb.cn/20251207/2391e2555b2d4825bfc88ca71deebceb/c.html</a></li>
<li><a href="https://www.dzwww.com/xinwen/guoneixinwen/202603/t20260313_17538328.htm">dzwww.com/xinwen/guoneixinwen/202603/t20260313_17538328.htm</a></li>
<li><a href="https://www.jfdaily.com/wx/detail.do?id=874565">三家“ 脑 机 接 口 ”头部企业为何出现在上海？｜跟着项目经理看未来产业</a></li>

</ul>
</details>

**Tags**: `#brain-computer interface`, `#neural technology`, `#medical devices`, `#policy`, `#China`

---

<a id="item-11"></a>
## [Apple Sues OpenAI for Trade Secret Theft](https://t.me/zaihuapd/42502) ⭐️ 8.0/10

On July 10, 2026, Apple filed a lawsuit in the U.S. District Court for the Northern District of California against OpenAI, two former employees (Chang Liu and Tang Yew Tan), and io Products, alleging systematic theft of trade secrets related to product design, manufacturing processes, and supply chain information to accelerate OpenAI's hardware business. This high-profile legal battle between two tech giants highlights the intensifying competition in AI hardware and the lengths companies may go to gain an edge, potentially reshaping how firms protect intellectual property and manage employee transitions. Apple alleges that Chang Liu kept a work-issued laptop and exploited a bug to access Apple's cloud file storage after leaving, while Tang Yew Tan emailed himself supplier information before departing and instructed job candidates to bring Apple components to interviews.

telegram · zaihuapd · Jul 11, 16:29

**Background**: OpenAI, best known for AI models like GPT-4, has been expanding into hardware, notably acquiring io Products (co-founded by former Apple designer Jony Ive) in May 2025. Tang Yew Tan, OpenAI's Chief Hardware Officer, previously served as a vice president at Apple. Trade secret lawsuits are common in Silicon Valley, but this case is notable for involving a leading AI company.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.yahoo.com/technology/ai/articles/apple-sues-openai-two-former-202836629.html">Apple sues OpenAI , two former employees for trade secrets theft</a></li>
<li><a href="https://www.macrumors.com/2026/07/10/apple-sues-openai/">Apple Sues OpenAI for Stealing Trade Secrets to Build... - MacRumors</a></li>
<li><a href="https://www.theguardian.com/technology/2026/jul/10/apple-sues-openai-trade-secrets">Apple sues OpenAI, alleging artificial intelligence company stole trade ...</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#OpenAI`, `#trade secrets`, `#legal`, `#hardware`

---