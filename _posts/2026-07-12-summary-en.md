---
layout: default
title: "Horizon Summary: 2026-07-12 (EN)"
date: 2026-07-12
lang: en
---

> From 28 items, 9 important content pieces were selected

---

1. [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](#item-1) ⭐️ 9.0/10
2. [Humanoid Robot Performs World's First Live Pig Gallbladder Surgery](#item-2) ⭐️ 9.0/10
3. [Apple sues OpenAI for systematic trade secret theft](#item-3) ⭐️ 9.0/10
4. [OpenAI Launches GPT-5.6 Series with Sol, Terra, Luna](#item-4) ⭐️ 9.0/10
5. [ClickHouse Scales PgBouncer to 4x Throughput with Peering](#item-5) ⭐️ 8.0/10
6. [VultronRetriever Models Top MTEB, Run on iPhone](#item-6) ⭐️ 8.0/10
7. [Six U-Boot Vulnerabilities Allow Code Execution Before OS Boot](#item-7) ⭐️ 8.0/10
8. [Google Opposes EU Site Blocking as US Pushes Similar Laws](#item-8) ⭐️ 8.0/10
9. [Shanghai Sets 2027 BCI Clinical Application Targets](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 9.0/10

vLLM v0.25.0 makes Model Runner V2 the default for all dense models, removes legacy PagedAttention, and introduces new models like LLaVA-OneVision-2 and GLM-5, along with a Streaming Parser Engine and universal speculative decoding. This release marks a major architectural shift in vLLM, improving performance and modularity, which benefits the entire LLM serving ecosystem by enabling faster inference and easier model integration. Model Runner V2 now supports EVS, realtime embeddings, prefix caching for Mamba hybrid models, and dynamic speculative decoding with full CUDA graphs. The Transformers backend matches native vLLM speed and gains FP8 MoE support.

github · khluu · Jul 11, 20:06

**Background**: vLLM is an open-source LLM inference engine that uses PagedAttention for efficient KV cache management. Model Runner V2 is a redesigned execution core that addresses technical debt and improves modularity, making it faster and more flexible than the original V1 backend.

<details><summary>References</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/en/v0.22.1/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://en.wikipedia.org/wiki/PagedAttention">PagedAttention</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#open-source`, `#release`, `#AI infrastructure`

---

<a id="item-2"></a>
## [Humanoid Robot Performs World's First Live Pig Gallbladder Surgery](https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/) ⭐️ 9.0/10

Surgeons remotely operated a Unitree G1 humanoid robot to perform laparoscopic cholecystectomies on two live pigs, marking the first use of a general-purpose humanoid robot for live surgery. The results were published in Nature. This breakthrough demonstrates that low-cost, general-purpose humanoid robots could make minimally invasive surgery more accessible in resource-limited settings like rural areas, battlefields, or space stations. It challenges the dominance of expensive specialized surgical robots like the da Vinci system. The Unitree G1 robot costs as low as $13,500 for the base model and about $67,000 with dexterous hands, compared to $500,000 to millions for dedicated surgical robots. The robot is 1.5 meters tall, weighs 27 kg, and was operated remotely by surgeons at the University of California San Diego.

telegram · zaihuapd · Jul 11, 02:29

**Background**: Laparoscopic cholecystectomy is a minimally invasive surgery to remove the gallbladder, commonly performed for symptomatic gallstones. The da Vinci surgical system, the current standard for robotic surgery, costs hundreds of thousands to millions of dollars, limiting its availability. General-purpose humanoid robots like the Unitree G1 are designed for diverse tasks and are much cheaper, but had never been used for live surgery before this study.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unitree_Robotics">Unitree Robotics - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Laparoscopic_cholecystectomy">Laparoscopic cholecystectomy</a></li>
<li><a href="https://www.unitree.com/g1/">Humanoid robot G1_Humanoid Robot Functions_Humanoid Robot Price | Unitree Robotics</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#surgery`, `#humanoid robot`, `#medical technology`, `#AI`

---

<a id="item-3"></a>
## [Apple sues OpenAI for systematic trade secret theft](https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html) ⭐️ 9.0/10

On July 10, 2026, Apple filed a lawsuit in the U.S. District Court for the Northern District of California against OpenAI, two former employees, and io Products, alleging that OpenAI systematically stole trade secrets related to product design, manufacturing processes, and supply chain to accelerate its consumer hardware development. This lawsuit between two tech giants could set a precedent for how companies protect trade secrets in the AI hardware race, potentially impacting OpenAI's hardware ambitions and the broader industry's hiring practices. Apple alleges that former employee Chang Liu accessed internal networks after leaving and downloaded dozens of hardware files, while OpenAI hardware head Tang Yew Tan sent supplier information to his personal email before resigning and asked job candidates to bring Apple components to interviews. Apple also claims over 400 former employees now work at OpenAI.

telegram · zaihuapd · Jul 11, 03:14

**Background**: OpenAI acquired io Products in May 2025 to lead its hardware development. io was founded in 2024 by Jony Ive, Scott Cannon, Evans Hankey, and Tang Tan to create AI hardware. The lawsuit claims OpenAI's hardware business is 'rotten to its core' due to reliance on stolen trade secrets.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/cy8w379e091o">Apple sues OpenAI , its employees claiming theft of trade secrets</a></li>
<li><a href="https://www.theguardian.com/technology/2026/jul/10/apple-sues-openai-trade-secrets">Apple sues OpenAI , alleging artificial intelligence company stole trade ...</a></li>
<li><a href="https://apnews.com/article/apple-openai-lawsuit-trade-secrets-theft-6fff8833f5889d86406b89a02dd8fb16">Apple files lawsuit accusing OpenAI of stealing trade secrets</a></li>

</ul>
</details>

**Tags**: `#lawsuit`, `#trade secrets`, `#Apple`, `#OpenAI`, `#AI hardware`

---

<a id="item-4"></a>
## [OpenAI Launches GPT-5.6 Series with Sol, Terra, Luna](https://t.me/zaihuapd/42497) ⭐️ 9.0/10

OpenAI has officially released the GPT-5.6 series, featuring three tiers: Sol (flagship), Terra (balanced), and Luna (cost-efficient). The series introduces max/ultra reasoning, multi-agent collaboration, and programmatic tool calling, with significant improvements in code, knowledge work, design, research, and cybersecurity. This release marks a major step in AI model efficiency and capability, offering tiered pricing to suit different use cases while introducing advanced features like multi-agent collaboration and programmatic tool calling that reduce token usage and cost for complex tasks. It sets a new benchmark for performance-to-cost ratio in the industry. Pricing per 1M tokens: Sol $5 input / $30 output, Terra $2.50 input / $15 output, Luna $1 input / $6 output. The bare gpt-5.6 API alias defaults to Sol. Programmatic tool calling allows models to orchestrate tools via code instead of individual API round-trips, improving efficiency.

telegram · zaihuapd · Jul 11, 13:34

**Background**: GPT-5.6 is OpenAI's latest generation of large language models, succeeding GPT-4. Multi-agent collaboration enables multiple AI agents to coordinate on complex tasks, while programmatic tool calling (previously seen in Anthropic's Claude) allows models to write code that calls external tools, reducing latency and cost. These features aim to make AI more practical for enterprise and research applications.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>
<li><a href="https://www.vellum.ai/blog/gpt-5-6-benchmarks-explained">GPT-5.6 Sol vs Terra vs Luna: Which Tier Should You Actually Use?</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-gpt-5-6-soul-terra-luna-explained">What Is GPT-5.6? OpenAI's Soul, Terra, and Luna Model Tiers Explained | MindStudio</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-5.6`, `#AI`, `#language models`, `#multi-agent`

---

<a id="item-5"></a>
## [ClickHouse Scales PgBouncer to 4x Throughput with Peering](https://clickhouse.com/blog/pgbouncer-clickhouse-managed-postgres) ⭐️ 8.0/10

ClickHouse implemented a peering mechanism in PgBouncer that forwards query cancellation requests to the correct process, enabling multi-process setups with so_reuseport to achieve up to 4x throughput improvement. This advancement allows PostgreSQL connection pooling to scale horizontally across multiple processes and machines without breaking query cancellation, which is critical for high-availability cloud deployments and large-scale managed database services. The peering feature, available since PgBouncer 1.19.0, uses a peer_id (max 16383) to coordinate cancel requests among processes. ClickHouse's implementation leverages this to run multiple PgBouncer instances behind a single port using so_reuseport.

hackernews · saisrirampur · Jul 11, 15:28 · [Discussion](https://news.ycombinator.com/item?id=48872874)

**Background**: PgBouncer is a lightweight connection pooler for PostgreSQL. When using so_reuseport to allow multiple processes to share the same listening port, a cancellation request may land on a process that does not own the session, causing the cancel to be ignored. Peering solves this by forwarding the request to the correct process.

<details><summary>References</summary>
<ul>
<li><a href="https://manpages.debian.org/testing/pgbouncer/pgbouncer.5.en.html">pgbouncer (5) — pgbouncer — Debian testing — Debian Manpages</a></li>
<li><a href="https://dataegret.com/2024/08/handling_cancellation_request/">Handling Cancellation Request - Data Egret</a></li>
<li><a href="https://boosterkrd.github.io/2024/08/20/Handling-Cancellation-Request.html">Handling Cancellation Request | Booster’s Blog</a></li>

</ul>
</details>

**Discussion**: Commenters suggested alternative solutions like Odyssey and pgdog, and asked about Kubernetes compatibility. Some noted that peering may not be needed in Kubernetes if each pod has its own pool, but others saw value for multi-instance setups.

**Tags**: `#PostgreSQL`, `#PgBouncer`, `#scaling`, `#connection pooling`, `#ClickHouse`

---

<a id="item-6"></a>
## [VultronRetriever Models Top MTEB, Run on iPhone](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

The VultronRetriever family of models, including Prime-8B, Core-4.5B, and Flash-0.8B, has been released on HuggingFace and achieved #1 rankings on the MTEB leaderboard in their respective classes, with the Prime model being the global #1. These models demonstrate up to 16x smaller index storage and 12x higher throughput compared to previous leaders, and can run fully offline on an iPhone, marking a significant advancement in edge AI and efficient retrieval. The VultronRetrieverFlash-0.8B outperforms models up to 5x its size and indexes up to 60 images per minute offline. The models use the Hydra Architecture for late interaction retrieval, offering high precision with up to half the memory of comparable models.

reddit · r/MachineLearning · /u/madkimchi · Jul 11, 15:22

**Background**: The MTEB (Massive Text Embedding Benchmark) is a standard public leaderboard for evaluating embedding models on tasks like retrieval, classification, and clustering. Late interaction retrieval, as used in ColBERT, processes queries and documents separately until the final matching step, enabling efficient and precise search. The Hydra Architecture is a modular design that combines sparse attention, mixture-of-experts, and dual memories for efficient long-context reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB Leaderboard - a Hugging Face Space by mteb</a></li>
<li><a href="https://weaviate.io/blog/late-interaction-overview">An Overview of Late Interaction Retrieval Models... | Weaviate</a></li>
<li><a href="https://arxiv.org/abs/2508.15099">[2508.15099] Hydra: A Modular Architecture for Efficient Long-Context Reasoning</a></li>

</ul>
</details>

**Tags**: `#retrieval`, `#MTEB`, `#edge AI`, `#embedding`, `#HuggingFace`

---

<a id="item-7"></a>
## [Six U-Boot Vulnerabilities Allow Code Execution Before OS Boot](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

Binarly disclosed six vulnerabilities in U-Boot's FIT signature verification, with two enabling arbitrary code execution and four causing denial of service, affecting versions since 2013.07. 这些漏洞允许攻击者在操作系统和安全软件启动前执行恶意代码，可能禁用固件安全功能或植入持久性恶意软件，影响超过 50 个稳定版本及大量下游厂商。 The vulnerabilities (BRLY-2026-037 to BRLY-2026-042) are in the FIT image parsing code; patches have been accepted upstream but require vendor firmware updates to reach devices, leaving unsupported hardware permanently vulnerable.

telegram · zaihuapd · Jul 11, 08:32

**Background**: U-Boot is a widely used open-source bootloader for embedded devices, responsible for initializing hardware and loading the operating system. FIT (Flattened Image Tree) is a standard format for packaging boot images, and its signature verification ensures only trusted firmware is executed. These vulnerabilities bypass that verification, enabling attacks at the earliest stage of device boot.

<details><summary>References</summary>
<ul>
<li><a href="https://www.binarly.io/blog/unfit-to-boot-breaking-u-boots-fit-signature-verification">Unfit to Boot: Breaking U-Boot's FIT Signature Verification</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/">New U-Boot flaws could enable stealthy firmware attacks</a></li>
<li><a href="https://thehackernews.com/2026/07/six-new-u-boot-flaws-could-let.html">Six New U-Boot Flaws Could Let Malicious Images Crash Devices ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#bootloader`, `#vulnerability`, `#firmware`, `#U-Boot`

---

<a id="item-8"></a>
## [Google Opposes EU Site Blocking as US Pushes Similar Laws](https://torrentfreak.com/google-opposes-site-blocking-in-europe-as-u-s-piracy-blocking-plans-gain-momentum/) ⭐️ 8.0/10

Google has submitted a filing to the European Commission opposing the expansion of site-blocking measures, arguing that blocking DNS resolvers, IP addresses, and VPNs is ineffective and disproportionate. Meanwhile, similar anti-piracy legislation is gaining momentum in the US Congress, with Representative Issa planning to advance a site-blocking bill. This highlights a growing global tension between copyright enforcement and internet freedom, with major tech companies like Google pushing back against broad blocking measures. The outcome could set precedents for how governments balance intellectual property protection with open internet principles. Google's filing cites specific overblocking incidents, such as Italy's anti-piracy system mistakenly blocking Google Drive subdomains and Cloudflare IP addresses hosting 42 million domains. Google has not yet publicly commented on the US legislation, but its EU filing suggests it prefers providing better legal alternatives over expanding blocking.

telegram · zaihuapd · Jul 11, 15:10

**Background**: Site blocking is a common anti-piracy technique where ISPs or DNS resolvers are ordered to prevent access to infringing websites. Critics argue that such measures often lead to overblocking, affecting legitimate services, and can be circumvented by users via VPNs or alternative DNS. The EU and US are both considering updated legal frameworks to combat online piracy, with differing approaches.

**Tags**: `#internet governance`, `#copyright`, `#site blocking`, `#tech policy`, `#Google`

---

<a id="item-9"></a>
## [Shanghai Sets 2027 BCI Clinical Application Targets](https://t.me/zaihuapd/42501) ⭐️ 8.0/10

The Shanghai Municipal Science and Technology Commission issued the 'Shanghai Brain-Computer Interface Future Industry Cultivation Action Plan (2025-2030)', aiming to achieve high-quality brain control by 2027, with semi-invasive BCI products leading clinical application in China and breakthroughs in invasive BCI. The plan targets at least 5 invasive and semi-invasive BCI products to complete medical device type testing and clinical trials, restoring partial language and motor functions for patients with aphasia and paralysis. This is a significant policy milestone that provides a clear roadmap and government backing for the clinical translation of brain-computer interfaces in China, potentially accelerating the development of BCI-based medical devices and positioning Shanghai as a global hub for neurotechnology. The specific targets and product goals indicate a strong push to move BCI from research labs to real-world medical applications, benefiting patients with severe neurological disorders. The plan distinguishes between semi-invasive and invasive BCI: semi-invasive devices (e.g., ECoG) are placed under the skull but outside the brain tissue, offering a balance between signal quality and safety, while invasive devices (e.g., microelectrode arrays) penetrate the brain for high-resolution signals but require surgery. The 2027 target includes completing medical device type testing (型式检验) and clinical trials, which are mandatory regulatory steps for market approval in China.

telegram · zaihuapd · Jul 11, 15:49

**Background**: Brain-computer interfaces (BCIs) enable direct communication between the brain and external devices by decoding neural signals. They are categorized into non-invasive (e.g., EEG headset), semi-invasive (e.g., ECoG), and invasive (e.g., Utah array) types, with increasing signal fidelity but also higher surgical risk. China has been actively investing in BCI technology, and this action plan aligns with national strategies to lead in emerging neurotechnology fields.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/76363987">【深度解析】一文看懂脑机接口技术的现状与未来！ - 知乎</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/699343201">侵入式、半侵入式、非侵入式脑机接口，具体应该怎么选</a></li>
<li><a href="https://www.nifdc.org.cn/nifdc///xxgk/zcfg/zcjd/202607011610522105082.html">《脑机接口医疗器械产品分类界定指导原则》解读</a></li>

</ul>
</details>

**Tags**: `#brain-computer interface`, `#policy`, `#clinical application`, `#China`, `#neurotechnology`

---