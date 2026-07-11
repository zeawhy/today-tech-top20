---
layout: default
title: "Horizon Summary: 2026-07-11 (EN)"
date: 2026-07-11
lang: en
---

> From 27 items, 9 important content pieces were selected

---

1. [Humanoid Robot Performs World's First Laparoscopic Surgery on Live Pigs](#item-1) ⭐️ 9.0/10
2. [SGLang v0.5.15 Boosts GLM-5.2 to 500+ tok/s on Blackwell](#item-2) ⭐️ 8.0/10
3. [Relativity rules chemical bonds in heavy elements](#item-3) ⭐️ 8.0/10
4. [Apple sues OpenAI over trade secret theft](#item-4) ⭐️ 8.0/10
5. [VultronRetriever Models Top MTEB, Enable Offline iPhone Q&A](#item-5) ⭐️ 8.0/10
6. [SpaceXAI and Cursor Launch Grok 4.5 for Coding, Legal, Finance](#item-6) ⭐️ 8.0/10
7. [U-Boot Bootloader Flaws Allow Code Execution Before OS Boot](#item-7) ⭐️ 8.0/10
8. [OpenAI Launches GPT-5.6 Series with Sol, Terra, Luna Tiers](#item-8) ⭐️ 8.0/10
9. [Shanghai Aims for High-Quality Brain Control by 2027](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Humanoid Robot Performs World's First Laparoscopic Surgery on Live Pigs](https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/) ⭐️ 9.0/10

Surgeons remotely operated a Unitree G1 humanoid robot to perform the world's first laparoscopic cholecystectomy on live pigs, with results published in Nature. This breakthrough demonstrates that low-cost, general-purpose humanoid robots could make minimally invasive surgery accessible in rural, battlefield, or space settings, challenging the dominance of expensive specialized systems like the da Vinci. The Unitree G1 base model costs $13,500, or about $67,000 with dexterous hands, compared to $500,000 to millions for da Vinci systems. The robot stands 1.5 meters tall and weighs 27 kg.

telegram · zaihuapd · Jul 11, 02:29

**Background**: Laparoscopic cholecystectomy is a minimally invasive surgery to remove the gallbladder, commonly performed for gallstones. The da Vinci Surgical System is the current standard for robotic-assisted surgery but costs hundreds of thousands to millions of dollars. Unitree G1 is a general-purpose humanoid robot designed for various tasks, not specifically for surgery.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unitree_Robotics">Unitree Robotics - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Laparoscopic_cholecystectomy">Laparoscopic cholecystectomy</a></li>
<li><a href="https://en.wikipedia.org/wiki/Da_Vinci_Surgical_System">da Vinci Surgical System - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#surgery`, `#humanoid robot`, `#medical technology`, `#AI`

---

<a id="item-2"></a>
## [SGLang v0.5.15 Boosts GLM-5.2 to 500+ tok/s on Blackwell](https://github.com/sgl-project/sglang/releases/tag/v0.5.15) ⭐️ 8.0/10

SGLang v0.5.15 introduces major performance optimizations for GLM-5.2 on Blackwell GPUs, achieving over 500 tokens per second per user on 8x B300 and 450 tok/s on 4x GB300. Key improvements include Spec V2 speculative decoding by default, IndexShare MTP reducing draft-step cost by up to 1.9x, and TopK V2 fusion. These optimizations make SGLang one of the fastest open-source LLM serving frameworks for production-grade models like GLM-5.2, directly benefiting users who need low-latency inference on NVIDIA Blackwell hardware. The release also sets a new performance benchmark for speculative decoding and MoE serving. Spec V2 achieves zero-overhead scheduling via CUDA-graphable DSA draft-extend and fused metadata ops, yielding an 11% end-to-end TPS boost. IndexShare MTP reuses the indexer top-k across draft steps, reducing draft-step cost by up to 1.9x at long context. The release also adds native web search via Exa, breakable CUDA Graph by default, and support for new models like Hunyuan 3 and Qwen3.6 NVFP4.

github · Fridge003 · Jul 10, 22:58

**Background**: SGLang is an open-source LLM serving framework designed for high-performance inference. Speculative decoding is a technique that uses a smaller draft model to predict multiple tokens, which are then verified by the main model, reducing latency. GLM-5.2 is a 753B-parameter Mixture-of-Experts model from ZAI, optimized for long-horizon tasks. NVFP4 is a 4-bit quantization format for NVIDIA Blackwell GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.sglang.io/docs/advanced_features/speculative_decoding">Speculative Decoding - SGLang Documentation</a></li>
<li><a href="https://www.lmsys.org/blog/2026-06-15-next-generation-speculative-decoding-dflash-v2/">The next generation of speculative decoding: DFlash and Spec V2</a></li>
<li><a href="https://huggingface.co/blog/zai-org/glm-52-blog">GLM-5.2: Built for Long-Horizon Tasks</a></li>

</ul>
</details>

**Tags**: `#LLM serving`, `#performance optimization`, `#GPU inference`, `#SGLang`, `#speculative decoding`

---

<a id="item-3"></a>
## [Relativity rules chemical bonds in heavy elements](https://www.brown.edu/news/2026-07-09/chemical-bonds-relativity) ⭐️ 8.0/10

New research published in Science confirms that Einstein's theory of relativity governs chemical bonding in heavy elements, providing direct experimental evidence for relativistic effects such as spin-orbit coupling. This work deepens our understanding of why heavy elements like mercury are liquid at room temperature and why gold appears yellow, with implications for materials science and quantum chemistry. The study demonstrates that in heavy elements, electrons orbit at a significant fraction of the speed of light, causing spin and orbit to couple—a relativistic effect that alters chemical bonding.

hackernews · hhs · Jul 10, 22:30 · [Discussion](https://news.ycombinator.com/item?id=48866134)

**Background**: Relativistic quantum chemistry considers corrections to the Schrödinger equation for heavy elements where electron speeds approach the speed of light. These effects explain properties like mercury's low melting point and gold's color, which cannot be predicted by non-relativistic theories.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Relativistic_quantum_chemistry">Relativistic quantum chemistry - Wikipedia</a></li>
<li><a href="https://sciencenotes.org/why-is-mercury-a-liquid-at-room-temperature/">Why Is Mercury a Liquid at Room Temperature?</a></li>

</ul>
</details>

**Discussion**: Commenters noted that relativistic effects in chemistry were already known (e.g., gold's color), but appreciated the new experimental confirmation. One user humorously cautioned against using their explanation for spacecraft design.

**Tags**: `#physics`, `#chemistry`, `#relativity`, `#chemical bonding`, `#heavy elements`

---

<a id="item-4"></a>
## [Apple sues OpenAI over trade secret theft](https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/) ⭐️ 8.0/10

Apple has filed a lawsuit against OpenAI, alleging that the AI company systematically stole trade secrets by hiring former Apple employees who emailed confidential information to themselves and used it to approach Apple suppliers. This lawsuit could have major implications for the AI industry, potentially setting legal precedents around trade secret protection and employee mobility, and may damage OpenAI's reputation and hardware partnerships. Apple claims OpenAI instructed new hires to avoid disclosing their new jobs to Apple, and that a pattern of emailing confidential information was discovered, including from a key employee named Tan. OpenAI allegedly used Apple's confidential hardware information when approaching Apple's suppliers.

hackernews · stock_toaster · Jul 10, 20:47 · [Discussion](https://news.ycombinator.com/item?id=48865019)

**Background**: Trade secret lawsuits are common in tech, but this case is notable due to the high profile of both companies and the alleged systematic nature of the theft. Apple has a history of aggressively protecting its intellectual property, while OpenAI has faced criticism for its data practices and hiring tactics.

**Discussion**: Community comments are largely critical of OpenAI, with many calling the alleged behavior 'damning' and suggesting this could be the end of OpenAI's hardware ambitions. Some commenters warn businesses against using OpenAI models due to IP risks, while others note that Apple's deep pockets make a settlement unlikely and discovery could be devastating for OpenAI.

**Tags**: `#Apple`, `#OpenAI`, `#trade secrets`, `#lawsuit`, `#AI ethics`

---

<a id="item-5"></a>
## [VultronRetriever Models Top MTEB, Enable Offline iPhone Q&A](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

Vultr released the VultronRetriever family of models on HuggingFace, achieving #1 on the MTEB leaderboard in each size class, with the 8B model as global #1. The models offer up to 16x smaller index storage and 12x higher throughput compared to previous 9B-class leaders, and can run fully offline on an iPhone for Q&A and document embedding. This breakthrough enables high-quality retrieval and embedding on edge devices like smartphones, reducing reliance on cloud infrastructure. It sets a new efficiency standard for retrieval models, potentially accelerating adoption of offline AI applications in mobile and IoT environments. The family includes three models: VultronRetrieverPrime-8B (global #1), Core-4.5B (outperforms models twice its size), and Flash-0.8B (outperforms models up to 5x its size, indexes up to 60 images per minute offline). They use the Hydra Architecture for late interaction retrieval with up to half the memory of comparable models, and were trained on datasets with 0% cross-dataset duplication and 0% eval contamination.

reddit · r/MachineLearning · /u/madkimchi · Jul 11, 15:22

**Background**: MTEB (Massive Text Embedding Benchmark) is a widely-used leaderboard for evaluating text embedding and retrieval models across diverse tasks. Late interaction retrieval, popularized by models like ColBERT, separates query and document encoding until the final matching step, enabling efficient and precise retrieval. The Hydra Architecture is a novel approach that combines late interaction with generation, reducing memory footprint.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB Leaderboard - a Hugging Face Space by mteb</a></li>
<li><a href="https://weaviate.io/blog/late-interaction-overview">An Overview of Late Interaction Retrieval Models... | Weaviate</a></li>

</ul>
</details>

**Discussion**: The Reddit community expressed excitement about the models' efficiency and edge deployment capabilities, with many asking technical questions about the Hydra Architecture and comparisons to existing models like ColBERT. Some users raised concerns about the lack of open-source training code and reproducibility, while others praised the significant improvements in index size and throughput.

**Tags**: `#retrieval`, `#MTEB`, `#edge AI`, `#NLP`, `#HuggingFace`

---

<a id="item-6"></a>
## [SpaceXAI and Cursor Launch Grok 4.5 for Coding, Legal, Finance](https://t.me/zaihuapd/42484) ⭐️ 8.0/10

SpaceXAI and Cursor have jointly released Grok 4.5, a new AI model that ranks first on the Harvey legal agent benchmark and is optimized for coding, legal, and financial services tasks. This marks the first joint model after SpaceX's $60 billion acquisition of Cursor, combining SpaceXAI's scale with Cursor's coding expertise, potentially setting a new standard for domain-specific AI in professional services. Grok 4.5 runs at 80 tokens per second, claims twice the token efficiency of leading competitors, and is priced at $2 per million input tokens and $6 per million output tokens, with cached input at $0.50.

telegram · zaihuapd · Jul 11, 01:44

**Background**: Harvey is an open-source legal agent benchmark with over 1,200 tasks across 24 practice areas, scored against expert-written rubrics. Cursor is an AI coding agent and development environment founded in 2022, recently acquired by SpaceX. Token efficiency refers to generating more useful output per token, reducing cost per task.

<details><summary>References</summary>
<ul>
<li><a href="https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark">Introducing Harvey ’s Legal Agent Benchmark</a></li>
<li><a href="https://byteiota.com/grok-45-ga-token-efficiency-api-guide/">Grok 4.5 Is GA: Token Efficiency Beats the Benchmark Gap</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(company)">Cursor (company) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Grok 4.5`, `#SpaceXAI`, `#Cursor`, `#legal AI`

---

<a id="item-7"></a>
## [U-Boot Bootloader Flaws Allow Code Execution Before OS Boot](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

Binarly disclosed six vulnerabilities in U-Boot's FIT signature verification, two enabling arbitrary code execution and four causing device crashes, affecting versions since 2013.07. These flaws allow attackers to bypass boot-time security checks and execute malicious code before the OS loads, potentially compromising firmware security features and enabling persistent malware on a wide range of devices. The vulnerabilities reside in the FIT image signature verification code, where untrusted boot images are processed before validation completes. Patches have been accepted by U-Boot maintainers, but deployment depends on hardware vendors integrating them into firmware updates.

telegram · zaihuapd · Jul 11, 08:32

**Background**: U-Boot is a widely used open-source bootloader for embedded devices, supporting FIT (Flattened Image Tree) images with signature verification for secure boot. The Verified Boot mechanism ensures only authenticated firmware runs, but these flaws allow bypassing that check. BMCs (Baseboard Management Controllers) that support remote firmware updates are particularly at risk as attackers can exploit the vulnerabilities without physical access.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.u-boot-project.org/en/latest/usage/fit/signature.html">U-Boot FIT Signature Verification</a></li>
<li><a href="https://cybersecuritynews.com/u-boot-fit-signature-verification/">Six U-Boot FIT Signature Verification Flaws Enable Code ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#bootloader`, `#U-Boot`, `#firmware`, `#vulnerability`

---

<a id="item-8"></a>
## [OpenAI Launches GPT-5.6 Series with Sol, Terra, Luna Tiers](https://t.me/zaihuapd/42497) ⭐️ 8.0/10

OpenAI has officially released the GPT-5.6 series, featuring three tiers: Sol (flagship), Terra (balanced), and Luna (cost-efficient), along with new capabilities like max/ultra reasoning, multi-agent collaboration, and programmatic tool calling. This release significantly improves performance-to-cost ratio, making advanced AI more accessible for complex tasks in coding, research, and cybersecurity, while the multi-agent and tool-calling features enable more autonomous and efficient workflows. Sol outperforms the previous Fable 5 benchmark by 13.1 points, while Luna costs one-fifth of Sol's price. The series introduces programmatic tool calling, which allows models to orchestrate tools via code instead of individual API round-trips.

telegram · zaihuapd · Jul 11, 13:34

**Background**: Large language models (LLMs) like GPT are typically accessed via API calls, with each tool invocation requiring a separate round-trip, which is inefficient for multi-step tasks. Programmatic tool calling enables the model to write and execute code that calls multiple tools in a single session, reducing latency and cost. Multi-agent collaboration allows multiple AI agents to coordinate on complex tasks, moving beyond single-model limitations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vellum.ai/blog/gpt-5-6-benchmarks-explained">GPT-5.6 Sol vs Terra vs Luna: Which Tier Should You Actually Use?</a></li>
<li><a href="https://www.marktechpost.com/2026/07/09/openai-releases-gpt-5-6-a-three-tier-model-family-with-programmatic-tool-calling/">OpenAI Releases GPT-5.6 (Sol, Terra, Luna): A Three-Tier Model Family With Programmatic Tool Calling in the Responses API - MarkTechPost</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-gpt-5-6-soul-terra-luna-explained">What Is GPT-5.6? OpenAI's Soul, Terra, and Luna Model Tiers Explained | MindStudio</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-5.6`, `#AI`, `#large language model`, `#machine learning`

---

<a id="item-9"></a>
## [Shanghai Aims for High-Quality Brain Control by 2027](https://t.me/zaihuapd/42501) ⭐️ 8.0/10

The Shanghai Municipal Science and Technology Commission issued the "Shanghai Brain-Computer Interface Future Industry Cultivation Action Plan (2025-2030)", targeting high-quality brain control by 2027, with semi-invasive BCI products first to achieve clinical application and breakthroughs in invasive BCI research. This policy signals strong government support and investment in BCI technology, potentially accelerating clinical adoption and positioning Shanghai as a global leader in neurotechnology. It could bring life-changing communication and motor restoration to patients with paralysis or aphasia. The plan aims to have at least five invasive or semi-invasive BCI products complete medical device type testing and clinical trials, restoring partial language and motor functions for patients with aphasia and paralysis. The action plan covers 2025-2030.

telegram · zaihuapd · Jul 11, 15:49

**Background**: Brain-computer interfaces (BCIs) enable direct communication between the brain and external devices. They are categorized into non-invasive (scalp electrodes), semi-invasive (electrodes placed under the skull but outside the brain), and invasive (electrodes implanted in brain tissue). Semi-invasive BCIs offer a balance between signal quality and surgical risk, making them promising for early clinical adoption.

<details><summary>References</summary>
<ul>
<li><a href="https://paper.people.com.cn/rmrb/pc/content/202607/04/content_30166549.html">无创接入，脑机接口迎来更多可能（院士讲科普·未来产业）</a></li>
<li><a href="https://www.nhsa.gov.cn/art/2025/3/13/art_52_15967.html">nhsa.gov.cn/art/2025/3/13/art_52_15967.html</a></li>
<li><a href="https://www.jfdaily.com/wx/detail.do?id=874565">三家“ 脑 机 接 口 ”头部企业为何出现在上海？｜跟着项目经理看未来产业</a></li>

</ul>
</details>

**Tags**: `#brain-computer interface`, `#policy`, `#China`, `#clinical application`, `#neurotechnology`

---