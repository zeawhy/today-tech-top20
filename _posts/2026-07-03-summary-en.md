---
layout: default
title: "Horizon Summary: 2026-07-03 (EN)"
date: 2026-07-03
lang: en
---

> From 42 items, 8 important content pieces were selected

---

1. [Wordgard: New Rich-Text Editor from ProseMirror Creator](#item-1) ⭐️ 8.0/10
2. [Crustc: Entire Rust Compiler Translated to C](#item-2) ⭐️ 8.0/10
3. [CDD recovers finetuning data from LLMs using only logits](#item-3) ⭐️ 8.0/10
4. [Anthropic Accuses Alibaba of Massive Distillation Attack on Claude](#item-4) ⭐️ 8.0/10
5. [Huawei Launches Atlas 350 Accelerator with ShengTeng 950PR](#item-5) ⭐️ 8.0/10
6. [Huawei Mate 80 Pro Gaming Efficiency Beats Snapdragon 8 Gen3](#item-6) ⭐️ 8.0/10
7. [NASA Launches Rescue Satellite to Save Aging Swift Telescope](#item-7) ⭐️ 8.0/10
8. [Tencent's Atuin AI beats Mythos in CyberGym benchmark](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Wordgard: New Rich-Text Editor from ProseMirror Creator](https://wordgard.net/) ⭐️ 8.0/10

Wordgard is a new in-browser rich-text editor released by the creator of ProseMirror, offering improved developer experience and static typing support. This matters because it provides a modern alternative to ProseMirror with better TypeScript integration, potentially simplifying development for teams that need statically-typed document models. Wordgard shares many concepts with ProseMirror but is not an upgrade path; switching requires significant rework. The editor is designed with a focus on developer experience and static typing.

hackernews · indy · Jul 3, 08:50 · [Discussion](https://news.ycombinator.com/item?id=48772573)

**Background**: ProseMirror is a widely-used open-source rich-text editor framework for the web, but it lacks built-in static typing support. Wordgard aims to address this by providing a statically-typed API from the ground up.

<details><summary>References</summary>
<ul>
<li><a href="https://prosemirror.net/">ProseMirror</a></li>

</ul>
</details>

**Discussion**: The community is excited about the new editor, with many praising its design and technical depth. Some users express concerns about the lack of an upgrade path from ProseMirror and the effort required to switch.

**Tags**: `#rich-text editor`, `#ProseMirror`, `#web development`, `#open source`, `#JavaScript`

---

<a id="item-2"></a>
## [Crustc: Entire Rust Compiler Translated to C](https://github.com/FractalFir/crustc) ⭐️ 8.0/10

A project called crustc has successfully translated the entirety of the Rust compiler (rustc) into C, enabling bootstrapping on platforms without LLVM or GCC support. This breakthrough significantly improves compiler portability, allowing Rust to run on old or obscure hardware that lacks LLVM or GCC backends, and also provides a new way to verify the official Rust compiler for backdoors via diverse double-compiling. The project is the 14th known attempt to compile Rust to C, and it transpiles the entire rustc codebase rather than just a subset. The author notes that transpiling to C is easier than to LLVM IR, and letting GCC optimize may yield practical performance.

hackernews · Philpax · Jul 2, 22:57 · [Discussion](https://news.ycombinator.com/item?id=48768464)

**Background**: Rust's primary compiler, rustc, uses LLVM as its backend, which limits its support to platforms that LLVM targets. Bootstrapping Rust from source typically requires an existing Rust compiler, creating a chicken-and-egg problem for new platforms. Translating rustc to C breaks this dependency, as C compilers are available on virtually every platform.

**Discussion**: The community expressed strong admiration for the project's technical novelty and dedication, with one commenter calling it an 'original work of art.' Several users discussed using crustc for diverse double-compiling to test for backdoors in the official Rust compiler, and others noted the historical context of LLVM's C backend being removed and later revived.

**Tags**: `#rust`, `#compiler`, `#transpilation`, `#bootstrapping`, `#systems programming`

---

<a id="item-3"></a>
## [CDD recovers finetuning data from LLMs using only logits](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

Researchers introduce Contrastive Decoding Diffing (CDD), a grey-box method that recovers verbatim finetuning data from LLMs using only logit access, without needing model weights or activations. CDD achieves a verbatim recovery score of 4+/5 on 19 out of 20 organism-model pairs across four model families, outperforming the white-box Activation Difference Lens (ADL) method. This work highlights a significant privacy and security risk in LLM finetuning, as it demonstrates that sensitive training data can be extracted with minimal access. It also provides a powerful tool for auditing and understanding what models have learned during finetuning, potentially improving transparency in AI systems. CDD requires no per-model calibration, no layer selection, and no probe corpus, using a single default configuration across all experiments. An unexpected finding was that the name 'Dr. Elena Rodriguez' appeared across semantically unrelated finetuning domains, traced back to Claude Sonnet 3.6's bias in generating fictional scientists for synthetic data.

reddit · r/MachineLearning · /u/CebulkaZapiekana · Jul 3, 19:01

**Background**: Model diffing aims to detect what a finetuned model has learned compared to its base model. Prior work, Activation Difference Lens (ADL), required full weight access and only recovered vague domain-level descriptions. CDD operates on logit distributions, making it a grey-box method that is both more accessible and more effective.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.25902">Reading the Finetuning Prior: Verbatim Content Recovery via Contrastive ...</a></li>
<li><a href="https://arxiv.org/html/2605.25902v2">Reading the Finetuning Prior: Verbatim Content Recovery via Contrastive ...</a></li>
<li><a href="https://www.machinebrief.com/news/unlocking-ais-hidden-memories-with-contrastive-decoding-9a3m">Unlocking AI's Hidden Memories with Contrastive Decoding</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#privacy`, `#model diffing`, `#finetuning`, `#security`

---

<a id="item-4"></a>
## [Anthropic Accuses Alibaba of Massive Distillation Attack on Claude](https://t.me/zaihuapd/42327) ⭐️ 8.0/10

Anthropic has accused Alibaba of orchestrating a massive 'distillation attack' using approximately 25,000 fraudulent accounts to extract capabilities from its Claude AI model, with over 28.8 million interactions between April 22 and June 5, 2026. This incident highlights growing concerns over AI model security and intellectual property theft, with significant implications for US-China tech competition and the enforcement of export controls on advanced AI technologies. Anthropic claims this is the largest known distillation attack against the company, involving Alibaba and its AI lab Qwen. In response, Alibaba reportedly ordered employees to uninstall all Anthropic products, including Claude models and Claude Code, effective July 10, 2026.

telegram · zaihuapd · Jul 3, 06:21

**Background**: Model distillation is a technique where a weaker model learns from a stronger model's outputs to replicate its capabilities. While legitimate when authorized, using it on proprietary models without permission constitutes intellectual property theft. Anthropic has consistently supported export controls to maintain America's lead in AI, and distillation attacks can undermine those controls by allowing foreign entities to acquire advanced capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained">AI Model Distillation Attacks: What They Are and Why They Matter | MindStudio</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#model distillation`, `#Anthropic`, `#Alibaba`, `#intellectual property`

---

<a id="item-5"></a>
## [Huawei Launches Atlas 350 Accelerator with ShengTeng 950PR](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

At the Huawei China Partner Conference 2026, Huawei officially launched and released the Atlas 350 AI training and inference accelerator card, powered by the new ShengTeng 950PR processor, claiming 2.87 times the compute power of NVIDIA's H20 and supporting FP4 precision. This announcement signals Huawei's aggressive push into the AI accelerator market, challenging NVIDIA's dominance with a domestically produced chip that offers higher performance and lower cost, which could reshape the AI hardware landscape in China. The Atlas 350 features 112 GB of HBM memory, supports FP4 low-precision inference, and can load a 70B-parameter model on a single card, significantly reducing inference latency and investment costs.

telegram · zaihuapd · Jul 3, 08:35

**Background**: Huawei's ShengTeng 950PR chip, based on a SIMD architecture, delivers 1 PFLOPS (FP8) / 2 PFLOPS (FP4) and supports multiple data formats. It is priced at 70,000 RMB, about one-third the cost of NVIDIA's H200 in China, while achieving nearly 80% of its performance. This chip is part of Huawei's broader AI chip roadmap, which includes future models like the 950DT and 960.

<details><summary>References</summary>
<ul>
<li><a href="https://wallstreetcn.com/articles/3755816">华为昇腾AI芯片路线图公布：明年Q1推出昇腾950PR，采用自研HBM</a></li>
<li><a href="https://cloud.tencent.com/developer/article/2652707">昇腾950PR加持！华为Atlas 350上市：算力是H20的3倍-腾讯云开发者社区-腾讯云</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2026893491125467122">华为昇腾950PR正式量产！7万定价打穿英伟达，国产AI芯片终于站起来了 - 知乎</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#Huawei`, `#accelerator`, `#FP4`, `#deep learning`

---

<a id="item-6"></a>
## [Huawei Mate 80 Pro Gaming Efficiency Beats Snapdragon 8 Gen3](https://www.bilibili.com/video/BV1F7T46wEyT) ⭐️ 8.0/10

Geekerwan's review shows that the Huawei Mate 80 Pro series, powered by the Kirin 9030 chip, achieves better gaming energy efficiency than the Snapdragon 8 Gen3 due to native HarmonyOS optimizations. This demonstrates that software-hardware co-optimization can overcome theoretical hardware disadvantages, potentially reshaping competition in the mobile chip market. The Kirin 9030 Pro features a 9-core, 14-thread CPU and a 6-core Maliang 935 GPU with ~15 billion transistors. In Genshin Impact at max settings 60fps, the Mate 80 Pro Max consumes only 4.9W, outperforming Snapdragon 8 Gen3 in efficiency.

telegram · zaihuapd · Jul 3, 13:27

**Background**: Huawei's Kirin chips have faced US sanctions, limiting their access to advanced manufacturing. HarmonyOS is Huawei's proprietary operating system designed for seamless multi-device integration. This review highlights how native app optimizations can compensate for hardware limitations.

**Tags**: `#Huawei`, `#Kirin 9030`, `#HarmonyOS`, `#mobile chips`, `#gaming performance`

---

<a id="item-7"></a>
## [NASA Launches Rescue Satellite to Save Aging Swift Telescope](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 8.0/10

On July 3, NASA launched the LINK spacecraft, a private rescue satellite, to rendezvous with the aging Swift space telescope and boost its orbit by about 240 kilometers, preventing its imminent atmospheric reentry as early as October. This mission marks the first time a private spacecraft will attempt to capture and service an uncrewed U.S. government satellite, potentially opening a new era of on-orbit servicing and space debris mitigation. The LINK spacecraft will use a robotic arm to grab the Swift telescope and then slowly raise its orbit using thrusters. If successful, Swift could resume observations as early as September.

telegram · zaihuapd · Jul 3, 15:43

**Background**: The Swift space telescope, launched in 2004, has been studying gamma-ray bursts and other cosmic phenomena for over 20 years. Due to increased solar activity, its orbit has been decaying faster than expected, threatening its mission. On-orbit servicing, where one spacecraft refuels or reboosts another, is a growing field aimed at extending satellite lifetimes and reducing space debris.

**Tags**: `#space`, `#NASA`, `#satellite servicing`, `#space debris`, `#astronomy`

---

<a id="item-8"></a>
## [Tencent's Atuin AI beats Mythos in CyberGym benchmark](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 8.0/10

Tencent Xuanwu Lab's Atuin AI scored 84.0% on the CyberGym cybersecurity benchmark, surpassing Anthropic's Claude Mythos Preview, while costing less than 0.1% of Mythos's budget. It also discovered multiple high-severity vulnerabilities in projects like curl, OpenSSL, and Python cryptography that Mythos missed. This demonstrates that open-source, cost-effective AI models can outperform proprietary ones in vulnerability detection, potentially democratizing advanced cybersecurity tools. It also highlights the growing role of AI in finding critical bugs in widely-used open-source software. Atuin AI is built on the open-source GLM-5.1 model and can be deployed locally. It achieved a severity rank of #1 on the Berkeley BVI real-world vulnerability list and #5 in total vulnerabilities found.

telegram · zaihuapd · Jul 3, 16:12

**Background**: CyberGym is a cybersecurity benchmark led by UC Berkeley that evaluates AI systems on vulnerability detection tasks. Mythos is Anthropic's AI system under the 'Glass Wing Project' for cybersecurity. The comparison highlights the efficiency of open-source models versus proprietary ones.

**Tags**: `#AI`, `#cybersecurity`, `#vulnerability detection`, `#open-source`, `#benchmark`

---