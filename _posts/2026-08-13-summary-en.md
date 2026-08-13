---
layout: default
title: "Horizon Summary: 2026-08-13 (EN)"
date: 2026-08-13
lang: en
---

> From 86 items, 14 important content pieces were selected

---

1. [Qwen3.8-2.4T-A95B: Massive MoE Model Released, Rivals Top-Tier Performance](#item-1) ⭐️ 9.0/10
2. [Researchers Steal Hidden Reasoning from Top LLM APIs](#item-2) ⭐️ 9.0/10
3. [DeepSeek V4 Pro 0813 Released with Strong Performance-to-Cost Ratio](#item-3) ⭐️ 8.0/10
4. [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](#item-4) ⭐️ 8.0/10
5. [xAI Releases Grok 4.6, Sparking Debate on API Prompts and Rapid Progress](#item-5) ⭐️ 8.0/10
6. [Chrome's Partial JPEG Decoding Alters Tiny Image Appearance](#item-6) ⭐️ 8.0/10
7. [AI Coding Tools Risk Creating Unmaintainable Codebases](#item-7) ⭐️ 8.0/10
8. [Amazon to Train AI on Twitch Streams by Default, Opt-Out Available](#item-8) ⭐️ 8.0/10
9. [AI Pioneers Advocate for Openness Amid Safety Concerns](#item-9) ⭐️ 8.0/10
10. [Anthropic's Unreleased Model Advances on Riemann Hypothesis](#item-10) ⭐️ 8.0/10
11. [Anthropic to Watermark AI Text Across All Claude Models](#item-11) ⭐️ 8.0/10
12. [Adam's Basis Dependence Breaks Implicit Low-Rank Bias in Factored Models](#item-12) ⭐️ 8.0/10
13. [Decoupled Descent: Enforcing Exact Train-Test Error Tracking via AMP](#item-13) ⭐️ 8.0/10
14. [DeepSeek Launches V4-Flash Official API Public Beta](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwen3.8-2.4T-A95B: Massive MoE Model Released, Rivals Top-Tier Performance](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Alibaba's Qwen team released Qwen3.8-2.4T-A95B, an open-weight sparse mixture-of-experts model with 2.4 trillion total parameters and 95 billion active parameters per token. The model is the open-weight variant of Qwen3.8-Max and is available in BF16 and FP8 formats. This release brings near-frontier capabilities to the open ecosystem, with performance claims rivaling top models like Opus 4.5 and Fable 5. It is significant for researchers and developers who need high-performance models without relying on proprietary APIs, and it intensifies competition among open-weight model providers. The model supports configurable reasoning and up to one million tokens of context, but the open-weight version lacks vision input and non-thinking support, which are exclusive to Qwen3.8-Max. The BF16 version is approximately 4.9TB, while FP8 is about 2.4TB, and a 1-bit quantized version is around 397GB, making deployment challenging on consumer hardware.

hackernews · Philpax · Aug 12, 15:01 · [Discussion](https://news.ycombinator.com/item?id=49273478)

**Background**: Mixture-of-experts (MoE) models activate only a subset of parameters per token, enabling massive total parameter counts while keeping inference costs manageable. Quantization techniques like FP8 reduce memory footprint and speed up inference, but may require careful calibration to maintain quality. The Qwen3.8-2.4T-A95B is part of a trend of increasingly large open-weight models, competing with proprietary models from companies like Anthropic and xAI.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/">Serve Qwen3.8-2.4T-A95B, a 2.4T-Parameter Model, with ...</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.8-2.4t-a95b">Qwen3.8 2.4T A95B - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://forums.developer.nvidia.com/t/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/379956">Serve Qwen3.8-2.4T-A95B, a 2.4T-Parameter Model, with ...</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the model's size and deployment challenges, noting that only BF16 and FP8 are available at launch, making it harder to serve than Kimi k3. Some users are impressed by the 1-bit quantized version's small size (397GB) and performance, while others lament the lack of vision support and 1M context in the open-weight version. There is also discussion about licensing restrictions and comparisons with DeepSeek V4-Pro-0813.

**Tags**: `#AI/ML`, `#Large Language Models`, `#MoE`, `#Open Source`, `#Hugging Face`

---

<a id="item-2"></a>
## [Researchers Steal Hidden Reasoning from Top LLM APIs](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/) ⭐️ 9.0/10

Researchers demonstrated a method to recover hidden chain-of-thought reasoning from proprietary LLM APIs by replaying encrypted traces into weaker sibling models and jailbreaking them. The attack affected Anthropic, OpenAI, and Google, but has since been fixed. This finding exposes a significant security vulnerability in major LLM APIs, revealing that encrypted reasoning traces were not truly private. It has broad implications for AI safety and privacy, as hidden reasoning could be extracted and potentially misused. The attack exploited the fact that all models in the same family shared the same encryption key, allowing encrypted blocks to be replayed across sessions and models. The easiest target was Claude Haiku 4.5, which was jailbroken with a simple prompt to transcribe the reasoning verbatim.

rss · Simon Willison · Aug 11, 22:40

**Background**: Chain-of-thought reasoning is a technique where LLMs generate intermediate steps before producing a final answer, improving accuracy. Proprietary LLM APIs often encrypt these reasoning traces to keep them hidden from users, but this research shows the encryption was flawed. The attack involved replaying encrypted traces into weaker models and jailbreaking them to reveal the hidden reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://reptile.haus/journal/encrypted-reasoning-traces-stolen-thoughts-llm-api-security-2026/">Your Encrypted Reasoning Traces Were Never Private: What Development Teams</a></li>
<li><a href="https://blog.cryptographyengineering.com/2026/05/29/fooling-around-with-encrypted-reasoning-blobs/">Let’s talk about encrypted reasoning</a></li>
<li><a href="https://thehackernews.com/2026/08/openai-anthropic-google-api-flaw-let.html">OpenAI, Anthropic, Google API Flaw Let Weaker AI Models Decode Stronger Models' Reasoning</a></li>

</ul>
</details>

**Tags**: `#LLM security`, `#AI safety`, `#chain-of-thought`, `#proprietary APIs`, `#research`

---

<a id="item-3"></a>
## [DeepSeek V4 Pro 0813 Released with Strong Performance-to-Cost Ratio](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 8.0/10

DeepSeek has released a new AI model, DeepSeek V4 Pro 0813, now available via API on OpenRouter. It offers a 1,048,576-token context window and pricing of $0.435 per million input tokens and $0.87 per million output tokens. This release is significant because it offers a compelling performance-to-cost ratio, as highlighted by community tests showing it can handle complex development tasks at a fraction of the cost of competitors like Grok 4.6. It strengthens DeepSeek's position in the competitive open-source LLM market, potentially making advanced AI more accessible. The model is a large-scale mixture-of-experts (MoE) architecture with 1.6T total parameters and 49B activated parameters. It supports a maximum output of 384,000 tokens, and while open weights have not been confirmed, previous DeepSeek models have been open-sourced, suggesting a likely release.

hackernews · explosion-s · Aug 12, 16:04 · [Discussion](https://news.ycombinator.com/item?id=49274600)

**Background**: DeepSeek is a Chinese AI research company known for releasing high-performance, cost-effective open-source language models. Mixture-of-experts (MoE) is an architecture that activates only a subset of parameters per token, enabling large models to run efficiently. The model is available via API, and users can access it through platforms like OpenRouter.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V4 Pro 0813 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro">DeepSeek V4 Pro - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://artificialanalysis.ai/models/deepseek-v4-pro">DeepSeek V4 Pro (max) - Intelligence, Performance & Price Analysis</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely positive, with users praising the model's cost-effectiveness and performance. One user reported that DeepSeek V4 Pro 0813 completed a development task in 12 minutes at $0.12 (with a bug), while Grok 4.6 took 3 minutes at $1.41 (no bug), highlighting the trade-off between cost and speed. Some users noted the lack of an official announcement page and linked to benchmarks for more information.

**Tags**: `#AI`, `#LLM`, `#DeepSeek`, `#Machine Learning`, `#Open Source`

---

<a id="item-4"></a>
## [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

Tailscale published a detailed post explaining how they traced database corruption to a 16-year-old SQLite WAL-reset bug, and funded an open-source VFS shim to help isolate the race condition. The bug was fixed in SQLite 3.51.3. This highlights the importance of investing in open-source debugging tools and the subtle dangers of concurrency even in well-tested software like SQLite. It also demonstrates how companies can contribute back to critical infrastructure projects. The bug involved a collision between a write transaction and a WAL-reset, which could only occur under specific concurrency conditions. Tailscale patched their SQLite driver to log warnings when these operations overlap, and the VFS shim they funded helps verify invariants and detect similar issues.

hackernews · ropbear · Aug 12, 14:22 · [Discussion](https://news.ycombinator.com/item?id=49272832)

**Background**: SQLite is a widely used embedded database that employs Write-Ahead Logging (WAL) for durability and performance. The WAL-reset bug, present since 2010, could cause database corruption under rare race conditions. Tailscale uses SQLite for its control plane, and their single-writer design was thought to be safe, but the bug still manifested.

<details><summary>References</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL-Reset bug</a></li>
<li><a href="https://antithesis.com/blog/2026/wal-reset-bug/">Breaking the WAL | Antithesis</a></li>
<li><a href="https://sqlite.org/vfs.html">The SQLite OS Interface or "VFS"</a></li>

</ul>
</details>

**Discussion**: Community members praised Tailscale for funding the open-source VFS shim and for their transparency. Some discussed the concurrency aspects, noting that the bug could only occur with multiple connections, and others appreciated the philosophical point about testing limitations.

**Tags**: `#SQLite`, `#database`, `#bug`, `#open-source`, `#Tailscale`

---

<a id="item-5"></a>
## [xAI Releases Grok 4.6, Sparking Debate on API Prompts and Rapid Progress](https://x.ai/news/grok-4-6) ⭐️ 8.0/10

xAI has released Grok 4.6, a new frontier AI model that builds on Grok 4.5 with a focus on long-running agents and ambitious interactive and visual work. The model is now available on the xAI API with a 500k context window, text and image inputs, and text-only output. Grok 4.6 represents a significant step in the competitive AI landscape, positioning xAI as a strong contender against other frontier models like GPT-5.6 and Claude 4.8. Its release at a competitive price point could influence market dynamics and user adoption, especially for agentic and coding tasks. Grok 4.6 has a 500k context window and no text output limit, according to the release notes. It is priced at half the cost of rival frontier models, with an ELO score of 1753, as highlighted by Elon Musk. The model focuses on long-running agents and improved interactive and visual capabilities.

hackernews · iLuddite · Aug 12, 15:32 · [Discussion](https://news.ycombinator.com/item?id=49274027)

**Background**: Grok is a series of large language models developed by xAI, launched in November 2023. The release of Grok 4.6 follows Grok 4.5 and is part of a rapid iteration cycle in the AI industry, where models are frequently updated to improve performance and capabilities. The model is designed for coding, agentic tasks, and knowledge work, and is available via the xAI API.

<details><summary>References</summary>
<ul>
<li><a href="https://x.ai/news/grok-4-6">Introducing Grok 4.6 | SpaceXAI</a></li>
<li><a href="https://docs.x.ai/developers/grok-4-6">Grok 4 . 6 | SpaceXAI Docs</a></li>
<li><a href="https://www.basenor.com/blogs/news/xai-launches-grok-4-6-1753-elo-half-the-price-of-rival-frontier-models">xAI Launches Grok 4.6: 1753 ELO, Half the Price of Rival Frontier Models</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed sentiments: some users are concerned about the API adding a default system prompt that overrides user instructions, while others question the rapid pace of model improvements, suggesting possible benchmark hacking or distillation. Some users find Grok 4.5 more pleasant to use than competitors, praising its conciseness and speed, while others see Grok as a healthy competitor despite its polarizing reputation.

**Tags**: `#AI`, `#Grok`, `#xAI`, `#LLM`, `#API`

---

<a id="item-6"></a>
## [Chrome's Partial JPEG Decoding Alters Tiny Image Appearance](https://guillaumetech.github.io/posts/jpg-scaling-chrome/) ⭐️ 8.0/10

The article explains that Chrome's partial JPEG decoding optimization causes tiny JPEGs to appear differently compared to other browsers like Firefox. It advises web developers to use appropriate image formats and resolutions to avoid these rendering discrepancies. This matters because subtle browser rendering differences can affect user experience and visual consistency across platforms. Web developers need to understand these quirks to ensure their images display as intended, especially for icons and small UI elements. The article highlights that Chrome's optimization decodes only part of the JPEG data, leading to different scaling results. It also notes that Firefox uses a different scaling algorithm, which may contribute to the visual differences, and that PNGs may face similar issues.

hackernews · gutechh · Aug 12, 14:00 · [Discussion](https://news.ycombinator.com/item?id=49272549)

**Background**: JPEG is a lossy compression format commonly used for photographs, while PNG is lossless and better suited for icons and graphics. Browsers use various decoding and scaling algorithms to display images, and these can produce different results, especially for small images. Chrome's partial decoding optimization aims to improve performance but can alter the appearance of tiny images.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JPEG">JPEG - Wikipedia</a></li>
<li><a href="https://www.baeldung.com/cs/jpeg-compression">JPEG Compression Explained | Baeldung on Computer Science</a></li>

</ul>
</details>

**Discussion**: Community comments confirm that similar issues occur with PNGs, and that Chrome's optimization caused problems in Electron apps. Some users note that Firefox and Chrome use different scaling algorithms, with Firefox being sharper but having ringing artifacts. There is also a reference to ongoing Firefox work on lower-scale decompression.

**Tags**: `#web development`, `#browser rendering`, `#image optimization`, `#Chrome`, `#JPEG`

---

<a id="item-7"></a>
## [AI Coding Tools Risk Creating Unmaintainable Codebases](https://simonwillison.net/2026/Aug/12/florian-herrengt/) ⭐️ 8.0/10

Florian Herrengt's blog post, quoted by Simon Willison, illustrates a scenario where AI-assisted development leads to a convoluted codebase that no one on the team understands, with developers relying on AI like Claude to explain their own code. This highlights a growing concern in the software engineering community about the erosion of core engineering skills and the accumulation of 'cognitive debt' as AI tools generate code that humans don't fully understand. It could impact code maintainability, debugging efficiency, and the long-term health of software projects. The quote describes a team repeatedly failing to fix a bug, with a developer admitting they don't know where the data comes from and suggesting asking Claude. The project has become so layered and complex that no one can understand it, illustrating the risks of over-reliance on AI without proper oversight.

rss · Simon Willison · Aug 12, 15:08

**Background**: AI-assisted development tools like Claude and Fable are increasingly used to generate code, boosting productivity but also raising concerns about code quality and developer understanding. The concept of 'cognitive debt' refers to the hidden cost of code that is difficult to understand and maintain, which can accumulate when AI generates code without human comprehension.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://www.linkedin.com/posts/sohamsahu03_codequality-generativeai-softwaredevelopment-activity-7428460951798153216-5u7A">Code Quality Matters in AI Era | Soham Sahu posted on the... | LinkedIn</a></li>
<li><a href="https://www.excellentwebworld.com/ai-assisted-software-development/">AI - Assisted Software Development : A Comprehensive Guide</a></li>

</ul>
</details>

**Tags**: `#AI`, `#software engineering`, `#code quality`, `#future of work`, `#AI-assisted development`

---

<a id="item-8"></a>
## [Amazon to Train AI on Twitch Streams by Default, Opt-Out Available](https://techcrunch.com/2026/08/12/amazon-will-train-on-twitch-streamers-content-by-default-unless-they-opt-out/) ⭐️ 8.0/10

Amazon will use Twitch streamers' content to train its AI models by default, with an opt-out option now available in settings. Twitch CPO Mike Minton acknowledged on a livestream that if it were opt-in, nobody would opt in. This policy shift raises significant ethical and legal questions about consent and creator rights, as it defaults to using creators' content without explicit permission. It could set a precedent for other platforms and impact the livelihoods of content creators who rely on Twitch. The opt-out toggle is available in Twitch settings, but it does not apply to all AI features. According to Insider Gaming, the policy allows streamers to opt out of Amazon AI training, but not all AI features are covered.

rss · TechCrunch AI · Aug 12, 20:10

**Background**: Twitch is a popular live-streaming platform owned by Amazon, and its content includes video, audio, and chat data. Amazon uses this data to train its generative AI models, such as those offered through AWS Bedrock. The default opt-out approach contrasts with more consent-forward practices, and the AWS privacy page states that customer prompts are not used unless consent is given, but this policy applies to Twitch content separately.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theverge.com/tech/979112/twitch-streamers-can-now-opt-out-from-training-amazons-ai">Twitch streamers can now opt out from training Amazon’s AI</a></li>
<li><a href="https://insider-gaming.com/twitch-ai-training-opt-out-setting/">Twitch Adds AI Training Opt - Out Setting for... - Insider Gaming</a></li>
<li><a href="https://aws.amazon.com/bedrock/amazon-models/privacy/">Amazon Model Training & Privacy - AWS</a></li>

</ul>
</details>

**Discussion**: The provided content includes a quote from Twitch's CPO, which sparked controversy. The community discussion likely reflects concerns about consent and the default opt-in practice, with many creators expressing dissatisfaction and calling for an opt-in model instead.

**Tags**: `#AI training`, `#Twitch`, `#Amazon`, `#data privacy`, `#content creators`

---

<a id="item-9"></a>
## [AI Pioneers Advocate for Openness Amid Safety Concerns](https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/) ⭐️ 8.0/10

At the Ai4 conference in Las Vegas, Geoffrey Hinton, Fei-Fei Li, and Andrew Ng debated AI regulation and open source access, arguing for balanced approaches and continued openness to maintain US competitiveness against China. This discussion highlights a critical tension in the AI industry between safety regulation and innovation, with prominent figures shaping policy debates that could affect global AI development and competition. The debate occurred at Ai4, described as America's largest AI conference, held August 4-6, 2026. The experts emphasized the importance of open source for transparency and collaboration while acknowledging the need for some regulation.

rss · TechCrunch AI · Aug 12, 17:51

**Background**: Open source AI models allow researchers and developers to access and modify code, promoting innovation and transparency. However, concerns about misuse and safety have led to calls for regulation, creating a debate between openness and control. The US-China competition in AI adds urgency to these discussions.

<details><summary>References</summary>
<ul>
<li><a href="https://ai4.io/">Ai4 2026</a></li>
<li><a href="https://www.toolify.ai/ai-news/the-debate-regulating-open-source-language-models-in-the-ai-industry-1954573">The Debate : Regulating Open Source Language Models in the AI ...</a></li>
<li><a href="https://pub.towardsai.net/tai-108-conflicting-developments-in-the-ai-regulation-debate-5b98990b6e5f">TAI #108:Conflicting Developments in the AI Regulation Debate</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#open source`, `#regulation`, `#Geoffrey Hinton`, `#Fei-Fei Li`

---

<a id="item-10"></a>
## [Anthropic's Unreleased Model Advances on Riemann Hypothesis](https://techcrunch.com/2026/08/11/an-unreleased-anthropic-model-made-progress-on-one-of-maths-biggest-unsolved-problems/) ⭐️ 8.0/10

An unreleased Anthropic model made notable progress on the Riemann hypothesis, a major unsolved problem in mathematics, though it did not provide a full proof. The development was reported by TechCrunch on August 11, 2026. This is significant because it demonstrates advanced reasoning capabilities in AI models, potentially accelerating research in pure mathematics. It could also signal that AI can assist in tackling long-standing mathematical problems, impacting both the AI and mathematics communities. The model is unreleased, so details about its architecture and training are not public. The progress is described as 'more than you might expect' but falls short of solving the hypothesis, which remains unproven.

rss · TechCrunch AI · Aug 11, 16:25

**Background**: The Riemann hypothesis, proposed by Bernhard Riemann in 1859, states that all nontrivial zeros of the Riemann zeta function have real part 1/2. It is one of the Millennium Prize Problems, with a $1 million reward, and has profound implications for the distribution of prime numbers. Despite extensive numerical evidence, no proof has been found for over 150 years.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis</a></li>
<li><a href="https://mathworld.wolfram.com/RiemannHypothesis.html">Riemann Hypothesis -- from Wolfram MathWorld</a></li>
<li><a href="https://www.anthropic.com/">Home \\ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#mathematics`, `#Anthropic`, `#Riemann hypothesis`, `#research`

---

<a id="item-11"></a>
## [Anthropic to Watermark AI Text Across All Claude Models](https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/) ⭐️ 8.0/10

Anthropic announced it will watermark text generated by its AI models, including older versions, to improve traceability. The watermark will be applied at the model level, ensuring it appears regardless of the Claude product or surface used. This move is significant for AI safety and content provenance, as it helps distinguish AI-generated text from human-written content. It sets an industry precedent and could influence other AI companies to adopt similar watermarking practices. Starting with models released on or after August 2, Anthropic will embed an imperceptible, machine-readable signal directly into Claude-generated text. The watermark persists through copying and pasting and may survive some editing, without affecting text quality.

rss · TechCrunch AI · Aug 11, 12:13

**Background**: AI text watermarking involves embedding hidden signals or identifiers within AI-generated content to trace its origin and verify authenticity. Techniques range from zero-watermarking, which extracts text features for verification, to directly inserting unique patterns. Anthropic's commitment extends watermarking to older models, ensuring broader coverage.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/">Anthropic says it will watermark text generated by its AI models | TechCrunch</a></li>
<li><a href="https://www.businessinsider.com/anthropic-watermarking-feature-stops-undetected-ai-generated-writing-2026-8">Anthropic just rolled out a tool that could decimate some people's dreams of writing AI novels undetected</a></li>
<li><a href="https://fortune.com/2026/08/11/anthropic-claude-watermark-ai-text-police-ai-slop/">Anthropic plans to add an invisible mark to AI text—as the industry scrambles to police AI slop | Fortune</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#watermarking`, `#AI safety`, `#content provenance`

---

<a id="item-12"></a>
## [Adam's Basis Dependence Breaks Implicit Low-Rank Bias in Factored Models](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 8.0/10

A new study demonstrates that Adam's per-coordinate second moment breaks rotation invariance in factored models, causing it to lose the implicit low-rank bias that gradient descent preserves. Experiments with nine update rules on matrix sensing show that optimizers like GD, Muon, and Shampoo retain the bias, while Adam, RMSProp, Lion, signum, and Adafactor do not. This finding identifies a fundamental property—basis invariance—that distinguishes optimizers preserving implicit low-rank bias from those that don't, which could influence future optimizer design. It also reconciles conflicting reports about Muon's spectral bias, showing that both behaviors occur depending on the spectral tail of the target. The study uses a one-parameter family that interpolates Adam's denominator from per-coordinate to a single shared scalar, showing recovery improves monotonically along this path, pinning the damage on anisotropy rather than adaptivity. Muon is exact on truly low-rank targets but degrades fastest as a spectral tail is added, ceding to GD near 4% tail energy. The paper also notes that momentum is empirical, not proven, and that the held-out error reduction on hyperspectral data is smaller when each method selects its own learning rate.

reddit · r/MachineLearning · /u/EtherealGlyph · Aug 12, 16:39

**Background**: In factored models where a weight matrix is expressed as W = UV^T, the loss is invariant to orthogonal rotations of the factors. Gradient descent respects this symmetry, but Adam's per-coordinate second moment does not, because it depends on the basis in which the factors are written. This property is linked to the implicit bias toward low-rank solutions that gradient descent exhibits in matrix factorization and matrix sensing problems. Muon is a newer optimizer that orthogonalizes momentum updates using Newton-Schulz iterations, aiming to exploit matrix structure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/rotational-adam-optimizer">Rotational Adam Optimizer - emergentmind.com</a></li>
<li><a href="https://arxiv.org/html/2501.16322v2">Implicit Bias in Matrix Factorization and its Explicit ...</a></li>
<li><a href="https://kellerjordan.github.io/posts/muon/">Muon: An optimizer for hidden layers in neural networks | Keller Jordan blog</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion includes the author inviting objections about tuning Adam harder, and comments likely debate the practical implications and the validity of the train-only learning rate rule. The author acknowledges that momentum is empirical and that the held-out error reduction is smaller when each method picks its own best rate, indicating a nuanced discussion about the experimental setup.

**Tags**: `#optimization`, `#low-rank`, `#Adam`, `#implicit bias`, `#matrix sensing`

---

<a id="item-13"></a>
## [Decoupled Descent: Enforcing Exact Train-Test Error Tracking via AMP](https://www.reddit.com/r/MachineLearning/comments/1vlu1se/decoupled_descent_enforcing_exact_traintest_error/) ⭐️ 8.0/10

The paper introduces Decoupled Descent (DD), a novel training method that leverages approximate message passing (AMP) Onsager corrections to enforce that the training error asymptotically equals the test error at each parameter iterate. This addresses the issue of data reuse bias in full-batch gradient descent, as demonstrated on Gaussian mixture models. This work provides a theoretically grounded approach to a fundamental problem in neural network training: the divergence between training and test errors. By offering a certificate of exact train-test error tracking, it opens new avenues for optimal stopping and hyperparameter tuning, potentially improving generalization in practical applications. The method is based on high-dimensional statistical theory, specifically approximate message passing, and is currently limited to stylized Gaussian mixture models and full-batch gradient descent. The author plans to develop a PyTorch-compatible package, and the paper includes simulations on a high-dimensional XOR model showing DD's advantage over standard GD.

reddit · r/MachineLearning · /u/mlovik1 · Aug 11, 21:06

**Background**: In machine learning, gradient descent often leads to overfitting, where training error decreases but test error stagnates or increases. Approximate message passing (AMP) is an efficient algorithm from high-dimensional statistics that can achieve Bayes-optimal performance for certain random matrix models. Data reuse bias refers to the bias introduced when the same data is used multiple times during training, which can cause the training error to underestimate the true generalization error.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2201.07487">[2201.07487] A Concise Tutorial on Approximate Message Passing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_model">Mixture model - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/machine-learning/bias-in-machine-learning-identifying-mitigating-and-preventing-discrimination/">Bias in Machine Learning: Identifying, Mitigating, and ...</a></li>

</ul>
</details>

**Discussion**: The Reddit post invites community feedback, but no comments are provided in the given content. The author expresses openness to questions and feature suggestions for a future PyTorch package.

**Tags**: `#machine learning`, `#generalization`, `#approximate message passing`, `#optimization`, `#theory`

---

<a id="item-14"></a>
## [DeepSeek Launches V4-Flash Official API Public Beta](https://t.me/zaihuapd/43149) ⭐️ 8.0/10

On July 31, 2026, DeepSeek launched the official API public beta for V4-Flash, a new model with significantly enhanced agent capabilities. It achieves strong benchmark scores, including 82.7 on Terminal Bench 2.1, 76.7 on Cybergym, 68.7 on DSBench-FullStack, and 59.6 on DSBench-Hard. This release marks a significant upgrade in DeepSeek's model lineup, offering improved agent performance that could rival leading models. The API availability enables developers to integrate these advanced capabilities into their applications, potentially accelerating AI adoption in coding and agentic tasks. V4-Flash natively supports the Responses API format and is specifically adapted for Codex. The model is a Mixture-of-Experts (MoE) with 284 billion total parameters and 13 billion activated parameters, and the V4-Pro version remains unchanged for now.

telegram · zaihuapd · Aug 12, 15:30

**Background**: DeepSeek is an AI research company known for developing open-weight language models. The V4-Flash model is part of the DeepSeek-V4 collection, and its API can be used as a backend for popular AI agent and coding tools like Claude Code, GitHub Copilot, and OpenCode without requiring code changes. The Responses API is an advanced interface for generating model responses, supporting stateful interactions and built-in tools.

<details><summary>References</summary>
<ul>
<li><a href="https://deepseek.com/en/index.html">DeepSeek</a></li>
<li><a href="https://api-docs.deepseek.com/">Your First API Call | DeepSeek API Docs</a></li>
<li><a href="https://docs.api.nvidia.com/nim/reference/deepseek-ai-deepseek-v4-flash">deepseek-ai / deepseek-v4-flash - docs.api.nvidia.com</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#AI`, `#API`, `#benchmark`, `#agent`

---