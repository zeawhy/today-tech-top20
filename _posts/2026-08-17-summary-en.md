---
layout: default
title: "Horizon Summary: 2026-08-17 (EN)"
date: 2026-08-17
lang: en
---

> From 58 items, 11 important content pieces were selected

---

1. [Stripe to Acquire AI Firm OpenRouter for Over $7 Billion](#item-1) ⭐️ 9.0/10
2. [DeepSeek-V4 Released with 1.6T Parameter Pro Model](#item-2) ⭐️ 9.0/10
3. [Anthropic Publishes Claude System Prompts, Sparking Debate](#item-3) ⭐️ 8.0/10
4. [Cloudflare silently injects analytics into sites on nameserver switch](#item-4) ⭐️ 8.0/10
5. [Qwen 3.8 27B Impresses but Defaults to Overthinking](#item-5) ⭐️ 8.0/10
6. [SpaceX Completes Acquisition of AI Coding Startup Cursor](#item-6) ⭐️ 8.0/10
7. [PJM's Modeling Error Wastes $12B of Ratepayer Money, Risks Repeat](#item-7) ⭐️ 8.0/10
8. [SSOG-Attention: Sub-Quadratic Attention via Sum of Separable Gaussians](#item-8) ⭐️ 8.0/10
9. [Jacobian Lens Transfers Across Qwen Model Versions Without Refitting](#item-9) ⭐️ 8.0/10
10. [BDH-CQ: 150M Model Breaks ARC-AGI-1 Cost-Accuracy Frontier](#item-10) ⭐️ 8.0/10
11. [Anthropic Q2 Revenue Soars 14x to Over $11.5B, Nears IPO](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Stripe to Acquire AI Firm OpenRouter for Over $7 Billion](https://www.bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion) ⭐️ 9.0/10

Stripe is acquiring OpenRouter, an AI model marketplace, for over $7 billion, according to Bloomberg. The deal, reported on August 16, 2026, marks one of the largest acquisitions in the AI infrastructure space. This acquisition signals a major convergence of payments and AI infrastructure, positioning Stripe to become a central player in AI commercialization. It could reshape how AI models are accessed and billed, affecting developers, enterprises, and the broader AI ecosystem. OpenRouter provides a unified API to access over 400 AI models, and its reported valuation was $1.3 billion just a few months ago, making the $7 billion price a significant premium. The deal also comes shortly after OpenAI chose Adyen as its payment provider, previously Stripe, highlighting competitive dynamics in AI payments.

hackernews · zacharyozer · Aug 16, 20:31 · [Discussion](https://news.ycombinator.com/item?id=49323381)

**Background**: OpenRouter is a developer-centric AI infrastructure startup that acts as a unified API gateway, or 'marketplace,' for accessing a wide range of large language models from multiple providers. Stripe is a leading online payments company known for its developer-friendly APIs and has been expanding into AI-related services. The acquisition would allow Stripe to extend from the payment layer to the distribution and billing layers of AI models, securing a more central position in the AI commercialization chain.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/about">About - The Unified Interface For LLMs | OpenRouter</a></li>
<li><a href="https://www.linkedin.com/posts/sanjeev-fintech_fintech-stripe-infrastructure-activity-7487504922406711296-F_8B">Stripe Acquires OpenRouter for $10B to Expand AI... | LinkedIn</a></li>
<li><a href="https://parameter.io/stripe-eyes-10-billion-acquisition-of-ai-model-marketplace-openrouter/">Stripe Eyes $10 Billion Acquisition of AI Model... - Parameter</a></li>

</ul>
</details>

**Discussion**: Community comments highlight strategic motivations, such as Stripe's ambition to abstract LLM rails and serve as a middleman for AI tokens. Some commenters question the high valuation, comparing it to the market caps of established companies, while others note the potential for payment volume growth and the competitive threat from OpenAI's switch to Adyen. There is also discussion about OpenRouter's switching costs and the benefits of Stripe's distribution.

**Tags**: `#acquisition`, `#AI`, `#payments`, `#OpenRouter`, `#Stripe`

---

<a id="item-2"></a>
## [DeepSeek-V4 Released with 1.6T Parameter Pro Model](https://t.me/zaihuapd/43224) ⭐️ 9.0/10

DeepSeek has released DeepSeek-V4, a major new version of its AI model, now available via chat.deepseek.com, the DeepSeek app, and the API. The lineup includes DeepSeek-V4-Pro (1.6T parameters) and DeepSeek-V4-Flash (284B parameters), both supporting 1M context and OpenAI/Anthropic-compatible endpoints. This release represents a significant advancement in open-source AI, potentially challenging closed-source rivals like GPT-5.4 and Claude 4.5. The availability of a 1.6T parameter open-source model with cost-effective pricing could democratize access to frontier AI capabilities for developers and enterprises. DeepSeek-V4 introduces three groundbreaking architectural innovations, according to deepseek.ai. The model is also notable for its shift to Huawei hardware, reflecting geopolitical factors in AI development. The API lineup includes Pro and Flash variants, with the Flash model being a unified multimodal understanding and generation model.

telegram · zaihuapd · Aug 16, 16:04

**Background**: DeepSeek is a Chinese AI company that develops large language models. Its previous version, DeepSeek-V3, pioneered an auxiliary-loss-free strategy for load balancing. DeepSeek-V4 builds on this foundation with a larger parameter count and enhanced capabilities, positioning it as a major contender in the AI model landscape.

<details><summary>References</summary>
<ul>
<li><a href="https://deepseekv4.dev/">DeepSeek V 4 : Future-Ready Reasoning for Teams</a></li>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V4 Explained: V4-Pro 1.6T vs V4-Flash 284B (2026)</a></li>
<li><a href="https://themenonlab.blog/blog/deepseek-v4-open-source-trillion-parameter-model">DeepSeek V 4 : A 1.6 Trillion Parameter Open-Source Model That...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#DeepSeek`, `#model release`, `#machine learning`

---

<a id="item-3"></a>
## [Anthropic Publishes Claude System Prompts, Sparking Debate](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic has published detailed system prompts for its Claude models on the official documentation site, revealing the exact instructions given to the models at the start of each conversation. The release includes prompts for various models, such as Opus 4.8 and the newly mentioned Claude Fable 5 and Claude Mythos 5. This transparency allows developers and researchers to understand and analyze Claude's behavior, potentially improving prompt engineering and model evaluation. The community discussion highlights concerns about prompt length and the implications for model intelligence, which could influence how AI systems are designed and deployed. The system prompts include instructions for Claude to check for images itself, as a prompt implying an image is present doesn't guarantee one was uploaded. Simon Willison has created a git history of changes, showing notable additions like the introduction of Claude Fable 5 and Claude Mythos 5, and there are also prompts to discourage hallucination about product details.

hackernews · tosh · Aug 16, 12:48 · [Discussion](https://news.ycombinator.com/item?id=49319556)

**Background**: System prompts are the initial instructions given to an AI model to set context and guide behavior. Anthropic's Claude models are used in web and mobile apps, and these prompts are updated over time to improve performance and safety. The release of these prompts is part of a broader trend of AI companies sharing more details about their models' inner workings.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/release-notes/system-prompts">System Prompts - Claude Platform Docs</a></li>
<li><a href="https://simonwillison.net/2025/May/25/claude-4-system-prompt/">Highlights from the Claude 4 system prompt</a></li>
<li><a href="https://github.com/Piebald-AI/claude-code-system-prompts">GitHub - Piebald-AI/claude-code-system-prompts: All parts of Claude Code's system prompt, 27 builtin tool descriptions, sub agent prompts (Plan/Explore/Task), utility prompts (CLAUDE.md, compact, statusline, magic docs, WebFetch, Bash cmd, security review, agent creation). Updated for each Claude Code version. · GitHub</a></li>

</ul>
</details>

**Discussion**: Community members expressed surprise at the length of the prompts, with some questioning why such powerful models need so much noise. Others noted that enforcing common sense via system prompts suggests Anthropic may not fully trust the model's intelligence. There were also concerns about moderation, with one user alleging that stories with negative AI connotations were being removed.

**Tags**: `#AI`, `#Claude`, `#system prompts`, `#Anthropic`, `#LLM`

---

<a id="item-4"></a>
## [Cloudflare silently injects analytics into sites on nameserver switch](https://news.ycombinator.com/item?id=49322107) ⭐️ 8.0/10

A user reported that after switching nameservers to Cloudflare, the service silently injected its Web Analytics JavaScript snippet into their HTML-only, JS-free site, requiring manual opt-out through the dashboard. This behavior was confirmed by other users and Cloudflare's own documentation, which states Web Analytics is enabled by default for proxied sites. This raises significant privacy and consent concerns, as Cloudflare injects tracking scripts without explicit user opt-in, affecting site owners who may be unaware. It also highlights broader industry debates about default-on analytics and the need for transparent, user-controlled defaults. The injected script is a beacon.min.js file from static.cloudflareinsights.com, with an integrity hash and a data-cf-beacon attribute containing a token. Users can disable it via the Cloudflare dashboard under Web Analytics, or use a Content-Security-Policy (CSP) meta tag to block external scripts. The behavior appears to occur only when Cloudflare is used as a proxy (not DNS-only mode).

hackernews · stagas · Aug 16, 17:49

**Background**: Cloudflare Web Analytics is a privacy-focused analytics service that provides insights without cookies. It is enabled by default for sites proxied through Cloudflare that previously used Browser Insights, and the JavaScript snippet is injected automatically. This practice has been criticized for lacking explicit opt-in consent, and users have sought workarounds such as CSP headers or disabling the feature in the dashboard.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49322107">Tell HN: Cloudflare silently injects its analytics when you switch nameservers | Hacker News</a></li>
<li><a href="https://developers.cloudflare.com/web-analytics/get-started/">Enabling Cloudflare Web Analytics · Cloudflare Web Analytics docs</a></li>
<li><a href="https://burgeonlab.com/blog/cloudflare-web-analytics-rum-injected-tracking-beacon-script-into-my-sites/">Cloudflare Auto Injected Tracking Scripts To My Sites</a></li>

</ul>
</details>

**Discussion**: Community comments express concern and provide solutions: one user suggests using a CSP meta tag to restrict script sources, another confirms the injection and shares the exact script snippet, while others question whether the injection occurs only when Cloudflare is used as a proxy. Some users report not seeing the injection on DNS-only setups, suggesting the behavior is tied to proxying.

**Tags**: `#Cloudflare`, `#privacy`, `#analytics`, `#web development`, `#security`

---

<a id="item-5"></a>
## [Qwen 3.8 27B Impresses but Defaults to Overthinking](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 8.0/10

Qwen 3.8 27B, an Apache 2 licensed 27B parameter vision-language model from Alibaba, was released, showing significant benchmark improvements over its predecessor and even closed-weight models. The model defaults to an 'xhigh' reasoning effort, leading to excessive token usage and long generation times. This release is significant for the open-weight LLM community, as 27B is an ideal size for local deployment on consumer hardware. The benchmark gains suggest it could rival larger closed models, but the default overthinking behavior may hinder practical use unless users adjust settings. The model supports a context window of up to 262,144 tokens, but LM Studio's default 8,192 token limit caused issues until increased. In one test, generating an SVG took 21 minutes, using 22,276 reasoning tokens for 3,223 output tokens, though the result was high quality.

rss · Simon Willison · Aug 16, 22:00

**Background**: Qwen 3.8 27B is a dense 27B-parameter model, requiring roughly 56GB VRAM at BF16, ~28GB at FP8, and ~14-16GB at 4-bit quantization. It is a native vision-language model that understands images and videos, with flexible thinking control. The Apache 2 license allows free use, modification, and distribution, making it attractive for local deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen/Qwen3.8-27B · Hugging Face</a></li>
<li><a href="https://www.yottalabs.ai/post/qwen-3-8-27b-specs-hardware-requirements-how-to-run-2026">Qwen 3.8 27B: Specs, Hardware Requirements, and How to Run It (2026) | Yotta Labs</a></li>
<li><a href="https://www.apache.org/licenses/LICENSE-2.0">Apache License , Version 2 .0 | Apache Software Foundation</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Qwen`, `#open-source`, `#AI`, `#benchmarks`

---

<a id="item-6"></a>
## [SpaceX Completes Acquisition of AI Coding Startup Cursor](https://techcrunch.com/2026/08/15/spacex-officially-closes-its-cursor-acquisition/) ⭐️ 8.0/10

SpaceX has officially closed its acquisition of AI coding startup Cursor, as confirmed by TechCrunch. The deal, reportedly valued at $60 billion, marks a major consolidation in the AI developer tools space. This acquisition signals SpaceX's strategic entry into the AI software market, potentially challenging established players like OpenAI and Anthropic. It could reshape the competitive landscape for AI coding tools and influence how aerospace and other industries adopt AI-assisted development. Cursor, known for its AI-powered coding assistant that adapts to a developer's style, has achieved rapid growth, reaching $100M ARR within 12 months and a valuation over $29B prior to the acquisition. The deal reportedly doubles the net worths of Cursor's co-founders, who are in their 20s.

rss · TechCrunch AI · Aug 15, 16:30

**Background**: Cursor is an AI coding startup that provides an IDE with AI-powered features like code completion, bug detection, and assistance, acting as a 'coding agent' for developers. The company has attracted significant investment from tech giants like Google and Nvidia, reflecting the growing demand for AI-assisted software development tools.

<details><summary>References</summary>
<ul>
<li><a href="https://cursor.com/">AI Coding Agent for Building Ambitious Software | Cursor</a></li>
<li><a href="https://www.linkedin.com/news/story/cursor-an-ai-coding-darling-now-worth-over-29b-6766332/">Cursor , an AI coding darling, now worth over $29B | LinkedIn</a></li>
<li><a href="https://www.growth-letter.com/p/this-startup-went-from-0-to-100m">This Startup Went From $0 to $100M ARR in 12 Months</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed, with some expressing excitement about the potential of combining Cursor's technology with SpaceX's resources, particularly around 'unlimited compute' and innovation in coding agents. Others question whether the $60 billion price tag is justified and debate the strategic implications for the AI industry.

**Tags**: `#AI`, `#acquisition`, `#SpaceX`, `#Cursor`, `#developer tools`

---

<a id="item-7"></a>
## [PJM's Modeling Error Wastes $12B of Ratepayer Money, Risks Repeat](https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted) ⭐️ 8.0/10

An investigative report reveals that flawed modeling in PJM's grid operations wasted $12 billion of US ratepayer money, and PJM is at risk of repeating the same mistake. The report highlights systemic issues in how PJM models its grid, leading to costly inefficiencies. This matters because PJM is the largest grid operator in the US, serving 65 million people, and such modeling errors directly impact electricity costs and reliability for millions of ratepayers. It also raises concerns about the grid's ability to handle the clean energy transition and increasing data center demand. The report suggests that PJM's modeling mistakes stem from outdated assumptions about demand growth and generator performance, leading to over-procurement of capacity and inflated costs. PJM's capacity market has also seen record-high prices due to these flaws, with critics pointing to a dysfunctional interconnection queue.

rss · Semianalysis · Aug 16, 22:27

**Background**: PJM Interconnection is a regional transmission organization (RTO) that coordinates the movement of wholesale electricity in all or parts of 13 states and the District of Columbia. Its capacity market is designed to ensure future electricity supply by paying generators to commit to providing power years in advance. However, modeling errors can lead to over- or under-procurement, affecting costs and reliability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.utilitydive.com/news/pjm-interconnection-capacity-auction-data-center/808264/">PJM capacity prices hit record high as grid operator falls short of reliability target | Utility Dive</a></li>
<li><a href="https://www.congress.gov/crs-product/R48553">PJM’s Electric Capacity Market: Background and Current Issues | Congress.gov | Library of Congress</a></li>
<li><a href="https://www.pjm.com/-/media/DotCom/library/reports-notices/special-reports/2026/20260506-powering-reliability-through-market-design.pdf">For Public Use Powering Reliability Through Market Design</a></li>

</ul>
</details>

**Tags**: `#energy grid`, `#modeling`, `#PJM`, `#policy`, `#infrastructure`

---

<a id="item-8"></a>
## [SSOG-Attention: Sub-Quadratic Attention via Sum of Separable Gaussians](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 8.0/10

SSOG-Attention replaces standard scaled dot-product attention (SDPA) with a sum of separable Gaussians, reducing complexity from O(N²·d) to O(N·√N·d). It matches or exceeds SDPA performance on CIFAR-100 and ImageNet while being faster and more memory-efficient. This offers a scalable alternative to quadratic attention, potentially enabling longer sequences and larger models in vision transformers. It could impact efficient transformer design and broaden applications in resource-constrained settings. The method learns a few Gaussian atoms per head and steers them based on the query token, exploiting factorization into separable Gaussians. Experiments show clear gains on small data (CIFAR-100) and equivalent performance with faster convergence on ImageNet.

reddit · r/MachineLearning · /u/4rtemi5 · Aug 16, 10:06

**Background**: Scaled dot-product attention (SDPA) computes pairwise similarities between all tokens, leading to quadratic complexity. Separable filters and Gaussian factorization are established techniques to reduce computational cost in signal processing and neural networks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2510.06685">Gaussian Equivalence for Self-Attention: Asymptotic Spectral Analysis</a></li>
<li><a href="https://apxml.com/courses/foundations-transformers-architecture/chapter-2-attention-mechanism-core-concepts/scaled-dot-product-attention">Scaled Dot-Product Attention Explained</a></li>
<li><a href="https://grokipedia.com/page/Separable_filter">Separable filter</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion includes technical questions about the method's theoretical guarantees and practical implementation, with the author actively engaging. Overall sentiment is positive, with interest in potential extensions and comparisons to other efficient attention mechanisms.

**Tags**: `#attention`, `#efficiency`, `#transformer`, `#machine learning`, `#scalability`

---

<a id="item-9"></a>
## [Jacobian Lens Transfers Across Qwen Model Versions Without Refitting](https://www.reddit.com/r/MachineLearning/comments/1vpa5cv/survival_of_the_fitted_qwen3627bs_jacobian_lens/) ⭐️ 8.0/10

A Jacobian lens fitted to Qwen3.6-27B was applied unchanged to Qwen3.8-27B, and it remained effective for latent entity identification and steering, with only modest degradation in next-token prediction readouts. This is the first empirical test of interpretability lens transferability across model versions, showing that lenses may not need refitting with every release. It has practical implications for monitoring pipelines and could reduce the cost of maintaining interpretability tools as models update. The transferred lens kept the latent entity near the top of the 248,320-token vocab, with median rank 4 at layer 48 on the home model vs 17 transferred, and even better at layer 24 (121 vs 38). Steering directions derived from the old checkpoint successfully suppressed 'paradox' in outputs on both models, while WikiText next-token prediction showed 1.2-1.3x cost mid-network and ~2x by layer 48.

reddit · r/MachineLearning · /u/imstilllearningthis · Aug 15, 18:24

**Background**: The Jacobian lens is a mechanistic interpretability technique that estimates which directions in a model's residual stream push it toward predicting specific tokens, using the Jacobian matrix. The logit lens is a simpler, training-free method that projects hidden states at each layer into the vocabulary space. This study tests whether such lenses, typically fitted to a single checkpoint, remain valid after a model update like Qwen3.6 to Qwen3.8.

<details><summary>References</summary>
<ul>
<li><a href="https://www.1950.ai/post/anthropic-s-j-lens-unlocks-the-hidden-logic-of-ai-a-major-leap-in-understanding-large-language-mode">Anthropic's J- Lens Unlocks the Hidden Logic of AI, A Major Leap in...</a></li>
<li><a href="https://www.emergentmind.com/topics/logit-lens-framework">Logit - Lens Framework for Transformer Interpretability</a></li>
<li><a href="https://huggingface.co/unsloth/Qwen3.8-27B">unsloth/ Qwen 3 .8-27B · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#interpretability`, `#mechanistic interpretability`, `#LLM`, `#Jacobian lens`, `#model versioning`

---

<a id="item-10"></a>
## [BDH-CQ: 150M Model Breaks ARC-AGI-1 Cost-Accuracy Frontier](https://www.reddit.com/r/MachineLearning/comments/1vov5r5/bdhcq_incontext_learning_with_recurrent_latent/) ⭐️ 8.0/10

Pathway introduced BDH-CQ, a 150M-parameter reasoning model that achieves 29.5% pass@2 on ARC-AGI-1 at a computed cost of $0.00070 per task, breaking the previously reported cost-accuracy Pareto frontier. The model performs in-context learning via recurrent latent reasoning without decoding intermediate reasoning states into language. This result demonstrates that recurrent latent reasoning can achieve strong performance on a challenging benchmark like ARC-AGI-1 at a fraction of the cost of larger models, potentially reshaping the efficiency landscape for reasoning systems. It also highlights a promising alternative to transformer-based architectures for in-context learning. BDH-CQ updates recurrent memory with demonstrations of unseen tasks and solves queries through iterative computation in a high-dimensional latent workspace. Neither task identifiers nor evaluation-task demonstration pairs are used in training, and no parameters are updated at inference time. The architecture scales naturally to large sizes, supporting tensor sharding patterns for training at 1T scale.

reddit · r/MachineLearning · /u/moschles · Aug 15, 06:18

**Background**: ARC-AGI-1 is a benchmark designed to measure general intelligence through fluid, systematic, and few-shot generalization across diverse tasks, emphasizing 'Easy for Humans, Hard for AI.' In-context learning allows models to adapt to new tasks from demonstrations without weight updates, while recurrent latent reasoning processes information in a continuous hidden state, avoiding explicit language generation. BDH-CQ combines these ideas to achieve efficient adaptation and inference.

<details><summary>References</summary>
<ul>
<li><a href="https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier">Pathway’s 150M-Parameter Model Breaks the...</a></li>
<li><a href="https://arxiv.org/html/2608.09888">BDH - CQ : In-Context Learning with Recurrent Latent Reasoning</a></li>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - The only AI benchmark that measures AGI progress.</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely includes commentary on the model's efficiency and the significance of breaking the Pareto frontier, with some users possibly questioning the cost calculations or the generalizability of the approach. However, no specific comments were provided in the search results.

**Tags**: `#in-context learning`, `#recurrent neural networks`, `#ARC-AGI`, `#latent reasoning`, `#efficiency`

---

<a id="item-11"></a>
## [Anthropic Q2 Revenue Soars 14x to Over $11.5B, Nears IPO](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 8.0/10

Anthropic's preliminary Q2 revenue exceeded $11.5 billion, a 14-fold year-over-year increase from $787 million, and up from $4.73 billion in Q1 2026. The company also reported positive adjusted operating profit for the quarter. This revenue surge signals strong commercial adoption of Anthropic's AI models and improved financial health, positioning the company for a potential large IPO this fall. It also reflects the broader boom in AI spending and competition in the industry. The figures are preliminary and subject to adjustment. The company is preparing for a major IPO that could launch this fall, according to Bloomberg citing documents.

telegram · zaihuapd · Aug 16, 07:26

**Background**: Anthropic is a leading AI company known for its Claude models, competing with OpenAI and others. Revenue growth is a key indicator of AI adoption, and a successful IPO would provide capital for further research and development.

**Tags**: `#Anthropic`, `#AI`, `#revenue`, `#IPO`, `#business`

---