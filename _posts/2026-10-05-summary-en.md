---
layout: default
title: "Horizon Summary: 2026-10-05 (EN)"
date: 2026-10-05
lang: en
---

> From 51 items, 12 important content pieces were selected

---

1. [2026 Nobel Prize in Physiology or Medicine Awarded for Optogenetics](#item-1) ⭐️ 9.0/10
2. [vLLM v0.31.0 Boosts DeepSeek-V4.1-Flash and Adds Fast Restart](#item-2) ⭐️ 8.0/10
3. [Denmark CPR Registry Breach Exposes 8.8 Million People's Data](#item-3) ⭐️ 8.0/10
4. [Strata Runs 125B Qwen 3.8 Flash Next on RTX 4090 at 100+ T/s](#item-4) ⭐️ 8.0/10
5. [CedarDB ports original Doom to run entirely in SQL](#item-5) ⭐️ 8.0/10
6. [Distilling Stockfish into a ResNet/ViT Model on 1B Positions, 3.9B Dataset Released](#item-6) ⭐️ 8.0/10
7. [Yandex Music's Sona transformer replaces 15+ component recommender pipeline](#item-7) ⭐️ 8.0/10
8. [ARC-AGI-3 Kaggle scores jump from 7% to 56% in 30 days](#item-8) ⭐️ 8.0/10
9. [SK Telecom Apologizes for Massive Data Breach, Offers Free USIM Replacements](#item-9) ⭐️ 8.0/10
10. [Google Releases VeriHarness Self-Verification Framework for Long-Horizon Tasks](#item-10) ⭐️ 8.0/10
11. [Huawei and Qualcomm Sign Broad Multi-Year Patent Deal Covering 5G and AI](#item-11) ⭐️ 8.0/10
12. [Quad9 Refuses French DNS Blocking Order, Faces €580K Daily Fine](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [2026 Nobel Prize in Physiology or Medicine Awarded for Optogenetics](https://www.nobelprize.org/all-nobel-prizes-2026/) ⭐️ 9.0/10

The 2026 Nobel Prize in Physiology or Medicine was awarded to Karl Deisseroth, Peter Hegemann, and Georg Nagel for their discovery of light-controlled ion channels and the development of optogenetics. This technique allows researchers to turn individual neurons on or off in the living brain using light. Optogenetics has revolutionized neuroscience by providing unprecedented precision in controlling neuronal activity, and it is now used in laboratories worldwide to study brain function and behavior. The Nobel recognition highlights the technique's broad impact on understanding decision-making, learning, memory, and even restoring vision in blind patients. Optogenetics works by expressing light-sensitive ion channels, such as channelrhodopsin, in specific neurons, allowing millisecond-precision control with light pulses. Beyond basic research, it has entered clinical trials, including a case where vision was partially restored in a patient with retinitis pigmentosa.

telegram · zaihuapd · Oct 5, 09:33

**Background**: Optogenetics is a biological technique that uses light to control cells in living tissue, typically neurons, that have been genetically modified to express light-sensitive ion channels. The approach was pioneered by Deisseroth, Hegemann, and Nagel, building on earlier discoveries of microbial rhodopsins that respond to light. It has become a foundational tool in systems neuroscience, enabling causal tests of how specific neural circuits contribute to behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Optogenetics">Optogenetics</a></li>
<li><a href="https://en.wikipedia.org/wiki/Karl_Deisseroth">Karl Deisseroth - Wikipedia</a></li>
<li><a href="https://deisseroth.com/">Karl Deisseroth — A timeline of discovery, from light to life</a></li>

</ul>
</details>

**Tags**: `#neuroscience`, `#optogenetics`, `#Nobel Prize`, `#research breakthrough`, `#science news`

---

<a id="item-2"></a>
## [vLLM v0.31.0 Boosts DeepSeek-V4.1-Flash and Adds Fast Restart](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) ⭐️ 8.0/10

vLLM released v0.31.0, a major update with 717 commits from 307 contributors (96 new). It delivers extensive performance optimizations for DeepSeek-V4.1-Flash, including FlashMLA mega attention with NVFP4 compressed KV cache as the SM100 default, plus a new fast restart capability via the `vllm preload` CLI that keeps post-quantized weights resident in GPU memory across engine restarts. As one of the most widely used open-source LLM inference engines, vLLM's improvements directly affect how efficiently and cheaply organizations can serve large models. The DeepSeek-V4.1-Flash optimizations and fast restart feature can significantly reduce latency and downtime for production deployments, making this release highly relevant to the AI/ML infrastructure community. The release includes several breaking changes: per-request multimodal kwargs are now gated behind `--trust-request-mm-kwargs`, `tokenizer_mode="slow"` was removed, `--enable-mamba-fine-grained-prefix-cache` was renamed to `--enable-mamba-shared-prefix-checkpoint`, and online quantization via `quantization="fp8"` was replaced by the `fp8_per_tensor` shorthand. It also adds scheduling controls like `--max-num-active-seqs` and `--long-prefill-token-threshold`, plus security hardening for prefix-cache keys and LoRA paths.

github · khluu · Oct 5, 06:44

**Background**: vLLM is an open-source framework for inference and serving of large language models, originally developed at UC Berkeley's Sky Computing Lab and centered on the PagedAttention memory-management method for transformer KV caches. It supports continuous batching, distributed inference, quantization, and OpenAI-compatible APIs. DeepSeek-V4.1-Flash is a multimodal large language model from DeepSeek, trained on a 45T-token corpus with sparse attention and context extended to 1M tokens. FlashMLA is DeepSeek's library of optimized attention kernels that power its models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLLM">VLLM</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek-V4.1-Flash">DeepSeek-V4.1-Flash</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/ FlashMLA : FlashMLA : Efficient Multi-head...</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#release`, `#performance optimization`, `#DeepSeek`

---

<a id="item-3"></a>
## [Denmark CPR Registry Breach Exposes 8.8 Million People's Data](https://www.cpr.dk/cpr-nyt/nyhedsarkiv/2026/okt/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger) ⭐️ 8.0/10

Denmark's national civil registration system (CPR) suffered a massive unauthorized data breach affecting the personal information of 8.8 million people, including all living Danish citizens and foreign nationals who have had residence in the country, as well as some deceased individuals. The compromised data reportedly includes CPR numbers, age, sex, family relations, physical and protected addresses, and sex change records. This is one of the largest national data breaches in Danish history, exposing sensitive identity data that could enable identity theft, fraud, and targeted attacks on vulnerable individuals such as those with protected addresses. It raises urgent questions about government data security and the systemic privacy risks of centralized citizen registries across the EU. The breach affects all living Danish citizens and foreign nationals who have had residence in Denmark, plus some deceased individuals, and includes highly sensitive fields like protected addresses and sex change records. It comes just days after a separate breach at the Technical University of Denmark (DTU) that exposed CPR numbers of students, faculty, and staff.

hackernews · clan · Oct 5, 08:09 · [Discussion](https://news.ycombinator.com/item?id=49962012)

**Background**: In Denmark, every resident is assigned a CPR number (Central Person Register number), a civil registration identifier used for all contact with Danish authorities, healthcare, banks, and many private institutions. Because it functions as a universal identity key, compromise of CPR data is especially dangerous—it can be used to impersonate individuals, open accounts, or access services. Denmark has previously faced criticism over inadequate anonymization of health and research data, and the country is currently debating the 'Chat Control' proposal that critics say could undermine end-to-end encryption across the EU.

<details><summary>References</summary>
<ul>
<li><a href="https://ihcph.kk.dk/registration-guidance/cpr-registration">CPR registration | International House Copenhagen</a></li>
<li><a href="https://www.norden.org/en/info-norden/civil-registration-denmark">Civil registration in Denmark | Nordic cooperation</a></li>
<li><a href="https://international.kk.dk/live/cpr-registration-and-documents/cpr-registration">CPR registration | City of Copenhagen</a></li>

</ul>
</details>

**Discussion**: Commenters expressed deep frustration with systemic privacy erosion, with one noting they now avoid routine activities like visiting doctors or booking flights out of fear of data misuse. Others pointed to Sweden's model of openly publishing residents' data as a contrast, warned that Denmark's Chat Control push could enable mass leaks of EU private conversations, and highlighted the breach's enormous scope—covering nearly the entire Danish population—as well as its proximity to the DTU breach days earlier.

**Tags**: `#data-breach`, `#privacy`, `#cybersecurity`, `#denmark`, `#identity-theft`

---

<a id="item-4"></a>
## [Strata Runs 125B Qwen 3.8 Flash Next on RTX 4090 at 100+ T/s](https://github.com/Niko1221/Strata) ⭐️ 8.0/10

A new open-source inference stack called Strata enables running the 125B-parameter Qwen 3.8 Flash Next Mixture-of-Experts model on consumer hardware such as the RTX 4090 at over 100 tokens per second. However, independent testing by a community member found that Strata produced a median error of 154.8 pixels on a 50-image vision benchmark, compared to 46.5 pixels when running the same GGUF and vision adapter weights on llama.cpp. This is significant because it suggests that very large Mixture-of-Experts models can be run locally on consumer GPUs at usable speeds, potentially reducing reliance on cloud inference for agentic coding, tool use, and vision tasks. The reported accuracy degradation, however, highlights the trade-offs between aggressive quantization and output quality, which matters for practitioners who need reliable results. Qwen 3.8 Flash Next has 125B total parameters with only 6B activated per token, plus 51B n-gram embeddings and 4B MTP, and is described as the first open-weight model built on the architecture that will underpin Qwen 4. Community reports show speeds of 124 T/s on an RTX 4090 with 128GB DDR5, about 60 T/s on an R9700 32GB with 96GB DDR4, and even 10 T/s on a Ryzen 6600H iGPU, though the accuracy gap versus llama.cpp remains a concern.

hackernews · snehesht · Oct 4, 12:51 · [Discussion](https://news.ycombinator.com/item?id=49953495)

**Background**: Mixture-of-Experts (MoE) models activate only a subset of their parameters for each token, which allows them to have a very large total parameter count while keeping inference cost closer to that of a much smaller model. Quantization reduces the precision of model weights (for example to 4-bit or lower) so that large models fit into limited GPU memory, but more aggressive quantization can degrade output quality. Strata is an open-source inference engine specifically designed to run Qwen 3.8 Flash Next on consumer hardware, while llama.cpp is a widely used inference framework known for its quantization support and accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen / Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://github.com/qwenlm/qwen3.8-flash-next">GitHub - QwenLM/ Qwen 3 . 8 - Flash - Next : Qwen 3 . 8 - Flash - Next is the...</a></li>

</ul>
</details>

**Discussion**: Community reaction is mixed: some users are impressed by the speed and ease of setup, with one reporting 124 T/s on an RTX 4090 and another calling it game-changing on an R9700 32GB. However, a11r expressed skepticism about going below 4-bit quantization due to quality degradation, and Jackson__ provided a benchmark showing Strata's median error of 154.8 pixels versus 46.5 for llama.cpp on the same weights, tempering the enthusiasm.

**Tags**: `#LLM inference`, `#quantization`, `#consumer hardware`, `#Qwen`, `#performance benchmarking`

---

<a id="item-5"></a>
## [CedarDB ports original Doom to run entirely in SQL](https://cedardb.com/blog/sqldoom/) ⭐️ 8.0/10

CedarDB developers ported the original 1993 Doom's game logic and renderer entirely into SQL queries, running the game inside a database at around 35 FPS, with multiplayer deathmatch also working. The game logic amounts to roughly 5,900 lines of SQL, fewer than the vanilla C implementation. The project challenges common assumptions about SQL's limitations, showing that contemporary SQL engines are powerful enough to express complex stateful logic like a full game engine. It fuels debate about whether business rules and complex domain logic could similarly be implemented in SQL, potentially improving maintainability and concurrency in enterprise systems. The port abuses SQL query planning as a state machine and drives the game loop through a tic sequence inside the database engine; deathmatch works almost for free thanks to the data model. The developers also explored compiling SQL for better performance, though running a game in a database is inherently unconventional.

hackernews · Vaslo · Oct 3, 22:14 · [Discussion](https://news.ycombinator.com/item?id=49948300)

**Background**: Doom, released by id Software in 1993, is a landmark first-person shooter whose engine architecture (id Tech 1) separates game logic from rendering and uses WAD files to store assets. SQL is the standard language for querying relational databases, and modern engines support procedural extensions like PL/SQL and T-SQL that add loops and branching. Porting Doom to SQL means reimplementing its game loop, state updates, and rendering as database queries rather than conventional procedural code.

<details><summary>References</summary>
<ul>
<li><a href="https://cedardb.com/blog/sqldoom/">We ported the original Doom to SQL | CedarDB</a></li>
<li><a href="https://en.wikipedia.org/wiki/Id_Tech">id Tech - Wikipedia</a></li>
<li><a href="https://vldb.org/pvldb/vol14/p1378-ramachandra.pdf">Procedural Extensions of SQL</a></li>

</ul>
</details>

**Discussion**: Commenters were impressed but divided: some praised SQL's expressive power for complex logic and shared related projects like pg_shell and pg_gpt2, while others called it 'engineering malpractice' or noted practical pain points such as deadlocks and scaling issues when using SQL tables as the source of truth for game state. Overall sentiment was a mix of admiration for the technical feat and skepticism about its practical use.

**Tags**: `#SQL`, `#Doom`, `#game development`, `#database`, `#engineering`

---

<a id="item-6"></a>
## [Distilling Stockfish into a ResNet/ViT Model on 1B Positions, 3.9B Dataset Released](https://www.reddit.com/r/MachineLearning/comments/1wxz5qq/distilling_stockfish_on_a_billion_positions_full/) ⭐️ 8.0/10

A developer distilled the Stockfish chess engine's value function into a combined ResNet/ViT neural network trained on 1 billion positions from the Gigafish dataset, and publicly released the full 3.9 billion position dataset on Hugging Face. The dataset was built from positions drawn from 37 months of Lichess games. This demonstrates that a neural network can approximate Stockfish's depth-limited search value function faster than the engine itself, potentially offering a competitive alternative to NNUE. The public release of a 3.9 billion position dataset also provides a valuable resource for chess AI and knowledge distillation research. The author found that a pure vision transformer was slow to understand the board, while a CNN benefited early training due to its geometric inductive biases; combining both architectures yielded the best results. Holding search depth constant was crucial because the goal was to approximate the value function at a fixed depth-limited search.

reddit · r/MachineLearning · /u/microscope1024 · Oct 5, 04:11

**Background**: Stockfish is a free, open-source chess engine that has been among the strongest in the world for years, and since 2020 it has used an efficiently updatable neural network (NNUE) for evaluation. Knowledge distillation is a technique that transfers knowledge from a large model to a smaller one, often to make evaluation faster or deployable on weaker hardware. The Gigafish dataset is a large collection of chess positions derived from Lichess games, intended for training chess neural networks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stockfish_NNUE">Stockfish NNUE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation</a></li>
<li><a href="https://huggingface.co/datasets/lukesalamone/gigafish-3.8b-d10">lukesalamone/ gigafish -3.8b-d10 · Datasets at Hugging Face</a></li>

</ul>
</details>

**Tags**: `#chess`, `#knowledge-distillation`, `#deep-learning`, `#dataset`, `#stockfish`

---

<a id="item-7"></a>
## [Yandex Music's Sona transformer replaces 15+ component recommender pipeline](https://www.reddit.com/r/MachineLearning/comments/1wy4qxm/sona_one_transformer_replaced_our_15_candidate/) ⭐️ 8.0/10

Yandex Music introduced Sona, a single generative transformer that replaced its production recommender's 15+ candidate generators, pre-ranker, and ranker in an A/B test. In a 7-day test on smart speakers with 15% of users per arm, Sona achieved +4.53% Active Users and +6.30% Total Listening Time over the production control, both significant at p < 0.01. This demonstrates that a single end-to-end generative model can replace a complex multi-stage recommender cascade in a real production A/B test, potentially simplifying architecture and reducing engineering overhead. If validated in long-term tests, it could influence how large-scale recommender systems are designed across the industry. Sona reads up to 8,192 events using a History Compression technique that splits history into older 6,144 and recent 2,048 events, exchanging information via cross-attention and one full-history self-attention layer, roughly halving inference cost. Catalog coverage is lower than the production stack, which the team plans to investigate, and a long-term A/B test is underway.

reddit · r/MachineLearning · /u/SettingAccording8986 · Oct 5, 10:07

**Background**: Traditional production recommenders use a multi-stage cascade: candidate generators retrieve a subset of items from a large catalog, a pre-ranker filters them, and a heavy ranker scores the final list using hundreds of engineered features. This design exists because scoring millions of items per request within tens of milliseconds is infeasible with a single model. Recent advances in generative recommenders and efficient attention mechanisms have made single-model alternatives more practical.

<details><summary>References</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/10/05/yandex-introduces-sona-a-single-generative-recommender-that-replaces-entire-recommendation-cascade/">Yandex Introduces Sona: A Single Generative Recommender That...</a></li>
<li><a href="https://preptima.com/questions/machine-learning/recommenders-and-ranking/candidate-generation-then-ranking">Candidate Generation and Ranking | Recommenders — Preptima</a></li>

</ul>
</details>

**Tags**: `#recommender systems`, `#transformer`, `#efficient attention`, `#production ML`, `#A/B testing`

---

<a id="item-8"></a>
## [ARC-AGI-3 Kaggle scores jump from 7% to 56% in 30 days](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 8.0/10

Over the past 30 days, the top scores on the Kaggle ARC-AGI-3 leaderboard rose from roughly 7% to 56%, achieved by small local models running inside a harness, according to a Reddit post on r/MachineLearning. The poster notes the leaderboard graphic is slightly out of date and asks the community what to make of the rapid climb. ARC-AGI-3 is explicitly designed to measure human-like fluid intelligence and to show where humans still outperform machines, so a jump to 56% on a Kaggle track suggests benchmark-style reasoning tasks are being solved faster than expected. If small local models can reach this level, it raises questions about how much of the remaining gap reflects genuine reasoning versus harness engineering and benchmark-specific tuning. Kaggle rules for the ARC Prize 2026 ARC-AGI-3 track restrict participants to small local models, so the gains come from harness design and agent scaffolding rather than large frontier models. ARC-AGI-3 is an interactive benchmark where agents must explore novel environments, infer goals on the fly, and build adaptable world models without instructions, and each frame is encoded as 4096 ASCII characters with spatial rather than semantic meaning.

reddit · r/MachineLearning · /u/we_are_mammals · Oct 4, 10:24 · [Discussion](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arcαgi3_scores_on_kaggle_just_went_from_7_to/)

**Background**: ARC-AGI (Abstraction and Reasoning Corpus for Artificial General Intelligence) is a benchmark family created to test general reasoning ability rather than memorized knowledge. ARC-AGI-3 moves beyond static puzzle grids to interactive environments where an agent must act, observe, and learn continuously, similar to how a human would explore an unfamiliar game. The ARC Prize 2026 competition on Kaggle hosts this track with prize money and rules that push participants toward efficient, small-model solutions.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC - AGI - 3</a></li>

</ul>
</details>

**Discussion**: The Reddit post is brief and the provided content does not include actual comment text, but the framing invites debate over whether small local models in a harness are genuinely beating average humans on a benchmark designed to show human superiority, or whether the result reflects benchmark-specific optimization.

**Tags**: `#ARC-AGI`, `#benchmark`, `#AI`, `#machine learning`, `#Kaggle`

---

<a id="item-9"></a>
## [SK Telecom Apologizes for Massive Data Breach, Offers Free USIM Replacements](https://t.me/zaihuapd/44206) ⭐️ 8.0/10

SK Telecom (SKT), South Korea's largest telecom operator, confirmed that its internal HSS server was hacked, exposing sensitive data of over 25 million users, including IMEI, SN, ICCID, PIN2/PUK2, eID, encryption K values, and private keys. The CEO publicly apologized and announced free USIM card replacements for all SKT users (including MVNO users on its network, with some device exceptions), and will reimburse those who recently paid for replacements. This is one of the largest telecom data breaches in recent years, affecting over 25 million people and exposing critical authentication credentials that could enable SIM cloning or identity theft. The incident highlights the vulnerability of core telecom infrastructure and sets a precedent for industry-wide incident response, potentially pressuring other carriers to reassess their security measures. The compromised HSS server stored authentication keys (K values) and private keys used to secure subscriber identity, which are critical for preventing unauthorized access. The free USIM replacement aims to mitigate risks by issuing new cards with fresh credentials, but some devices (e.g., certain IoT or older models) may not be eligible, and users may still face residual risks if other data like IMEI is misused.

telegram · zaihuapd · Oct 4, 09:02

**Background**: A Home Subscriber Server (HSS) is a central database in 4G/5G networks that manages subscriber profiles, authentication, and security keys. A USIM card is a universal subscriber identity module used in 3G/4G/5G devices to securely store the international mobile subscriber identity (IMSI) and related keys for network authentication. The breach of an HSS server is particularly severe because it can compromise the root of trust for mobile communications, enabling attackers to impersonate users or intercept calls and data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.p1sec.com/blog/home-subscriber-server-hss">Home Subscriber Server ( HSS ): The Backbone of Modern Telecom ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/USIM_(card)">USIM (card)</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#data breach`, `#telecom`, `#privacy`, `#incident response`

---

<a id="item-10"></a>
## [Google Releases VeriHarness Self-Verification Framework for Long-Horizon Tasks](https://arxiv.org/abs/2610.00972v1) ⭐️ 8.0/10

Google Research released VeriHarness, an agentic verification framework that uses the same model that generated candidate outputs to verify them by checking disputed claims against environment evidence and actively challenging consensus claims, then selecting, revising, or rebuilding the final result. It achieved the highest selection scores across five long-horizon benchmarks and two models, and after evidence-driven revision improved Gemini 3.5 Flash by an average of 6.2 points and Claude Opus 4.8 by 6.4 points over single-pass generation, while releasing roughly 26,000 rollouts. This is a training-free, plug-and-play verification harness that improves long-horizon LLM agent performance without reference answers or grading rubrics, which could make agentic AI more reliable in real-world multi-step tasks where ground-truth labels are unavailable. The release of 26,000 rollouts also provides a valuable public dataset for studying agent verification and evaluation. VeriHarness is described as the first agentic verification harness for long-horizon tasks, and it is training-free and plug-and-play across benchmarks and models, relying on disagreement resolution, consensus challenging, and evidence-backed revision rather than external graders. The reported gains are measured against single-pass generation on five long-horizon benchmarks with two models, and the framework's code is available in the google-research/veriharness GitHub repository.

telegram · zaihuapd · Oct 4, 13:32

**Background**: Long-horizon tasks require an AI agent to make many decisions over an extended sequence of steps, and they cannot be completed reliably by a single prompt or short exchange. Because pure generation tends to drift over long dependency chains, verification before or during execution is increasingly seen as a way to keep agents honest. Rollouts are the sampled generation trajectories an LLM produces during training or evaluation, and releasing them lets researchers analyze agent behavior systematically.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2610.00972">VeriHarness : Scaling Agentic Verification for Long-Horizon Tasks</a></li>
<li><a href="https://huggingface.co/papers/2610.00972">Paper page - VeriHarness : Scaling Agentic Verification for...</a></li>
<li><a href="https://github.com/google-research/veriharness/issues">Issues · google -research/ veriharness · GitHub</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#verification`, `#long-horizon tasks`, `#Google`, `#benchmark`

---

<a id="item-11"></a>
## [Huawei and Qualcomm Sign Broad Multi-Year Patent Deal Covering 5G and AI](https://www.huawei.com/en/news/2026/10/qualcomm-broad-patent-agreement) ⭐️ 8.0/10

Huawei and Qualcomm announced a multi-year, broad patent cross-licensing agreement covering 5G, computing, AI, and networking, under which Qualcomm will also purchase some of Huawei's U.S. patents and license Huawei's logic-folding chip manufacturing technology. The deal, subject to regulatory approval, is expected to bring Huawei's cumulative patent licensing contract value to over $6.9 billion. This is the first licensing deal between the two companies to include 5G technology, signaling a significant shift in the global tech industry landscape and potentially easing long-standing patent tensions between Huawei and major U.S. chipmakers. It also strengthens Huawei's IP monetization strategy, which has generated positive revenue since 2021. The agreement covers cross-licenses to both companies' patent portfolios across 5G, compute, AI, and networking, and includes Qualcomm acquiring certain Huawei U.S. patents as well as a license to Huawei's logic-folding chip manufacturing technology. The transaction is subject to necessary regulatory approvals before it can be completed.

telegram · zaihuapd · Oct 5, 06:45

**Background**: Patent cross-licensing agreements allow companies to use each other's patented technologies without risking infringement lawsuits, often creating synergies and reducing litigation costs. Huawei has been actively monetizing its patent portfolio, and this deal with Qualcomm—a major U.S. chip designer—marks a notable expansion of its licensing reach into 5G and AI. Logic-folding chip manufacturing is a Huawei technology that restructures circuit topology within a single chip's logic layer, distinct from advanced packaging or 3D stacking approaches.

<details><summary>References</summary>
<ul>
<li><a href="https://en.shiftdelete.net/huawei-and-qualcomm-sign-landmark-5g-patent-licensing-agreement/">Huawei and Qualcomm Sign Landmark 5 G Patent Licensing Agreement</a></li>
<li><a href="https://www.techzine.eu/news/infrastructure/144742/huawei-and-qualcomm-sign-broad-patent-agreement/">Huawei and Qualcomm sign broad patent agreement - Techzine Global</a></li>
<li><a href="https://www.ithome.com/1/009/852.htm">高通与华为达成 逻 辑 折 叠 芯 片 技 术 相关专利授权，韬定律加速出海 - IT...</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#Qualcomm`, `#patent-licensing`, `#5G`, `#AI`

---

<a id="item-12"></a>
## [Quad9 Refuses French DNS Blocking Order, Faces €580K Daily Fine](https://torrentfreak.com/dns-resolver-quad9-rejects-french-piracy-blocks-weighs-exit-as-bein-seeks-up-to-e580k-a-day/) ⭐️ 8.0/10

Swiss non-profit DNS resolver Quad9 has refused to comply with a French court order requiring it to block 58 piracy-related domains, with beIN Sports seeking fines of €10,000 per domain per day — up to €580,000 daily. A Paris court heard the case last Thursday and is expected to rule within three weeks. This case highlights the growing conflict between DNS providers and state-mandated censorship, and could set a global precedent for how DNS resolvers handle jurisdiction-specific blocking demands. Quad9's principled stance may influence other privacy-focused DNS operators and shape the future of internet governance and digital rights. Quad9 states it has never blocked any domain and, because it does not collect user data, cannot target only French users — leaving it with the choice of either global blocking or exiting the French market. It also criticized France's July law allowing real-time automatic blacklisting of domains as 'reckless and dangerous'.

telegram · zaihuapd · Oct 5, 08:05

**Background**: Quad9 is a Swiss non-profit DNS resolver whose founding charter prioritizes privacy, meaning it does not log users' IP addresses. DNS resolvers translate human-readable domain names into IP addresses, and blocking at the DNS level is a common method for enforcing copyright-related site blocks. France has increasingly pushed for automated, real-time domain blacklisting to combat piracy, particularly of live sports streams.

<details><summary>References</summary>
<ul>
<li><a href="https://quad9.net/">Quad 9 | A public and free DNS service for a better security and privacy</a></li>

</ul>
</details>

**Tags**: `#DNS`, `#Internet Censorship`, `#Privacy`, `#Digital Rights`, `#France`

---