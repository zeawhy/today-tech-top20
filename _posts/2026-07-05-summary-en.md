---
layout: default
title: "Horizon Summary: 2026-07-05 (EN)"
date: 2026-07-05
lang: en
---

> From 30 items, 9 important content pieces were selected

---

1. [F-Droid Declares Google ADV Malware on 4 Billion Devices](#item-1) ⭐️ 9.0/10
2. [Shadcn/UI switches default from Radix to Base UI](#item-2) ⭐️ 8.0/10
3. [EU Council Fast-Tracks Chat Control 1.0](#item-3) ⭐️ 8.0/10
4. [Newer Claude Models Worse at Tool Call Schema Adherence](#item-4) ⭐️ 8.0/10
5. [Competence Gate: Gating Tool Use via Internal Confidence](#item-5) ⭐️ 8.0/10
6. [USAF: Sparse Fine-Tuning for MoE on Consumer GPUs](#item-6) ⭐️ 8.0/10
7. [Guardian: OpenAI Never Visited Key Stargate UK Site, $30B Pledge a Stunt](#item-7) ⭐️ 8.0/10
8. [Fudan Exam: Students Stump AI to Test Critical Thinking](#item-8) ⭐️ 8.0/10
9. [SpaceX Shows Investors Thinner-than-iPhone Prototype](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [F-Droid Declares Google ADV Malware on 4 Billion Devices](https://f-droid.org/2026/07/01/adv-malware.html) ⭐️ 9.0/10

F-Droid has officially classified Google's Android Developer Verifier (ADV) as malware, stating it is pre-installed on approximately 4 billion Android devices and will begin restricting unapproved software installations in select countries starting September 2026. This marks a significant escalation in the conflict between Google's centralized control over Android and the open-source community, potentially threatening user freedom and the viability of alternative app stores like F-Droid. ADV runs as a system service with root privileges and cannot be removed; it will first activate in Brazil, Indonesia, Singapore, and Thailand on September 30, 2026, with global rollout planned for 2027 and beyond.

telegram · zaihuapd · Jul 5, 00:41

**Background**: F-Droid is a free and open-source app repository for Android, offering only libre software. Google Play Protect is a built-in security service that scans apps for malware. ADV is a new Google system service that verifies developer identities and can block apps not approved by Google, which F-Droid argues gives Google arbitrary power to label any unwanted software as malware.

<details><summary>References</summary>
<ul>
<li><a href="https://f-droid.org/2026/07/01/adv-malware.html">What We Talk About When We Talk About Malware | F-Droid - Free and Open Source Android App Repository</a></li>
<li><a href="https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html">Android Developers Blog: Android developer verification: Rolling out to all developers on Play Console and Android Developer Console</a></li>
<li><a href="https://developer.android.com/developer-verification">Android developer verification | Android Developers</a></li>

</ul>
</details>

**Tags**: `#Android`, `#malware`, `#F-Droid`, `#Google`, `#digital rights`

---

<a id="item-2"></a>
## [Shadcn/UI switches default from Radix to Base UI](https://ui.shadcn.com/docs/changelog) ⭐️ 8.0/10

Shadcn/UI, a popular React component library, has changed its default underlying UI library from Radix to Base UI, as announced in its changelog. This shift affects the default components provided by the library. This change impacts a large developer community that relies on Shadcn/UI for building React applications, as it alters the default component architecture and may require migration efforts. It also signals a broader trend in the UI library ecosystem toward Base UI, which is built by contributors from MUI, Radix, and Floating UI. Base UI is an unstyled, accessible React component library, while Radix UI also provides unstyled primitives. The migration from Radix to Base UI may involve changes in component APIs and behavior, and the community discussion highlights concerns about AI-generated announcements, div overuse, and the shift from codemods to LLMs for migration.

hackernews · dabinat · Jul 5, 04:46 · [Discussion](https://news.ycombinator.com/item?id=48791328)

**Background**: Shadcn/UI is a widely-used React component library that provides beautifully-designed, accessible components via a copy-paste or CLI installation approach. It originally used Radix UI as its default primitive library for unstyled, accessible components. Base UI is a newer alternative, also unstyled and accessible, built by a team including former contributors to MUI, Radix, and Floating UI.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/shadcn-ui/ui">GitHub - shadcn-ui/ui: A set of beautifully-designed, accessible components and a code distribution platform. Works with your favorite frameworks. Open Source. Open Code. · GitHub</a></li>
<li><a href="https://base-ui.com/">Unstyled UI components for accessible design systems · Base UI</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed reactions: some find the AI-generated announcement tone off-putting, others question the copy-paste approach versus traditional libraries like Mantine, and there are concerns about div overuse in Base UI components. A notable point is the shift from codemods to LLMs for migration, with speculation that codemods may become obsolete.

**Tags**: `#React`, `#UI Libraries`, `#Web Development`, `#Open Source`

---

<a id="item-3"></a>
## [EU Council Fast-Tracks Chat Control 1.0](https://www.heise.de/en/news/Chat-Control-1-0-EU-Council-forces-messenger-scans-via-fast-track-11353659.html) ⭐️ 8.0/10

The EU Council has fast-tracked Chat Control 1.0, a regulation that would require messaging providers to scan chats for harmful content, bypassing the usual legislative process. This move raises serious concerns about digital privacy and the future of encryption in the EU, as it could mandate mass surveillance of private communications and undermine end-to-end encryption. Chat Control 1.0 is a temporary derogation from the ePrivacy Directive that was set to expire on April 4, 2026, but the Council's fast-track aims to extend it. Critics argue that there is no technological way to detect child sexual abuse material without high error rates and false positives.

hackernews · stavros · Jul 5, 11:44 · [Discussion](https://news.ycombinator.com/item?id=48793393)

**Background**: Chat Control refers to a set of EU regulations proposed to combat child sexual abuse online. The first iteration, Chat Control 1.0, was a temporary measure allowing voluntary scanning, while the more controversial Chat Control 2.0 would mandate scanning of encrypted messages. The European Parliament had previously rejected extending Chat Control 1.0.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control_1.0">Chat Control 1.0</a></li>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://cdt.org/insights/cdt-europes-response-to-the-european-parliament-rejection-of-the-chat-control-1-0s-extension/">CDT Europe’s Response to the European Parliament Rejection of the Chat Control 1.0's Extension - Center for Democracy and Technology</a></li>

</ul>
</details>

**Discussion**: Community comments express concern about the fast-track process and the erosion of privacy, with some noting that Chat Control 1.0 is less dangerous than Chat Control 2.0 but still problematic. Others criticize the EU institutions for questionable decision-making and highlight the need for more investigation.

**Tags**: `#privacy`, `#EU legislation`, `#encryption`, `#surveillance`, `#technology policy`

---

<a id="item-4"></a>
## [Newer Claude Models Worse at Tool Call Schema Adherence](https://simonwillison.net/2026/Jul/4/better-models-worse-tools/#atom-everything) ⭐️ 8.0/10

Armin Ronacher reports that newer Claude models (Opus 4.8, Sonnet 5) sometimes add extra, invented fields to tool call arguments, causing Pi to reject the calls, while older models do not exhibit this issue. This regression undermines the reliability of LLM-based coding agents that depend on strict schema adherence, and highlights a tension between model training for specific tools and general tool-use capability. The issue appears only with newer Anthropic models, suggesting reinforcement learning for Claude's built-in edit tools may have inadvertently harmed performance on custom schemas. Pi uses its own edit tool schema, which the newer models fail to follow correctly.

rss · Simon Willison · Jul 4, 22:53

**Background**: LLM tool calling allows models to invoke external functions by generating structured JSON arguments matching a provided schema. Coding harnesses like Pi define custom edit tools with specific schemas; if the model produces invalid arguments, the call is rejected. Anthropic and OpenAI train their models to use their own built-in editing tools effectively, which may bias the model against third-party schemas.

<details><summary>References</summary>
<ul>
<li><a href="https://letsdatascience.com/news/newer-claude-models-show-tool-calling-regression-6f029d5f">Newer Claude Models Show Tool-Calling Regression | Let's Data Science</a></li>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling">Programmatic tool calling - Claude Platform Docs</a></li>
<li><a href="https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling">Tool Calling - AI SDK Core</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#tool calling`, `#Anthropic`, `#AI reliability`, `#regression`

---

<a id="item-5"></a>
## [Competence Gate: Gating Tool Use via Internal Confidence](https://www.reddit.com/r/MachineLearning/comments/1unw5un/competence_gate_gating_tooluse_on_a_small_models/) ⭐️ 8.0/10

A 10MB LoRA adapter for Qwen3.5-4B gates tool use based on internal confidence signals, improving error detection and reducing hallucination. This approach addresses a key limitation of small LLMs—poor verbalized confidence—by reading internal activations, enabling more reliable tool use and privacy protection for local deployment. The gate improves d′ by 0.46 (95% CI [0.01, 0.89]) and reduces private query leakage from 22% to 10%. It runs locally on Apple Silicon via MLX or GGUF for llama.cpp/Ollama.

reddit · r/MachineLearning · /u/Synthium- · Jul 5, 07:49

**Background**: Small instruct models often fail to accurately express their confidence, leading to overconfident incorrect answers. LoRA adapters are lightweight fine-tuning modules that can be added to base models without full retraining. Internal confidence signals refer to hidden-state patterns that correlate with answer correctness, which can be extracted via probing.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/learn/llm-course/chapter11/4">LoRA (Low-Rank Adaptation) · Hugging Face</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/lora.html">LoRA Adapters — vLLM</a></li>

</ul>
</details>

**Discussion**: The community discussion is not provided, but the post author invites critique and notes the approach is open-source and extendable to other models.

**Tags**: `#LLM`, `#tool use`, `#confidence estimation`, `#LoRA`, `#local AI`

---

<a id="item-6"></a>
## [USAF: Sparse Fine-Tuning for MoE on Consumer GPUs](https://www.reddit.com/r/MachineLearning/comments/1unl62q/if_your_gpu_can_run_inference_it_should_be_able/) ⭐️ 8.0/10

A new sparse fine-tuning method called USAF enables fine-tuning of Mixture-of-Experts (MoE) models on GPUs that previously could only run inference, demonstrated by fine-tuning Qwen3-30B-A3B on a 12GB AMD RX 6750 XT. This method lowers the hardware barrier for fine-tuning large MoE models, allowing researchers and hobbyists with consumer GPUs to adapt state-of-the-art models without expensive hardware. USAF trains only sparse expert weights and the router, avoiding full-weight or adapter-based updates, and is released under Apache 2.0 license on GitHub.

reddit · r/MachineLearning · /u/tsuyu122 · Jul 4, 21:56

**Background**: Mixture-of-Experts (MoE) models use multiple specialized sub-networks (experts) and a router to select which experts to activate per input, enabling larger model capacity with lower computational cost. Traditional fine-tuning methods like LoRA add adapter modules, which still require significant memory. Sparse fine-tuning updates only a small subset of weights, reducing memory usage.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>

</ul>
</details>

**Tags**: `#fine-tuning`, `#MoE`, `#sparse training`, `#open source`, `#GPU optimization`

---

<a id="item-7"></a>
## [Guardian: OpenAI Never Visited Key Stargate UK Site, $30B Pledge a Stunt](https://www.theguardian.com/technology/2026/jul/04/openai-apparent-failure-visit-key-site-questions-stargate-uk-project) ⭐️ 8.0/10

A Guardian investigation revealed that OpenAI never visited the primary site for its Stargate UK project, Cobalt Park in North Tyneside, and local government never met with OpenAI or partner Nscale. The project was suspended in April 2026, with insiders calling it a PR stunt. This story undermines the credibility of high-profile AI infrastructure investments and raises questions about the sincerity of tech giants' commitments to UK tech policy. It could affect public trust and future investment in the UK's AI sector. The Stargate UK project was announced during a Trump visit to the UK as a flagship UK-US AI collaboration, but was suspended in April 2026 citing regulatory environment and high energy costs. A local Conservative MP stated the project's realization 'looks extremely unlikely.'

telegram · zaihuapd · Jul 5, 05:09

**Background**: Stargate UK was a proposed AI infrastructure partnership between OpenAI, NVIDIA, and Nscale to build sovereign compute capabilities in the UK, allowing AI models to run on local data centers. Cobalt Park is one of the largest business parks in the UK, located in North Tyneside. The project's suspension and lack of site visits suggest it may have been more about political optics than actual investment.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-stargate-uk/">Introducing Stargate UK | OpenAI</a></li>
<li><a href="https://www.theguardian.com/technology/2026/apr/09/openai-pulls-out-of-landmark-31bn-uk-investment">OpenAI shelves Stargate UK in blow to Britain’s AI ambitions | OpenAI | The Guardian</a></li>

</ul>
</details>

**Discussion**: The Telegram source indicates community discussion, but no specific comments were provided in the input. The high score suggests significant interest and likely skepticism about OpenAI's claims.

**Tags**: `#OpenAI`, `#Stargate UK`, `#AI infrastructure`, `#investigative journalism`, `#UK tech policy`

---

<a id="item-8"></a>
## [Fudan Exam: Students Stump AI to Test Critical Thinking](https://mp.weixin.qq.com/s/d53O-6mVFZqMa_Sti1yEPw) ⭐️ 8.0/10

Fudan University replaced its traditional 'Data Mining Techniques' final exam with a 'Human vs. AI' challenge, where 51 students each designed 10 calculation problems to test three AI models; students scored higher when AI answered incorrectly. This novel assessment reflects a paradigm shift in education for the AI era, moving from rote memorization to evaluating AI literacy, critical thinking, and the ability to judge AI outputs, which could influence pedagogy worldwide. 50 out of 51 students managed to stump at least one AI model, but only 4 students achieved a perfect zero score on any model; the strongest model, Claude, was never completely stumped, and the class average score was 85.7 out of 100.

telegram · zaihuapd · Jul 5, 08:40

**Background**: The course 'Data Mining Techniques' traditionally tests algorithmic knowledge and memory, but instructor Xiao Yanghua argued that such methods are obsolete in the AI era. The new exam format trains students to command AI and evaluate its results, emphasizing higher-order thinking skills.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude ( AI ) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI in Education`, `#Assessment Reform`, `#AI Evaluation`, `#Pedagogy`, `#Critical Thinking`

---

<a id="item-9"></a>
## [SpaceX Shows Investors Thinner-than-iPhone Prototype](https://www.wsj.com/tech/spacexs-telecom-dreams-d461e568) ⭐️ 8.0/10

SpaceX has shown investors a prototype smartphone that is thinner than an iPhone and runs its own operating system, as part of its plan to expand Starlink into mobile communications. This move could disrupt the telecom industry by integrating satellite connectivity directly into a custom device, potentially reducing reliance on traditional carriers and enabling global coverage. The prototype is reportedly thinner than an iPhone and runs its own OS; SpaceX President Gwynne Shotwell also mentioned plans to build ground networks and partner with cellular carriers.

telegram · zaihuapd · Jul 5, 14:10

**Background**: SpaceX's Starlink currently provides broadband internet via satellite and has launched a Direct to Cell service for 4G LTE phones. The prototype represents a step toward a dedicated device that could fully leverage Starlink's satellite network for mobile communication.

<details><summary>References</summary>
<ul>
<li><a href="https://starlink.com/public-files/DIRECT_TO_CELL_SERVICE_FEB_25.pdf">STARLINK DIRECT TO CELL SERVICE NOW AVAILABLE</a></li>
<li><a href="https://winbuzzer.com/2026/07/03/musk-denies-reported-spacex-handset-like-ai-prototype-xcxwbn/">Elon Musk Denies Rumors of SpaceX Handset-Like AI Device Prototype</a></li>

</ul>
</details>

**Discussion**: Elon Musk denied rumors of a SpaceX handset-like AI device prototype, creating some confusion. However, the WSJ report suggests the prototype exists, sparking debate about Musk's ecosystem ambitions.

**Tags**: `#SpaceX`, `#Starlink`, `#mobile`, `#telecom`, `#hardware`

---