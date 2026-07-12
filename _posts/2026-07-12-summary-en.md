---
layout: default
title: "Horizon Summary: 2026-07-12 (EN)"
date: 2026-07-12
lang: en
---

> From 29 items, 7 important content pieces were selected

---

1. [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](#item-1) ⭐️ 9.0/10
2. [GPT-5.6 Sol Ultra Proves 50-Year Graph Theory Conjecture in 1 Hour](#item-2) ⭐️ 9.0/10
3. [World's First Invasive BCI Medical Device Approved in China](#item-3) ⭐️ 9.0/10
4. [Terry Tao Uses AI Coding Agents to Build Research Apps](#item-4) ⭐️ 8.0/10
5. [Grok Build CLI Uploads Entire Repos Including Git History](#item-5) ⭐️ 8.0/10
6. [Mesh LLM: Distributed AI Computing on iroh](#item-6) ⭐️ 8.0/10
7. [Zer0Fit: MCP Server for Google's TabFM & TimesFM Models](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 9.0/10

vLLM v0.25.0 makes Model Runner V2 the default execution path for all dense models, removes the legacy PagedAttention backend, and introduces a new Streaming Parser Engine for tool-call and reasoning parsing. The release also adds support for several new models including LLaVA-OneVision-2, Unlimited OCR, and GLM-5. This release marks a major architectural shift in vLLM, simplifying the codebase and improving performance by standardizing on Model Runner V2. The removal of PagedAttention, a foundational component of vLLM, signals the engine's maturity and readiness for production use with modern attention implementations. Model Runner V2 now supports EVS (efficient video sampling), realtime embeddings, prefix caching for Mamba hybrid models, and dynamic speculative decoding with full CUDA graphs. The Transformers modeling backend has been optimized to match native vLLM performance and now supports FP8 MoE.

github · khluu · Jul 11, 20:06

**Background**: vLLM is a high-throughput, memory-efficient inference engine for large language models, originally developed at UC Berkeley. PagedAttention was a key innovation that enabled efficient KV cache management by paging memory like an operating system. Model Runner V2 is a newer execution framework that consolidates various model execution paths into a unified, optimized pipeline.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PagedAttention">PagedAttention - Wikipedia</a></li>
<li><a href="https://docs.vllm.ai/en/latest/models/supported_models/">Supported Models - vLLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#open source`, `#release`, `#AI/ML`

---

<a id="item-2"></a>
## [GPT-5.6 Sol Ultra Proves 50-Year Graph Theory Conjecture in 1 Hour](https://www.qbitai.com/2026/07/447873.html) ⭐️ 9.0/10

On July 10, 2026, OpenAI announced that its GPT-5.6 Sol Ultra model produced a proof of the cycle double cover conjecture, a 50-year-old open problem in graph theory, in under one hour using 64 parallel sub-agents. This marks the first time an AI has autonomously solved a long-standing open mathematical conjecture, demonstrating advanced reasoning and multi-agent collaboration capabilities that could accelerate research in mathematics and other fields. The proof was generated as a 3-page PDF, and OpenAI published the full 700-character orchestration prompt that defines acceptance criteria, definitions, boundary conditions, and failure cases without prescribing fixed steps.

telegram · zaihuapd · Jul 12, 03:49

**Background**: The cycle double cover conjecture, posed by W. T. Tutte and others, asks whether every bridgeless undirected graph has a collection of cycles such that each edge appears exactly twice. A bridge is an edge whose removal disconnects the graph. The conjecture is a fundamental problem in graph theory with connections to graph embeddings and the four-color theorem.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cycle_double_cover_conjecture">Cycle double cover conjecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bridge_(graph_theory)">Bridge (graph theory)</a></li>
<li><a href="https://the-decoder.com/openais-gpt-5-6-sol-ultra-reportedly-solves-a-50-year-old-math-problem-in-under-an-hour/">OpenAI's GPT-5.6 Sol Ultra reportedly solves a 50-year-old ...</a></li>

</ul>
</details>

**Discussion**: Mathematician Thomas Bloom called the proof surprisingly elementary but criticized the lack of citations for known prior work. The broader community is debating whether the AI truly discovered new mathematics or merely recombined existing knowledge.

**Tags**: `#AI`, `#graph theory`, `#LLM`, `#mathematical proof`, `#OpenAI`

---

<a id="item-3"></a>
## [World's First Invasive BCI Medical Device Approved in China](https://t.me/zaihuapd/42515) ⭐️ 9.0/10

China's National Medical Products Administration (NMPA) has approved the 'Implantable Brain-Computer Interface Hand Motor Function Compensation System' developed by BrainCo Medical Technology (Shanghai) Co., Ltd., marking the world's first invasive BCI medical device to enter clinical use. This approval represents a paradigm shift in neurotechnology and rehabilitation, offering a new therapeutic option for quadriplegic patients with cervical spinal cord injury. It sets a precedent for regulatory pathways and clinical adoption of invasive BCIs worldwide. The device uses epidural minimally invasive implantation and wireless power and data transmission, and is paired with a pneumatic glove to assist patients aged 18–60 with hand grasping function. Clinical trials showed significant improvement in hand grasping ability and quality of life.

telegram · zaihuapd · Jul 12, 14:39

**Background**: Invasive brain-computer interfaces (BCIs) involve implanting electrodes directly on or in the brain to record neural signals, enabling direct communication between the brain and external devices. Unlike non-invasive BCIs, invasive approaches offer higher signal fidelity but require surgery. This device is distinct from Neuralink's Telepathy product, as it uses epidural electrodes and wireless power without implanted batteries, reducing tissue damage.

<details><summary>References</summary>
<ul>
<li><a href="https://bydrug.pharmcube.com/news/detail/4ff694804b93d4abc8588e8180ce7d1b">博睿康无线微创植入脑机接口NEO迎来突破性进展，四肢截瘫患者通过植入实现自主脑控喝水| 松禾Portfolio医药新闻-ByDrug-一站式医药资源共享中心-医药魔方</a></li>

</ul>
</details>

**Tags**: `#brain-computer interface`, `#medical device`, `#neurotechnology`, `#rehabilitation`, `#China`

---

<a id="item-4"></a>
## [Terry Tao Uses AI Coding Agents to Build Research Apps](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/) ⭐️ 8.0/10

Terry Tao, a renowned mathematician, used modern LLM-based coding agents to port over two dozen old applets and create new interactive visualizations for his research, finding only one minor bug in the process. This demonstrates that AI coding agents can empower domain experts without deep coding skills to create software, potentially unlocking vast latent demand for specialized applications across many fields. Tao used guided interaction with LLM agents to port and build applets, noting that while LLM code can contain bugs, he found only one minor drag-event bug, and the agent even identified two bugs in his original code.

hackernews · subset · Jul 12, 11:09 · [Discussion](https://news.ycombinator.com/item?id=48880170)

**Background**: AI coding agents are tools that can write, debug, and deploy code from natural language descriptions, going beyond simple autocomplete. They are increasingly used to improve productivity and lower barriers to software creation, especially for non-professional programmers.

<details><summary>References</summary>
<ul>
<li><a href="https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/">Old and new apps, via modern coding agents | What's new</a></li>
<li><a href="https://agentic.ai/best/coding-agents">20 Best AI Coding Agents in 2026 — Agentic.ai</a></li>
<li><a href="https://www.analyticsinsight.net/artificial-intelligence/best-ai-coding-agents-and-development-platforms-for-developers-in-2026">Best AI Coding Agents and Development Platforms in 2026</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the democratization of coding, with one noting that even Tao finds some code too complex, and another emphasizing the infinite latent demand for software outside traditional tech spaces. The sentiment was broadly positive, with a balanced view that LLMs are a useful tool but not to be fully trusted.

**Tags**: `#LLM`, `#coding agents`, `#software development`, `#AI-assisted programming`, `#democratization`

---

<a id="item-5"></a>
## [Grok Build CLI Uploads Entire Repos Including Git History](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) ⭐️ 8.0/10

A wire-level analysis of xAI's Grok Build CLI reveals that it uploads the entire repository, including all tracked file contents and git history, regardless of what the AI agent actually reads. This behavior was discovered by inspecting network traffic between the CLI and xAI servers. This raises serious privacy concerns for developers using Grok Build, as entire codebases and sensitive git history are transmitted to xAI without explicit user awareness. It highlights the broader risk of proprietary AI coding tools that may silently exfiltrate data, undermining trust in such tools. The analysis shows that the upload happens independently of what the agent reads, meaning even files not accessed by the AI are sent. The tool is installed via a curl command and requires signing in with an xAI account, and it is available to SuperGrok and X Premium Plus subscribers.

hackernews · jhoho · Jul 12, 01:09 · [Discussion](https://news.ycombinator.com/item?id=48877371)

**Background**: Wire-level analysis involves inspecting the raw network traffic between a client and server to understand what data is being transmitted. Grok Build is a terminal-based AI coding agent from xAI that assists developers by reading and modifying code in a workspace. Many AI coding tools operate by sending code context to remote models, but the extent of data sent is often not transparent to users.

<details><summary>References</summary>
<ul>
<li><a href="https://x.ai/news/grok-build-cli">Introducing Grok Build | SpaceXAI</a></li>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>

</ul>
</details>

**Discussion**: Community comments express shock and concern, with users noting that this behavior is extremely concerning and undermines trust in xAI. Some users suggest sandboxing tools like bubblewrap to limit access, while others argue that users should assume the agent can read everything in the workspace. There is debate about the tradeoffs between using proprietary agents versus open-source alternatives like opencode.

**Tags**: `#privacy`, `#AI coding tools`, `#security`, `#xAI`, `#Grok`

---

<a id="item-6"></a>
## [Mesh LLM: Distributed AI Computing on iroh](https://www.iroh.computer/blog/mesh-llm) ⭐️ 8.0/10

Mesh LLM enables distributed AI computing across heterogeneous nodes with a simple setup, achieving 16 tok/s on a 235B model across 2 nodes. This simplifies running large language models on consumer hardware by pooling VRAM across devices, making advanced AI more accessible to individuals and small teams. The project uses a peer-to-peer architecture built on iroh, and the public mesh allows users to join and contribute compute resources with a single command.

hackernews · tionis · Jul 11, 22:38 · [Discussion](https://news.ycombinator.com/item?id=48876505)

**Background**: Large language models (LLMs) require significant GPU memory (VRAM) to run, often exceeding what a single consumer GPU can provide. Distributed inference splits the model across multiple machines, but traditional setups are complex. Mesh LLM aims to make this as easy as joining a swarm.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Mesh-LLM/mesh-llm">GitHub - Mesh - LLM / mesh - llm : Distributed AI/ LLM for the people.</a></li>
<li><a href="https://meshllm.cloud/">Mesh LLM</a></li>

</ul>
</details>

**Discussion**: Users report extremely easy setup, with one commenter noting it 'worked first try.' However, some express concerns about performance over consumer networks, though the project claims 16 tok/s on a 235B model across 2 nodes.

**Tags**: `#distributed computing`, `#LLM`, `#AI`, `#open source`, `#peer-to-peer`

---

<a id="item-7"></a>
## [Zer0Fit: MCP Server for Google's TabFM & TimesFM Models](https://www.reddit.com/r/MachineLearning/comments/1uue8cc/zer0fit_i_took_googles_new_tabfm_timesfm_ml/) ⭐️ 8.0/10

A graduate student created Zer0Fit, an MCP server that wraps Google's TabFM and TimesFM foundation models, enabling zero-shot classification, regression, and time-series forecasting via a chat interface like Open WebUI. The server runs locally in a Docker container and achieved 94.7% accuracy on the Iris dataset and an R² of 0.91 on California housing regression. Zer0Fit bridges the gap between traditional ML models and LLM-based interfaces, allowing users to perform complex ML tasks without manual model training or hyperparameter tuning. This makes advanced ML accessible to a broader audience and integrates seamlessly with local LLM workflows. The server requires 16GB of VRAM and is CUDA-only (PyTorch-based), supporting Nvidia GPUs like the 3090 and H100. It dynamically loads/unloads models with a 5-minute TTL to free VRAM when idle, and currently supports CSV input with plans for XLS, XLSX, JSON, and JSONL.

reddit · r/MachineLearning · /u/Porespellar · Jul 12, 12:32

**Background**: TabFM and TimesFM are foundation models from Google Research for tabular data and time-series forecasting, respectively. TabFM uses in-context learning to perform zero-shot classification and regression without training, while TimesFM is a decoder-only model pre-trained on billions of real-world time points. MCP (Model Context Protocol) is a standard for connecting AI models to external tools and data sources, enabling LLMs to invoke ML models as tools.

<details><summary>References</summary>
<ul>
<li><a href="https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/">Introducing TabFM: A zero-shot foundation model for tabular data</a></li>
<li><a href="https://github.com/google-research/tabfm">GitHub - google-research/tabfm</a></li>
<li><a href="https://github.com/google-research/timesfm/">GitHub - google-research/timesfm: TimesFM (Time Series ...</a></li>

</ul>
</details>

**Discussion**: The Reddit post received positive engagement, with users praising the practical integration of Google's new models into a local MCP server. Some discussed the 16GB VRAM requirement as a limitation, while others expressed interest in testing the server with their own datasets.

**Tags**: `#MCP`, `#TabFM`, `#TimesFM`, `#zero-shot ML`, `#local LLM`

---