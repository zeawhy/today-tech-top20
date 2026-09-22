---
layout: default
title: "Horizon Summary: 2026-09-22 (EN)"
date: 2026-09-22
lang: en
---

> From 102 items, 16 important content pieces were selected

---

1. [Alibaba Announces Qwen 4 at Apsara Conference](#item-1) ⭐️ 9.0/10
2. [vLLM v0.30.0 ships Fast Start weight cache and new model support](#item-2) ⭐️ 8.0/10
3. [GPT-6 Astra Helps Break Enigma Message Unsolved Since 2005](#item-3) ⭐️ 8.0/10
4. [Can gzip function as a language model?](#item-4) ⭐️ 8.0/10
5. [Xiaomi Releases MiMo v2.6 Open-Weight MoE Model Family](#item-5) ⭐️ 8.0/10
6. [Bryan Cantrill Analyzes What Sun Microsystems Got Wrong](#item-6) ⭐️ 8.0/10
7. [Blogger Argues Against Using LLMs to Generate Written Content](#item-7) ⭐️ 8.0/10
8. [Essay Argues AI Lacks Wisdom, Over-Reliance Risks Human Judgment](#item-8) ⭐️ 8.0/10
9. [TypeSafe AI Unveils Jev, a 'System One' Decision Model](#item-9) ⭐️ 8.0/10
10. [OpenAI forms math advisory group as AI solves 100+ open problems](#item-10) ⭐️ 8.0/10
11. [Alibaba Plans 5-10 Trillion Parameter AI Model, Unveils Zhenwu V900 Chip](#item-11) ⭐️ 8.0/10
12. [phantom-kv uncensors LLMs via a swappable 18MB KV-cache bank](#item-12) ⭐️ 8.0/10
13. [25 Fields Medalists Warn AI May Be Misaligned with Math Research Goals](#item-13) ⭐️ 8.0/10
14. [Alibaba Unveils Zhenwu V900, Claiming 3x Compute Over M890](#item-14) ⭐️ 8.0/10
15. [DeepSeek and Tsinghua Release DSec Sandbox Platform Serving 3 Million Sandboxes Daily](#item-15) ⭐️ 8.0/10
16. [China Probes DeepSeek and Moonshot Over Data Leaks](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Alibaba Announces Qwen 4 at Apsara Conference](https://www.reddit.com/r/LocalLLaMA/comments/1wmxfjs/qwen_4_announced_at_apsara_conference/) ⭐️ 9.0/10

Alibaba officially announced Qwen 4 at the Apsara Conference, introducing a new generation of its open-source large language model series. The announcement was shared by a community member on r/LocalLLaMA, drawing significant attention from local AI enthusiasts. Qwen is one of the most widely used open-weight LLM families, so a new generation could reshape the open-source model landscape and give developers a stronger alternative to proprietary models. Local AI users and enterprises building on open weights will be directly affected. The Reddit post itself is brief and mainly links to an image from the conference, so specific technical details such as parameter counts, benchmarks, and licensing terms are not yet available. The announcement aligns with Alibaba's pattern of releasing Qwen models at its annual Apsara Conference in Hangzhou.

reddit · r/LocalLLaMA · /u/Salah_H_Hasan · Sep 22, 02:45

**Background**: Qwen, also known as Tongyi Qianwen, is a family of predominantly open-weight large and small language models developed by Alibaba Cloud. The series has become popular in the open-source community for its strong performance and permissive licensing, with versions like Qwen-72B outperforming LLaMA2-70B on many tasks. The Apsara Conference is Alibaba Cloud's premier annual technology summit, held in Hangzhou, where the company showcases its latest AI and cloud innovations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://www.alibabacloud.com/en/apsara-conference/2026-about?_p_lc=1">2026 About Apsara Conference – Alibaba Cloud</a></li>
<li><a href="https://github.com/QwenLM/qwen">GitHub - QwenLM/Qwen: The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud. · GitHub</a></li>

</ul>
</details>

**Tags**: `#Qwen`, `#LLM`, `#Alibaba`, `#open-source`, `#AI announcement`

---

<a id="item-2"></a>
## [vLLM v0.30.0 ships Fast Start weight cache and new model support](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM released v0.30.0, a major update with 762 commits from 315 contributors (104 of them new), adding support for models such as DeepSeek-V4.1-Flash, DeepSeek-V4-Flash-Vision-Exp, GLM-5.3-Flash, K2-Horizon, Cohere Compass, Bailing V3 VL, and Nanbeige4.2. The release also introduces a persistent per-GPU weight-cache daemon called Fast Start, Gumbel-max watermarking, the HiSparse host-resident KV tier, and a large set of performance and quantization improvements. vLLM is one of the most widely used open-source LLM inference and serving engines, so its releases directly shape how production AI infrastructure is deployed. Features like Fast Start and HiSparse target two of the biggest operational pain points — slow engine restarts and GPU memory pressure during long-context decoding — which matters to anyone running large models at scale. Fast Start keeps post-quantized, tensor-parallel-sharded weights in GPU memory and remaps them over CUDA IPC via `--load-format ipc_cache` instead of reloading from disk, now covering FP4 checkpoints and multi-node TP. Other notable details include MXFP8 KV storage for DeepSeek-V4.1-Flash through FlashMLA on SM100, a DeepSeek-V4 CPU backend with AVX512/AMX sparse MLA kernels, and Model Runner V2 changes that cut CUDA graph capture from 12s to 2s and engine init from 28.9s to 8.2s on H200.

github · khluu · Sep 22, 05:20

**Background**: vLLM is an open-source framework for inference and serving of large language models, originally developed at UC Berkeley's Sky Computing Lab and centered on PagedAttention, a memory-management method for transformer key-value caches. It supports continuous batching, distributed inference, quantization, and OpenAI-compatible APIs, and has become one of the most active open-source AI projects. FlashMLA is DeepSeek's library of optimized multi-head latent attention kernels, while MXFP8 is a block floating-point format that shares one exponent across a group of values to save memory and compute.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLLM">VLLM</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/FlashMLA: FlashMLA: Efficient Multi-head Latent Attention Kernels · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/MXFP8">MXFP8</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#model serving`, `#release`, `#AI infrastructure`

---

<a id="item-3"></a>
## [GPT-6 Astra Helps Break Enigma Message Unsolved Since 2005](https://www.cryptocellar.org/bgac/the-mvueh-break.html) ⭐️ 8.0/10

OpenAI's GPT-6 Astra reportedly assisted researcher Leffer in cracking a stubborn Enigma-encrypted message that had resisted decryption since 2005, in what is described as a two-day collaboration. The breakthrough was possible because the message used a completely different key from the rest of that day's traffic, the original transcription contained errors, and the left rotor turned over at letter 72, which is rare and defeats standard crib attacks. This case illustrates how large language models like GPT-6 Astra are increasingly being applied to hard cryptographic and historical puzzles, potentially changing how researchers approach long-standing unsolved problems. It also fuels broader debate about AI's growing capabilities and whether human expertise in fields like cryptanalysis is becoming replaceable. The actual decrypted message reads approximately: 'Please specify the route of march. I am in Rosenow, Rosenow. Immediate reply by radio. Waschbusch,' with several misspellings in the original German ciphertext. The message's unusual key and the rare rotor turnover at letter 72 explain why it remained unsolved for nearly two decades, and the decryption was a collaboration between researcher Leffer and Astra rather than a fully autonomous AI solve.

hackernews · sohkamyung · Sep 22, 13:52 · [Discussion](https://news.ycombinator.com/item?id=49801324)

**Background**: The Enigma machine was a German rotor cipher device used extensively in World War II; although it was believed unbreakable, Allied cryptanalysts led by Alan Turing at Bletchley Park exploited procedural flaws and operator mistakes to decrypt many messages. Some individual messages, however, remained unsolved for decades due to unusual key settings, transcription errors, or rare rotor behavior. GPT-6 Astra is OpenAI's most capable large language model, released in September 2026, designed for complex reasoning, coding, and research tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Enigma_machine">Enigma machine - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cryptanalysis_of_the_Enigma">Cryptanalysis of the Enigma - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT - 6 Astra - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters corrected the sensationalized headline, noting the message was broken with 'good help' from Astra rather than by the AI alone, and highlighted technical reasons for its long resistance: a unique key, transcription errors, and a rare rotor turnover at letter 72. Some expressed unease about AI making even the smartest humans replaceable, while others noted a recent Veritasium video on Enigma and questioned the significance of the 2005 date.

**Tags**: `#AI`, `#cryptography`, `#Enigma`, `#OpenAI`, `#GPT-6`

---

<a id="item-4"></a>
## [Can gzip function as a language model?](https://nathan.rs/posts/gzip-lm/) ⭐️ 8.0/10

An article on nathan.rs investigates whether the gzip compression algorithm can function as a language model, sparking a 307-point Hacker News discussion with 120 comments. The piece explores compression-based classification and its conceptual ties to language modeling research. This matters because it connects information theory and machine learning, showing how classical compression tools can approximate language modeling tasks and offering a low-resource alternative to large neural models. It also highlights the deep theoretical link between compression and prediction that underpins modern AI research. Community members note that gzip can classify text by compressing a test file together with topic-specific corpora and picking the smallest output, a technique pioneered by Witten's group at Waikato. Critics point out that the search space for generating continuations is far too large to explore meaningfully, so results only provide a lower bound on gzip's plausibility-testing ability.

hackernews · networked · Sep 22, 06:08 · [Discussion](https://news.ycombinator.com/item?id=49797323)

**Background**: gzip is a widely used compression utility released in 1992, based on the DEFLATE algorithm combining LZ77 and Huffman coding. Language models are computational models that predict sequences in natural language, and recent research such as Google's 'Language Modeling Is Compression' paper has shown that compression and prediction are mathematically equivalent. Compression-based classification uses the normalized compression distance to measure similarity between files.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gzip">gzip - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Language_modeling">Language modeling</a></li>
<li><a href="https://github.com/ranfysvalle02/compressed-classification">GitHub - ranfysvalle02/ compressed - classification · GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters shared practical gzip classification examples and referenced related research, including Google's 'Language Modeling Is Compression' paper and the Gibbs randomness-compression proposition. Some raised concerns about the limited search space, while others humorously noted that Winrar is more profitable than OpenAI.

**Tags**: `#compression`, `#language-modeling`, `#gzip`, `#information-theory`, `#machine-learning`

---

<a id="item-5"></a>
## [Xiaomi Releases MiMo v2.6 Open-Weight MoE Model Family](https://mimo.xiaomi.com/mimo-v2-6) ⭐️ 8.0/10

Xiaomi's MiMo team released the MiMo-V2.6 series on September 22, open-sourcing two models: Flash with 309B total / 15B activated parameters and Pro with 1.02T total / 42B activated parameters, both available on Hugging Face. The release includes an unusually transparent realtime training dashboard and a detailed technical report covering methodology and over 7,000 RL environments. This is a significant open-weight LLM release from a major consumer electronics company, pushing trillion-parameter scale into the open ecosystem and intensifying competition among Chinese AI labs. Its transparent training methodology raises the bar for how open models are documented and shared. The models use a Mixture-of-Experts architecture, with Pro at 1.02T total but only 42B activated parameters, and were trained across 750,000 RL trajectories in programming, vision, and CFT tasks. Community benchmarks show MiMo-V2.6-Pro scoring 34.9 on Terminal Bench 4.0, well behind leading closed models like GPT 6 Astra at 59.6.

hackernews · volf_ · Sep 21, 20:12 · [Discussion](https://news.ycombinator.com/item?id=49792730)

**Background**: Mixture-of-Experts (MoE) is an architecture that routes each input through only a subset of the model's parameters, allowing models to scale to enormous total size while keeping per-token compute manageable. Open-weight models are those whose trained parameters are publicly downloadable, though they may not include training data or code. Xiaomi's MiMo team is the company's dedicated AI research unit, and this release follows earlier MiMo versions.

<details><summary>References</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo-V2.6 | Xiaomi</a></li>
<li><a href="https://www.kucoin.com/news/flash/xiaomi-releases-mimo-v2-6-with-trillion-parameter-models-and-7-000-rl-environments">Xiaomi Releases MiMo-V2.6 with Trillion-Parameter Models and 7,000+ RL Environments | KuCoin</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>

</ul>
</details>

**Discussion**: Commenters praised Xiaomi's transparency, especially the realtime training dashboard as a learning tool, while others debated the US-China AI race with energy as a key bottleneck. Some expressed skepticism about benchmarks, and users shared links to Hugging Face model cards and test outputs.

**Tags**: `#LLM`, `#open-weights`, `#Mixture-of-Experts`, `#AI-research`, `#Xiaomi`

---

<a id="item-6"></a>
## [Bryan Cantrill Analyzes What Sun Microsystems Got Wrong](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) ⭐️ 8.0/10

Bryan Cantrill, a former Sun Microsystems engineer and co-creator of DTrace, published a retrospective essay titled "What Sun got wrong" on his personal blog, examining the strategic and technical missteps that led to the company's decline. The post sparked a large Hacker News discussion with 653 points and 375 comments from industry veterans sharing their own experiences and perspectives. Sun Microsystems was one of the most influential computing companies of the 1980s and 1990s, and its decline offers enduring lessons about business strategy, technology commoditization, and the dangers of ignoring market shifts. Cantrill's insider perspective, combined with the community discussion, provides valuable insight for today's engineers and founders navigating similar competitive pressures. Cantrill worked at Sun Microsystems and later at Oracle after its acquisition of Sun, and co-developed DTrace, a dynamic tracing framework for production systems, alongside Adam Leventhal and Mike Shapiro. The community discussion highlights specific missteps such as briefly cancelling Solaris on x86 in 2002 and failing to strike a deal with Google in 2002 over server count disclosure.

hackernews · chmaynard · Sep 21, 14:03 · [Discussion](https://news.ycombinator.com/item?id=49787436)

**Background**: Sun Microsystems was an American technology company founded in 1982 that developed and sold computers, computer hardware, and software, becoming famous for its SPARC workstations, Solaris operating system, and Java platform. The company was acquired by Oracle in 2010, ending its existence as an independent firm. Bryan Cantrill is a software engineer known for his work at Sun and Oracle and is now co-founder and CTO of Oxide Computer Company.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sun_Microsystems">Sun Microsystems - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bryan_Cantrill">Bryan Cantrill - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Bryan_Cantrill">Bryan Cantrill</a></li>

</ul>
</details>

**Discussion**: Commenters broadly agreed that Sun's engineering was exceptional but its business execution was poor, with one noting that Sun "was never interested in running a business" and cared more about building amazing technology. Others shared concrete grievances, such as the painful enterprise sales process compared with Dell, and pointed to specific strategic errors like cancelling Solaris on x86 and failing to close a deal with Google. A few drew parallels to today's high-valuation tech stocks, warning of similar bubble dynamics.

**Tags**: `#Sun Microsystems`, `#computing history`, `#business strategy`, `#Hacker News`, `#technology industry`

---

<a id="item-7"></a>
## [Blogger Argues Against Using LLMs to Generate Written Content](https://blog.colinbreck.com/i-dont-want-to-read-what-you-didnt-write/) ⭐️ 8.0/10

Colin Breck published a blog post titled "I don't want to read what you didn't write" arguing that using LLMs to generate written content undermines authentic communication, and the post sparked a highly engaged Hacker News discussion with 904 points and 382 comments. As LLMs become embedded in software engineering workflows, this debate touches on how teams write design documents, pull request descriptions, and technical communication, raising questions about trust, information transfer, and the value of human authorship. Commenters raised an information-theoretic argument that writing is the transfer of semantic information from one brain to another, and that an LLM cannot fill in semantic bits the author never provided; others noted that AI-generated pull request descriptions have become so verbose that reviewers feel forced to read pages of text for a 20-line change.

hackernews · mooreds · Sep 21, 22:30 · [Discussion](https://news.ycombinator.com/item?id=49794330)

**Background**: Large language models (LLMs) such as ChatGPT and Claude can generate fluent text on demand, and they are increasingly used to draft documentation, summaries, and code review comments. This has prompted debate about whether AI-generated writing genuinely conveys the author's intent or merely produces plausible-sounding filler, and tools marketed as "AI humanizers" now exist to make such text sound more natural.

<details><summary>References</summary>
<ul>
<li><a href="https://www.alphaxiv.org/overview/2309.11210">Speak While You Think: Streaming Speech Synthesis During Text ...</a></li>
<li><a href="https://notegpt.io/ai-humanizer">Free AI Humanizer – 100% Human Text & No Sign-up, Unlimited</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was largely sympathetic to the article's thesis, with one commenter offering an information-theoretic framing that an LLM cannot supply semantic information the author never had, and another complaining that AI-generated pull request descriptions are now so bloated that reviewers cannot afford to skip them. A contrarian commenter argued that LLMs can still serve as useful sparring partners for structuring thoughts, provided the author proofreads and rewrites until the text genuinely conveys the intended information.

**Tags**: `#AI`, `#Writing`, `#LLM`, `#Communication`, `#Software Engineering`

---

<a id="item-8"></a>
## [Essay Argues AI Lacks Wisdom, Over-Reliance Risks Human Judgment](https://alexn.org/blog/2026/09/22/ai-has-no-wisdom-and-neither-will-you/) ⭐️ 8.0/10

A blog essay titled "AI Has No Wisdom and Neither Will You" argues that AI systems lack genuine wisdom and that humans who over-rely on them risk losing their own. The piece sparked a 430-comment Hacker News discussion (308 points) debating the limits of AI for knowledge work and software development. The debate touches on a growing concern in the AI/ML and software engineering communities: that offloading cognitive tasks to AI may erode institutional knowledge and human expertise over time. It matters because the industry is rapidly adopting AI coding agents and assistants, and the long-term effects on skill development and maintainability remain unclear. Commenters noted that code maintainability and good architecture lack good measurable metrics, making it hard to prove whether AI-assisted development degrades quality. One commenter with 20 years of experience described building a MongoDB-like database in two weeks using Claude, Kiro, Qwen Coder, and Cursor, then spending much longer reworking internals after studying relational algebra and database design.

hackernews · dimonomid · Sep 22, 12:11 · [Discussion](https://news.ycombinator.com/item?id=49799965)

**Background**: The essay's title plays on the idea that wisdom is not the same as knowledge or pattern matching — it requires judgment, experience, and context that current AI models do not possess. Hacker News is a popular technology forum where engineers and researchers debate industry trends, and a 430-comment thread with 308 points indicates unusually high engagement. The discussion reflects broader anxiety about AI's role in replacing or augmenting human cognitive work.

**Discussion**: Commenters were divided: some warned that offloading wisdom-gathering to AI causes slow institutional knowledge decay, comparing it to the outsourcing of manufacturing. Others argued that AI coding agents can produce maintainable code if properly directed, and one commenter predicted that within 5-10 years most human developers will not touch a single line of code.

**Tags**: `#AI`, `#wisdom`, `#software-engineering`, `#institutional-knowledge`, `#Hacker-News`

---

<a id="item-9"></a>
## [TypeSafe AI Unveils Jev, a 'System One' Decision Model](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 8.0/10

TypeSafe AI has unveiled Jev, the first of a new class of 'System One' models (also called decision models) that accept text input but return typed probabilistic outputs — floating point numbers for yes/no questions, choice distributions, and scores — along with confidence values, rather than generating text. The first model is priced at just $0.042 per million input tokens with output charged at zero, making it cheaper than OpenAI's GPT-5 Nano. This introduces a novel paradigm that reframes LLMs as decision-making functions rather than conversational text generators, which could meaningfully change how AI is applied to classification, ranking, and automation tasks in software. Because it is extremely fast and cheap, it may lower the cost barrier for embedding AI decisions directly into production systems. Jev supports three question types: 'Noul' (Bernoulli) yes/no questions returning a 0–1 confidence, choice questions returning a probability distribution over provided options, and score questions returning a float along a numeric range; questions are evaluated in parallel against a single 'state' object. A notable caveat is that Jev is a pure black box — it returns only numbers with no explanation or justification, raising concerns about hidden bias in high-stakes uses like ranking job applicants.

rss · Simon Willison · Sep 21, 23:09

**Background**: Traditional large language models generate text token by token and are billed per input and output token, with output typically costing more. TypeSafe AI is positioning Jev as a 'frontier-intelligence function call' for machine-native automation: unstructured state in, typed probabilistic decisions out. The 'System One' name contrasts with slower, deliberative 'System Two' reasoning, while the alternative label 'decision model' emphasizes its role in classification-style tasks such as spam detection, labeling, prioritization, and search reranking.

<details><summary>References</summary>
<ul>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models & Jev - TypeSafe AI Blog</a></li>
<li><a href="https://www.requesty.ai/blog/typesafe-jev-explained">TypeSafe Jev explained: how it works, LLM differences and... | Requesty</a></li>
<li><a href="https://mchromiak.github.io/articles/2026/Sep/17/Jev-Typed-Decisions-for-Enterprise-AI/">Jev: Typed decisions for enterprise AI - Michał Chromiak's blog</a></li>

</ul>
</details>

**Discussion**: Simon Willison, a highly respected commentator, finds the 'decision model' framing useful for understanding where to apply Jev, especially classification and search reranking, but expresses discomfort that it represents a further regression toward black-box machine learning. He warns that bias concerns should be front and center, hoping nobody uses Jev to rank job applicants since the floating point number could conceal unseen bias.

**Tags**: `#LLM`, `#AI Models`, `#Decision Models`, `#TypeSafe AI`, `#Probabilistic Inference`

---

<a id="item-10"></a>
## [OpenAI forms math advisory group as AI solves 100+ open problems](https://techcrunch.com/2026/09/21/openai-forms-math-advisory-group-as-its-ai-resolves-more-than-100-open-problems/) ⭐️ 8.0/10

OpenAI has formed an independent Advisory Group on Mathematics and Artificial Intelligence to guide the review and communication of emerging AI results, following its AI system resolving more than 100 open mathematical problems. The group is explicitly not given leeway to slow down or redirect OpenAI's ongoing mathematical research. This signals a major milestone in AI-driven mathematical discovery, potentially shifting how mathematical research is conducted and validated. It also raises governance questions about who reviews and communicates AI-generated mathematical results, affecting mathematicians, AI researchers, and the broader scientific community. The advisory group is independent and can advise but cannot make company decisions, and it has no authority to slow or redirect OpenAI's mathematical research. The announcement comes as OpenAI's AI system reportedly resolved over 100 open problems, though the specific problems and verification methods have not been detailed in the provided content.

rss · TechCrunch AI · Sep 21, 20:15

**Background**: Automated theorem proving is a subfield of automated reasoning in which computer programs attempt to prove mathematical theorems, with systems such as Lean, Coq, Isabelle, and Mizar serving as proof assistants. In recent years, AI models have increasingly been applied to mathematics, moving from simple problem solving toward generating and verifying original mathematical results. OpenAI's advisory group is meant to build a formal bridge to the mathematics community so that AI-produced results are reviewed and communicated responsibly.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/advisory-group-on-mathematics-and-ai/">Advisory Group on Mathematics and Artificial Intelligence | OpenAI</a></li>
<li><a href="https://kingy.ai/blog/openai-math-advisory-group-control/">OpenAI ’s Math Advisory Group : Who Controls Mathematics ?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving</a></li>

</ul>
</details>

**Discussion**: Commentary around the announcement has been skeptical, with observers noting that the advisory group can advise but cannot make company decisions, and some mathematicians object to being treated as an AI benchmark. The main concern is that the group lacks real authority to slow or redirect OpenAI's research, making its oversight role largely symbolic.

**Tags**: `#OpenAI`, `#AI for Mathematics`, `#Automated Theorem Proving`, `#AI Research`, `#Mathematical Discovery`

---

<a id="item-11"></a>
## [Alibaba Plans 5-10 Trillion Parameter AI Model, Unveils Zhenwu V900 Chip](https://www.reddit.com/r/LocalLLaMA/comments/1wmyh9z/alibaba_plans_ai_model_with_5_trillion_to_10/) ⭐️ 8.0/10

At its annual Apsara Conference in Hangzhou on September 22, Alibaba CEO Eddie Wu announced plans to train an AI model with 5 to 10 trillion parameters and unveiled the Zhenwu V900, a new in-house AI chip for both training and inference. The company also said it aims to operate more than 20 gigawatts of global data center capacity by 2032. If realized, a 5-10 trillion parameter model would be among the largest ever attempted, pushing the frontier of AI scaling while Alibaba's custom silicon reduces its dependence on Nvidia amid tightening export controls. The combination of extreme model scale and in-house hardware signals that Chinese cloud providers are building full-stack AI ecosystems to compete globally. The Zhenwu V900 reportedly delivers three times the performance of its predecessor and is slated for mass production in the first quarter of 2027, with new server CPUs planned for the third quarter of 2027. Alibaba has not disclosed the training timeline, cost, or whether the 5-10 trillion parameter model's weights will be released openly.

reddit · r/LocalLLaMA · /u/tengo_harambe · Sep 22, 03:35

**Background**: Parameters are the internal numerical weights a neural network learns during training; larger parameter counts generally correlate with greater capability, though scaling laws show diminishing returns and rising costs. Alibaba's Qwen family of models, including the previewed 2.4-trillion-parameter Qwen3.8-Max, has become a widely used open-weight alternative to Western models. The Zhenwu V900 is designed by Alibaba's T-Head semiconductor unit as part of a broader trend of Chinese tech firms developing domestic AI accelerators to work around US export restrictions on advanced chips.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/alibaba-ai-model-zhenwu-v900-chip/">Alibaba plans AI model with 5 -10 trillion parameters , unveils Zhenwu...</a></li>
<li><a href="https://www.cnbc.com/2026/09/22/alibaba-ai-alibabacloud-zhenwu-v900-.html">Alibaba shares jump as new AI chip , data center buildout plans unveiled</a></li>
<li><a href="https://www.trendforce.com/news/2026/09/22/news-alibaba-unveils-ai-chip-zhenwu-v900-for-1q27-mass-production-maps-out-new-server-cpus-for-3q27/">[News] Alibaba Unveils AI Chip Zhenwu V900 for 1Q27 Mass...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#large language models`, `#Alibaba`, `#AI chips`, `#scaling`

---

<a id="item-12"></a>
## [phantom-kv uncensors LLMs via a swappable 18MB KV-cache bank](https://www.reddit.com/r/LocalLLaMA/comments/1wms904/uncensor_an_llm_without_touching_weights_inject_a/) ⭐️ 8.0/10

A developer released phantom-kv, a refusal-removal system that injects a small trained bank of key/value tensors (~18MB) directly into a model's KV cache as context, without modifying any model weights. Because the graft lives only in the input channel, it can be unloaded per request, leaving the base model byte-identical, and it supports hot-swappable capability modes such as a defensive 'blue pill' and an offensive 'red pill'. This reframes uncensoring from a permanent checkpoint edit into a per-request, hot-swappable capability mode, which could let a single set of weights serve multiple deployment roles without re-flashing or re-quantizing. It also sidesteps the fragility of prior methods like weight-space abliteration and activation-space projection, which commit changes permanently or patch the model's signal path at boot. The graft is trained offline against the model's own objective (comply on harmful prompts, preserve behavior on harmless ones) and avoids the single 1-D refusal-direction assumption, forwarding-pass hooks, and per-architecture rebuilds. Self-auditing with an 8B judge model found that lexical refusal-suppression metrics over-claim compliance, the graft fades with a roughly 2–4k token half-life in long sessions (mitigated by a measured re-injection cadence), and answers retain legal/ethical framing.

reddit · r/LocalLLaMA · /u/Anony6666 · Sep 21, 22:55

**Background**: The KV cache is the memory of key/value tensors that attention mechanisms read as prior context during inference, so injecting content there influences the model through the same channel as conversation history. Prior refusal-removal approaches include abliteration, which projects out refusal directions from weight matrices, and activation-space projection, which subtracts a refusal direction at runtime per token and per layer. phantom-kv instead ships as megabytes of cache content rather than a new checkpoint, and the author presents it as a deployment-controlled mode rather than a jailbreak.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/abliteration">Abliteration in LLMs: Removing Refusal Behavior</a></li>
<li><a href="https://www.lesswrong.com/posts/jGuXSZgv6qfdhMCuJ/refusal-in-llms-is-mediated-by-a-single-direction">Refusal in LLMs is mediated by a single direction - LessWrong</a></li>
<li><a href="https://toytag.net/posts/efficient-llm/">Efficient Large Language Model Inference · @toytag.net</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#uncensoring`, `#KV-cache`, `#refusal-removal`, `#local-llama`

---

<a id="item-13"></a>
## [25 Fields Medalists Warn AI May Be Misaligned with Math Research Goals](https://t.me/zaihuapd/43973) ⭐️ 8.0/10

A group of 25 Fields Medalists, including Terence Tao and Deng Yu, issued a joint statement warning that the rapid deployment of AI to solve mathematical problems could cause AI development goals to become 'severely misaligned' with the core aims of mathematical research. The statement argues that using mathematical problem-solving as a benchmark for AI capability may harm mathematical research and the broader academic ecosystem. The statement carries unusual weight because it comes from the world's most decorated mathematicians, and it could shape how universities, journals, and funders evaluate AI-generated mathematical work. It also raises broader questions about whether optimizing AI for benchmark performance distorts the goals of the fields it is applied to. The statement emphasizes that the core of mathematical research is forming conceptual understanding and new insights rather than merely obtaining answers, and warns that AI-generated output at scale could compress the time available for verification, communication, and citing prior work while raising issues of authorship and plagiarism. It also acknowledges that AI could improve research efficiency, with the outcome depending on how people choose to use the technology.

telegram · zaihuapd · Sep 22, 03:00

**Background**: The Fields Medal is awarded every four years by the International Mathematical Union to up to four mathematicians under 40, and is widely described as the 'Nobel Prize of Mathematics'; 68 people have received it as of 2026. Large language models have improved markedly in recent years at solving mathematical problems, prompting debate over whether such benchmark performance reflects genuine mathematical understanding. The joint statement reflects growing concern within the mathematics community about AI's role in research ethics, publishing, and academic credit.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fields_Medal">Fields Medal</a></li>
<li><a href="https://otontechnology.com/leiden-declaration-ai-mathematics-ethics/">Leiden Declaration Demands AI Transparency in Mathematics</a></li>
<li><a href="https://www.allscientificjournal.com/assets/archives/2026/vol11issue2/11055.pdf">The impact of AI on mathematical research</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Mathematics`, `#Research Ethics`, `#Academic Publishing`, `#Fields Medal`

---

<a id="item-14"></a>
## [Alibaba Unveils Zhenwu V900, Claiming 3x Compute Over M890](https://finance.sina.com.cn/stock/bxjj/2026-09-22/doc-inissitf7048094.shtml) ⭐️ 8.0/10

At the 2026 Yunqi Conference, Alibaba's chip unit T-Head unveiled the Zhenwu V900, a train-and-inference integrated AI chip it calls the most powerful domestic Chinese AI chip, claiming 3x the compute of its Zhenwu M890 predecessor and scalability to a single 500,000-card cluster. CEO Wu Yongming also said the self-developed M890 supernode already supports inference for 2-trillion-parameter models and will scale onto Alibaba Cloud this quarter. The announcement signals that China's domestic AI chip ecosystem is maturing fast enough to challenge Nvidia's constrained presence in the market, with Bernstein Research predicting Huawei will hold 50% of China's AI chip market in 2026 while Nvidia's share shrinks to about 8%. If the V900's claims hold up, it could give Chinese cloud providers a viable path to train and serve frontier-scale models without relying on export-restricted foreign hardware. According to IT之家's on-site report, the Zhenwu V900 supports 216GB of memory and 1200GB/s of inter-die bandwidth, though full specifications for the V900 and the follow-up J900 remain undisclosed. All performance figures are vendor-sourced and have not been independently benchmarked, and Alibaba also set ambitious targets: Qwen models of 5-10 trillion parameters and over 20GW of global Alibaba Cloud datacenter capacity by 2032.

telegram · zaihuapd · Sep 22, 03:30

**Background**: T-Head (平头哥) is Alibaba's in-house semiconductor design unit, and the Zhenwu series is its line of AI accelerators for training and inference. A "supernode" refers to a tightly interconnected cluster of many accelerators that acts as one large compute unit, a design Nvidia has popularized with systems like NVL72 and that Chinese vendors such as Huawei are also pursuing with CloudMatrix 384. China's AI chip push is driven largely by U.S. export controls that limit access to top Nvidia GPUs, making domestic alternatives strategically important.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/1/005/602.htm">最强国产 AI 芯 片 阿里 平 头 哥 真 武 V 900 ...</a></li>
<li><a href="https://tech.ifeng.com/c/8tHMSnuzdDJ">真 武 M890只是开胃菜！阿里 平 头 哥 首曝路线图： V 900 +J900两年两代</a></li>
<li><a href="https://www.chip37.com/m/article/20260922-3032.shtml">chip37.com/m/article/20260922-3032.shtml</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#Alibaba`, `#semiconductor`, `#AI infrastructure`, `#cloud computing`

---

<a id="item-15"></a>
## [DeepSeek and Tsinghua Release DSec Sandbox Platform Serving 3 Million Sandboxes Daily](https://arxiv.org/abs/2609.22978) ⭐️ 8.0/10

DeepSeek-AI and Tsinghua University jointly released a technical report on DeepSeek Elastic Compute (DSec), a sandbox infrastructure that supports large-scale agent training and evaluation. DSec provides four backend types — FnCall, containers, Firecracker microVMs, and full VMs — through a unified SDK, and serves roughly 3 million sandbox instances per day with peak concurrency exceeding 380,000. Agent training and reinforcement learning increasingly depend on massive numbers of isolated execution environments, and DSec shows how a production-grade sandbox platform can be built to sustain that scale. The architectural choices and performance numbers offer a concrete reference for teams building agent training infrastructure, and reinforce DeepSeek's push into open systems work alongside its models. A single production unit uses about 160 nodes, creates sandboxes at over 5,000 per second, and can host up to 3,200 containers or 800 microVMs per node. By loading EROFS images on demand from the 3FS distributed file system instead of pulling full Docker images, DSec achieves 1.7x faster task completion and 57% less disk write, while memory sharing and reclamation cut peak memory usage by about 40%.

telegram · zaihuapd · Sep 22, 04:45

**Background**: Sandboxes are isolated execution environments used to safely run untrusted code, and agent training frameworks need them at enormous scale to let models interact with tools, operating systems, and software tasks. Firecracker is a lightweight virtualization technology that creates microVMs with fast startup and low memory overhead, while EROFS is a read-only Linux file system optimized for compression and efficient I/O. 3FS is DeepSeek's own high-performance distributed file system designed for AI training and inference workloads, and DSec combines these pieces into a unified platform that decouples stateful rollout execution from preemptible GPU training.

<details><summary>References</summary>
<ul>
<li><a href="https://firecracker-microvm.github.io/">Firecracker</a></li>
<li><a href="https://en.wikipedia.org/wiki/EROFS">EROFS - Wikipedia</a></li>
<li><a href="https://medium.com/@drishabh521/deepseek-ai-unveils-fire-flyer-file-system-3fs-a-high-performance-distributed-file-system-for-1dac7e4b8d21">DeepSeek AI Unveils Fire-Flyer File System ( 3 FS )... | Medium</a></li>

</ul>
</details>

**Tags**: `#agent-training`, `#sandbox-infrastructure`, `#systems`, `#reinforcement-learning`, `#DeepSeek`

---

<a id="item-16"></a>
## [China Probes DeepSeek and Moonshot Over Data Leaks](https://www.theinformation.com/articles/china-probes-deepseek-moonshot-potential-data-leaks-anthropic) ⭐️ 8.0/10

China's internet regulator is investigating DeepSeek and Moonshot AI over potential data leaks, following Anthropic's September 10 report accusing seven Chinese companies of large-scale misuse of its Claude model. Anthropic's 154-page report specifically cited DeepSeek for forwarding a request from an engineer working on a police surveillance system to Claude. This investigation highlights growing tensions between Chinese AI developers and foreign model providers, and could reshape how Chinese companies access overseas AI services. It also signals that Beijing is taking data privacy and cross-border data flows seriously, with potential regulatory consequences for two of China's most prominent AI startups. Anthropic's report names seven Chinese companies and provides specific examples, including DeepSeek forwarding a police surveillance engineer's request to Claude. The investigation is being conducted by China's internet regulator, though no formal charges or penalties have been announced yet.

telegram · zaihuapd · Sep 22, 14:37

**Background**: DeepSeek is a Hangzhou-based AI company owned by hedge fund High-Flyer, known for its open-weight large language models. Moonshot AI, whose Chinese name means 'dark side of the moon,' is another major Chinese AI startup. Anthropic is an American AI safety company that develops the Claude series of large language models, which are widely used via API by developers worldwide.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://www.moonshot.ai/">Welcome to Moonshot AI . Our mission is to seek the optimal...</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#data privacy`, `#DeepSeek`, `#Moonshot AI`, `#Anthropic`

---