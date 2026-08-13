---
layout: default
title: "Horizon Summary: 2026-08-13 (EN)"
date: 2026-08-13
lang: en
---

> From 83 items, 15 important content pieces were selected

---

1. [DeepSeek V4 Pro 0813 Released with Strong Performance and Low Cost](#item-1) ⭐️ 9.0/10
2. [Tailscale Details 16-Year-Old SQLite WAL-Reset Bug Fix](#item-2) ⭐️ 9.0/10
3. [Qwen Releases Massive 2.4T MoE Model Qwen3.8-2.4T-A95B](#item-3) ⭐️ 9.0/10
4. [Researchers Steal Hidden Reasoning from Top LLM APIs](#item-4) ⭐️ 9.0/10
5. [HTML over WebSockets: Real-Time SPAs with Minimal JavaScript](#item-5) ⭐️ 8.0/10
6. [xAI Releases Grok 4.6, Sparking Debate on Performance and API Quirks](#item-6) ⭐️ 8.0/10
7. [Chrome's Tiny JPEG Rendering Quirk Explained](#item-7) ⭐️ 8.0/10
8. [Amazon to Train AI on Twitch Streams by Default, Opt-Out Available](#item-8) ⭐️ 8.0/10
9. [AI Pioneers Debate Open Source, Regulation at Ai4](#item-9) ⭐️ 8.0/10
10. [General Catalyst leads $1.1B round into 2-month-old River AI](#item-10) ⭐️ 8.0/10
11. [Anthropic's Unreleased Model Makes Progress on Riemann Hypothesis](#item-11) ⭐️ 8.0/10
12. [Anthropic Extends AI Text Watermarking to Older Models](#item-12) ⭐️ 8.0/10
13. [Adam's Per-Coordinate Scaling Breaks Rotation Invariance and Low-Rank Bias](#item-13) ⭐️ 8.0/10
14. [Decoupled Descent: Exact Train-Test Error Tracking via AMP](#item-14) ⭐️ 8.0/10
15. [White House to Expand AI Policy to Include Open-Source Models in Safety Testing](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek V4 Pro 0813 Released with Strong Performance and Low Cost](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 9.0/10

DeepSeek V4 Pro 0813, the GA release of DeepSeek's 1.6T-parameter flagship model, is now available via API on OpenRouter. It features a 1,048,576-token context window, 384,000-token maximum output, and pricing of $0.435 per million input tokens and $0.87 per million output tokens. This release is significant because it offers a high-performance model at a very competitive price, potentially disrupting the AI model market. Early community tests show it can handle complex development tasks effectively, making advanced AI more accessible to developers and businesses. The model is available via API only, and it is unclear whether open weights will be released. It includes independent benchmarks from Artificial Analysis, and the official announcement highlights enhanced agent capabilities, support for the Responses API, and Codex integration.

hackernews · explosion-s · Aug 12, 16:04 · [Discussion](https://news.ycombinator.com/item?id=49274600)

**Background**: DeepSeek is a Chinese AI company known for releasing powerful open-source language models at low cost. Mixture-of-experts (MoE) architecture, used in this model, activates only a subset of parameters per token, improving efficiency. The model is now fully available across web, mobile app, and API, according to DeepSeek's official site.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V4 Pro 0813 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://lovableapp.org/blog/deepseek-v4-pro-0813">DeepSeek V4 Pro 0813 (2026): Complete Guide to Pricing ...</a></li>
<li><a href="https://deepseek.com/en/index.html">DeepSeek</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely positive, with users reporting strong performance on complex tasks at low cost. One user noted minor issues compared to GPT-5.6-terra-high on a Docker deployment task, while another praised significant gains in a traffic simulator without new problems. Some users expressed interest in trying the model, and one highlighted cost-effectiveness as a key factor.

**Tags**: `#AI`, `#DeepSeek`, `#LLM`, `#model release`, `#open source`

---

<a id="item-2"></a>
## [Tailscale Details 16-Year-Old SQLite WAL-Reset Bug Fix](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 9.0/10

Tailscale published a detailed blog post about discovering and fixing a 16-year-old SQLite bug, a rare data race between a checkpoint and a write transaction in WAL mode. The fix was developed collaboratively with the SQLite team, aided by a custom VFS shim funded by Tailscale. This bug could corrupt SQLite databases under specific concurrency conditions, affecting countless applications that rely on SQLite. The debugging process highlights the value of commercial support and specialized tools for open-source projects, and the fix improves SQLite's reliability for all users. The bug occurs when a write happens at a specific time during a checkpoint, causing the checkpoint to think pages have been copied from the WAL to the main database when they haven't. Tailscale funded the development of the tmstmpvfs shim, which added logging that helped isolate the race condition.

hackernews · ropbear · Aug 12, 14:22 · [Discussion](https://news.ycombinator.com/item?id=49272832)

**Background**: SQLite uses Write-Ahead Logging (WAL) mode to improve concurrency, allowing multiple readers and a single writer. A checkpoint operation copies pages from the WAL file back into the main database. The bug was a data race that could corrupt the database when a write and checkpoint occurred concurrently on separate connections. SQLite is widely used in embedded systems and applications, making such bugs particularly impactful.

<details><summary>References</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL-Reset bug</a></li>
<li><a href="https://www.sqlite.org/howtocorrupt.html">How To Corrupt An SQLite Database File</a></li>
<li><a href="https://ubuntu.com/blog/hunting-a-16-year-old-sqlite-bug-with-tla-is-dqlite-affected">Hunting a 16-year-old SQLite bug with TLA+: is dqlite affected? | Ubuntu</a></li>

</ul>
</details>

**Discussion**: The community praised Tailscale for funding open-source development and taking the bug seriously with a commercial support contract. Commenters noted the irony of SQLite's extensive testing yet the presence of a bug, and appreciated the detailed write-up. Some discussed the specifics of the race condition and the single-writer design.

**Tags**: `#SQLite`, `#bug`, `#debugging`, `#open-source`, `#database`

---

<a id="item-3"></a>
## [Qwen Releases Massive 2.4T MoE Model Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen has released Qwen3.8-2.4T-A95B, a 2.4-trillion-parameter Mixture-of-Experts model with 95 billion active parameters per token, available in BF16 and FP8 formats. The model claims performance between Opus 4.8 and Fable 5. This release is significant as it brings frontier-level performance to the open-weight community, potentially rivaling proprietary models like Opus and Fable. It could accelerate adoption of large MoE models in research and industry, though serving requirements remain high. The model uses a fine-grained MoE architecture with 512 routed experts (10 active) plus one shared expert, over a 92-layer hybrid-attention backbone, supporting up to 1M context and 128K output. The BF16 version requires about 4.9TB of memory, while a 1-bit quantized version is around 397GB.

hackernews · Philpax · Aug 12, 15:01 · [Discussion](https://news.ycombinator.com/item?id=49273478)

**Background**: Mixture-of-Experts (MoE) models activate only a subset of parameters per token, enabling massive scale with manageable compute. Qwen3.8-2.4T-A95B is the open-weight version of Qwen3.8-Max, which adds vision, 1M context, and built-in tools. BF16 and FP8 are precision formats; FP8 reduces memory and speeds up inference but may require careful quantization.

<details><summary>References</summary>
<ul>
<li><a href="https://recipes.vllm.ai/Qwen/Qwen3.8-2.4T-A95B">Qwen/Qwen3.8-2.4T-A95B — 2.4T / 95B active · MOE · 256K ctx</a></li>
<li><a href="https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/">Serve Qwen3.8-2.4T-A95B, a 2.4T-Parameter Model, with Configurable Reasoning on NVIDIA GB300 NVL72 | NVIDIA Technical Blog</a></li>
<li><a href="https://www.mindstudio.ai/blog/qwen3-8-2-4t-a95b-release">Qwen3.8-2.4T-A95B: Alibaba's Open-Weight Qwen-Max Flagship Explained | MindStudio</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the model's size and serving challenges, with some noting it is harder to serve than Kimi k3 due to lack of QAT quantization. Others are excited about the 1-bit quantized version fitting into consumer hardware, and there is discussion about hardware cost projections. Some express disappointment that the open-weight model lacks vision and 1M context features of the official version.

**Tags**: `#AI/ML`, `#Large Language Models`, `#MoE`, `#Qwen`, `#Open Source`

---

<a id="item-4"></a>
## [Researchers Steal Hidden Reasoning from Top LLM APIs](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/) ⭐️ 9.0/10

Researchers demonstrated a method to recover encrypted chain-of-thought reasoning from proprietary LLM APIs by replaying traces into weaker sibling models and jailbreaking them. The attack affected Anthropic, OpenAI, and Google, but has since been fixed. This research exposes a significant security vulnerability in major AI APIs, highlighting risks of hidden reasoning extraction and potential for model distillation or data exfiltration. It underscores the need for robust encryption and access controls in AI services. The attack exploited that all models in the same family share the same encryption key, allowing encrypted reasoning blocks to be replayed into weaker models like Claude Haiku 4.5, which could be jailbroken to output plaintext. The paper includes extensive extracted reasoning traces, revealing raw chain-of-thought content not intended for human consumption.

rss · Simon Willison · Aug 11, 22:40

**Background**: Chain-of-thought reasoning is a technique where LLMs generate intermediate steps to arrive at answers, often hidden from users in proprietary APIs. To maintain context, APIs encrypt these reasoning traces and pass them back to clients, but the encryption keys are shared across model families, enabling the attack.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/top-ai-models-apis-flaw-exposes-hidden-reasoning/">OpenAI, Anthropic, and Google LLM APIs vulnerability Exposes...</a></li>
<li><a href="https://arxiv.org/pdf/2608.09867">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>

</ul>
</details>

**Tags**: `#LLM security`, `#chain-of-thought`, `#proprietary APIs`, `#AI safety`, `#research`

---

<a id="item-5"></a>
## [HTML over WebSockets: Real-Time SPAs with Minimal JavaScript](https://en.andros.dev/blog/ef4968f5/html-over-websockets-real-time-spas-with-barely-any-javascript/) ⭐️ 8.0/10

The article discusses building real-time SPAs using HTML over WebSockets, a technique popularized by Phoenix LiveView, and highlights how it minimizes JavaScript usage. It also references new HTML streaming APIs in Chrome that could further reduce JS dependencies. This approach challenges the traditional heavy-JavaScript SPA paradigm, offering a simpler and more efficient way to build real-time applications. It could influence future web development practices, especially for server-rendered apps needing real-time updates. The technique uses WebSockets to send HTML fragments directly to the browser, which then updates the DOM without custom client-side JavaScript. The article notes that for most apps, SSE (Server-Sent Events) is simpler and cheaper, but WebSockets are necessary for bidirectional low-latency communication.

hackernews · redbell · Aug 12, 16:51 · [Discussion](https://news.ycombinator.com/item?id=49275335)

**Background**: Phoenix LiveView, created by Chris McCord, is a framework that allows building interactive web applications without writing much JavaScript by sending HTML over WebSockets. This technique predates LiveView, as McCord had experimented with similar ideas in Rails before moving to Phoenix. The approach contrasts with traditional SPAs that rely heavily on client-side rendering and REST APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/phoenixframework/phoenix_live_view">Phoenix LiveView</a></li>
<li><a href="https://www.phoenixframework.org/">Phoenix Framework</a></li>
<li><a href="https://websocket.org/comparisons/sse/">WebSocket vs SSE: Which One Should You Use?</a></li>

</ul>
</details>

**Discussion**: The comments highlight the historical context, noting that Chris McCord pioneered this technique with Rails before LiveView. Some discuss the trade-offs between WebSockets and SSE, with one commenter suggesting SSE is simpler for most cases. Others point to new HTML streaming APIs in Chrome that could further reduce JS bundles, and there is a link to a critical response.

**Tags**: `#WebSockets`, `#Real-time`, `#SPA`, `#Phoenix LiveView`, `#SSE`

---

<a id="item-6"></a>
## [xAI Releases Grok 4.6, Sparking Debate on Performance and API Quirks](https://x.ai/news/grok-4-6) ⭐️ 8.0/10

xAI released Grok 4.6, a new frontier AI model, on an unspecified date. It debuts on the AA-Briefcase benchmark with an Elo of 1577, placing it at Fable 5-tier, and shows strong performance across multiple benchmarks. Grok 4.6's release intensifies competition among major AI labs, offering a cost-effective alternative with competitive performance. Its strong benchmark results and lower pricing could pressure other frontier models and benefit users seeking high intelligence at lower cost. Grok 4.6 supports a 500k context window and offers four reasoning effort levels: xhigh, high (default), medium, and low. Pricing is $2.00 per 1M input tokens and $6.00 per 1M output tokens, which is lower than the median for output tokens.

hackernews · iLuddite · Aug 12, 15:32 · [Discussion](https://news.ycombinator.com/item?id=49274027)

**Background**: Grok is a chatbot developed by xAI, led by Elon Musk. The company has been releasing successive versions of the Grok model, with Grok 4 and 4 Heavy released in July 2025. Grok 4.6 is the latest iteration, aiming to compete with other frontier models like GPT-5.6 and Claude 4.8/5.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis">Grok 4 . 6 returns SpaceXAI to the intelligence frontier and leads on cost...</a></li>
<li><a href="https://x.ai/news/grok-4-6">Introducing Grok 4 . 6 | SpaceXAI</a></li>
<li><a href="https://docs.x.ai/developers/grok-4-6">Grok 4 . 6 | SpaceXAI Docs</a></li>

</ul>
</details>

**Discussion**: Community comments highlight concerns about the API adding a default system prompt that overrides user instructions, and skepticism about rapid benchmark improvements across labs, suggesting possible benchmark hacking. Some users find Grok 4.5 more pleasant to use than competitors, while others see Grok as a healthy competitor despite its polarizing reputation.

**Tags**: `#AI`, `#Grok`, `#xAI`, `#LLM`, `#benchmarks`

---

<a id="item-7"></a>
## [Chrome's Tiny JPEG Rendering Quirk Explained](https://guillaumetech.github.io/posts/jpg-scaling-chrome/) ⭐️ 8.0/10

A technical article explains that Chrome renders tiny JPEGs differently because it performs partial decompression, which can cause visual artifacts. The author advises against using JPEGs for small icons, recommending PNG or appropriately sized images instead. This matters because many developers use JPEGs for icons and small images, and the rendering difference can cause unexpected visual issues across browsers. Understanding this behavior helps developers choose the right image format and avoid subtle bugs in web and Electron applications. The article highlights that Chrome's partial decompression is an optimization that can lead to artifacts when images are scaled down significantly. It also notes that Firefox is working on similar lower-scale decompression (see bug 2033250), and that different scaling algorithms between browsers contribute to the visual differences.

hackernews · gutechh · Aug 12, 14:00 · [Discussion](https://news.ycombinator.com/item?id=49272549)

**Background**: JPEG is a lossy compression standard commonly used for photographs, but it can introduce compression artifacts such as blockiness and color banding, especially at low quality settings. When an image is displayed at a size much smaller than its original resolution, browsers must scale it down, and the scaling algorithm and decompression method can affect the final appearance. Chrome's partial decompression decodes only part of the JPEG data to speed up rendering, which can produce different results compared to full decompression followed by scaling.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JPEG">JPEG - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Compression_artifact">Compression artifact - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the same issue may occur with PNGs, and that using appropriately sized images is more important than the format. One commenter linked to a Firefox bug for lower-scale decompression, while another suggested that different scaling algorithms between Chrome and Firefox contribute more to the visual difference. A user also questioned whether Firefox does full rendering or partial rendering, indicating a desire for a more balanced comparison.

**Tags**: `#browser`, `#image-processing`, `#JPEG`, `#Chrome`, `#web-performance`

---

<a id="item-8"></a>
## [Amazon to Train AI on Twitch Streams by Default, Opt-Out Available](https://techcrunch.com/2026/08/12/amazon-will-train-on-twitch-streamers-content-by-default-unless-they-opt-out/) ⭐️ 8.0/10

Amazon will use Twitch streamers' content to train its generative AI models by default, with an opt-out setting now available under Security and Privacy in Twitch account settings. Twitch CPO Mike Minton confirmed the default-on approach, stating that an opt-in model would result in few participants. This policy shift raises significant privacy and consent concerns, as it leverages user-generated content for AI training without explicit consent, potentially setting a precedent for other platforms. It affects millions of Twitch streamers and could influence broader debates on AI training data ethics and user rights. The opt-out setting is labeled 'Training for Generative AI' and prevents Amazon from using a channel's streams, VODs, clips, highlights, chat, and text for training. However, some AI-powered features deemed necessary for platform functionality cannot be opted out of, and opting out does not affect models already trained.

rss · TechCrunch AI · Aug 12, 20:10

**Background**: Twitch is a popular live-streaming platform owned by Amazon, where users broadcast gameplay, creative content, and more. Generative AI models, such as Amazon's Nova series, require vast amounts of data for training, and companies often use user-generated content to improve these models. This move follows industry trends where platforms like Reddit and Google have faced backlash for similar practices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.engadget.com/2235928/how-to-stop-twitch-training-ai-on-streams/">How to stop Twitch from training AI on your streams - Engadget</a></li>
<li><a href="https://appleinsider.com/articles/26/08/12/twitch-will-train-amazons-ai-on-your-streams-unless-you-opt-out">Twitch will train Amazon's AI on your streams unless you opt out</a></li>
<li><a href="https://www.bbc.com/news/articles/cp30pz8d09jo">Twitch users can now block Amazon from using their content to train AI</a></li>

</ul>
</details>

**Discussion**: The community reaction has been largely negative, with users flooding Twitch's chat with criticism during the announcement. Many expressed concerns about consent and the lack of opt-in, while some noted that the opt-out option is a step forward but insufficient given the default-on nature.

**Tags**: `#AI training`, `#privacy`, `#Twitch`, `#Amazon`, `#ethics`

---

<a id="item-9"></a>
## [AI Pioneers Debate Open Source, Regulation at Ai4](https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/) ⭐️ 8.0/10

At the Ai4 conference in Las Vegas, Geoffrey Hinton, Fei-Fei Li, and Andrew Ng publicly debated AI regulation, open source access, and US competitiveness amid China's advances. The discussion highlighted deep divisions among the three pioneers on how to balance safety and innovation. This debate matters because it brings together three of the most influential voices in AI to address a critical policy question: whether open source AI should be restricted for safety reasons. Their positions could influence regulators and industry leaders as they shape the future of AI governance. The debate occurred at Ai4 2026, held August 4-6 in Las Vegas, and was part of a rare joint appearance. Reports indicate the three experts clashed over jobs, regulation, and who should shape AI's future, with Hinton emphasizing existential risks and Li and Ng advocating for pragmatic, open approaches.

rss · TechCrunch AI · Aug 12, 17:51

**Background**: Geoffrey Hinton, a Nobel Prize-winning AI pioneer, has recently warned that AI may outsmart humans and escape testing environments, highlighting safety gaps. Fei-Fei Li, a Stanford researcher and founder of World Labs, has previously urged policymakers to adopt a pragmatic attitude rather than an ideological one. Andrew Ng, a prominent AI educator and entrepreneur, has consistently advocated for open source and democratized AI access. The debate reflects broader tensions in the AI community over how to manage rapid advancement while ensuring safety and competitiveness.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/">As AI safety concerns mount, three pioneers make the case for ...</a></li>
<li><a href="https://www.forbes.com/sites/ronschmelzer/2026/08/06/hinton-li-ng-ai-jobs-regulation/">Three AI Pioneers Clash Over Jobs, Regulation And The Future ...</a></li>
<li><a href="https://www.datacenterknowledge.com/regulations/hinton-fei-fei-li-and-andrew-ng-clash-over-ai-risks-jobs-and-regulation-at-ai4">Hinton, Fei-Fei Li, and Andrew Ng Clash Over AI Risks at Ai4</a></li>

</ul>
</details>

**Discussion**: No community comments were provided for this news item.

**Tags**: `#AI safety`, `#open source`, `#regulation`, `#AI policy`, `#Geoffrey Hinton`

---

<a id="item-10"></a>
## [General Catalyst leads $1.1B round into 2-month-old River AI](https://techcrunch.com/2026/08/11/general-catalyst-leads-1-1b-round-into-2-month-old-river-ai/) ⭐️ 8.0/10

River AI, a startup founded by xAI co-founder Igor Babuschkin, has raised $1.1 billion in a funding round led by General Catalyst, just two months after its founding. The company aims to develop personal AI agents. This massive early-stage investment signals strong investor confidence in personal AI agents, a rapidly growing area. It also highlights the continued influence of high-profile AI founders and could accelerate competition in the consumer AI space. The funding round was led by General Catalyst, a major venture capital firm with over $43 billion in assets. River AI is only two months old and has not yet released any products, indicating the investment is based largely on the team and vision.

rss · TechCrunch AI · Aug 11, 17:41

**Background**: Personal AI agents are autonomous software systems that can perform tasks on behalf of users, such as managing emails, scheduling, and reminders. Igor Babuschkin is a co-founder of xAI, Elon Musk's AI company, and recently left to start his own ventures. General Catalyst is a prominent VC firm with investments in companies like Anthropic and Mistral.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/General_Catalyst">General Catalyst</a></li>
<li><a href="https://grokipedia.com/page/igor-babuschkin">Igor Babuschkin</a></li>
<li><a href="https://aimultiple.com/personal-ai-agents">Building Personal AI Agents + 18 Agent Platforms and Tools</a></li>

</ul>
</details>

**Tags**: `#AI`, `#funding`, `#startup`, `#personal agents`

---

<a id="item-11"></a>
## [Anthropic's Unreleased Model Makes Progress on Riemann Hypothesis](https://techcrunch.com/2026/08/11/an-unreleased-anthropic-model-made-progress-on-one-of-maths-biggest-unsolved-problems/) ⭐️ 8.0/10

Anthropic's unreleased AI model reportedly made unexpected progress on the Riemann hypothesis, a famous unsolved math problem, though it did not solve it. The specific details of the model and its findings have not been disclosed. This is significant because it demonstrates that advanced AI models can contribute to frontier mathematical research, potentially accelerating progress on long-standing problems. It also highlights the growing role of AI in scientific discovery, which could impact mathematicians and researchers worldwide. The article does not provide technical specifics about the model or the nature of its progress, leaving many questions unanswered. The Riemann hypothesis, formulated in 1859, asserts that all non-trivial zeros of the Riemann zeta function have real part 1/2, and it remains unproven despite extensive efforts.

rss · TechCrunch AI · Aug 11, 16:25

**Background**: The Riemann hypothesis is one of the most important unsolved problems in pure mathematics, with deep connections to the distribution of prime numbers. It is one of the Clay Mathematics Institute's Millennium Prize Problems, offering a $1 million reward for a proof. AI models like Anthropic's Claude series have shown advanced reasoning capabilities, and this news suggests they may be applied to such mathematical challenges.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://www.claymath.org/millennium/riemann-hypothesis/">Riemann Hypothesis - Clay Mathematics Institute</a></li>

</ul>
</details>

**Tags**: `#AI`, `#mathematics`, `#Anthropic`, `#Riemann hypothesis`, `#research`

---

<a id="item-12"></a>
## [Anthropic Extends AI Text Watermarking to Older Models](https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/) ⭐️ 8.0/10

Anthropic announced it will extend watermarking support for AI-generated text to older models, following its commitment to the EU AI Act's transparency framework. All models released after August 2 will automatically include technology to watermark both text and files, with files using the C2PA open standard. This move enhances traceability of AI-generated content, helping to combat misinformation and meet regulatory requirements. It sets a precedent for other AI labs and could accelerate industry-wide adoption of watermarking standards. The text watermarks are designed to remain invisible during normal reading and persist when content is copied or pasted. Anthropic is also working to retrofit older models and plans to provide detection tools for third parties.

rss · TechCrunch AI · Aug 11, 12:13

**Background**: Text watermarking is a technique for embedding hidden information within textual content to verify its authenticity or origin. With the rise of generative AI, there has been significant development in watermarking AI-generated text to address concerns about misinformation and regulatory compliance, such as the EU AI Act's Article 50, which requires AI outputs to be detectable as artificially generated.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/">Anthropic says it will watermark text generated by its AI models</a></li>
<li><a href="https://en.wikipedia.org/wiki/Text_watermarking">Text watermarking - Wikipedia</a></li>
<li><a href="https://www.seangoedecke.com/text-ai-watermarks/">Text AI watermarks will always be trivial to remove</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#watermarking`, `#AI safety`, `#content authenticity`

---

<a id="item-13"></a>
## [Adam's Per-Coordinate Scaling Breaks Rotation Invariance and Low-Rank Bias](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 8.0/10

A new study shows that Adam's per-coordinate second moment destroys rotation invariance in factored models, eliminating the implicit low-rank bias that gradient descent exhibits. The authors tested nine optimizers on matrix sensing and found that rotation-invariant methods like GD, Muon, and Shampoo preserve the bias, while Adam, RMSProp, and others lose it. This insight clarifies why certain optimizers generalize better in low-rank settings, which is crucial for training large language models and other overparameterized systems. It also highlights a previously overlooked design criterion—rotation invariance—that could guide the development of new optimizers. The study uses a one-parameter family that interpolates between per-coordinate and shared-scalar denominators, showing recovery improves monotonically as anisotropy decreases. Muon behaves unexpectedly: it excels on truly low-rank targets but degrades fastest with added spectral tail, crossing over with GD near 4% tail energy. The paper also notes that the 43-44% error reduction on hyperspectral data shrinks when each optimizer is tuned on its own grid.

reddit · r/MachineLearning · /u/EtherealGlyph · Aug 12, 16:39

**Background**: In factored models like W = UV^T, the loss is invariant to rotations (U,V) → (UQ, VQ), and gradient descent respects this symmetry. Adam's per-coordinate second moment, however, depends on the basis, breaking this invariance. Implicit low-rank bias refers to the tendency of certain optimizers to converge to low-rank solutions even without explicit regularization, which is beneficial for generalization in many tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.01472v1">The Newton–Muon Optimizer - arXiv.org</a></li>
<li><a href="https://github.com/KellerJordan/Muon">GitHub - KellerJordan/Muon: Muon is an optimizer for hidden ...</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely includes debates about whether the results are an artifact of insufficient tuning of Adam, as the author anticipates objections like 'you should have just tuned Adam harder.' Some may question the practical relevance of matrix sensing experiments to real-world deep learning, while others may appreciate the theoretical clarity and the surprising behavior of Muon.

**Tags**: `#optimization`, `#Adam`, `#low-rank bias`, `#matrix sensing`, `#implicit bias`

---

<a id="item-14"></a>
## [Decoupled Descent: Exact Train-Test Error Tracking via AMP](https://www.reddit.com/r/MachineLearning/comments/1vlu1se/decoupled_descent_enforcing_exact_traintest_error/) ⭐️ 8.0/10

A new training method called Decoupled Descent (DD) is introduced, which uses approximate message passing (AMP) corrections to enforce that the training error asymptotically equals the test error at each iteration. This is demonstrated on stylized Gaussian mixture models and a high-dimensional XOR model, showing that DD avoids the overfitting issue seen with gradient descent. This work addresses a fundamental issue in neural network training where training error decreases but test error stagnates or worsens, offering a theoretically grounded method to mitigate overfitting. It could enable validation without holding out data and open new directions for optimal stopping and hyperparameter tuning, potentially impacting how models are trained and evaluated. The method relies on AMP theory and operates under a low-dimensional state evolution recursion, making its dynamics transparent and tractable. The paper is theoretical and focuses on stylized problems, with plans for a PyTorch-compatible package in the future.

reddit · r/MachineLearning · /u/mlovik1 · Aug 11, 21:06

**Background**: Approximate message passing (AMP) is a technique from high-dimensional statistics used for signal recovery and inference, known for its state evolution analysis that precisely characterizes algorithm behavior. In machine learning, overfitting occurs when a model fits training data too closely, hurting generalization to new data. Decoupled Descent leverages AMP to enforce a train-test identity, ensuring that training error tracks test error, thus preventing overfitting.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2201.07487">A Concise Tutorial on Approximate Message Passing A unifying tutorial on Approximate Message Passing Lecture 19: Approximate message passing algorithms Approximate Message Passing Tutorial - GitHub Pages Vector Approximate Message Passing - IEEE Xplore Message-passing algorithms for compressed sensing Approximate Message Passing - GitHub Pages</a></li>
<li><a href="https://arxiv.org/abs/2105.02180">A unifying tutorial on Approximate Message Passing Lecture 19: Approximate message passing algorithms Approximate Message Passing Tutorial - GitHub Pages Vector Approximate Message Passing - IEEE Xplore Message-passing algorithms for compressed sensing Approximate Message Passing - GitHub Pages</a></li>
<li><a href="https://arxiv.org/pdf/2604.27883">Decoupled Descent: Exact Test Error Tracking Via Approximate ...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#optimization`, `#generalization`, `#approximate message passing`, `#theory`

---

<a id="item-15"></a>
## [White House to Expand AI Policy to Include Open-Source Models in Safety Testing](https://www.wired.com/story/the-white-house-is-going-to-expand-its-ai-policy/) ⭐️ 8.0/10

The White House plans to revise its AI policy framework to include open-source models in pre-release safety testing once they reach 'frontier' capability, expanding beyond the current coverage of closed-source models like those from Anthropic and OpenAI. The framework remains voluntary, and the change is expected to take effect in the coming months. This expansion could significantly impact the open-source AI ecosystem, potentially slowing the release of powerful open models and affecting US competitiveness in AI development. It signals a shift in regulatory attention toward open-weight models, which have been a major driver of innovation but also raise safety concerns. The policy would require safety testing for open-source models once they reach 'frontier' capability, a term referring to models that exceed prior-generation capabilities and outrun existing regulatory frameworks. Some officials worry that a potential 30-day testing requirement could stifle US companies, and the framework's voluntary nature is partly due to President Trump's belief that formal regulation would help China catch up.

telegram · zaihuapd · Aug 13, 00:43

**Background**: Frontier AI refers to models at the cutting edge of capability, often exceeding prior-generation models and posing novel risks. The White House's AI policy framework was initially designed for closed-source models like those from OpenAI and Anthropic, but the growing influence of open-source models has prompted a need for broader oversight. Safety testing aims to identify and mitigate risks such as adversarial attacks or unintended behaviors before deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://zertia.ai/glossary/governance/frontier-ai/">Frontier AI : Capability Beyond the Framework | Zertia</a></li>
<li><a href="https://www.politico.com/news/2026/08/04/white-house-ai-vetting-plan-to-exempt-nonproprietary-models-01024816">White House AI vetting plan to exempt lower-cost ‘open’ models</a></li>
<li><a href="https://owasp.org/www-project-ai-testing-guide/">OWASP AI Testing Guide</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open-source`, `#safety testing`, `#regulation`, `#White House`

---