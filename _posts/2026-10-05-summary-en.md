---
layout: default
title: "Horizon Summary: 2026-10-05 (EN)"
date: 2026-10-05
lang: en
---

> From 65 items, 11 important content pieces were selected

---

1. [2026 Nobel Prize in Physiology or Medicine Awarded for Optogenetics](#item-1) ⭐️ 9.0/10
2. [vLLM v0.31.0 ships DeepSeek-V4.1-Flash optimizations and fast-restart weight cache](#item-2) ⭐️ 8.0/10
3. [Reflection releases Beam, a 501B open-weight MoE model](#item-3) ⭐️ 8.0/10
4. [Anthropic reported a Florida woman's Claude diary to police, sparking felony charge](#item-4) ⭐️ 8.0/10
5. [Qualcomm licenses Huawei's LogicFolding chip patents in landmark deal](#item-5) ⭐️ 8.0/10
6. [Existing Tech Could Eradicate Mosquito-Borne Diseases, Article Argues](#item-6) ⭐️ 8.0/10
7. [OpenAI to Watermark ChatGPT and Codex Text in the EU](#item-7) ⭐️ 8.0/10
8. [Distilling Stockfish into a Neural Net on 1B Positions, 3.9B Dataset Released](#item-8) ⭐️ 8.0/10
9. [Yandex Music's Sona replaces 15+ recommender components with one transformer](#item-9) ⭐️ 8.0/10
10. [ARC-AGI-3 Kaggle Scores Jump from 7% to 56% in 30 Days](#item-10) ⭐️ 8.0/10
11. [Quad9 Refuses French DNS Blocking Order, Faces €580K Daily Fine](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [2026 Nobel Prize in Physiology or Medicine Awarded for Optogenetics](https://www.nobelprize.org/all-nobel-prizes-2026/) ⭐️ 9.0/10

The 2026 Nobel Prize in Physiology or Medicine was awarded to Karl Deisseroth, Peter Hegemann, and Georg Nagel for their discovery of light-controlled ion channels and the development of optogenetics. This technique allows researchers to turn individual neurons on or off in living brains and is now used in laboratories worldwide for brain research. Optogenetics represents a paradigm shift in neuroscience, giving researchers unprecedented precision to control specific neurons and study how neural circuits drive behavior, learning, memory, and disease. Its recognition with a Nobel Prize underscores the broad impact of this tool, which has already moved toward clinical applications such as partial vision restoration in a blind patient. Optogenetics works by expressing light-sensitive ion channels, pumps, or enzymes in target cells, allowing light to precisely control biochemical signaling and neuronal activity. Beyond controlling individual cells, the technique has been used to map functional brain connectivity and to study behaviors such as decision making, fear memory, addiction, and feeding.

telegram · zaihuapd · Oct 5, 09:33

**Background**: Optogenetics is a biological technique that uses light to manipulate the activity of neurons or other cell types. It relies on light-sensitive proteins, such as ion channels and pumps, that are genetically introduced into target cells; when light shines on these cells, the proteins change the flow of ions across the cell membrane, activating or silencing the cell. This method has become a foundational tool in systems neuroscience, enabling researchers to establish causal links between specific neural activity and behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Optogenetics">Optogenetics</a></li>
<li><a href="https://en.wikipedia.org/wiki/Karl_Deisseroth">Karl Deisseroth - Wikipedia</a></li>
<li><a href="https://www.downtoearth.org.in/health/2026-medicine-nobel-awarded-for-discoveries-concerning-light-gated-ion-channels-and-optogenetics">2026 Medicine Nobel Prize Honors Pioneers of Optogenetics and...</a></li>

</ul>
</details>

**Tags**: `#optogenetics`, `#neuroscience`, `#Nobel Prize`, `#brain research`, `#light-controlled ion channels`

---

<a id="item-2"></a>
## [vLLM v0.31.0 ships DeepSeek-V4.1-Flash optimizations and fast-restart weight cache](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) ⭐️ 8.0/10

vLLM released v0.31.0, a large update with 717 commits from 307 contributors (96 new) that delivers major DeepSeek-V4.1-Flash inference optimizations such as FlashMLA mega attention with NVFP4 compressed KV cache, DeepGEMM sparse MQA logits, and fused decoder-boundary kernels. It also introduces a new `vllm preload` CLI that launches a weight-cache daemon keeping post-quantized weights resident in GPU memory across engine restarts, plus experimental CRIU-based engine snapshots. vLLM is one of the most widely used open-source high-throughput LLM inference and serving engines, so these optimizations directly affect how efficiently and cheaply teams can serve large models like DeepSeek-V4.1-Flash. The fast-restart weight cache and snapshot features could substantially cut cold-start and restart times in production deployments, which matters for autoscaling and reliability. The release includes several breaking changes: per-request multimodal kwargs are now gated behind `--trust-request-mm-kwargs`, `tokenizer_mode="slow"` was removed, `--enable-mamba-fine-grained-prefix-cache` was renamed to `--enable-mamba-shared-prefix-checkpoint`, and online quantization via `quantization="fp8"` was replaced by the `fp8_per_tensor` shorthand. It also adds scheduling controls like `--max-num-active-seqs` and `--long-prefill-token-threshold`, plus security fixes for prefix-cache key collisions and stale multimodal cache entries.

github · khluu · Oct 5, 06:44

**Background**: vLLM is an open-source framework for inference and serving of large language models, originally developed at UC Berkeley's Sky Computing Lab and built around PagedAttention, a memory-management method for transformer key-value caches. It supports continuous batching, distributed inference, quantization, and OpenAI-compatible APIs, making it a common choice for production LLM serving. DeepSeek-V4.1-Flash is a recent DeepSeek model trained from scratch on a 45T-token multimodal corpus with sparse attention and context extended to 1M tokens, and FlashMLA is DeepSeek's library of optimized attention kernels.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLLM">VLLM</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek-V4.1-Flash">DeepSeek-V4.1-Flash</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/ FlashMLA : FlashMLA : Efficient Multi-head...</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#model serving`, `#performance optimization`, `#release`

---

<a id="item-3"></a>
## [Reflection releases Beam, a 501B open-weight MoE model](https://reflection.ai/blog/introducing-beam) ⭐️ 8.0/10

Reflection has released Beam, an open-weight sparse Mixture-of-Experts model with 501 billion total parameters and 23 billion active parameters, targeting coding, reasoning, and agentic workloads. The model was pretrained on 23.8 trillion curated tokens and further tuned with reinforcement learning, with Reflection claiming it matches or outperforms similar-sized open base models. Beam adds another large open-weight contender to a field increasingly dominated by Chinese labs, and its release fuels debate about whether Western open models are keeping pace. For developers and researchers, it offers a new high-capacity option for coding and agentic use cases that can be self-hosted and inspected. Beam uses a sparse MoE design where only 23B of the 501B parameters are active per token, and it was trained on 28T tokens according to community comparisons. Community member wren6991 contrasted it with DeepSeek V4.1 Flash, noting Beam has more active parameters (23B vs 8B prefill/16B decode) but fewer pretraining tokens (28T vs 45T) and no N-gram/PLE parameters.

hackernews · Philpax · Oct 5, 19:16 · [Discussion](https://news.ycombinator.com/item?id=49969183)

**Background**: Mixture-of-Experts (MoE) is an architecture that splits a model into many specialized sub-networks (experts) and uses a router to activate only a few per input, so total parameters can be huge while active parameters—and thus compute per token—stay small. Open-weight models release their trained parameters for anyone to download and run, unlike closed API-only models. Beam's 501B/23B split places it in the same weight class as other frontier open MoE models such as DeepSeek's.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://berges.ai/concepts/mixture-of-experts">What is a mixture-of-experts (MoE) model? Total vs active parameters</a></li>
<li><a href="https://vettedconsumer.com/mixture-of-experts-moe-explained-why-active-parameters-decide-what-runs-on-your-machine/">Mixture-of-Experts (MoE), Explained: Why “ Active Parameters ”...</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed another open-weight release but were skeptical of Reflection's generalization claims, with Ariarule noting a demo citing 95.5% coverage on a recent viral puzzle. wren6991 provided a detailed spec comparison against DeepSeek V4.1 Flash, while NorwegianDude argued Western open models still lag smaller free Chinese models and hoped for more competition and providers like Google's Gemma.

**Tags**: `#open-weight models`, `#Mixture-of-Experts`, `#large language models`, `#AI research`, `#model release`

---

<a id="item-4"></a>
## [Anthropic reported a Florida woman's Claude diary to police, sparking felony charge](https://www.techspot.com/news/114091-florida-woman-used-claude-diary-anthropic-reported-shoot.html) ⭐️ 8.0/10

A Florida woman was charged with a second-degree felony under Florida Statute 836.10 after Anthropic reported a diary entry she wrote using its Claude chatbot that contained threats of violence. The case, reported by TechSpot and Cybernews, marks one of the first known instances of an AI company proactively sharing user conversations with law enforcement. The case raises major legal and ethical questions about AI surveillance, user privacy, and free speech, and could set a precedent for how AI companies handle potentially threatening content. It affects every user of AI chatbots, as it shows that private-seeming conversations may be monitored and reported to authorities. Florida Statute 836.10 makes it a second-degree felony to send, post, or transmit a written or electronic record threatening to kill or injure someone, carry out a mass shooting, or commit terrorism, and the communication must be made in a manner in which another person may view it. The woman told authorities she used Claude as a diary, and the case highlights that AI chatbot conversations may be reviewed and shared with police for serious threats.

hackernews · emptybits · Oct 5, 05:37 · [Discussion](https://news.ycombinator.com/item?id=49961057)

**Background**: Anthropic is an AI safety and research company that develops the Claude chatbot using Constitutional AI to make it safe, accurate, and secure. Like other AI chat services, Claude collects user data and may filter or moderate content, though the exact monitoring and reporting policies are not always transparent. This incident follows similar debates about whether AI companies should report users who express violent intentions, with some critics arguing it amounts to surveillance.

<details><summary>References</summary>
<ul>
<li><a href="https://cybernews.com/ai-news/claude-diary-police/">Claude diary threat : Florida woman reported to police | Cybernews</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>
<li><a href="https://claude.com/">Claude</a></li>

</ul>
</details>

**Discussion**: Commenters are deeply divided: some argue that reading a private diary entry and charging the author is unconstitutional surveillance, while others sympathize with Anthropic, noting that failing to report a potential shooter would also draw criticism. Many question whether a diary entry to a chatbot legally constitutes a transmitted threat under Florida law, and some suggest running local open-source models to avoid corporate monitoring.

**Tags**: `#AI ethics`, `#privacy`, `#surveillance`, `#free speech`, `#legal`

---

<a id="item-5"></a>
## [Qualcomm licenses Huawei's LogicFolding chip patents in landmark deal](https://www.bloomberg.com/news/articles/2026-10-05/qualcomm-licenses-patents-on-huawei-s-logicfolding-chip-tech) ⭐️ 8.0/10

On October 5, 2026, Huawei and Qualcomm announced a multi-year, broad patent cross-license agreement covering 5G, computing, AI, and networking, under which Qualcomm also licensed patents related to Huawei's LogicFolding chip manufacturing technology and agreed to purchase certain Huawei U.S. patents. Huawei said the deal's cumulative expected contract value for its licensing business exceeds $6.9 billion, pending regulatory approval. This marks a notable reversal in semiconductor IP dynamics, with Huawei shifting from a net licensee of Western technology to a provider whose chipmaking IP is licensed by a major U.S. chipmaker. It could reshape patent bargaining power across 5G and AI and carries significant geopolitical implications given Huawei's presence on the U.S. Entity List. Huawei claims LogicFolding improves chip performance and helps narrow the gap with leading foundries such as TSMC, targeting 1.4nm-class density by 2031 without EUV, though 3D stacking itself is not new and the deal still requires regulatory approval. Qualcomm is purchasing certain Huawei U.S. patents as part of the arrangement.

hackernews · 0xedb · Oct 5, 07:46 · [Discussion](https://news.ycombinator.com/item?id=49961861)

**Background**: LogicFolding is Huawei's chip technology that stacks multiple wafer layers so signals travel shorter distances in layer space rather than across a single chip, which Huawei says reduces overall heat. The deal is a cross-license, meaning both companies gain access to each other's patent portfolios, and it comes as Huawei's IP licensing business has generated positive revenue since 2021. Huawei remains on the U.S. Entity List, which restricts U.S. firms from certain dealings with it, making the regulatory path for this agreement notable.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tipranks.com/news/qualcomm-stock-rises-after-huawei-logicfolding-chip-deal">Qualcomm Stock Rises after Huawei LogicFolding Chip Deal</a></li>
<li><a href="https://www.buildmvpfast.com/blog/huawei-logicfolding-tau-scaling-chip-breakthrough-2026">Huawei LogicFolding Tau Scaling Chip Breakthrough 2026</a></li>
<li><a href="https://moorinsightsstrategy.com/field-notes/huawei-qualcomms-historic-cross-license-agreement/">Huawei & Qualcomm ’s Historic Cross - License Agreement</a></li>

</ul>
</details>

**Discussion**: Commenters debated whether Huawei is now earning net revenue from Qualcomm, a reversal from its past role as a technology buyer, while others questioned how Qualcomm can strike such a deal given Huawei's Entity List status. Some praised LogicFolding as an obvious-in-hindsight innovation that reduces heat, and others wondered how Ericsson might respond or lamented the shift in the 5G leadership race.

**Tags**: `#semiconductors`, `#patents`, `#Huawei`, `#Qualcomm`, `#geopolitics`

---

<a id="item-6"></a>
## [Existing Tech Could Eradicate Mosquito-Borne Diseases, Article Argues](https://worksinprogress.co/issue/mosquitoes-are-a-choice/) ⭐️ 8.0/10

A Works in Progress article argues that the technology to eradicate mosquito-borne diseases such as dengue and malaria already exists, and that failing to deploy it is a deliberate choice costing millions of lives each year. The piece highlights tools like gene drives and Wolbachia-based methods that are ready for wider use. Mosquito-borne diseases kill hundreds of thousands of people annually, mostly in tropical regions, so wider deployment of these technologies could save millions of lives and reduce immense economic burdens. The debate also raises ethical and regulatory questions about deliberately altering wild insect populations. The article points to gene drives, which use CRISPR to spread anti-parasite genes through mosquito populations, and Wolbachia bacteria, which reduce mosquitoes' ability to transmit viruses like dengue. Trials such as Singapore's Wolbachia AlbB strain have shown a 72% reduction in dengue risk, though regulatory and ecological concerns remain.

hackernews · benbreen · Oct 4, 18:06 · [Discussion](https://news.ycombinator.com/item?id=49956290)

**Background**: Gene drives are genetic systems that ensure a particular trait is inherited by nearly all offspring, allowing a modification to spread rapidly through a wild population. Wolbachia is a common bacterium that, when introduced into mosquitoes, blocks them from transmitting viruses such as dengue. Both approaches aim to suppress or modify mosquito populations rather than relying solely on insecticides and nets.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geneconvenevi.org/articles/mosquito-gene-drives-and-the-malaria-eradication-agenda/">Mosquito Gene Drives and the Malaria Eradication Agenda</a></li>
<li><a href="https://www.worldmosquitoprogram.org/en/work/wolbachia-method/how-it-works">How WMP's Wolbachia method works | World Mosquito Program</a></li>
<li><a href="https://www.ocacademy.in/blogs/wolbachia-mosquito-dengue-control-singapore-trial/">Wolbachia mosquito dengue control : A 72% risk reduction</a></li>

</ul>
</details>

**Discussion**: Commenters were largely supportive, with one noting that dengue is 'no joke' and another arguing there is 'no good reason not to' deploy the technology. Some raised practical questions about DIY use in endemic areas, while others compared the situation to tuberculosis, where a cure exists but human choices still allow the disease to persist.

**Tags**: `#public health`, `#biotechnology`, `#genetic engineering`, `#mosquito-borne diseases`, `#global health`

---

<a id="item-7"></a>
## [OpenAI to Watermark ChatGPT and Codex Text in the EU](https://techcrunch.com/2026/10/05/openai-will-start-watermarking-chatgpts-text-in-the-eu/) ⭐️ 8.0/10

OpenAI announced it will add machine-readable invisible watermarks to qualifying ChatGPT and Codex text outputs in the EU over the coming weeks to comply with the AI Act's content transparency requirements. API users can optionally enable watermarking for some models, though it is off by default, and OpenAI is opening its text watermark detector to researchers and professional organizations. This is one of the first concrete implementations of the EU AI Act's transparency obligations by a major AI provider, and it could set a de facto standard for how AI-generated text is marked and detected across the industry. It affects EU users, developers building on OpenAI's API, enterprises relying on AI-generated content, and regulators seeking enforceable provenance mechanisms. OpenAI notes that editing the text can make the invisible marks harder to detect, echoing known limitations of text watermarking, such as reduced detector confidence after rewriting or translation. The watermarking applies only to qualifying outputs in the EU, and API watermarking is opt-in rather than enabled by default.

rss · TechCrunch AI · Oct 5, 20:36

**Background**: The EU AI Act's Article 50 requires providers of certain AI systems to make AI-generated or manipulated content detectable through machine-readable marking, so that synthetic content can be identified as such. Text watermarking works by embedding hidden, statistically detectable patterns into LLM-generated text, which a detector can later recognize. OpenAI's Codex is its coding agent that helps developers with tasks like bug fixing and refactoring, so watermarking it extends the transparency requirement beyond chat to code generation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.resemble.ai/resources/complete-guide-to-eu-ai-act-watermarking-requirements-for-generative-ai">Complete Guide to EU AI Act Watermarking Requirements for...</a></li>
<li><a href="https://vryse.co/blog/claude-ai-watermarking">Claude AI Watermarking : EU AI Act & Content Rules Explained</a></li>
<li><a href="https://ai.google.dev/responsible/docs/safeguards/synthid">SynthID: Tools for watermarking and detecting LLM- generated Text</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI Act`, `#watermarking`, `#AI regulation`, `#content provenance`

---

<a id="item-8"></a>
## [Distilling Stockfish into a Neural Net on 1B Positions, 3.9B Dataset Released](https://www.reddit.com/r/MachineLearning/comments/1wxz5qq/distilling_stockfish_on_a_billion_positions_full/) ⭐️ 8.0/10

A developer distilled Stockfish's value function into a combined ResNet/ViT model using 1 billion positions from the Gigafish dataset, and released the full 3.9 billion position dataset on Hugging Face. The dataset is built from 37 months of Lichess games, and the project specifically holds search depth constant to approximate depth-limited search with a neural network. This work explores whether a learned function can approximate Stockfish's depth-limited search faster than the engine itself, potentially offering a competitive alternative to NNUE. The public 3.9B dataset also gives the chess AI community a large, ready-to-use resource for training and benchmarking evaluation models. The author found that a pure vision transformer was very slow to understand the board, while a CNN benefited early in training from its geometric inductive biases; combining the two architectures gave the best results. Holding search depth constant was a deliberate design choice to make the distilled value function approximate the full search tree underneath each position.

reddit · r/MachineLearning · /u/microscope1024 · Oct 5, 04:11

**Background**: Stockfish is a top open-source chess engine that evaluates positions and picks moves, and since adopting NNUE (an efficiently updatable neural network) it has used a small neural net for evaluation. Knowledge distillation transfers knowledge from a large or strong model (the teacher) to a smaller model (the student), and here Stockfish acts as the teacher. ResNets are convolutional networks with strong spatial inductive biases, while vision transformers process images as patch sequences and must learn spatial structure from data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Efficiently_updatable_neural_network">Efficiently updatable neural network - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://genmind.ch/posts/ResNet-vs-ViT-Benchmark-Reality-Check/">I Benchmarked ResNet vs ViT on 50K Images. They're Nearly Identical.</a></li>

</ul>
</details>

**Tags**: `#chess`, `#distillation`, `#neural-networks`, `#dataset`, `#stockfish`

---

<a id="item-9"></a>
## [Yandex Music's Sona replaces 15+ recommender components with one transformer](https://www.reddit.com/r/MachineLearning/comments/1wy4qxm/sona_one_transformer_replaced_our_15_candidate/) ⭐️ 8.0/10

Yandex Music introduced Sona, a single generative transformer that replaced over 15 candidate generators, a pre-ranker, and a ranker in a production A/B test on smart speakers, delivering +4.53% Active Users and +6.30% Total Listening Time over the control (p < 0.01). The model uses a History Compression technique that splits up to 8,192 events into 6,144 older and 2,048 recent events, roughly halving inference cost while retaining most of the quality of full attention. This is a rare production-validated demonstration that a single end-to-end generative recommender can replace a complex multi-stage cascade, potentially simplifying recommender architectures across the industry. If the approach generalizes, it could reduce engineering overhead and inference costs for large-scale recommendation systems. Sona reads up to 8,192 events, with the older 6,144 and recent 2,048 blocks exchanging information via cross-attention and one full-history self-attention layer, after which a 7-layer stack runs only on the recent 2,048. The decoder and Ranking Module share the same encoder output so the encoder runs once per request, but catalog coverage is lower than the production stack and the model has not yet shipped to full traffic.

reddit · r/MachineLearning · /u/SettingAccording8986 · Oct 5, 10:07

**Background**: Traditional production recommenders use a multi-stage cascade: many candidate generators retrieve items, a pre-ranker filters them, and a heavy ranker scores the survivors using hundreds of engineered features. Transformers, originally built for sequences, have recently been adapted into generative recommenders that can produce recommendations end-to-end, but full attention over long user histories is computationally expensive because its cost grows quadratically with sequence length. History Compression is a practical attention-efficiency technique that keeps older events visible while limiting expensive full attention to a shorter recent window.

<details><summary>References</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/10/05/yandex-introduces-sona-a-single-generative-recommender-that-replaces-entire-recommendation-cascade/">Yandex Introduces Sona: A Single Generative Recommender That...</a></li>
<li><a href="https://www.deeplearning.ai/the-batch/more-efficient-transformers">BigBird is an Efficient Attention Mechanism for Transformers</a></li>
<li><a href="https://mbrenndoerfer.com/writing/quadratic-attention-bottleneck-transformers-long-sequences">Quadratic Attention Bottleneck - Interactive</a></li>

</ul>
</details>

**Tags**: `#recommender systems`, `#transformer`, `#efficient attention`, `#production ML`, `#A/B testing`

---

<a id="item-10"></a>
## [ARC-AGI-3 Kaggle Scores Jump from 7% to 56% in 30 Days](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 8.0/10

Over the past 30 days, top scores on the ARC-AGI-3 Kaggle competition surged from roughly 7% to 56%, achieved by small local models running inside custom harnesses under strict competition compute constraints. This means these compact, locally-runnable systems are now outperforming average humans on a benchmark explicitly designed to demonstrate human superiority. ARC-AGI-3 was built as a hard test of fluid, human-like reasoning, so a rapid jump from near-zero to above-average-human performance signals that interactive reasoning benchmarks may be saturating faster than expected. This could reshape how the AI community measures progress toward AGI and raise questions about whether current benchmarks still meaningfully separate human and machine intelligence. Kaggle competitors are restricted to smallish local models, so the 56% figure reflects efficiency under tight compute budgets rather than raw scale. The reported leaderboard graphic is noted as slightly out-of-date, and ARC-AGI-3 scores are known to swing widely depending on the harness wrapped around a model, meaning harness engineering is a major factor in these gains.

reddit · r/MachineLearning · /u/we_are_mammals · Oct 4, 10:24 · [Discussion](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arcαgi3_scores_on_kaggle_just_went_from_7_to/)

**Background**: ARC-AGI-3 is an interactive reasoning benchmark from the ARC Prize that challenges AI agents to explore novel environments, infer goals on the fly, build adaptable world models, and learn continuously through action-response loops. Unlike static puzzle benchmarks, it has no instructions and requires agents to figure out rules and objectives from observation alone, with a 100% score meaning an agent can beat every game as efficiently as a human. The Kaggle competition is a systems-track challenge where participants must submit efficient, purpose-built methods under strict compute constraints, and a $2M prize pool is attached to the broader ARC Prize effort.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC - AGI - 3</a></li>
<li><a href="https://arcprize.org/leaderboard">ARC Prize - Leaderboard</a></li>
<li><a href="https://www.mindstudio.ai/blog/gpt6-astra-benchmarks-agi-claims">GPT-6 Astra Benchmarks : Do the Numbers Actually Mean AGI ?</a></li>

</ul>
</details>

**Tags**: `#ARC-AGI`, `#AI benchmarks`, `#Kaggle`, `#AGI`, `#machine learning`

---

<a id="item-11"></a>
## [Quad9 Refuses French DNS Blocking Order, Faces €580K Daily Fine](https://torrentfreak.com/dns-resolver-quad9-rejects-french-piracy-blocks-weighs-exit-as-bein-seeks-up-to-e580k-a-day/) ⭐️ 8.0/10

Swiss non-profit DNS provider Quad9 has refused to comply with a French court order requiring it to block 58 piracy-linked domains, and beIN Sports is seeking fines of up to €580,000 per day (€10,000 per domain). A Paris court heard the case last Thursday, with a ruling expected within three weeks. This case could set a global precedent for how state-mandated DNS blocking applies to privacy-focused resolvers, potentially forcing Quad9 to exit France or block domains worldwide. It highlights the growing tension between national copyright enforcement and the borderless, privacy-centric architecture of public DNS services. Quad9 says it has never blocked any domain and, because it does not collect user data, it cannot geo-target blocks to French users only — leaving it with the choice of global blocking or exiting France. It also criticized France's July law allowing automated real-time domain blacklisting as 'reckless and dangerous.'

telegram · zaihuapd · Oct 5, 08:05

**Background**: DNS resolvers like Quad9 translate human-readable domain names into IP addresses, and blocking at this level is a common anti-piracy tool. Quad9 is a Swiss non-profit that emphasizes privacy by not logging user queries, which makes selective, jurisdiction-specific blocking technically difficult. France has recently expanded its piracy-blocking regime, including a July law enabling automated, real-time blocking of pirate sports streams.

<details><summary>References</summary>
<ul>
<li><a href="https://torrentfreak.com/dns-resolver-quad9-rejects-french-piracy-blocks-weighs-exit-as-bein-seeks-up-to-e580k-a-day/">DNS Resolver Quad9 Rejects French Piracy Blocks ... * TorrentFreak</a></li>
<li><a href="https://quad9.net/">Quad9 | A public and free DNS service for a better security and privacy</a></li>
<li><a href="https://torrentfreak.com/wrong-logo-no-piracy-proof-french-court-rejects-dns-piracy-blocking-bids-250515/">Wrong Logo, No Piracy Proof: French Court Rejects DNS Piracy...</a></li>

</ul>
</details>

**Tags**: `#DNS`, `#Internet Censorship`, `#Privacy`, `#Digital Rights`, `#France`

---