---
layout: default
title: "Horizon Summary: 2026-07-21 (EN)"
date: 2026-07-21
lang: en
---

> From 76 items, 16 important content pieces were selected

---

1. [Apple Wins CSAM Scanning Lawsuit, Judge Criticizes Privacy Trade-off](#item-1) ⭐️ 8.0/10
2. [Jane Street's Incremental Library for Efficient Computations](#item-2) ⭐️ 8.0/10
3. [Fireside Chat with Claude Code Team Reveals 65% PRs via Claude Tag](#item-3) ⭐️ 8.0/10
4. [AI coding agents make reverse-engineering cheap](#item-4) ⭐️ 8.0/10
5. [Ben Thompson Proposes US Law to Legalize AI Data Collection](#item-5) ⭐️ 8.0/10
6. [Sam Altman's 2022 Email Reveals Open Source Strategy](#item-6) ⭐️ 8.0/10
7. [Data Centers to Quadruple Electricity Use by 2035](#item-7) ⭐️ 8.0/10
8. [US threatens sanctions on Chinese AI models over IP theft](#item-8) ⭐️ 8.0/10
9. [Deezer: Over 50% of daily uploads are AI-generated](#item-9) ⭐️ 8.0/10
10. [Anthropic's $1.5B Copyright Settlement Approved](#item-10) ⭐️ 8.0/10
11. [EU to Share Biometric Data with US for Visa-Free Travel](#item-11) ⭐️ 8.0/10
12. [Zhipu AI Completes Giant Data Center with Domestic Chips](#item-12) ⭐️ 8.0/10
13. [Google Develops 'Frozen v2' AI Chip for Gemini](#item-13) ⭐️ 8.0/10
14. [Cloudflare Launches Internal DNS Service](#item-14) ⭐️ 8.0/10
15. [TSMC May Raise Advanced Node Prices 5-10% in 2026](#item-15) ⭐️ 8.0/10
16. [Google Launches Gemini 3.5 Flash, Pro Coming Next Month](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Apple Wins CSAM Scanning Lawsuit, Judge Criticizes Privacy Trade-off](https://blog.ericgoldman.org/archives/2026/07/apple-defeats-liability-for-not-scanning-icloud-for-csam-but-the-judge-was-not-pleased-amy-v-apple.htm) ⭐️ 8.0/10

A U.S. court ruled that Apple is not liable for failing to scan iCloud for Child Sexual Abuse Material (CSAM), dismissing a lawsuit against the company. The judge expressed displeasure with the outcome, stating that privacy protections leave child victims as collateral damage. This ruling sets a legal precedent that tech companies may not be required to scan encrypted cloud services for illegal content, reinforcing the tension between privacy and child safety. It could influence future legislation and corporate policies on encryption and content moderation. Apple previously proposed client-side CSAM scanning on devices but abandoned it after privacy backlash. The court noted that end-to-end encryption inherently prevents server-side scanning, and Apple's current iCloud encryption is not fully end-to-end by default.

hackernews · speckx · Jul 21, 14:31 · [Discussion](https://news.ycombinator.com/item?id=48992870)

**Background**: Child Sexual Abuse Material (CSAM) refers to illegal images and videos depicting child sexual abuse. Tech companies face pressure to detect and report CSAM, but end-to-end encryption prevents service providers from accessing content. Apple's iCloud uses encryption, but Advanced Data Protection (ADP) is required for full end-to-end encryption.

<details><summary>References</summary>
<ul>
<li><a href="https://9to5mac.com/guides/csam/">CSAM : Apple's efforts to detect Child Sexual Abuse Materials - 9to5Mac</a></li>
<li><a href="https://www.lawfaremedia.org/article/apple-client-side-scanning-system">The Apple Client-Side Scanning System | Lawfare</a></li>

</ul>
</details>

**Discussion**: Commenters largely supported the ruling as a win for privacy, with some arguing that true end-to-end encryption is impossible when the company controls both the app and servers. Others noted the tragic trade-off, acknowledging that privacy protections can hinder CSAM detection.

**Tags**: `#privacy`, `#encryption`, `#Apple`, `#CSAM`, `#legal`

---

<a id="item-2"></a>
## [Jane Street's Incremental Library for Efficient Computations](https://github.com/janestreet/incremental) ⭐️ 8.0/10

Jane Street has released Incremental, an OCaml library that enables efficient incremental computations by automatically recomputing only the parts of a computation graph that change when inputs are updated. This library brings the power of incremental computation to OCaml, enabling developers to build responsive applications and systems (like build tools or financial models) that avoid full recomputation, saving time and resources. Incremental is similar to reactive programming signals in JavaScript frameworks (e.g., Vue, SolidJS) but is designed for OCaml's functional programming paradigm. It uses a directed acyclic graph (DAG) to model dependencies and propagate changes efficiently.

hackernews · handfuloflight · Jul 21, 03:50 · [Discussion](https://news.ycombinator.com/item?id=48987822)

**Background**: Incremental computation is a technique that reuses previous results to compute new outputs when inputs change, avoiding redundant work. This concept is widely used in build systems (e.g., Make, Bazel) and reactive programming. Jane Street's Incremental library implements self-adjusting computations, a concept introduced by Umut Acar, and has evolved through seven implementations over years of practical use.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/janestreet/incremental">GitHub - janestreet/incremental: A library for incremental computations</a></li>
<li><a href="https://www.janestreet.com/tech-talks/seven-implementations-of-incremental/">Seven Implementations of Incremental - Jane Street</a></li>

</ul>
</details>

**Discussion**: Commenters noted the similarity between Incremental and JavaScript signals, with one mentioning its use in frameworks like Vue and SolidJS. Another commenter recalled Goldman Sachs using a similar approach for instrument pricing decades ago, highlighting the long history of incremental computation in finance.

**Tags**: `#incremental computation`, `#reactive programming`, `#Jane Street`, `#OCaml`, `#build systems`

---

<a id="item-3"></a>
## [Fireside Chat with Claude Code Team Reveals 65% PRs via Claude Tag](https://simonwillison.net/2026/Jul/21/cat-and-thariq/#atom-everything) ⭐️ 8.0/10

Simon Willison hosted a fireside chat with Anthropic's Claude Code team, revealing that Claude Tag now handles 65% of product engineering pull requests for the team, and that the Claude Code system prompt has been reduced by 80% for newer models like Fable 5. These metrics demonstrate the growing maturity and trust in AI coding agents within Anthropic itself, offering concrete evidence of productivity gains and best-practice evolution for the broader AI engineering community. The team ships features to employees first and only releases those that show user retention; critical changes still undergo manual review, but automated review is used for outer layers. Adding examples to system prompts is no longer recommended for latest models.

rss · Simon Willison · Jul 21, 12:54

**Background**: Claude Code is Anthropic's AI coding agent, launched alongside Claude 3.7 Sonnet in early 2025. Claude Tag is a Slack integration that allows users to @ mention Claude in channels for collaborative coding. The AI Engineer World's Fair is a conference focused on AI engineering practices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI)</a></li>
<li><a href="https://claude.com/product/tag">Claude in Slack: Tag @ Claude in any thread | Claude by Anthropic</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Claude Code`, `#Anthropic`, `#coding agents`, `#AI engineering`

---

<a id="item-4"></a>
## [AI coding agents make reverse-engineering cheap](https://simonwillison.net/2026/Jul/20/cheap-reverse-engineering/#atom-everything) ⭐️ 8.0/10

AI coding agents have drastically reduced the cost and effort required to reverse-engineer undocumented APIs in home devices, making automation projects viable even for hobbyists. This shift changes the ROI calculus for home automation, lowering the barrier to entry and reducing the psychological burden of future maintenance, potentially accelerating adoption of custom smart home solutions. The post highlights that prior to agents, the effort to reverse-engineer and maintain undocumented APIs often outweighed the benefits; now, the low cost of trying and failing makes experimentation risk-free.

rss · Simon Willison · Jul 20, 19:24

**Background**: Reverse-engineering involves analyzing a device's network traffic or firmware to understand its protocols, often to control it without official support. Undocumented APIs are common in consumer smart home devices, which may change without notice, requiring ongoing maintenance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.agentre-bench.ai/">AgentRE-Bench — LLM Reverse Engineering Benchmark</a></li>
<li><a href="https://www.linkedin.com/pulse/i-used-ai-coding-agent-my-phone-reverse-engineer-smart-daniel-potts-ovd4c">I Used an AI Coding Agent on My Phone to Reverse - Engineer ...</a></li>
<li><a href="https://stevessmarthomeguide.com/smart-home-apis/">Understanding Smart Home APIs</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#reverse engineering`, `#software engineering`, `#home automation`, `#cost of code`

---

<a id="item-5"></a>
## [Ben Thompson Proposes US Law to Legalize AI Data Collection](https://simonwillison.net/2026/Jul/20/afraid-of-chinese-models/#atom-everything) ⭐️ 8.0/10

Ben Thompson proposed that the US should pass a law explicitly making data collection for AI training fair use and barring terms of service that forbid distillation, to help US open models compete with Chinese counterparts. He also noted that Alibaba released Qwen 3.8 Max as open weights, possibly influenced by a recent Xi Jinping speech encouraging open source. This proposal addresses a key hypocrisy in AI: labs that train on unlicensed data often prohibit others from distilling their models. If enacted, it could level the playing field for US open models against Chinese ones, and reshape copyright policy for AI training. Distillation is the process of querying a larger model's API to train a smaller model, which is nearly impossible to stop technically. Qwen 3.8 Max is a 2.4 trillion parameter model, nearly as large as Kimi K3's 2.8 trillion parameters.

rss · Simon Willison · Jul 20, 17:09

**Background**: Knowledge distillation is a machine learning technique where a smaller 'student' model learns from a larger 'teacher' model's outputs. Open weights models allow users to download and run the model locally, but do not include full training code or data. The US Copyright Office has recently weighed in on whether AI training constitutes fair use, with some courts considering the public benefit.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told – Open Source Initiative</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_intelligence_and_copyright">Artificial intelligence and copyright - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open models`, `#distillation`, `#copyright`, `#Chinese AI`

---

<a id="item-6"></a>
## [Sam Altman's 2022 Email Reveals Open Source Strategy](https://simonwillison.net/2026/Jul/20/sam-altman/#atom-everything) ⭐️ 8.0/10

A 2022 email from Sam Altman to OpenAI's board, exposed in the Musk v. Altman lawsuit, reveals plans to release a GPT-3-level open source model that can run on consumer hardware to preempt competitors like Stability AI and discourage new entrants. This email provides rare insight into OpenAI's internal strategic thinking about open source models, highlighting how competitive pressures influenced decisions that affect AI accessibility, ethics, and market dynamics. The email is dated October 1, 2022, and was part of the Musk v. Altman legal case in 2026. Altman specifically mentions releasing the model before 'Stability or someone else does,' referring to Stability AI's StableLM series.

rss · Simon Willison · Jul 20, 03:47

**Background**: GPT-3 is a large language model developed by OpenAI, released in 2020, known for its ability to generate human-like text. At the time of the email, open source alternatives like GPT-Neo and OPT were emerging, but none matched GPT-3's capability. Running such models on consumer hardware was a significant technical challenge, requiring optimization and quantization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-3">GPT-3 - Wikipedia</a></li>
<li><a href="https://github.com/Stability-AI/StableLM">Stability - AI /StableLM: StableLM: Stability AI Language Models ...</a></li>
<li><a href="https://www.local-llm.net/learn/what-is-local-ai/">What Is Local AI? The Complete Guide to Running AI... | local - llm .net</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#ai-ethics`, `#openai`, `#sam-altman`, `#generative-ai`

---

<a id="item-7"></a>
## [Data Centers to Quadruple Electricity Use by 2035](https://techcrunch.com/2026/07/21/data-centers-expected-to-use-4x-more-electricity-by-2035/) ⭐️ 8.0/10

A new projection indicates that data centers built through 2033 could consume as much electricity as India's current total usage, quadrupling their power demand by 2035. This surge in energy consumption poses significant challenges for energy infrastructure, AI scalability, and global sustainability efforts, potentially straining power grids and increasing carbon emissions. The projection covers data centers built through 2033, and the comparison to India's electricity usage highlights the enormous scale of expected growth.

rss · TechCrunch AI · Jul 21, 18:06

**Background**: Data centers are facilities that house computer systems and associated components, such as telecommunications and storage. They are critical for cloud computing, AI training, and digital services, but are highly energy-intensive.

**Tags**: `#data centers`, `#energy consumption`, `#AI infrastructure`, `#sustainability`

---

<a id="item-8"></a>
## [US threatens sanctions on Chinese AI models over IP theft](https://techcrunch.com/2026/07/21/us-threatens-sanctions-against-chinese-ai-models-over-ip-theft/) ⭐️ 8.0/10

U.S. Treasury Secretary Scott Bessent said the Trump administration could sanction Chinese open-source AI models if they are found to be built on intellectual property theft from American companies. This escalates US-China tech tensions and could reshape the global AI landscape by restricting the distribution of Chinese open-source models, affecting developers and companies worldwide. Bessent specifically mentioned the practice of 'distillation,' where a model is trained on outputs from another model, as a potential form of IP theft. The administration is reportedly considering adding Chinese AI labs to sanctions lists and holding US companies liable for security failures.

rss · TechCrunch AI · Jul 21, 15:37

**Background**: Open-source AI models have become popular due to their transparency and lower cost, but they can still be black boxes regarding training data. The US has previously imposed export controls on advanced AI chips to China, and this sanctions threat represents a new front in the technology competition.

<details><summary>References</summary>
<ul>
<li><a href="https://www.businessinsider.com/treasury-secretary-chinese-ai-open-source-sanctions-kimi-k3-2026-7">Treasury Secretary says its 'unacceptable' that Chinese open source AI models may have been built on 'IP theft'</a></li>
<li><a href="https://www.cnbc.com/2026/07/21/bessent-china-ai-sanctions.html">Bessent says U.S. could sanction China over AI model 'theft'</a></li>
<li><a href="https://the-decoder.com/trump-administration-reportedly-builds-a-slow-motion-ban-on-chinese-ai-models-through-sanctions-and-soft-pressure/">Trump administration reportedly builds a slow-motion ban on Chinese AI models through sanctions and soft pressure</a></li>

</ul>
</details>

**Tags**: `#AI`, `#geopolitics`, `#sanctions`, `#open source`, `#policy`

---

<a id="item-9"></a>
## [Deezer: Over 50% of daily uploads are AI-generated](https://techcrunch.com/2026/07/21/music-streamer-deezer-says-more-than-50-of-daily-uploads-are-ai-generated/) ⭐️ 8.0/10

Deezer reported that in June, more than 90,000 AI-generated tracks were uploaded daily to its platform, accounting for over 50% of all daily uploads. This statistic quantifies the massive scale of AI-generated content on a major streaming platform, highlighting urgent challenges for copyright, curation, and content moderation across the music industry. Deezer has developed an AI music detector that has identified over 13.4 million AI tracks in 2025, and it offers this detection tool for free to users across multiple platforms.

rss · TechCrunch AI · Jul 21, 13:27

**Background**: Generative AI tools like SOUNDRAW, AIVA, and Canva's AI music generator allow anyone to create royalty-free music in seconds. As these tools become widespread, streaming platforms face the challenge of distinguishing human-made from AI-generated content. Deezer's aggressive detection approach contrasts with competitors like Spotify and Apple Music, which only add labels to AI content.

<details><summary>References</summary>
<ul>
<li><a href="https://www.deezer.com/explore/ai-music-detector/">Free AI Music Detector by Deezer | AI Song checker</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pQdmZhc0VSRVJiN05uZlRXbXhpZ0FQAQ?hl=en-NA&gl=NA&ceid=NA:en">Google News - Deezer 's AI music detector - Overview</a></li>

</ul>
</details>

**Tags**: `#AI-generated content`, `#music streaming`, `#generative AI`, `#content moderation`, `#industry impact`

---

<a id="item-10"></a>
## [Anthropic's $1.5B Copyright Settlement Approved](https://techcrunch.com/2026/07/20/anthropics-landmark-1-5b-copyright-settlement-is-approved/) ⭐️ 8.0/10

A U.S. court has granted final approval to Anthropic's $1.5 billion copyright settlement with authors who claimed the company used their works without permission to train AI models. This landmark settlement is the largest of its kind in the AI era, signaling that AI companies may face significant financial liability for using copyrighted training data, though the core legal question of fair use remains unresolved. The settlement provides compensation for each class work but does not establish a legal precedent on whether using copyrighted material for AI training constitutes fair use, leaving the broader legal landscape uncertain.

rss · TechCrunch AI · Jul 21, 00:12

**Background**: Anthropic, an AI safety company, faced a class-action lawsuit from authors alleging that its AI models were trained on pirated copies of their books and articles. The case is part of a wave of copyright lawsuits against AI companies, including OpenAI and Meta, over the use of copyrighted data in training large language models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/story/anthropic-settlement-lawsuit-copyright/">Anthropic Agrees to Pay Authors at Least $1.5 Billion in AI Copyright ...</a></li>
<li><a href="https://www.linkedin.com/pulse/anthropic-settlement-ai-training-data-what-means-businesses-using-hvvme">The Anthropic Settlement & AI Training Data: What It Means for...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#copyright`, `#legal`, `#Anthropic`, `#settlement`

---

<a id="item-11"></a>
## [EU to Share Biometric Data with US for Visa-Free Travel](https://edri.org/our-work/the-eu-is-about-to-sell-our-most-sensitive-data-to-the-us-for-visa-free-travel/) ⭐️ 8.0/10

The European Commission is negotiating an Enhanced Border Security Partnership (EBSP) framework with the US, which would require EU member states to share biometric data with US authorities in exchange for visa-free travel for US citizens. This agreement could set a precedent for mass surveillance and data sharing between major powers, potentially undermining EU privacy protections and exposing sensitive biometric data to risks of misuse. A leaked draft shows the EU has largely accepted US demands for unrestricted access to biometric databases, including the sharing of 'risk indicators' based on political views, which could threaten freedom of expression.

telegram · zaihuapd · Jul 20, 15:08

**Background**: Biometric data includes unique physical characteristics like fingerprints and facial recognition patterns, which cannot be changed if compromised. The EBSP framework would be the first large-scale agreement for sharing EU citizens' biometric data with US border authorities, raising concerns about privacy and data security.

<details><summary>References</summary>
<ul>
<li><a href="https://leantrustgovernance.substack.com/p/the-eu-us-biometric-data-deal-trading">How the EU – US Border Deal Rewrites Privacy</a></li>
<li><a href="https://cdt.org/insights/responding-to-the-eu-us-negotiations-on-reciprocal-data-exchanges-for-border-procedures/">Responding to the EU - US Negotiations on Reciprocal Data Exchanges...</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#biometric data`, `#EU-US agreement`, `#data protection`, `#civil liberties`

---

<a id="item-12"></a>
## [Zhipu AI Completes Giant Data Center with Domestic Chips](https://www.bloomberg.com/news/articles/2026-07-20/z-ai-completes-giant-data-center-with-chinese-chips-to-train-ai) ⭐️ 8.0/10

Zhipu AI has completed construction of a large data center powered entirely by domestically produced Chinese chips, with a power capacity of 1 gigawatt, and has begun partial operations to support its GLM platform development. This milestone demonstrates China's progress toward AI self-sufficiency by reducing reliance on foreign chips, and it is one of the largest AI facilities built by a Chinese AI lab, potentially boosting domestic AI model training capabilities. The data center's 1 GW power capacity is enough to supply approximately 750,000 households. Zhipu AI operates multiple computing clusters each with over 10,000 chips, and this new facility is among the largest of its kind in China.

telegram · zaihuapd · Jul 20, 15:43

**Background**: Zhipu AI is a Chinese AI company spun off from Tsinghua University's Knowledge Engineering Lab (KEG Lab), known for its open-source GLM (General Language Model) series. The GLM-5 flagship model achieved a SWE-Bench score of 77.8%, the highest among open-source models for tool-calling ability. Domestic chip development in China has been accelerating, with Morgan Stanley predicting the domestic AI chip market could reach $67 billion by 2030, with domestic chips meeting about 76% of demand.

<details><summary>References</summary>
<ul>
<li><a href="https://www.it007.com/article-331776-1.html">产 业_消息称智谱建成大型 AI 数 据 中 心 ： 全 部采用 国 产 芯 片 _ IT007...</a></li>
<li><a href="https://vpn07.com/tw/blog/2026-glm4-quanpingtai-anzhuang-jiaoxue-bendi-bushu.html">智 谱 GLM 全 平 台 安裝教學：清華系開源 AI 本地部署 2026</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#domestic chips`, `#China`, `#data center`, `#GLM`

---

<a id="item-13"></a>
## [Google Develops 'Frozen v2' AI Chip for Gemini](https://www.quiverquant.com/news/Google+Reportedly+Developing+%E2%80%98Frozen+v2%E2%80%99+AI+Chip+to+Boost+Gemini+Efficiency) ⭐️ 8.0/10

Google is reportedly developing a new AI server chip codenamed 'Frozen v2' that hard-codes some capabilities of its Gemini model directly into hardware, aiming to achieve 6 to 10 times better tokens-per-watt than its latest TPUs, with deployment planned for 2028. This chip could dramatically improve inference efficiency, addressing a critical bottleneck in AI deployment and potentially reducing the GPU advantage in AI compute. It also highlights a trend of custom hardware designed for specific models, which could reshape the AI hardware landscape. Frozen v2 is positioned as a complementary product to Google's TPU, not a replacement, and aims to alleviate internal compute shortages that have limited Google Cloud's ability to serve some enterprise customers. The chip is expected to be deployed by 2028.

telegram · zaihuapd · Jul 21, 01:01

**Background**: Tokens-per-watt is a key metric for AI inference efficiency, measuring how many output tokens a system produces per unit of power. Google's TPUs are already specialized AI accelerators, but Frozen v2 goes further by embedding model-specific logic into silicon, potentially offering significant efficiency gains for Gemini workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://qz.com/google-gemini-chip-frozen-tpu-efficiency-072026">Google developing Gemini-specific chip called Frozen v 2</a></li>
<li><a href="https://logicity.in/en/blog/google-s-frozen-v2-chip-embeds-gemini-in-hardware-for-6-10x-gains">Google 's Frozen v 2 chip embeds Gemini in hardware for... | Logicity</a></li>
<li><a href="https://cowlpane.com/ai/my-ai-diary-google-s-frozen-v2-chip-shakes-the-gpu-moat/">Google Frozen v 2 Chip vs GPU Moat — Cowlpane</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#Google`, `#Gemini`, `#TPU`, `#inference efficiency`

---

<a id="item-14"></a>
## [Cloudflare Launches Internal DNS Service](https://blog.cloudflare.com/internal-dns/) ⭐️ 8.0/10

Cloudflare announced the general availability of its Internal DNS service on July 20, 2026, providing authoritative and recursive DNS resolution for private networks, integrated with Zero Trust and the global Cloudflare network. This service unifies public and private DNS on a single platform, simplifying split-horizon DNS management and extending Zero Trust policies to the DNS layer, reducing complexity for enterprises. Existing Cloudflare Gateway customers can enable Internal DNS at no additional cost. It supports deployment via API, Terraform, and Cloudflare WAN, and allows administrators to set resolver policies to control which internal views different users and devices can access.

telegram · zaihuapd · Jul 21, 03:49

**Background**: Split-horizon DNS (also known as split-view or split-brain DNS) provides different DNS responses based on the source of the request, typically returning internal IP addresses for internal users and public IPs for external users. Traditionally, managing split-horizon DNS requires maintaining separate DNS servers or views, which can lead to data drift and configuration complexity. Cloudflare's Internal DNS integrates this capability with its Zero Trust and network services, offering a unified control plane.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Split-horizon_DNS">Split-horizon DNS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero_trust_design">Zero trust design</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#DNS`, `#Zero Trust`, `#networking`, `#enterprise`

---

<a id="item-15"></a>
## [TSMC May Raise Advanced Node Prices 5-10% in 2026](https://t.me/zaihuapd/42691) ⭐️ 8.0/10

TSMC is considering a 5-10% price increase for all its advanced process nodes (5nm/4nm, 3nm, and 2nm) in 2026 to offset US tariffs, currency fluctuations, and supply chain cost pressures. The company has already communicated the higher 2026 quotes to its foundry partners. This price hike directly impacts major clients like NVIDIA and Apple, potentially raising chip costs and affecting the entire semiconductor ecosystem. It signals industry-wide cost pressures and may lead to higher prices for consumer electronics and AI hardware. The increase applies to all advanced nodes including 5nm/4nm, 3nm, and 2nm. TSMC chairman Wei Zhejia humorously declined to confirm the plan, saying 'what's in the heart cannot be spoken by the mouth.'

telegram · zaihuapd · Jul 21, 09:28

**Background**: TSMC is the world's largest dedicated semiconductor foundry, manufacturing chips for companies like Apple, NVIDIA, and AMD. Advanced nodes (5nm and below) are critical for high-performance computing and mobile devices. The US has been considering tariffs on imported semiconductors, and currency fluctuations (e.g., USD/TWD) affect TSMC's revenue.

<details><summary>References</summary>
<ul>
<li><a href="https://www.elecfans.com/d/1528945.html">台 积 电 在 5 nm 及未来的 3 nm 工 艺 上依然是老大- 电 子发烧友网</a></li>
<li><a href="https://m.laoyaoba.com/n/954522">【头条】 232 半 导 体 关 税 对 国 内企 业 影 响 有限</a></li>

</ul>
</details>

**Tags**: `#TSMC`, `#semiconductor`, `#pricing`, `#chip manufacturing`, `#supply chain`

---

<a id="item-16"></a>
## [Google Launches Gemini 3.5 Flash, Pro Coming Next Month](https://t.me/zaihuapd/42699) ⭐️ 8.0/10

Google has officially launched the Gemini 3.5 Flash model, which is now available globally, and announced that the more powerful Gemini 3.5 Pro will be released next month. This release marks a significant step in Google's AI strategy, offering near-Pro level reasoning and coding capabilities at Flash-tier cost and speed, which could accelerate the adoption of agentic AI in enterprise and developer workflows. Gemini 3.5 Flash delivers 4x faster output speed and significantly lower cost compared to comparable models, with a 1M token context window and support for text, image, video, audio, and PDF inputs.

telegram · zaihuapd · Jul 21, 15:23

**Background**: Gemini is Google's family of multimodal large language models. The Flash series is designed for high efficiency and low latency, while the Pro series targets complex reasoning and coding tasks. Agentic AI refers to AI systems that can autonomously execute multi-step workflows to achieve goals, going beyond simple text generation.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3 . 5 Flash — Google DeepMind</a></li>
<li><a href="https://openrouter.ai/google/gemini-3.5-flash">Gemini 3 . 5 Flash - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/">Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Google`, `#Gemini`, `#LLM`, `#Machine Learning`

---