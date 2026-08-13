---
layout: default
title: "Horizon Summary: 2026-08-13 (EN)"
date: 2026-08-13
lang: en
---

> From 82 items, 14 important content pieces were selected

---

1. [Tailscale Uncovers 16-Year-Old SQLite WAL-Reset Race Condition](#item-1) ⭐️ 9.0/10
2. [Qwen3.8-2.4T-A95B: Massive MoE Model Nears Frontier Performance](#item-2) ⭐️ 9.0/10
3. [Researchers Steal Hidden Reasoning from Major LLM APIs](#item-3) ⭐️ 9.0/10
4. [uBlock Origin Stops Blocking Facebook Ads](#item-4) ⭐️ 8.0/10
5. [xAI Releases Grok 4.6 with Benchmark Gains and API Changes](#item-5) ⭐️ 8.0/10
6. [HTML over WebSockets: Real-Time SPAs with Minimal JavaScript](#item-6) ⭐️ 8.0/10
7. [Chrome's Tiny JPEG Rendering Difference Explained](#item-7) ⭐️ 8.0/10
8. [Twitch auto-enrolls streamers in Amazon AI training, opt-out only](#item-8) ⭐️ 8.0/10
9. [AI Pioneers Advocate for Open Development Amid Safety Concerns](#item-9) ⭐️ 8.0/10
10. [General Catalyst leads $1.1B round into 2-month-old River AI](#item-10) ⭐️ 8.0/10
11. [Anthropic's Unreleased Model Advances on Riemann Hypothesis](#item-11) ⭐️ 8.0/10
12. [Adam's Coordinate Adaptivity Breaks Rotation Invariance and Low-Rank Bias](#item-12) ⭐️ 8.0/10
13. [Decoupled Descent: Enforcing Exact Train-Test Error Tracking via AMP Corrections](#item-13) ⭐️ 8.0/10
14. [DeepMind's SL2T Sign Language-to-Text Model Debuts on Pixel 11](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Tailscale Uncovers 16-Year-Old SQLite WAL-Reset Race Condition](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 9.0/10

Tailscale detailed the discovery and fix of a 16-year-old SQLite WAL-reset race condition that could cause data corruption. The bug was isolated with a custom SQLite VFS shim funded by Tailscale and fixed by SQLite maintainers. This bug affected a widely-used embedded database, and its discovery highlights the value of open-source funding and modern deterministic concurrency testing. The collaborative debugging effort underscores the importance of investing in correctness for critical infrastructure. The bug is a race condition in WAL checkpointing that could corrupt data files, and SQLite developers estimate it existed for at least 16 years. Tailscale funded the development of a custom SQLite VFS shim that helped isolate the race condition almost immediately, and the fix also uncovered a second stale expression index bug.

hackernews · ropbear · Aug 12, 14:22 · [Discussion](https://news.ycombinator.com/item?id=49272832)

**Background**: SQLite is a widely-used embedded database that supports Write-Ahead Logging (WAL) for improved concurrency and durability. The WAL-reset bug is a race condition that occurs during checkpointing, where the WAL file is reset, potentially leading to data corruption. Deterministic concurrency testing is a methodology that aims to reproduce scheduling sequences to find such races, which traditional testing may miss.

<details><summary>References</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL - Reset bug</a></li>
<li><a href="https://news.ycombinator.com/item?id=49272832">Tracking down the 16-year-old WAL - reset SQLite bug | Hacker News</a></li>
<li><a href="https://www.youngju.dev/blog/2026-07-16-sqlite-wal-reset-bug.en">The SQLite WAL - Reset Bug: A Data Corruption Race That Hid for 15...</a></li>

</ul>
</details>

**Discussion**: The Hacker News community praised Tailscale for funding open-source development and engaging with SQLite maintainers, with some noting the value of deterministic concurrency testing. Others expressed skepticism about SQLite's production readiness, suggesting that such bugs might push companies toward Postgres, while some appreciated the detailed write-up and the single-writer design clarification.

**Tags**: `#SQLite`, `#bug`, `#concurrency`, `#open-source`, `#debugging`

---

<a id="item-2"></a>
## [Qwen3.8-2.4T-A95B: Massive MoE Model Nears Frontier Performance](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Alibaba released Qwen3.8-2.4T-A95B, an open-weight MoE model with 2.4 trillion total parameters and 95 billion active parameters, claiming performance near Opus 4.5/4.8 and Fable 5. The model is available in BF16 and FP8 formats, with a 1-bit quantized version at 397GB. This release brings near-frontier AI capabilities to the open ecosystem, potentially democratizing access to top-tier model performance. It intensifies competition among open-weight models and may influence hardware requirements and deployment strategies for large-scale MoE models. The model uses a fine-grained MoE architecture with hybrid full and linear attention, supporting a context length of up to 1M tokens in the official Qwen3.8-Max version, though the open-weight version lacks vision support and built-in tools. The BF16 version requires about 4.9TB of storage, while the 1-bit quantized version is 397GB, making it feasible for high-end consumer hardware.

hackernews · Philpax · Aug 12, 15:01 · [Discussion](https://news.ycombinator.com/item?id=49273478)

**Background**: Mixture-of-Experts (MoE) models activate only a subset of parameters per token, enabling large total parameter counts with efficient inference. Quantization techniques like FP8 and 1-bit reduce memory footprint and computational cost, making large models more accessible. Qwen is a series of open-weight models from Alibaba, and this release is part of a trend toward open-weight models rivaling proprietary frontier models.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/">Serve Qwen3.8-2.4T-A95B, a 2.4T-Parameter Model, with Configurable ...</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.8-2.4t-a95b">Qwen3.8 2.4T A95B - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://www.baseten.co/blog/fp8-efficient-model-inference-with-8-bit-floating-point-numbers/">FP8: Efficient model inference with 8-bit floating point numbers</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the model's size and serving challenges, noting that BF16 and FP8 releases are harder to serve than competitors like Kimi k3, and that QAT on q4 is not provided, requiring external quantization efforts. Some express excitement about the 1-bit quantized version enabling near-Opus performance on consumer hardware, while others lament the lack of vision support and 1M context in the open-weight version. There is also speculation about future hardware cost reductions and comparisons with DeepSeek's upcoming models.

**Tags**: `#AI/ML`, `#Large Language Models`, `#MoE`, `#Qwen`, `#Model Release`

---

<a id="item-3"></a>
## [Researchers Steal Hidden Reasoning from Major LLM APIs](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/) ⭐️ 9.0/10

Researchers demonstrated a method to recover hidden chain-of-thought reasoning from proprietary LLM APIs (OpenAI, Anthropic, Google) by replaying encrypted reasoning blocks into weaker sibling models and jailbreaking them. The attack has been acknowledged and fixed by all providers. This exposes a significant security flaw in how major AI providers protect their internal reasoning, potentially allowing extraction of sensitive chain-of-thought data. It highlights the need for stronger encryption and isolation of reasoning traces, impacting AI safety and security practices. The attack exploited the fact that models in the same family share the same encryption key, allowing encrypted blocks to be replayed across models. Claude Haiku 4.5 was the easiest to attack, using a prompt to transcribe the reasoning verbatim, and the paper includes extracted reasoning traces in its appendix.

rss · Simon Willison · Aug 11, 22:40

**Background**: Proprietary LLM APIs often return encrypted chain-of-thought blocks to avoid exposing raw reasoning, but these blocks are portable and can be replayed. The paper demonstrates that weaker sibling models, with fewer safety guardrails, can be jailbroken to decode these blocks, revealing the stronger model's hidden reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2608.09867">Stealing Reasoning Traces from Proprietary LLM APIs - arXiv.org</a></li>
<li><a href="https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://cybersecuritynews.com/top-ai-models-apis-flaw-exposes-hidden-reasoning/">OpenAI, Anthropic, and Google LLM APIs vulnerability Exposes ...</a></li>

</ul>
</details>

**Tags**: `#LLM security`, `#chain-of-thought`, `#AI safety`, `#proprietary APIs`, `#research`

---

<a id="item-4"></a>
## [uBlock Origin Stops Blocking Facebook Ads](https://digitalescapetools.com/2026/08/ublock-origin-stops-chasing-facebook-ads.html) ⭐️ 8.0/10

uBlock Origin's volunteer team announced it will no longer attempt to block ads on Facebook, citing the platform's constantly changing anti-ad-blocking techniques. This decision was made public around August 2026, following years of escalating technical challenges. This marks a significant moment in the ad-blocking arms race, as one of the most popular ad blockers concedes defeat against a major platform. It highlights the increasing difficulty for open-source tools to keep up with sophisticated ad obfuscation, potentially impacting user privacy and ad experience for millions. Facebook uses techniques such as splitting words like 'ad' into single-letter spans with random class names, nesting divs eight layers deep, and using data attributes instead of plain text to evade CSS selectors. These methods make it nearly impossible for filter lists to keep up, leading uBlock Origin to focus efforts elsewhere.

hackernews · Markoff · Aug 12, 11:28 · [Discussion](https://news.ycombinator.com/item?id=49270726)

**Background**: Ad blockers like uBlock Origin rely on filter lists that identify and hide ad elements based on selectors. Facebook has long employed obfuscation tactics to make its ads harder to detect, creating a cat-and-mouse game. The Meta ad delivery system uses machine learning and auctions to serve ads, further complicating blocking efforts.

<details><summary>References</summary>
<ul>
<li><a href="https://digitalescapetools.com/2026/08/ublock-origin-stops-chasing-facebook-ads.html">uBlock Origin Is Giving Up the Fight to Keep Ads Off Facebook</a></li>
<li><a href="https://www.neowin.net/news/facebook-ads-are-so-hard-to-block-that-ublock-origin-stopped-filtering-them/">Facebook ads are so hard to block that uBlock Origin ... - Neowin</a></li>
<li><a href="https://www.dylanpaulus.com/posts/how-fb-avoids-adblockers">How Facebook Avoids Ad Blockers - Dylan Paulus</a></li>

</ul>
</details>

**Discussion**: Community comments express frustration with Facebook's tactics, with some suggesting that ads are a form of 'brain malware' and that users should leave the platform. Others predict the arms race will eventually lead to computer vision-based ad blocking, while some note the accessibility issues caused by Facebook's obfuscated markup.

**Tags**: `#ad-blocking`, `#privacy`, `#Facebook`, `#uBlock Origin`, `#arms race`

---

<a id="item-5"></a>
## [xAI Releases Grok 4.6 with Benchmark Gains and API Changes](https://x.ai/news/grok-4-6) ⭐️ 8.0/10

xAI has released Grok 4.6, a new AI model that shows a 5-point improvement over Grok 4.5 on the Artificial Analysis Intelligence Index, bringing it back to the frontier alongside OpenAI and behind only Anthropic. The model is available via the xAI API, Grok Build, Cursor, OpenRouter, Vercel, and Cloudflare, with a 500,000-token context window. This release signals xAI's return to the competitive frontier of AI models, intensifying competition among major labs. The improvements in coding and agentic behavior, along with a large context window, could make Grok 4.6 a strong choice for developers and enterprises, potentially shifting market dynamics. Grok 4.6 is trained on a wide range of agentic RL tasks, including knowledge work, general coding, and domain-specific environments for kernel optimization and web tasks. The model shows stronger post-training, coding and agent behavior, speed and token efficiency, and one-shot UI or 3D code generation, but no verified benchmark has been released by xAI itself.

hackernews · iLuddite · Aug 12, 15:32 · [Discussion](https://news.ycombinator.com/item?id=49274027)

**Background**: Grok is a series of large language models developed by xAI, led by Elon Musk. The Artificial Analysis Intelligence Index is a third-party composite score that provides a neutral cross-model comparison. Grok 4.6's release comes just over a month after Grok 4.5, and it gains 5 points on the index, or +23 points compared to Grok 4.3.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis">Grok 4 . 6 returns SpaceXAI to the intelligence frontier and leads on cost...</a></li>
<li><a href="https://x.ai/news/grok-4-6">Introducing Grok 4.6 | SpaceXAI</a></li>
<li><a href="https://kingy.ai/blog/grok-4-6-price-benchmarks-api-cursor-context-window/">Grok 4.6: Price, Benchmarks, 500K Context & Access</a></li>

</ul>
</details>

**Discussion**: Community comments highlight concerns about the SpaceXAI API adding a default system prompt that overrides user instructions, causing refusals to discuss system prompts. Some users question the rapid benchmark improvements across labs, suspecting benchmark hacking or distillation, while others praise Grok's concise and direct style compared to competitors. Overall sentiment is mixed, with some seeing Grok as a healthy competitor but noting its polarizing reputation.

**Tags**: `#AI`, `#Grok`, `#xAI`, `#LLM`, `#benchmarks`

---

<a id="item-6"></a>
## [HTML over WebSockets: Real-Time SPAs with Minimal JavaScript](https://en.andros.dev/blog/ef4968f5/html-over-websockets-real-time-spas-with-barely-any-javascript/) ⭐️ 8.0/10

The article advocates building real-time single-page applications (SPAs) by sending HTML over WebSockets, a technique popularized by Phoenix LiveView, which allows server-side rendering with minimal client-side JavaScript. It argues this approach simplifies development by using a single language and eliminating the need for separate API contracts. This approach could shift how developers build real-time web applications, reducing front-end complexity and potentially lowering development costs. It challenges the dominance of JavaScript-heavy frameworks and offers an alternative for teams that prefer server-centric development. The article highlights that WebSockets provide bidirectional, low-latency communication, making them suitable for chat, collaboration, and games, whereas Server-Sent Events (SSE) are simpler and cheaper for one-way server pushes. It also notes that modern browsers multiplex HTTP requests over a single TCP connection, so latency is similar for many use cases.

hackernews · redbell · Aug 12, 16:51 · [Discussion](https://news.ycombinator.com/item?id=49275335)

**Background**: Phoenix LiveView is a real-time web framework feature in the Elixir Phoenix framework that enables rich, real-time user experiences with server-rendered HTML. It begins as a regular HTTP request and then upgrades to a stateful view, automatically pushing updates to the client. The HTML-over-WebSockets technique extends this idea to general web development, allowing server-side generation of HTML fragments that are sent over WebSockets and inserted into the DOM.

<details><summary>References</summary>
<ul>
<li><a href="https://testdriven.io/blog/html-over-websockets/">HTML Over WebSockets | TestDriven.io</a></li>
<li><a href="https://alistapart.com/article/the-future-of-web-software-is-html-over-websockets/">The Future of Web Software Is HTML-over-WebSockets – A List Apart</a></li>
<li><a href="https://hexdocs.pm/phoenix_live_view/Phoenix.LiveView.html">Phoenix.LiveView — Phoenix LiveView v1.2.9</a></li>

</ul>
</details>

**Discussion**: Community comments show a mix of support and critique. Some users point out that the technique has historical roots, such as Chris McCord's earlier work on Rails' Sync, and that context matters when choosing between WebSockets and SSE. Others highlight new browser APIs like declarative partial updates that could enhance this approach, while some link to a critical response questioning the technique's merits.

**Tags**: `#WebSockets`, `#Real-time`, `#SPA`, `#JavaScript`, `#Server-Sent Events`

---

<a id="item-7"></a>
## [Chrome's Tiny JPEG Rendering Difference Explained](https://guillaumetech.github.io/posts/jpg-scaling-chrome/) ⭐️ 8.0/10

An article explains that Chrome renders tiny JPEGs differently from other browsers due to partial decompression, and recommends using appropriate image formats and resolutions. The issue has gained significant community attention, with 321 points and 66 comments. This matters because it highlights a subtle but impactful browser rendering difference that can affect web developers' image display consistency across browsers. Understanding this can help developers avoid visual glitches and improve cross-browser compatibility. The article advises against using JPEG for icons and recommends using images at an appropriate resolution for their display size. Firefox is actively working on lower-scale decompression, as referenced in Bugzilla bug 2033250.

hackernews · gutechh · Aug 12, 14:00 · [Discussion](https://news.ycombinator.com/item?id=49272549)

**Background**: JPEG compression involves converting images to YCbCr, subsampling color, and applying frequency transforms, then quantizing and compressing. When decoding, browsers may partially decompress to speed up rendering, which can lead to different results for very small images. Chrome and Firefox also use different scaling algorithms, contributing to visual differences.

<details><summary>References</summary>
<ul>
<li><a href="https://cgjennings.ca/articles/jpeg-compression/">How JPEG works - Home (Christopher G. Jennings)</a></li>
<li><a href="https://stackoverflow.com/questions/63502778/blurry-downscaled-images-in-the-chrome-84">Blurry downscaled images in the Chrome 84 - Stack Overflow</a></li>

</ul>
</details>

**Discussion**: Commenters note that the same issue occurs with PNGs, and that Chrome's optimization broke icons in Electron apps. Some point out that using appropriate image resolution is more important than format, while others mention Firefox's ongoing work and differing scaling algorithms.

**Tags**: `#web development`, `#browser rendering`, `#image processing`, `#Chrome`, `#Firefox`

---

<a id="item-8"></a>
## [Twitch auto-enrolls streamers in Amazon AI training, opt-out only](https://techcrunch.com/2026/08/12/amazon-will-train-on-twitch-streamers-content-by-default-unless-they-opt-out/) ⭐️ 8.0/10

Amazon-owned Twitch has announced that it will automatically enroll all streamers in AI training programs, using their content to train Amazon's AI models by default. Streamers who do not want their content used must manually opt out via a settings toggle. This policy shift is significant because it establishes a default opt-out approach for AI training data, which could set a precedent for other platforms. It directly impacts millions of content creators, raising ethical concerns about consent and the balance between platform innovation and user rights. Twitch CPO Mike Minton admitted on a livestream that the opt-out design was chosen because 'if this was opt-in, nobody would opt in.' The opt-out setting is available in streamer settings, but some AI features may still use content even after opting out, according to reports.

rss · TechCrunch AI · Aug 12, 20:10

**Background**: Twitch is a live-streaming platform owned by Amazon, and Amazon has been developing AI models that require large amounts of training data. This move follows a broader industry trend where platforms like Meta and Google have faced backlash for using user content to train AI without explicit consent. The default opt-out approach contrasts with opt-in models, which require active user consent before data usage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.windowscentral.com/artificial-intelligence/if-it-was-opt-in-nobody-would-opt-in-cringe-twitch-cpo-admits-everyone-hates-its-ai-training-feature-doesnt-care">"If it was opt in ... nobody would opt-in." Twitch CPO ... | Windows Ce...</a></li>
<li><a href="https://www.tubefilter.com/2026/08/12/twitch-amazon-llm-scraping-opt-in-mike-minton/">"If it was opt-in, nobody would opt in": Twitch auto-enrolls... - Tube...</a></li>
<li><a href="https://insider-gaming.com/twitch-ai-training-opt-out-setting/">Twitch Adds AI Training Opt - Out Setting for Streamers - Insider Gaming</a></li>

</ul>
</details>

**Discussion**: Community reactions have been largely negative, with many streamers expressing anger and frustration over the default opt-out policy. Critics argue that Twitch is prioritizing its own interests over user consent, and some have compared the move unfavorably to other platforms like YouTube, which also faces similar criticism.

**Tags**: `#AI training`, `#Twitch`, `#Amazon`, `#privacy`, `#content policy`

---

<a id="item-9"></a>
## [AI Pioneers Advocate for Open Development Amid Safety Concerns](https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/) ⭐️ 8.0/10

At the Ai4 conference, Geoffrey Hinton, Fei-Fei Li, and Andrew Ng argued for maintaining open AI development despite rising safety concerns and geopolitical competition. They debated regulation, open source access, and how the U.S. can compete with China's advances. This discussion is significant as it brings together three top AI pioneers to address critical policy issues, potentially influencing regulation and industry practices. Their stance on openness could shape the future of AI development and international competition. The conference, Ai4, is described as the world's largest gathering of AI leaders in business, held in Las Vegas. The debate covered regulation, open source access, and U.S. competitiveness against China's AI progress.

rss · TechCrunch AI · Aug 12, 17:51

**Background**: AI safety is an interdisciplinary field focused on preventing accidents, misuse, or harmful consequences from AI systems. Open-source AI development has been a topic of debate, with concerns about potential misuse versus the benefits of transparency and collaboration. The U.S. and China are in a competitive race for AI dominance, making these discussions timely.

<details><summary>References</summary>
<ul>
<li><a href="https://ai4.io/">Ai4 2026</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_safety">AI safety - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-source_artificial_intelligence">Open-source artificial intelligence - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#open source`, `#regulation`, `#Geoffrey Hinton`, `#Fei-Fei Li`

---

<a id="item-10"></a>
## [General Catalyst leads $1.1B round into 2-month-old River AI](https://techcrunch.com/2026/08/11/general-catalyst-leads-1-1b-round-into-2-month-old-river-ai/) ⭐️ 8.0/10

River AI, a startup founded by xAI co-founder Igor Babuschkin, has raised $1.1 billion in a funding round led by General Catalyst, just two months after its inception. The company aims to develop personal agents. This massive early-stage investment signals strong investor confidence in the personal agent space, a key trend in AI. It also highlights the continued influence of top AI talent like Babuschkin, potentially accelerating competition among AI startups. The funding round was led by General Catalyst, though the exact valuation and other investors were not disclosed. River AI is focused on building personal agents, which are AI systems that can autonomously perform tasks on behalf of users.

rss · TechCrunch AI · Aug 11, 17:41

**Background**: Igor Babuschkin co-founded xAI with Elon Musk in 2023 but left the company in August 2025 to start his own venture. Personal agents are a class of AI agents that know user context, use tools, and take actions autonomously, such as booking meetings or sending emails. The AI agent market is rapidly growing, with major investments flowing into startups developing these technologies.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2025/08/13/co-founder-of-elon-musks-xai-departs-the-company/">Co - founder of Elon Musk's xAI departs the company | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://www.ego.app/blog/what-is-a-personal-agent/">What is a personal agent? Everything to know in 2026</a></li>

</ul>
</details>

**Tags**: `#AI`, `#funding`, `#startups`, `#personal agents`

---

<a id="item-11"></a>
## [Anthropic's Unreleased Model Advances on Riemann Hypothesis](https://techcrunch.com/2026/08/11/an-unreleased-anthropic-model-made-progress-on-one-of-maths-biggest-unsolved-problems/) ⭐️ 8.0/10

Anthropic's unreleased AI model reportedly made notable progress on the Riemann hypothesis, a famous unsolved problem in mathematics, demonstrating advanced reasoning capabilities. The model did not solve the problem but achieved more than expected. This development highlights the growing capability of AI models in tackling complex mathematical problems, potentially accelerating research in number theory and related fields. It also signals that frontier AI models are approaching human-level reasoning in specialized domains, which could have broad implications for scientific discovery. The Riemann hypothesis, proposed by Bernhard Riemann, concerns the distribution of nontrivial zeros of the Riemann zeta function, all of which are conjectured to lie on the critical line with real part 1/2. It is one of the Millennium Prize Problems, with a $1 million reward for a proof. The specific progress made by Anthropic's model has not been disclosed in detail.

rss · TechCrunch AI · Aug 11, 16:25

**Background**: The Riemann hypothesis is a central conjecture in analytic number theory, implying results about the distribution of prime numbers. Despite overwhelming numerical evidence, no proof has been found in over 150 years. Anthropic is an AI safety company known for its Claude series of large language models, which are trained using a constitution-based approach to improve ethical compliance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#mathematics`, `#Anthropic`, `#research`, `#Riemann hypothesis`

---

<a id="item-12"></a>
## [Adam's Coordinate Adaptivity Breaks Rotation Invariance and Low-Rank Bias](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 8.0/10

A new study shows that Adam's per-coordinate second moment breaks rotation invariance in matrix factorization, causing it to lose gradient descent's implicit low-rank bias in matrix sensing. Nine update rules were tested, revealing that optimizers with shared scaling (GD, Muon, Shampoo) preserve the bias, while coordinate-wise ones (Adam, RMSProp, Lion) lose it. This finding connects optimizer design to implicit bias, offering a new criterion for choosing optimizers in low-rank recovery tasks. It could guide the development of optimizers that retain beneficial inductive biases, impacting fields like deep learning and compressed sensing. The study used a one-parameter family to transition Adam's denominator from per-coordinate to a shared scalar, showing recovery improves monotonically, indicating anisotropy is the culprit. Muon's behavior was unexpected: it is exact on truly low-rank targets but degrades with spectral tail, ceding to GD near 4% tail energy. A caveat: the 43-44% error reduction on hyperspectral data relies on a train-only learning rate rule that assigns Adam the worst rate; with optimal rates, the gap narrows.

reddit · r/MachineLearning · /u/EtherealGlyph · Aug 12, 16:39

**Background**: In matrix factorization, the loss is invariant to rotations of the factors, and gradient descent respects this symmetry. Adam's per-coordinate adaptivity breaks this invariance, affecting its implicit bias in underdetermined problems like matrix sensing. Implicit bias refers to the tendency of optimization algorithms to converge to solutions with certain properties (e.g., low rank) even without explicit regularization.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/papers/2608.05136">Paper page - The Loss Does Not See the Basis, but Adam Does</a></li>
<li><a href="https://arxiv.org/abs/2008.12091">[2008.12091] Limitations of Implicit Bias in Matrix Sensing ... Limitations of Implicit Bias in Matrix Sensing ... - NASA/ADS [PDF] Limitations of Implicit Bias in Matrix Sensing ... [2008.12091] Limitations of Implicit Bias in Matrix Sensing ... Implicit Regularization in Matrix Sensing via Mirror Descent Gradient descent for deep matrix factorization: Dynamics and ...</a></li>

</ul>
</details>

**Tags**: `#optimization`, `#deep learning`, `#implicit bias`, `#matrix factorization`, `#Adam`

---

<a id="item-13"></a>
## [Decoupled Descent: Enforcing Exact Train-Test Error Tracking via AMP Corrections](https://www.reddit.com/r/MachineLearning/comments/1vlu1se/decoupled_descent_enforcing_exact_traintest_error/) ⭐️ 8.0/10

The paper introduces Decoupled Descent (DD), a novel training method that uses approximate message passing (AMP) corrections to enforce that the training error asymptotically equals the test error at each parameter iterate. The author demonstrates its effectiveness on a stylized Gaussian mixture model with a two-layer network, showing improved train-test error tracking compared to standard gradient descent. This work addresses a fundamental issue in deep learning where training error decreases but test error stagnates or worsens, a phenomenon attributed to data reuse bias. By providing a theoretical guarantee of train-test error tracking, Decoupled Descent could enable better model selection, optimal stopping, and hyperparameter tuning, potentially improving generalization in practical applications. The method is based on high-dimensional statistical theory, specifically approximate message passing (AMP), and is currently a theoretical paper with experiments on a stylized Gaussian mixture model. The author notes that scaling to very large models is a future direction, and plans to release a PyTorch-compatible package.

reddit · r/MachineLearning · /u/mlovik1 · Aug 11, 21:06

**Background**: Approximate message passing (AMP) is a class of iterative algorithms used in high-dimensional statistical problems, such as compressed sensing, that provide precise asymptotic guarantees via state evolution. In deep learning, the gap between training and test error is often due to overfitting, where the model memorizes training data but fails to generalize. This paper leverages AMP to correct the training dynamics, ensuring that the training error tracks the test error, which is a novel application of AMP to neural network training.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2201.07487">A Concise Tutorial on Approximate Message Passing A unifying tutorial on Approximate Message Passing Lecture 19: Approximate message passing algorithms Approximate Message Passing Tutorial - GitHub Pages A unifying tutorial on Approximate Message Passing Message-passing algorithms for compressed sensing Fast, Robust Approximate Message Passing | Proceedings of the ...</a></li>
<li><a href="https://arxiv.org/abs/2105.02180">A unifying tutorial on Approximate Message Passing Lecture 19: Approximate message passing algorithms Approximate Message Passing Tutorial - GitHub Pages A unifying tutorial on Approximate Message Passing Message-passing algorithms for compressed sensing Fast, Robust Approximate Message Passing | Proceedings of the ...</a></li>
<li><a href="https://www.stat.berkeley.edu/~songmei/Teaching/STAT260_Spring2021/Lecture_notes/scribe_lecture19.pdf">Lecture 19: Approximate message passing algorithms</a></li>

</ul>
</details>

**Discussion**: The Reddit post is by the author, inviting discussion. The community has not yet provided comments, but the author is open to questions and suggestions for the future PyTorch package.

**Tags**: `#machine learning`, `#optimization`, `#generalization`, `#approximate message passing`, `#theory`

---

<a id="item-14"></a>
## [DeepMind's SL2T Sign Language-to-Text Model Debuts on Pixel 11](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 8.0/10

Google DeepMind has released SL2T, a massively multilingual sign language-to-text model, and integrated it into consumer products for the first time. It is now available on Pixel 11's Gboard and Live Transcribe, supporting American Sign Language (ASL) to English translation. This marks a significant step in making sign language AI accessible to everyday users, potentially improving communication for Deaf and hard-of-hearing individuals. It sets a precedent for integrating such models into mainstream devices, which could drive further adoption and development in accessibility technology. The model was trained on over 100,000 hours of data across more than 50 sign languages, and it achieves a zero-shot score of 70 BLEURT on the FLEURS-ASL benchmark, far exceeding previous records. To protect privacy, it processes only hand and body pose keypoints, not raw video.

telegram · zaihuapd · Aug 13, 08:55

**Background**: Sign language translation is challenging due to the complexity and diversity of sign languages, which are distinct from spoken languages. FLEURS-ASL is a benchmark designed to evaluate ASL translation, and pose keypoints are a privacy-preserving way to represent human movement without storing raw video. DeepMind's SL2T leverages these keypoints to enable on-device translation.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/">Putting sign language AI into users’ hands — Google DeepMind</a></li>
<li><a href="https://datanorth.ai/news/google-deepmind-releases-sl2t">Google DeepMind releases SL 2 T sign language AI - DataNorth</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/google-sign-language-model-body-landmarks">Google's new model turns sign language into text for web searches</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Sign Language`, `#DeepMind`, `#Accessibility`, `#Machine Learning`

---