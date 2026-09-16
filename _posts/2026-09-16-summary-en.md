---
layout: default
title: "Horizon Summary: 2026-09-16 (EN)"
date: 2026-09-16
lang: en
---

> From 89 items, 11 important content pieces were selected

---

1. [TypeSafe AI Launches System One Models and Jev for Typed Inference](#item-1) ⭐️ 8.0/10
2. [E-ink frame listens for birds and draws 1800s-style illustrations](#item-2) ⭐️ 8.0/10
3. [Apple Reference Image: Cryptographic Proof for Verified Photography](#item-3) ⭐️ 8.0/10
4. [Internet Archive Adds Protections as Wayback Machine Faces Scraping Waves](#item-4) ⭐️ 8.0/10
5. [Google launches Gemini 3.8 Live and Live Extended Thinking](#item-5) ⭐️ 8.0/10
6. [Developer Builds Linux GPU Driver for M4 Mac Mini in One Month](#item-6) ⭐️ 8.0/10
7. [Strix finds exposed GitHub PAT granting admin access to Baseten's production GitHub](#item-7) ⭐️ 8.0/10
8. [Vera Rubin NVL72 Delivers 67x Better Agentic Inference Performance per Dollar](#item-8) ⭐️ 8.0/10
9. [SemiAnalysis: On-Device vs Datacenter Inference for Robot Brains](#item-9) ⭐️ 8.0/10
10. [Prior Labs releases TabPFN-3.5, new SOTA tabular foundation model](#item-10) ⭐️ 8.0/10
11. [Low-Quality Chinese Casino Sites Hide APT Command-and-Control Infrastructure](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TypeSafe AI Launches System One Models and Jev for Typed Inference](https://typesafe.ai/blog/introducing-system-one-models-and-jev) ⭐️ 8.0/10

TypeSafe AI, a San Francisco lab founded by Diogo Almeida (who previously built RLHF methods at OpenAI for ChatGPT), has emerged from stealth with $40 million in seed funding led by DCVC and launched System One Models along with its first model, Jev. Jev is a model that skips text generation entirely, instead returning typed probabilistic decisions from unstructured input, and is available in early access. This represents a novel approach to structured output generation that trades general-purpose text generation for fast, typed inference, potentially making LLM-style intelligence practical for classification, routing, scoring, and extraction tasks where hand-written logic is too brittle. The 403-comment discussion suggests strong interest in the trade-offs between general-purpose generation and specialized typed inference. According to TypeSafe, Jev is 20-200x faster and 40-400x cheaper than LLMs, and because it gives up string generation it is architecturally incapable of hallucinating. However, these headline speed and cost gains remain vendor-tested, and critics note that Jev can only generate structured output, not arbitrary code or text.

hackernews · albelfio · Sep 15, 19:25 · [Discussion](https://news.ycombinator.com/item?id=49717558)

**Background**: System One models are a class of AI models built to make fast, structured decisions that software can use directly: they evaluate a state and return typed answers and probabilities, similar to how an LLM understands natural-language input but returning typed decisions rather than text. Jev is TypeSafe's flagship model and the first System One model, trained with RLCD (Reinforcement Learning from Contrastive Data) and positioned as a frontier-intelligence function call: unstructured state in, typed probabilistic decisions out. This contrasts with conventional LLMs, which generate free-form text and can hallucinate.

<details><summary>References</summary>
<ul>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models & Jev - TypeSafe AI Blog</a></li>
<li><a href="https://docs.typesafe.ai/concepts/system-one">System One - TypeSafe AI</a></li>
<li><a href="https://www.explainx.ai/blog/typesafe-ai-jev-system-one-models-launch-2026">Jev by TypeSafe AI: 200x Faster Structured-Output Model (2026 ...</a></li>

</ul>
</details>

**Discussion**: Commenters largely found the approach genuinely interesting and new, with ymir_e highlighting contract analysis and vintermann citing genealogy matching as strong use cases, especially valuing the certainty output for flagging low-confidence results for human review. jacobgold argued the title should be 'Jev: Trading general purpose generation for fast typed inference' and questioned whether the speed comparison is misleading, since a generative model that can output code in a Turing-complete language can do anything a computer can do, while Jev can only generate structured output. cfowles said the value clicked after seeing the Home Assistant demo, and futurisold noted combining this with design-by-contract patterns could enable many new applications.

**Tags**: `#LLM`, `#structured-output`, `#typed-inference`, `#AI`, `#typesafe`

---

<a id="item-2"></a>
## [E-ink frame listens for birds and draws 1800s-style illustrations](https://github.com/arnegiacomo/fugleramme) ⭐️ 8.0/10

A developer released 'fugleramme' on GitHub, an e-ink frame that continuously listens for bird sounds, identifies species using the BirdNET classifier, and renders each detected bird as a 19th-century-style illustration on the display. The Show HN post reached 1664 points with 208 comments, sparking discussion about embedded ML and e-ink projects. The project demonstrates how existing open-source ML models like BirdNET can be combined with low-power e-ink hardware to create delightful, always-on ambient devices, inspiring other builders to pursue similar embedded ML applications. It also highlights the growing ecosystem of hobbyist e-ink and ESP32 projects that prioritize energy efficiency and single-purpose design. BirdNET is a traditional convolutional neural network designed for acoustic bird identification, not an LLM, and it processes raw audio through a multi-stage pipeline for ecological accuracy. E-ink displays only consume power when refreshing, so with a BLE driver and a 2000mAh battery, a similar setup can last years on a single charge even with multiple daily refreshes.

hackernews · arnemunthekaas · Sep 15, 12:31 · [Discussion](https://news.ycombinator.com/item?id=49711544)

**Background**: E Ink is an electronic paper display technology that reflects light like paper and only uses power when the image changes, making it ideal for low-power, always-on devices. BirdNET is an AI-powered bird sound identification system developed by the Cornell Lab of Ornithology and Chemnitz University of Technology, available as a free app and open model. Embedded machine learning refers to running ML models directly on small, low-power devices such as microcontrollers, enabling applications like this without cloud connectivity.

<details><summary>References</summary>
<ul>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://en.wikipedia.org/wiki/E_Ink">E Ink - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Embedded_Machine_Learning">Embedded Machine Learning</a></li>

</ul>
</details>

**Discussion**: Commenters overwhelmingly praised the project as magical and inspiring, with one noting it was the coolest thing on HN in a while. A commenter clarified that BirdNET is a traditional neural network rather than an LLM, and another shared a replication attempt on FrameOS, while a third described long-lasting BLE e-ink setups that run for years on a single charge.

**Tags**: `#e-ink`, `#embedded-systems`, `#bird-classification`, `#hardware`, `#machine-learning`

---

<a id="item-3"></a>
## [Apple Reference Image: Cryptographic Proof for Verified Photography](https://security.apple.com/blog/apple-reference-image/) ⭐️ 8.0/10

Apple introduced Apple Reference Image, an opt-in camera mode on the iPhone 18 Pro series that cryptographically proves a photograph depicts a real event and has not been tampered with. The system is detailed in a new Apple Security blog post titled "Apple Reference Image: A New Approach for Verified Photography." This is a significant technical development with major privacy and security implications, potentially shifting verified photography from an open industry standard to a proprietary Apple-controlled system. It could affect journalists, insurance and identity-verification apps, and raise concerns about requiring an iPhone to participate in normal civic and commercial life. Reference Image works only with the iPhone 18 Pro's main camera, so photos taken with the ultrawide and telephoto cameras cannot be verified the same way. The system requires uploading every verified "developed" image to Apple's servers and relies on many closed-source components, which critics say makes trust and auditing difficult.

hackernews · imwally · Sep 16, 02:07 · [Discussion](https://news.ycombinator.com/item?id=49721322)

**Background**: Cryptographic image provenance aims to verify a digital image's origin and edit history using signatures and metadata, similar to the C2PA Content Credentials standard backed by Adobe, The New York Times, and others. Apple's approach differs by tying verification to specific capture hardware and Apple's own infrastructure rather than an open cross-vendor standard.

<details><summary>References</summary>
<ul>
<li><a href="https://9to5mac.com/2026/09/15/apple-explains-how-the-iphone-18-pros-new-reference-image-camera-mode-works/">Apple explains how the iPhone 18 Pro’s new Reference Image ...</a></li>
<li><a href="https://www.androidauthority.com/apple-reference-image-vs-android-c2pa-3711734/">Apple claims iPhone 18 Pro's camera is more... - Android Authority</a></li>
<li><a href="https://c2pa.org/">C 2 PA | Verifying Media Content Sources</a></li>

</ul>
</details>

**Discussion**: Commenters were highly critical: some noted the system doesn't address replay attacks, where a photo of an edited image displayed on a monitor could still receive a valid Apple Reference signature. Others objected to the complexity, closed-source trust requirements, mandatory uploads to Apple's servers, and the risk that a "certified real" tag would lead people to accept misleading narratives at face value.

**Tags**: `#Apple`, `#photo-verification`, `#cryptography`, `#privacy`, `#security`

---

<a id="item-4"></a>
## [Internet Archive Adds Protections as Wayback Machine Faces Scraping Waves](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) ⭐️ 8.0/10

The Internet Archive reported that its Wayback Machine has been hit by waves of high-volume automated scraping traffic, forcing it to deploy new protections to keep the service running. The organization believes much of this traffic comes from scrapers trying to bypass blocks on original sites by pulling archived copies instead. The Internet Archive is critical public infrastructure for web preservation, and sustained scraping pressure threatens the availability of a free, open resource used by journalists, researchers, and Wikipedia editors. If sites respond by opting out of archiving, the historical record of the web could shrink for everyone. The Archive says it has put protections in place but has not detailed them, and service has been inconsistent while remaining accessible, including anonymously via Tor without a centralized gatekeeper. Some sites have already opted out of archiving in response to the scraping.

hackernews · ChrisArchitect · Sep 15, 17:52 · [Discussion](https://news.ycombinator.com/item?id=49716176)

**Background**: The Wayback Machine is a digital archive of the World Wide Web launched for public access on October 25, 2001, by the Internet Archive, a San Francisco-based nonprofit founded in 1996 by Brewster Kahle. It lets users view historical snapshots of websites and, as of October 2025, has archived more than 1 trillion web pages and well over 99 petabytes of data. Web scraping refers to automated bots collecting data at mass scale, and in the mid-2020s scrapers operated by LLM vendors became a major source of web traffic, often using distributed crawling to avoid detection.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wayback_Machine">Wayback Machine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Internet_Archive">Internet Archive</a></li>
<li><a href="https://en.wikipedia.org/wiki/Web_scraping">Web scraping - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters widely praised the Archive as vital open infrastructure and urged donations, with simonw arguing the traffic likely comes from scrapers circumventing blocks on original sites. Others shared personal stories of recovering lost early-2000s content, while one user noted persistent 429 errors from a work computer but not a phone, suggesting the protections may affect some legitimate users unevenly.

**Tags**: `#internet-archive`, `#web-scraping`, `#open-access`, `#digital-preservation`, `#infrastructure`

---

<a id="item-5"></a>
## [Google launches Gemini 3.8 Live and Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) ⭐️ 8.0/10

Google announced Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking, described as its most advanced live dialogue models yet, built for natural real-time conversation. The Extended Thinking variant is a high-reasoning audio-to-audio model that captures the #1 spot on Artificial Analysis' Speech to Speech Quality Index with a score of 82.6. The release pushes real-time voice AI toward enterprise-grade reliability, with the Extended Thinking model leading agentic task completion benchmarks (68.6% on τ-Voice and 35.1% on Sierra's benchmark). This matters for developers and businesses building latency-sensitive, high-volume voice agents, and it intensifies competition with other frontier model providers. The models are positioned as cost-efficient and fast, optimized for high-volume, latency-sensitive tasks such as real-time dialogue, and are part of the natively multimodal Gemini 3 series. The Extended Thinking variant is specifically recommended when higher background reasoning is needed for complex, multi-step problem solving during live voice interactions.

hackernews · leumon · Sep 15, 17:38 · [Discussion](https://news.ycombinator.com/item?id=49715947)

**Background**: Gemini is Google's flagship family of multimodal AI models, and the 'Live' line refers to models designed for real-time, speech-to-speech conversation rather than text-only chat. 'Extended Thinking' denotes a mode where the model performs additional background reasoning before responding, trading some latency for better accuracy on complex tasks. The release follows Google's recent Gemini 3.8 Flash and 3.8 Flash Cyber models, continuing a rapid cadence of Gemini 3-series launches.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Gemini 3 . 8 Live & Gemini 3 . 8 Live Extended Thinking</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-audio/">Gemini 3.8 Audio (Live, Live Extended Thinking) - Model Card — Google DeepMind</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking">Gemini 3 . 8 Live Extended Thinking | Gemini API | Google AI for...</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were divided: some praised the model's low latency, pleasant voices, and strong handling of accented speech and niche languages like Afrikaans, while others reported issues with context loss and unrequested product links. Several users also questioned why Google still trails competitors like Fable and Astra despite its data, TPU hardware, and advertising resources.

**Tags**: `#Gemini`, `#Google`, `#AI`, `#LLM`, `#Model Release`

---

<a id="item-6"></a>
## [Developer Builds Linux GPU Driver for M4 Mac Mini in One Month](https://codyho.dev/blog/gpu-driver/) ⭐️ 8.0/10

A developer built a working Linux GPU driver for the M4 Mac Mini in about one month, according to a blog post that sparked extensive discussion on Hacker News. The achievement is notable because the M4 is a newer Apple Silicon generation that previously lacked GPU acceleration under Linux. This could significantly accelerate Linux support for newer Apple Silicon hardware, where GPU acceleration has been a major pain point, especially for M3 and later chips. It also fuels debate about whether LLM-assisted reverse engineering can replace years of manual effort and how such contributions should be treated by upstream projects. The author was reportedly banned from Asahi Linux for hiding extensive LLM use in a prior contribution and for concealing that he is a former Apple engineer with direct contacts in Apple Silicon development. Asahi Linux has a strict no-AI policy, which likely prevents this driver from being upstreamed into the Linux kernel.

hackernews · ADevWithAnIdea · Sep 15, 19:30 · [Discussion](https://news.ycombinator.com/item?id=49717638)

**Background**: Apple Silicon Macs use custom ARM-based chips whose GPU architecture is undocumented, so Linux support requires reverse engineering. The Asahi Linux project has led this effort, but its GPU driver work has focused on older M1 and M2 generations and has faced slowdowns. LLMs are increasingly used in reverse engineering to help understand binary code and hardware behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49717638">Building a Linux GPU Driver for the M4 Mac Mini in... | Hacker News</a></li>
<li><a href="https://www.phoronix.com/news/Asahi-Lina-Steps-Down-Linux-GPU">Asahi Lina Pausing Work On Apple GPU Linux Driver Development</a></li>
<li><a href="https://www.linuxencaja.net/en/asahi-lina-pauses-development-of-linux-gpu-driver-for-apple/">Asahi Lina suspends development of Linux GPU driver for Apple</a></li>

</ul>
</details>

**Discussion**: Commenters were impressed by the speed of the achievement and saw it as a strong use case for LLMs in reverse engineering, though some raised ethical concerns about the author's concealed LLM use and former Apple employment. Others noted that Asahi Linux's no-AI policy means this work likely cannot be upstreamed, potentially leading to AI-assisted forks.

**Tags**: `#Linux`, `#GPU driver`, `#Apple Silicon`, `#reverse engineering`, `#LLM`

---

<a id="item-7"></a>
## [Strix finds exposed GitHub PAT granting admin access to Baseten's production GitHub](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) ⭐️ 8.0/10

Strix, an AI penetration testing platform, discovered an exposed GitHub Personal Access Token (PAT) and a public container image that together granted admin access to Baseten's production GitHub organization. Baseten confirmed the report, immediately invalidated the leaked key, removed the public Harbor container image, and stated that logs show no exploitation or customer data exposure. This incident highlights how a single exposed credential can cascade into full administrative control over a company's production code repositories, and it fuels the ongoing debate about whether AI agents meaningfully improve vulnerability discovery or simply automate what a motivated human could already find. It also raises questions about the ethics and rules of engagement when AI security tools are pointed at prospective vendors without prior negotiation. The disclosure timeline shows Strix reported the live basetenbot token, the public Harbor project, and repository permissions on July 13 at 11:10 PM; Baseten made the Harbor project private the next morning but the token still worked until Baseten Security confirmed the issue as critical and rotated the token on July 14 at 4:34 PM. Baseten also asked Strix to securely delete the images they had pulled, and community members questioned whether running Strix against a prospective vendor's domain was negotiated in advance.

hackernews · bearsyankees · Sep 15, 18:11 · [Discussion](https://news.ycombinator.com/item?id=49716476)

**Background**: Baseten is an AI infrastructure company that provides an inference platform for deploying and scaling open-source and custom AI models in production. A GitHub Personal Access Token (PAT) is a credential that allows programmatic access to GitHub repositories and organizations; if exposed publicly, it can let attackers read, modify, or administer code and CI/CD pipelines. Strix is an open-source AI penetration testing tool that uses autonomous agents to dynamically run code, find vulnerabilities, and validate them with proofs-of-concept, similar in spirit to manual red-teaming but automated.

<details><summary>References</summary>
<ul>
<li><a href="https://www.baseten.co/">Inference Platform: Deploy AI models in production | Baseten</a></li>
<li><a href="https://github.com/usestrix/strix">GitHub - usestrix/strix: Open-source AI penetration testing ...</a></li>
<li><a href="https://www.csoonline.com/article/4103717/github-action-secrets-arent-secret-anymore-exposed-pats-now-a-direct-path-into-cloud-environments-2.html">GitHub Action Secrets aren’t secret anymore: exposed PATs now a direct path into cloud environments | CSO Online</a></li>

</ul>
</details>

**Discussion**: Baseten's Philip Kiely confirmed the coordinated remediation and thanked Strix for responsible disclosure, noting no exploitation or data exposure. Commenters like ivraatiems argued the value of AI agents is speed rather than finding things humans couldn't, while SaucyWrong questioned whether Strix had permission to test a prospective vendor and raised rules-of-engagement concerns. Overall sentiment was positive about Baseten's response but skeptical about the novelty and ethics of AI-driven security research.

**Tags**: `#security`, `#vulnerability-disclosure`, `#cloud-security`, `#ai-agents`, `#responsible-disclosure`

---

<a id="item-8"></a>
## [Vera Rubin NVL72 Delivers 67x Better Agentic Inference Performance per Dollar](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-agentic-inference) ⭐️ 8.0/10

SemiAnalysis reports that NVIDIA's Vera Rubin NVL72 rack-scale platform achieves 67x better performance per dollar for agentic inference workloads, based on its new AgentX benchmark built from recorded real-world agentic coding sessions. NVIDIA separately highlights SemiAnalysis AgentX data showing the system delivers up to 30x higher throughput per megawatt than GB300 NVL72 on the same agentic workloads. The claim reframes AI infrastructure economics around profit per gigawatt rather than raw FLOPS, which directly affects how data center operators and hyperscalers plan power-constrained buildouts. If the numbers hold, agentic inference could become dramatically cheaper per unit of useful work, shifting purchasing decisions toward NVIDIA's next-generation rack platform. Vera Rubin NVL72 unites 36 Vera CPUs and 72 Rubin GPUs in a third-generation MGX rack design, delivering 3.6 exaFLOPS of AI performance and 75TB of memory with cable-free modularity for rapid deployment. The AgentX workload preserves real context growth, tool calls, and sub-agent spawning, making it more representative than earlier fixed-sequence benchmarks such as 8k1k or 1k1k.

rss · Semianalysis · Sep 14, 22:08

**Background**: Agentic inference refers to the multi-step work an AI agent performs while reading files, calling tools, revisiting context, and producing changes, rather than a single prompt-response exchange. SemiAnalysis's InferenceX is an open-source, Apache-2.0 automated benchmark suite, and AgentX is its newer scenario that replaces single-turn traffic with agentic coding traffic. NVIDIA's NVL72 rack-scale systems integrate CPUs and GPUs into one coherent unit to serve very large models efficiently.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/">Up to 30x More Work Per Watt: NVIDIA Vera Rubin NVL72 Sets a New Efficiency Standard for AI Agents</a></li>
<li><a href="https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat">AgentX - InferenceXv3: Does CUDA Moat Hold up in Agentic ...</a></li>
<li><a href="https://servers.asus.com/glossary/What-is-NVIDIA-Vera-Rubin-NVL72">What is NVIDIA Vera Rubin NVL72? | ASUS Servers</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#AI Hardware`, `#Inference`, `#Performance`, `#Data Center Economics`

---

<a id="item-9"></a>
## [SemiAnalysis: On-Device vs Datacenter Inference for Robot Brains](https://newsletter.semianalysis.com/p/a-brain-too-big-to-carry-on-device) ⭐️ 8.0/10

SemiAnalysis published an in-depth analysis titled "A Brain Too Big to Carry — On-Device vs Datacenter Inference," examining whether robot foundation models should run locally on edge silicon or be offloaded to datacenter GPUs over wireless links. The piece compares silicon and DRAM efficiency, Jetson Thor versus B300 total cost of ownership, real-world deployments, and the network constraints that shape the decision. As robots move from labs to factory floors and homes, this architecture choice determines hardware cost, latency, and reliability for the entire generalist robotics industry. The analysis suggests the answer depends on fleet size, network conditions, and how much intelligence a task demands, which could reshape how robotics companies design their compute stacks. For a fleet of 96 robots, aggregate TCO is reported at $14.97/hr for on-device Jetson Thor, $15.61/hr for RTX 6000 Pro offload, and $18.63/hr for B300 datacenter inference. Boston Dynamics reportedly offloads its System 2 planner to Google TPUs because models at hundreds of billions to a trillion parameters are too large to run on the robot itself.

rss · Semianalysis · Sep 14, 16:37

**Background**: Robot foundation models are increasingly split into fast reactive "System 1" policies and slower deliberative "System 2" planners, mirroring dual-process theories of cognition. Unlike cloud language models where compute scales flexibly, robotics inverts the design paradigm: the robot must act in the physical world with hard latency and safety constraints, so engineers must decide whether to carry heavy edge silicon or depend on a reliable low-latency network link. On-device inference avoids connectivity risk but limits model size, while datacenter offload enables larger models at the cost of bandwidth, latency, and network reliability.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/a-brain-too-big-to-carry-on-device">Where Does a Robot Think — On-Device vs Datacenter Inference</a></li>
<li><a href="https://aiweekly.co/alerts/boston-dynamics-runs-robot-brains-on-tpus-rivals-stay-on-jetson">Boston Dynamics runs robot brains on TPUs; rivals stay on Jetson</a></li>
<li><a href="https://news.lavx.hu/article/where-does-a-robot-think-on-device-vs-datacenter-inference">Where Does a Robot Think — On-Device vs Datacenter Inference</a></li>

</ul>
</details>

**Tags**: `#AI inference`, `#edge computing`, `#robotics`, `#hardware`, `#TCO`

---

<a id="item-10"></a>
## [Prior Labs releases TabPFN-3.5, new SOTA tabular foundation model](https://www.reddit.com/r/MachineLearning/comments/1wh4xhy/tabpfn35_is_released_as_the_next_sota_tabular/) ⭐️ 8.0/10

Prior Labs released TabPFN-3.5, a new tabular foundation model that tops both the TabArena and BeyondArena benchmarks and is claimed to be SOTA for datasets with up to 1M rows and 20k features. It ships in three variants: TabPFN-3.5-Fast (alpha, 6x faster than the base model), TabPFN-3.5-Thinking (API-only, trades compute for accuracy), and TabPFN-3.5-Plus. Tabular data remains the dominant format in enterprise and scientific settings, so a stronger foundation model here can directly replace gradient-boosted trees in many real-world pipelines. The +250 Elo gain over the strongest previous baseline on BeyondArena suggests foundation models are finally becoming competitive on the harder, non-IID tabular tasks where trees have historically dominated. On BeyondArena, TabPFN-3.5 leads on text-rich, high-cardinality, and high-dimensional data, beating the previous overall leader by +150 Elo, while TabPFN-3.5-Thinking adds +20 Elo over the base model on BeyondArena and +44 Elo on TabArena. The Fast variant is still in alpha, and the Thinking variant is only accessible through the API rather than as downloadable weights.

reddit · r/MachineLearning · /u/tuanacelik · Sep 15, 16:18

**Background**: TabPFN is a transformer-based foundation model from Prior Labs that solves tabular prediction problems via in-context learning in a single forward pass, rather than requiring per-dataset training like XGBoost or CatBoost. TabArena is a living benchmark for IID tabular machine learning that continuously adds curated datasets and well-implemented models, while BeyondArena extends this to non-IID settings including temporal and grouped tasks across a wide range of dataset sizes and dimensionalities. Elo ratings are used in these leaderboards to express relative model strength in a way similar to chess rankings.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/PriorLabs/TabPFN">GitHub - PriorLabs/ TabPFN : TabPFN : Foundation Model for Tabular ...</a></li>
<li><a href="https://arxiv.org/abs/2506.16791">TabArena : A Living Benchmark for Machine Learning on Tabular Data</a></li>
<li><a href="https://aiweekly.co/alerts/beyondarena-finds-trees-still-beat-tabular-fms-off-iid-data">BeyondArena finds trees still beat tabular FMs off-IID data | AI Weekly</a></li>

</ul>
</details>

**Tags**: `#tabular-data`, `#foundation-models`, `#machine-learning`, `#benchmarking`, `#SOTA`

---

<a id="item-11"></a>
## [Low-Quality Chinese Casino Sites Hide APT Command-and-Control Infrastructure](https://www.theregister.com/security/2026/09/15/low-quality-casino-sites-conceal-highly-dangerous-threat-actors/5296652) ⭐️ 8.0/10

Security researchers have identified roughly 1.7 million Chinese-language casino and adult websites, some of which are being used as covert command-and-control (C2) infrastructure by China-linked APT groups. Since 2023, these actors have used a JScript-based framework called "PeckBirdy" to hide malware C2 domains inside low-quality gambling sites and lure victims into downloading malware through fake software updates. This technique lets attackers blend malicious traffic into ordinary-looking gambling site visits, making detection and attribution significantly harder for defenders. It also risks causing security teams to misclassify C2 traffic as employee policy violations rather than active intrusions, potentially delaying incident response. PeckBirdy is a script-based framework implemented in JScript that can run in browsers, MSHTA, WScript, Classic ASP, Node JS, and .NET ScriptControl environments, giving it broad flexibility for LOLBins-style exploitation. Because the hosting sites closely resemble legitimate gambling sites, defenders may overlook the associated traffic as benign or non-compliant user behavior.

telegram · zaihuapd · Sep 16, 07:31

**Background**: Command-and-control (C2) infrastructure is the set of tools and channels attackers use to maintain communication with compromised devices after initial exploitation. Advanced persistent threats (APTs) are sophisticated, long-term cyberattacks typically conducted by highly skilled, often nation-state-backed actors. By hosting C2 domains on seemingly innocuous casino sites, attackers exploit the fact that such traffic is common and rarely scrutinized, complicating both detection and attribution.

<details><summary>References</summary>
<ul>
<li><a href="https://www.trendaisecurity.com/en-gb/resources-insights/trendai-security-blog/peckbirdy-script-framework">PeckBirdy : A Versatile Script Framework for LOLBins Exploitation...</a></li>
<li><a href="https://www.scworld.com/brief/peckbirdy-framework-used-by-china-linked-apts-targets-gambling-and-government-entities">PeckBirdy framework used by China-linked APTs targets gambling...</a></li>
<li><a href="https://www.varonis.com/blog/what-is-c2">What is C2? Command and Control Infrastructure Explained</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#APT`, `#malware`, `#threat-intelligence`, `#C2-infrastructure`

---