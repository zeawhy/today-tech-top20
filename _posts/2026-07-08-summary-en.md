---
layout: default
title: "Horizon Summary: 2026-07-08 (EN)"
date: 2026-07-08
lang: en
---

> From 42 items, 15 important content pieces were selected

---

1. [MIRA: 5B-Parameter World Model for Multiplayer Rocket League](#item-1) ⭐️ 9.0/10
2. [Anthropic Releases Claude Sonnet 5 with Stronger Agentic Abilities](#item-2) ⭐️ 9.0/10
3. [Januscape: 16-Year-Old KVM VM Escape Flaw Affects Intel & AMD](#item-3) ⭐️ 9.0/10
4. [China Considers Restricting Exports of Top AI Models](#item-4) ⭐️ 9.0/10
5. [Kokoro: CPU-Friendly, High-Quality Open-Source TTS](#item-5) ⭐️ 8.0/10
6. [EU Chat Control Proposals Threaten Encryption](#item-6) ⭐️ 8.0/10
7. [Microsoft lays off id Tech engine team at id Software](#item-7) ⭐️ 8.0/10
8. [sqlite-utils 4.0 Introduces Schema Migrations](#item-8) ⭐️ 8.0/10
9. [Ph.D. Thesis on Differentiable Ray Tracing for Radio Propagation](#item-9) ⭐️ 8.0/10
10. [Mozilla CTO Raffi Krikorian AMA on Open Source AI Report](#item-10) ⭐️ 8.0/10
11. [Constraining Fine-Tuning to Trusted LoRA Subspace](#item-11) ⭐️ 8.0/10
12. [China Plans $295B National Computing Network Over 5 Years](#item-12) ⭐️ 8.0/10
13. [new-api Fixes Billing Bug: Oversized Params Cause Negative Charges](#item-13) ⭐️ 8.0/10
14. [Nvidia Blackwell Wafers Made in US, Still Packaged in Taiwan](#item-14) ⭐️ 8.0/10
15. [DeepSeek Develops Own AI Chip to Reduce Reliance on NVIDIA and Huawei](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [MIRA: 5B-Parameter World Model for Multiplayer Rocket League](https://www.reddit.com/r/MachineLearning/comments/1upofuw/mira_multiplayer_interactive_world_models_trained/) ⭐️ 9.0/10

MIRA is a 5-billion-parameter world model trained on 10,000 hours of synthetic Rocket League data, enabling interactive 4-player simulation at 20 frames per second on a single NVIDIA B200 GPU. The team released a playable online demo, a technical report, and a 1,000-hour dataset of 4-player gameplay. This is a groundbreaking step toward large-scale interactive world models for multiplayer games, potentially transforming game AI, simulation, and reinforcement learning. The open-source release of code, dataset, and model lowers the barrier for researchers and developers to build on this work. The model runs at 20 fps for 4 players on a single B200 GPU, which is built on NVIDIA's Blackwell architecture with 208 billion transistors. The training data is entirely synthetic, generated using the Rocket League game engine, and the released dataset contains 1,000 hours of 4-player gameplay.

reddit · r/MachineLearning · /u/MasterScrat · Jul 7, 07:59

**Background**: A world model in AI is a machine learning system that builds an internal representation of an environment and predicts how it changes in response to actions. Synthetic data, artificially generated rather than collected from real events, is often used to train AI models when real data is scarce or expensive. The B200 GPU is a high-end NVIDIA accelerator designed for AI workloads, offering significant performance improvements over previous generations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/dgx-b200/">DGX B200: The Foundation for Your AI Factory | NVIDIA</a></li>
<li><a href="https://medium.com/cdrin-cctt/the-power-of-synthetic-data-using-game-engines-to-improve-ai-67e872bab997">The Power of Synthetic Data: Using Game Engines to Improve AI | by CDRIN | CDRIN-CCTT | Medium</a></li>

</ul>
</details>

**Tags**: `#world models`, `#reinforcement learning`, `#multiplayer games`, `#large-scale models`, `#open source`

---

<a id="item-2"></a>
## [Anthropic Releases Claude Sonnet 5 with Stronger Agentic Abilities](https://t.me/zaihuapd/42404) ⭐️ 9.0/10

Anthropic has released Claude Sonnet 5, which it claims is the most agent-capable Sonnet model to date, able to plan and use tools like browsers and terminals autonomously. The model is available immediately across all plans and becomes the default for Free and Pro users. Claude Sonnet 5 offers near-Opus performance at a lower price point, making advanced agentic AI more accessible to developers and enterprises. Its enhanced reasoning, tool use, and coding abilities could accelerate the adoption of AI agents in real-world workflows. Claude Sonnet 5 outperforms Sonnet 4.6 in reasoning, tool use, coding, and knowledge tasks, and its performance is close to Opus 4.8. Pricing is set at $2 per million input tokens and a limited-time output token price until August 31, 2026.

telegram · zaihuapd · Jul 7, 09:02

**Background**: Anthropic's Claude model family includes Opus (most capable), Sonnet (balanced), and Haiku (fast/cheap). Sonnet models are designed for a wide range of tasks including agentic workflows, where the model autonomously plans and executes multi-step actions using external tools. The new Sonnet 5 aims to bring stronger agentic capabilities at a lower cost than the top-tier Opus models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-sonnet-5">Introducing Claude Sonnet 5 \ Anthropic</a></li>
<li><a href="https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/">Anthropic launches Claude Sonnet 5 as a cheaper way to run ...</a></li>
<li><a href="https://www.anthropic.com/claude/opus">Claude Opus \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#Claude`, `#LLM`, `#Agent`

---

<a id="item-3"></a>
## [Januscape: 16-Year-Old KVM VM Escape Flaw Affects Intel & AMD](https://github.com/V4bel/Januscape) ⭐️ 9.0/10

Security researcher Hyunwoo Kim disclosed Januscape (CVE-2026-53359), the first KVM/x86 VM escape vulnerability that works on both Intel and AMD platforms, with a proof-of-concept causing host kernel panic. This flaw breaks multi-tenant isolation in cloud environments, allowing a malicious guest VM to compromise the host, affecting Linux kernels from 2010 to 2026 and potentially enabling full host takeover. The vulnerability is a use-after-free in the KVM shadow MMU, where a guest can corrupt the host's shadow page tables. A separate unreleased exploit reportedly achieves full host code execution.

telegram · zaihuapd · Jul 7, 10:14

**Background**: KVM (Kernel-based Virtual Machine) is a Linux hypervisor that uses shadow MMU on older hardware to manage guest memory. A use-after-free occurs when a program accesses memory after it has been freed, potentially allowing an attacker to execute arbitrary code. This bug remained undetected for 16 years.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html">16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on ...</a></li>
<li><a href="https://www.csoonline.com/article/4194085/16-year-old-kvm-flaw-allows-attackers-to-escape-vms-and-take-over-linux-servers.html">16-year-old KVM flaw allows attackers to escape VMs and take ...</a></li>
<li><a href="https://threat-modeling.com/cve-2026-53359-januscape-linux-kvm-vm-escape-intel-amd/">CVE-2026-53359 'Januscape': 16-Year-Old Linux KVM Guest-to ...</a></li>

</ul>
</details>

**Discussion**: The Telegram discussion highlights the severity and long latency of the bug, with some expressing concern about cloud provider response times and the need for immediate patching.

**Tags**: `#KVM`, `#VM escape`, `#CVE`, `#Linux kernel`, `#security`

---

<a id="item-4"></a>
## [China Considers Restricting Exports of Top AI Models](https://www.reuters.com/world/beijing-is-looking-curbing-overseas-access-chinas-top-ai-models-sources-say-2026-07-07/) ⭐️ 9.0/10

China's Ministry of Commerce has held meetings with Alibaba, ByteDance, and Zhipu AI to discuss restricting overseas access to the country's most advanced AI models, including future releases, and potentially classifying AI technology leaks as national security crimes. This policy could significantly reshape the global AI landscape by limiting international access to cutting-edge Chinese AI models, affecting major tech companies and potentially accelerating the fragmentation of the global AI ecosystem. The restrictions are still under discussion and may only apply to future model releases; the final implementation remains uncertain. The talks also consider restricting foreign capital investment in Chinese AI startups.

telegram · zaihuapd · Jul 7, 11:42

**Background**: China has rapidly developed advanced AI models like Alibaba's Qwen series, ByteDance's Doubao, and Zhipu AI's GLM series. Export controls on AI models are a growing trend globally, with the US already imposing restrictions on advanced AI chips and model weights. This move mirrors similar concerns about national security and technological leadership.

<details><summary>References</summary>
<ul>
<li><a href="https://zglg.work/ai/news/zh/2026-07-07-china-holds-talks-with-alibaba-and-bytedance-on-restricting-ai-model-exports">中国就限制 AI 模型出口与阿里巴巴和字节跳动展开磋商 | zglg.work</a></li>
<li><a href="https://zh.wikipedia.org/wiki/智谱">智谱 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#China`, `#export control`, `#national security`, `#tech policy`

---

<a id="item-5"></a>
## [Kokoro: CPU-Friendly, High-Quality Open-Source TTS](https://ariya.io/2026/03/local-cpu-friendly-high-quality-tts-text-to-speech-with-kokoro/) ⭐️ 8.0/10

Kokoro, an open-source text-to-speech model with 82 million parameters, delivers high-quality speech synthesis that runs efficiently on CPU without requiring a GPU. It supports manual IPA pronunciation guides to correct homograph errors. This makes high-quality TTS accessible to users without powerful GPUs, democratizing voice synthesis for accessibility tools, content consumption, and more. The IPA support addresses a common pain point in TTS accuracy. Kokoro-82M is optimized for Apple Silicon via mlx-audio but also runs on other CPUs. Community members have built Chrome extensions and RSS-based podcast workflows using Kokoro.

hackernews · speckx · Jul 7, 18:24 · [Discussion](https://news.ycombinator.com/item?id=48821576)

**Background**: Most high-quality TTS models require a GPU for real-time inference, limiting their use for users with modest hardware. Kokoro is an open-source model that achieves competitive quality with only 82 million parameters, making it lightweight enough for CPU inference. IPA (International Phonetic Alphabet) allows precise pronunciation control, useful for homographs or foreign words.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Kokoro_TTS">Kokoro TTS</a></li>
<li><a href="https://github.com/nazdridoy/kokoro-tts">GitHub - nazdridoy/kokoro-tts: A CLI text-to-speech tool ...</a></li>

</ul>
</details>

**Discussion**: Community feedback is overwhelmingly positive, with users praising Kokoro's quality and CPU efficiency. Some note limitations with single-word utterances and homograph handling, but the IPA override feature mitigates this. Users have integrated Kokoro into accessibility products and podcast pipelines.

**Tags**: `#TTS`, `#machine learning`, `#accessibility`, `#open source`, `#CPU`

---

<a id="item-6"></a>
## [EU Chat Control Proposals Threaten Encryption](https://fightchatcontrol.eu/chat-control-overview) ⭐️ 8.0/10

The EU's Chat Control 1.0 and 2.0 proposals would mandate client-side scanning of encrypted messages to detect child sexual abuse material, effectively breaking end-to-end encryption. If enacted, these proposals would undermine digital privacy and security for all EU citizens, setting a dangerous precedent for mass surveillance and weakening encryption globally. Chat Control 1.0 allowed voluntary scanning under a temporary derogation from the ePrivacy Directive, while Chat Control 2.0 would make scanning mandatory. Both rely on client-side scanning, which scans content before encryption or after decryption on the user's device.

hackernews · gasull · Jul 7, 14:23 · [Discussion](https://news.ycombinator.com/item?id=48818311)

**Background**: Client-side scanning (CSS) is a technique that analyzes message content on the user's device before it is encrypted or after it is decrypted, bypassing end-to-end encryption. The EU's Chat Control proposals aim to combat child sexual abuse material (CSAM) but have been widely criticized by privacy advocates and security experts for creating vulnerabilities and enabling mass surveillance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Regulation_to_Prevent_and_Combat_Child_Sexual_Abuse">Chat Control - Wikipedia</a></li>
<li><a href="https://www.eff.org/deeplinks/2026/04/eu-parliament-blocks-mass-scanning-our-chats-whats-next">EU Parliament Blocks Mass-Scanning of Our Chats—What's Next? | Electronic Frontier Foundation</a></li>
<li><a href="https://www.patrick-breyer.de/en/posts/chat-control/">Chat Control: The EU's CSAM scanner proposal</a></li>

</ul>
</details>

**Discussion**: Commenters express strong opposition, arguing the proposals are a broad surveillance power grab rather than a targeted measure. Some note that even voluntary scanning (Chat Control 1.0) continues despite legal expiration, and others highlight the risk to innocent content like baby photos.

**Tags**: `#privacy`, `#encryption`, `#EU legislation`, `#surveillance`, `#cybersecurity`

---

<a id="item-7"></a>
## [Microsoft lays off id Tech engine team at id Software](https://gamefromscratch.com/microsoft-fire-idtech-team-at-id-software/) ⭐️ 8.0/10

Microsoft has laid off the entire id Tech engine development team at id Software, the studio behind iconic game engines like id Tech 7 used in Doom Eternal. This move effectively ends internal engine development at id Software, shifting focus to external engines like Unreal Engine 5. This layoff signals a major consolidation in the game engine market, reducing competition and innovation as more studios abandon proprietary engines for Unreal Engine 5. It also raises concerns about Microsoft's long-term strategy for its acquired studios, potentially homogenizing game development and losing unique technical expertise. The id Tech team was responsible for developing and maintaining id Software's proprietary game engine, which has powered titles like Doom, Quake, and Rage. The layoffs are part of broader restructuring at Microsoft's Xbox division, affecting multiple studios.

hackernews · bauc · Jul 7, 15:33 · [Discussion](https://news.ycombinator.com/item?id=48819244)

**Background**: id Software is a legendary game developer founded in 1991 by John Carmack and John Romero, known for pioneering first-person shooters and creating the id Tech engine series. The engines have been licensed to other developers and some versions were open-sourced. Microsoft acquired id Software's parent company ZeniMax Media in 2021.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Id_Tech">id Tech - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Id_Software">id Software - Wikipedia</a></li>
<li><a href="https://www.konvoy.vc/newsletters/the-great-unbundling-of-game-engines">The Great Unbundling of Game Engines - konvoy.vc</a></li>

</ul>
</details>

**Discussion**: The community expressed deep disappointment and concern, with many lamenting the loss of id's engine expertise and warning that this move strengthens Epic Games' monopoly on game engines. Some commenters criticized Microsoft's short-term cost-cutting strategy, arguing it will harm long-term innovation and studio culture.

**Tags**: `#gaming`, `#game engines`, `#Microsoft`, `#id Software`, `#layoffs`

---

<a id="item-8"></a>
## [sqlite-utils 4.0 Introduces Schema Migrations](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything) ⭐️ 8.0/10

sqlite-utils 4.0, released on July 7, 2026, adds database schema migrations, nested transactions via a new db.atomic() method, and support for compound foreign keys. This major release significantly enhances sqlite-utils, a widely-used Python CLI and library for SQLite, making it easier for developers to manage schema changes and complex transactions without external tools. Migrations are defined in Python files using the sqlite-utils Python library, leveraging the powerful table.transform() method that implements the SQLite-recommended pattern of creating a new table, copying data, and renaming. The release also includes breaking changes detailed in an upgrade guide.

rss · Simon Willison · Jul 7, 19:32

**Background**: Schema migrations allow developers to apply a sequence of changes to a database schema while tracking which have been applied. SQLite's ALTER TABLE is limited, so tools like sqlite-utils provide enhanced capabilities. Nested transactions enable atomic operations within larger transactions, and compound foreign keys allow referencing multiple columns in a parent table.

<details><summary>References</summary>
<ul>
<li><a href="https://sqlite-utils.datasette.io/en/latest/migrations.html">Database migrations - sqlite-utils</a></li>
<li><a href="https://simonwillison.net/2026/Jul/7/sqlite-utils-4/">sqlite-utils 4.0, now with database schema migrations</a></li>
<li><a href="https://sqlite.org/foreignkeys.html">SQLite Foreign Key Support</a></li>

</ul>
</details>

**Tags**: `#sqlite`, `#python`, `#database`, `#migrations`, `#open source`

---

<a id="item-9"></a>
## [Ph.D. Thesis on Differentiable Ray Tracing for Radio Propagation](https://www.reddit.com/r/MachineLearning/comments/1upvkp5/phd_thesis_on_differentiable_ray_tracing_for/) ⭐️ 8.0/10

A Ph.D. thesis titled 'Differentiable Ray Tracing for Radio Propagation Modeling' has been published, integrating differentiable ray tracing with automatic differentiation frameworks like JAX to compute exact gradients through physical environments for wireless communications. This work bridges radio propagation simulation and machine learning, enabling gradient-based optimization and direct ML training for inverse problems, which is crucial for next-generation wireless design such as 6G. The thesis is structured as a self-contained textbook with three parts: physics fundamentals, algorithmic core including GPU-accelerated path tracing and discontinuity smoothing, and practical applications like channel modeling and material calibration. The author provides open access and open-source libraries such as DiffeRT.

reddit · r/MachineLearning · /u/jeertmans · Jul 7, 13:45

**Background**: Differentiable ray tracing extends traditional ray tracing by enabling automatic differentiation through the rendering pipeline, allowing gradient computation with respect to scene parameters. JAX is a high-performance numerical computing library that supports automatic differentiation and GPU/TPU acceleration, commonly used in machine learning. Radio propagation modeling simulates how radio waves travel through environments, essential for wireless network planning.

<details><summary>References</summary>
<ul>
<li><a href="https://people.csail.mit.edu/tzumao/diffrt/">Differentiable Monte Carlo Ray Tracing through Edge Sampling</a></li>
<li><a href="https://research.nvidia.com/publication/2024-10_learning-radio-environments-differentiable-ray-tracing">Learning Radio Environments by Differentiable Ray Tracing | Research</a></li>
<li><a href="https://github.com/jax-ml/jax">GitHub - jax-ml/jax: Composable transformations of Python+NumPy programs: differentiate, vectorize, JIT to GPU/TPU, and more · GitHub</a></li>

</ul>
</details>

**Tags**: `#differentiable ray tracing`, `#radio propagation`, `#automatic differentiation`, `#JAX`, `#wireless communications`

---

<a id="item-10"></a>
## [Mozilla CTO Raffi Krikorian AMA on Open Source AI Report](https://www.reddit.com/r/MachineLearning/comments/1upxdvc/raffi_krikorian_cto_mozilla_ama_on_the_state_of/) ⭐️ 8.0/10

Mozilla CTO Raffi Krikorian will host an AMA on July 14, 2025, to discuss the inaugural State of Open Source AI report, covering real-world costs, enterprise adoption, China's influence, and developer trust. This AMA provides a rare opportunity to hear directly from a major open-source advocate about the practical challenges and opportunities in open-source AI, which is increasingly critical for enterprise adoption and developer trust. The report is based on a survey of over 950 developers and focuses on production realities rather than common narratives. Key topics include the 'hidden tax' of free models, the 'agentic harness' layer, and the impact of Chinese open-source models.

reddit · r/MachineLearning · /u/raffikrikorian · Jul 7, 14:51

**Background**: Open-source AI refers to AI models and tools with publicly available source code, allowing modification and redistribution. Mozilla, known for the Firefox browser, has been advocating for open and trustworthy AI. The 'agentic harness' is the infrastructure layer that wraps AI models to enable agent-like behaviors, such as managing context and external interactions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mozilla.org/en-US/foundation/annualreport/2024/article/evolving-together-redefining-mozilla-in-the-ai-era/">Evolving Together: Redefining Mozilla in the AI Era</a></li>
<li><a href="https://www.langchain.com/blog/the-anatomy-of-an-agent-harness">The Anatomy of an Agent Harness</a></li>
<li><a href="https://www.cio.com/article/4140634/the-hidden-tax-on-every-ai-initiative-and-how-to-stop-paying-it.html">The hidden tax on every AI initiative (and how to stop paying ...</a></li>

</ul>
</details>

**Tags**: `#open source`, `#AI`, `#Mozilla`, `#enterprise`, `#developer trust`

---

<a id="item-11"></a>
## [Constraining Fine-Tuning to Trusted LoRA Subspace](https://www.reddit.com/r/MachineLearning/comments/1uq68li/what_if_a_model_could_only_learn_what_trusted/) ⭐️ 8.0/10

A new paper proposes constraining fine-tuning updates to a subspace learned from trusted LoRA adapters, preventing malicious updates even if poisoned data is present. This geometric defense addresses a critical gap in fine-tuning security by making certain malicious directions geometrically unreachable, offering a practical safeguard for deploying models that adapt from user data. The approach was tested on 196 public LoRA adapters, including adaptive attacks designed to bypass the defense, and showed sharp drops in attack success while preserving useful adaptation on tasks covered by the adapter pool.

reddit · r/MachineLearning · /u/Bright_Warning_8406 · Jul 7, 20:00

**Background**: LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning technique that updates only a small set of low-rank matrices, reducing computational cost. Fine-tuning poisoning attacks inject hidden behaviors (backdoors) into models by manipulating training data. Existing defenses focus on detecting poisoned data or reducing its impact, but this work takes a different approach by restricting the space of possible updates.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/deep-learning/low-rank-adaptation-lora/">Low Rank Adaptation (LoRA) - GeeksforGeeks</a></li>
<li><a href="https://arxiv.org/abs/2402.12168">[2402.12168] Defending Against Weight-Poisoning Backdoor ... Defending Against Weight-Poisoning Backdoor Attacks for ... Data Poisoning Attacks of Fine-Tuning for Large Language ... LLM Poisoning: Detection, Defense, and Prevention Strategies I Poisoned an AI Model to Sell You Software: Fine-Tuning ... GitHub - agw2005/pbp-reproduced: Reproduction of the novel ...</a></li>
<li><a href="https://arxiv.org/pdf/2512.11760">SpectralKrum: A Spectral-Geometric Defense Against Byzantine ...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#security`, `#LoRA`, `#fine-tuning`, `#adversarial robustness`

---

<a id="item-12"></a>
## [China Plans $295B National Computing Network Over 5 Years](https://t.me/zaihuapd/42399) ⭐️ 8.0/10

China plans to invest approximately 2 trillion yuan ($295 billion) over the next five years to build a nationwide interconnected data center network, with state-owned telecom operators managing the core facilities. The plan prioritizes domestic AI chips from suppliers like Huawei, aiming for at least 80% domestic content to reduce reliance on US companies such as Nvidia and AMD. This massive investment could reshape the global AI hardware supply chain and cloud computing landscape, as China seeks technological self-sufficiency. It also signals a strategic shift toward integrating computing resources into a unified national network, making high-performance computing more accessible to businesses and public sectors. The plan is a key part of Beijing's 'Six Networks' infrastructure initiative, which aims to consolidate fragmented regional computing resources. Telecom operators like China Telecom and China Unicom have already launched 'token' packages that sell computing power like mobile data, paving the way for large-scale AI applications.

telegram · zaihuapd · Jul 7, 04:45

**Background**: China's 'Six Networks' infrastructure plan includes computing, energy, transportation, and other networks to support digital economy and AI development. The national computing network, also known as the 'East-to-West Computing Resources Transfer' project, aims to connect data centers across regions. Token-based pricing for computing power is a recent innovation by Chinese telecom operators, allowing users to purchase AI compute resources on demand.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gov.cn/lianbo/202605/content_7070126.htm">统筹建设、动态推进“六张网” - 中国政府网</a></li>
<li><a href="https://www.nda.gov.cn/sjj/swdt/mtsy/0616/20260616182702649345771_pc.html">六网织就新未来丨支撑人工智能等高质量发展 算力网开启万亿级投资周期...</a></li>
<li><a href="https://news.qq.com/rain/a/20260518A05V3X00">Token套餐全面上线!三大运营商悉数入局，算力进入“按Token收费”时代_...</a></li>

</ul>
</details>

**Tags**: `#China`, `#AI infrastructure`, `#computing network`, `#semiconductors`, `#cloud computing`

---

<a id="item-13"></a>
## [new-api Fixes Billing Bug: Oversized Params Cause Negative Charges](https://github.com/QuantumNous/new-api/commit/d0bd8aa) ⭐️ 8.0/10

The QuantumNous/new-api project has fixed a critical billing vulnerability where oversized user-controllable parameters could trigger integer overflow, causing the quota calculation to produce negative values and effectively reverse-charge the user. This vulnerability could allow attackers to exploit the billing system to gain free credits or even increase their balance, posing a serious financial risk to service providers using new-api. The fix strengthens input validation and prevents integer overflow, ensuring billing integrity. The fix introduces upper-bound validation on quota-related parameters and uses saturating arithmetic to prevent wraparound when converting results to integers. A follow-up commit adds boundary checks at other entry points to block similar attacks on pre-deduction and settlement logic.

telegram · zaihuapd · Jul 7, 07:26

**Background**: Integer overflow occurs when an arithmetic operation produces a value outside the representable range of an integer type, causing it to wrap around (e.g., a large positive number becomes negative). In billing systems, such flaws can be exploited to manipulate charges. new-api is an open-source API gateway that handles quota and billing for AI services, making this fix critical for production deployments.

<details><summary>References</summary>
<ul>
<li><a href="https://www.comparitech.com/blog/information-security/integer-overflow-attack/">What is an Integer Overflow Attack (with Examples)? - Comparitech CWE - CWE-190: Integer Overflow or Wraparound (4.20) Understanding & Exploiting Integer Overflow Vulnerabilities ... Vulnerability: Integer Overflow and Underflow - OWASP Foundation NVD - CVE-2025-54091 What is Integer Overflow? Exploits & Impact - blogs.jsmon.sh NVD - CVE-2026-3536</a></li>
<li><a href="https://deepwiki.com/QuantumNous/new-api/2.6-quota-and-billing-system">Quota & Billing System | QuantumNous/new-api | DeepWiki</a></li>
<li><a href="https://deepwiki.com/QuantumNous/new-api/9.2-quota-calculation-and-consumption">Quota Calculation and Consumption | QuantumNous/new-api ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#billing`, `#vulnerability`, `#open-source`, `#API`

---

<a id="item-14"></a>
## [Nvidia Blackwell Wafers Made in US, Still Packaged in Taiwan](https://www.tomshardware.com/tech-industry/nvidia-and-intel-tout-chips-built-in-america-but-every-arizona-made-blackwell-die-is-still-packaged-in-taiwan) ⭐️ 8.0/10

Nvidia's Blackwell wafers are now being mass-produced at TSMC's Fab 21 in Arizona using the custom 4NP process, but they must be shipped to Taiwan for advanced CoWoS-L packaging and HBM integration. This highlights a critical bottleneck in the US semiconductor supply chain: despite domestic wafer fabrication, advanced packaging capacity won't be fully available until 2028-2029, leaving reliance on Taiwan for the foreseeable future. The wafers travel over 7,000 miles from Arizona to Taiwan for dicing, stacking, and CoWoS-L packaging. Additionally, the US currently lacks facilities for HBM production and packaging, which are essential for AI accelerators.

telegram · zaihuapd · Jul 7, 09:47

**Background**: CoWoS (Chip-on-Wafer-on-Substrate) is an advanced 2.5D/3D packaging technology that interconnects logic dies and HBM stacks using a silicon interposer. TSMC's 4NP process is a custom 5nm-class node optimized for Nvidia. The US is investing in packaging fabs by Amkor, TSMC, and SK Hynix, but full supply chain independence is years away.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.csdn.net/u013669912/article/details/143434272">CoWoS 封装 | CoWoS-S / CoWoS-R / CoWoS-L-CSDN博客</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/688119389">RTX 50升级台积电4NP工艺：但其实还是5nm - 知乎</a></li>
<li><a href="https://baike.baidu.com/item/HBM封装/68105001">HBM封装_百度百科</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#supply chain`, `#Nvidia`, `#advanced packaging`, `#geopolitics`

---

<a id="item-15"></a>
## [DeepSeek Develops Own AI Chip to Reduce Reliance on NVIDIA and Huawei](https://www.reuters.com/world/china/chinas-deepseek-developing-its-own-ai-chip-sources-say-2026-07-07/) ⭐️ 8.0/10

DeepSeek is developing its own AI chip focused on inference, aiming to reduce dependence on NVIDIA and Huawei chips. The effort began about a year ago and is still in early stages, with the company recruiting chip design engineers and engaging with foundries and memory suppliers. This move signals a strategic shift in the AI hardware landscape, as DeepSeek seeks to circumvent US export controls that restrict access to advanced chips. If successful, it could reduce China's reliance on foreign chipmakers and accelerate the trend toward domestic AI chip development. The chip is designed specifically for inference, the stage where a trained model generates responses for users, rather than for training new models. DeepSeek previously relied on NVIDIA H800 and Huawei Ascend chips, and founder Liang Wenfeng acknowledged chip restrictions as a challenge in a rare 2024 interview.

telegram · zaihuapd · Jul 7, 11:08

**Background**: US export controls since 2018 have restricted China's access to advanced semiconductors and related technologies, impacting companies like DeepSeek that rely on high-performance AI chips. Inference computing is the fastest-growing segment of AI demand as applications spread, making inference-specific chips strategically important. DeepSeek's move mirrors a broader trend of Chinese firms shifting AI accelerator budgets to domestic suppliers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/world/china/chinas-deepseek-developing-its-own-ai-chip-sources-say-2026-07-07/">EXCLUSIVE: China's DeepSeek developing its own AI chip ...</a></li>
<li><a href="https://www.usnews.com/news/top-news/articles/2026-07-07/exclusive-chinas-deepseek-developing-its-own-ai-chip-sources-say">Exclusive-China's DeepSeek Developing Its Own AI Chip ...</a></li>
<li><a href="https://www.cryptopolitan.com/deepseek-plans-its-own-inference-chip/">DeepSeek plans its own inference chip, a threat to Nvidia and ...</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#DeepSeek`, `#semiconductors`, `#export controls`, `#inference`

---