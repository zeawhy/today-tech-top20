---
layout: default
title: "Horizon Summary: 2026-08-05 (EN)"
date: 2026-08-05
lang: en
---

> From 91 items, 16 important content pieces were selected

---

1. [Gwern Retires from Writing to Launch Guardian Angel AI Project](#item-1) ⭐️ 8.0/10
2. [DeepSeek V4 Flash Runs on Single AMD MI300X at 150+ tok/s](#item-2) ⭐️ 8.0/10
3. [Keyv and friends compromised in active Shai-Hulud npm supply chain attack](#item-3) ⭐️ 8.0/10
4. [Oxide Computer Raises $445M in Series D](#item-4) ⭐️ 8.0/10
5. [LLM 0.32 Adds Reasoning Traces, Server-Side Tools, and Smarter Logging](#item-5) ⭐️ 8.0/10
6. [MiniMax-H3 Runs on Apple Silicon via MLX Port](#item-6) ⭐️ 8.0/10
7. [Open-Weight AI Models Catch Up to Frontier, Safety Gap Widens](#item-7) ⭐️ 8.0/10
8. [Texas Halts New Data Centers, Orders Audits Amid Power Grid Strain](#item-8) ⭐️ 8.0/10
9. [AI Cuts Customer Service Jobs at Major Firms](#item-9) ⭐️ 8.0/10
10. [Kimi K3: Compressed Memory, Cross-Depth Attention, Latent Expert Routing](#item-10) ⭐️ 8.0/10
11. [Desk Reject Papers Without Reproducible Code](#item-11) ⭐️ 8.0/10
12. [Explorative Modeling: A New Pretraining Axis for Generative Models](#item-12) ⭐️ 8.0/10
13. [Huawei Unveils 'Tao's Law' for Time-Based Semiconductor Scaling](#item-13) ⭐️ 8.0/10
14. [Cloudflare Ditches Third-Party Security Tools for $58/Month AI Triage](#item-14) ⭐️ 8.0/10
15. [Google Builds $200B Wall Street Financing Machine for Anthropic](#item-15) ⭐️ 8.0/10
16. [China's First Mandatory L3/L4 Autonomous Driving Standard Submitted for Approval](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Gwern Retires from Writing to Launch Guardian Angel AI Project](https://twitter.com/gwern/status/2084739205071343837) ⭐️ 8.0/10

Gwern announced his retirement from full-time writing and pseudonymity to launch Guardian Angel, a project proposing highly personalized LLMs that emulate users' values to amplify productivity and defend against AI-powered threats. The announcement was made via a tweet linking to his detailed essay on gwern.net. This is significant because Gwern is a highly respected figure in the AI community, and his shift to an AI startup signals a growing trend of individuals building personal AI tools to counter corporate AI alignment. The project challenges the current chatbot paradigm, potentially influencing how AI assistants are developed and used. The Guardian Angel proposal includes techniques like dynamic evaluation, active learning, and local-first UI to create a 'digital twin' of the user. Gwern emphasizes that current chatbots are misaligned with users and aligned with their corporate owners, and his project aims to give individuals more control over their AI interactions.

hackernews · mattsterett · Aug 4, 20:48 · [Discussion](https://news.ycombinator.com/item?id=49174900)

**Background**: AI alignment refers to the challenge of ensuring AI systems act in accordance with human values and intentions. Gwern's project is a response to concerns that large language models (LLMs) are optimized for corporate interests, such as advertising and subscriptions, rather than for the individual user's benefit. The idea of a 'guardian angel' AI is inspired by the concept of 'uploading' one's mind to a digital form, aiming to create a personal AI that amplifies the user's capabilities rather than replacing them.

<details><summary>References</summary>
<ul>
<li><a href="https://gwern.net/guardian-angel">Guardian Angels: LLM Personalization for Productivity and ...</a></li>
<li><a href="https://www.devdigest.org/articles/gwerns-guardian-angel-personalized-llms-for-productivity-and-security">Gwern's Guardian Angel: Personalized LLMs for Productivity a</a></li>
<li><a href="https://ecency.com/@crrdlx/gwern-moving-from-writing-to-ai-startup">Gwern moving from writing to AI startup | Ecency</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some praise Gwern's humanity and vision, while others express skepticism, calling the project 'a kind of mania' and questioning the emphasis on productivity over self-actualization. There is also curiosity about the project's details and its potential impact.

**Tags**: `#AI alignment`, `#pseudonymity`, `#personal AI`, `#Gwern`, `#tech community`

---

<a id="item-2"></a>
## [DeepSeek V4 Flash Runs on Single AMD MI300X at 150+ tok/s](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐️ 8.0/10

A GitHub project demonstrates running DeepSeek V4 Flash with full weights on a single AMD MI300X accelerator, achieving over 150 tokens per second. The context window is reduced to 256k tokens instead of the original 1M. This achievement shows that frontier-class MoE models can be served on a single high-end GPU, potentially lowering hardware costs and enabling more accessible local or edge deployment. It highlights the growing capability of AMD's MI300X for large-scale inference. The model is a 284B-parameter Mixture-of-Experts with 13B active parameters, originally supporting a 1M-token context. The reduced 256k context is still practical for many coding and agentic tasks, and the full weights are preserved without quantization.

hackernews · zhoutong · Aug 4, 10:00 · [Discussion](https://news.ycombinator.com/item?id=49166386)

**Background**: DeepSeek V4 Flash is a lightweight variant of DeepSeek's V4 family, designed for coding, tool use, and agentic workflows. The AMD MI300X is a high-bandwidth memory (HBM) accelerator with 192GB of memory, making it suitable for large models. Tokens per second is a key metric for interactive inference, and memory bandwidth often limits performance.

<details><summary>References</summary>
<ul>
<li><a href="https://lmstudio.ai/models/deepseek-v4-flash">DeepSeek V4 Flash - lmstudio.ai</a></li>
<li><a href="https://www.orcarouter.ai/blog/deepseek-v4-flash-official-release">DeepSeek V4 Flash: Official Release, Explained - orcarouter.ai</a></li>
<li><a href="https://tokoscope.com/articles/deepseek-v4-flash">DeepSeek V4 Flash: The Fastest Open-Weight Frontier Model in ...</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the MI300X is typically sold in 8-GPU boxes, making single-unit purchase difficult, and suggested the MI350P as a PCIe alternative with 144GB memory. Some pointed out that prior art like DwarfStar can run the same model in less memory, and others appreciated the practical tradeoff of reduced context window for high speed.

**Tags**: `#DeepSeek`, `#AMD MI300X`, `#LLM inference`, `#hardware`, `#quantization`

---

<a id="item-3"></a>
## [Keyv and friends compromised in active Shai-Hulud npm supply chain attack](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) ⭐️ 8.0/10

An active npm supply chain attack has compromised the Keyv package and over 400 other packages, with the Shai-Hulud worm harvesting credentials and self-propagating. The attack was identified by JFrog Security Research and is ongoing. This attack affects widely-used npm packages, potentially compromising thousands of downstream projects and exposing sensitive credentials. It underscores the fragility of the open-source dependency ecosystem and the urgent need for stronger supply chain security measures. The Shai-Hulud worm publishes itself to every writable npm package and plants execution hooks in GitHub repositories. It harvests credentials and uses static and dynamic analysis to evade detection, with new versions continuing to emerge.

hackernews · cimi_ · Aug 4, 11:01 · [Discussion](https://news.ycombinator.com/item?id=49166874)

**Background**: Shai-Hulud is a self-replicating worm that targets the npm ecosystem, first identified in late 2025. It exploits compromised packages to spread, often through pre-install or post-install hooks, and has been linked to significant cloud-native ecosystem compromises.

<details><summary>References</summary>
<ul>
<li><a href="https://research.jfrog.com/post/shai-hulud-is-back-august/">Major Shai Hulud campaign strikes npm again, affecting keyv and 400+ packages - JFrog Security Research</a></li>
<li><a href="https://unit42.paloaltonetworks.com/npm-supply-chain-attack/">"Shai-Hulud" Worm Compromises npm Ecosystem in Supply Chain ...</a></li>
<li><a href="https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack">Shai-Hulud 2.0 Supply Chain Attack: 25K+ Repos Exposing Secrets</a></li>

</ul>
</details>

**Discussion**: Community members expressed concern over the attack, with some calling for a moratorium on pre-install hooks and others recommending devcontainers or tools like Packj for detection. There was also a request for grep patterns to check local node_modules for compromise.

**Tags**: `#supply chain`, `#npm`, `#security`, `#open source`, `#dependency`

---

<a id="item-4"></a>
## [Oxide Computer Raises $445M in Series D](https://www.sec.gov/Archives/edgar/data/1795071/000179507126000002/xslFormDX01/primary_doc.xml) ⭐️ 8.0/10

Oxide Computer Company has raised $445 million in a Series D round, according to a recent SEC Form D filing. This follows previous rounds of $44 million (Series A, 2023), $100 million (Series B, 2025), and $200 million (Series C, 2026). This significant funding round underscores strong investor confidence in Oxide's rack-scale hardware and software approach to on-premises cloud infrastructure. It could accelerate the company's growth and challenge established players in the data center market, potentially benefiting enterprises seeking alternatives to hyperscale cloud providers. The funding was disclosed via an SEC Form D filing, which is used for exempt offerings under Regulation D. Oxide designs and manufactures rack-scale systems with integrated software and hardware for on-premises data centers, serving enterprises and federal organizations.

hackernews · depr · Aug 4, 20:13 · [Discussion](https://news.ycombinator.com/item?id=49174407)

**Background**: Oxide Computer Company is a hardware startup founded by former engineers from companies like Joyent and Amazon, including Bryan Cantrill and Adam Leventhal. The company aims to provide a complete, integrated cloud platform that customers can own and operate on-premises, contrasting with traditional cloud providers. Form D is a notice filed with the SEC to report exempt offerings of securities, allowing private companies to raise capital without a full public registration.

<details><summary>References</summary>
<ul>
<li><a href="https://oxide.computer/press">Press | Oxide Computer Company</a></li>
<li><a href="https://www.linkedin.com/company/oxidecomputer">Oxide Computer Company - LinkedIn</a></li>
<li><a href="https://www.bloomberg.com/profile/company/1776316D:US">Oxide Computer Co - Company Profile and News - Bloomberg Markets</a></li>
<li><a href="https://en.wikipedia.org/wiki/Form_D">Form D - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some express excitement about the product concept and the company's progress, while others raise concerns about product availability and sales responsiveness. One commenter noted that they submitted a sales inquiry but never received a response, despite spending $900k/year on AWS, while another questioned whether Oxide actually ships hardware to customers.

**Tags**: `#funding`, `#hardware`, `#startup`, `#Oxide Computer`

---

<a id="item-5"></a>
## [LLM 0.32 Adds Reasoning Traces, Server-Side Tools, and Smarter Logging](https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything) ⭐️ 8.0/10

LLM 0.32, released on August 4, 2026, introduces visible reasoning traces for reasoning models, support for server-side tools like OpenAI's CodeInterpreter and WebSearch, and redesigned content-addressable SQLite logs. It also adds the GPT-5.6 model family with GPT-5.6 Luna as the new default model, and a new 'llm openai endpoint' command for one-off prompts against any OpenAI-compatible endpoint. This release significantly enhances the usability of LLM, a widely-used CLI tool, by making reasoning traces visible and enabling server-side tools, which aligns with current AI trends toward agentic workflows. The improvements to logging and the new endpoint command also streamline workflows for developers and power users, potentially increasing adoption and productivity. Reasoning traces are displayed to standard error by default, with a -R/--hide-reasoning flag to disable them. The llm-anthropic plugin adds WebSearch, WebFetch, CodeExecution, and AnthropicMCP tools, enabling MCP calls within a single request. The 'llm openai endpoint' command does not log prompts, making it ideal for one-off interactions.

rss · Simon Willison · Aug 4, 23:58

**Background**: LLM is a CLI tool and Python library for interacting with various large language models, storing results in SQLite, and generating embeddings. It supports plugins for additional models and tools. The OpenAI Responses API, released in March 2025, simplifies agentic applications by combining chat completions with advanced tool-calling capabilities, which LLM 0.32 leverages.

<details><summary>References</summary>
<ul>
<li><a href="https://llm.datasette.io/en/stable/">LLM: A CLI utility and Python library for ... - Datasette</a></li>
<li><a href="https://github.com/simonw/llm">GitHub - simonw/llm: Access large language models from the ... llm - a tool for Datasette LLM: A CLI utility and Python library for interacting with ... llm CLI Tool Guide 2026: Run Any LLM From Your Terminal GitHub - sorokinvld/llmcli: Access large language models from ...</a></li>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#CLI`, `#AI`, `#OpenAI`, `#release`

---

<a id="item-6"></a>
## [MiniMax-H3 Runs on Apple Silicon via MLX Port](https://simonwillison.net/2026/Aug/4/minimax-h3-mlx/#atom-everything) ⭐️ 8.0/10

Simon Willison successfully ran MiniMax's new omni-modal MiniMax-H3 model on an M5 Max MacBook Pro using the PipeNetwork/minimax-h3-mlx Python package, generating a 15-second video clip with audio from a text prompt. The model accepts text, images, audio, and video inputs and generates up to 2K resolution video with native stereo audio. This demonstrates that cutting-edge omni-modal generative models can run locally on consumer Apple hardware, making advanced AI video generation accessible to developers without cloud dependencies. The MLX port lowers the barrier for experimentation and could accelerate adoption of multimodal AI in creative and development workflows. The model download required approximately 115 GB of storage, and generating the video took just under 45 minutes on the M5 Max. The generated audio was described as 'weird speech-like garbage' because no audio-specific prompt guidance was provided, highlighting the importance of following the prompting guide for optimal results.

rss · Simon Willison · Aug 4, 19:10

**Background**: MiniMax-H3 is an open-weights, general-purpose omni-modal generative model that can understand and generate across text, images, video, and audio in a unified architecture. MLX is an array framework from Apple designed for efficient machine learning on Apple silicon, and the MLX port enables running such models locally on Macs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between ...</a></li>
<li><a href="https://fal.ai/minimax-h3">MiniMax H3 - Open-Weights General-Purpose Multimodal Video ...</a></li>
<li><a href="https://github.com/ml-explore/mlx">GitHub - ml-explore/mlx: MLX: An array framework for Apple silicon · GitHub</a></li>

</ul>
</details>

**Tags**: `#MLX`, `#MiniMax-H3`, `#multimodal`, `#Apple Silicon`, `#video generation`

---

<a id="item-7"></a>
## [Open-Weight AI Models Catch Up to Frontier, Safety Gap Widens](https://techcrunch.com/2026/08/04/open-weight-ai-models-are-catching-up-to-the-frontier-the-safety-gap-remains/) ⭐️ 8.0/10

A new SaferAI report reveals that Z.ai's open-weight GLM-5.2 model is approaching frontier AI capabilities while lacking essential safety mitigations, intensifying concerns about governance and oversight. This development highlights the growing tension between the rapid advancement of open-weight models and the slower pace of safety and governance frameworks. It could influence policy debates on how to regulate powerful open-source AI systems, affecting developers, researchers, and the broader AI ecosystem. GLM-5.2, developed by Chinese company Z.ai, is an open-weight model released under permissive licenses like MIT or Apache 2.0, allowing local or cloud deployment. The SaferAI report specifically notes that GLM-5.2 approaches frontier capabilities but lacks key safety mitigations, raising concerns about potential misuse.

rss · TechCrunch AI · Aug 4, 20:05

**Background**: Open-weight models are AI models whose learned parameters (weights and biases) are publicly released, allowing others to download and use them, with modification rights depending on the license. Frontier AI refers to the most advanced general-purpose models, often built at high cost and with extensive safety measures. The GLM series, including GLM-5.2, is a flagship open-weight model line from Z.ai, one of China's leading AI companies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>
<li><a href="https://en.wikipedia.org/wiki/Frontier_AI">Frontier AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM-5.2">GLM-5.2</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#open-weight models`, `#frontier AI`, `#governance`, `#GLM-5.2`

---

<a id="item-8"></a>
## [Texas Halts New Data Centers, Orders Audits Amid Power Grid Strain](https://techcrunch.com/2026/08/04/texas-halts-new-data-centers-as-governor-calls-for-audits/) ⭐️ 8.0/10

Texas has halted approvals for new data centers and ordered audits of existing ones due to strain on the power grid, as announced by Governor Greg Abbott. This marks a significant policy shift in the state's previously data-center-friendly environment. This move signals a major shift in data center expansion, highlighting the limits of power infrastructure even in states with loose regulations. It will impact tech companies planning new facilities, energy policy, and regional planning, potentially setting a precedent for other states facing similar challenges. The halt and audits come after Texas Governor Greg Abbott directed agencies to develop regulations for data centers, including requiring them to pay for infrastructure and undergo a screening process. The state's power grid has been strained by rising data center demand, which is projected to nearly triple by 2030.

rss · TechCrunch AI · Aug 4, 15:42

**Background**: Data centers are large facilities that house computer systems and associated components, consuming significant electricity. In the U.S., data center power demand is projected to jump 22% next year and nearly triple by 2030, straining regional grids and driving up costs. Texas, with its loose regulations and abundant power supply, has been a popular destination for data center developers, but the rapid growth has pushed the grid to its limits.

<details><summary>References</summary>
<ul>
<li><a href="https://www.edgesg.com/2026/01/07/data-centers-are-overwhelming-power-grids-worldwide/">Data Centers Are Overwhelming Power Grids Worldwide</a></li>
<li><a href="https://www.fox7austin.com/news/new-texas-data-center-rules">Texas regulators announce new rules for data centers | FOX 7 Austin</a></li>
<li><a href="https://comptroller.texas.gov/taxes/data-centers/">State Sales Tax Exemption for Qualifying Data Centers and ...</a></li>

</ul>
</details>

**Tags**: `#data centers`, `#energy policy`, `#Texas`, `#infrastructure`, `#tech industry`

---

<a id="item-9"></a>
## [AI Cuts Customer Service Jobs at Major Firms](https://www.solidot.org/story?sid=84994) ⭐️ 8.0/10

Major companies including Commonwealth Bank of Australia, Microsoft, Uber, and Hyatt are using AI chatbots and automated phone systems to replace human customer service work, leading to significant job cuts. Microsoft reduced its customer service team from about 50,000 to 40,000, and Uber cut 10% of its customer service roles to embrace AI. This trend signals a major shift in the labor market, with analysts estimating that nearly half of customer service jobs could be affected by 2030. It has broad implications for employment in countries like the US, India, and the Philippines, where millions work in call centers, and highlights the accelerating adoption of generative AI in enterprise operations. Commonwealth Bank of Australia cut hundreds of customer service roles, saving tens of millions of dollars annually. Microsoft's sales and services operations lead Judson Althoff stated that AI saves the company about $750 million per year in customer service costs, while noting that complex issues still require human support. Hyatt cut 30% of its internal customer service staff in the Americas last year.

rss · Solidot 奇客 · Aug 3, 14:22

**Background**: Customer service call centers have traditionally been a major source of employment, especially in countries like India and the Philippines, where Western companies outsourced support roles. Advances in generative AI and pressure on executives to adopt new technologies are driving companies to replace human agents with automated systems. This shift is part of a broader trend of AI automation affecting various job sectors.

<details><summary>References</summary>
<ul>
<li><a href="https://www.commbox.io/the-new-era-of-generative-ai-customer-service-empowering-humans-with-automation/">The New Era of Generative AI Customer Service ... - CommBox</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-in-customer-service">AI in Customer Service | IBM</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Customer Service`, `#Employment`, `#Automation`, `#Industry Trends`

---

<a id="item-10"></a>
## [Kimi K3: Compressed Memory, Cross-Depth Attention, Latent Expert Routing](https://newsletter.semianalysis.com/p/kimi-k3-the-manos-the-mythos-the) ⭐️ 8.0/10

SemiAnalysis published a deep technical breakdown of Kimi K3's architecture, detailing innovations in compressed memory (Kimi Delta Attention), cross-depth attention, and latent expert routing (LatentMoE) that improve inference performance. This analysis is highly relevant for AI/ML researchers and engineers, as Kimi K3's architecture could set new standards for efficient LLM inference, reducing memory footprint and improving speed. The innovations may influence future model designs and inference optimizations across the industry. Kimi K3 uses Kimi Delta Attention (KDA), a compressed attention mechanism similar to Multi-head Latent Attention (MLA), which aggressively reduces per-token KV cache footprint. LatentMoE compresses routed tokens before dispatch and decompresses after aggregation, with an RMSNorm applied before up-projection in the Stable LatentMoE variant.

rss · Semianalysis · Aug 3, 19:42

**Background**: Large language models (LLMs) rely on attention mechanisms that store key-value (KV) caches, which grow with context length and memory usage. Compressed attention like KDA reduces this footprint, while cross-depth attention allows layers to selectively reuse earlier representations, improving information flow. Latent expert routing in Mixture-of-Experts (MoE) models reduces communication overhead by compressing tokens before routing.

<details><summary>References</summary>
<ul>
<li><a href="https://wan27.org/blog/kimi-k3-vram-guide">Kimi K3 VRAM Requirements: How Much Memory You Actually Need to Run K3 | Wan 2.7</a></li>
<li><a href="https://vllm.ai/blog/2026-07-27-k3">Kimi K3 Is Here: Efficient Day-0 Support on vLLM | vLLM Blog</a></li>
<li><a href="https://arxiv.org/abs/2606.05014">Depth-Attention: Cross-Layer Value Mixing for Language Models</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#architecture`, `#inference`, `#Kimi K3`, `#AI research`

---

<a id="item-11"></a>
## [Desk Reject Papers Without Reproducible Code](https://www.reddit.com/r/MachineLearning/comments/1vei12v/its_time_to_desk_reject_papers_that_dont_include/) ⭐️ 8.0/10

A reviewer reports that out of 12 papers reviewed for major ML conferences this year, only 1 provided full runnable code, and 3 of the 5 with partial code had bugs invalidating results. They argue for mandatory code submission with desk rejection as a penalty. This highlights a reproducibility crisis in ML research, where hidden code undermines quality and trust. Mandatory code submission could shift incentives, improving verification and reducing false claims, impacting researchers, reviewers, and the broader AI community. The reviewer notes that 7 of 12 papers provided no code, and only 1 ran the full pipeline from input to AUROC. They propose desk rejection for missing code, citing that current incentives favor hiding code to avoid bug detection.

reddit · r/MachineLearning · /u/Flaky-Ambition5900 · Aug 3, 16:17

**Background**: Desk rejection is when an editor rejects a manuscript without peer review, often for not meeting scope or quality standards. AUROC (Area Under the Receiver Operating Characteristic curve) is a common metric for binary classification performance, ranging from 0.5 (random) to 1.0 (perfect). Reproducibility is a growing concern in ML, as many papers fail to share code, hindering verification.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Receiver_operating_characteristic">Receiver operating characteristic - Wikipedia</a></li>
<li><a href="https://peerreviewai.org/guides/desk-rejection-prevention">How to Avoid Desk Rejection | PeerReviewAI</a></li>

</ul>
</details>

**Tags**: `#reproducibility`, `#machine learning`, `#research practices`, `#peer review`

---

<a id="item-12"></a>
## [Explorative Modeling: A New Pretraining Axis for Generative Models](https://www.reddit.com/r/MachineLearning/comments/1vf6r6f/explorative_modeling_unlocking_a_third/) ⭐️ 8.0/10

The paper introduces 'explorative modeling' as a third pretraining axis beyond parameters and data, where the model explores K candidate matches between its generations and the data, training on the best to avoid mode blurring. This approach enables end-to-end generation and shows monotonic performance improvements across images, video, and language. This work could redefine how generative models are scaled, offering a new axis for improvement that complements existing scaling laws. It may lead to more robust and accurate generation across modalities, impacting both research and practical applications in AI. The method factors the training loop rather than the generation procedure, exploring K candidate matches and training on the best. It is effective in both continuous and discrete domains, including images, video, and language, with exploration scaling monotonically improving performance.

reddit · r/MachineLearning · /u/Benlus · Aug 4, 10:42

**Background**: Traditional generative models scale by increasing parameters and data, but this paper introduces exploration as a third axis. The approach addresses the problem of mode blurring, where models average over multiple plausible outputs, by committing to specific modes during training. This is relevant to the broader trend of improving generative models' fidelity and diversity.

<details><summary>References</summary>
<ul>
<li><a href="https://explorative-modeling.github.io/">Explorative Modeling: Unlocking a Third Pretraining Axis and ...</a></li>
<li><a href="https://arxiv.org/abs/2607.27372">[2607.27372] Explorative Modeling: Unlocking a Third ...</a></li>
<li><a href="https://arxiv.org/html/2607.27372v1">Explorative Modeling: Unlocking a Third Pretraining Axis and ...</a></li>

</ul>
</details>

**Tags**: `#pretraining`, `#machine learning`, `#generative models`, `#research`

---

<a id="item-13"></a>
## [Huawei Unveils 'Tao's Law' for Time-Based Semiconductor Scaling](https://t.me/zaihuapd/42966) ⭐️ 8.0/10

At the 2026 International Symposium on Circuits and Systems (ISCAS) held in Shanghai, Huawei officially proposed 'Tao's Law' (τ-law), advocating a shift from traditional geometric scaling to 'time scaling' in semiconductor advancement. The company claims to have designed and mass-produced 381 chips over the past six years under this principle, with a new Kirin smartphone chip using logic folding technology expected this fall. This announcement is significant as it proposes an alternative to Moore's Law, which is approaching physical limits, potentially reshaping the global semiconductor industry's roadmap. If validated, it could reduce reliance on extreme ultraviolet lithography (EUV) and challenge the dominance of equipment makers like ASML, affecting the competitive landscape. Tao's Law focuses on reducing the time constant (τ) through multi-level co-optimization across devices, circuits, chips, and systems, using logic folding to restructure circuit topology in 3D. Huawei projects that by 2031, high-end chips based on this law could achieve transistor density equivalent to that of a 1.4nm process, and emphasizes open collaboration for industry advancement.

telegram · zaihuapd · Aug 4, 08:04

**Background**: Moore's Law, which predicts that transistor density on integrated circuits doubles roughly every two years, has driven semiconductor progress for decades but is now hitting physical limits. Geometric scaling, the traditional approach of shrinking transistor dimensions, faces challenges such as increased leakage and manufacturing complexity. Tao's Law proposes an alternative by optimizing time-related parameters, potentially extending performance gains without relying solely on lithographic miniaturization. Logic folding, a key technique, involves 3D stacking of circuit logic paths to reduce signal transmission distances, differing from conventional 3D packaging like chiplet integration.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/时间缩微/67842555">时间缩微_百度百科</a></li>
<li><a href="https://www.zhihu.com/question/2042175008198357766">如何评价华为发表的半导体领域新定律“韬（τ）定律”？</a></li>
<li><a href="https://xueqiu.com/1578376429/390887181">华为“韬 (τ)定律”深度研究（半导体产业从“几何缩微”到“时间缩微”的范...</a></li>

</ul>
</details>

**Discussion**: Community discussions on platforms like Zhihu and Xueqiu show mixed reactions. Some express excitement about a potential breakthrough that could reduce reliance on ASML, while others are skeptical, questioning the lack of detailed technical data and the feasibility of achieving 1.4nm-equivalent density by 2031. There is also debate over whether logic folding is truly distinct from advanced packaging, with some clarifying that it is a design-level circuit topology restructuring rather than simple die stacking.

**Tags**: `#semiconductors`, `#Huawei`, `#Moore's Law`, `#chip design`, `#technology`

---

<a id="item-14"></a>
## [Cloudflare Ditches Third-Party Security Tools for $58/Month AI Triage](https://www.theregister.com/security/2026/08/04/cloudflare-has-mostly-ditched-third-party-security-tools-suggests-not-trying-that-at-home/5282600) ⭐️ 8.0/10

Cloudflare's CISO Grant Bourzikas revealed that the company has automated vulnerability bounty triage using Anthropic's Claude Sonnet model for just $58 per month, and has built over 200 autonomous security agents, largely replacing third-party security tools. This demonstrates a significant shift toward AI-driven security operations, with dramatic cost savings compared to specialized models (Mythos would cost ~$200k/month). It highlights the potential for AI to transform security workflows, though Cloudflare advises others not to follow suit due to its unique in-house capabilities. The $58/month figure applies to Claude Sonnet for deduplication and value assessment of vulnerability reports, while the security-specific Mythos model would cost ~$200k/month for the same task. Cloudflare has also built 200+ autonomous security agents and replaced most third-party tools with in-house applications, some AI-assisted. CISO Bourzikas cautioned that not every company should develop its own security software.

telegram · zaihuapd · Aug 4, 09:24

**Background**: Cloudflare is a major web infrastructure and security company that has increasingly integrated AI into its products. Claude Sonnet is Anthropic's cost-effective LLM, while Mythos is a specialized cybersecurity model known for offensive security capabilities. The company's move reflects a broader trend of using general-purpose LLMs for security tasks, as seen in GitHub's use of Claude Sonnet for vulnerability triage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.adwaitx.com/github-ai-taskflow-agent-vulnerability-triage/">GitHub Deploys AI to Triage Vulnerabilities : 30 Flaws Found</a></li>
<li><a href="https://www.speakeasy.com/blog/mythos-security-story/">The Mythos security story is only half told</a></li>
<li><a href="https://www.cloudflare.com/products/agents/">Cloudflare Agents - Build Stateful AI Agents</a></li>

</ul>
</details>

**Tags**: `#AI`, `#security`, `#Cloudflare`, `#vulnerability management`, `#automation`

---

<a id="item-15"></a>
## [Google Builds $200B Wall Street Financing Machine for Anthropic](https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c) ⭐️ 8.0/10

Google has quietly constructed a massive infrastructure financing structure worth approximately $200 billion to deliver over $150 billion in AI chips to Anthropic. The first transactions, completed in June via a special purpose vehicle called Compute SPV, involved about $35 billion in hardware, equivalent to 1 gigawatt of compute and 1 million TPUs. This novel vendor-financing model distributes risk among multiple parties, enabling Anthropic to access vast AI compute without a credit rating. It could reshape how AI infrastructure is funded and accelerate the deployment of large-scale AI models, impacting the entire AI ecosystem. The structure involves Google guaranteeing data centers, Broadcom purchasing and helping finance chips, and Apollo and Blackstone buying hardware to lease back to Anthropic. About 80% of the contracts are directly tied to chips, with participants including Morgan Stanley and several crypto mining firms.

telegram · zaihuapd · Aug 4, 10:52

**Background**: Vendor financing is a credit arrangement where a seller provides a loan to a buyer, often used for expensive equipment. Google's Tensor Processing Units (TPUs) are custom AI chips designed to accelerate machine learning workloads. This model is inspired by how Boeing and GE finance aircraft and engines, keeping large hardware assets off balance sheets.

<details><summary>References</summary>
<ul>
<li><a href="https://nucleuscommercialfinance.com/finance-glossary/vendor-finance/">Vendor Finance | What is Vendor Finance for Business?</a></li>
<li><a href="https://www.linkedin.com/pulse/googles-ai-tpus-secret-engine-powering-revolution-bayonle-akinmurele-wkmuf">Google's AI TPUs : The Secret Engine Powering the AI Revolution</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#Google`, `#Anthropic`, `#financing`, `#chips`

---

<a id="item-16"></a>
## [China's First Mandatory L3/L4 Autonomous Driving Standard Submitted for Approval](https://t.me/zaihuapd/42972) ⭐️ 8.0/10

China's Ministry of Industry and Information Technology (MIIT) has completed the draft of the mandatory national standard 'Safety Requirements for Autonomous Driving Systems of Intelligent Connected Vehicles' and opened it for public comment starting June 17. The standard is recommended to take effect on July 1, 2027, making it China's first mandatory national standard for L3 and L4 autonomous driving. This standard marks a shift in China's autonomous driving regulation from loose concepts to hard safety constraints, introducing a Safety Case mechanism that requires companies to systematically demonstrate safety. It will significantly impact automakers and technology providers, forcing them to move away from vague marketing and adopt rigorous safety validation practices. The standard introduces the Safety Case mechanism, requiring companies to use a 'claim-argument-evidence' structure to prove safety. It also specifies distinct requirements for L3 human-machine handover (including driver takeover capability monitoring) and L4 system autonomous risk handling, as well as requirements for human-machine interaction and user notification to prevent misuse.

telegram · zaihuapd · Aug 4, 13:06

**Background**: Autonomous driving is categorized into levels from L0 to L5, with L3 (conditional automation) and L4 (high automation) being key milestones where the system takes over driving tasks. Safety Case is a structured safety argumentation system supported by evidence, used to prove that a system is acceptably safe in a specific environment, shifting regulatory logic from 'meeting clauses' to 'self-certifying safety'. China's new standard is part of a global trend where autonomous driving safety regulation is entering the Safety Case era.

<details><summary>References</summary>
<ul>
<li><a href="https://yfrobotics.github.io/self-driving-handbook-cn/system/safety/">系统安全保障 - 自动驾驶指南 - GitHub Pages</a></li>
<li><a href="https://baike.baidu.com/item/Safety+Case/67871945">Safety Case - 百度百科</a></li>
<li><a href="https://www.autohome.com.cn/news/202608/1316205.html">autohome.com.cn/news/202608/1316205.html</a></li>

</ul>
</details>

**Tags**: `#autonomous driving`, `#regulation`, `#China`, `#safety standard`, `#L3/L4`

---