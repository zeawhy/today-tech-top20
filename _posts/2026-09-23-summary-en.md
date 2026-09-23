---
layout: default
title: "Horizon Summary: 2026-09-23 (EN)"
date: 2026-09-23
lang: en
---

> From 95 items, 14 important content pieces were selected

---

1. [Anthropic says Claude discovered a novel CRISPR-like enzyme system](#item-1) ⭐️ 9.0/10
2. [Anthropic and OpenAI Launch Claude Opus 5.5 and GPT-6 Sol/Luna, Sparking Price War](#item-2) ⭐️ 9.0/10
3. [vLLM v0.30.0 adds new models, Fast Start caching, MXFP8 KV](#item-3) ⭐️ 8.0/10
4. [Google launches Gemini 3.8 text-to-speech with 30-second voice cloning](#item-4) ⭐️ 8.0/10
5. [Jev in 25 Lines of Python: Minimal LLM Logprobs Classifier](#item-5) ⭐️ 8.0/10
6. [Seattle City Council bans surveillance pricing for groceries](#item-6) ⭐️ 8.0/10
7. [OpenAI's GPT-6 Astra Reportedly Cracks Long-Unsolved Enigma Message](#item-7) ⭐️ 8.0/10
8. [GPT-6 Astra Demonstrates Ability to Drive a Car](#item-8) ⭐️ 8.0/10
9. [TypeSafe AI Launches Jev, a 'System One' Decision Model](#item-9) ⭐️ 8.0/10
10. [Xiaomi Releases MiMo-V2.6 Multimodal Model With $3.5M RL Cost](#item-10) ⭐️ 8.0/10
11. [China Probes DeepSeek and Moonshot Over Data Leaks to Anthropic's Claude](#item-11) ⭐️ 8.0/10
12. [DeepSeek to Brief UN Security Council on AI Risks This Week](#item-12) ⭐️ 8.0/10
13. [OpenAI Begins Limited Preview of GPT-5.6 Series: Sol, Terra, Luna](#item-13) ⭐️ 8.0/10
14. [ShinyHunters Claims Breach of FBI Employee and Applicant Data](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic says Claude discovered a novel CRISPR-like enzyme system](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) ⭐️ 9.0/10

Anthropic announced that its AI model Claude discovered a previously unknown enzyme system whose gene sits beside a long array of repeating DNA resembling CRISPR repeats. The finding was published as an Anthropic news post rather than a traditional peer-reviewed journal submission or preprint. CRISPR repeats became the foundation of modern gene-editing medicines, so an AI-flagged CRISPR-like system could point toward new gene-editing or biotechnology tools. It also fuels debate over whether AI companies should conduct and publish frontier scientific research in-house rather than partnering with academic labs. Anthropic notes that the function of the repeating DNA structure is not yet understood, and the discovery has not been validated through peer review. Community members also questioned whether Claude found the system autonomously or whether a human using Claude found it.

hackernews · raahelb · Sep 23, 18:06 · [Discussion](https://news.ycombinator.com/item?id=49820134)

**Background**: CRISPR is a family of DNA sequences found in bacteria and archaea, originally noticed as unusual repeat sequences and now the basis of gene-editing therapies. AI-driven scientific discovery uses machine learning to analyze large datasets and surface patterns that might be hard for humans to spot. Anthropic has been expanding into science tools, including a Claude Science workbench for researchers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-discovers-novel-enzyme-system">Claude discovers a novel enzyme system with CRISPR-like repeats - Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/CRISPR">CRISPR - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists - Anthropic</a></li>

</ul>
</details>

**Discussion**: Commenters were divided: some criticized Anthropic for publishing a marketing whitepaper instead of a journal submission, while others questioned why AI companies run this research in-house rather than partnering externally. Several noted that biology is harder for LLMs than math and that the problem had to be scoped down significantly, though many were glad the work was being done at all.

**Tags**: `#AI`, `#CRISPR`, `#scientific discovery`, `#Anthropic`, `#biotechnology`

---

<a id="item-2"></a>
## [Anthropic and OpenAI Launch Claude Opus 5.5 and GPT-6 Sol/Luna, Sparking Price War](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 9.0/10

Anthropic released Claude Opus 5.5, and roughly an hour later OpenAI released GPT-6 Sol and GPT-6 Luna, with GPT-6 Luna priced at half the cost of its GPT-5.6 predecessor ($0.10/M input, $0.50/M output). Claude Opus 5.5 also received a price cut, now at $4/M input and $20/M output. This simultaneous release and aggressive price reduction signals an intensifying price war among frontier model providers, dramatically lowering the cost of building AI applications and likely reshaping which models developers choose for production workloads. GPT-6 Luna at $0.10/$0.50 is one of the cheapest models OpenAI has ever released, beaten only by the weaker GPT-4.1 Nano and GPT-5 Nano; GPT-5.6 has a scheduled 25% price increase in November, so GPT-6 is half the price of even the promotional pricing.

rss · Simon Willison · Sep 22, 23:46

**Background**: Frontier AI labs like Anthropic and OpenAI regularly release new flagship large language models, and pricing per million tokens is a key competitive lever for developers building applications on top of them. Anthropic's Claude line uses Haiku, Sonnet, and Opus tiers, while OpenAI's GPT-6 family introduces Sol and Luna variants alongside existing Terra and Astra models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://x.ai/news/grok-4-7">Introducing Grok 4.7 - SpaceXAI</a></li>
<li><a href="https://artificialanalysis.ai/models/claude-opus-5-5">Claude Opus 5 . 5 (max with fallback) - Intelligence... | Artificial Analysis</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted GPT-6 Luna's halved price as a major development, with one noting an emotional attachment to the previous GPT-5.6 Sol model and concern that successors may feel less natural to work with. Others compared Claude Code and Codex Pro subscription value, with Codex winning on usage limits, while some praised ChatGPT Plus as effectively limitless for everyday tasks.

**Tags**: `#AI`, `#LLM`, `#OpenAI`, `#Anthropic`, `#model-releases`

---

<a id="item-3"></a>
## [vLLM v0.30.0 adds new models, Fast Start caching, MXFP8 KV](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM released v0.30.0, a major update with 762 commits from 315 contributors (104 new), adding support for models such as DeepSeek-V4.1-Flash, DeepSeek-V4-Flash-Vision-Exp, GLM-5.3-Flash, K2-Horizon, Cohere Compass, Bailing V3 VL and Nanbeige4.2. It introduces a persistent per-GPU weight-cache daemon called Fast Start, MXFP8 KV storage for DeepSeek-V4.1-Flash on SM100, Gumbel-max watermarking, HiSparse host-resident KV tiering, and numerous performance optimizations for Qwen3.8-Flash-Next and Kimi K3. vLLM is one of the most widely used open-source LLM inference and serving engines, so this release directly affects AI infrastructure teams deploying models at scale. Features like Fast Start weight caching and MXFP8 KV storage can substantially reduce engine startup time and GPU memory pressure, while broad new model support keeps vLLM aligned with the fast-moving frontier of open-weight LLMs. Fast Start keeps post-quantized, TP-sharded weights in GPU memory and maps them over CUDA IPC via `--load-format ipc_cache`, now covering FP4 checkpoints and multi-node TP. HiSparse spills sparse-MLA KV pages to pinned host memory under GPU pressure and serves top-k misses from a per-request GPU hot buffer, while Model Runner V2 cuts graph capture from 12s to 2s and engine init from 28.9s to 8.2s on H200.

github · khluu · Sep 22, 05:20

**Background**: vLLM is an open-source high-throughput engine for serving large language models, built around techniques like PagedAttention and continuous batching to maximize GPU utilization. KV cache refers to the key/value tensors stored during attention computation, and its size often limits how many concurrent requests a server can handle; quantizing it to formats like MXFP8 reduces that memory footprint. FlashMLA is DeepSeek's library of optimized attention kernels for its MLA-based models, and speculative decoding speeds up generation by using a small draft model to propose tokens that a larger model verifies.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/stable/configuration/optimization/">Optimization and Tuning - vLLM Documentation</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">FlashMLA</a></li>
<li><a href="https://docs.vllm.ai/en/stable/design/prefix_caching/">Automatic Prefix Caching - vLLM Documentation</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#model serving`, `#release`, `#AI infrastructure`

---

<a id="item-4"></a>
## [Google launches Gemini 3.8 text-to-speech with 30-second voice cloning](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/) ⭐️ 8.0/10

Google announced Gemini 3.8 Flash and Flash-Lite text-to-speech models, which can recreate consistent vocal profiles from just a 30-second audio sample, offer over 2,000 production-ready voices, and support 100 languages. The release includes built-in consent verification, SynthID watermarking, and C2PA content credentials to protect voice talent and developers. This marks Google's full embrace of voice cloning, a capability already offered by other providers, and could accelerate the adoption of personalized synthetic voices in audiobooks, games, and accessibility tools. The inclusion of consent verification and watermarking sets a potential industry precedent for ethical voice AI deployment. The model is optimized for high-volume bulk production, conversational voice agents, and read-aloud features, and it claims the #1 spot on Hume AI's voice benchmarks. Voice remixing is listed as coming soon, and availability differs across Google's consumer, prosumer, and cloud platforms.

hackernews · swolpers · Sep 23, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49817615)

**Background**: Text-to-speech (TTS) systems convert written text into spoken audio, and recent AI models can now mimic a specific person's voice from a short sample. SynthID is Google DeepMind's technology that embeds invisible digital watermarks into AI-generated content, while C2PA is an open standard for cryptographically signed provenance metadata that records how a piece of media was created and edited.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/">Gemini 3.8 text-to-speech says hello</a></li>
<li><a href="https://deepmind.google/models/synthid/">SynthID — Google DeepMind</a></li>
<li><a href="https://c2pa.org/">C2PA</a></li>

</ul>
</details>

**Discussion**: Commenters criticized Google for inconsistent feature availability across its consumer, prosumer, and cloud platforms, noting that models often have different capabilities on each. Others observed that voice cloning is now common enough that Google no longer hesitates to ship it, while some shared practical TTS projects and welcomed the large voice library and fine-grained control.

**Tags**: `#AI`, `#text-to-speech`, `#voice cloning`, `#Google Gemini`, `#Hacker News`

---

<a id="item-5"></a>
## [Jev in 25 Lines of Python: Minimal LLM Logprobs Classifier](https://www.nobodywho.ai/posts/jev-in-25-lines/) ⭐️ 8.0/10

A blog post at nobodywho.ai demonstrates how to implement Jev — a technique for extracting classification probabilities directly from an LLM's token logprobs — in just 25 lines of Python. The post has sparked a large discussion (564 points, 182 comments) with contributions from notable practitioners including antirez, the creator of Redis. This minimal implementation makes a powerful classification technique accessible to any Python developer, potentially reducing the cost and latency of text classification tasks that currently rely on full LLM text generation. The high-profile community discussion surfaces practical pitfalls and optimization tricks that could shape how practitioners adopt logprob-based classification. The discussion highlights that chat models tend to dilute the probabilities of choice tokens because they are trained to produce prose, so careful system instructions and prompt formatting are needed. antirez points out that due to masked attention, placing the options before the body of text lets the transformer use more tokens to build state for the task, and repeating the question can improve calibration.

hackernews · bashbjorn · Sep 23, 07:26 · [Discussion](https://news.ycombinator.com/item?id=49812769)

**Background**: Jev is a classification method from TypeSafe that uses an LLM's log probabilities (logprobs) — the logarithm of the probability assigned to each token — to determine which predefined category a piece of text belongs to, rather than generating free-form text. Logprobs are derived from the model's raw logits after applying the softmax function, and they provide a natural confidence score for classification. This approach avoids the latency and cost of full text generation while leveraging the LLM's understanding of language.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jev_(AI_model)">Jev (AI model) - Wikipedia</a></li>
<li><a href="https://www.langchain.com/blog/building-a-harness-with-jev">What Is Jev? A Guide to TypeSafe AI’s System One Model</a></li>

</ul>
</details>

**Discussion**: Commenters broadly agree the technique is clever but raise important caveats: sigmoid10 warns that chat models dilute choice-token probabilities and recommends clear system instructions, while antirez suggests placing options before the text and repeating the task for better calibration. visarga shares an alternative embedding-based classifier trained with ridge regression in under a second, noting Jev lacks in-domain training data, and rcarmo describes prototyping with Gemma on a local GPU.

**Tags**: `#LLM`, `#classification`, `#logprobs`, `#Python`, `#prompt-engineering`

---

<a id="item-6"></a>
## [Seattle City Council bans surveillance pricing for groceries](https://advocacy.consumerreports.org/press_release/seattle-city-council-votes-to-ban-surveillance-pricing-in-sale-of-groceries/) ⭐️ 8.0/10

The Seattle City Council voted to ban surveillance pricing in the sale of groceries, prohibiting retailers from using consumers' personal data to set individualized prices for food items. The bill also permits various discounting practices while requiring greater transparency around discounts and placing some limits on how consumers can be profiled. This is one of the first municipal bans on surveillance pricing in the US, setting a precedent for how cities and states might regulate algorithmic price personalization. It could influence broader consumer protection efforts and push retailers to rethink data-driven pricing strategies in the grocery sector and beyond. The ban is limited to groceries and includes a discounting loophole that allows retailers to offer personalized discounts, which critics say could undermine the law's intent. The bill also requires increased transparency around discounts and places some limitations on consumer profiling.

hackernews · ortusdux · Sep 23, 14:04 · [Discussion](https://news.ycombinator.com/item?id=49816374)

**Background**: Surveillance pricing is a form of dynamic pricing where a consumer's personal data and behavior are used to infer their willingness to pay, often resulting in different prices for the same product. It has raised concerns over algorithmic discrimination, consumer privacy, and digital redlining, and several states have recently considered or enacted related regulations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Surveillance_pricing">Surveillance pricing</a></li>
<li><a href="https://epic.org/issues/consumer-privacy/surveillance-pricing/">Surveillance Pricing – EPIC – Electronic Privacy Information Center</a></li>
<li><a href="https://www.brookings.edu/articles/what-is-dynamic-pricing-and-why-do-consumers-need-better-protections/">What is dynamic pricing, and why do consumers need better protections? | Brookings</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters broadly supported the ban but debated its scope, with some arguing it should apply to all goods and services, not just groceries. Others highlighted the discount loophole and called for stronger privacy protections, such as a constitutional right to privacy.

**Tags**: `#privacy`, `#surveillance-pricing`, `#regulation`, `#consumer-protection`, `#algorithmic-fairness`

---

<a id="item-7"></a>
## [OpenAI's GPT-6 Astra Reportedly Cracks Long-Unsolved Enigma Message](https://www.cryptocellar.org/bgac/the-mvueh-break.html) ⭐️ 8.0/10

OpenAI's GPT-6 Astra reportedly decrypted an 82-letter Enigma-encrypted message, known by its indicator MVUEH, that had remained unbroken on Frode Weierud's CryptoCellar research site since 2005. The decrypted text reads approximately: 'Please specify the route of march. I am in Rosenow, Rosenow. Immediate reply by radio. Waschbusch.' If verified, this marks a notable milestone in AI-assisted cryptanalysis, showing that large language models can contribute to solving historical ciphers that resisted decades of human and computational effort. It also fuels the broader debate about how much credit AI deserves when it relies on generated or existing software tools to perform the actual computation. The message's plaintext contains misspellings typical of field transmissions, and the decryption was reportedly achieved with GPT-6 Astra developing Python and C++ software for an Enigma simulator. Skeptics note that much of the generated code may not be novel and that the actual breaking process may have been offloaded to that software, raising questions about the AI's true contribution.

hackernews · sohkamyung · Sep 22, 13:52 · [Discussion](https://news.ycombinator.com/item?id=49801324)

**Background**: The Enigma machine was a rotor-based cipher device used by Nazi Germany during World War II; its codes were famously broken by Alan Turing and others at Bletchley Park, which significantly aided the Allied war effort. Despite these successes, some individual messages remained unsolved for decades due to missing key settings or operator errors. Frode Weierud's CryptoCellar site maintains a list of such unbroken messages, and the MVUEH message had been on that list since 2005.

<details><summary>References</summary>
<ul>
<li><a href="https://mixed-news.com/en/gpt-6-astra-cracks-1941-enigma-message-unsolved-since-2005/">GPT-6 Astra cracks a 1941 Enigma message that had resisted solution since 2005</a></li>
<li><a href="https://news.ycombinator.com/item?id=49801324">OpenAI GPT–6 Astra breaks Enigma message that has resisted solution since 2005 | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cryptanalysis_of_the_Enigma">Cryptanalysis of the Enigma - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters expressed skepticism about the novelty and credit attributed to GPT-6 Astra, with one noting that 'did it entirely on its own' is incongruous with the AI developing software for an Enigma simulator. Another commenter reported that Gemini 3.8 Flash also solved the message in about 45 minutes, suggesting the task may not be uniquely challenging for advanced models. Others shared the decrypted text and pointed to a recent Veritasium video on Enigma, while one joked that the solution is 'a bit late for the war effort.'

**Tags**: `#AI`, `#cryptography`, `#Enigma`, `#OpenAI`, `#Hacker News`

---

<a id="item-8"></a>
## [GPT-6 Astra Demonstrates Ability to Drive a Car](https://drivingbench.com/) ⭐️ 8.0/10

OpenAI's GPT-6 Astra, released in September 2026, has been demonstrated driving a car in a benchmark hosted at drivingbench.com, prompting intense discussion on Hacker News (249 points, 213 comments). The demo shows a cloud-delivered LLM can map sensor inputs to steering and actuator outputs well enough to complete a driving route. This suggests that end-to-end LLM-based driving could eventually challenge the traditional modular self-driving stack of vision, 3D maps, lane-selection grammar, and occupancy networks. If low-latency open-weight equivalents emerge, it could reshape how autonomous driving systems are built and who can build them. The core limitation is latency: the model is too large to run locally, so a cloud round-trip makes real-world driving infeasible for now. Commenters also note Astra's unusually strong vision and spatial reasoning, as reflected in high ARC 3, SpatialBench, and ZeroBench scores, which may explain its driving capability.

hackernews · plurby · Sep 23, 15:14 · [Discussion](https://news.ycombinator.com/item?id=49817404)

**Background**: GPT-6 Astra is OpenAI's large language model released to approved users on September 3, 2026, with general availability the next day. Autonomous driving has traditionally relied on modular pipelines combining cameras, LiDAR, HD maps, and hand-engineered planners, while recent research such as LMDrive and Talk2Drive has explored using LLMs as driving agents. The drivingbench.com demo tests whether a general-purpose LLM can directly control a vehicle from sensor data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT - 6 Astra : A new generation of intelligence | OpenAI</a></li>
<li><a href="https://paperswithcode.co/paper/2312.07488">LMDrive: Closed-Loop End - to - End Driving with Large Language ...</a></li>

</ul>
</details>

**Discussion**: Commenters were split: an openpilot contributor argued the demo proves an LLM could drive a route but absolutely cannot work in the real world due to latency, while others said the 'bitter lesson' is coming for self-driving and that open-weight low-latency equivalents like Qwen are not far off. Several praised Astra's vision and spatial reasoning scores, and some joked about it landing a plane next or automating neighborhood parking.

**Tags**: `#LLM`, `#autonomous driving`, `#GPT-6`, `#AI`, `#self-driving cars`

---

<a id="item-9"></a>
## [TypeSafe AI Launches Jev, a 'System One' Decision Model](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 8.0/10

TypeSafe AI unveiled Jev, its first public 'System One' model, which accepts unstructured text input and returns typed probabilistic outputs — yes/no (Noul) confidences, choice distributions, and numeric scores — instead of generated text. It is priced at $0.042 per million input tokens with free output, cheaper than OpenAI's GPT-5 Nano at $0.05 per million, and is available in early access. Jev represents a genuinely new model category that reframes LLM inference as a typed decision function rather than text generation, making it dramatically faster and cheaper for classification-style tasks like spam detection, labeling, prioritization, and search reranking. If the approach holds up, it could shift a large class of enterprise automation workloads away from general-purpose chat models toward specialized decision models. Jev supports three question types — Noul (Bernoulli) yes/no confidence scores, choice questions returning a probability distribution over options, and score questions returning a float along a described numeric range — and evaluates many questions in parallel against a single 'state' document. Its own jaggedness documentation notes weaknesses with numbers, dates, and adversarial content, and because it only returns floats, it offers no natural-language justification for its decisions.

rss · Simon Willison · Sep 21, 23:09

**Background**: Most LLMs are autoregressive: they generate output one token at a time, which is why output tokens are typically priced higher than input tokens. TypeSafe AI is positioning 'System One' models as a separate class built specifically for making decisions inside software, analogous to fast, intuitive 'System 1' thinking rather than deliberate reasoning. Structured-output APIs can already force an LLM to emit valid JSON, but the model is still generating text, and its stated confidence is prose rather than a number an application can branch on.

<details><summary>References</summary>
<ul>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models & Jev - TypeSafe AI Blog</a></li>
<li><a href="https://www.mindstudio.ai/blog/jev-system-one-model-launch">Jev Explained: Typesafe AI's Non-Autoregressive System-1 Model | MindStudio</a></li>
<li><a href="https://apimaster.ai/blog/jev-vs-llm">Jev vs LLMs: Where a Decision Model Beats Prompting... | APIMaster.AI</a></li>

</ul>
</details>

**Discussion**: Simon Willison endorsed the 'decision model' framing suggested by Maggie Appleton over TypeSafe's 'System One' branding, and the naming debate signals genuine community engagement. Willison also raised discomfort that Jev pushes machine learning further toward black-box systems, since it returns only a floating-point number with no explanation of which content signals drove the decision.

**Tags**: `#LLM`, `#AI/ML`, `#decision-models`, `#inference`, `#model-architecture`

---

<a id="item-10"></a>
## [Xiaomi Releases MiMo-V2.6 Multimodal Model With $3.5M RL Cost](https://www.reddit.com/r/MachineLearning/comments/1wn36d4/xiaomi_releases_mimov26_frontier_intelligence_all/) ⭐️ 8.0/10

Xiaomi has officially released and open-sourced the MiMo-V2.6 series, a frontier multimodal AI model whose total reinforcement learning training cost was disclosed as $3.5 million. The release is accompanied by a live "benchmaxxing" dashboard that publicly tracks the model's benchmark performance. The disclosure of a concrete $3.5M RL training cost and a public benchmark dashboard bring unusual transparency to frontier model development, which is typically kept secret. This could pressure other labs to reveal training economics and give the open-source community a stronger reference point for cost-efficient multimodal training. MiMo-V2.6 is available on Hugging Face (including a Flash-RL variant), with recommended sampling of temperature=1.0 and top_p=0.95, and is also accessible via AI Studio, MiMo Code, Xiaomi MiMo Desktop, the MiMo Open Platform API, and OpenRouter. Xiaomi's materials experts reportedly used MiMo-V2.6-Pro to design a new metal-organic framework (MOF) for adsorbing PFAS "forever chemicals."

reddit · r/MachineLearning · /u/we_are_mammals · Sep 22, 07:56

**Background**: MiMo is Xiaomi's in-house large model series, and V2.6 focuses on scaling up reinforcement learning (RL) for self-improvement. RL is a post-training technique where a model learns from reward signals rather than labeled examples, and its compute cost is a major driver of frontier AI expenses. "Benchmaxxing" refers to optimizing a model specifically to score well on public benchmarks, so a live dashboard invites scrutiny of whether reported gains are genuine.

<details><summary>References</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo - V 2 . 6 | Xiaomi</a></li>
<li><a href="https://mimo.mi.com/docs/en-US/news/latest/v2-6">Xiaomi MiMo Home</a></li>
<li><a href="https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL">XiaomiMiMo/ MiMo - V 2 . 6 -Flash-RL · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Multimodal`, `#Xiaomi`, `#Model Release`, `#Reinforcement Learning`

---

<a id="item-11"></a>
## [China Probes DeepSeek and Moonshot Over Data Leaks to Anthropic's Claude](https://www.theinformation.com/articles/china-probes-deepseek-moonshot-potential-data-leaks-anthropic) ⭐️ 8.0/10

China's internet regulator is investigating DeepSeek and Moonshot AI following allegations that the two companies forwarded sensitive user data to Anthropic's Claude model. The probe was triggered by a 154-page report Anthropic published on September 10, which accused seven Chinese companies of large-scale violations of Claude's usage terms, citing an example in which DeepSeek allegedly forwarded a request from an engineer working on a police surveillance system to Claude. This is a rare case of a Chinese regulator investigating domestic AI champions over cross-border data flows, and it could reshape how Chinese AI firms use foreign models and handle sensitive user data. It also raises the stakes for Anthropic and other US model providers, whose terms of service and data-handling practices are now at the center of a geopolitical and compliance dispute. The investigation stems from Anthropic's 154-page report, which names seven Chinese companies and specifically alleges that DeepSeek forwarded a request from an engineer developing police surveillance systems to Claude. The probe is being conducted by China's internet regulator, and the companies involved have not yet issued public responses.

telegram · zaihuapd · Sep 22, 14:37

**Background**: DeepSeek is a Hangzhou-based AI company owned by the hedge fund High-Flyer, known for releasing open-weight large language models, while Moonshot AI (月之暗面) is a Beijing-based AI startup. Anthropic is the American company behind the Claude series of large language models, first released as a chatbot in March 2023. Chinese AI developers have sometimes used foreign models like Claude for tasks such as data generation or benchmarking, which can conflict with providers' terms of service and with China's data-security rules.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#data privacy`, `#DeepSeek`, `#Moonshot AI`, `#Anthropic`

---

<a id="item-12"></a>
## [DeepSeek to Brief UN Security Council on AI Risks This Week](https://t.me/zaihuapd/43989) ⭐️ 8.0/10

Two people familiar with the matter said Chinese AI startup DeepSeek will brief the 15-member UN Security Council on the risks posed by artificial intelligence this week, with OpenAI CEO Sam Altman and senior Anthropic representatives also expected to attend the Wednesday session on AI and international security. DeepSeek and Moonshot were among the Chinese AI companies invited to speak, though DeepSeek founder Liang Wenfeng does not plan to attend and the arrangements could still change. This marks a rare moment in which a Chinese AI startup shares a global governance stage with leading US AI labs, underscoring how AI safety has become a top-tier international security issue rather than a purely technical debate. It also signals the rising international profile of Chinese AI firms and could shape how future global AI rules are negotiated among major powers. The briefing is scheduled for Wednesday at the Security Council, which has 15 members, and the agenda covers AI and international security; DeepSeek founder Liang Wenfeng is not expected to attend, and the speaker lineup may still change at short notice. DeepSeek is a Hangzhou-based developer of open-weights large language models, owned and funded by the hedge fund High-Flyer.

telegram · zaihuapd · Sep 22, 17:39

**Background**: The UN Security Council is the body primarily responsible for maintaining international peace and security, and it has increasingly turned its attention to artificial intelligence as the technology's rapid advance raises concerns about misuse and loss of control. DeepSeek is a Chinese AI company known for releasing open-weights large language models, including DeepSeek-R1, which became the most downloaded free app on the US iOS App Store in early 2025. Anthropic is an American AI safety and research company, while OpenAI is the developer of ChatGPT and is led by Sam Altman.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://news.un.org/en/story/2026/09/1168414">LIVE: OpenAI and Anthropic to brief Security Council as AI ... | UN News</a></li>
<li><a href="https://cointelegraph.com/news/openai-anthropic-to-brief-un-security-council-on-ai-risks">OpenAI and Anthropic CEOs Join UN Security Council AI Briefing</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#DeepSeek`, `#UN Security Council`, `#AI safety`, `#international policy`

---

<a id="item-13"></a>
## [OpenAI Begins Limited Preview of GPT-5.6 Series: Sol, Terra, Luna](https://t.me/zaihuapd/43990) ⭐️ 8.0/10

OpenAI has begun a limited preview of its GPT-5.6 series, which includes the flagship Sol model, the balanced Terra model, and the low-cost Luna model, initially available to select trusted partners via the API and Codex. Sol emphasizes stronger coding, biology, and cybersecurity capabilities and adds new max reasoning intensity and ultra mode, while Terra is roughly twice as cheap as GPT-5.5 and Luna is positioned as the lowest-cost option. This preview signals OpenAI's continued push toward tiered model families that let developers trade off capability, speed, and cost, which could reshape how teams choose models for coding agents and production workloads. The government-requested, partner-only rollout also highlights growing scrutiny and coordination between frontier AI labs and regulators before broad public release. The three tiers are priced per 1M tokens: Sol at $5 input / $30 output, Terra at $2.50 input / $15 output, and Luna at $1 input / $6 output. OpenAI has published no parameter count or architecture description, and the preview is closed in the strict sense, with general availability planned for ChatGPT, Codex, and the API in the coming weeks.

telegram · zaihuapd · Sep 22, 18:04

**Background**: OpenAI's GPT series is its flagship family of large language models, and the company has increasingly released models in multiple size tiers so users can pick one matching their budget and performance needs. Codex is OpenAI's suite of AI-driven coding agents that automates software engineering tasks, and it is often among the first surfaces to receive new models. A limited preview means the models are available only to a small set of vetted partners before a wider launch, allowing OpenAI to gather feedback and address safety concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-gpt-5-6-sol-terra-luna-explained">What Is GPT-5.6? OpenAI's Sol, Terra, and Luna Model Tiers Explained | MindStudio</a></li>
<li><a href="https://www.reddit.com/r/codex/comments/1utzi5w/gpt56_sol_vs_terra_vs_luna_my_early_guide_to/">GPT-5.6 Sol vs Terra vs Luna: my early guide to choosing the right model without burning your limits : r/codex - Reddit</a></li>

</ul>
</details>

**Discussion**: Early Reddit discussion in r/codex suggests Sol is clearly strong but burns tokens very fast, Terra uses more of users' limits than expected, and some users question whether Terra is worth using at all. Overall sentiment is cautiously interested but concerned about cost and rate-limit consumption.

**Tags**: `#OpenAI`, `#GPT-5.6`, `#AI models`, `#API`, `#Codex`

---

<a id="item-14"></a>
## [ShinyHunters Claims Breach of FBI Employee and Applicant Data](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) ⭐️ 8.0/10

The hacking group ShinyHunters claims to have breached multiple FBI-related services and stolen data on all FBI employees and job applicants, providing 404 Media with a sample of roughly 5,000 alleged employee records. The sample reportedly includes names, home addresses, phone numbers, and details about family members such as spouses, though the FBI has not confirmed the claim. If verified, the breach could expose FBI personnel and their families to tracking, harassment, or threats, and pose serious security and counterintelligence risks to U.S. law enforcement and intelligence operations. It also highlights how even a top government agency can be compromised through third-party enterprise software, underscoring supply-chain vulnerabilities across the public sector. The sample of about 5,000 records reportedly contains personal and family details, and the stolen data is said to have come from systems accessed after an initial PeopleSoft compromise, allegedly including the FBI's AWS GovCloud environment used to store employee and applicant information. The FBI has not confirmed the breach, so the claim remains unverified.

telegram · zaihuapd · Sep 23, 05:00

**Background**: ShinyHunters is a black-hat criminal hacker and extortion group active since 2019, known for a large number of data breaches and for leaking or selling stolen databases. 404 Media is an independent technology news publication founded in 2023 by former Motherboard journalists. The FBI has suffered prior hacking incidents, including a 2021 email hack that sent fake warnings from an FBI address, so claims of this kind are taken seriously even before official confirmation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ShinyHunters">ShinyHunters - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/404_Media">404 Media - Wikipedia</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/">ShinyHunters claims FBI hack, data theft in PeopleSoft zero-day breach</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#data breach`, `#FBI`, `#ShinyHunters`, `#national security`

---