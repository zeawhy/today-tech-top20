---
layout: default
title: "Horizon Summary: 2026-07-11 (EN)"
date: 2026-07-11
lang: en
---

> From 38 items, 10 important content pieces were selected

---

1. [GPT-5.6 Sol Ultra Claims Proof of Cycle Double Cover Conjecture](#item-1) ⭐️ 10.0/10
2. [China's Long March 10B achieves world's first net-based rocket recovery at sea](#item-2) ⭐️ 9.0/10
3. [SGLang v0.5.15 Boosts GLM-5.2 on Blackwell GPUs](#item-3) ⭐️ 8.0/10
4. [Apple sues OpenAI over trade secret theft](#item-4) ⭐️ 8.0/10
5. [Chinese Courts Rule Game Accounts Inheritable, Platform Bans Invalid](#item-5) ⭐️ 8.0/10
6. [Tencent in Talks to Acquire AI Startup Manus from Meta](#item-6) ⭐️ 8.0/10
7. [OpenAI, Google reportedly provided AI models to blacklisted Chinese firms via Singapore](#item-7) ⭐️ 8.0/10
8. [China Imposes Temporary Ban on Helium Exports](#item-8) ⭐️ 8.0/10
9. [Meta Faces $12 Billion EU Fine Over Addictive Design](#item-9) ⭐️ 8.0/10
10. [SpaceXAI and Cursor Launch Grok 4.5 for Coding, Legal, Finance](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GPT-5.6 Sol Ultra Claims Proof of Cycle Double Cover Conjecture](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf) ⭐️ 10.0/10

OpenAI's GPT-5.6 Sol Ultra model has produced a purported proof of the Cycle Double Cover Conjecture, a major open problem in graph theory, released as a preprint on July 10, 2026. If verified, this would mark the first time an AI has autonomously proven a long-standing mathematical conjecture, representing a paradigm shift in both AI capabilities and mathematical research. The proof is extremely concise, suggesting a clever trick that experts may have missed, and the prompt included extensive instructions to avoid vague optimism and to actually solve the problem.

hackernews · scrlk · Jul 10, 18:29 · [Discussion](https://news.ycombinator.com/item?id=48863490)

**Background**: The Cycle Double Cover Conjecture, posed by Tutte, Itai, Rodeh, Szekeres, and Seymour, asks whether every bridgeless undirected graph has a collection of cycles such that each edge appears exactly twice. It is a central problem in graph theory with connections to graph embeddings and the circular embedding conjecture.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cycle_double_cover_conjecture">Cycle double cover conjecture</a></li>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT - 5 . 6 Sol : a next-generation model | OpenAI</a></li>
<li><a href="https://www.datacamp.com/blog/gpt-5-6-sol-luna-terra">GPT - 5 . 6 Sol , Terra, and Luna: OpenAI's Next-Gen Model... | DataCamp</a></li>

</ul>
</details>

**Discussion**: Commenters noted the irony that the prompt spent much effort telling the model to actually solve the problem, and some questioned whether the community truly cares about the conjecture, given its low prior engagement. Others highlighted that the proof's conciseness suggests a clever trick, but that autonomous theory-building remains an AI milestone yet to be achieved.

**Tags**: `#AI`, `#mathematics`, `#proof`, `#GPT-5.6`, `#graph theory`

---

<a id="item-2"></a>
## [China's Long March 10B achieves world's first net-based rocket recovery at sea](https://weibo.com/7340734455/R814of1Ki) ⭐️ 9.0/10

On July 10, 2026, China's Long March 10B rocket launched from Hainan Commercial Space Launch Site and successfully recovered its first stage via a net-based system on a sea platform, marking China's first controlled recovery of a rocket first stage and the world's first net-based recovery of a launch vehicle. This breakthrough establishes China as a key player in reusable rocket technology, reducing launch costs and enabling more frequent access to space. The net-based recovery method eliminates the need for landing legs, simplifying the rocket design and potentially accelerating the development of reusable launch vehicles globally. The Long March 10B is derived from the Long March 10A by removing crew safety equipment and replacing the second stage with a liquid oxygen/methane variant. The net-based recovery uses a well-shaped arresting cable system on the recovery ship to catch the rocket's hook and buffer it to a stop, achieving无损 (nondestructive) recovery.

telegram · zaihuapd · Jul 10, 04:36

**Background**: Reusable rocket technology, pioneered by SpaceX's Falcon 9, typically uses landing legs for vertical touchdown. China's Long March series has traditionally been expendable. The net-based recovery approach offers an alternative that avoids the mass penalty of landing legs and allows recovery on a moving platform at sea, which could be more flexible for various mission profiles.

<details><summary>References</summary>
<ul>
<li><a href="https://www.news.cn/20260710/76bfd64fb0b1446ba00ac7514c49bb40/c.html">新华社快讯：长征十号乙运载火箭实现一子级可控回收-新华网</a></li>
<li><a href="https://www.news.cn/20260710/699cccd9572b4c70a0c9eddc96b77eaf/c.html">新华鲜报丨长征十号乙首飞成功 我国运载火箭首次实现可控回收-新华网</a></li>
<li><a href="https://www.guancha.cn/kegongliliang/2026_07_10_823277.shtml">长10乙 回 收 成功：美国人做了和没做的事，我们都要做-科工力量</a></li>

</ul>
</details>

**Tags**: `#rocket recovery`, `#reusable rockets`, `#aerospace`, `#China space program`, `#engineering milestone`

---

<a id="item-3"></a>
## [SGLang v0.5.15 Boosts GLM-5.2 on Blackwell GPUs](https://github.com/sgl-project/sglang/releases/tag/v0.5.15) ⭐️ 8.0/10

SGLang v0.5.15 delivers optimized serving for GLM-5.2 NVFP4 on Blackwell GPUs, achieving over 500 tokens per second per user on 8x B300 and 450 tok/s/user on 4x GB300 at batch size 1. Key improvements include Speculative Decoding V2 by default, IndexShare MTP, TopK V2, and GEMM optimizations. This release significantly improves the efficiency of serving large language models on NVIDIA's latest Blackwell architecture, enabling higher throughput and lower latency for production AI inference. The optimizations, especially Spec V2 and IndexShare MTP, reduce overhead and improve draft-step efficiency, benefiting applications that require real-time or high-throughput LLM serving. Speculative Decoding V2 becomes the default, using CUDA-graphable DSA draft-extend to eliminate CPU syncs and fuse metadata ops, yielding an 11% end-to-end TPS gain. IndexShare MTP reuses the indexer top-k across draft steps, reducing draft-step cost by up to 1.9x at long context. TopK V2 fuses top-k selection with page-table transform, supporting runtime k up to 2048.

github · Fridge003 · Jul 10, 22:58

**Background**: NVFP4 is a 4-bit floating-point format introduced with NVIDIA's Blackwell GPU architecture, designed for efficient low-precision inference while maintaining accuracy. SGLang is an open-source framework for serving large language models, and speculative decoding is a technique that uses a smaller draft model to predict multiple tokens per step, reducing latency. The Blackwell B300 and GB300 GPUs are NVIDIA's latest high-performance accelerators for AI workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/">Introducing NVFP4 for Efficient and Accurate Low-Precision Inference</a></li>
<li><a href="https://docs.sglang.io/cookbook/autoregressive/GLM/GLM-5.2">GLM-5.2 - SGLang Documentation</a></li>

</ul>
</details>

**Tags**: `#AI inference`, `#GPU optimization`, `#LLM serving`, `#SGLang`, `#Blackwell`

---

<a id="item-4"></a>
## [Apple sues OpenAI over trade secret theft](https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/) ⭐️ 8.0/10

Apple has filed a lawsuit against OpenAI, alleging that the company systematically recruited ex-Apple employees who stole trade secrets, including confidential hardware information and supplier contacts. This high-profile legal battle between two tech giants could set a precedent for trade secret protection in the AI industry and impact how companies handle employee transitions. Apple claims OpenAI instructed new hires to avoid disclosing their new jobs to Apple, and that employees emailed themselves confidential data upon leaving. The lawsuit also alleges OpenAI used Apple's hardware information to approach suppliers.

hackernews · stock_toaster · Jul 10, 20:47 · [Discussion](https://news.ycombinator.com/item?id=48865019)

**Background**: Trade secrets are confidential business information that provides a competitive edge. Companies like Apple rely on strict confidentiality agreements to protect such assets. This case highlights the tension between talent mobility and intellectual property protection.

**Discussion**: Commenters largely side with Apple, calling the evidence damning and predicting OpenAI will face severe consequences. Some note that discovery could reveal more damaging information for OpenAI.

**Tags**: `#Apple`, `#OpenAI`, `#trade secrets`, `#legal`, `#AI`

---

<a id="item-5"></a>
## [Chinese Courts Rule Game Accounts Inheritable, Platform Bans Invalid](https://www.tomshardware.com/tech-industry/big-tech/chinese-courts-allow-heirs-to-inherent-accounts-of-deceased-gamers-multiple-cases-spanning-years-establish-precedent-for-digital-ownership-of-games-in-game-items-and-microtransactions) ⭐️ 8.0/10

Chinese courts have ruled in multiple cases spanning several years that virtual assets such as game accounts, equipment, and cryptocurrencies are inheritable property, invalidating platform clauses that prohibit inheritance. This establishes a significant legal precedent for digital ownership in China, affecting millions of gamers and their heirs, and pressures platforms to revise user agreements to comply with inheritance rights. The courts ruled that chat logs and other purely personal privacy content are not inheritable and will be archived by the platform; platforms may charge reasonable fees for transferring accounts.

telegram · zaihuapd · Jul 10, 02:56

**Background**: In China, the Civil Code recognizes virtual property as legal property, but platform user agreements often prohibit inheritance. These court decisions clarify that such clauses violate statutory rights and are unenforceable, building on earlier cases like the 'Dragon Saber' case in the game 'Zheng Tu'.

<details><summary>References</summary>
<ul>
<li><a href="https://www.spp.gov.cn/spp/llyj/201808/t20180811_388070.shtml">网络虚拟账号能否继承_中华人民共和国最高人民检察院</a></li>
<li><a href="https://peking.bjd.com.cn/channels/5b165687a010550e5ddc0e70/contentShare/64632331e4b0cee0ece8db92/AP662793a6e4b0f6c5abd5d6c4.html">“我的游戏账号，孩子能继承吗？”</a></li>
<li><a href="https://www.dehenglaw.com/CN/tansuocontent/0008/030668/7.aspx?MID=0902">虚拟财产能否继承？ - 德恒探索 - 德恒律师事务所</a></li>

</ul>
</details>

**Tags**: `#digital inheritance`, `#virtual assets`, `#Chinese law`, `#gaming`, `#digital ownership`

---

<a id="item-6"></a>
## [Tencent in Talks to Acquire AI Startup Manus from Meta](https://www.reuters.com/technology/tencent-talks-become-ai-start-up-manus-largest-shareholder-ft-reports-2026-07-10/) ⭐️ 8.0/10

Tencent is negotiating to acquire AI startup Manus from Meta, aiming to become its largest shareholder, after Beijing blocked Meta's $2 billion acquisition. This deal could reshape the AI landscape in China, giving Tencent control over a promising AI agent platform and intensifying competition with other tech giants. Tencent will partner with original investors ZhenFund and HSG to buy back Manus from Meta at a price no less than $2 billion.

telegram · zaihuapd · Jul 10, 06:45

**Background**: Manus is an AI agent platform that goes beyond chat to execute multi-step tasks autonomously. ZhenFund is a Chinese angel investment fund co-founded by New Oriental co-founders, and HSG (HongShan) is a major Chinese venture capital firm formerly known as Sequoia Capital China.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Manus_AI_company">Manus ( AI company ) — Grokipedia</a></li>
<li><a href="https://www.followme.com/baike/27122.html">真 格 基 金 是什么 真 格 基 金 怎么样_Followme交易社区</a></li>
<li><a href="https://en.wikipedia.org/wiki/HongShan">HongShan - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#M&A`, `#Tencent`, `#Meta`, `#Manus`

---

<a id="item-7"></a>
## [OpenAI, Google reportedly provided AI models to blacklisted Chinese firms via Singapore](https://www.ft.com/content/5d6aafa1-5d47-4585-aa95-6ec06a6cd20f) ⭐️ 8.0/10

According to a Financial Times report, OpenAI and Google have been providing advanced AI services to Singapore subsidiaries of Alibaba, Baidu, and Tencent, whose parent companies are on the Pentagon's 1260H list of Chinese military companies. This revelation highlights potential loopholes in US export controls, as current restrictions do not broadly ban Chinese parent companies from accessing advanced AI models outside mainland China, reigniting calls for stricter AI export regulations. OpenAI suspended API access for an Alibaba-affiliated user last month after detecting suspected model distillation, and reported the incident to the US government; Anthropic has adopted stricter policies, fully banning Chinese companies and their overseas entities from accessing its frontier AI models.

telegram · zaihuapd · Jul 10, 09:59

**Background**: The 1260H list, part of the US National Defense Authorization Act, identifies Chinese military companies operating directly or indirectly in the US. Model distillation is a technique that transfers knowledge from a large AI model to a smaller one, which can be used to circumvent API access restrictions by extracting model capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://research.umd.edu/resources/restricted-entities-lists">U . S . Restricted Parties Lists | Division of Research</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>

</ul>
</details>

**Tags**: `#AI`, `#export control`, `#geopolitics`, `#OpenAI`, `#Google`

---

<a id="item-8"></a>
## [China Imposes Temporary Ban on Helium Exports](https://wms.mofcom.gov.cn/zcfb/wmgl/art/2026/art_2a795a0d55df4cada91c9fbd2a2cc13a.html) ⭐️ 8.0/10

On July 10, 2026, China's Ministry of Commerce and General Administration of Customs jointly issued an announcement imposing a temporary ban on the export of helium (HS code 2804290010), effective immediately. This ban could disrupt global supply chains for semiconductors, medical imaging (MRI), and scientific research, as China is a major helium consumer and its domestic demand is rising. The move may exacerbate the ongoing global helium shortage, impacting industries reliant on this critical gas. The ban covers helium with HS code 2804290010 and is based on the Foreign Trade Law of China. The announcement did not specify a duration, stating that adjustments will be announced separately.

telegram · zaihuapd · Jul 10, 13:27

**Background**: Helium is a non-renewable resource essential for cooling in semiconductor manufacturing, as a coolant in MRI machines, and for pressurizing rocket fuel tanks. China has been rapidly expanding its semiconductor industry, increasing domestic helium demand, while global supply has been strained due to production outages and geopolitical tensions.

<details><summary>References</summary>
<ul>
<li><a href="https://thedeepdive.ca/china-helium-export-ban-chip-supply/">China bans helium exports to protect domestic supply</a></li>
<li><a href="https://www.chosun.com/english/world-en/2026/07/10/SZGBZAJ64NAVZCBQT4747RBY7A/">China Bans Helium Exports Vital for Semiconductor Production</a></li>

</ul>
</details>

**Tags**: `#trade policy`, `#helium`, `#supply chain`, `#semiconductors`, `#China`

---

<a id="item-9"></a>
## [Meta Faces $12 Billion EU Fine Over Addictive Design](https://www.theverge.com/policy/963872/meta-eu-addictive-design-200b-fine-risk-digital-services-act-dsa) ⭐️ 8.0/10

The European Commission has preliminarily found that Meta's Facebook and Instagram violate the Digital Services Act due to addictive design features like infinite scroll, autoplay, and personalized recommendations, potentially leading to a fine of up to $12 billion (6% of global annual revenue). This marks one of the largest potential fines under the DSA and could force Meta to redesign core features, setting a precedent for regulating addictive design across the tech industry. The EU criticizes Meta's current time-limiting tools as ineffective and demands default disabling of addictive features, effective screen breaks, and reduced engagement-driven algorithms. The final decision could still change before the fine is imposed.

telegram · zaihuapd · Jul 10, 14:47

**Background**: Infinite scroll exploits the human need for closure, trapping users in endless loops. Personalized recommendation algorithms maximize engagement by predicting user preferences, often leading to compulsive use. The EU's Digital Services Act (DSA) imposes strict obligations on large platforms to mitigate systemic risks, including harms to mental health.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@nireshratnam/infinite-scroll-how-your-brain-is-trapped-in-an-endless-loop-57ebbcd8d125">Infinite Scroll : How Your Brain Is Trapped in an Endless Loop | Medium</a></li>
<li><a href="https://sparkco.ai/blog/social-media-algorithm-engagement-addiction-optimization">Algorithmic Engagement and Surveillance Capitalism: Industry...</a></li>

</ul>
</details>

**Tags**: `#Meta`, `#EU regulation`, `#addictive design`, `#Digital Services Act`, `#tech policy`

---

<a id="item-10"></a>
## [SpaceXAI and Cursor Launch Grok 4.5 for Coding, Legal, Finance](https://t.me/zaihuapd/42484) ⭐️ 8.0/10

SpaceXAI and Cursor have jointly released Grok 4.5, a new AI model optimized for coding, legal, and financial tasks, claiming top performance on the Harvey legal agent benchmark and 2x token efficiency over leading models. This marks the first joint model after SpaceX's $60 billion acquisition of Cursor, signaling a major push into domain-specific AI for high-stakes professional tasks, potentially reshaping competition in the AI coding and legal tech markets. Grok 4.5 runs at 80 tokens per second and is priced at $2 per million input tokens. It is built on a 1.5 trillion-parameter V9 foundation and incorporates data from Cursor, though the acquisition claim remains unverified.

telegram · zaihuapd · Jul 11, 01:44

**Background**: Grok is a series of AI models developed by xAI, SpaceX's AI subsidiary. Cursor is an AI-powered code editor and IDE that achieved a $29.3 billion valuation by early 2026. The Harvey Legal Agent Benchmark evaluates AI agents on legal tasks using tools like file reading and editing.

<details><summary>References</summary>
<ul>
<li><a href="https://x.ai/news/grok-4-5">Grok 4 . 5 is SpaceXAI's smartest model built for coding, agentic tasks...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grok_(chatbot)">Grok (chatbot) - Wikipedia</a></li>
<li><a href="https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark">Introducing Harvey ’s Legal Agent Benchmark</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Grok`, `#SpaceXAI`, `#Cursor`, `#LLM`

---