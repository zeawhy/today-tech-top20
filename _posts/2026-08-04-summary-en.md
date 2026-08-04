---
layout: default
title: "Horizon Summary: 2026-08-04 (EN)"
date: 2026-08-04
lang: en
---

> From 78 items, 14 important content pieces were selected

---

1. [LLMs Reward Expertise, Not Replace It](#item-1) ⭐️ 8.0/10
2. [Swiftlet: Run 80B Qwen in 4.3GB RAM on Mac, 35B on iPhone](#item-2) ⭐️ 8.0/10
3. [OpenAI Highlights Ten Advances in Math and CS](#item-3) ⭐️ 8.0/10
4. [MiniMax H3 Day-0 Support in ComfyUI: Open Weights, Native Audio, 2K Video](#item-4) ⭐️ 8.0/10
5. [Pandoc Creator Reflects on 20 Years of Document Conversion](#item-5) ⭐️ 8.0/10
6. [Andy Pavlo joins ClickHouse to launch ClickHouse Labs](#item-6) ⭐️ 8.0/10
7. [Jane Street's Bonsai: Type-Safe OCaml UI Library](#item-7) ⭐️ 8.0/10
8. [AI Begins to Drastically Cut Customer Service Jobs](#item-8) ⭐️ 8.0/10
9. [Kimi K3 Architecture: Compressed Memory, Depth Attention, Latent Routing](#item-9) ⭐️ 8.0/10
10. [ML Reviewers Call for Desk Rejection of Papers Without Reproducible Code](#item-10) ⭐️ 8.0/10
11. [At least 50 US officers accused of misusing license plate cameras to spy on exes](#item-11) ⭐️ 8.0/10
12. [Nvidia CMP 170HX Mining Card Unlocked to 80GB VRAM, Prices Surge](#item-12) ⭐️ 8.0/10
13. [UK Demands Apple Backdoor for Encrypted Cloud Backups, Limited to UK Citizens](#item-13) ⭐️ 8.0/10
14. [Huawei Unveils 'Tao's Law' for Time-Based Semiconductor Scaling](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [LLMs Reward Expertise, Not Replace It](https://www.seangoedecke.com/llms-reward-expertise/) ⭐️ 8.0/10

The article argues that LLMs are not a substitute for expertise but rather a tool that amplifies the skills of those who already possess deep domain knowledge, challenging the popular narrative that AI makes expertise obsolete. This perspective is significant for the software engineering community as it reframes the role of LLMs in development, suggesting that investment in deep expertise remains crucial and that LLMs can widen the productivity gap between experts and novices. The article uses analogies like an amplifying mirror to illustrate that LLMs reflect the user's own knowledge and interaction quality. It emphasizes that familiarity with a specific codebase is more valuable than general software knowledge when using LLMs effectively.

hackernews · MaxMussio · Aug 3, 21:13 · [Discussion](https://news.ycombinator.com/item?id=49161518)

**Background**: Large Language Models (LLMs) like GPT-4 are AI systems trained on vast text data to generate human-like text. In software engineering, they are used for code generation, debugging, and documentation, but their effectiveness depends on the user's ability to craft precise prompts and evaluate outputs, which requires domain expertise.

**Discussion**: Commenters largely agree with the article's thesis, sharing personal anecdotes that support the idea that LLMs amplify existing expertise. Some note that the effect may be subject to confirmation bias and call for formal studies, while others highlight that even novices can get useful results with simple prompts, suggesting nuance.

**Tags**: `#LLM`, `#software engineering`, `#AI tools`, `#expertise`, `#productivity`

---

<a id="item-2"></a>
## [Swiftlet: Run 80B Qwen in 4.3GB RAM on Mac, 35B on iPhone](https://github.com/leonickson1/Swiftlet) ⭐️ 8.0/10

A new open-source project called Swiftlet demonstrates running an 80B-parameter Qwen model in just 4.3GB of RAM on a Mac, and a 35B model on an iPhone, marking a significant milestone in on-device AI. This achievement pushes the boundaries of what's possible on consumer hardware, potentially enabling powerful AI models to run locally without cloud dependence, which could democratize access to large language models and enhance privacy and offline capabilities. The project leverages streaming weights and efficient memory management to fit large models into limited RAM. It builds upon prior work like TurboFieldfare and is optimized for Apple Silicon, with potential for further speedups by increasing RAM cache on Macs with 24-32GB.

hackernews · leonickson · Aug 3, 16:54 · [Discussion](https://news.ycombinator.com/item?id=49158333)

**Background**: Large language models (LLMs) typically require massive GPU memory, but techniques like quantization, mixture-of-experts (MoE), and streaming weights allow them to run on devices with limited RAM. Qwen3-Next-80B-A3B is an MoE model with 80B total parameters but only 3B active, making it more efficient. Apple Silicon's unified memory architecture is particularly suited for such optimizations.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-qwen-qwen3-next-80b-a3b.html">Qwen3 Next 80B A3B - Amazon Bedrock</a></li>
<li><a href="https://qwen.ai/blog?id=4074cca80393150c248e508aa62983f9cb7d27cd&from=research.latest-advancements-list">Qwen</a></li>
<li><a href="https://blog.starmorph.com/blog/apple-silicon-llm-inference-optimization-guide">Apple Silicon LLM Inference Optimization: The Complete Guide ...</a></li>

</ul>
</details>

**Discussion**: The community response is largely positive, with users praising the progress and practicality. Some note that similar claims have been made before, referencing other projects like anemll's 400B model on iPhone. Others express excitement about the future of on-device AI and plan to test the project themselves.

**Tags**: `#on-device AI`, `#LLM`, `#optimization`, `#Apple Silicon`, `#open source`

---

<a id="item-3"></a>
## [OpenAI Highlights Ten Advances in Math and CS](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 8.0/10

OpenAI published a post titled 'Ten advances in mathematics and theoretical computer science,' highlighting recent achievements in these fields. The post has sparked significant discussion on Hacker News, with 525 points and 804 comments. This announcement underscores the growing role of AI in mathematical discovery, potentially accelerating research and changing how mathematicians work. It also fuels debate about the broader implications of AI's exponential progress across various domains. The post lists ten specific advances, though the details are not provided in the given content. The discussion includes comments about AI's ability to disprove conjectures quickly and the potential for AI to make math proofs more computable.

hackernews · milkshakes · Aug 3, 16:27 · [Discussion](https://news.ycombinator.com/item?id=49157930)

**Background**: AI has been increasingly applied to mathematical and theoretical computer science problems, with models like GPT-4 and specialized systems assisting in theorem proving and conjecture generation. This post by OpenAI highlights recent successes, reflecting a trend where AI is becoming a valuable tool in research, though it still lacks human-like intuition for conjecturing.

**Discussion**: The community is generally impressed but divided on the significance. Some see exponential progress and believe AI's impact is undeniable, while others caution that not all math is automatically solved. There is also humor referencing Douglas Adams, and a note that AI can quickly disprove conjectures through grinding that humans cannot do.

**Tags**: `#AI`, `#Mathematics`, `#Theoretical Computer Science`, `#OpenAI`, `#Research`

---

<a id="item-4"></a>
## [MiniMax H3 Day-0 Support in ComfyUI: Open Weights, Native Audio, 2K Video](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui) ⭐️ 8.0/10

ComfyUI has added day-0 support for MiniMax H3, an open-weights omni-modal generation model that can generate video with native stereo audio at up to 2K resolution and 15 seconds in length. The model accepts text, images, video, and audio as input, and the support is available as of the model's release day. This is significant because it provides the AI/ML community with immediate access to a next-generation open-weights video model within a popular workflow tool, enabling local experimentation and integration. The combination of open weights, native audio, and high-resolution video generation could accelerate innovation in video synthesis and multimodal AI applications. The model's modulation weights, which constitute about 40% of total parameters, can be pruned and replaced with a functionally equivalent lookup table, reducing memory footprint by 66% (from 123.6 GB to 42.5 GB) without loss of output quality. Combined with dynamic VRAM offloading, this enables running the 2K video model locally on a GPU like the RTX 3060.

hackernews · vblanco · Aug 3, 13:34 · [Discussion](https://news.ycombinator.com/item?id=49155629)

**Background**: MiniMax H3 is a general-purpose omni-modal generation model that jointly understands multimodal contexts spanning text, images, video, and audio. Open-weights models are AI models whose core components are publicly released, allowing anyone to download and use them, often with restrictions depending on the license. ComfyUI is a popular node-based interface for AI image and video generation, and day-0 support means the model is integrated into the tool on the same day it is released.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between ...</a></li>
<li><a href="https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui">MiniMax H3 Day - 0 Support in ComfyUI : Open Weights, Native Audio...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>

</ul>
</details>

**Discussion**: Community members reported impressive results, with one user noting that a 10-second 480p video took 10 minutes on a 4070 Ti Super (16 GB VRAM) but the results were spectacular. Another user highlighted that the mouse render was surprisingly good and a significant leap over current SOTA models, though some clips still showed an 'AI smoothening' effect. Some users found that the model still has jank when moving away from normal scenarios, but overall text-to-video quality and speed were praised.

**Tags**: `#AI/ML`, `#Video Generation`, `#Open Weights`, `#ComfyUI`, `#MiniMax`

---

<a id="item-5"></a>
## [Pandoc Creator Reflects on 20 Years of Document Conversion](https://pandoc.org/twenty-years-of-pandoc.html) ⭐️ 8.0/10

John MacFarlane, the creator of Pandoc, published a retrospective article titled 'Twenty Years of Pandoc' on the official Pandoc website, reflecting on the tool's history, design decisions, and the role of Haskell in its development. Pandoc is a widely used open-source document converter, and this retrospective provides valuable insights into its design philosophy and evolution. It highlights how a well-designed tool built on fundamental principles can grow in usefulness over time, especially in an era of rapid AI-driven development. The article explains that Pandoc's architecture, which uses N readers and M writers to support N×M conversions, has been key to its extensibility. MacFarlane also notes that the choice of Haskell, initially made for personal interest, has led to a high-quality but low-volume contributor base.

hackernews · fiddlosopher · Aug 3, 15:04 · [Discussion](https://news.ycombinator.com/item?id=49156750)

**Background**: Pandoc is a universal document converter that can transform files between hundreds of formats, including Markdown, HTML, PDF, DOCX, and EPUB. It is built on Haskell and serves as the core engine for tools like Quarto. The article reflects on how Pandoc has become one of the most popular Haskell programs, supporting over fifty document formats.

<details><summary>References</summary>
<ul>
<li><a href="https://pandoc.org/twenty-years-of-pandoc.html">Twenty Years of Pandoc</a></li>
<li><a href="https://hackage.haskell.org/package/pandoc">pandoc: Conversion between markup formats - Hackage Using the pandoc API Haskell Pandoc: a call to arms : r/haskell - Reddit Twenty years of Pandoc | Noise GitHub - adamConnerSax/knit-haskell: Use Pandoc to write ... 24 Days of Hackage: pandoc : r/haskell - Reddit</a></li>
<li><a href="https://servinagrero.github.io/reproducible_research/02-pandoc_and_basics.html">What is Pandoc ? – Reproducible Research with Quarto</a></li>

</ul>
</details>

**Discussion**: Community comments express appreciation for Pandoc's design and practicality. Users share personal experiences, such as using Pandoc in bash scripts for site generation and integrating it with Typst for PDF creation. Some commenters agree with MacFarlane's observation about Haskell's influence on contributor culture, noting that technology choices can shape community dynamics.

**Tags**: `#pandoc`, `#document conversion`, `#Haskell`, `#open source`, `#software history`

---

<a id="item-6"></a>
## [Andy Pavlo joins ClickHouse to launch ClickHouse Labs](https://clickhouse.com/blog/andy-pavlo-joins-clickhouse) ⭐️ 8.0/10

Andy Pavlo, a prominent database researcher and professor at Carnegie Mellon University, has joined ClickHouse to establish ClickHouse Labs, a new research lab aimed at bridging academia and industry in database research. This move is significant because it brings top academic talent into an open-source OLAP database company, potentially accelerating innovation in database technologies and fostering stronger industry-academia collaboration. It also highlights the growing trend of companies investing in fundamental infrastructure research beyond AI. ClickHouse Labs will focus on advancing database research, with Pavlo continuing his educational efforts, such as his popular CMU lecture series, potentially in a sponsored format. The lab aims to address challenges in OLAP systems, including decoupled storage/compute architectures and ingestion/indexing strategies.

hackernews · nikolay_sivko · Aug 3, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49156011)

**Background**: ClickHouse is an open-source, columnar OLAP database known for its high performance in real-time analytics, leveraging vectorized processing and efficient CPU/memory usage. OLAP databases are designed for analytical queries across large datasets, contrasting with traditional OLTP systems. Pavlo is a well-known figure in the database community, recognized for his research and educational contributions.

<details><summary>References</summary>
<ul>
<li><a href="https://clickhouse.com/docs/academic_overview">Architecture overview - ClickHouse Documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Online_analytical_processing">Online analytical processing - Wikipedia</a></li>
<li><a href="https://clickhouse.com/resources/engineering/olap-database">What is an OLAP database?</a></li>

</ul>
</details>

**Discussion**: Community comments express excitement and support, with users hoping Pavlo will advocate for funding academic database research and continue his lecture series. Some discuss the convergence of OLAP systems like ClickHouse with Trino, and the implications for storage and ingestion architectures. Overall sentiment is positive, with appreciation for corporate research labs outside AI.

**Tags**: `#database`, `#ClickHouse`, `#research`, `#industry-academia`, `#OLAP`

---

<a id="item-7"></a>
## [Jane Street's Bonsai: Type-Safe OCaml UI Library](https://github.com/janestreet/bonsai) ⭐️ 8.0/10

Jane Street has released Bonsai, a new OCaml-based UI library for building performant, reactive web applications, now available on GitHub and opam. It enables type-safe full-stack development by using OCaml on both frontend and backend. Bonsai demonstrates OCaml's viability in frontend development, potentially expanding its adoption beyond backend systems. It offers a type-safe alternative to JavaScript frameworks, which could appeal to functional programming enthusiasts and companies seeking end-to-end type safety. Bonsai is partly inspired by Elm and is used internally at Jane Street for almost all web applications, from corporate directories to trading system monitors. It integrates with Incremental-style frameworks like Incr_dom or React, and the initial release is version 0.17.0 on opam.

hackernews · KolmogorovComp · Aug 3, 08:29 · [Discussion](https://news.ycombinator.com/item?id=49152842)

**Background**: OCaml is a general-purpose, multi-paradigm language known for its strong static typing and functional programming features. Bonsai leverages these features to provide a type-safe UI development experience, allowing developers to share types between client and server, reducing runtime errors and improving code maintainability.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/janestreet/bonsai">GitHub - janestreet / bonsai : A library for building dynamic webapps...</a></li>
<li><a href="https://opam.ocaml.org/packages/bonsai/bonsai.v0.17.0/">The homepage of opam, a package manager for OCaml</a></li>
<li><a href="https://en.wikipedia.org/wiki/OCaml">OCaml - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community discussion is largely positive, with users praising the type-safe full-stack capability and referencing a related podcast episode. However, some users raised concerns about the library's aesthetics and questioned its comparison to Melange, another OCaml-to-JavaScript tool, and whether it sacrifices the JS ecosystem. Additionally, a user noted broken documentation links and inquired about DOM update mechanisms.

**Tags**: `#OCaml`, `#UI framework`, `#full-stack`, `#functional programming`, `#Jane Street`

---

<a id="item-8"></a>
## [AI Begins to Drastically Cut Customer Service Jobs](https://www.solidot.org/story?sid=84994) ⭐️ 8.0/10

Major companies including Microsoft, Uber, and Commonwealth Bank of Australia are using AI-powered chatbots and automated phone systems to replace human customer service roles, leading to significant job cuts. Analysts estimate that nearly half of customer service positions could be affected by 2030. This trend signals a major shift in the labor market, particularly in countries like the US, India, and the Philippines where customer service employs millions. It highlights the growing impact of generative AI on white-collar jobs and raises concerns about job displacement and the need for workforce reskilling. Commonwealth Bank cut hundreds of customer service roles, saving tens of millions of dollars annually. Microsoft reduced its customer service team from about 50,000 to 40,000 employees, with AI saving roughly $750 million per year in customer service costs, according to Judson Althoff. Hyatt laid off 30% of its internal customer service staff in the Americas, and Uber cut 10% of its customer service roles to 'embrace AI'.

rss · Solidot 奇客 · Aug 3, 14:22

**Background**: Customer service has traditionally been a major employment sector, with many Western companies outsourcing roles to English-speaking countries like India and the Philippines. Advances in generative AI have made automated systems more capable of handling routine inquiries, prompting companies to adopt them to cut costs and improve efficiency. However, complex issues still require human support, and the transition is expected to continue.

**Tags**: `#AI`, `#automation`, `#customer service`, `#employment`, `#generative AI`

---

<a id="item-9"></a>
## [Kimi K3 Architecture: Compressed Memory, Depth Attention, Latent Routing](https://newsletter.semianalysis.com/p/kimi-k3-the-manos-the-mythos-the) ⭐️ 8.0/10

SemiAnalysis published a deep technical breakdown of Kimi K3's architecture, detailing innovations in compressed memory, attention across depth, and latent expert routing. The analysis highlights how these mechanisms improve inference performance for the 3T-class open model. Kimi K3 represents a frontier open 3T-class model, and its architectural choices could influence future LLM designs. The focus on inference efficiency and long-context handling addresses key industry challenges, potentially lowering deployment costs and enabling new applications. The architecture scales information flow along sequence length, network depth, and model width. It uses Hybrid Attention combining Kimi Delta Attention (KDA) layers with Gated MLA layers, and employs latent expert routing that decouples routing from the hidden dimension for efficiency.

rss · Semianalysis · Aug 3, 19:42

**Background**: Kimi K3 is the world's first open 3T-class model, offering frontier performance in coding, knowledge work, and reasoning, with native multimodality and 1M context. Attention mechanisms allow models to weigh token importance, while mixture-of-experts (MoE) techniques enable scaling without proportional compute increase. Latent expert routing projects tokens into a lower-dimensional space before expert processing, improving efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.24653">Kimi K3: Open Frontier Intelligence - arXiv.org</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://newsletter.semianalysis.com/p/kimi-k3-the-manos-the-mythos-the">Kimi K3, The Manos, The Mythos, The Legendos</a></li>

</ul>
</details>

**Tags**: `#AI`, `#architecture`, `#inference`, `#Kimi K3`, `#LLM`

---

<a id="item-10"></a>
## [ML Reviewers Call for Desk Rejection of Papers Without Reproducible Code](https://www.reddit.com/r/MachineLearning/comments/1vei12v/its_time_to_desk_reject_papers_that_dont_include/) ⭐️ 8.0/10

A reviewer reported that out of 12 papers reviewed for major ML conferences this year, only 1 provided full code, and 3 of the 5 with partial code had bugs invalidating results. They argue that conferences should desk-reject papers that do not include code capable of reproducing the results. This highlights a reproducibility crisis in ML research, where hidden code undermines scientific integrity and wastes reviewer effort. If adopted, such a policy could incentivize authors to share code, improving verification and trust in published results. The reviewer noted that 7 papers provided no code, and 4 provided only fragments. They emphasized that small bugs in ML code can have large impacts, and that current incentives discourage code sharing because it increases the risk of rejection due to bugs.

reddit · r/MachineLearning · /u/Flaky-Ambition5900 · Aug 3, 16:17

**Background**: Desk rejection is when an editor rejects a paper before peer review, often for clear violations of submission guidelines. In machine learning, reproducibility requires access to code and data to verify results, and metrics like AUROC are commonly used to evaluate model performance. The lack of code sharing has been a long-standing issue in the field, with many papers failing to provide sufficient implementation details.

<details><summary>References</summary>
<ul>
<li><a href="https://scientific-publishing.webshop.elsevier.com/publication-process/paper-rejection-common-reasons/">Paper Rejection: Common Reasons | Elsevier Language Services</a></li>
<li><a href="https://glassboxmedicine.com/2019/02/23/measuring-performance-auc-auroc/">Measuring Performance: AUC ( AUROC ) – Glass Box Medicine</a></li>

</ul>
</details>

**Tags**: `#reproducibility`, `#machine learning`, `#research policy`, `#peer review`, `#open source`

---

<a id="item-11"></a>
## [At least 50 US officers accused of misusing license plate cameras to spy on exes](https://www.washingtonpost.com/technology/2026/08/02/how-police-officers-used-vast-network-cameras-spy-their-exes/) ⭐️ 8.0/10

A Washington Post investigation revealed that at least 50 US law enforcement officers have been accused or charged with misusing license plate recognition systems, such as Flock, for unauthorized surveillance. Among these, 26 cases involved spying on wives, girlfriends, exes, or women they were interested in, and 46 cases used Flock systems. This investigation highlights systemic privacy and ethical failures in the deployment of automated license plate readers (ALPRs) by law enforcement. It underscores the urgent need for stronger regulations, audits, and accountability measures to prevent abuse of surveillance technologies that are increasingly widespread across the US. The investigation found that a Georgia police chief, Michael Steffman, conducted about 600 searches of his ex-girlfriend Bakely and her daughter's license plates before his arrest in November 2025; he died by suicide before his trial in April. Flock claims to have over 120,000 cameras covering more than 6,000 communities, recording 20 billion plate scans monthly, and has introduced an optional 'audit assistance' feature, while only 13 states require audits and at least 8 states criminalize misuse.

telegram · zaihuapd · Aug 3, 09:03

**Background**: Automated license plate recognition (ALPR) systems use cameras to capture and record license plate numbers and vehicle details, often storing data for extended periods. Flock Safety is a major provider of such systems, widely adopted by police departments across the US to aid in crime investigations, but their extensive data collection has raised privacy concerns. The abuse cases involve officers using these systems for personal reasons, such as stalking romantic interests, which is often not explicitly prohibited by law or adequately audited.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://edition.cnn.com/2026/07/26/us/flock-cameras-surveillance-abuse">Inside the growing police use and misuse of Flock’s license ...</a></li>
<li><a href="https://ij.org/police-have-reportedly-used-license-plate-readers-to-stalk-romantic-interests-at-least-14-times-in-recent-years/">Police Have Reportedly Used License Plate Readers to Stalk ...</a></li>

</ul>
</details>

**Tags**: `#surveillance`, `#privacy`, `#law enforcement`, `#license plate cameras`, `#ethics`

---

<a id="item-12"></a>
## [Nvidia CMP 170HX Mining Card Unlocked to 80GB VRAM, Prices Surge](https://finance.sina.com.cn/tech/roll/2026-08-03/doc-inikzqsf4659769.shtml) ⭐️ 8.0/10

Researchers at Arizona State University publicly disclosed an exploit that unlocks Nvidia's CMP 170HX mining card, bypassing OTP fuse locks to increase VRAM up to 80GB and FP32 compute from 0.39 to 94 TFLOPS. The exploit leverages a stack overflow in the GPU's security coprocessor (Falcon) to modify hardware registers. This unlock transforms a previously crippled mining card into a viable AI inference accelerator, significantly lowering the cost barrier for AI workloads. The price surge from 300-500 RMB to 3000-4000 RMB (or $1500 overseas) reflects high demand, and it highlights the security implications of hardware locking mechanisms. The exploit targets the Falcon security coprocessor's DMA unbounded overflow vulnerability, allowing privilege escalation to modify registers. While unlocked cards can run AI image generation and LLM inference on Windows and Linux, long-term stability and unlock limits vary by batch, and not all cards may reach the full 80GB.

telegram · zaihuapd · Aug 3, 11:29

**Background**: The CMP 170HX is a mining-specific GPU released by Nvidia in 2021, based on the GA100 core (same as A100) but with hardware locks (OTP fuses) limiting compute, memory, and PCIe capabilities. These locks were previously considered irreversible. The exploit demonstrates that even hardware-level restrictions can be bypassed, raising concerns about the security of GPU security coprocessors.

<details><summary>References</summary>
<ul>
<li><a href="https://minerstat.com/hardware/nvidia-cmp-170hx">Nvidia CMP 170HX mining calculator ⛏️ | minerstat</a></li>
<li><a href="https://www.nvidia.com/en-us/cmp/">The NVIDIA CMP HX Professional Crypto Mining Processor</a></li>
<li><a href="https://www.usenix.org/conference/usenixsecurity24/presentation/guo-yanan">GPU Memory Exploitation for Fun and Profit - USENIX</a></li>

</ul>
</details>

**Discussion**: The Chinese community has begun verifying the unlock, with reports of successful AI inference on unlocked cards. Some users express excitement about affordable AI hardware, while others caution about potential instability and the risk of buying cards that may not unlock fully.

**Tags**: `#hardware security`, `#GPU`, `#Nvidia`, `#AI inference`, `#exploit`

---

<a id="item-13"></a>
## [UK Demands Apple Backdoor for Encrypted Cloud Backups, Limited to UK Citizens](https://t.me/zaihuapd/42953) ⭐️ 8.0/10

In early September, the UK Home Office issued a new Technical Capability Notice to Apple, demanding a backdoor for encrypted cloud backups, but this time limited to UK citizens' data. This follows a January notice that sought global access, which caused diplomatic tensions with the US. This move could set a precedent for governments to compel tech companies to weaken encryption, potentially undermining global user privacy and security. It also highlights the ongoing conflict between national security demands and tech industry's commitment to end-to-end encryption. Apple previously withdrew its iCloud Advanced Data Protection feature from the UK in February after the earlier global demand. Privacy activists warn that any attempt to force Apple to compromise system security could endanger the private information of users worldwide.

telegram · zaihuapd · Aug 3, 15:40

**Background**: The UK's Investigatory Powers Act 2016, also known as the 'Snoopers' Charter', provides the legal basis for Technical Capability Notices, which require companies to provide specific capabilities to law enforcement. Apple's Advanced Data Protection uses end-to-end encryption to protect iCloud data, meaning even Apple cannot access it, making it a target for government backdoor demands.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Technical_capability_notice">Technical capability notice</a></li>
<li><a href="https://www.gov.uk/government/publications/notices-regime-code-of-practice/notices-regime-code-of-practice-accessible">Notices regime code of practice (accessible) - GOV.UK</a></li>
<li><a href="https://support.apple.com/en-us/108756">How to turn on Advanced Data Protection for iCloud - Apple Support</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#UK government`, `#encryption backdoor`, `#privacy`, `#cloud security`

---

<a id="item-14"></a>
## [Huawei Unveils 'Tao's Law' for Time-Based Semiconductor Scaling](https://t.me/zaihuapd/42966) ⭐️ 8.0/10

At the 2026 International Symposium on Circuits and Systems (ISCAS) in Shanghai, Huawei introduced 'Tao's Law' (τ-law), proposing 'time scaling' as a replacement for traditional geometric scaling. The company also announced that 381 chips have been designed and mass-produced under this principle over the past six years, with a new Kirin chip using logic folding technology slated for release this autumn. This announcement is significant because it proposes a new scaling principle that could extend semiconductor progress beyond Moore's Law, which is approaching physical limits. If validated, it could reshape industry strategies and offer an alternative path for advanced chip manufacturing, especially for companies facing export restrictions. Tao's Law focuses on reducing time constants to achieve multi-level co-optimization across devices, circuits, chips, and systems. Huawei projects that by 2031, high-end chips based on this law could achieve transistor density equivalent to 1.4nm process technology, and the company plans to promote industry development through open collaboration.

telegram · zaihuapd · Aug 4, 08:04

**Background**: Moore's Law, which predicts that the number of transistors on a chip doubles approximately every two years, has driven semiconductor advancement for decades but is now slowing due to physical limits. Geometric scaling, the traditional method of shrinking transistor dimensions, is becoming increasingly difficult and costly. Tao's Law proposes an alternative approach by optimizing time-related parameters, potentially offering a new direction for continued performance gains without relying solely on size reduction.

<details><summary>References</summary>
<ul>
<li><a href="https://news.pedaily.cn/202605/564396.shtml">详解华为“ 韬 定 律 ”：对 半 导 体 行业究竟意味着什么？_ 投资界</a></li>
<li><a href="https://m.gelonghui.com/p/4911792">韬 定 律 开启 半 导 体 新周期：四大增量方向梳理</a></li>
<li><a href="https://baike.baidu.com/item/逻辑折叠技术/67870423">逻辑折叠技术_百度百科</a></li>

</ul>
</details>

**Discussion**: The provided content does not include community comments, so no discussion summary is available.

**Tags**: `#semiconductors`, `#Huawei`, `#Moore's Law`, `#chip design`, `#technology`

---