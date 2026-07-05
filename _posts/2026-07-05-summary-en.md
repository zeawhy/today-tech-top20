---
layout: default
title: "Horizon Summary: 2026-07-05 (EN)"
date: 2026-07-05
lang: en
---

> From 39 items, 10 important content pieces were selected

---

1. [F-Droid Declares Google ADV Malware, Pre-installed on 4 Billion Devices](#item-1) ⭐️ 9.0/10
2. [Shadcn/UI switches default from Radix to Base UI](#item-2) ⭐️ 8.0/10
3. [GPT-5.5 Codex 516-Token Bug Causes Reasoning Failures](#item-3) ⭐️ 8.0/10
4. [sqlite-utils 4.0rc2: Claude Fable Catches Critical Bugs](#item-4) ⭐️ 8.0/10
5. [Newer Claude Models Worse at Tool Schema Adherence](#item-5) ⭐️ 8.0/10
6. [Competence Gate: Gating Tool Use via Internal Confidence](#item-6) ⭐️ 8.0/10
7. [USAF: Sparse Fine-Tuning for MoE on Consumer GPUs](#item-7) ⭐️ 8.0/10
8. [iOS 27 Introduces Trust Insights Anti-Fraud Feature](#item-8) ⭐️ 8.0/10
9. [OpenAI Never Visited Key UK Stargate Site, Guardian Finds](#item-9) ⭐️ 8.0/10
10. [Fudan Exam: Students Stump AI, Only 4 Get Zero](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [F-Droid Declares Google ADV Malware, Pre-installed on 4 Billion Devices](https://f-droid.org/2026/07/01/adv-malware.html) ⭐️ 9.0/10

F-Droid has officially classified Google's Android Developer Verification (ADV) as malware, stating it is a system process with root privileges that cannot be removed and is pre-installed on approximately 4 billion Android devices. Starting September 30, 2026, ADV will be activated in Brazil, Indonesia, Singapore, and Thailand, blocking users from installing software not approved by Google. This move threatens the openness of the Android ecosystem and user freedom, potentially allowing Google to block any unapproved software, including ad blockers and FOSS apps. It has sparked widespread opposition from digital rights organizations like EFF, FSF, and ACLU, and could set a precedent for platform control. F-Droid notes that Google deliberately avoids defining 'malware' in its developer terms, allowing it to arbitrarily classify disliked software. Despite a petition with hundreds of thousands of signatures and an open letter signed by over 70 organizations, Google is proceeding with the global rollout planned for 2027 and beyond.

telegram · zaihuapd · Jul 5, 00:41

**Background**: F-Droid is a free and open-source app store for Android that hosts only FOSS applications. Google Play Protect is a built-in security service that scans apps. ADV is a new system process introduced by Google as an extra security layer, but critics argue it gives Google excessive control over what software users can install, undermining Android's open nature.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.android.com/developer-verification">Android developer verification | Android Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/F-Droid">F-Droid</a></li>

</ul>
</details>

**Tags**: `#Android`, `#malware`, `#F-Droid`, `#Google`, `#digital rights`

---

<a id="item-2"></a>
## [Shadcn/UI switches default from Radix to Base UI](https://ui.shadcn.com/docs/changelog) ⭐️ 8.0/10

Shadcn/UI has changed its default component library from Radix UI to Base UI, a new unstyled component library from the creators of Radix, Floating UI, and Material UI. This shift affects thousands of projects using Shadcn/UI and sparks debate about migration strategies, including the use of codemods versus LLMs, and the maintainability of the copy-paste approach. Base UI is an unstyled, headless component library that provides complete control over styling and accessibility, similar to Radix but with a different API. The change reflects Shadcn/UI's ongoing evolution and community feedback.

hackernews · dabinat · Jul 5, 04:46 · [Discussion](https://news.ycombinator.com/item?id=48791328)

**Background**: Shadcn/UI is a popular collection of reusable React components built on Radix UI and Tailwind CSS, distributed via CLI for full code ownership. Radix UI is a low-level, unstyled component library focused on accessibility. Base UI, from the same team, offers a similar philosophy with a fresh approach.

<details><summary>References</summary>
<ul>
<li><a href="https://ui.shadcn.com/docs">Introduction - shadcn/ui</a></li>
<li><a href="https://base-ui.com/">Unstyled UI components for accessible design systems · Base UI</a></li>
<li><a href="https://github.com/mui/base-ui">GitHub - mui/base-ui: Unstyled UI components for building accessible web apps and design systems. From the creators of Radix, Floating UI, and Material UI. · GitHub</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed feelings: some find the copy-paste approach creates upgrade challenges, while others welcome the move away from over-engineered solutions. There is also debate about using LLMs for migration instead of traditional codemods.

**Tags**: `#UI Libraries`, `#React`, `#Frontend Development`, `#Open Source`

---

<a id="item-3"></a>
## [GPT-5.5 Codex 516-Token Bug Causes Reasoning Failures](https://github.com/openai/codex/issues/30364) ⭐️ 8.0/10

Users report that GPT-5.5 Codex's reasoning token clustering at exactly 516 tokens causes degraded performance and incorrect answers, with community-provided scripts to reproduce the issue. This bug affects a widely-used AI coding tool, potentially impacting many developers who rely on Codex for code generation and reasoning tasks, and highlights concerns about silent server-side changes. The clustering occurs at multiples of 516 tokens (516, 1034, 1552), and when the model stops reasoning at exactly 516 tokens, it often returns wrong results; using more tokens (6000-8000) yields correct answers.

hackernews · maille · Jul 4, 21:51 · [Discussion](https://news.ycombinator.com/item?id=48789428)

**Background**: GPT-5.5 Codex is OpenAI's latest coding-focused model, released in 2026 as an upgrade to GPT-5.3 Codex. Reasoning tokens are internal tokens the model uses to think through problems before generating a final answer. Token clustering refers to the model disproportionately stopping at specific token counts, suggesting a bug in the adaptive thinking mechanism.

<details><summary>References</summary>
<ul>
<li><a href="https://explainx.ai/blog/gpt-5-5-codex-reasoning-token-clustering-bug-2026">GPT-5.5 Codex 516- Token Bug: Evidence and Theories... | explainx.ai</a></li>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT - 5 . 5 | OpenAI</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely negative, with users reporting daily quality drops and switching to alternatives like Claude. Some draw parallels to a similar Claude Code regression in April, and others suggest using local models to avoid server-side changes.

**Tags**: `#AI`, `#LLM`, `#Codex`, `#bug`, `#performance`

---

<a id="item-4"></a>
## [sqlite-utils 4.0rc2: Claude Fable Catches Critical Bugs](https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/#atom-everything) ⭐️ 8.0/10

Simon Willison used Claude Fable to review sqlite-utils 4.0rc1, leading to the discovery of five release-blocking bugs, including a data loss bug in delete_where(). After 37 prompts and 34 commits, the fixes resulted in sqlite-utils 4.0rc2. This demonstrates how AI-assisted code review can catch subtle, high-impact bugs before a major release, improving software quality and reducing the need for emergency patches. It also showcases a practical workflow for integrating LLMs into open-source maintenance. The worst bug found was that Table.delete_where() never committed and left the connection in a poisoned state, causing subsequent writes to be silently lost. The review cost approximately $149.25 in Claude API usage, and the entire process spanned 37 prompts and 34 commits across 30 files.

rss · Simon Willison · Jul 5, 01:00

**Background**: sqlite-utils is a Python library and CLI tool for manipulating SQLite databases. Semantic versioning (SemVer) uses a three-part version number (Major.Minor.Patch) where breaking changes require a major version bump. Claude Fable is Anthropic's advanced AI model designed for complex coding tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/simonw/sqlite-utils">GitHub - simonw/sqlite-utils: Python CLI utility and library for ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable">Claude Fable</a></li>
<li><a href="https://en.wikipedia.org/wiki/SemVer">SemVer</a></li>

</ul>
</details>

**Tags**: `#AI-assisted development`, `#open source`, `#Python`, `#sqlite-utils`, `#Claude`

---

<a id="item-5"></a>
## [Newer Claude Models Worse at Tool Schema Adherence](https://simonwillison.net/2026/Jul/4/better-models-worse-tools/#atom-everything) ⭐️ 8.0/10

Armin Ronacher reported on July 4, 2026 that newer Claude models, including Opus 4.8 and Sonnet 5, sometimes generate invalid tool call arguments with extra invented fields, causing Pi's edit tool to reject them. This regression was not observed in older Claude models. This regression undermines the reliability of AI coding agents that rely on precise tool call schemas, affecting developers using third-party harnesses like Pi. It highlights a tension between model training for specific tools and general-purpose tool use. The extra fields are invented by the model and can include keys like 'new_text_x', 'type', 'in_file', or 'closeenough'. Enabling strict mode in Claude's API reportedly fixes the issue for some users.

rss · Simon Willison · Jul 4, 22:53

**Background**: Large language models (LLMs) like Claude can be given tool definitions and are expected to output calls matching a JSON schema. Pi is a coding harness that uses custom edit tools; Claude Code has its own built-in edit tools. The newer models may have been trained via reinforcement learning to favor Claude Code's internal tool format, causing them to hallucinate fields when used with different schemas.

<details><summary>References</summary>
<ul>
<li><a href="https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/">Better Models: Worse Tools | Armin Ronacher's Thoughts and ...</a></li>
<li><a href="https://github.com/earendil-works/pi/issues/6278">New Claude models work poorly with the current Pi 's edit tool , failing...</a></li>
<li><a href="https://chatforest.com/builders-log/opus-4-8-sonnet-5-tool-schema-hallucination-strict-mode-fix-builder-guide/">Better Models, Worse Tools: Opus 4.8 and Sonnet 5 Hallucinate ...</a></li>

</ul>
</details>

**Discussion**: The community discussion on the issue tracker (GitHub issue #6278) shows developers confirming the problem and sharing examples of extra fields. Some users suggest enabling strict mode as a workaround, while others debate whether third-party tools should adapt to model-specific quirks.

**Tags**: `#LLM`, `#tool calling`, `#AI reliability`, `#Claude`, `#regression`

---

<a id="item-6"></a>
## [Competence Gate: Gating Tool Use via Internal Confidence](https://www.reddit.com/r/MachineLearning/comments/1unw5un/competence_gate_gating_tooluse_on_a_small_models/) ⭐️ 8.0/10

A 10MB LoRA adapter for Qwen3.5-4B gates tool use based on internal confidence signals, improving error detection and reducing hallucination. It runs locally on Apple Silicon via MLX and on llama.cpp/Ollama via GGUF. This approach addresses a key limitation of small language models: their inability to accurately verbalize confidence, leading to overconfident incorrect answers. By gating tool use on internal signals, it reduces hallucinations and protects private data from being leaked to public search engines. The gate achieved a d′ improvement of 0.46 in error detection over the base model's tool calling, and 87% of cases flagged by the gate but not by the base model were genuinely wrong. A two-signal version reduced private queries sent to public search from 22% to 10%.

reddit · r/MachineLearning · /u/Synthium- · Jul 5, 07:49

**Background**: LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning method that adds small trainable adapters to a frozen base model, enabling task-specific customization with minimal overhead. Internal confidence signals refer to the model's hidden state activations that correlate with its certainty, which can be more reliable than the model's verbalized confidence statements.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/learn/llm-course/chapter11/4">LoRA (Low-Rank Adaptation) · Hugging Face</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-4B">Qwen/Qwen3.5-4B · Hugging Face</a></li>
<li><a href="https://arxiv.org/abs/2604.22271">[2604.22271] How LLMs Detect and Correct Their Own Errors ...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#LLM`, `#tool use`, `#confidence calibration`, `#open source`

---

<a id="item-7"></a>
## [USAF: Sparse Fine-Tuning for MoE on Consumer GPUs](https://www.reddit.com/r/MachineLearning/comments/1unl62q/if_your_gpu_can_run_inference_it_should_be_able/) ⭐️ 8.0/10

A new open-source method called USAF (Ultra Sparse Adaptive Fine-Tuning) enables fine-tuning of Mixture-of-Experts (MoE) models on GPUs that previously could only run inference, demonstrated on a 12GB AMD RX 6750 XT with Qwen3-30B-A3B. This breakthrough dramatically lowers the hardware barrier for fine-tuning large MoE models, allowing researchers and hobbyists with consumer GPUs to customize state-of-the-art models without expensive cloud or enterprise hardware. USAF trains only 26 million out of 4.8 billion parameters (sparse expert weights and the router) on a 12GB GPU, whereas full fine-tuning would require over 120GB. It is the only method that works on AMD GPUs and the only one that trains both expert weights and the router.

reddit · r/MachineLearning · /u/tsuyu122 · Jul 4, 21:56

**Background**: Mixture-of-Experts (MoE) models use multiple specialized subnetworks (experts) activated by a router, enabling large model capacity with lower inference cost. However, fine-tuning such models typically requires massive GPU memory because all parameters are updated. Sparse fine-tuning methods like USAF update only a small subset of parameters, drastically reducing memory needs.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/tsuyu122/usaf/blob/master/README.md">usaf/README.md at master · tsuyu122/usaf · GitHub</a></li>
<li><a href="https://github.com/tsuyu122/usaf/blob/master">GitHub - tsuyu122/usaf</a></li>

</ul>
</details>

**Tags**: `#fine-tuning`, `#MoE`, `#sparse training`, `#open source`, `#GPU`

---

<a id="item-8"></a>
## [iOS 27 Introduces Trust Insights Anti-Fraud Feature](https://www.cultofmac.com/news/ios-27-trust-insights-feature) ⭐️ 8.0/10

Apple announced Trust Insights, a new on-device anti-fraud framework for iOS 27 that analyzes user behavior patterns, timing, context, and sensor data to detect scam-induced actions like coerced transfers or account changes. This marks a significant step in proactive fraud prevention on mobile devices, using privacy-preserving on-device AI to protect users from social engineering scams without compromising personal data. The feature does not read messages, emails, or photo content; raw data is immediately deleted, and only a single output value is sent to the server. Developers must opt in to integrate Trust Insights into their apps.

telegram · zaihuapd · Jul 4, 14:30

**Background**: Social engineering scams, where fraudsters trick users into performing actions like transferring money or changing account credentials, are a growing threat. Traditional anti-fraud measures often rely on server-side analysis or user reports, which can be too late. Trust Insights uses on-device machine learning to detect suspicious behavior in real time, adding a layer of protection before the user completes the scammer's requested action.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=jY-_rqz_VEM">WWDC26: Meet Trust Insights | Apple - YouTube</a></li>
<li><a href="https://www.ithinkdiff.com/ios-27-trust-insights-scam-detection-framework/">iOS 27 Adds Trust Insights to Detect Scams Before They Happen</a></li>
<li><a href="https://www.newsy-today.com/real-time-social-engineering-detection-how-trust-insights-stops-fraud-before-it-starts/">Real-Time Social Engineering Detection: How Trust Insights Stops...</a></li>

</ul>
</details>

**Tags**: `#iOS`, `#security`, `#anti-fraud`, `#privacy`, `#Apple`

---

<a id="item-9"></a>
## [OpenAI Never Visited Key UK Stargate Site, Guardian Finds](https://www.theguardian.com/technology/2026/jul/04/openai-apparent-failure-visit-key-site-questions-stargate-uk-project) ⭐️ 8.0/10

A Guardian investigation reveals that OpenAI never visited the Cobalt Park site in North Tyneside, the proposed location for its Stargate UK data center, and local officials never met with OpenAI or partner Nscale. The project, announced in September 2025 as a flagship UK-US AI collaboration, was paused in April 2026 due to regulatory and energy cost concerns. The findings suggest the $30 billion Stargate UK pledge may have been a PR stunt rather than a genuine investment, undermining trust in major AI infrastructure announcements and raising questions about government transparency in tech partnerships. The Stargate UK project was announced in September 2025 with partners Nvidia and Nscale, aiming to build a large data centre in north-east England. It was paused in April 2026, with a local Conservative MP stating the project 'looks extremely unlikely' to proceed.

telegram · zaihuapd · Jul 5, 05:09

**Background**: Stargate UK was part of OpenAI's broader Stargate initiative to build massive AI infrastructure globally. The UK project was touted as a key component of the UK's AI Opportunities Action Plan, promising local computing power for sensitive AI workloads. Cobalt Park is one of the largest business parks in the UK, but OpenAI never sent representatives to the site.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-stargate-uk/">Introducing Stargate UK - OpenAI</a></li>
<li><a href="https://www.bbc.com/news/articles/clyd032ej70o">OpenAI pauses UK data centre deal over energy costs and ... - BBC</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Stargate`, `#AI infrastructure`, `#investigative journalism`, `#UK`

---

<a id="item-10"></a>
## [Fudan Exam: Students Stump AI, Only 4 Get Zero](https://mp.weixin.qq.com/s/d53O-6mVFZqMa_Sti1yEPw) ⭐️ 8.0/10

In a Fudan University data mining course, the final exam was redesigned so that 51 students each created 10 calculation questions to stump three AI models; only 4 students succeeded in making any AI score zero, and the strongest model, Claude, was never completely defeated. This innovative assessment shifts focus from rote memorization to evaluating AI outputs, reflecting a necessary reform in education as AI capabilities advance. It highlights a new paradigm where students learn to command and judge AI, preparing them for an AI-integrated workforce. The exam involved three unnamed AI models, with Claude being the most robust. The class average score was 85.7 out of 100, meaning most students successfully stumped at least one model on some questions, but only four achieved a perfect zero on any model's entire paper.

telegram · zaihuapd · Jul 5, 08:40

**Background**: Traditional exams that test algorithmic recall and memorization are becoming obsolete as AI can easily solve such problems. This course, taught by Professor Xiao Yanghua, represents a shift toward training students in critical thinking, evaluation, and creative problem-solving—skills that AI cannot easily replicate.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/overview">Models overview - Claude Platform Docs</a></li>
<li><a href="https://www.science.org/doi/10.1126/science.aec5115">Generative AI use and misuse call for assessment reform in higher education | Science</a></li>
<li><a href="https://www.unesco.org/en/articles/whats-worth-measuring-future-assessment-ai-age">What's worth measuring? The future of assessment in the AI age</a></li>

</ul>
</details>

**Tags**: `#AI in Education`, `#Assessment Reform`, `#LLM Evaluation`, `#Pedagogy`, `#AI Safety`

---