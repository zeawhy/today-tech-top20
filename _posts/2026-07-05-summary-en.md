---
layout: default
title: "Horizon Summary: 2026-07-05 (EN)"
date: 2026-07-05
lang: en
---

> From 37 items, 10 important content pieces were selected

---

1. [Prompt injection leaks YouTube creators' private videos](#item-1) ⭐️ 9.0/10
2. [Huawei's 'Tao's Law' Proposes Time Scaling to Extend Moore's Law](#item-2) ⭐️ 9.0/10
3. [GPT-5.5 Codex Reasoning Degradation Due to Token Clustering](#item-3) ⭐️ 8.0/10
4. [Anna's Archive Offers $200k Bounty for Google Books Scans](#item-4) ⭐️ 8.0/10
5. [Session/Cache Leakage Reported in LLM Workspaces](#item-5) ⭐️ 8.0/10
6. [Better Models, Worse Tool-Calling Reliability](#item-6) ⭐️ 8.0/10
7. [USAF: Sparse Fine-Tuning for MoE on Consumer GPUs](#item-7) ⭐️ 8.0/10
8. [BaryGraph: Relationships as First-Class Documents in Knowledge Graphs](#item-8) ⭐️ 8.0/10
9. [Linux Tops 2026 CVE Charts, Kernel Maintainer Says It's Good](#item-9) ⭐️ 8.0/10
10. [F-Droid Labels Google ADV as Malware on 4 Billion Devices](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Prompt injection leaks YouTube creators' private videos](https://javoriuski.com/post/youtube) ⭐️ 9.0/10

A security researcher discovered a prompt injection vulnerability in YouTube Studio's AI comment suggestion feature that allows attackers to leak creators' private and unlisted videos by embedding malicious instructions in comments. This vulnerability affects millions of YouTube creators who rely on the platform's AI tools, potentially exposing unpublished content and undermining trust in YouTube's security. It highlights the growing risk of prompt injection in AI-integrated applications. The attack works when a creator opens the comments tab in YouTube Studio and clicks a suggested AI prompt; the injected comment then causes the AI to include a link to a private video in its response. The researcher reported the issue to Google in July 2024, but it was initially classified as a low-severity 'spam' issue.

hackernews · javxfps · Jul 4, 16:45 · [Discussion](https://news.ycombinator.com/item?id=48786781)

**Background**: Prompt injection is a security vulnerability where an attacker crafts input that manipulates an AI model's behavior, often bypassing intended instructions. YouTube Studio's AI comment suggestions use large language models to generate reply suggestions for creators, but they can be tricked by malicious comments. This type of attack is increasingly common as AI features are integrated into more applications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://support.google.com/youtube/answer/10357396?hl=en&co=GENIE.Platform=Android">Use comment reply suggestions - Android - YouTube Help</a></li>
<li><a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection/">LLM01:2025 Prompt Injection - OWASP Gen AI Security Project</a></li>

</ul>
</details>

**Discussion**: The community discussion includes a former Google engineer who explains why YouTube may have handled the bug slowly, and a user who attempted to reproduce the attack but found it didn't work with only one unlisted video. Overall sentiment is critical of YouTube's response, with many calling for prompt injection to be treated as a serious security bug.

**Tags**: `#security`, `#prompt injection`, `#YouTube`, `#vulnerability`, `#AI`

---

<a id="item-2"></a>
## [Huawei's 'Tao's Law' Proposes Time Scaling to Extend Moore's Law](https://t.me/zaihuapd/42346) ⭐️ 9.0/10

At the 2026 International Symposium on Circuits and Systems in Shanghai, Huawei announced 'Tao's Law', a new semiconductor scaling principle that replaces geometric scaling with time scaling. Over the past six years, Huawei has designed and mass-produced 381 chips based on this principle, and plans to release a new Kirin smartphone chip using logic folding technology this autumn. Tao's Law offers a potential path beyond Moore's Law, which is approaching physical limits, by optimizing time constants across devices, circuits, chips, and systems. This breakthrough could sustain semiconductor advancement and impact the entire industry, with Huawei predicting that high-end chips based on this law could achieve transistor density equivalent to 1.4nm process by 2031. The new Kirin chip will be the first to implement logic folding technology, which restructures logic circuits from a 2D plane into layered channels within a single chip, significantly boosting transistor density without increasing chip size. Huawei's He Tingbo published a detailed paper titled 'A Time Scaling Theory for Multi-Layer Electronic Systems' on the Chinese Academy of Sciences preprint platform.

telegram · zaihuapd · Jul 4, 04:56

**Background**: Moore's Law, which states that transistor density on a chip doubles approximately every two years, has driven semiconductor progress for decades but is now slowing due to physical limits. Traditional geometric scaling shrinks transistor dimensions, while time scaling focuses on reducing signal propagation delays through innovative circuit design and architecture. Logic folding is a specific technique that rearranges circuits into multiple layers within a single chip, improving performance without relying on advanced fabrication nodes.

<details><summary>References</summary>
<ul>
<li><a href="https://www.peopleapp.com/column/30052254360-500007517346">“ 韬 定 律 ”，做 时 间 的朋友_人民日报</a></li>
<li><a href="https://www.guancha.cn/economy/2026_05_25_818264.shtml">华为何庭波：今年麒麟芯片首次实施逻辑折叠技术，性能将大幅提升</a></li>
<li><a href="https://www.21jingji.com/article/20260526/herald/88be312b20ad7d0d18384eb8169efded.html">究竟｜“ 韬 定 律 ”将如何影响 半 导 体 产业演进路径 - 21经济网</a></li>

</ul>
</details>

**Discussion**: The provided content does not include community comments, so no discussion summary is available.

**Tags**: `#semiconductor`, `#Huawei`, `#Moore's Law`, `#chip design`, `#technology breakthrough`

---

<a id="item-3"></a>
## [GPT-5.5 Codex Reasoning Degradation Due to Token Clustering](https://github.com/openai/codex/issues/30364) ⭐️ 8.0/10

Users report that GPT-5.5 Codex exhibits degraded reasoning performance, with the model sometimes short-circuiting and using exactly 516 thinking tokens to produce incorrect results on puzzles, while using 6000-8000 tokens yields correct answers. This regression undermines trust in OpenAI's flagship coding assistant, especially for complex reasoning tasks, and may drive users to competing models like Claude or local alternatives. The issue appears to be a token clustering bug where the model prematurely stops reasoning after a fixed number of tokens, leading to incorrect outputs. Community members note similar regressions in other models, such as Claude Code in April.

hackernews · maille · Jul 4, 21:51 · [Discussion](https://news.ycombinator.com/item?id=48789428)

**Background**: GPT-5.5 Codex is OpenAI's latest coding and reasoning model, released on April 23, 2026, designed for agentic coding tasks. Token clustering is a technique used to reduce inference time by grouping similar tokens, but when misconfigured, it can cause the model to truncate reasoning prematurely.

<details><summary>References</summary>
<ul>
<li><a href="https://www.stet.sh/blog/gpt-55-codex-graphql-reasoning-curve">GPT - 5 . 5 low vs medium vs high vs xhigh: the reasoning curve... — Stet</a></li>
<li><a href="https://apidog.com/blog/what-is-gpt-5-5/">What Is GPT - 5 . 5 ? OpenAI's New Frontier Model Explained</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely negative, with users expressing frustration over the silent regression and comparing it to similar issues in other models. Some users have switched to Claude or plan to use a mix of models to mitigate the problem.

**Tags**: `#AI`, `#GPT-5.5`, `#Codex`, `#performance regression`, `#reasoning`

---

<a id="item-4"></a>
## [Anna's Archive Offers $200k Bounty for Google Books Scans](https://software.annas-archive.gl/AnnaArchivist/annas-archive/-/work_items/234) ⭐️ 8.0/10

Anna's Archive has announced a $200,000 bounty for a complete collection of all book scans from Google Books, aiming to acquire the full dataset for open access. This bounty underscores the ongoing struggle between open access advocates and copyright holders, potentially making millions of digitized books freely available to the public, especially in regions with limited access. The bounty is part of Anna's Archive's broader mission to catalog all books in existence, and it follows previous legal challenges to Google's book scanning project, which was deemed legal by U.S. courts.

hackernews · Cider9986 · Jul 4, 16:51 · [Discussion](https://news.ycombinator.com/item?id=48786838)

**Background**: Google Books is a service that scans and indexes the full text of books from libraries and publishers, using OCR to convert images to text. Anna's Archive is a metasearch engine for shadow libraries like Z-Library and Sci-Hub, aggregating metadata for over 97 million books. The project has faced legal actions for copyright infringement but operates as a non-profit, open-source platform.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anna's_Archive">Anna's Archive</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Books">Google Books - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments express gratitude for Anna's Archive, with users sharing personal stories of accessing rare or out-of-print books. Some discuss related projects like SourceLibrary.org, while others raise concerns about internet scraping and Cloudflare captchas. There is also a correction about a malicious link in the bounty description.

**Tags**: `#open access`, `#digital libraries`, `#bounty`, `#books`, `#archiving`

---

<a id="item-5"></a>
## [Session/Cache Leakage Reported in LLM Workspaces](https://github.com/anthropics/claude-code/issues/74066) ⭐️ 8.0/10

Users report potential session or cache leakage between LLM workspace instances, with one provider postmortem citing HTTP 100 status code mishandling as a root cause. This issue raises significant security and privacy concerns for LLM services, as it could lead to cross-account data exposure. If confirmed, it would undermine trust in cloud-based AI platforms. The bug manifests as users receiving responses that appear to belong to other sessions, such as unrelated Minecraft building suggestions. Anthropic's Claude Code team has stated they believe it is a hallucination but are investigating.

hackernews · chatmasta · Jul 4, 14:03 · [Discussion](https://news.ycombinator.com/item?id=48785485)

**Background**: LLM workspace instances are isolated environments for interacting with AI models, typically with session-specific context and caching. HTTP 100 Continue is an informational status code that can cause request routing errors if mishandled by API gateways, potentially leading to response mix-ups.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/anthropics/claude-code/issues/74066">[Bug] Potential session /cache leakage between workspace ...</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/100">100 Continue - HTTP | MDN</a></li>
<li><a href="https://news.ycombinator.com/item?id=48785485">Potential session /cache leakage between workspace instances or...</a></li>

</ul>
</details>

**Discussion**: Community comments include reports of similar issues across providers like Gemini, with some users suspecting cache collisions. A commenter with insider knowledge mentioned two instances of response swapping, one involving HTTP 100 mishandling. Skepticism exists, with some attributing the behavior to hallucinations.

**Tags**: `#LLM`, `#security`, `#privacy`, `#cache`, `#Anthropic`

---

<a id="item-6"></a>
## [Better Models, Worse Tool-Calling Reliability](https://simonwillison.net/2026/Jul/4/better-models-worse-tools/#atom-everything) ⭐️ 8.0/10

Newer Claude models (Opus 4.8, Sonnet 5) are more likely to invent extra fields in tool call arguments, causing rejection by custom coding harnesses like Pi, while older models did not exhibit this issue. This regression undermines the reliability of LLM-based coding agents, forcing third-party tool builders to either adapt to model-specific quirks or risk broken workflows. The issue appears because Anthropic trains newer models via reinforcement learning to use Claude Code's built-in edit tools, which inadvertently biases them against third-party schemas. Pi's edit tool uses a nested 'edits[]' array where models invent keys like 'search' or 'replace' that don't exist in the schema.

rss · Simon Willison · Jul 4, 22:53

**Background**: LLM tool calling allows models to invoke external functions by generating structured arguments matching a provided schema. Coding harnesses like Pi and Claude Code use edit tools to modify code files. Anthropic and OpenAI train their models to excel at their own tool formats, which can hurt compatibility with others.

**Tags**: `#LLM`, `#tool calling`, `#regression`, `#Anthropic`, `#AI reliability`

---

<a id="item-7"></a>
## [USAF: Sparse Fine-Tuning for MoE on Consumer GPUs](https://www.reddit.com/r/MachineLearning/comments/1unl62q/if_your_gpu_can_run_inference_it_should_be_able/) ⭐️ 8.0/10

A new sparse fine-tuning method called USAF enables fine-tuning of Mixture-of-Experts (MoE) models on the same GPU used for inference, demonstrated by fine-tuning Qwen3-30B-A3B on a 12GB AMD RX 6750 XT. This significantly lowers the hardware barrier for fine-tuning large MoE models, making it accessible to users with consumer-grade GPUs and potentially accelerating community-driven customization of MoE models. USAF trains only sparse expert weights and the router, avoiding full model updates or adapters, and is released under Apache 2.0 license with no commercial intent.

reddit · r/MachineLearning · /u/tsuyu122 · Jul 4, 21:56

**Background**: Mixture-of-Experts (MoE) models use multiple specialized sub-networks (experts) activated sparsely per input, enabling large model capacity with lower inference cost. Fine-tuning such models typically requires significant GPU memory, often beyond consumer hardware.

**Tags**: `#fine-tuning`, `#MoE`, `#sparse training`, `#open source`, `#GPU efficiency`

---

<a id="item-8"></a>
## [BaryGraph: Relationships as First-Class Documents in Knowledge Graphs](https://www.reddit.com/r/MachineLearning/comments/1un3lsf/barygraph_knowledge_graph_where_every/) ⭐️ 8.0/10

BaryGraph introduces a knowledge graph where every relationship is embedded as a first-class document (BaryEdge) with its own vector, rather than a simple edge between nodes. It recursively stacks BaryEdges to form MetaBary triads that surface structural bridges between distant concepts, demonstrated on the full English Wiktionary. This approach addresses a fundamental limitation of standard vector search and RAG systems, which treat relationships as byproducts of point proximity and miss cross-domain connections. By embedding relationships as retrievable documents, BaryGraph can surface structural bridges between concepts from different domains, such as linking orbital mechanics to stellar dynamics or collagen folding to linguistic syntax. BaryGraph runs locally on MongoDB Community + mongot with nomic-embed-text (768-dim), processing 6.6 million documents from English Wiktionary in 8–14 hours on a single workstation. The BaryEdge vector is computed as bary_vector = normalize(q·v(CM1) + q·v(CM2) + (1−q)·v(type)), where q is connection quality and v(type) is a contextual embedding of the relationship type.

reddit · r/MachineLearning · /u/adseipsum · Jul 4, 08:24

**Background**: Traditional knowledge graphs represent relationships as edges between nodes, and vector search treats similarity as proximity in embedding space. This fails to capture structural connections between concepts that are far apart in embedding space but share relational patterns. BaryGraph introduces BaryEdges as first-class documents that can be recursively composed into MetaBary triads, forming an abstraction hierarchy without additional embedding calls.

**Tags**: `#Knowledge Graphs`, `#Embeddings`, `#RAG`, `#Vector Search`, `#Machine Learning`

---

<a id="item-9"></a>
## [Linux Tops 2026 CVE Charts, Kernel Maintainer Says It's Good](https://linuxiac.com/linux-tops-2026-cve-charts/) ⭐️ 8.0/10

In the first half of 2026, Linux led all vendors with 2,308 CVEs, surpassing Google (1,752), Microsoft (843), and Apple (284). Kernel maintainer Greg Kroah-Hartman argued this reflects more complete and transparent vulnerability reporting, not worse security. This news challenges the common perception that a high CVE count indicates poor security, highlighting the transparency advantage of open-source projects. It also pressures commercial vendors to adopt more comprehensive vulnerability disclosure practices. Greg Kroah-Hartman noted that commercial vendors like Apple and Microsoft often only report vulnerabilities classified as 'high severity,' while open-source projects report all issues because they cannot predict downstream usage. Linux runs on billions of devices including servers, phones, embedded systems, and cloud infrastructure.

telegram · zaihuapd · Jul 4, 16:00

**Background**: CVE (Common Vulnerabilities and Exposures) is a global standard for identifying and cataloging publicly disclosed cybersecurity vulnerabilities. A higher CVE count is often misinterpreted as a sign of insecurity, but it can also indicate more thorough reporting. Open-source projects like Linux are inherently more transparent because their code is publicly audited, leading to more vulnerabilities being discovered and reported.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cve.org/">CVE: Common Vulnerabilities and Exposures</a></li>

</ul>
</details>

**Tags**: `#Linux`, `#CVE`, `#open source`, `#security`, `#kernel`

---

<a id="item-10"></a>
## [F-Droid Labels Google ADV as Malware on 4 Billion Devices](https://f-droid.org/2026/07/01/adv-malware.html) ⭐️ 8.0/10

F-Droid has officially labeled Google's Android Developer Verification (ADV) as malware, claiming it is a system process with root privileges that cannot be removed and is pre-installed on approximately 4 billion Android devices. The program is set to activate in Brazil, Indonesia, Singapore, and Thailand starting September 30, 2026, blocking unapproved apps, with global rollout planned for 2027 and beyond. This move highlights a major conflict between Google's centralized control over Android and the open-source community's commitment to user freedom. If ADV rolls out globally, it could effectively kill alternative app stores like F-Droid and sideloading, affecting billions of users and developers who rely on unapproved apps. F-Droid points out that Google deliberately avoids defining 'malware' in its developer terms, allowing it to arbitrarily classify unwanted software like ad blockers as malware and ban developers. Despite over 70 organizations including EFF, FSF, and ACLU signing an open letter against ADV, and hundreds of thousands of signatures opposing it, Google is proceeding with the plan.

telegram · zaihuapd · Jul 5, 00:41

**Background**: F-Droid is a free and open-source (FOSS) app store for Android that only hosts open-source apps and flags anti-features like tracking. Android Developer Verification (ADV) is a Google initiative embedded via Play Protect that aims to restrict installation of apps not approved by Google, effectively controlling sideloading and third-party app stores.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=47580297">Android Developer Verification | Hacker News</a></li>
<li><a href="https://www.reddit.com/r/degoogle/comments/1sa0lek/how_to_fight_developer_verification_on_android/">How to fight Developer Verification on Android plus first looks at ... - Reddit</a></li>
<li><a href="https://en.wikipedia.org/wiki/F-Droid">F-Droid</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion calls ADV a 'death sentence' for F-Droid and other competitors. Reddit users are discussing ways to fight ADV, such as enabling developer mode and unverified apps, but the overall sentiment is one of concern and opposition.

**Tags**: `#Android`, `#F-Droid`, `#Google`, `#malware`, `#privacy`

---