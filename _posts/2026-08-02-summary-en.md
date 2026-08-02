---
layout: default
title: "Horizon Summary: 2026-08-02 (EN)"
date: 2026-08-02
lang: en
---

> From 74 items, 12 important content pieces were selected

---

1. [OpenAI's Astra Model Achieves Breakthroughs on Ten Long-Standing Math Problems](#item-1) ⭐️ 9.0/10
2. [Go 1.27 Introduces Generic Type Aliases and Auto HTTP Body Draining](#item-2) ⭐️ 8.0/10
3. [ByteDance Launches Seedance 2.5 Video Generation Model](#item-3) ⭐️ 8.0/10
4. [EU Orders Google to Open Android Features to Rivals](#item-4) ⭐️ 8.0/10
5. [Postmortem of Lean Kernel Soundness Bug #14576](#item-5) ⭐️ 8.0/10
6. [DeepSeek V4 Flash 0731: Top Value-Per-Intelligence Model](#item-6) ⭐️ 8.0/10
7. [Stateless MCP 2.0 Reignites Interest, Inspires New Tools](#item-7) ⭐️ 8.0/10
8. [KataGo Study Reveals How Go Neural Networks Handle Board Symmetries](#item-8) ⭐️ 8.0/10
9. [User Trains Encoder-Only Transformer to Predict Blood Sugar](#item-9) ⭐️ 8.0/10
10. [VLMs Score Well on Benchmarks While Erasing Clinical Terms and Introducing Bias](#item-10) ⭐️ 8.0/10
11. [China Promotes Open-Weight AI Models to Global South at UN Summit](#item-11) ⭐️ 8.0/10
12. [Microsoft Confirms Copilot 'Super App' Launch This Year](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI's Astra Model Achieves Breakthroughs on Ten Long-Standing Math Problems](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 9.0/10

OpenAI announced that an internal version of its next-generation model, Astra, has produced new results on ten long-standing open problems in mathematics and theoretical computer science, including high-dimensional sphere packing, the existence of non-Sofic groups, a counterexample to Connes' rigidity conjecture, arithmetic circuit lower bounds, quantum parallel repetition, the hardness of the closest vector problem, and multicolor Ramsey numbers. The model generated arguments at a token cost of approximately $2,000 per problem, and the results were formalized in Lean. This milestone demonstrates that AI can contribute to frontier mathematical research, potentially accelerating discovery and transforming how mathematicians work. It also raises important questions about authorship, verification, and the role of AI in academia, as the proofs were AI-generated and human-formalized. The results are detailed in a paper and formalized in Lean 4, with a repository (openai/ten-proofs) containing the formalizations. OpenAI also released an LLM-generated PDF that reconstructs the reasoning process. Notably, the model's token cost was under $2,000 per problem, but the number of problems attempted without success was not disclosed.

telegram · zaihuapd · Aug 1, 07:59

**Background**: Lean is an open-source proof assistant that allows formal verification of mathematical proofs, ensuring correctness. Connes' rigidity conjecture, proposed in 1980, predicts that certain von Neumann algebras completely determine the underlying group; a counterexample would be a major result. The AI model Astra is an internal version of OpenAI's next major model, and its use in mathematics reflects a trend toward 'big mathematics' where humans and AI collaborate on complex problems.

<details><summary>References</summary>
<ul>
<li><a href="https://lean-lang.org/">Lean Programming Language</a></li>
<li><a href="https://www.implicator.ai/openai-astra-10-math-problems-lean-proofs/">OpenAI Says Astra Solved 10 Math Problems With Lean Proofs</a></li>
<li><a href="https://math.ucsd.edu/seminar/connes-rigidity-conjecture">On Connes' rigidity conjecture | Department of Mathematics</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion highlights a mix of awe and concern, with some mathematicians experiencing a 'Deep Blue' moment, while others call for transparency about prompts and failed attempts. The sentiment is largely positive but cautious, emphasizing the need for rigorous review.

**Tags**: `#AI research`, `#mathematics`, `#OpenAI`, `#formal verification`, `#breakthrough`

---

<a id="item-2"></a>
## [Go 1.27 Introduces Generic Type Aliases and Auto HTTP Body Draining](https://victoriametrics.com/blog/go-1-27/index.html) ⭐️ 8.0/10

Go 1.27, as highlighted in an interactive tour by VictoriaMetrics, brings major features including generic type aliases and automatic HTTP response body draining. The release also includes a fix for runtime.findnull() to be compatible with Memory Tagging Extension (MTE) on Android. These changes are significant for the Go ecosystem as they simplify code and improve performance, but the automatic draining behavior could subtly affect applications relying on the old behavior. The community's mixed reactions highlight the balance between innovation and stability in a widely-used language. Generic type aliases, previously experimental, are now enabled by default, allowing aliases to have type parameters. The automatic HTTP response body draining reads up to 256KB or waits 50 milliseconds after close, which may cause unexpected delays or resource usage in some cases.

hackernews · Hixon10 · Aug 2, 01:35 · [Discussion](https://news.ycombinator.com/item?id=49140218)

**Background**: Go is a statically typed, compiled programming language known for its simplicity and strong standard library. Generic type aliases allow developers to create aliases for generic types, improving code reuse and readability. Automatic HTTP response body draining aims to prevent connection leaks by ensuring response bodies are fully read or closed, a common source of goroutine leaks in Go applications.

<details><summary>References</summary>
<ul>
<li><a href="https://go.dev/blog/alias-names">A description of generic alias types , a planned feature for Go 1 .24</a></li>
<li><a href="https://github.com/golang/go/issues/77370">net/http: drain response body after close #77370 - GitHub</a></li>
<li><a href="https://dev.to/snhacker9/debugging-a-goroutine-leak-caused-by-missing-respbodyclose-in-go-4n6g">Debugging a Goroutine Leak Caused by Missing resp.Body.Close ...</a></li>

</ul>
</details>

**Discussion**: Community comments show a mix of enthusiasm and caution. Some praise the standard library improvements, while others express concern about the silent behavior change in HTTP response draining. One commenter criticizes the use of 'LLM-isms' in the release notes, and another highlights the MTE fix as a positive for Android security.

**Tags**: `#Go`, `#programming languages`, `#release`, `#standard library`, `#generics`

---

<a id="item-3"></a>
## [ByteDance Launches Seedance 2.5 Video Generation Model](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) ⭐️ 8.0/10

ByteDance officially launched Seedance 2.5, a next-generation video generation model that can produce up to 30-second audio-video clips in a single pass and supports multi-round extensions. It introduces 50 multimodal references, timestamp-level editing control, and enhanced features like green screen and camera perspective control. This release marks a significant advancement in AI video generation, offering longer, higher-quality outputs with more precise control, which could impact filmmakers and content creators. The community discussion highlights differing market demands between China and the West, and the competitive landscape with open-weight models like MiniMax H3. Seedance 2.5 supports up to 30 seconds per generation with multi-round extensions, and includes 50 multimodal references for input. It also offers timestamp-level control for targeted editing of audio and video, and advanced features such as green screen and camera perspective control.

hackernews · njaremko · Aug 1, 20:45 · [Discussion](https://news.ycombinator.com/item?id=49138302)

**Background**: Seedance is ByteDance's series of AI video generation models. The 2.5 version builds on previous iterations, focusing on longer, more controllable video creation. Video generation models use deep learning to create video from text, images, or other videos, and are increasingly used in creative industries for storyboarding, prototyping, and content production.

<details><summary>References</summary>
<ul>
<li><a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5">Seedance 2.5 — One-take Creation, Flexible Referencing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Seedance_2.0">Seedance 2.0 - Wikipedia</a></li>
<li><a href="https://www.seeddance.io/models/seedance-2-5">Seedance 2 . 5 Free: Try ByteDance AI Video , No Queue, Instant Results</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed sentiment: some praise the quality and fun of using the model, while others express concerns about cost and ethical implications. A notable observation is the model's focus on action/high-effect shots, which may reflect differing market demands between China and the West. Some users prefer open-weight alternatives like MiniMax H3 for control and cost, and one commenter questions the existence of such generative tools due to potential harm.

**Tags**: `#AI`, `#video generation`, `#ByteDance`, `#machine learning`, `#creative tools`

---

<a id="item-4"></a>
## [EU Orders Google to Open Android Features to Rivals](https://www.openhomefoundation.org/blog/a-big-win-for-android-interoperability/) ⭐️ 8.0/10

The European Commission has mandated that Google make 11 Android features accessible to third parties under the Digital Markets Act, with most required by August 2027. This includes enabling rival AI assistants to integrate deeply with the OS and share anonymized search data. This ruling significantly challenges Google's control over Android, potentially boosting competition and innovation in AI and mobile services. It could set a precedent for how dominant platforms are regulated globally, affecting developers, users, and tech giants like OpenAI. The 11 features include structured on-device integration for AI services, allowing them to interact with other apps and perform tasks on behalf of users. Support for multiple assistants listening for wake words simultaneously is required by August 2028 with Android 19.

hackernews · soheilpro · Jul 31, 15:01 · [Discussion](https://news.ycombinator.com/item?id=49124051)

**Background**: The Digital Markets Act (DMA) is an EU regulation aimed at curbing the power of 'gatekeeper' platforms like Google. The European Commission's July 2026 decisions clarify how Google must comply, addressing Android interoperability and search data access. This is part of broader efforts to ensure fair competition in digital markets.

<details><summary>References</summary>
<ul>
<li><a href="https://www.remio.ai/post/google-must-open-android-and-search-to-rivals-putting-gemini-s-platform-advantage-at-risk">Google Must Open Android and Search to Rivals, Putting...</a></li>
<li><a href="https://innopanda.com/eu-forces-google-to-open-android-to-rival-ai-agents/">EU Forces Google to Open Android to Rival AI Agents</a></li>
<li><a href="https://windowsforum.com/windows-news.4/google-android-must-open-ai-assistant-access-in-eu-by-july-2027.439760/">Google Android Must Open AI Assistant Access in EU by July 2027</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely positive, with praise for the EU's role in holding corporations accountable. Some commenters highlight specific features like AI integration, while others express skepticism, noting that the core issue of allowing small businesses to sell modified Android devices remains unresolved.

**Tags**: `#Android`, `#Interoperability`, `#Regulation`, `#EU`, `#Digital Markets Act`

---

<a id="item-5"></a>
## [Postmortem of Lean Kernel Soundness Bug #14576](https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/) ⭐️ 8.0/10

A detailed postmortem of a soundness bug in Lean's kernel, bug #14576, was published, highlighting the fragility of even verified systems and the need for independent checking. This bug undermines the core guarantee of Lean, a widely-used proof assistant, affecting formal verification and programming language theory. It underscores the importance of independent kernel checking and the limitations of relying solely on a single implementation. The bug required two distinct bugs in two implementations to be exploited, meaning independent checking with current versions still works. The postmortem likely discusses the root cause, fix, and implications for the Lean ecosystem.

hackernews · juhopitk · Aug 1, 18:32 · [Discussion](https://news.ycombinator.com/item?id=49137060)

**Background**: Lean is a theorem prover and programming language with a small, trusted kernel that checks proofs. Soundness bugs in the kernel are critical because they can allow unsound proofs to be accepted. Independent kernel checkers, such as those developed in the Lean4Lean project, help mitigate such risks by providing a separate verification path.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2403.14064">[2403.14064] Lean4Lean: Verifying a Typechecker for Lean, in Lean</a></li>
<li><a href="https://news.ycombinator.com/item?id=49137060">Postmortem for Kernel Soundness Bug #14576 | Hacker News</a></li>
<li><a href="https://ammkrn.github.io/type_checking_in_lean4/whats_a_kernel.html">What's a kernel? - Type Checking in Lean 4 - GitHub Pages</a></li>

</ul>
</details>

**Discussion**: Community comments express a range of views: some note that soundness bugs are not surprising given similar issues in other systems like Rust, while others argue that such bugs highlight the fragility of the ideology behind proof assistants. Some suggest that alternative systems like Metamath might be more robust, and there is a call for further work on independent checking and verification of the kernel itself.

**Tags**: `#Lean`, `#formal verification`, `#soundness bug`, `#theorem prover`, `#kernel`

---

<a id="item-6"></a>
## [DeepSeek V4 Flash 0731: Top Value-Per-Intelligence Model](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek released DeepSeek-V4-Flash-0731, a 304B parameter model with substantially enhanced agentic capabilities, scoring 82.7 on Terminal Bench 2.1 and 54.4 on DeepSWE. It is priced at $0.14 per million input tokens and $0.27 per million output tokens, and is ranked by Artificial Analysis as the best value-per-intelligence model currently available. This release offers top-tier performance at a fraction of the cost of competitors, potentially disrupting the AI model market by making advanced agentic capabilities more accessible. It could pressure other providers to lower prices or improve efficiency, benefiting developers and businesses that rely on LLMs. The model has a 1,048,576-token context window and supports up to 384K output tokens, with reasoning, tool calling, and structured JSON output. It uses FP4 and FP8 mixed precision for efficiency, and supports three reasoning effort modes; however, it does not include a Jinja-format chat template, requiring custom encoding scripts.

rss · Simon Willison · Jul 31, 23:59

**Background**: DeepSeek is a Chinese AI research company known for releasing open-weight models that compete with leading proprietary models. The V4-Flash-0731 is part of the V4 family, which includes a Pro version and a Flash version optimized for cost-efficiency. Artificial Analysis Intelligence Index is a benchmark that aggregates multiple tests to measure model intelligence, and the model's strong performance relative to its cost makes it attractive for budget-conscious users.

<details><summary>References</summary>
<ul>
<li><a href="https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash | vLLM Recipes</a></li>
<li><a href="https://www.orcarouter.ai/blog/deepseek-v4-flash-official-release">DeepSeek V4 Flash: Official Release, Explained</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion highlights the model's impressive cost-performance ratio, with some users noting that it outperforms much larger models like MiniMax M3. However, some users reported mixed results with image generation at default reasoning settings, suggesting that higher reasoning effort is needed for complex tasks.

**Tags**: `#AI`, `#DeepSeek`, `#LLM`, `#model release`, `#cost efficiency`

---

<a id="item-7"></a>
## [Stateless MCP 2.0 Reignites Interest, Inspires New Tools](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 8.0/10

Simon Willison reports that the release of MCP 2.0 (the 2026-07-28 Model Context Protocol specification) has reignited his interest in the protocol, leading him to build three new tools, including mcp-explorer and datasette-mcp. The new stateless design simplifies client and server implementation by eliminating the need for session IDs and multi-step initialization. This update marks a significant milestone in the AI tooling ecosystem, making MCP more accessible and scalable for web applications. It could shift developer preference back from terminal-based agent harnesses to more auditable and controllable MCP tools, especially for smaller models. The stateless MCP uses a single HTTP request with headers like MCP-Protocol-Version and Mcp-Method, replacing the previous two-step initialize and call process. This reduces server-side state management and improves scalability, but may increase repetitive data in requests.

rss · Simon Willison · Jul 31, 23:13

**Background**: MCP (Model Context Protocol) is an open protocol introduced by Anthropic in November 2024 to standardize how LLM agents access external tools and data. It gained huge popularity in 2025 but was later overshadowed by 'Skills' and terminal-based approaches. Stateless protocols, like HTTP, do not retain session state between requests, offering better visibility, reliability, and scalability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stateless_protocol">Stateless protocol</a></li>
<li><a href="https://www.linkedin.com/pulse/new-mcp-stateless-here-what-actually-changes-arnold-cartagena-dpcte">The new MCP is stateless . Here is what actually changes.</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#AI`, `#LLM`, `#tools`, `#specification`

---

<a id="item-8"></a>
## [KataGo Study Reveals How Go Neural Networks Handle Board Symmetries](https://www.reddit.com/r/MachineLearning/comments/1vcrki2/how_symmetric_are_the_insides_of_a_go_network_r/) ⭐️ 8.0/10

The maintainer of KataGo published a research study analyzing how superhuman Go-playing neural networks internally represent board symmetries, finding that they learn orientation-invariant concepts to a significant degree despite only using stochastic 8-fold data augmentation during training. The study includes an unexpected finding and is accompanied by code and an educational writeup. This study contributes to neural network interpretability, particularly for board games like Go, and could inform model design by showing how symmetry can be learned implicitly. It also provides insights into the internal representations of strong AI systems, which is valuable for the broader ML community. The study uses KataGo, an open-source Go AI, and examines the degree to which its neural networks learn orientation-invariant concepts. The writeup was largely AI-generated but with detailed human direction and feedback, and the code is linked from the post.

reddit · r/MachineLearning · /u/icosaplex · Aug 1, 16:18

**Background**: Go is a board game with complete symmetry under rotation and reflection, but KataGo's neural networks do not enforce this symmetry; instead, they rely on stochastic 8-fold data augmentation during training. This study explores whether the networks automatically learn to represent the board independently of orientation, which is relevant to understanding how neural networks handle symmetries in general.

<details><summary>References</summary>
<ul>
<li><a href="https://deepwiki.com/lightvector/KataGo/7.2-model-architecture">Model Architecture | lightvector/KataGo | DeepWiki</a></li>
<li><a href="https://github.com/lightvector/KataGo">GitHub - lightvector/KataGo: GTP engine and self-play ... KataGo Distributed Training KataGo - Networks for kata1 KataGo — Grokipedia KataGo/docs/KataGoMethods.md at master · lightvector/KataGo</a></li>
<li><a href="https://medium.com/@youpiter.dr/symmetry-for-data-scientists-how-go-engines-turn-one-position-into-eight-and-you-can-too-30312158da87">Symmetry for Data Scientists: How Go Engines Turn One ...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#interpretability`, `#Go`, `#neural networks`, `#symmetry`

---

<a id="item-9"></a>
## [User Trains Encoder-Only Transformer to Predict Blood Sugar](https://www.reddit.com/r/MachineLearning/comments/1vc1txc/i_have_trained_a_model_to_predict_my_blood_sugar_p/) ⭐️ 8.0/10

A Reddit user trained an encoder-only transformer to predict blood glucose levels up to 2 hours ahead using past and future meal/insulin data, with multiple model sizes and training strategies. The largest model has ~17 million parameters and was pretrained on a simulator, then finetuned on real diabetes datasets. This demonstrates a practical application of transformer models to personalized health monitoring, potentially enabling more accurate glucose forecasting for diabetes management. It highlights the feasibility of running such models on mobile devices, which could improve patients' quality of life. The model uses BERT-style bidirectional attention with future blood glucose masked, and combines DILATE loss for median prediction and pinball loss for uncertainty bands. It operates in Kovatchev risk space reparameterized to [40, 400] mg/dL, and can work autoregressively to predict beyond 2 hours.

reddit · r/MachineLearning · /u/0xdeadf1sh · Jul 31, 20:09

**Background**: Encoder-only transformers, like BERT, are designed for representation learning and are typically used for tasks like sentiment analysis. DILATE loss is a loss function for time series forecasting that optimizes both shape and temporal alignment, while pinball loss is used for quantile regression to estimate uncertainty. The model requires announced meals and insulin doses, which limits its use in unannounced scenarios.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/BERT_(language_model)">BERT (language model) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Transformer_(deep_learning)">Transformer (deep learning) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quantile_regression">Quantile regression - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community discussion likely includes questions about the model's architecture, training data, and practical deployment, as well as feedback on its limitations. Some may express interest in the open-source release and potential improvements, while others might raise concerns about data privacy and generalizability.

**Tags**: `#transformer`, `#health`, `#blood glucose prediction`, `#time series`, `#deep learning`

---

<a id="item-10"></a>
## [VLMs Score Well on Benchmarks While Erasing Clinical Terms and Introducing Bias](https://www.reddit.com/r/MachineLearning/comments/1vcipzz/vlms_can_score_well_on_benchmarks_while_silently/) ⭐️ 8.0/10

A new paper introduces a framework to measure clinical terminology erasure and biased term introduction in radiology report generation (RRG) by vision-language models (VLMs), revealing that current benchmark metrics reward repetitive, clinically meaningless reports. This matters because high benchmark scores can mask clinically significant failures in AI-generated medical reports, potentially leading to misdiagnosis or overlooked findings. The framework provides a way to evaluate VLMs more accurately for healthcare applications, where precision and clinical relevance are critical. The paper is titled 'Measuring What VLMs Don't Say: Validation Metrics Hide Clinical Terminology Erasure in Radiology Report Generation' and is available on arXiv (2603.01625). The authors observed that VLMs often erase rare but clinically meaningful terms, making reports repetitive and of no clinical utility.

reddit · r/MachineLearning · /u/ade17_in · Aug 1, 09:27

**Background**: Vision-language models (VLMs) are increasingly used for automated radiology report generation, but their evaluation often relies on reference-based metrics like BLEU or ROUGE, which compare generated text to ground truth. These metrics can be gamed by generating repetitive or generic templates, and they do not penalize the omission of clinically important terms. The new framework aims to address this gap by directly measuring term erasure and bias introduction.

<details><summary>References</summary>
<ul>
<li><a href="https://learnopencv.com/vlm-evaluation-metrics/">The Ultimate Guide To VLM Evaluation Metrics ... | LearnOpenCV</a></li>
<li><a href="https://github.com/mk-runner/Awesome-Radiology-Report-Generation">GitHub - mk-runner/Awesome-Radiology-Report-Generation: paper list, dataset, and tools for radiology report generation · GitHub</a></li>
<li><a href="https://arxiv.org/html/2309.14381">Survey of Social Bias in Vision - Language Models</a></li>

</ul>
</details>

**Tags**: `#VLM`, `#evaluation metrics`, `#radiology report generation`, `#bias`, `#clinical AI`

---

<a id="item-11"></a>
## [China Promotes Open-Weight AI Models to Global South at UN Summit](https://www.semafor.com/article/07/28/2026/token-diplomacy-how-china-is-shaping-the-worlds-ai-future) ⭐️ 8.0/10

At the UN 'AI for Good' summit in Geneva in late July, China sent a delegation to promote its open-weight AI models to countries like Pakistan, Russia, and Zambia. Alibaba Cloud architect Wang Jian stated that Chinese AI could serve as a 'cornerstone' for other nations' development, akin to energy. This move highlights China's strategy to export AI infrastructure to developing nations, contrasting with the US's closed-model approach. It could reshape global AI adoption and influence, with the US expressing concerns about dependency on Chinese standards. The US State Department spokesperson warned that this could lead to reliance on Chinese infrastructure and standards. The summit also marked the first meeting of the UN's Global Dialogue on AI Governance, where China supported the first global AI standardization resolution.

telegram · zaihuapd · Aug 1, 10:06

**Background**: Open-weight models are AI models whose trained parameters are publicly released, allowing developers to fine-tune and deploy them, unlike closed models where only the API is accessible. China has been actively promoting its open-weight models, such as Alibaba's Qwen and DeepSeek, as affordable alternatives to US offerings, especially for developing countries.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.zhiding.cn/2025/0401/3164906.shtml">OpenAI 将发布自 2019 年以来首个" 开 放 权 重 " 模 型 --人工智能-至顶网</a></li>
<li><a href="https://wap.miit.gov.cn/xwfb/bldhd/art/2026/art_7b206a82ae3844fd981ff3e42daf0267.html">李乐成率团出席联合国人工智能治理全球对话首次会议等系列活动</a></li>
<li><a href="https://www.neican.ai/insights/aws-bedrock-ai-20250919121005080-1/">开 放 权 重 的云端跃迁：AWS Bedrock 如何 重 塑企业AI的未来格局 | AI内参</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#geopolitics`, `#open-source AI`, `#China`, `#global south`

---

<a id="item-12"></a>
## [Microsoft Confirms Copilot 'Super App' Launch This Year](https://www.theverge.com/tech/972927/microsoft-copilot-super-app-confirmed) ⭐️ 8.0/10

Microsoft CEO Satya Nadella confirmed on an earnings call that the company will launch an AI 'super app' this year, merging Copilot's chat, coding, and agentic capabilities for both consumers and businesses. The app will consolidate experiences like Copilot, GitHub Copilot, Copilot Cowork, and Autopilot systems. This move signals a major strategic direction for Microsoft, consolidating its AI offerings into a single platform, which could reshape how users interact with AI across work and personal contexts. It also intensifies competition with OpenAI's ChatGPT Work and other AI super apps, potentially accelerating the adoption of agentic AI in everyday workflows. Nadella described Copilot evolving from a chat tool to 'Cowork' and then 'Autopilots,' with the super app integrating these experiences, including coding features, this quarter. Microsoft's quarterly revenue rose to $90 billion, driven by AI and cloud businesses, providing financial backing for this initiative.

telegram · zaihuapd · Aug 1, 13:18

**Background**: Copilot is Microsoft's AI assistant integrated across its products, and 'Cowork' is a feature that automates tasks and workflows in Microsoft 365, while 'Autopilot' refers to autonomous AI systems that execute end-to-end processes. The concept of a 'super app' is a single application that combines multiple services, popularized by apps like WeChat, and Microsoft aims to create a similar hub for AI capabilities. This announcement follows OpenAI's launch of ChatGPT Work, which integrates ChatGPT and Codex, indicating a trend toward consolidating AI tools.

<details><summary>References</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/microsoft-365-copilot/cowork">Copilot Cowork: Automate Tasks and Workflows | Microsoft</a></li>
<li><a href="https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/">Copilot Cowork: A new way of getting work done | Microsoft 365 Blog</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#Copilot`, `#AI`, `#Super App`, `#Product News`

---