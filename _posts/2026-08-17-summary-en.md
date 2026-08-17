---
layout: default
title: "Horizon Summary: 2026-08-17 (EN)"
date: 2026-08-17
lang: en
---

> From 66 items, 14 important content pieces were selected

---

1. [DuckDB v2.0 Preview: Quack Protocol and Stable C++ API](#item-1) ⭐️ 8.0/10
2. [AI-Generated Copilot Autofix Introduces Critical Vulnerability in Snowflake's Jira Workflow](#item-2) ⭐️ 8.0/10
3. [Anthropic's Claude Watermarking Sparks Ethical and Technical Debate](#item-3) ⭐️ 8.0/10
4. [Apple's ATT Treated Its Own Apps Better; Regulators Demand Equal Treatment](#item-4) ⭐️ 8.0/10
5. [AirTag Tracks Rare Book Order to Amazon AI Training Facility](#item-5) ⭐️ 8.0/10
6. [Qwen 3.8 27B: Strong Benchmarks but Defaults to Overthinking](#item-6) ⭐️ 8.0/10
7. [Nvidia Invests $1.5B in SoftBank Data Center Developer for OpenAI](#item-7) ⭐️ 8.0/10
8. [Stripe to Acquire AI Gateway Startup OpenRouter for $7B+](#item-8) ⭐️ 8.0/10
9. [PJM's $12B Modeling Mistake: Ratepayers at Risk Again](#item-9) ⭐️ 8.0/10
10. [How to Make Sparse Attention and KV Compression Look Good: A Guide to Evaluation Pitfalls](#item-10) ⭐️ 8.0/10
11. [SSOG-Attention: Sub-quadratic Attention via Separable Gaussians](#item-11) ⭐️ 8.0/10
12. [OpenAI Previews Ultrafast Mode for GPT-5.6 Sol, 14x Faster](#item-12) ⭐️ 8.0/10
13. [Meituan Executive Reflects on Costly 'Shrimp Farming' AI Initiative](#item-13) ⭐️ 8.0/10
14. [Unitree Teases 'Superman' Humanoid Robot with 2-Meter Jump](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DuckDB v2.0 Preview: Quack Protocol and Stable C++ API](https://duckdb.org/2026/08/17/duckdb-20-highlights) ⭐️ 8.0/10

DuckDB has released a preview of v2.0, introducing major features including the Quack remote protocol for client-server setups and a stable C++ API for extensions. The preview highlights these capabilities ahead of the official release. This release is significant because DuckDB is widely used for analytical workloads, and the Quack protocol enables concurrent writers and client-server deployments, expanding its use cases. The stable C++ API lowers the barrier for extension development, fostering a richer ecosystem. Quack is an RPC protocol built on HTTP, allowing DuckDB instances to communicate in a client-server setup with multiple concurrent writers. The stable C++ API is available in a dedicated repository (duckdb-cpp-api) and is designed for building extensions that remain compatible across versions.

hackernews · ibotty · Aug 17, 13:46 · [Discussion](https://news.ycombinator.com/item?id=49330781)

**Background**: DuckDB is an in-process analytical database known for its speed and ease of use, often used for data processing and analytics. Previously, its C++ API was internal and unstable, and it lacked a native client-server protocol, limiting certain deployment scenarios. The v2.0 preview addresses these gaps.

<details><summary>References</summary>
<ul>
<li><a href="https://duckdb.org/quack/">Quack Remote Protocol – DuckDB</a></li>
<li><a href="https://duckdb.org/2026/05/12/quack-remote-protocol">Quack: The DuckDB Client-Server Protocol – DuckDB</a></li>
<li><a href="https://github.com/duckdb/duckdb-cpp-api">GitHub - duckdb/duckdb-cpp-api: Stable C++ API for DuckDB that can be used to make extensions · GitHub</a></li>

</ul>
</details>

**Discussion**: Community sentiment is highly positive, with users expressing excitement about Quack and the stable C++ API. Some users highlight practical benefits like easier extension maintenance and broader tooling integration, while others appreciate DuckDB's portability and performance in real-world projects.

**Tags**: `#DuckDB`, `#database`, `#analytics`, `#release`, `#open source`

---

<a id="item-2"></a>
## [AI-Generated Copilot Autofix Introduces Critical Vulnerability in Snowflake's Jira Workflow](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) ⭐️ 8.0/10

A GitHub Copilot Autofix-generated commit (4a1b8ce, PR #1218) replaced a safe pattern in Snowflake's jira_issue.yml workflow with direct string expansion, allowing arbitrary command execution on the Actions runner for any unauthenticated GitHub user. This vulnerability was discovered by Wiz's Red Agent and highlights the security risks of AI-generated code in CI/CD pipelines. This incident demonstrates that AI-generated code can introduce critical vulnerabilities, shifting the bottleneck from code generation to code verification. It underscores the urgent need for robust static analysis and security review processes in CI/CD workflows, especially as AI-assisted development becomes more prevalent. The vulnerable workflow fired on issues:opened and interpolated the attacker-controlled title directly into a run: block, enabling arbitrary command execution. The fix removed the safe pattern that used an env: variable and jq --arg to build JSON, replacing it with direct string expansion.

hackernews · galnagli · Aug 17, 14:18 · [Discussion](https://news.ycombinator.com/item?id=49331423)

**Background**: GitHub Copilot Autofix is an AI-powered remediation tool in GitHub Advanced Security that automatically suggests fixes for code scanning alerts. CI/CD workflows, such as GitHub Actions, often use issue titles or other user-controlled data in shell commands, which can lead to command injection if not properly sanitized. Static analysis tools like zizmor can detect such vulnerabilities in GitHub Actions workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cyberkendra.com/2026/08/copilot-autofix-snowflake-jira-github-actions.html">Copilot Autofix Bug Exposed Snowflake's Internal Jira - Cyber Kendra</a></li>
<li><a href="https://github.blog/news-insights/product-news/secure-code-more-than-three-times-faster-with-copilot-autofix/">Found means fixed: Secure code more than three times faster with Copilot Autofix - The GitHub Blog</a></li>
<li><a href="https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning">Responsible use of Copilot Autofix for code scanning - GitHub Docs</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that the mistake is understandable without static analysis, recommending tools like zizmor to catch such issues. One commenter notes that the real lesson is not AI generating insecure code, but that AI lowers the cost of changes while review costs remain high, making verification the new bottleneck. Another commenter criticizes YAML's footguns, preferring XML.

**Tags**: `#AI security`, `#CI/CD`, `#GitHub Actions`, `#vulnerability`, `#code review`

---

<a id="item-3"></a>
## [Anthropic's Claude Watermarking Sparks Ethical and Technical Debate](https://daringfireball.net/2026/08/anthropics_watermark_text_adulteration_in_claude_is_a_perversion_of_writing) ⭐️ 8.0/10

Anthropic announced that future Claude models will generate text with an invisible watermark to help determine if AI was involved in writing, complying with the EU AI Act. This has sparked a critical essay and community debate about the implications for writing integrity and privacy. This watermarking technique affects all users of Claude and potentially other AI providers, raising concerns about privacy, detection accuracy, and the philosophical nature of writing. The debate highlights the tension between regulatory compliance and user autonomy in AI-generated content. The watermark works by altering the randomness source during token selection rather than changing word probabilities, so it does not affect output quality. However, checking for watermarks requires sending the entire text to Anthropic, and it only works for Claude, not other models like ChatGPT or Gemini.

hackernews · ropbear · Aug 16, 21:53 · [Discussion](https://news.ycombinator.com/item?id=49324087)

**Background**: LLM watermarking is a technique to embed a hidden signature in AI-generated text, often by manipulating the random sampling process during token generation. The EU AI Act requires major AI providers to implement such measures to increase transparency. Critics argue that this could compromise the authenticity of writing and create privacy risks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-text-watermark">How Claude 's text watermarking works \ Anthropic</a></li>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/980869/anthropic-claude-watermarks-synthid-text-system">Anthropic explains how Claude ’s invisible text watermarks will work</a></li>
<li><a href="https://www.linkedin.com/pulse/how-llm-text-watermarking-works-where-breaks-kelvin-adungosi-6olgf">How LLM Text Watermarking Works — and Where It Breaks</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed reactions: some criticize the essay's misunderstanding of the gumbel softmax technique, noting it provably does not affect writing quality. Others express concerns about privacy and the need to send text to multiple AI providers for detection, as well as the philosophical objection that watermarking perverts the craft of writing.

**Tags**: `#AI`, `#watermarking`, `#Anthropic`, `#ethics`, `#LLM`

---

<a id="item-4"></a>
## [Apple's ATT Treated Its Own Apps Better; Regulators Demand Equal Treatment](https://www.bundeskartellamt.de/SharedDocs/Meldung/EN/Pressemitteilungen/2026/08_17_2026_Apple_ATTF.html) ⭐️ 8.0/10

Germany's Federal Cartel Office (Bundeskartellamt) has found that Apple's App Tracking Transparency (ATT) gave preferential treatment to Apple's own apps, and regulators are requiring Apple to treat third-party apps equally. Apple's proposed solution may lower privacy standards for all users. This regulatory action could reshape how app tracking permissions are handled, potentially affecting user privacy and competition in the app ecosystem. It highlights the tension between platform control and fair competition, and may set a precedent for other regulators. The Bundeskartellamt's preliminary decision from February 2025 was that Apple abused its market power by giving itself preferential treatment in ATT prompts. Apple's response, as noted in community comments, may involve reducing the burden for third-party apps rather than increasing its own, which could lower overall privacy standards.

hackernews · nyku · Aug 17, 14:07 · [Discussion](https://news.ycombinator.com/item?id=49331222)

**Background**: App Tracking Transparency (ATT) is Apple's framework that requires apps to get user permission before tracking them across other apps and websites. It was introduced in iOS 14.5 and has been controversial, with critics arguing it gives Apple's own apps an unfair advantage. The German regulator's probe is part of broader scrutiny of Apple's practices in Europe.

<details><summary>References</summary>
<ul>
<li><a href="https://www.macrumors.com/2025/12/02/germany-app-tracking-transparency/">Germany Considering Apple's App Tracking Transparency Changes - MacRumors</a></li>
<li><a href="https://developer.apple.com/app-store/user-privacy-and-data-use/">User Privacy and Data Use - App Store - Apple Developer</a></li>
<li><a href="https://apple.gadgethacks.com/news/apple-hit-with-986m-fine-over-privacy-policy-abuse/">Apple Hit with €98.6M Fine Over Privacy Policy Abuse << Apple :: Gadget Hacks</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed feelings: some see the regulator's action as a good step but note that Apple's own apps still have privileged permissions. Others are disappointed that Apple is likely to lower third-party burdens rather than raise its own, potentially reducing overall privacy. A few point out other Apple practices that seem unfair to developers.

**Tags**: `#Apple`, `#privacy`, `#regulation`, `#app tracking`, `#competition`

---

<a id="item-5"></a>
## [AirTag Tracks Rare Book Order to Amazon AI Training Facility](https://simonwillison.net/2026/Aug/17/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-tra/) ⭐️ 8.0/10

404 Media used an Apple AirTag hidden in a rare book to trace a large order of about 1,000 books from Biblio to the VGT3 corner of Amazon's LAS8 facility in Las Vegas, confirming that Amazon is destructively scanning books for AI training data. This investigation provides concrete evidence that major tech companies are acquiring and destroying rare books for AI training, raising serious ethical and legal concerns about copyright infringement and the loss of cultural heritage. It also demonstrates a novel investigative technique using consumer tracking devices to expose corporate data sourcing practices. The book was delivered to the VGT3 corner of the LAS8 facility, where the entrance displayed a logo of a dinosaur with a book. Online forum discussions among Amazon workers confirmed that VGT3 destructively scans large volumes of books, meaning the books are likely destroyed after scanning.

rss · Simon Willison · Aug 17, 15:21

**Background**: For some time, book dealers have reported receiving large, price-insensitive orders from anonymous customers, widely suspected to be AI companies scanning books for training data. In June 2025, Anthropic was sued for using a hydraulic cutting machine to remove pages from books and scanning them with industrial-grade imaging equipment. Apple AirTag uses ultra-wideband technology and Apple's Find My network to track items, and Biblio is a major online marketplace for rare and collectible books.

<details><summary>References</summary>
<ul>
<li><a href="https://wairco.com/blogs/news/apple-airtag-tracking-technology">Apple AirTag Tracking Technology – wairco</a></li>
<li><a href="https://www.linkedin.com/company/biblio">Biblio - Used & Rare Book Marketplace | LinkedIn</a></li>
<li><a href="https://futurism.com/artificial-intelligence/ai-companies-destroying-rare-books">AI Companies Are Buying Antique Books, Ingesting Their Contents to Train Models, and Then Destroying Them at Incredible Scale, Even If Almost No Copies Remain</a></li>

</ul>
</details>

**Tags**: `#AI training data`, `#book scanning`, `#investigative journalism`, `#Amazon`, `#data sourcing`

---

<a id="item-6"></a>
## [Qwen 3.8 27B: Strong Benchmarks but Defaults to Overthinking](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 8.0/10

Qwen 3.8 27B, an Apache 2 licensed 27B parameter vision-capable LLM from Alibaba's Qwen lab, was released on Friday, showing significant benchmark improvements over its predecessor Qwen 3.6 27B and even the closed-weight Qwen 3.7-Plus. However, it defaults to an 'xhigh' reasoning effort, leading to excessive token usage and long generation times. This release is significant because it offers a compact, open-weights model that can run on consumer hardware while delivering strong performance, potentially democratizing access to advanced AI capabilities. The overthinking issue highlights the importance of tuning reasoning effort for practical deployment, especially on local machines. Simon Willison tested the model on a 128GB M5 Max MacBook Pro and an NVIDIA DGX Spark, using LM Studio's 17GB Q4_K_M quantized build. With the default 'xhigh' reasoning effort, a simple prompt to generate an SVG of a pelican riding a bicycle took 21 minutes, using 22,276 reasoning tokens to produce 3,223 output tokens, but the resulting image was notably high quality.

rss · Simon Willison · Aug 16, 22:00

**Background**: Qwen is a family of large language models developed by Alibaba Cloud, many of which are released under the Apache 2.0 license, allowing free use and modification. Vision-language models (VLMs) extend LLMs to process both images and text, enabling tasks like image generation from text prompts. The 'reasoning_effort' parameter allows users to control the depth of reasoning, balancing accuracy and speed.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/qwen3-8-27b">Qwen 3 . 8 27 B - Intelligence, Performance & Price Analysis</a></li>
<li><a href="https://lmstudio.ai/models/qwen/qwen3.8-27b">qwen / qwen 3 . 8 - 27 b • LM Studio</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Qwen`, `#open-source`, `#AI`, `#benchmarks`

---

<a id="item-7"></a>
## [Nvidia Invests $1.5B in SoftBank Data Center Developer for OpenAI](https://techcrunch.com/2026/08/17/nvidia-investing-1-5b-in-softbank-data-center-developer-behind-openai-project/) ⭐️ 8.0/10

Nvidia has invested $1.5 billion in SB Energy, a SoftBank-backed data center developer, to secure its chips as the sole compute infrastructure for OpenAI's Ports-Pike data center near Cincinnati, Ohio. This investment underscores the escalating costs and strategic importance of AI infrastructure, as major players like Nvidia, SoftBank, and OpenAI align to secure compute resources. It also signals Nvidia's commitment to maintaining dominance in AI chip supply for flagship projects. The investment guarantees Nvidia as the sole supplier of compute infrastructure at the Ports-Pike site. Earlier, OpenAI and SoftBank each invested $500 million in SB Energy, which is building a site for the Stargate project.

rss · TechCrunch AI · Aug 17, 15:16

**Background**: The Stargate project is a massive AI infrastructure initiative involving OpenAI, SoftBank, and others, aimed at building data centers to support advanced AI models. SB Energy, a SoftBank subsidiary, is developing data center sites for this project. Nvidia's investment is part of a broader trend of tech giants investing heavily in AI compute infrastructure to meet growing demand.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/17/nvidia-investing-1-5b-in-softbank-data-center-developer-behind-openai-project/">Nvidia investing $1.5B in SoftBank data center ... | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stargate_LLC">Stargate LLC - Wikipedia</a></li>
<li><a href="https://www.theinformation.com/briefings/openai-softbank-invest-1-billion-data-center-developer">OpenAI, SoftBank Invest $1 Billion in Data Center Developer — The Information</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#SoftBank`, `#OpenAI`, `#data center`, `#AI infrastructure`

---

<a id="item-8"></a>
## [Stripe to Acquire AI Gateway Startup OpenRouter for $7B+](https://techcrunch.com/2026/08/16/stripe-will-reportedly-acquire-ai-gateway-startup-openrouter-for-7b/) ⭐️ 8.0/10

Stripe is reportedly acquiring OpenRouter, an AI gateway startup, for over $7 billion. The deal, reported on August 16, 2026, marks one of the largest acquisitions in the AI infrastructure space. This acquisition signals a major consolidation in the AI infrastructure market, validating the importance of AI gateways as critical middleware. It could reshape how developers access and pay for AI models, potentially integrating AI usage with financial infrastructure. OpenRouter's CEO had previously described the startup as 'Stripe for AI,' highlighting its role as a neutral, model-agnostic gateway. The acquisition price of $7B+ reflects the strategic value of controlling the AI API layer, though specific terms and integration plans have not been disclosed.

rss · TechCrunch AI · Aug 16, 20:57

**Background**: An AI gateway is a middleware platform that sits between applications and multiple AI model providers, offering a single API layer for routing requests, managing costs, and ensuring reliability. Stripe is a financial infrastructure platform that enables businesses to accept payments and manage money movement. The acquisition would combine Stripe's financial services with OpenRouter's AI routing capabilities, potentially creating a unified platform for AI usage and billing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=gbzQjJv0F18">ai morning #49 — stripe buys openrouter for $7 billion and... - YouTube</a></li>
<li><a href="https://www.banandre.com/blog/stripe-openrouter-acquisition-api-ai-infrastructure">Stripe Just Bought the AI Router, and Your API... - Banandre</a></li>
<li><a href="https://bug0.com/blog/ai-gateway-vendor-lock-in-testing-2026">AI gateway for testing: how to avoid model vendor lock-in | Bug0</a></li>

</ul>
</details>

**Discussion**: Community discussions highlight both excitement and concern. Some see this as a positive validation of AI gateways, while others worry about the loss of neutrality that OpenRouter provided, potentially leading to vendor lock-in. The 'Stripe for AI' comparison has been widely discussed, with mixed opinions on whether Stripe can maintain OpenRouter's model-agnostic approach.

**Tags**: `#AI`, `#acquisition`, `#Stripe`, `#OpenRouter`, `#fintech`

---

<a id="item-9"></a>
## [PJM's $12B Modeling Mistake: Ratepayers at Risk Again](https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted) ⭐️ 8.0/10

A SemiAnalysis article reveals that a modeling error in PJM's grid planning wasted $12 billion of US ratepayer money, and PJM plans to run an emergency auction without correcting the model, risking further inflated costs. This highlights systemic flaws in US grid planning that can lead to massive financial waste and hinder the transition to clean energy. It underscores the urgent need for regulatory and technical reforms to ensure cost-effective and reliable grid expansion. The error involved capacity estimation in PJM's modeling, which cascaded into billions in unnecessary procurement. PJM's plan to proceed with an emergency auction without fixing the model could repeat the mistake, affecting ratepayers across multiple states.

rss · Semianalysis · Aug 16, 22:27

**Background**: PJM Interconnection is the largest grid operator in the US, managing electricity for 13 states. Grid planning involves forecasting future capacity needs and procuring resources accordingly. Modeling errors can lead to over-procurement, wasting ratepayer money. FERC has recently ordered changes to PJM's interconnection process to address such issues.

<details><summary>References</summary>
<ul>
<li><a href="https://www.elseif.net/stories/12b-of-us-ratepayers-money-wasted-on-a-modeling-mistake-in-pjm-5ff76f3">PJM's model error wasted $12B of ratepayer money and its... — elseif</a></li>
<li><a href="https://insideclimatenews.org/news/05072023/pjm-grid-clean-energy/">Country’s Largest Grid Operator Must Process ... - Inside Climate News</a></li>
<li><a href="https://www.utilitydive.com/news/ferc-pjm-grid-interconnection-queue-christie/754050/">FERC orders changes to PJM ’s grid interconnection process , plus...</a></li>

</ul>
</details>

**Tags**: `#energy`, `#grid`, `#policy`, `#infrastructure`, `#modeling`

---

<a id="item-10"></a>
## [How to Make Sparse Attention and KV Compression Look Good: A Guide to Evaluation Pitfalls](https://www.reddit.com/r/MachineLearning/comments/1vqqqcs/how_to_make_any_sparse_attention_kv_compression/) ⭐️ 8.0/10

A practitioner with years of experience in efficient attention and KV cache compression published a critical guide on X (Twitter) and Reddit, detailing common evaluation pitfalls that make sparse attention and KV compression methods appear more effective than they truly are. The post highlights tactics such as using synthetic tasks with no distractors, avoiding isolating contributions, relying on aggregated metrics, and exploiting saturated benchmarks. This guide is significant because it exposes widespread methodological weaknesses in the evaluation of efficiency-focused LLM techniques, which can mislead the research community and industry practitioners into adopting suboptimal methods. By raising awareness of these pitfalls, it encourages more rigorous benchmarking and honest reporting, ultimately benefiting the broader AI ecosystem. The author lists four main pitfalls: (1) using single-hop retrieval tasks with no distractors, (2) never isolating the contribution of the proposed method (e.g., comparing with different window sizes or block sizes), (3) reporting only aggregated metrics to hide failures on specific subtasks, and (4) exploiting saturated tasks where models already perform well. The post also mentions that LLMs can now generate custom Triton kernels, which can unfairly speed up the proposed method compared to outdated baselines.

reddit · r/MachineLearning · /u/korec1234 · Aug 17, 12:18

**Background**: Sparse attention and KV cache compression are techniques to reduce the computational and memory overhead of transformer-based large language models (LLMs), especially for long contexts. Sparse attention limits attention computation to selected token pairs, reducing complexity from O(n²) to O(n log n) or O(n√n), while KV cache compression reduces the memory footprint of stored key-value pairs. Proper evaluation is crucial because these methods often trade off quality for efficiency, and misleading benchmarks can lead to false confidence in their effectiveness.

<details><summary>References</summary>
<ul>
<li><a href="https://groundy.com/articles/minimax-m3-bets-on-sparse-attention-for-1m-context-does-the-math-hold/">MiniMax M3 Bets on Sparse Attention for 1M Context. Does the Math...</a></li>
<li><a href="https://www.cerebras.ai/blog/compressing-kv-cache-memory-by-half-with-sparse-attention">Compressing KV cache memory by half with sparse attention</a></li>
<li><a href="https://arxiv.org/html/2608.09412">KVDiagnosis: A Diagnostic Benchmark for KV - Cache Compression ...</a></li>

</ul>
</details>

**Tags**: `#sparse attention`, `#KV compression`, `#evaluation`, `#LLM efficiency`, `#research methodology`

---

<a id="item-11"></a>
## [SSOG-Attention: Sub-quadratic Attention via Separable Gaussians](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 8.0/10

SSOG-Attention replaces scaled dot-product attention (SDPA) with a sum of separable Gaussians, reducing complexity from O(N²·d) to O(N·√N·d). It achieves competitive performance on CIFAR-100 and ImageNet while being faster and more memory-efficient. This offers a scalable alternative to standard attention, potentially enabling longer sequences and larger models with lower computational cost. It could influence future efficient attention designs in vision and beyond. The method learns a few Gaussian atoms per head and steers them geometrically based on the query token, avoiding explicit query-key scoring. Experiments show it clearly beats SDPA on small data (CIFAR-100) and matches performance with faster convergence on ImageNet.

reddit · r/MachineLearning · /u/4rtemi5 · Aug 16, 10:06

**Background**: Scaled dot-product attention (SDPA) computes similarity scores between all query-key pairs, leading to O(N²·d) complexity, which becomes prohibitive for long sequences. Efficient attention variants aim to reduce this cost, and SSOG uses separable Gaussians to approximate attention distributions without full pairwise scoring.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/4rtemi5/ssog">GitHub - 4rtemi5/ssog: SSOG- Attention : Near-linear Visual- Attention ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=49318407">SSOG: Near linear Visual- Attention that doesn't score... | Hacker News</a></li>
<li><a href="https://www.openai-hub.com/news/1620/">SSOG- Attention ... - OpenAI Hub</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion likely includes technical feedback on the approach, comparisons with other efficient attention methods, and questions about scalability and implementation details. The Reddit thread may have similar debates, but no specific comments were provided.

**Tags**: `#attention`, `#efficiency`, `#machine learning`, `#computer vision`, `#scalability`

---

<a id="item-12"></a>
## [OpenAI Previews Ultrafast Mode for GPT-5.6 Sol, 14x Faster](https://t.me/zaihuapd/43228) ⭐️ 8.0/10

OpenAI has previewed a new Ultrafast mode for its flagship GPT-5.6 Sol model, delivering up to 14x faster inference and up to 750 output tokens per second. The service is powered by Cerebras and is initially available to select customers via the OpenAI API. This performance leap could make the most intelligent AI models practical for time-sensitive applications like fault response, financial research, customer service, and e-commerce. It also highlights the growing role of specialized hardware providers like Cerebras in the AI inference landscape. The Ultrafast mode is currently in limited preview, with OpenAI planning to expand access as compute capacity grows. The service leverages Cerebras's wafer-scale engine technology, which reduces latency and interconnect bottlenecks compared to traditional GPU clusters.

telegram · zaihuapd · Aug 17, 00:47

**Background**: GPT-5.6 is a family of large language models released by OpenAI in July 2026, with Sol being the most capable variant. Cerebras Systems is a company known for its wafer-scale processors, which are the largest AI semiconductors ever built, and it has signed a deal with OpenAI to support inference workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode : GPT-5.6 Sol at up to 14X the... | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6_Sol">GPT-5.6 Sol</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-5.6`, `#AI inference`, `#performance`, `#Cerebras`

---

<a id="item-13"></a>
## [Meituan Executive Reflects on Costly 'Shrimp Farming' AI Initiative](https://weibo.com/1642634100/RdM6hhhpW) ⭐️ 8.0/10

Wang Puzhong, CEO of Meituan's core local commerce business, publicly reflected on the company's internal AI transformation, revealing that the 'shrimp farming' campaign from February to March incurred daily token costs of tens of millions of yuan and produced errors that disrupted real operations. He noted that starting in April, business units established AI organizations, and by July, AI had initially run through internal product processes and generated value. This candid reflection highlights the real-world challenges of enterprise AI adoption, including high token costs and misalignment with business goals, which are relevant to many companies investing heavily in AI. It underscores the need for systematic integration of business, organization, and technology, rather than indiscriminate AI deployment. Wang identified four mismatches—cognition, efficiency, scenario, and assessment—that hinder AI implementation. He also mentioned that from June to July, a horse-racing mechanism clarified that AI transformation is a systematic project involving business, organization, and technology, and by July, AI had initially created value in internal product processes.

telegram · zaihuapd · Aug 17, 02:09

**Background**: Meituan, a leading Chinese local services platform, has been aggressively pursuing AI integration, including launching an AI Transformation division and deploying models like LongCat across its operations. The 'shrimp farming' campaign likely refers to a company-wide push to use AI tools indiscriminately, leading to excessive token consumption and operational disruptions. This reflection comes amid broader industry discussions about the practical difficulties of translating AI investment into measurable business value.

<details><summary>References</summary>
<ul>
<li><a href="https://www.binance.com/en/square/post/08-12-2026-meituan-s-wang-puzhong-says-it-will-not-open-offline-pharmacies-focuses-on-ai-support-for-drug-retailers-354796956208690">Meituan 's Wang Puzhong Says It... | Binance News on Binance Square</a></li>
<li><a href="https://chinabizinsider.com/meituan-bets-on-physical-ai-infrastructure-play-sidestepping-the-model-arms-race/">Meituan Launches AI Unit, Targets Agent Infrastructure</a></li>
<li><a href="https://technode.com/2025/02/11/meituan-doubles-down-on-ai-in-2025-strategic-plan/">Meituan doubles down on AI in 2025 strategic plan · TechNode</a></li>

</ul>
</details>

**Tags**: `#AI adoption`, `#enterprise AI`, `#cost management`, `#Meituan`, `#digital transformation`

---

<a id="item-14"></a>
## [Unitree Teases 'Superman' Humanoid Robot with 2-Meter Jump](https://m.weibo.cn/detail/5332901463070926) ⭐️ 8.0/10

Unitree Robotics has released a teaser for a new humanoid robot nicknamed 'Superman', claiming it can perform a standing jump of 2 meters and reach a top speed of 12.66 m/s (with a leg length of 0.85 meters), surpassing human records in both vertical jump and sprinting. The company states the entire robot was developed in just over three months, with further improvements expected in the coming months. This announcement is significant as it showcases a humanoid robot achieving athletic feats beyond human capabilities, potentially pushing the boundaries of robotics in agility and speed. It could influence the development of humanoid robots for applications such as search-and-rescue, industrial inspection, and entertainment, while also intensifying competition among robotics companies. The teaser video reportedly shows the robot jumping 2 meters in place and reaching a top speed of 12.66 m/s, with a leg length of 0.85 meters. The robot is described as a new whole-body design, and the company notes that it has significant room for improvement in the coming months, suggesting this is an early prototype.

telegram · zaihuapd · Aug 17, 07:12

**Background**: Unitree Robotics is a Chinese company known for developing legged robots, including the H1 and G1 humanoid platforms. Humanoid robots are designed to mimic human form and movement, and achieving dynamic feats like jumping and high-speed running requires advanced actuators, control algorithms, and energy systems. This teaser follows a trend of humanoid robots demonstrating athletic abilities, such as Boston Dynamics' Atlas, but Unitree's claims of surpassing human records are notable.

<details><summary>References</summary>
<ul>
<li><a href="https://mezha.net/eng/bukvy/b94d3966_unitree_robotics_unveils/">Unitree Robotics Unveils Superman Robot That Jumps... - #Mezha</a></li>
<li><a href="https://cryptopanic.com/news/33222781/Unitree-Releases-30-Second-Video-of-Humanoid-Robot-Jumping-2-Meters">Unitree Releases 30-Second Video of Humanoid Robot Jumping ...</a></li>
<li><a href="https://www.humanoidsdaily.com/news/unitree-unveils-superman-robot-claims-to-shatter-human-speed-and-jump-records">Unitree Unveils "Superman" Robot , Claims to... | Humanoids Daily</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#humanoid robot`, `#Unitree`, `#announcement`

---