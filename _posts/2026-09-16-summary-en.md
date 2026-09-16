---
layout: default
title: "Horizon Summary: 2026-09-16 (EN)"
date: 2026-09-16
lang: en
---

> From 87 items, 13 important content pieces were selected

---

1. [Typesafe.ai Launches System One Models and Jev for Fast Typed Inference](#item-1) ⭐️ 8.0/10
2. [E-ink frame listens for birds and draws 1800s-style illustrations](#item-2) ⭐️ 8.0/10
3. [Internet Archive Adds Protections as Wayback Machine Faces Scraping Surge](#item-3) ⭐️ 8.0/10
4. [Google launches Gemini 3.8 Live and 3.8 Live Extended Thinking](#item-4) ⭐️ 8.0/10
5. [AI agent finds Baseten production GitHub admin token in 25 minutes](#item-5) ⭐️ 8.0/10
6. [Ex-Apple Engineer Builds M4 Mac Mini Linux GPU Driver in One Month Using LLMs](#item-6) ⭐️ 8.0/10
7. [Bruce Schneier: 25 Years of Mass Surveillance Has Failed](#item-7) ⭐️ 8.0/10
8. [SemiAnalysis: Vera Rubin NVL72 Delivers 67x Better Agentic Inference Performance per Dollar](#item-8) ⭐️ 8.0/10
9. [44M-parameter ternary LLM runs at 1,900 tok/s on CPU in 19.8 MB](#item-9) ⭐️ 8.0/10
10. [Prior Labs releases TabPFN-3.5, new SOTA tabular foundation model](#item-10) ⭐️ 8.0/10
11. [China's 15th Five-Year Plan Targets Advanced Chips and OpenHarmony](#item-11) ⭐️ 8.0/10
12. [US and UK Lawmakers Push Bills to Ban Superintelligent AI](#item-12) ⭐️ 8.0/10
13. [Google Opens Anthropic's Claude Opus 5 to All Engineers](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Typesafe.ai Launches System One Models and Jev for Fast Typed Inference](https://typesafe.ai/blog/introducing-system-one-models-and-jev) ⭐️ 8.0/10

Typesafe.ai has launched System One Models and Jev, a fast typed inference system that trades general-purpose generation for speed and structured output, as announced on their blog. The launch quickly gained traction on Hacker News with 819 upvotes and 270 comments, indicating strong community interest. This approach could significantly lower the cost and latency of structured output tasks like classification and real-time decision-making, making previously infeasible projects viable. It also highlights a trend of distilling common use cases from frontier LLMs into smaller, faster specialized models. Jev is designed for machine-to-machine execution, targeting compliance pipelines, real-time decisions, and autonomous agents, and is trained using RLCD (Reinforcement Learning from Community Data or similar). It only generates structured output, so it cannot perform general-purpose generation like a Turing-complete code model.

hackernews · albelfio · Sep 15, 19:25 · [Discussion](https://news.ycombinator.com/item?id=49717558)

**Background**: Typed inference refers to generating outputs that conform to a predefined schema or type, ensuring structural validity without post-processing. System One Models are a new class of AI designed for fast, intuitive reasoning, as opposed to slower, more deliberate System Two thinking. Typesafe.ai is a stealth AI lab focused on building reliable, production-grade AI workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models and Jev</a></li>
<li><a href="https://news.ycombinator.com/item?id=49717558">Introducing System One Models and Jev | Hacker News</a></li>
<li><a href="https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds">Mini-Vibe Check: TypeSafe's Jev Judged Everything I’ve Written in 0.7 Seconds</a></li>

</ul>
</details>

**Discussion**: Community reaction is largely positive, with users praising the novelty and potential for classification and memory systems. Some question the misleading speed comparison, noting that general-purpose models can do anything while Jev is limited to structured output. Others highlight the distillation angle, suggesting Typesafe can cheaply extract common tasks from frontier LLMs and serve them faster.

**Tags**: `#AI/ML`, `#typed inference`, `#model distillation`, `#structured output`, `#Hacker News`

---

<a id="item-2"></a>
## [E-ink frame listens for birds and draws 1800s-style illustrations](https://github.com/arnegiacomo/fugleramme) ⭐️ 8.0/10

Developer Arne Munthe-Kaas (arnegiacomo) released 'fugleramme' on GitHub, an e-ink picture frame built with an ESP32 microcontroller and the BirdNET sound-classification model that listens for bird calls and displays matching 1800s-style illustrations. The project was shared as a Show HN post and quickly drew enthusiastic community attention. The project shows how cheap microcontrollers and existing bioacoustics AI can be combined into a delightful, low-power ambient device, inspiring other makers to build 'magical' everyday objects. It also highlights the growing wave of bird-monitoring projects and the maturity of BirdNET as an accessible, non-LLM neural network for real-world sound classification. The frame runs on an ESP32, a low-cost dual-core Wi-Fi/Bluetooth microcontroller from Espressif, and uses BirdNET, a traditional neural network (not an LLM) developed for acoustic bird identification. E-ink displays only consume power when the image changes, which makes them well suited to a device that refreshes occasionally when a new bird is detected.

hackernews · arnemunthekaas · Sep 15, 12:31 · [Discussion](https://news.ycombinator.com/item?id=49711544)

**Background**: BirdNET is a widely used AI system from the Cornell Lab of Ornithology and Chemnitz University of Technology that identifies bird species from sound recordings, and it is available as a free phone app. E-ink (e-paper) displays mimic ink on paper and hold an image without power, making them popular for low-power, always-on devices. The ESP32 is a common hobbyist microcontroller that provides Wi-Fi and Bluetooth connectivity at a very low cost.

<details><summary>References</summary>
<ul>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://en.wikipedia.org/wiki/ESP32">ESP32 - Wikipedia</a></li>
<li><a href="https://jiclcd.com/what-is-e-ink-display-technology/">What Is E - Ink Display Technology ? Complete Guide to E-Paper...</a></li>

</ul>
</details>

**Discussion**: Commenters were highly enthusiastic, with one calling it 'the coolest thing on HN' and praising its magical feel; others noted that BirdNET is a traditional neural network rather than an LLM, shared their own e-ink projects and battery-life calculations, and linked related bird-monitoring efforts like birdnet-go.

**Tags**: `#e-ink`, `#ESP32`, `#bird-classification`, `#hardware`, `#Show HN`

---

<a id="item-3"></a>
## [Internet Archive Adds Protections as Wayback Machine Faces Scraping Surge](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) ⭐️ 8.0/10

The Internet Archive published a blog update on September 15, 2026, stating that the Wayback Machine has been hit by waves of high-volume automated traffic and that new protections have been put in place to keep the service running. The Archive attributes the surge to scrapers trying to circumvent blocks on original sites by pulling content from Wayback Machine copies instead. The Internet Archive is widely treated as critical public infrastructure for digital preservation, so sustained scraping pressure threatens free, anonymous access to the historical web for researchers, journalists, and ordinary users. The incident also highlights a growing tension between AI-driven data harvesting and the nonprofit services that preserve the open web. The protective measures have caused inconsistent service and rate-limiting errors such as HTTP 429 for some users, and the Archive notes that some sites have already opted out of being archived as a result of the scraping behavior. Community members report being blocked from one network while succeeding from another, suggesting the filtering is at least partly IP- or network-based.

hackernews · ChrisArchitect · Sep 15, 17:52 · [Discussion](https://news.ycombinator.com/item?id=49716176)

**Background**: The Internet Archive is a nonprofit digital library that preserves snapshots of the public web through its Wayback Machine, which contains hundreds of billions of archived pages. Its crawlers automatically collect much of this material, and the service is normally free to use without login. High-volume scraping tools and commercial scraping APIs can generate enormous request loads, which is why the Archive must now throttle or filter traffic to stay online.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Internet_Archive">Internet Archive - Wikipedia</a></li>
<li><a href="https://github.com/sangaline/wayback-machine-scraper">GitHub - sangaline/wayback-machine-scraper: A command-line utility and Scrapy middleware for scraping time series data from Archive.org's Wayback Machine. · GitHub</a></li>
<li><a href="https://www.proxyrack.com/blog/how-to-safely-scrape-data-from-wayback-machine/">How To Safely Scrape Data From Wayback Machine</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters largely praised the Archive's resilience and commitment to open, anonymous access, with some noting they can still reach it via Tor without a centralized gatekeeper. Others suggested paid donation tiers for higher rate limits, shared confusing experiences with 429 errors on some networks but not others, and argued that AI companies profiting from scraped data should pay the Archive for access.

**Tags**: `#internet-archive`, `#wayback-machine`, `#web-scraping`, `#digital-preservation`, `#infrastructure`

---

<a id="item-4"></a>
## [Google launches Gemini 3.8 Live and 3.8 Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) ⭐️ 8.0/10

Google announced Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking, described as its most advanced live dialogue models yet, with general availability on September 15, 2026. Gemini 3.8 Live delivers fast, fluid real-time voice conversations with visual and language support, while the Extended Thinking variant adds higher background reasoning for complex, multi-step tasks during live voice interactions. This release pushes real-time voice AI closer to natural human conversation, letting models handle reasoning and tool use in the background without interrupting the dialogue. It matters for users of Gemini Live, Gmail and other Google products, and raises the competitive bar against rival live-audio models from OpenAI and others. Gemini 3.8 Live is built on Gemini 3 Pro with a 128K context window, support for 97 languages, and audio output priced at $0.018 per minute. The Extended Thinking variant is recommended when higher background reasoning is needed for complex, multi-step problem solving during real-time voice interactions.

hackernews · leumon · Sep 15, 17:38 · [Discussion](https://news.ycombinator.com/item?id=49715947)

**Background**: Gemini is Google's flagship family of large language models, and the "Live" line refers to its audio-to-audio API models designed for real-time spoken conversation rather than text chat. "Extended Thinking" is Google's term for models that spend extra compute on internal reasoning before answering, a pattern popularized by reasoning-focused LLMs. These models can manage tools and visual context in the background while the user keeps talking.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Gemini 3 . 8 Live & Gemini 3 . 8 Live Extended Thinking</a></li>
<li><a href="https://9to5google.com/2026/09/15/gemini-3-8-live-announced/">Gemini 3 . 8 Live Extended Thinking powers Gemini Live , Gmail</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking">Gemini 3 . 8 Live Extended Thinking | Gemini API | Google AI for...</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were largely positive about the release: one praised its handling of a thick accent, pleasant voices, low latency and finally working on a workspace account, while another said Gemini produces the only prose that is bearable to read. A user of the niche language Afrikaans called the live chat and grammar lessons phenomenal, though others questioned when Gemini would beat rivals like Fable and Astra, and one criticized a demo video showing the model losing to a common chess checkmate pattern.

**Tags**: `#AI`, `#Gemini`, `#Google`, `#LLM`, `#Model Release`

---

<a id="item-5"></a>
## [AI agent finds Baseten production GitHub admin token in 25 minutes](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) ⭐️ 8.0/10

An AI-powered penetration testing agent from Strix discovered a live GitHub personal access token for the account 'basetenbot' that had admin and push access to Baseten's main product repository, GitOps cluster repository, and Homebrew tap, within 25 minutes of starting its scan. The token was found in Docker build history after the agent located a public Baseten image repository, and Baseten confirmed the issue as critical, made the Harbor project private, and rotated the token the following day. This incident demonstrates that autonomous AI agents can rapidly uncover exposed secrets that humans might overlook, highlighting a growing supply chain security risk for companies that embed credentials in container build artifacts. It also fuels the debate over whether such agents represent a fundamental shift in penetration testing or simply automate tasks that motivated humans could already perform. The exposed token granted read/write access to other private repositories, including customer-specific ones, and was found in Docker build history rather than in source code. Baseten responded within about 17 hours, confirming the issue as critical, making the Harbor project private, and rotating the token, while also asking Strix to securely delete the images they had pulled.

hackernews · bearsyankees · Sep 15, 18:11 · [Discussion](https://news.ycombinator.com/item?id=49716476)

**Background**: Baseten is an AI inference platform for deploying and operating open-source, custom, and fine-tuned models in production. GitHub personal access tokens (PATs) are an alternative to passwords for authenticating to GitHub APIs, command line, or integrations, and if exposed they can grant broad repository access. Strix is an AI-powered penetration testing agent that autonomously performs reconnaissance, exploitation, and reporting, similar to other emerging tools like HackerAI and Cyberstrike.

<details><summary>References</summary>
<ul>
<li><a href="https://www.baseten.co/">Inference Platform : Deploy AI models in production | Baseten</a></li>
<li><a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens">Managing your personal access tokens - GitHub Docs</a></li>
<li><a href="https://www.linkedin.com/pulse/man-machine-future-penetration-testing-ai-agents-louis-sin-kpcuc">“Man + Machine: The Future of Penetration Testing with AI Agents ”</a></li>

</ul>
</details>

**Discussion**: Commenters largely praised Baseten's swift response but debated the novelty of the agent's findings, with some arguing that the power of such agents lies in speed rather than finding things humans couldn't. Others questioned the legality of the unauthorized testing, while several saw it as effective marketing for Strix.

**Tags**: `#security`, `#AI agents`, `#penetration testing`, `#GitHub`, `#supply chain`

---

<a id="item-6"></a>
## [Ex-Apple Engineer Builds M4 Mac Mini Linux GPU Driver in One Month Using LLMs](https://codyho.dev/blog/gpu-driver/) ⭐️ 8.0/10

An ex-Apple engineer named Cody Ho, working with a collaborator called Niklas, reverse engineered Apple's AGX GPU firmware ABI and user-space components in about one month and produced an OpenGL ES 3.0 conformant Linux GPU driver for the M4 Mac Mini, fast enough to run Minecraft at around 200fps. The work relied heavily on LLM assistance, a process that normally takes years of manual reverse engineering. This could dramatically accelerate Linux GPU support for newer Apple Silicon chips like the M3 and M4, which have long lacked GPU acceleration under Asahi Linux. It also serves as a high-profile test case for whether LLM-assisted reverse engineering can be accepted into major open-source projects, given Asahi Linux's strict no-AI policy. The driver is OpenGL ES 3.0 conformant and reportedly runs Minecraft at 212fps on the M4 Mac Mini, but it cannot currently be upstreamed into Asahi Linux because of that project's no-AI policy. The author was previously banned from Asahi Linux for concealing extensive LLM use and his status as a former Apple engineer with direct contacts to Apple Silicon developers.

hackernews · ADevWithAnIdea · Sep 15, 19:30 · [Discussion](https://news.ycombinator.com/item?id=49717638)

**Background**: Asahi Linux is a community project that reverse engineers Apple Silicon hardware to run Linux on modern Macs, and its GPU drivers for M1 and M2 chips took years of manual work. Apple's GPU, internally called AGX, has an undocumented firmware ABI and user-space components that must be reverse engineered to build open-source drivers. LLMs are increasingly used to assist such low-level reverse engineering, but many open-source projects, including Asahi Linux, ban AI-generated contributions for legal and ethical reasons.

<details><summary>References</summary>
<ul>
<li><a href="https://codyho.dev/blog/gpu-driver/">I Came, I Prompted, I Left Part 2: Building a GPU Driver ... — Cody Ho</a></li>
<li><a href="https://asahilinux.org/2022/12/gpu-drivers-now-in-asahi-linux/">Apple GPU drivers now in Asahi Linux - Asahi Linux</a></li>
<li><a href="https://zerohour.day/item/d0b9509c549f79d6c25dd760e89742a7f807263e">Building a Linux GPU Driver for the M4 Mac Mini in One Month</a></li>

</ul>
</details>

**Discussion**: Commenters widely praised the technical feat, with one calling it one of the best use cases for LLMs since it removes years of manual reverse engineering. However, many raised ethical and legal concerns: the author's ex-Apple status and concealed LLM use create a conflict of interest, and Asahi Linux's no-AI policy likely blocks upstreaming, leading some to predict AI-assisted forks will dominate while purists stick to older hardware.

**Tags**: `#Linux`, `#GPU driver`, `#Apple Silicon`, `#LLM`, `#Asahi Linux`

---

<a id="item-7"></a>
## [Bruce Schneier: 25 Years of Mass Surveillance Has Failed](https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html) ⭐️ 8.0/10

Bruce Schneier published a blog post titled "25 Years of Mass Surveillance Is Enough," arguing that a quarter-century of mass surveillance programs have failed to deliver the promised security benefits while steadily eroding civil liberties. The post sparked a large Hacker News discussion with 812 points and 293 comments debating privacy, decentralization, and policy reform. Schneier is one of the most authoritative voices in security and cryptography, so his argument that mass surveillance is ineffective as well as harmful carries significant weight in policy debates. The discussion highlights growing concern that surveillance powers are being normalized and expanded, with commenters pointing to NSPM-7 as a looming escalation. Schneier notes that mass surveillance is now a routine tool used by law enforcement, with ICE employing it in immigration actions and against people exercising their First Amendment rights to protest. Commenters proposed limiting camera network access to local jurisdictions and building easy-to-use self-hosted privacy services to leverage First and Fourth Amendment protections.

hackernews · iamnothere · Sep 15, 11:26 · [Discussion](https://news.ycombinator.com/item?id=49710883)

**Background**: Mass surveillance refers to the indiscriminate collection and analysis of communications and movement data on entire populations, dramatically expanded after the September 11 attacks and revealed publicly through the 2013 Snowden disclosures. Bruce Schneier is a cryptographer and public-interest technologist who has long argued, including in his book Data and Goliath, that mass surveillance cannot reliably stop terrorist attacks. NSPM-7, referenced by a commenter, is a US national security policy memorandum that critics say would further expand surveillance authorities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html">25 Years of Mass Surveillance Is Enough - Schneier on Security</a></li>
<li><a href="https://www.lawfaremedia.org/article/25-years-of-mass-surveillance-is-enough">25 Years of Mass Surveillance Is Enough | Lawfare</a></li>
<li><a href="https://www.vice.com/en/article/bruce-schneier-mass-surveillance-wont-stop-terror-876/">This Security Expert Thinks Mass Surveillance Doesn't Stop Terror...</a></li>

</ul>
</details>

**Discussion**: Commenters largely agreed with Schneier, with one quoting the Tao Te Ching to argue that restriction breeds the disorder it aims to prevent, and another proposing locally bounded camera networks and self-hosted privacy services. Several expressed alarm that NSPM-7 will make mass surveillance far more oppressive, and one warned the issue will only be addressed once surveillance becomes a national security liability.

**Tags**: `#surveillance`, `#privacy`, `#security`, `#policy`, `#civil-liberties`

---

<a id="item-8"></a>
## [SemiAnalysis: Vera Rubin NVL72 Delivers 67x Better Agentic Inference Performance per Dollar](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-agentic-inference) ⭐️ 8.0/10

SemiAnalysis published an analysis claiming that NVIDIA's Vera Rubin NVL72 rack-scale platform delivers 67x better performance per dollar for agentic inference workloads, using its new AgentX benchmark built from 393 opt-in Claude Code sessions. The article also argues NVIDIA is sandbagging performance claims, and highlights 2x more annual profit per gigawatt along with the themes of extreme co-design and 'the more you buy, the more you earn.' If accurate, a 67x improvement in performance per dollar for agentic inference would substantially reshape the economics of running AI agents at scale, affecting data center operators, cloud providers, and enterprises planning large inference deployments. It also signals that hardware design is increasingly being co-optimized around multi-turn, stateful agentic workloads rather than single-shot model completions. The Vera Rubin NVL72 platform combines 36 Vera CPUs and 72 Rubin GPUs in a rack-scale system, delivering 3.6 exaFLOPS of AI performance and 75TB of memory, built on NVIDIA's third-generation MGX design for cable-free modularity and rapid deployment. The AgentX benchmark is a replay workload derived from real Claude Code sessions, designed to capture long-context, multi-turn coding scenarios that differ from fixed-sequence inference benchmarks.

rss · Semianalysis · Sep 14, 22:08

**Background**: Agentic inference refers to the full execution path an AI agent follows when it reasons, selects actions, calls tools, revisits prior context, and updates its next step — a stateful, multi-turn workflow rather than a single model completion. As agentic AI becomes a dominant production use case, benchmarks like MLPerf and SemiAnalysis's InferenceX/AgentX have been extended to measure these multi-turn workloads. NVIDIA's Vera Rubin NVL72 is a rack-scale AI platform positioned for gigascale training and inference, and SemiAnalysis is a widely cited source for deep technical analysis of AI hardware and inference economics.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">NVIDIA Vera Rubin NVL72 | Co-Designed Infrastructure for Agentic AI</a></li>
<li><a href="https://servers.asus.com/glossary/What-is-NVIDIA-Vera-Rubin-NVL72">What is NVIDIA Vera Rubin NVL72? | ASUS Servers</a></li>
<li><a href="https://inferencex.semianalysis.com/">Open-Source Agentic Inference Benchmark | InferenceX</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#inference`, `#performance`, `#NVIDIA`, `#agentic AI`

---

<a id="item-9"></a>
## [44M-parameter ternary LLM runs at 1,900 tok/s on CPU in 19.8 MB](https://www.reddit.com/r/MachineLearning/comments/1wgzpli/i_trained_a_44m_parameter_quantized_llm_from/) ⭐️ 8.0/10

A developer trained SHADOW-50M, a 44M-parameter LLM, from scratch on 45B tokens, shipping as a 19.8 MB ternary-weight model that runs at ~1,900 tok/s on a laptop CPU and ~500 tok/s in a browser via WebAssembly. It introduces a 73,880-token vocabulary encoded as fixed 512-bit fingerprints instead of trained embeddings, plus a hybrid calculation circuit that handles arithmetic, dates, units, and sorting inside the token stream. This demonstrates that extreme quantization and architectural tricks can push useful language and retrieval capabilities into a sub-20 MB footprint that runs entirely offline on commodity CPUs, which is significant for edge AI, privacy-preserving on-device inference, and TinyML applications. It also shows a practical alternative to tool-calling by embedding deterministic calculation circuits directly into the model's token stream. The model uses ternary {-1,0,+1} weights and a 159 KB compiled kernel, with a disk-based archive storing attention states at 1 bit (288 bytes/token) and a 22 bytes/token index that avoids vector databases or embedding models. On standard benchmarks it underperforms a 51.8M-parameter bf16 Llama-style model (ARC-Easy 0.307 vs 0.435, PIQA 0.570 vs 0.600, WikiText-2 perplexity 186 vs 165), but it excels at arithmetic, date, and retrieval tasks where the larger model fails.

reddit · r/MachineLearning · /u/Final-Data-1410 · Sep 15, 12:59

**Background**: Ternary weight networks quantize weights to {-1, 0, +1}, enabling multiplication-free inference and dramatic model compression, which is a key technique for running LLMs on edge devices. Quantized LLMs reduce memory and compute requirements by using low-bit representations, and WebAssembly allows such models to run cross-platform, including in browser tabs. This project builds on those ideas by combining ternary weights with a fingerprint-based vocabulary and a deterministic calculation circuit.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/ternary-weight-networks-twns">Ternary Weight Networks Overview</a></li>
<li><a href="https://symbl.ai/developers/blog/a-guide-to-quantization-in-llms/">A Guide to Quantization in LLMs | Symbl.ai</a></li>
<li><a href="https://gcore.com/resources/web-assembly-for-ai-inference">WebAssembly for AI Inference</a></li>

</ul>
</details>

**Discussion**: The community response has been strongly positive, with 360+ upvotes on the original post and 94 GitHub stars, indicating high interest in efficient tiny LLMs. Commenters likely appreciate the transparency about benchmark weaknesses and the novel retrieval and calculation mechanisms, though some may question the practical utility of a model that underperforms on standard benchmarks.

**Tags**: `#LLM`, `#Quantization`, `#Edge AI`, `#Efficient Inference`, `#TinyML`

---

<a id="item-10"></a>
## [Prior Labs releases TabPFN-3.5, new SOTA tabular foundation model](https://www.reddit.com/r/MachineLearning/comments/1wh4xhy/tabpfn35_is_released_as_the_next_sota_tabular/) ⭐️ 8.0/10

Prior Labs released TabPFN-3.5, a new tabular foundation model that tops both the TabArena and BeyondArena benchmarks and is state-of-the-art for datasets up to 1M rows and 20k features. It ships in three variants: TabPFN-3.5-Fast (alpha, 6x faster than the base model), TabPFN-3.5-Thinking (trades compute for accuracy via the API), and TabPFN-3.5-Plus. Tabular data remains the dominant format in enterprise and scientific settings, yet it has lagged behind text and vision in foundation-model progress, so a new SOTA release with large benchmark gains signals that tabular foundation models are maturing quickly. The new speed and compute-scaling variants also make these models more practical for real-world deployment, affecting data scientists and ML engineers who rely on gradient-boosted trees like XGBoost. On BeyondArena, TabPFN-3.5 leads on text-rich, high-cardinality and high-dimensional data with +250 Elo over the strongest previous baseline and +150 Elo ahead of the previous overall leader. TabPFN-3.5-Thinking adds +20 Elo over the base model on BeyondArena and +44 Elo on TabArena, though the Fast variant is still in alpha.

reddit · r/MachineLearning · /u/tuanacelik · Sep 15, 16:18

**Background**: TabPFN is a pre-trained transformer-based foundation model for tabular data, developed by Prior Labs; instead of training a separate model per dataset, it generates large corpora of synthetic tabular datasets and learns to make predictions in-context. TabArena is a living benchmark that continuously integrates new datasets and models to reliably compare tabular ML methods, while BeyondArena is a newer unified benchmark covering IID, temporal and grouped tasks across different scales and dimensionalities. Elo is a relative rating score borrowed from chess, where higher values indicate stronger performance against opponents.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/PriorLabs/tabpfn">PriorLabs/TabPFN - Foundation Model for Tabular Data - GitHub</a></li>
<li><a href="https://arxiv.org/abs/2506.16791">TabArena : A Living Benchmark for Machine Learning on Tabular Data</a></li>
<li><a href="https://www.linkedin.com/posts/probabl_theres-a-new-tabular-ai-benchmark-in-town-activity-7481346525374271488-KtqC">There’s a new tabular AI benchmark in town: BeyondArena Our...</a></li>

</ul>
</details>

**Tags**: `#tabular-data`, `#foundation-models`, `#machine-learning`, `#SOTA`, `#benchmarks`

---

<a id="item-11"></a>
## [China's 15th Five-Year Plan Targets Advanced Chips and OpenHarmony](https://www.secrss.com/articles/93961) ⭐️ 8.0/10

China's Ministry of Industry and Information Technology (MIIT) and National Development and Reform Commission (NDRC) jointly issued the 15th Five-Year Plan for the electronic information manufacturing industry, outlining 17 key tasks. The plan calls for improving advanced process capabilities, breaking through high-end mobile phone core chips and PC high-performance chips, and strengthening the adoption of domestic operating systems such as OpenHarmony. This policy sets ambitious targets—over 30 trillion yuan in revenue and 3.5% R&D intensity by 2030—that could significantly reshape China's semiconductor self-sufficiency and global supply chains. It directly impacts chip designers, manufacturers, OS developers, and downstream device makers in China and abroad. The plan also promotes RISC-V, AI chips and terminals, and BeiDou-related development, while emphasizing domestic OS adoption. However, it remains a strategic roadmap without specific funding or enforcement mechanisms disclosed.

telegram · zaihuapd · Sep 15, 03:10

**Background**: OpenHarmony is an open-source distributed operating system donated by Huawei to the OpenAtom Foundation, forming the basis for HarmonyOS. RISC-V is a free and open instruction set architecture that allows customizable chip designs, seen as an alternative to proprietary architectures like ARM and x86. Advanced process nodes (e.g., 7nm, 5nm, 3nm) refer to cutting-edge semiconductor fabrication technologies that enable more powerful and efficient chips.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenHarmony">OpenHarmony - Wikipedia</a></li>
<li><a href="https://riscv.org/">Home - RISC - V International</a></li>
<li><a href="https://www.tessolve.com/blogs/7nm-vs-5nm-vs-2nm-how-to-choose-the-right-semiconductor-process-node/">7nm vs 5nm vs 2nm: Choosing the Right Process Node</a></li>

</ul>
</details>

**Tags**: `#China policy`, `#semiconductor`, `#OpenHarmony`, `#RISC-V`, `#AI chips`

---

<a id="item-12"></a>
## [US and UK Lawmakers Push Bills to Ban Superintelligent AI](https://t.me/zaihuapd/43832) ⭐️ 8.0/10

US Senator Bernie Sanders announced he will introduce a "Ban on Artificial Superintelligence Act" to prohibit developing AI smarter than humans and pause other advanced AI research, while UK MP Sorbell introduced what is reportedly the first such bill in a G7 parliament, granting the government power to monitor and restrict superintelligent "precursor" systems. This marks a notable escalation in AI governance efforts, as major Western legislators move beyond safety guidelines toward outright bans on superintelligent systems, potentially shaping global AI regulation and international treaty discussions. Both bills also call on their governments to push for global treaties, but passage prospects are slim; UC Berkeley professor Stuart Russell warned AI could cause a "Chernobyl-scale disaster" by coordinating attacks on financial, communications, or power grid systems.

telegram · zaihuapd · Sep 15, 04:26

**Background**: Superintelligent AI refers to a hypothetical AI that surpasses human intelligence in reasoning and decision-making. AI safety researchers and policymakers have increasingly called for binding international agreements to establish red lines preventing unchecked escalation of AI capabilities, similar to efforts by EU MEP Brando Benifei urging global cooperation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.euronews.com/video/2026/09/15/eu-has-the-power-to-lead-on-global-treaty-on-ai-says-mep-brando-benifei">Video. EU has 'the power' to lead on ' global treaty on AI ... | Eu...</a></li>
<li><a href="https://www.antoinebuteau.com/lessons-from-yoshua-bengio/">Lessons from Yoshua Bengio | Antoine Buteau</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/what-is-artificial-intelligence-ai/">What is Artificial Intelligence ( AI ) - GeeksforGeeks</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#superintelligence`, `#policy`, `#AI safety`, `#legislation`

---

<a id="item-13"></a>
## [Google Opens Anthropic's Claude Opus 5 to All Engineers](https://www.businessinsider.com/google-finally-lets-all-engineers-use-anthropics-claude-2026-9) ⭐️ 8.0/10

Google has granted all of its engineers access to Anthropic's Claude Opus 5 for internal development, but only through its in-house Antigravity platform. Previously, Google barred most employees from using external coding tools like Claude Code and OpenAI's Codex, pushing them toward its own Gemini instead. The move signals that even a company with its own frontier model feels competitive pressure in AI coding tools, and it marks a notable strategic shift for Google, which is also a major Anthropic investor. It could influence how other large enterprises balance first-party and third-party AI coding assistants. Gemini remains the primary internal development model, while Claude is offered as a supplement under a per-employee quota. Google announced earlier this year that it plans to invest up to $40 billion in Anthropic, underscoring the intertwined relationship between the two companies.

telegram · zaihuapd · Sep 15, 05:31

**Background**: Claude is Anthropic's family of large language models, released in three tiers named Haiku, Sonnet, and Opus, with Opus being the most capable; Claude Code is Anthropic's terminal-based agentic coding tool. Google Antigravity is Google's agentic development platform, which evolves the traditional IDE into an agent-first environment where developers orchestrate AI agents rather than write every line themselves. Google's own competing model is Gemini, which it has historically required employees to use for internal work.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://antigravity.google/">Google Antigravity</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Google`, `#Anthropic`, `#Claude`, `#developer-tools`

---