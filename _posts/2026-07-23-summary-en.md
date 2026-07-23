---
layout: default
title: "Horizon Summary: 2026-07-23 (EN)"
date: 2026-07-23
lang: en
---

> From 95 items, 17 important content pieces were selected

---

1. [Terrence Tao Uses ChatGPT to Explore Jacobian Conjecture Counterexample](#item-1) ⭐️ 9.0/10
2. [SkewAdam cuts MoE optimizer memory by 97%](#item-2) ⭐️ 9.0/10
3. [GigaToken: 1000x Faster LLM Tokenization via SIMD](#item-3) ⭐️ 8.0/10
4. [Bento: Entire PowerPoint in One HTML File](#item-4) ⭐️ 8.0/10
5. [Postgres Survival Guide for Startups](#item-5) ⭐️ 8.0/10
6. [Take-Home Interview Project Hides Malicious Git Hook](#item-6) ⭐️ 8.0/10
7. [Anthropic's Claude Tag handles 65% of product engineering PRs](#item-7) ⭐️ 8.0/10
8. [US Treasury threatens sanctions over Moonshot AI model distillation](#item-8) ⭐️ 8.0/10
9. [OpenAI's Infrastructure Spending Hits $750B](#item-9) ⭐️ 8.0/10
10. [Mathematicians Still Don't Know the Fastest Way to Multiply](#item-10) ⭐️ 8.0/10
11. [Vera Rubin NVL72 vs GB200 NVL72: Inference TCO & Architecture](#item-11) ⭐️ 8.0/10
12. [Hugging Face Discloses AI Agent Attack, Commercial LLMs Refuse Forensics](#item-12) ⭐️ 8.0/10
13. [Chinese Tech Firms Recruit Teenagers to Tackle AI Talent Shortage](#item-13) ⭐️ 8.0/10
14. [Moonshot AI seeks $2B funding at $30B valuation](#item-14) ⭐️ 8.0/10
15. [Microsoft Eyes DeepSeek Integration for Copilot Cowork Cost Cuts](#item-15) ⭐️ 8.0/10
16. [Sandbox Escape in 4 Major AI Coding Agents via Prompt Injection](#item-16) ⭐️ 8.0/10
17. [Trump May Restrict US Firms from Using Chinese Open-Weight AI Models](#item-17) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Terrence Tao Uses ChatGPT to Explore Jacobian Conjecture Counterexample](https://chatgpt.com/share/6a5fdc7a-d6f8-83e8-bbea-8deb42cfed56) ⭐️ 9.0/10

Terrence Tao shared a ChatGPT conversation where he systematically guided the AI to discover a counterexample to the Jacobian conjecture, demonstrating advanced AI-assisted mathematical reasoning. This shows that large language models can be powerful tools for mathematical research when guided by an expert, potentially accelerating discovery and democratizing access to advanced reasoning. The counterexample is a structured polynomial in three variables, not a brute-force selection, and Tao's prompts are highly specific, using jargon and step-by-step progression to extract useful insights from the model.

hackernews · gmays · Jul 22, 17:30 · [Discussion](https://news.ycombinator.com/item?id=49010345)

**Background**: The Jacobian conjecture states that if a polynomial map has a nonzero constant Jacobian determinant, then it has a polynomial inverse. It was first stated in 1939 and is known for many false proofs. A counterexample for dimensions greater than 2 was recently found using AI, but the 2D case remains open.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jacobian_conjecture">Jacobian conjecture</a></li>
<li><a href="https://mathworld.wolfram.com/JacobianConjecture.html">Jacobian Conjecture -- from Wolfram MathWorld</a></li>
<li><a href="https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/">A digestion of the Jacobian conjecture counterexample | What's new</a></li>

</ul>
</details>

**Discussion**: Commenters are fascinated by Tao's expert prompting technique, noting that his specific, jargon-heavy questions are key to getting useful results. They also highlight that the counterexample is structurally meaningful, not just a brute-force find, and that this demonstrates how AI can efficiently map new knowledge to an expert's mental model.

**Tags**: `#mathematics`, `#AI-assisted research`, `#LLM applications`, `#Jacobian Conjecture`, `#expert prompting`

---

<a id="item-2"></a>
## [SkewAdam cuts MoE optimizer memory by 97%](https://www.reddit.com/r/MachineLearning/comments/1v38k1m/skewadam_a_tiered_optimizer_that_cuts_moe_state/) ⭐️ 9.0/10

SkewAdam, a tiered optimizer, reduces Mixture-of-Experts (MoE) optimizer state memory by 97.4%, from 50.6 GB to 1.29 GB, enabling a 6.78B MoE model to fit on a single 40GB GPU. This breakthrough dramatically lowers the hardware barrier for training large MoE models, allowing researchers with consumer-grade GPUs to experiment with architectures previously limited to high-end clusters. SkewAdam uses a tiered state allocation: backbone parameters (5%) get momentum and factored second moment, experts (95%) get only factored second moment, and the router (<0.01%) gets exact second moment, maintaining convergence and router stability.

reddit · r/MachineLearning · /u/Kooky-Ad-4124 · Jul 22, 07:04

**Background**: Mixture-of-Experts (MoE) models use multiple specialized sub-networks (experts) activated by a router, enabling larger model capacity without proportional compute. However, training MoEs with standard optimizers like AdamW requires storing large optimizer states (momentum and second moment) for each parameter, which often dominates GPU memory. Factored second-moment estimates, as used in Adafactor, reduce memory by approximating the second moment matrix with low-rank factors.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@apoorvajain1111/inside-the-sparse-brain-how-mixture-of-experts-moe-makes-llms-smarter-faster-and-greener-205b0fea1416">Inside the Sparse Brain: How Mixture - of - Experts ( MoE )... | Medium</a></li>
<li><a href="https://deepwiki.com/google-deepmind/optax/3.1-standard-optimizers">Standard Optimizers | google-deepmind/optax | DeepWiki</a></li>

</ul>
</details>

**Tags**: `#Mixture-of-Experts`, `#Optimizer`, `#Memory Efficiency`, `#Deep Learning`, `#GPU Training`

---

<a id="item-3"></a>
## [GigaToken: 1000x Faster LLM Tokenization via SIMD](https://github.com/marcelroed/gigatoken/) ⭐️ 8.0/10

GigaToken is an open-source library that achieves approximately 1000x faster language model tokenization by using SIMD-optimized pretokenization and caching techniques. Tokenization is a critical preprocessing step for LLMs, and this speedup can significantly reduce time and cost when processing terabytes of text for training datasets. The speedup comes from replacing regex-based pretokenization with SIMD instructions and heavily optimizing caching of pretoken mappings, with consistent results across modern x86 and ARM CPUs.

hackernews · syrusakbary · Jul 22, 17:20 · [Discussion](https://news.ycombinator.com/item?id=49010167)

**Background**: Tokenization converts raw text into numerical tokens that LLMs can process. Traditional tokenizers rely on regex for pretokenization, which is computationally expensive. SIMD (Single Instruction, Multiple Data) allows parallel processing of multiple characters, dramatically speeding up this step.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/marcelroed/gigatoken/">GitHub - marcelroed/gigatoken: Language model tokenization at GB/s · GitHub</a></li>
<li><a href="https://medium.com/@shashankag14/tokenization-in-large-language-models-llms-0ba0aea6b1d6">Tokenization in Large Language Models (LLMs) | by Shashank Agarwal | Medium</a></li>
<li><a href="https://www.traceloop.com/blog/a-comprehensive-guide-to-tokenizing-text-for-llms">A Comprehensive Guide to Tokenizing Text for LLMs | Traceloop - LLM Application Observability</a></li>

</ul>
</details>

**Discussion**: The community praised the work as fantastic, noting its value for offline pretraining data preparation rather than inference. Some humorously noted that tokenization is typically <0.1% of inference time, but acknowledged the significant impact on data preprocessing.

**Tags**: `#tokenization`, `#LLM`, `#performance optimization`, `#SIMD`, `#open source`

---

<a id="item-4"></a>
## [Bento: Entire PowerPoint in One HTML File](https://bento.page/slides/) ⭐️ 8.0/10

Bento is a single HTML file that provides a full slide deck tool with editing, animations, and real-time collaboration, requiring no installation or cloud login. This approach challenges traditional presentation software by offering a portable, offline-first, and privacy-preserving alternative that can be shared and edited by anyone with a browser. The default deck is about 560 KB and uses an encrypted blind relay for collaboration, ensuring the relay cannot see the data. The code is MIT licensed on GitHub.

hackernews · starfallg · Jul 22, 15:19 · [Discussion](https://news.ycombinator.com/item?id=49008211)

**Background**: Traditional presentation tools like PowerPoint require installation and often cloud storage. Bento packages the entire app, data, and editor into a single HTML file that works offline, leveraging web technologies like reveal.js and DecompressionStream.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49008211">Show HN: Bento - An entire PowerPoint in one HTML file (edit+view+data+collab) | Hacker News</a></li>
<li><a href="https://bento.page/">Bento/Suite — the office suite that fits in a file</a></li>
<li><a href="https://github.com/nyblnet/bento">GitHub - nyblnet/bento · GitHub</a></li>

</ul>
</details>

**Discussion**: The community praised Bento's innovation and potential, with some noting it could become more common. One user reported a freeze during heavy collaborative editing, suggesting performance limits under extreme load.

**Tags**: `#single-file web app`, `#presentation tool`, `#offline-first`, `#collaboration`, `#web development`

---

<a id="item-5"></a>
## [Postgres Survival Guide for Startups](https://hatchet.run/blog/postgres-survival-guide) ⭐️ 8.0/10

A comprehensive guide for startups on scaling and optimizing PostgreSQL has been published, covering indexing, connection pooling, and common pitfalls. This guide provides practical, actionable advice that helps startups avoid costly database mistakes and scale efficiently, addressing a critical need in the startup community. The guide emphasizes using uuidv7 over uuid v4, deterministic lock ordering to prevent deadlocks, and using EXPLAIN (GENERIC_PLAN) for query analysis. It also recommends avoiding ORMs, using serial primary keys, and considering an append-only data model.

hackernews · abelanger · Jul 22, 12:36 · [Discussion](https://news.ycombinator.com/item?id=49005787)

**Background**: PostgreSQL is a popular open-source relational database used by many startups. Scaling it requires careful indexing, connection management, and understanding of locking behavior. Connection pooling tools like pgBouncer help manage database connections efficiently.

<details><summary>References</summary>
<ul>
<li><a href="https://scalegrid.io/blog/postgresql-connection-pooling-part-1-pros-and-cons/">PostgreSQL Connection Pooling : Part 1 - Pros & Cons</a></li>
<li><a href="https://www.freecodecamp.org/news/postgresql-indexing-strategies/">Advanced Indexing Strategies in PostgreSQL</a></li>
<li><a href="https://tembo.io/docs/getting-started/postgres_guides/postgres-indexing-strategies">Postgres indexing strategies | Tembo Docs</a></li>

</ul>
</details>

**Discussion**: Commenters provided valuable corrections and additions, such as preferring uuidv7 over uuid v4, deterministic lock ordering, and using EXPLAIN (GENERIC_PLAN). Some noted missing topics like backup strategies and organizational pitfalls like ORM misuse.

**Tags**: `#PostgreSQL`, `#startups`, `#database optimization`, `#scaling`

---

<a id="item-6"></a>
## [Take-Home Interview Project Hides Malicious Git Hook](https://citizendot.github.io/articles/fake-job-interview-git-hook-malware/) ⭐️ 8.0/10

A developer discovered that a take-home interview project contained a malicious git hook that silently executed a remote payload, revealing a sophisticated scam targeting job seekers. This attack vector exploits trust in the hiring process and could compromise many developers' systems, highlighting a growing trend of social engineering combined with technical malware delivery. The malicious git hook was hidden in a .git/hooks directory and executed on git commit, checking the host OS and downloading a payload from a raw IP address. The article also mentions a similar scam using a Visual Studio Code project that runs custom code on project open.

hackernews · CITIZENDOT · Jul 22, 20:33 · [Discussion](https://news.ycombinator.com/item?id=49013036)

**Background**: Git hooks are scripts that run automatically at certain points in Git's workflow, such as before a commit. They are stored in the .git/hooks directory and can be used for automation, but also abused for malicious purposes. Scammers have begun embedding malware in take-home interview projects to infect job seekers' machines.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/xanderselorm/fake-job-offers-are-turning-github-repos-into-a-trap-5fad">Fake Job Offers Are Turning GitHub Repos Into a Trap - DEV Community</a></li>
<li><a href="https://cybertex.io/how-recruitment-scams-target-developers-through-github-test-tasks/">How Recruitment Scams Target Developers via GitHub | Cybertex</a></li>
<li><a href="https://git-scm.com/docs/githooks">Git - githooks Documentation</a></li>

</ul>
</details>

**Discussion**: Commenters shared similar experiences, with one user realizing they were hacked in a more sophisticated attack involving a fake interview with camera disabled. Others noted that using a raw IP address is a red flag, and expressed concern that VS Code projects can run code on open, creating another malware vector.

**Tags**: `#security`, `#malware`, `#social engineering`, `#job scams`, `#git hooks`

---

<a id="item-7"></a>
## [Anthropic's Claude Tag handles 65% of product engineering PRs](https://simonwillison.net/2026/Jul/21/cat-and-thariq/#atom-everything) ⭐️ 8.0/10

Simon Willison hosted a fireside chat with Anthropic's Claude Code team, revealing that Claude Tag now handles 65% of product engineering pull requests for the team. The team also shared that the Claude Code system prompt was reduced by 80% and that adding examples to system prompts is no longer best practice for models like Fable 5. These metrics demonstrate the growing maturity and trust in AI coding agents within Anthropic, showing that AI can autonomously handle a majority of routine engineering work. The shift away from verbose system prompts and negative instructions signals a new paradigm for prompting advanced models. Critical changes to Claude Code are still manually reviewed, but the team increasingly relies on automated code review for outer product layers. Anthropic uses an internal dogfooding process called 'ant fooding' and only ships features that demonstrate user retention with employees first.

rss · Simon Willison · Jul 21, 12:54

**Background**: Claude Code is Anthropic's agentic coding tool that lives in the terminal and helps developers turn ideas into code faster. Claude Tag is a Slack integration that allows users to tag @Claude in threads for real-time assistance. Fable 5 is Anthropic's latest frontier model, built for autonomous knowledge work and coding.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI)</a></li>
<li><a href="https://claude.com/product/tag">Claude in Slack: Tag @ Claude in any thread | Claude by Anthropic</a></li>
<li><a href="https://docs.anthropic.com/en/docs/claude-code/overview">Claude Code overview - Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Claude Code`, `#Anthropic`, `#coding agents`, `#AI engineering`

---

<a id="item-8"></a>
## [US Treasury threatens sanctions over Moonshot AI model distillation](https://techcrunch.com/2026/07/22/treasury-threatens-sanctions-after-white-house-claims-moonshot-distilled-anthropics-fable/) ⭐️ 8.0/10

The US Treasury has threatened sanctions after the White House accused Chinese AI startup Moonshot of distilling Anthropic's Fable model, escalating tensions over Chinese open-source AI models. This incident highlights growing geopolitical friction over AI model distillation and open-source AI, potentially impacting global AI regulation and the flow of open-source models across borders. Model distillation involves transferring knowledge from a large model to a smaller one, which can be used to replicate proprietary models without authorization. The White House claims Moonshot used Anthropic's Fable model without permission.

rss · TechCrunch AI · Jul 22, 20:49

**Background**: Model distillation is a machine learning technique where a smaller 'student' model learns from a larger 'teacher' model, often used to create efficient models for deployment. Moonshot AI is a Chinese startup focused on building foundation models for AGI. Anthropic's Fable model is a state-of-the-art AI model for autonomous knowledge work and coding.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#geopolitics`, `#open-source AI`, `#model distillation`, `#national security`

---

<a id="item-9"></a>
## [OpenAI's Infrastructure Spending Hits $750B](https://techcrunch.com/2026/07/22/openais-ai-spending-spree-has-ballooned-to-750b/) ⭐️ 8.0/10

OpenAI has announced plans to spend $750 billion on AI infrastructure through 2030, a sum comparable to Sweden's entire GDP. This massive investment signals a dramatic escalation in the AI arms race, potentially reshaping global technology infrastructure and influencing how other major players allocate capital. The spending covers data centers, computing hardware, and energy resources through 2030, reflecting OpenAI's bet on continued exponential growth in AI compute demands.

rss · TechCrunch AI · Jul 22, 16:13

**Background**: AI infrastructure spending has been rising rapidly as companies like OpenAI, Google, and Microsoft compete to build ever-larger models. Training state-of-the-art models requires vast clusters of specialized chips and enormous amounts of electricity. This $750 billion figure dwarfs previous estimates and underscores the capital-intensive nature of frontier AI development.

**Tags**: `#OpenAI`, `#AI infrastructure`, `#investment`, `#industry trends`

---

<a id="item-10"></a>
## [Mathematicians Still Don't Know the Fastest Way to Multiply](https://www.solidot.org/story?sid=84899) ⭐️ 8.0/10

The article explores the history and current state of fast multiplication algorithms, from Karatsuba's O(n^1.585) algorithm to the conjectured optimal O(n log n) algorithm by Harvey and van der Hoeven, which has not yet been formally proven. Understanding the fastest possible multiplication algorithm is a fundamental problem in computational complexity, with implications for cryptography, numerical computing, and algorithm design. The search for an optimal algorithm continues to drive theoretical computer science research. Karatsuba's algorithm reduces multiplication complexity to O(n^1.585) using a divide-and-conquer approach, and Python uses a hybrid method switching to Karatsuba for numbers larger than 630 decimal digits. The Harvey-van der Hoeven algorithm achieves O(n log n) but only outperforms Karatsuba for astronomically large numbers.

rss · Solidot 奇客 · Jul 22, 16:52

**Background**: Multiplication algorithms are measured by how the number of operations grows with the number of digits (n). The naive grade-school method has O(n^2) complexity. In 1960, Anatoly Karatsuba discovered a faster algorithm, breaking the O(n^2) barrier and sparking a search for even faster methods.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Karatsuba_algorithm">Karatsuba algorithm</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multiplication_algorithm">Multiplication algorithm - Wikipedia</a></li>
<li><a href="https://stackoverflow.com/questions/70646578/understanding-harvey-van-der-hoeven-2019-algorithm-huge-integer-multiplicatio">Understanding Harvey & van der Hoeven 2019 algorithm ...</a></li>

</ul>
</details>

**Tags**: `#algorithms`, `#computational complexity`, `#mathematics`, `#multiplication`, `#computer science`

---

<a id="item-11"></a>
## [Vera Rubin NVL72 vs GB200 NVL72: Inference TCO & Architecture](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-vs-gb200-nvl72-inference) ⭐️ 8.0/10

A detailed analysis compares NVIDIA's upcoming Vera Rubin NVL72 architecture with the current GB200 NVL72, focusing on inference total cost of ownership (TCO), performance per watt, and performance per dollar. The Rubin architecture introduces 3-bit LUT-based tensor cores and the Feynman SM140 design, promising significant improvements in inference efficiency. This comparison is critical for AI infrastructure planners as it quantifies the potential cost and performance benefits of next-generation hardware. The findings could influence purchasing decisions for large-scale AI inference deployments, especially for models like MoE and DeepSeek-R1. The Vera Rubin NVL72 features 72 Rubin GPUs with 3.6 exaFLOPS of NVFP4 inference performance and 260 TB/s of NVLink 6 bandwidth, while the GB200 NVL72 offers 72 Blackwell GPUs with up to 28x higher throughput than AMD's MI355X in MoE workloads. The analysis also covers software improvements in PyTorch, vLLM, and OpenAI Triton.

rss · Semianalysis · Jul 23, 00:47

**Background**: NVIDIA's GPU architectures evolve rapidly to meet AI demands. The GB200 NVL72 is a current rack-scale system with 72 Blackwell GPUs, while the upcoming Vera Rubin NVL72 integrates the Vera CPU, Rubin GPU, NVLink 6, and other components. The 3-bit LUT tensor core is a novel hardware-software co-design that uses lookup tables for efficient low-bit LLM inference.

<details><summary>References</summary>
<ul>
<li><a href="https://www.r3con.co.uk/post/nvidia-unveils-vera-rubin-nvl72-ai-supercomputer-with-massive-performance-leap">Nvidia Unveils Vera Rubin NVL 72 AI Supercomputer With Massive...</a></li>
<li><a href="https://blogs.nvidia.com/blog/vera-rubin/">NVIDIA Vera Rubin Driving Performance Per Watt... | NVIDIA Blog</a></li>
<li><a href="https://www.kad8.com/ai/gb200-nvl72-vs-mi355x-why-systems-win-moe-inference/">GB 200 NVL 72 vs MI355X: Why Systems Win MoE Inference · KAD</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#GPU architecture`, `#AI inference`, `#TCO analysis`, `#hardware`

---

<a id="item-12"></a>
## [Hugging Face Discloses AI Agent Attack, Commercial LLMs Refuse Forensics](https://t.me/zaihuapd/42701) ⭐️ 8.0/10

Hugging Face disclosed a July 2026 security incident where attackers used an autonomous AI agent framework to exploit two code execution vulnerabilities in dataset processing pipelines, stealing internal credentials and accessing multiple clusters. This is the first publicly known case of an autonomous AI agent being used to breach a major ML platform, highlighting a new class of AI-driven cyberattacks that traditional defenses may not catch. The agent performed tens of thousands of operations over a weekend, stole internal dataset and service credentials, but public models, datasets, and Spaces were unaffected; Hugging Face has since patched the vulnerabilities and rotated credentials.

telegram · zaihuapd · Jul 22, 00:46

**Background**: Hugging Face is a leading platform for hosting machine learning models, datasets, and demo apps (Spaces). Autonomous AI agents are LLM-powered systems that can independently plan and execute tasks. Code execution vulnerabilities allow attackers to run arbitrary code on a target system.

**Tags**: `#AI security`, `#Hugging Face`, `#cyberattack`, `#AI agent`, `#vulnerability`

---

<a id="item-13"></a>
## [Chinese Tech Firms Recruit Teenagers to Tackle AI Talent Shortage](https://restofworld.org/2026/china-tech-recruiting-teenagers-ai-shortage/) ⭐️ 8.0/10

Chinese tech companies including Tencent, ByteDance, and Geely have launched programs to recruit teenagers as young as 13 for AI training and early employment, aiming to address a severe talent shortage. Tencent's camp targets ages 13-18, ByteDance's non-profit research center selects 30 students aged 16-18 annually, and Geely offers direct hiring after high school with graduate-level pay. This trend signals a strategic shift in AI talent pipeline development, potentially reshaping education and employment pathways in China. With an AI talent gap projected to reach 5 million by 2030, early recruitment could give Chinese firms a competitive edge in the global AI race. Data shows the AI job supply-demand ratio was 3.08:1 from January to May 2026, with AI engineering positions growing 28.4% year-over-year. AI company MiniMax stated that age is no longer a barrier, prioritizing native intelligence and learning ability over traditional credentials.

telegram · zaihuapd · Jul 22, 04:25

**Background**: Chinese tech companies face a severe shortage of AI engineers as demand for AI talent surges. Similar programs exist in the US, such as Palantir's high school internship and Google's initiatives, reflecting a global trend of early talent identification. The programs aim to build long-term talent pools and track student development while enhancing corporate branding.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MiniMax_(company)">MiniMax (company)</a></li>
<li><a href="https://edutimes.com/news/2025/11/202511285559">[Diagnosing the Breakdown of Universities] Palantir ’s “Post-University”...</a></li>

</ul>
</details>

**Tags**: `#AI talent`, `#China tech`, `#talent acquisition`, `#education`, `#AI shortage`

---

<a id="item-14"></a>
## [Moonshot AI seeks $2B funding at $30B valuation](https://t.me/zaihuapd/42706) ⭐️ 8.0/10

Moonshot AI is raising up to $2 billion in new funding at a target valuation of $30 billion, its third funding round in six months, with annual recurring revenue reaching $200 million in April. This rapid valuation growth from $4 billion to $30 billion in six months underscores surging demand for AI chatbots and large language models in China, and signals Moonshot AI's ambition to compete globally. The company is also dismantling its offshore structure to prepare for a Hong Kong IPO and has launched Kimi Work, a general-purpose AI agent for knowledge workers.

telegram · zaihuapd · Jul 22, 05:10

**Background**: Moonshot AI, founded in March 2023 in Beijing, is known for its Kimi chatbot and large language models with industry-leading long-context capabilities. Annual Recurring Revenue (ARR) is a key metric for SaaS startups, representing the annualized value of recurring revenue from subscriptions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi ( chatbot ) - Wikipedia</a></li>
<li><a href="https://www.moonshot.ai/">Welcome to Moonshot AI . Our mission is to seek the optimal...</a></li>
<li><a href="https://trythatllm.com/model-family/moonshot-ai">Moonshot AI | Try That LLM</a></li>

</ul>
</details>

**Tags**: `#AI`, `#funding`, `#startup`, `#large language models`, `#valuation`

---

<a id="item-15"></a>
## [Microsoft Eyes DeepSeek Integration for Copilot Cowork Cost Cuts](https://t.me/zaihuapd/42710) ⭐️ 8.0/10

Microsoft is exploring integrating a fine-tuned version of DeepSeek V4 or other open-source models into its enterprise AI tool Copilot Cowork within weeks, as a lower-cost alternative to existing Anthropic and OpenAI models. The company also announced a shift to usage-based pricing for Copilot Cowork, moving away from unlimited plans. This move signals a potential shift in enterprise AI adoption, as major vendors like Microsoft consider open-source models to reduce costs, which could pressure proprietary model providers to adjust pricing. It also reflects the growing importance of usage-based pricing in AI services, addressing the challenge of heavy users driving up costs. The DeepSeek model would be fully hosted on Azure, ensuring data does not leave Microsoft's cloud and remains under enterprise security and compliance controls. Microsoft executives noted that some users executing hundreds of tasks per week caused costs to skyrocket under unlimited plans, necessitating the pricing change.

telegram · zaihuapd · Jul 22, 07:18

**Background**: DeepSeek V4 is a family of open-source Mixture-of-Experts (MoE) models, with variants like DeepSeek-V4-Pro (1.6 trillion total parameters, 49 billion active) and DeepSeek-V4-Flash (284 billion total, 13 billion active), excelling at coding and agentic tasks with a 1 million token context window. Copilot Cowork is Microsoft's agentic AI assistant for Microsoft 365, which became generally available in June 2026 with usage-based billing via Copilot Credits.

<details><summary>References</summary>
<ul>
<li><a href="https://windowsforum.com/threads/copilot-coworks-usage-pricing-why-agentic-ai-needs-a-meter-deepseek-included.428891/">Copilot Cowork ’s Usage Pricing : Why Agentic AI... | Windows Forum</a></li>
<li><a href="https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-overview-copilot-credits">Usage - Based Billing and Cost Management for Copilot Credits</a></li>
<li><a href="https://unsloth.ai/docs/models/deepseek-v4">DeepSeek - V 4 : How to Run Locally | Unsloth Documentation</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#DeepSeek`, `#AI`, `#Enterprise`, `#Cost Optimization`

---

<a id="item-16"></a>
## [Sandbox Escape in 4 Major AI Coding Agents via Prompt Injection](https://www.bleepingcomputer.com/news/security/cursor-codex-gemini-cli-antigravity-hit-by-sandbox-escapes/) ⭐️ 8.0/10

Researchers at Pillar Security disclosed that Cursor, OpenAI Codex, Google Gemini CLI, and Antigravity are vulnerable to sandbox escape through indirect prompt injection in open-source repositories, allowing arbitrary code execution on developer machines. This vulnerability affects millions of developers using these tools, and the attack vector—indirect prompt injection via workspace files—bypasses traditional sandbox protections, highlighting a critical blind spot in AI agent security. The attack exploits the fact that host tools (e.g., Python interpreter, Git) automatically read and execute workspace files generated by the AI agent, which are not sandboxed. Vendors have released patches: Cursor 3.0.0, Codex CLI v0.95.0, but Google downgraded two Antigravity bugs, citing social engineering requirements.

telegram · zaihuapd · Jul 22, 08:08

**Background**: Indirect prompt injection is a technique where malicious instructions are embedded in data (e.g., README files) that an AI agent reads, causing it to act against the user's intent. Sandbox escape vulnerabilities allow attackers to break out of a restricted environment and execute code on the host system. This disclosure combines both, showing that even if the AI agent runs in a sandbox, the files it writes can be executed by trusted host tools.

<details><summary>References</summary>
<ul>
<li><a href="https://prepfast.in/topics/ai-agents/prompt-injection/">Prompt Injection ( Direct & Indirect ) — AI Coding Agents Interview...</a></li>
<li><a href="https://devops.com/mozilla-shows-the-danger-of-indirect-prompt-injections-in-ai-coding-agents/">Mozilla Shows the Danger of Indirect Prompt Injections in AI Coding ...</a></li>
<li><a href="https://www.ox.security/blog/the-aftermath-of-cve-2025-4609-critical-sandbox-escape-leaves-1-5m-developers-vulnerable/">The aftermath of CVE-2025-4609: Critical Sandbox Escape Leaves...</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#sandbox escape`, `#prompt injection`, `#vulnerability disclosure`, `#developer tools`

---

<a id="item-17"></a>
## [Trump May Restrict US Firms from Using Chinese Open-Weight AI Models](https://t.me/zaihuapd/42715) ⭐️ 8.0/10

Axios reports that the Trump administration is considering new restrictions to discourage US companies from using cost-effective Chinese open-weight AI models like Kimi K3, citing the model's strong performance. This policy shift could fragment the global AI ecosystem, increase costs for US firms, and accelerate the decoupling of US and Chinese AI supply chains. The restrictions may not be a hard ban but rather a soft blockade through procurement rules, entity list threats, and public pressure. Kimi K3 is a 2.8-trillion-parameter open-weight model with a 1-million-token context window.

telegram · zaihuapd · Jul 22, 13:30

**Background**: Open-weight models make their trained parameters publicly available, allowing anyone to download and run them, but they differ from fully open-source models which also include training code and data. Chinese open-weight models like Kimi K3 have recently narrowed the performance gap with US counterparts while being more cost-effective.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://promtable.com/glossary/open-weight-model">Open - weight model — Definition , when to use, and... | Promtable</a></li>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-what-we-finally-opened-bonnet-nicolas-pistorio-n3ulf">Open - weight AI : what if we finally opened the bonnet ?</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#geopolitics`, `#open-weight models`, `#Kimi K3`, `#US-China tech`

---