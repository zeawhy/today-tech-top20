---
layout: default
title: "Horizon Summary: 2026-09-17 (EN)"
date: 2026-09-17
lang: en
---

> From 87 items, 12 important content pieces were selected

---

1. [AWS admits permanent data loss after Iran strike on Middle East facilities](#item-1) ⭐️ 9.0/10
2. [Nvidia Announces Native GPU Programming in Rust for CUDA Kernels](#item-2) ⭐️ 8.0/10
3. [Xiaomi launches live post-training dashboard for MiMo 2.6](#item-3) ⭐️ 8.0/10
4. [E-ink frame listens for birds and draws them as 1800s illustrations](#item-4) ⭐️ 8.0/10
5. [DeepMind Launches Policy Institute to Shape AI Governance](#item-5) ⭐️ 8.0/10
6. [Hackers Expose Hardcoded Credentials in Flock Surveillance Cameras](#item-6) ⭐️ 8.0/10
7. [TMLR probes authors of 10 desk-rejected papers on their own work](#item-7) ⭐️ 8.0/10
8. [GoBench benchmarks LLMs on 9x9 Go against KataGo](#item-8) ⭐️ 8.0/10
9. [Prior Labs releases TabPFN-3.5, new SOTA tabular foundation model](#item-9) ⭐️ 8.0/10
10. [StepFun Releases StepAudio 3 Music: Full Songs from Natural Language](#item-10) ⭐️ 8.0/10
11. [Sina Cloud SAE shuts down permanently, erasing early Bilibili video source files](#item-11) ⭐️ 8.0/10
12. [Micron Unveils World's First 512GB DDR5 RDIMM, Targeting 2027 Production](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AWS admits permanent data loss after Iran strike on Middle East facilities](https://www.wsj.com/world/middle-east/aws-says-it-cant-restore-some-data-from-mideast-facilities-struck-by-iran-ddcb7e5d) ⭐️ 9.0/10

AWS has acknowledged that some customer data stored in its Middle East facilities struck by Iran cannot be restored, marking a rare admission of permanent data loss by a hyperscaler. The disclosure directly contradicts earlier public assurances from AWS leadership that a single data center destruction would go unnoticed due to redundancy. This event undermines the long-held assumption that hyperscale cloud redundancy guarantees data survival even under extreme geopolitical events, forcing cloud architects and business continuity planners to rethink multi-region and multi-cloud strategies. It also highlights how data residency laws can trap data in vulnerable regions, leaving customers with no viable recovery path. The affected region appears to be me-south-1 (Bahrain) and me-central-1 (UAE), with community reports indicating availability zones down since early 2026. AWS's standard S3 durability guarantee of 11 nines (99.999999999%) applies to hardware failures within a region, not to the physical destruction of an entire region or to data that cannot be replicated out due to residency constraints.

hackernews · berkeleyjunk · Sep 15, 21:41 · [Discussion](https://news.ycombinator.com/item?id=49719249)

**Background**: Cloud redundancy typically involves replicating data across multiple availability zones or geographic regions so that an outage in one location does not cause data loss. Data residency laws, such as those in the UAE, require certain data to be stored and processed within national borders, which can prevent replication to other regions. Force majeure clauses in cloud contracts, like AWS's Section 11.3, excuse providers from liability for failures caused by events beyond their reasonable control, including war and acts of God.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_residency">Data residency</a></li>
<li><a href="https://en.wikipedia.org/wiki/Force_majeure">Force majeure</a></li>
<li><a href="https://www.akamai.com/glossary/what-is-cloud-redundancy">What Is Redundancy in Cloud Computing? | Akamai</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the contradiction between AWS's earlier claim that blowing up a data center would go unnoticed and the current admission of permanent loss. Many pointed to UAE data residency requirements as a key factor preventing replication, and some cited the force majeure clause and the 11 nines durability guarantee as evidence that customers bear the risk. The overall sentiment is critical of AWS's prior messaging and concerned about the real-world limits of cloud resilience.

**Tags**: `#AWS`, `#cloud infrastructure`, `#data loss`, `#geopolitics`, `#disaster recovery`

---

<a id="item-2"></a>
## [Nvidia Announces Native GPU Programming in Rust for CUDA Kernels](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/) ⭐️ 8.0/10

Nvidia published an official developer blog post introducing CUDA Rust, offering two tracks for writing GPU kernels natively in Rust. This marks Nvidia's first official endorsement of Rust as a first-class language for CUDA kernel development, moving beyond the long-standing C++-only convention. This is a significant shift for both the Rust and GPU computing communities, since Rust's memory-safety guarantees could reduce a major class of bugs in GPU code. It also signals that Nvidia is responding to developer demand for safer, more modern tooling while reinforcing CUDA's ecosystem dominance. The announcement describes two distinct tracks for writing CUDA kernels in Rust, though the blog post's tone drew criticism for reading like AI-generated marketing copy rather than Nvidia's usual technical writing. Community members also noted the comparison to existing projects like Rust-GPU and vectorware, and to DSLs such as Triton.

hackernews · nonmaskable · Sep 16, 11:15 · [Discussion](https://news.ycombinator.com/item?id=49724881)

**Background**: CUDA is Nvidia's proprietary parallel computing platform, and kernels are the functions programmers write to run on the GPU. Historically, writing CUDA kernels required C++, which tied codebases tightly to Nvidia hardware and made porting difficult. Rust is a systems programming language known for compile-time memory safety, and projects like Rust-GPU have been exploring GPU support in Rust for years.

<details><summary>References</summary>
<ul>
<li><a href="https://rust-gpu.github.io/rust-gpu/book/">Introduction - Rust GPU Dev Guide</a></li>
<li><a href="https://www.javacodegeeks.com/2026/09/cuda-and-the-vendor-lock-in-problem-in-gpu-programming.html">CUDA and the Vendor Lock-In Problem in GPU Programming</a></li>

</ul>
</details>

**Discussion**: Commenters were divided: some welcomed anything that makes reliable GPU code less painful, while others strongly criticized CUDA's proprietary nature and the vendor lock-in it creates. Several noted the blog's AI-sounding tone, and others pointed to related work like Hugging Face's Candle crate and vectorware as context for judging the announcement.

**Tags**: `#Rust`, `#GPU`, `#CUDA`, `#Nvidia`, `#Programming Languages`

---

<a id="item-3"></a>
## [Xiaomi launches live post-training dashboard for MiMo 2.6](https://mimo.xiaomi.com/rl/) ⭐️ 8.0/10

Xiaomi has released a public live dashboard at mimo.xiaomi.com/rl/ that shows real-time post-training and reinforcement learning progress for its MiMo 2.6 model. The dashboard exposes training runs and RL environment scores as they happen, a rare move toward transparency in frontier AI development. By making post-training and RL progress publicly visible, Xiaomi sets a precedent that could pressure other labs—especially those with near-frontier models—to disclose more about how their models are trained. This transparency could reshape how the community evaluates model quality and trustworthiness, and it strengthens Xiaomi's position in the open-source AI ecosystem. The dashboard focuses on the post-training phase, which includes supervised fine-tuning and reinforcement learning, rather than the initial pre-training. Community members noted that the previous MiMo-V2.5-Pro scored only 19% on DeepSWE 1.1, while competitors like Fable, Kimi K3, and Astra scored 69–74%, suggesting MiMo 2.6 is aiming for a significant jump in coding and reasoning benchmarks.

hackernews · krackers · Sep 16, 20:09 · [Discussion](https://news.ycombinator.com/item?id=49732270)

**Background**: MiMo is a family of large language models developed by Xiaomi, first released in April 2025 with the MiMo-7B model and now available to developers via API. Post-training is the stage after large-scale pre-training where techniques like supervised fine-tuning (SFT) and reinforcement learning (RL) are used to align a model with human preferences and improve reasoning. Live dashboards for RL training are common in robotics and game AI research, but publishing one for a frontier-scale language model is unusual and signals a new level of openness.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xiaomi_MiMo">Xiaomi MiMo - Wikipedia</a></li>
<li><a href="https://pytorch.org/blog/a-primer-on-llm-post-training/">A Primer on LLM Post-Training - PyTorch</a></li>
<li><a href="https://huggingface.co/blog/karina-zadorozhny/guide-to-llm-post-training-algorithms">A Guide to Reinforcement Learning Post-Training for LLMs: PPO, DPO, GRPO, and Beyond</a></li>

</ul>
</details>

**Discussion**: The community reaction is overwhelmingly positive, with users praising MiMo 2.5's cost-effectiveness and quality for software engineering tasks, and applauding Xiaomi for the transparency of the dashboard. Some commenters frame this as a competitive threat to closed labs like OpenAI and Anthropic, while others share benchmark comparisons showing MiMo 2.6's potential improvement over its predecessor.

**Tags**: `#AI`, `#machine-learning`, `#open-source`, `#model-training`, `#transparency`

---

<a id="item-4"></a>
## [E-ink frame listens for birds and draws them as 1800s illustrations](https://github.com/arnegiacomo/fugleramme) ⭐️ 8.0/10

Developer Arne Munthe-Kaas (arnegiacomo) published a GitHub project called 'fugleramme' that combines an e-ink display, an ESP32 microcontroller, and the BirdNET neural network to detect bird calls and render the identified species as 1800s-style illustrations. The project was shared on Hacker News as a 'Show HN' post and quickly drew 240 comments and an 8.0/10 score. The project is a standout example of playful, cross-disciplinary engineering that blends embedded hardware, bioacoustics AI, and generative illustration, showing how cheap microcontrollers and open models can turn everyday nature observation into a magical ambient experience. It also highlights the growing ecosystem of ESP32 plus e-ink DIY devices and the popularity of BirdNET-based bird monitoring tools. The classifier is BirdNET, a traditional convolutional neural network for acoustic bird identification rather than an LLM, and the e-ink display is chosen for its paper-like, low-power characteristics that suit always-on ambient devices. The project is hosted at github.com/arnegiacomo/fugleramme and was cross-referenced with a related May 2026 HN post titled 'Avian Visitors'.

hackernews · arnemunthekaas · Sep 15, 12:31 · [Discussion](https://news.ycombinator.com/item?id=49711544)

**Background**: BirdNET is an AI system developed at the Cornell Lab of Ornithology and Chemnitz University of Technology that identifies bird species from sound recordings, and it is widely used in ecological research and consumer apps. E-ink (electronic ink) displays look like paper, consume almost no power when static, and are popular in DIY projects built around the ESP32, a low-cost Wi-Fi/Bluetooth microcontroller. This project sits at the intersection of those two trends, adding a generative illustration layer that turns detected species into 19th-century-style drawings.

<details><summary>References</summary>
<ul>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://www.howtogeek.com/esp32-e-ink-display-projects-weekend-may-29-jun-1/">5 ESP32-powered E-Ink display projects to make this weekend ...</a></li>

</ul>
</details>

**Discussion**: Commenters were highly enthusiastic, with one calling it 'the coolest thing on HN' and praising its blend of ideas into something magical; others clarified that BirdNET is a traditional neural network rather than an LLM, shared their own ESP32/e-ink projects and battery-life calculations, and noted the recent wave of bird-related projects such as birdnet-go. A Norwegian commenter described the work as 'pure art' by the developer.

**Tags**: `#e-ink`, `#birdnet`, `#esp32`, `#hardware`, `#creative-coding`

---

<a id="item-5"></a>
## [DeepMind Launches Policy Institute to Shape AI Governance](https://institute.deepmind.com/) ⭐️ 8.0/10

DeepMind has launched the DeepMind Institute, an in-house policy think tank publishing positions on reasoning transparency, economic policy for AGI, and principles for a new utopianism. The launch quickly drew scrutiny on Hacker News, where users questioned the framing of AGI timelines and noted that many top links were submitted by a single 11-day-old account. A leading AI lab directly entering policy debates could shape regulation, labor-market safeguards, and how AI profits are distributed, affecting governments, workers, and competitors alike. It also raises questions about whether corporate-funded research can be a neutral voice in governance discussions. The institute's economic policy article outlines three impact scenarios from mild to major disruption, proposing expanded unemployment insurance and Earned Income Tax Credit in milder cases and profit-sharing or ownership stakes in AI in more severe ones, plus AI evaluators to weigh policy effectiveness. Its AGI framing claims today's systems are approaching human-brain-level cognitive capabilities, a claim commenters strongly disputed.

hackernews · vertigoruntime · Sep 16, 14:32 · [Discussion](https://news.ycombinator.com/item?id=49727659)

**Background**: DeepMind is Google's AI research lab, known for systems like AlphaGo and AlphaFold, and AGI refers to a hypothetical AI with all the cognitive capabilities of the human brain. Policy institutes are organizations that research and recommend governance approaches, and AI labs have increasingly created their own to influence regulation. Debates over AGI timelines and AI's economic impact have intensified as models grow more capable.

<details><summary>References</summary>
<ul>
<li><a href="https://institute.deepmind.com/">DeepMind Institute</a></li>
<li><a href="https://gsas.harvard.edu/news/how-ai-might-impact-economy-and-what-government-could-do-about-it">How AI Might Impact the Economy—and What Government Could Do ...</a></li>
<li><a href="https://skynetcountdown.com/agi-timeline">AGI Timeline 2026: Expert Predictions Tracker | Skynet Countdown</a></li>

</ul>
</details>

**Discussion**: Commenters were split: one praised the economic policy article as sensible and well-reasoned, while others accused the institute of being an in-house think tank pushing an agenda with exaggerated AGI claims. Several users flagged apparent astroturfing, noting that many top links came from a single 11-day-old account, and one criticized the website's low-contrast grey text.

**Tags**: `#AI policy`, `#DeepMind`, `#AGI`, `#AI governance`, `#economics`

---

<a id="item-6"></a>
## [Hackers Expose Hardcoded Credentials in Flock Surveillance Cameras](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 8.0/10

Security researcher Micah Lee published findings showing that Flock Safety's ALPR surveillance cameras contain hardcoded API keys and plaintext credentials, allowing attackers with physical access to extract sensitive data. The disclosure was made in collaboration with 404 Media, and Distributed Denial of Secrets has published the camera partition images. Flock operates in over 6,000 communities across 49 US states and performs over 20 billion vehicle scans monthly, so these vulnerabilities could expose a massive surveillance network to unauthorized access. The incident raises serious questions about the security practices of companies handling sensitive law-enforcement data. The hardcoded API key can be used to request credentials that are stored in plaintext, potentially granting access to Flock's servers; however, it is not yet clear what an attacker could do after authenticating as a camera. Flock's Vulnerability Disclosure Policy has been criticized for carving out exceptions when researchers must interact with the device or download its data.

hackernews · driverdan · Sep 16, 13:18 · [Discussion](https://news.ycombinator.com/item?id=49726586)

**Background**: Flock Safety is a company that builds automated license plate recognition (ALPR) cameras and a nationwide network that shares vehicle data with police departments. ALPR cameras capture images of passing vehicles and use machine learning to identify license plates, and Flock has been expanding into video feeds and AI-powered natural-language searches. Hardcoded credentials are secrets embedded directly in source code or firmware, making them easy for attackers to extract from physical devices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://www.aclu.org/news/privacy-technology/tracking-alpr-cameras/flock-roundup">Flock’s Aggressive Expansions Go Far Beyond Simple Driver Surveillance | American Civil Liberties Union</a></li>
<li><a href="https://blogs.jsmon.sh/what-is-hardcoded-api-keys-in-mobile-apps-ways-to-exploit-examples-and-impact/">Hardcoded API Keys in Mobile Apps: Risks & Fixes</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong criticism of Flock, calling hardcoded credentials a sign of incompetence and describing the company's Vulnerability Disclosure Policy as performative rather than genuinely aimed at learning about flaws. Several noted that the use of off-the-shelf hardware and software in public spaces makes local physical access a real threat, and one commenter highlighted that the data is not even suitably encrypted on the device.

**Tags**: `#security`, `#vulnerability-disclosure`, `#surveillance`, `#IoT`, `#privacy`

---

<a id="item-7"></a>
## [TMLR probes authors of 10 desk-rejected papers on their own work](https://www.reddit.com/r/MachineLearning/comments/1wid67h/tmlr_reached_out_to_the_authors_of_10_papers/) ⭐️ 8.0/10

TMLR's Co-Editor-in-Chief reached out to the authors of 10 papers slated for desk rejection to ask them to explain their own submissions, and the results were concerning: one paper was withdrawn, one author cited other commitments, one scheduled a meeting but did not show up, three authors could not answer basic questions, three could handle high-level ideas but struggled with technical details, and only one answered all questions — though the interviewer still identified a major flaw in that paper. This experiment suggests that a meaningful share of submissions may not be genuinely authored by the people who submit them, pointing to possible AI-generated papers or paper-mill activity and raising hard questions about the integrity of peer review and authorship verification in machine learning publishing. The probe covered only 10 desk-rejected submissions, so the sample is small and self-selected, and desk rejection itself is reserved for clear cases such as non-anonymized submissions, violations of the unmodified TMLR stylefile requirement, or obvious overlap with already published or under-review work.

reddit · r/MachineLearning · /u/hihey54 · Sep 16, 23:20

**Background**: TMLR (Transactions on Machine Learning Research) is an open-review machine learning journal that publishes reviews publicly and uses desk rejection to filter out submissions that violate basic formatting or originality rules before review. Academic authorship normally means making genuine intellectual contributions to the work, and it is the primary basis for hiring, promotion, and tenure decisions, which is why journals increasingly worry about submissions whose listed authors cannot explain their own research.

<details><summary>References</summary>
<ul>
<li><a href="https://jmlr.org/tmlr/ae-guide.html">TMLR guidelines for action editors</a></li>
<li><a href="https://en.wikipedia.org/wiki/Academic_authorship">Academic authorship - Wikipedia</a></li>
<li><a href="https://phdflow.ai/guides/tmlr-explained">TMLR explained: a differently shaped bar, not a lower one</a></li>

</ul>
</details>

**Tags**: `#peer-review`, `#academic-publishing`, `#research-integrity`, `#machine-learning`, `#AI-ethics`

---

<a id="item-8"></a>
## [GoBench benchmarks LLMs on 9x9 Go against KataGo](https://www.reddit.com/r/MachineLearning/comments/1wi68jg/gobench_evaluating_llms_on_the_game_of_go_r/) ⭐️ 8.0/10

GoBench is a new benchmark that evaluates large language models on 9x9 Go games against a ladder of KataGo opponents ranging from random play to superhuman strength. Its author reports that GPT-6 Astra max reaches 2500 Elo, far below the best KataGo at 4400 Elo, while Codex with Astra reaches 3560 Elo when given coding tools and two hours of preparation. The benchmark shows a strong correlation (r=0.83) with ARC-AGI 2, suggesting Go performance may serve as a proxy for general reasoning ability, and it remains highly unsaturated, leaving substantial headroom for future models. This gives researchers a new, open-source tool for measuring LLM reasoning progress beyond saturated text benchmarks. The evaluation uses 9x9 Go rather than the full 19x19 board, and the leaderboard will be kept updated as long as it is not saturated. The author has released the leaderboard, code, and paper openly, and notes that tool use and preparation time significantly boost model Elo.

reddit · r/MachineLearning · /u/Roland31415 · Sep 16, 18:54

**Background**: KataGo is a free, open-source computer Go engine trained via self-play with deep neural networks and advanced search, capable of superhuman play. Elo is a rating system originally developed for chess and also used in Go to quantify relative playing strength, where higher numbers indicate stronger players. ARC-AGI 2 is a benchmark designed to stress-test state-of-the-art AI reasoning systems and track progress toward AGI.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/KataGo">KataGo - Wikipedia</a></li>
<li><a href="https://arcprize.org/arc-agi/2">ARC-AGI-2</a></li>
<li><a href="https://en.wikipedia.org/wiki/Elo_rating_system">Elo rating system - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#benchmark`, `#Go`, `#reasoning`, `#AI`

---

<a id="item-9"></a>
## [Prior Labs releases TabPFN-3.5, new SOTA tabular foundation model](https://www.reddit.com/r/MachineLearning/comments/1wh4xhy/tabpfn35_is_released_as_the_next_sota_tabular/) ⭐️ 8.0/10

Prior Labs released TabPFN-3.5, a new tabular foundation model that now tops both the TabArena and BeyondArena benchmarks, with support for up to 1M rows and 20k features. The release includes three variants: TabPFN-3.5-Fast (in alpha, 6x faster than the base model), TabPFN-3.5-Thinking (available via API, trading compute for accuracy), and TabPFN-3.5-Plus. This is a significant state-of-the-art advance in tabular foundation models, a domain where gradient-boosted trees have long dominated and where foundation models have struggled to match them off-IID. The large Elo gains on BeyondArena suggest foundation models are closing the gap on text-rich, high-cardinality, and high-dimensional tabular data, which could shift how practitioners approach tabular ML. On BeyondArena, TabPFN-3.5 leads on text-rich, high-cardinality, and high-dimensional data with +250 Elo over the strongest previous baseline and +150 Elo ahead of the previous overall leader. TabPFN-3.5-Thinking adds +20 Elo over the base model on BeyondArena and +44 Elo on TabArena, while the Fast variant is still in alpha.

reddit · r/MachineLearning · /u/tuanacelik · Sep 15, 16:18

**Background**: TabPFN is a foundation model for small- to medium-sized tabular data, introduced in a 2025 Nature paper by Hollmann, Müller, Purucker and colleagues, and designed to make accurate predictions without dataset-specific training. TabArena is a continuously maintained "living" benchmark for tabular ML that standardizes preprocessing and evaluation, while BeyondArena extends evaluation beyond IID data to temporal and grouped tasks across a wide range of dataset sizes and dimensionalities. Elo is a relative rating system, originally from chess, used here to compare model performance across benchmark tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-024-08328-6">Accurate predictions on small data with a tabular foundation model | Nature</a></li>
<li><a href="https://arxiv.org/abs/2506.16791">[2506.16791] TabArena: A Living Benchmark for Machine Learning on Tabular Data</a></li>
<li><a href="https://aiweekly.co/alerts/beyondarena-finds-trees-still-beat-tabular-fms-off-iid-data">BeyondArena finds trees still beat tabular FMs off-IID data | AI Weekly</a></li>

</ul>
</details>

**Tags**: `#tabular-data`, `#foundation-models`, `#machine-learning`, `#benchmarking`, `#SOTA`

---

<a id="item-10"></a>
## [StepFun Releases StepAudio 3 Music: Full Songs from Natural Language](https://static.stepfun.com/blog/stepaudio3/music/) ⭐️ 8.0/10

StepFun has released StepAudio 3 Music, an AI music generation model that produces complete 48 kHz stereo songs directly from natural language descriptions. It combines a Mixture-of-Experts (MoE) architecture with an AR + DiT paradigm and an ABC-COT technique that converts creative intent into a song structure plan before audio synthesis, achieving state-of-the-art results on the Audiobox and MuQ-Similarity benchmarks. This marks a notable step forward in AI music generation, since the model claims to balance musical quality with controllability by letting users specify style, vocals, mood, instruments, key, and tempo in plain language. It targets practical applications such as short-video soundtracks, songwriting demos, and game theme music, where fast, customizable full-song generation is valuable. The model outputs full 48 kHz stereo audio and uses the ABC-COT technique to plan song structure from natural language before generation, with benchmark leadership on Audiobox and MuQ-Similarity. However, the announcement provides no details on model size, training data, latency, licensing, or public availability, so independent verification of the SOTA claims is still pending.

telegram · zaihuapd · Sep 16, 08:48

**Background**: Mixture-of-Experts (MoE) is a deep learning architecture in which only a subset of specialized sub-networks, or 'experts,' is activated for each input, improving efficiency and scaling for large models. AR + DiT combines autoregressive (AR) sequence modeling with Diffusion Transformers (DiT), a sequence-based generative architecture that has largely replaced U-Net designs in modern image and audio generation. ABC-COT appears to be StepFun's chain-of-thought-style planning method that translates a user's natural language brief into an explicit song structure before the audio is synthesized.

<details><summary>References</summary>
<ul>
<li><a href="https://www.architectureandgovernance.com/applications-technology/mixture-of-experts-moe-architecture-a-deep-dive-and-comparison-of-top-open-source-offerings/">Mixture of Experts ( MoE ) Architecture : A Deep Dive and Comparison...</a></li>
<li><a href="https://blog.bako.co/deconstructing-the-diffusion-transformer-paradigm">Deconstructing the Diffusion Transformer ( DiT ) Paradigm - BAKO Blog</a></li>
<li><a href="https://www.lmsys.org/blog/2026-08-05-glmImage-optimization/">Full-Stack Performance Optimization of AR + DiT in... - LMSYS Org</a></li>

</ul>
</details>

**Tags**: `#AI music generation`, `#MoE`, `#AR+DiT`, `#natural language processing`, `#audio synthesis`

---

<a id="item-11"></a>
## [Sina Cloud SAE shuts down permanently, erasing early Bilibili video source files](https://tracker.archiveteam.org/sinavideo/#show-all) ⭐️ 8.0/10

Sina Cloud SAE, China's first PaaS platform launched in 2009, will permanently shut down at 24:00 on September 16, 2026, deleting all user data. Roughly 420 TB of early Bilibili video source files still stored in Sina Cloud S3 buckets will be lost, while Archive Team's distributed archiving project has rescued about 680 TB and reached 96.26% completion. This marks the end of China's first public PaaS platform after nearly 17 years and represents a major loss of early Chinese internet video history that may never be recoverable. It highlights how cloud platform shutdowns can silently destroy cultural heritage, and underscores the critical role of volunteer digital preservation efforts. The shutdown notice was sent to users on June 10, 2026, confirming the September 16, 2026 termination date. Archive Team's rescue effort is a distributed volunteer project, and the remaining 3.74% of data may be lost forever once the platform goes offline.

telegram · zaihuapd · Sep 16, 15:00

**Background**: Sina App Engine (SAE), later renamed Sina Cloud, was launched in 2009 as China's first public PaaS offering, providing website hosting, storage, databases, caching, queues, and security services to nearly a million developers. PaaS (Platform as a Service) lets developers deploy and run applications without managing underlying servers, which made SAE popular for its low cost and zero-maintenance model. Archive Team is a volunteer collective co-founded by Jason Scott in 2009 that races to preserve content on at-risk online services, having previously saved GeoCities, Yahoo! Video, Google Video, and TwitPic.

<details><summary>References</summary>
<ul>
<li><a href="https://wanyr.com/2026/06/新浪云（sae）宣布9月16日永久关停：国内首家paas平台17.html">新浪云（SAE）宣布9月16日永久关停：国内首家PaaS平台17年历程落幕</a></li>
<li><a href="https://en.wikipedia.org/wiki/Archive_Team">Archive Team</a></li>
<li><a href="https://sae.sinacloud.com/">网站连接 - 新浪云计算</a></li>

</ul>
</details>

**Tags**: `#cloud-computing`, `#digital-preservation`, `#PaaS`, `#Bilibili`, `#data-loss`

---

<a id="item-12"></a>
## [Micron Unveils World's First 512GB DDR5 RDIMM, Targeting 2027 Production](https://videocardz.com/newz/micron-says-worlds-first-512gb-ddr5-module-will-be-production-ready-for-2027) ⭐️ 8.0/10

Micron announced the world's first 512GB DDR5 RDIMM for servers, achieving speeds up to 9200 MT/s and using 3D stacked DRAM dies. The company says the module will be production-ready by 2027, with AMD and Intel actively validating it for future server platforms. This represents a major memory density breakthrough for data centers, as 24 modules can deliver 12TB of memory per server, enabling larger AI/ML models and in-memory databases to run on fewer systems. The over 60% power reduction per module also addresses the growing energy costs of dense server deployments. Each 512GB module consumes 16W, compared to 44.2W for four 128GB modules delivering the same capacity, a reduction of over 60%. The module uses 3D stacked DRAM and is being validated by AMD and Intel, though production is not expected until 2027.

telegram · zaihuapd · Sep 16, 16:15

**Background**: DDR5 RDIMM is a registered DIMM form factor used in servers, where a register chip buffers address and command signals to improve stability and allow higher capacities. 3D stacked DRAM refers to stacking multiple DRAM dies vertically and connecting them with through-silicon vias (TSVs), a technique popularized by High Bandwidth Memory (HBM) to increase density and bandwidth within a small footprint. Micron's use of this technique in a standard RDIMM module is notable because it brings HBM-like density to conventional server memory slots.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/micron-crams-512-gb-memory-into-single-ddr5-stick-next-gen-intel-amd-servers/">Micron Crams 512 GB Memory Into A Single DDR5 Stick, Pushing...</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#DDR5`, `#memory`, `#server hardware`, `#Micron`, `#3D stacking`

---