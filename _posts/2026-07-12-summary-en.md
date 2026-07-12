---
layout: default
title: "Horizon Summary: 2026-07-12 (EN)"
date: 2026-07-12
lang: en
---

> From 30 items, 8 important content pieces were selected

---

1. [OpenAI Releases GPT-5.6 Series with Flagship Sol Model](#item-1) ⭐️ 9.0/10
2. [GPT-5.6 Proves 50-Year-Old Graph Theory Conjecture in Under an Hour](#item-2) ⭐️ 9.0/10
3. [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](#item-3) ⭐️ 8.0/10
4. [VultronRetriever Models Top MTEB Leaderboard](#item-4) ⭐️ 8.0/10
5. [6 U-Boot Bootloader Flaws Allow Code Execution at Boot](#item-5) ⭐️ 8.0/10
6. [Shanghai Aims for High-Quality Brain Control by 2027](#item-6) ⭐️ 8.0/10
7. [Apple Sues OpenAI for Trade Secret Theft in Hardware Push](#item-7) ⭐️ 8.0/10
8. [xAI Grok CLI Uploads Entire Codebase and Secrets by Default](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Releases GPT-5.6 Series with Flagship Sol Model](https://t.me/zaihuapd/42497) ⭐️ 9.0/10

OpenAI has officially launched the GPT-5.6 series, introducing three models: Sol (flagship for maximum capability), Terra (balanced performance and cost), and Luna (high-throughput, low-cost). The series brings significant improvements in code generation, knowledge work, design, research, and cybersecurity, along with new features like max/ultra reasoning, multi-agent collaboration, and Programmatic Tool Calling. This release marks a paradigm shift in AI cost efficiency and capability, enabling complex tasks with fewer tokens and lower costs. The multi-tier model strategy allows developers to choose the right balance of intelligence and price, while advanced features like multi-agent collaboration and Programmatic Tool Calling pave the way for more autonomous and efficient AI workflows. GPT-5.6 Sol is the default model for the GPT-5.6 endpoint, offering the highest intelligence. Programmatic Tool Calling allows the model to write and execute JavaScript to coordinate tool calls in a single request, reducing round trips and token usage. Multi-agent collaboration enables multiple AI agents to work together on complex multi-step tasks.

telegram · zaihuapd · Jul 11, 13:34

**Background**: OpenAI's GPT series has evolved from GPT-3 to GPT-4 and now GPT-5.6, each generation improving reasoning, context length, and task completion. The new series introduces a tiered model lineup similar to other AI providers, allowing users to optimize for cost or capability. Programmatic Tool Calling is a technique where the model writes code to call tools programmatically, reducing latency and token costs compared to traditional round-trip tool calling.

<details><summary>References</summary>
<ul>
<li><a href="https://codingfleet.com/blog/gpt-5-6-sol-vs-terra-vs-luna/">GPT‑5.6 Sol vs Terra vs Luna: Which Model Should You Use?</a></li>
<li><a href="https://www.elser.ai/blog/gpt-5-6-sol-vs-terra-vs-luna-which-model-should-you-use">GPT-5.6 Sol vs Terra vs Luna: Which Model Should You Use?</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling">Programmatic Tool Calling | OpenAI API</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-5.6`, `#AI models`, `#machine learning`, `#cost optimization`

---

<a id="item-2"></a>
## [GPT-5.6 Proves 50-Year-Old Graph Theory Conjecture in Under an Hour](https://www.qbitai.com/2026/07/447873.html) ⭐️ 9.0/10

OpenAI's GPT-5.6 Sol Ultra autonomously proved the cycle double cover conjecture, a 50-year-old open problem in graph theory, in under one hour using 64 parallel sub-agents. The model generated a 3-page PDF proof and OpenAI released the full prompt used. This demonstrates that large language models can now autonomously solve long-standing mathematical conjectures, potentially accelerating research in mathematics and theoretical computer science. It also showcases advanced multi-agent reasoning and verification capabilities. The conjecture states that every bridgeless graph has a collection of cycles covering each edge exactly twice. GPT-5.6 transformed the problem into edge labeling over finite fields and solving linear equations, with 64 sub-agents working in parallel and independent verification checks.

telegram · zaihuapd · Jul 12, 03:49

**Background**: The cycle double cover conjecture was independently posed by Szekeres (1973) and Seymour (1979) and is a major open problem in graph theory. A bridge is an edge whose removal disconnects the graph; the conjecture applies only to bridgeless graphs. Previous attempts using traditional mathematical methods had not yielded a full proof.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cycle_double_cover_conjecture">Cycle double cover conjecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bridge_(graph_theory)">Bridge (graph theory)</a></li>

</ul>
</details>

**Tags**: `#AI`, `#mathematics`, `#graph theory`, `#OpenAI`, `#reasoning`

---

<a id="item-3"></a>
## [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 8.0/10

vLLM v0.25.0 makes Model Runner V2 the default for all dense models, removes the legacy PagedAttention implementation, and introduces new models like LLaVA-OneVision-2 and GLM-5, along with a Streaming Parser Engine and universal speculative decoding. This release marks a major architectural shift in vLLM, improving performance and modularity while simplifying the codebase by removing legacy components. It also expands model support and introduces new features that benefit the broader LLM serving ecosystem. Model Runner V2 now supports EVS, realtime embeddings, prefix caching for Mamba hybrid models, and dynamic speculative decoding with full CUDA graphs. The Transformers modeling backend is now as fast as native vLLM, and the release includes 558 commits from 232 contributors.

github · khluu · Jul 11, 20:06

**Background**: vLLM is an open-source LLM inference and serving engine that uses PagedAttention for efficient memory management. Model Runner V2 is a redesigned execution core that addresses design flaws in V1, offering better modularity and performance. PagedAttention was the original attention mechanism that enabled vLLM's high throughput.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#open source`, `#release`, `#performance`

---

<a id="item-4"></a>
## [VultronRetriever Models Top MTEB Leaderboard](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

VultronRetriever family of retrieval models has been released on HuggingFace, achieving #1 on the MTEB leaderboard with up to 16x smaller index and 12x higher throughput, and can run fully offline on an iPhone. This breakthrough enables state-of-the-art retrieval on edge devices, significantly reducing infrastructure costs and latency for applications like offline Q&A and document embedding. The family includes three models: Prime-8B (global #1), Core-4.5B (outperforms models twice its size), and Flash-0.8B (outperforms models up to 5x its size, indexes 60 images/min offline). They use the Hydra architecture for late-interaction retrieval and generation with up to half the memory of comparable models.

reddit · r/MachineLearning · /u/madkimchi · Jul 11, 15:22

**Background**: The MTEB leaderboard is a standard benchmark for evaluating embedding models on retrieval and other tasks. Late-interaction retrieval, like ColBERT, computes token-level similarities for higher precision. The Hydra architecture unifies retrieval and generation in a single model, reducing memory and complexity.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB Leaderboard - a Hugging Face Space by mteb</a></li>
<li><a href="https://arxiv.org/abs/2603.28554">[2603.28554] Hydra: Unifying Document Retrieval and ...</a></li>
<li><a href="https://weaviate.io/blog/late-interaction-overview">An Overview of Late Interaction Retrieval Models: ColBERT, ColPali, and ColQwen | Weaviate</a></li>

</ul>
</details>

**Tags**: `#retrieval`, `#MTEB`, `#edge AI`, `#embedding`, `#NLP`

---

<a id="item-5"></a>
## [6 U-Boot Bootloader Flaws Allow Code Execution at Boot](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

Binarly disclosed six vulnerabilities in U-Boot's FIT signature verification, including two critical remote code execution flaws (BRLY-2026-037 through BRLY-2026-042), affecting versions since 2013.07. These flaws allow attackers to bypass signature checks and execute malicious code before the OS boots, enabling stealthy firmware attacks that can persist undetected. The vulnerabilities affect millions of devices across industries, from embedded systems to servers. Two of the six flaws enable arbitrary code execution, while four cause denial-of-service crashes. Patches have been accepted by U-Boot maintainers, but device vendors must integrate them into firmware updates; end-of-life devices may never be fixed.

telegram · zaihuapd · Jul 11, 08:32

**Background**: U-Boot is a widely used open-source bootloader for embedded devices, responsible for loading the operating system. FIT (Flattened Image Tree) is a format for packaging kernel, device tree, and other images with cryptographic signatures to ensure integrity. The vulnerabilities reside in the signature verification code, allowing attackers to craft malicious FIT images that bypass validation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/">New U-Boot flaws could enable stealthy firmware attacks</a></li>
<li><a href="https://cybersecuritynews.com/u-boot-fit-signature-verification/">Six U - Boot FIT Signature Verification Flaws Enable Code Execution...</a></li>
<li><a href="https://thehackernews.com/2026/07/six-new-u-boot-flaws-could-let.html">Six New U-Boot Flaws Could Let Malicious Images Crash Devices ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#bootloader`, `#firmware`, `#U-Boot`

---

<a id="item-6"></a>
## [Shanghai Aims for High-Quality Brain Control by 2027](https://t.me/zaihuapd/42501) ⭐️ 8.0/10

The Shanghai Municipal Science and Technology Commission issued the "Shanghai Brain-Computer Interface Future Industry Cultivation Action Plan (2025-2030)", setting a target to achieve high-quality brain control by 2027, with semi-invasive BCI products leading clinical application in China and breakthroughs in invasive BCI research. This policy signals strong government support for BCI technology in China, potentially accelerating the development and clinical adoption of BCI devices for medical rehabilitation, such as restoring speech and motor functions for patients with paralysis or aphasia. The plan aims to have five or more invasive and semi-invasive BCI products complete medical device type testing and clinical trials by 2027, targeting restoration of partial language and motor functions. Semi-invasive BCIs are implanted under the skull but not into brain tissue, offering a balance between signal quality and safety.

telegram · zaihuapd · Jul 11, 15:49

**Background**: Brain-computer interfaces (BCIs) enable direct communication between the brain and external devices. They are categorized into invasive (electrodes implanted in brain tissue), semi-invasive (electrodes under skull but outside brain), and non-invasive (scalp electrodes). Invasive BCIs offer the highest signal quality but carry surgical risks, while non-invasive ones are safer but have lower signal resolution. China recently conducted its first clinical trial of invasive BCI, becoming the second country to do so.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/脑机接口">脑机接口 - 维基百科，自由的百科全书</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/699343201">侵入式、半侵入式、非侵入式脑机接口，具体应该怎么选 - 知乎</a></li>
<li><a href="https://www.cas.cn/syky/202506/t20250614_5073157.shtml">我国侵入式脑机接口进入临床试验阶段----中国科学院</a></li>

</ul>
</details>

**Tags**: `#brain-computer interface`, `#neurotechnology`, `#policy`, `#China`, `#medical AI`

---

<a id="item-7"></a>
## [Apple Sues OpenAI for Trade Secret Theft in Hardware Push](https://t.me/zaihuapd/42502) ⭐️ 8.0/10

On July 10, 2026, Apple filed a lawsuit in the U.S. District Court for the Northern District of California against OpenAI, two former employees, and io Products, alleging systematic theft of trade secrets related to product design, manufacturing processes, and supply chain information to accelerate OpenAI's consumer hardware development. This lawsuit escalates tensions between two of the world's most valuable tech companies, potentially impacting OpenAI's hardware ambitions and setting a precedent for how AI companies can recruit talent from established hardware leaders like Apple. Apple alleges that former employee Chang Liu accessed internal networks and downloaded dozens of hardware files after leaving, while OpenAI hardware head Tang Yew Tan sent supplier information to his personal email before resigning and asked job candidates to bring Apple components to interviews. The lawsuit also claims that over 40 former Apple employees now work at OpenAI's hardware division.

telegram · zaihuapd · Jul 11, 16:29

**Background**: OpenAI, best known for ChatGPT, has been expanding into hardware, acquiring io Products in May 2025—a company co-founded by former Apple design chief Jony Ive. The lawsuit alleges that OpenAI's hardware business was built on stolen Apple secrets, including details about unreleased products and manufacturing techniques.

<details><summary>References</summary>
<ul>
<li><a href="https://www.macrumors.com/2026/07/10/apple-sues-openai/">Apple Sues OpenAI for Stealing Trade Secrets to Build AI Hardware</a></li>
<li><a href="https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/">Apple sues OpenAI, accuses ex-employees of stealing trade secrets</a></li>
<li><a href="https://www.nytimes.com/2026/07/10/technology/apple-openai-lawsuit.html">Apple Sues OpenAI, Accusing It of Stealing Company Secrets</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#OpenAI`, `#trade secrets`, `#lawsuit`, `#hardware`

---

<a id="item-8"></a>
## [xAI Grok CLI Uploads Entire Codebase and Secrets by Default](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) ⭐️ 8.0/10

Security researchers discovered that xAI's Grok Build CLI tool (version 0.2.93) uploads entire code repositories and sensitive files like .env to xAI servers by default, with no effective opt-out mechanism. This poses a critical privacy and security risk for developers, as proprietary code and credentials could be exposed without consent, undermining trust in AI-assisted development tools. The tool uploads code via two channels: file contents are embedded in model requests and also packaged as git bundles to Google Cloud Storage; disabling the 'improve model' toggle does not prevent uploads.

telegram · zaihuapd · Jul 12, 04:19

**Background**: Grok CLI is a command-line interface tool that provides access to xAI's Grok AI models. Git bundle is a file format that packages an entire Git repository into a single file for easy transfer. Google Cloud Storage is a cloud object storage service.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Grok_CLI">Grok CLI</a></li>
<li><a href="https://git-scm.com/docs/git-bundle">Git - git-bundle Documentation</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely expresses strong concern over the default data upload behavior, with many users questioning xAI's transparency and calling for an immediate fix or opt-out option.

**Tags**: `#security`, `#privacy`, `#xAI`, `#CLI`, `#data leakage`

---