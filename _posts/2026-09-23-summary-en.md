---
layout: default
title: "Horizon Summary: 2026-09-23 (EN)"
date: 2026-09-23
lang: en
---

> From 94 items, 15 important content pieces were selected

---

1. [Anthropic and OpenAI Launch New Frontier Models, Sparking Price War](#item-1) ⭐️ 9.0/10
2. [OpenAI forms math advisory group as AI solves 100+ open problems](#item-2) ⭐️ 9.0/10
3. [OpenAI Begins Limited Preview of GPT-5.6 Series: Sol, Terra, Luna](#item-3) ⭐️ 9.0/10
4. [vLLM v0.30.0 ships Fast Start weight cache and new model support](#item-4) ⭐️ 8.0/10
5. [OpenAI's GPT-6 Astra Reportedly Cracks Long-Unsolved Enigma Message](#item-5) ⭐️ 8.0/10
6. [FoxPro revived with Rust/WASM runtime](#item-6) ⭐️ 8.0/10
7. [ShinyHunters claims FBI hack, says it has data on all employees](#item-7) ⭐️ 8.0/10
8. [Trail of Bits Critiques SAML as a 'Fractal of Bad Design'](#item-8) ⭐️ 8.0/10
9. [WordPress Patches Unauthenticated Path Traversal Enabling Conditional RCE](#item-9) ⭐️ 8.0/10
10. [Pentagon report links AI overreliance to deadly Iran school strike](#item-10) ⭐️ 8.0/10
11. [TypeSafe AI Unveils Jev, a 'System One' Decision Model](#item-11) ⭐️ 8.0/10
12. [Xiaomi releases MiMo-V2.6 multimodal model with $3.5M RL training cost](#item-12) ⭐️ 8.0/10
13. [Complex KDA Extends Kimi Delta Attention Expressivity](#item-13) ⭐️ 8.0/10
14. [US Proposes AI Incident Reporting Channel With China](#item-14) ⭐️ 8.0/10
15. [China Probes DeepSeek and Moonshot Over Data Leaks to Claude](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic and OpenAI Launch New Frontier Models, Sparking Price War](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 9.0/10

Anthropic released Claude Opus 5.5, and about an hour later OpenAI released GPT-6 Sol and GPT-6 Luna, with GPT-6 Luna priced at half the cost of its GPT-5.6 predecessor. GPT-6 Luna now costs $0.10 per million input tokens and $0.50 per million output tokens, while Claude Opus 5.5 is priced at $4 input and $20 output. This simultaneous release and dramatic price reduction signals an intensifying price war among frontier AI labs, making advanced models far cheaper for developers and businesses to build on. It could reshape the economics of AI application development and pressure competitors like xAI to adjust their pricing. GPT-5.6 models have a scheduled 25% price increase for November, so GPT-6 is actually half the price of the promotional pricing for those models. GPT-6 Sol reasons about twice as much as GPT-5.6, making it roughly twice as slow and 25% more expensive in practice despite lower token costs.

rss · Simon Willison · Sep 22, 23:46

**Background**: Claude is Anthropic's family of large language models, with Opus being its most capable tier, while GPT is OpenAI's flagship series. Frontier models are the most advanced and expensive AI systems, and their pricing directly affects how much developers pay to build AI-powered applications. A price war occurs when competing labs cut prices aggressively to win market share.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://openrouter.ai/x-ai/grok-4.7">Grok 4 . 7 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Opus_4.1">Claude Opus 4.1</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted GPT-6 Luna's halved price as a major deal and praised its intelligence-per-cost ratio, while some expressed concern that GPT-6 Sol is slower and more expensive in practice. Others noted attachment to GPT-5.6 Sol's working style and discussed usage limits and pricing math between Claude Code and Codex Pro plans.

**Tags**: `#AI`, `#LLM`, `#OpenAI`, `#Anthropic`, `#pricing`

---

<a id="item-2"></a>
## [OpenAI forms math advisory group as AI solves 100+ open problems](https://techcrunch.com/2026/09/21/openai-forms-math-advisory-group-as-its-ai-resolves-more-than-100-open-problems/) ⭐️ 9.0/10

On Monday, OpenAI announced an independent Advisory Group on Mathematics and Artificial Intelligence, hosted at the Institute for Advanced Study in Princeton, New Jersey, to give mathematicians more input into its math-oriented research. As part of the announcement, OpenAI also claimed that the same internal model has resolved more than 100 additional open problems across most areas of mathematics. If verified, an AI resolving over 100 open mathematical problems would mark a major leap in AI-for-math, potentially reshaping how mathematical research is conducted and how quickly new results are produced. The advisory group also signals that OpenAI is trying to build institutional oversight for AI-generated mathematical discoveries, even as the field debates how novel such results really are. The advisory group is explicitly not given leeway to slow down or redirect OpenAI's ongoing mathematical research, meaning it functions mainly as a review and communication body rather than a governance or safety brake. OpenAI has previously shared results such as an AI-generated disproof of the Erdős unit-distance conjecture and a selection of ten advances in mathematics and theoretical computer science.

rss · TechCrunch AI · Sep 21, 20:15

**Background**: OpenAI is a leading AI lab whose models are increasingly used to attack open problems in mathematics, a field where results are typically verified by peer review and formal proof. The Institute for Advanced Study in Princeton is a renowned independent research institution, and hosting the advisory group there is meant to lend the effort academic credibility. Open problems are long-standing unsolved questions that mathematicians consider important but have not yet resolved.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/advisory-group-on-mathematics-and-ai/">Advisory Group on Mathematics and Artificial Intelligence | OpenAI</a></li>
<li><a href="https://techcrunch.com/2026/09/21/openai-forms-math-advisory-group-as-its-ai-resolves-more-than-100-open-problems/">OpenAI forms math advisory group as its AI resolves more than 100 open problems | TechCrunch</a></li>
<li><a href="https://openai.com/index/ten-advances-in-mathematics/">Ten advances in mathematics and theoretical computer science | OpenAI</a></li>

</ul>
</details>

**Discussion**: Discussion on r/mathematics largely echoed OpenAI's own framing, focusing on the advisory group's stated purpose of guiding the review and communication of emerging AI results. Some commentators, cited in broader coverage, argue that recent AI mathematical breakthroughs consist of clever recombination of existing ideas rather than the development of truly novel theory.

**Tags**: `#OpenAI`, `#AI for Mathematics`, `#Research Breakthrough`, `#AI Safety`, `#Mathematical Discovery`

---

<a id="item-3"></a>
## [OpenAI Begins Limited Preview of GPT-5.6 Series: Sol, Terra, Luna](https://t.me/zaihuapd/43990) ⭐️ 9.0/10

OpenAI has started a limited preview of its GPT-5.6 model family, which includes three tiers: the flagship Sol, the balanced Terra, and the low-cost Luna. The preview is initially available only to a small group of trusted partners through the API and Codex, with broader rollout to ChatGPT and Codex planned in the coming weeks. This is a major flagship model release from OpenAI, with Sol claiming stronger coding, biology, and cybersecurity capabilities that could reshape developer workflows and security research. The government-influenced limited rollout also signals a new era of regulatory involvement in frontier AI deployment. Sol introduces new 'max' reasoning intensity and an 'ultra' mode, Terra is roughly twice as cheap as GPT-5.5 while performing close to it, and Luna is positioned as the lowest-cost option. OpenAI describes the limited preview as a short-term step taken at the request of the US government, with participation shared with the government before broader release.

telegram · zaihuapd · Sep 22, 18:04

**Background**: GPT-5.6 is the latest iteration of OpenAI's flagship large language model series, following GPT-5.5. Codex is OpenAI's AI coding agent, released in April 2025, which can write code and fix bugs across ChatGPT, CLI, desktop, and IDE integrations. The tiered naming (Sol, Terra, Luna) reflects a strategy of offering different price-performance tradeoffs for different use cases.

<details><summary>References</summary>
<ul>
<li><a href="https://www.businessinsider.com/openai-gpt-5-6-limited-preview-us-government-ai-security-2026-6">OpenAI Launches Limited Preview of GPT-5.6 at US Government's Request - Business Insider</a></li>
<li><a href="https://www.cybersecuritydive.com/news/openai-model-government-limit-request/823966/">OpenAI voluntarily limits new AI models at government’s request | Cybersecurity Dive</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent)</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-5.6`, `#AI models`, `#limited preview`, `#API`

---

<a id="item-4"></a>
## [vLLM v0.30.0 ships Fast Start weight cache and new model support](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM released v0.30.0, a major update with 762 commits from 315 contributors (104 of them new). The release adds a persistent per-GPU weight-cache daemon called Fast Start, new model architectures such as DeepSeek-V4.1-Flash, DeepSeek-V4-Flash-Vision-Exp, GLM-5.3-Flash, K2-Horizon, Cohere Compass and Bailing V3 VL, plus Gumbel-max watermarking, the HiSparse host-resident KV tier, and numerous performance optimizations. vLLM is one of the most widely used open-source LLM inference and serving engines, so its releases directly shape how companies and researchers deploy models in production. Fast Start can cut engine restart time dramatically, and the broad new model coverage means users can serve the latest architectures without waiting for third-party forks or patches. Fast Start keeps post-quantized, TP-sharded weights in GPU memory and remaps them over CUDA IPC via `--load-format ipc_cache` instead of reloading from disk, now covering FP4 checkpoints and multi-node TP. Other notable items include dual-batch overlap with FULL CUDA graphs, adaptive speculative-decoding verification, MXFP8 KV storage for DeepSeek-V4.1-Flash on SM100, and targeted online quantization through `quantization_config.targets`.

github · khluu · Sep 22, 05:20

**Background**: vLLM is an open-source engine for high-throughput LLM inference and serving, known for techniques like PagedAttention that manage KV cache memory efficiently. Quantization formats such as MXFP8 and NVFP4 compress model weights to lower precision so they use less memory and run faster on modern GPUs like NVIDIA's Blackwell (SM100) generation. FlashMLA is DeepSeek's library of optimized multi-head latent attention kernels, and speculative decoding speeds up generation by having a small draft model propose tokens that a larger model verifies.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/weight_cache/daemon/">daemon - vLLM</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/FlashMLA: FlashMLA: Efficient Multi-head Latent Attention Kernels · GitHub</a></li>
<li><a href="https://barrahome-quantization-formats-and-cuda-compute-c34be9a.static.hf.space/">LLM Quantization Formats & CUDA Support Reference</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#model serving`, `#release`, `#AI infrastructure`

---

<a id="item-5"></a>
## [OpenAI's GPT-6 Astra Reportedly Cracks Long-Unsolved Enigma Message](https://www.cryptocellar.org/bgac/the-mvueh-break.html) ⭐️ 8.0/10

OpenAI's GPT-6 Astra reportedly decrypted an Enigma-encrypted message that had resisted solution since 2005, producing the plaintext 'BTTE UM ANGABE DES MARSQWEGES X BEFINDE MIQ IN X ROSENOW ROSENOW X SOFORT FUNKANTWORT X WASCHBBSCH'. The claim, published on cryptocellar.org, has drawn intense debate over how much of the work was truly autonomous. If verified, this would be a notable demonstration of a large language model tackling a real cryptanalysis problem that stumped human codebreakers for roughly two decades, reinforcing the trend of AI agents being applied to security and cryptography research. It also fuels the broader debate about AI autonomy, since the model reportedly wrote its own Enigma-simulating software rather than relying on existing tools. The decrypted text contains apparent misspellings and German military telegraph conventions, translating roughly to a request to specify a march route, a location report from Rosenow, and a demand for an immediate radio reply. Skeptics note that Astra reportedly developed Python and C++ Enigma-simulator software to do the work, raising questions about how novel that code was and how much of the cracking was offloaded to conventional computation.

hackernews · sohkamyung · Sep 22, 13:52 · [Discussion](https://news.ycombinator.com/item?id=49801324)

**Background**: The Enigma machine was a German rotor cipher device used heavily in World War II; its rotors advanced with each keypress so that every letter was encrypted with a different substitution, making it resistant to conventional cryptanalysis until Allied codebreakers exploited operational and procedural weaknesses. The message in question is a short, difficult ciphertext that had remained unsolved in the cryptography community since 2005. GPT-6 Astra is a large language model from OpenAI, described as its most aligned and capable model, with strong reasoning and computer-use abilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Enigma_machine">Enigma machine - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra - Wikipedia</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>

</ul>
</details>

**Discussion**: Commenters were sharply divided: one reported that Gemini 3.8 Flash solved the same ciphertext in about 45 minutes in a non-steered run, undercutting the uniqueness of the feat, while another argued that 'did it entirely on its own' is incongruous with the model generating its own Enigma-simulator software, since much of the work may be offloaded to conventional code. Others noted the message's rough translation and joked that the breakthrough came a bit late for the war effort.

**Tags**: `#AI`, `#cryptography`, `#Enigma`, `#OpenAI`, `#language models`

---

<a id="item-6"></a>
## [FoxPro revived with Rust/WASM runtime](https://foxscript.org/) ⭐️ 8.0/10

A project called FoxScript has revived Visual FoxPro by implementing a new runtime in Rust compiled to WebAssembly, maintaining compatibility with legacy VFP9 code while adding modern features like lambdas, JSON support, and an HTTP server. The runtime is checked against the real vfp9.exe, lifts the 2 GB table size limit, and still loads old 32-bit .fll add-ins. Many businesses still rely on long-lived Visual FoxPro applications that are costly to rewrite, so this revival offers a practical path to modernize and extend them without a full migration. It also demonstrates how legacy languages can be preserved and enhanced using modern toolchains like Rust and WebAssembly. The runtime is MIT-licensed, but reports are not yet implemented and builds are unsigned. It maintains compatibility with legacy 32-bit .fll add-ins and lifts the 2 GB table size limit, though security concerns about the Database Container (DBC) design remain unaddressed.

hackernews · boredjohnny · Sep 22, 21:00 · [Discussion](https://news.ycombinator.com/item?id=49808023)

**Background**: Visual FoxPro is a data-centric, object-oriented programming language and IDE developed by Microsoft, derived from FoxPro and FoxBASE. Version 9.0, released in 2004 and updated in 2007, was the final version, with support ending in 2015. Despite this, many business applications still run on Visual FoxPro, often because rewriting them is too risky or expensive. WebAssembly is a binary instruction format that allows code written in languages like Rust to run efficiently in various environments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Visual_FoxPro">Visual FoxPro</a></li>
<li><a href="https://fileproinfo.com/file-type/fll">FLL File Extension | Associated Programs | Free Online... - FileProInfo</a></li>
<li><a href="https://dev.to/wasmer/embedding-webassembly-in-your-rust-application-33n4">Embedding WebAssembly in your Rust application - DEV Community</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted that Visual FoxPro remains critical in niche industries with significant revenue, and shared experiences of its use in medical and real estate applications. A major concern raised was a security hole in the Database Container (DBC) design, where stored procedures can execute arbitrary FoxPro code, including Win32 calls, and are stored as plain text. Others reminisced about the ease of building CRUD applications in FoxPro and the business impact it had.

**Tags**: `#Visual FoxPro`, `#legacy systems`, `#Rust`, `#WebAssembly`, `#language revival`

---

<a id="item-7"></a>
## [ShinyHunters claims FBI hack, says it has data on all employees](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) ⭐️ 8.0/10

The extortion group ShinyHunters claims it breached multiple FBI-related services and exfiltrated data on all FBI employees and job applicants, providing a sample of roughly 5,000 alleged employee records that reportedly include names, home addresses, phone numbers, and family member details. The FBI has not confirmed the claim, and the group says its motive is not financial, describing its planned action as 'coercion' rather than extortion. If the data is genuine, the leak could be used to track, harass, or threaten FBI employees and their families, posing serious security and counterintelligence risks to US law enforcement and intelligence systems. The incident also highlights how even high-value government targets remain vulnerable to criminal extortion groups, echoing past large-scale breaches of federal personnel data. According to BleepingComputer, ShinyHunters claims it breached FBI systems by exploiting a new Oracle PeopleSoft zero-day vulnerability to access internal services and steal sensitive employee and applicant data. The group also defaced a website with a message reading 'this site has been seized by ShinyHunters,' though the authenticity of the sample data and the claimed zero-day has not been independently verified.

hackernews · spenvo · Sep 22, 17:46 · [Discussion](https://news.ycombinator.com/item?id=49805278)

**Background**: ShinyHunters is a black-hat criminal hacking and extortion group active since 2019, known for stealing and selling large databases from hundreds of companies. Oracle PeopleSoft is widely used enterprise HR and personnel management software, making it an attractive target for attackers seeking employee records. The 2015 Office of Personnel Management breach, which exposed records of about 22.1 million US government employees, is a key precedent for the national-security stakes of such leaks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/">ShinyHunters claims FBI hack, data theft in PeopleSoft zero-day breach</a></li>
<li><a href="https://en.wikipedia.org/wiki/ShinyHunters">ShinyHunters - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters were largely skeptical and darkly humorous, with some noting that no large database seems safe and citing the 2015 OPM breach as evidence that state actors likely already hold such data. Others mocked the group's non-financial framing, joked about AI agent swarms and Battlestar Galactica's unnetworked ships, and shared links to ShinyHunters' own 'PSA' text and a defacement screenshot.

**Tags**: `#cybersecurity`, `#data-breach`, `#FBI`, `#ShinyHunters`, `#government-security`

---

<a id="item-8"></a>
## [Trail of Bits Critiques SAML as a 'Fractal of Bad Design'](https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/) ⭐️ 8.0/10

Trail of Bits published a blog post titled 'SAML: A fractal of bad design,' delivering a deep technical critique of the Security Assertion Markup Language's flawed architecture and its persistent security pitfalls. The post argues that SAML's XML-based design is fundamentally unsuited to authentication, even as it remains widely deployed for enterprise single sign-on alongside the newer OIDC protocol. SAML underpins enterprise SSO for countless organizations, so its design flaws translate directly into real-world attack surface, including XML signature wrapping and improper assertion validation. The critique matters because teams must decide whether to keep supporting SAML for enterprise customers or migrate to OIDC, and the article shows that neither choice is free of risk. The article highlights that SAML's complexity stems from XML's structural flexibility, which enables attacks like XML Signature Wrapping that trick applications into processing unauthenticated data while passing signature validation. Community commenters added that early C implementations of XML signature validation would accept HMAC signatures using attacker-controlled passwords or validate signatures against web PKI, meaning an attacker could sign a SAML document with their own TLS key.

hackernews · aray07 · Sep 22, 18:57 · [Discussion](https://news.ycombinator.com/item?id=49806335)

**Background**: SAML (Security Assertion Markup Language) is an XML-based open standard for exchanging authentication and authorization data between identity providers and service providers, widely used for enterprise single sign-on. OIDC (OpenID Connect) is a newer identity layer built on OAuth 2.0 that uses JSON Web Tokens instead of XML, and is often positioned as SAML's modern replacement. XML Signature Wrapping is a class of attack that exploits XML's ability to represent the same data in multiple structural forms, allowing a valid signature to cover one element while the application processes another.

<details><summary>References</summary>
<ul>
<li><a href="https://workos.com/blog/common-saml-security-vulnerabilities">Common SAML security vulnerabilities and how to... — WorkOS</a></li>
<li><a href="https://www.ibm.com/think/topics/xml-signature-wrapping">What is XML Signature Wrapping ? | IBM</a></li>
<li><a href="https://fusionauth.io/blog/saml-and-oidc-difference">OIDC vs SAML : What's the Difference Between OpenID Connect and...</a></li>

</ul>
</details>

**Discussion**: Commenters largely agreed with the critique but pushed back on the article's one-sided framing, noting that OIDC has its own vulnerabilities such as JWT algorithm confusion, 'none' algorithm attacks, and missing audience checks. Several argued SAML still offers enterprise-specific features OIDC lacks, most notably IdP-initiated flow, and that vendors selling to enterprises should support both protocols while also dealing with SCIM.

**Tags**: `#SAML`, `#authentication`, `#security`, `#XML`, `#OIDC`

---

<a id="item-9"></a>
## [WordPress Patches Unauthenticated Path Traversal Enabling Conditional RCE](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp) ⭐️ 8.0/10

On September 22, 2026, the WordPress Security Team released WordPress 7.1.2 to fix a critical unauthenticated path traversal issue in page-template resolution that can lead to conditional remote code execution, and backported the fix to every branch back to WordPress 4.7. The vulnerability was reported by Robert Ressl and is tracked in the official WordPress security advisory GHSA-7hp8-65ch-5whp. Because the flaw is unauthenticated, any attacker can trigger it without logging in, and WordPress powers a huge share of the web, so millions of sites running versions as old as 4.7 are potentially exposed. The conditional nature of the RCE means exploitation depends on specific server configurations, but the broad backport signals how seriously the security team views the risk. The bug lives in WordPress's page-template resolution logic and is described as an unauthenticated path traversal leading to conditional remote code execution; the fix is included in WordPress 7.1.2 and in security backports for all affected branches since 4.7. Users are advised to update immediately, and about one-third of installs are reportedly not yet on the recent 7.x branch.

hackernews · vntok · Sep 22, 16:33 · [Discussion](https://news.ycombinator.com/item?id=49803959)

**Background**: A path traversal vulnerability lets an attacker manipulate file paths (for example with ../ sequences) to access or include files outside the intended directory. In WordPress, page templates determine which theme file renders a given page, so if an attacker can influence that resolution, they may be able to load unintended files and, under certain conditions, execute code. WordPress is a free, open-source content management system that powers a large fraction of all websites, which is why core security flaws attract widespread attention.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wordfence.com/blog/2026/09/psa-critical-unauthenticated-path-traversal-vulnerability-patched-in-wordpress-core/">PSA: Critical Unauthenticated Path Traversal Vulnerability Patched in...</a></li>
<li><a href="https://wordpress.org/documentation/wordpress-version/version-7-1-2/">Version 7.1.2 – Documentation – WordPress .org</a></li>
<li><a href="https://mariushosting.com/synology-ugreen-nas-wordpress-7-1-2-released/">Synology & UGREEN NAS WordPress 7.1.2 Released – Marius Hosting</a></li>

</ul>
</details>

**Discussion**: Commenters noted that path traversal bugs are a recurring problem across many programs, with one developer pointing to their libpathrs project as a fix because standard libraries lack proper file-handling abstractions. Others criticized WordPress's long history of exploitability and its large install base, while some shared relief at having migrated away from WordPress to static site generators or Rust-based frameworks.

**Tags**: `#WordPress`, `#security`, `#vulnerability`, `#RCE`, `#path traversal`

---

<a id="item-10"></a>
## [Pentagon report links AI overreliance to deadly Iran school strike](https://www.bloomberg.com/graphics/2026-iran-school-attack/) ⭐️ 8.0/10

A Pentagon investigation, reported by Bloomberg, concluded that overreliance on an AI targeting tool built by Palantir, combined with staff cuts and rushed targeting procedures, contributed to a U.S. missile strike on a girls' school in Minab, Iran, that killed 123 children. The report found the U.S. "failed in its obligation to do everything feasible to verify" the school was a military objective, and that the failure "went beyond mere negligence." This is one of the most consequential documented cases of AI-assisted military targeting causing mass civilian casualties, and it raises urgent questions about accountability, automation bias, and who bears responsibility when AI-informed decisions go wrong. It could reshape policy debates over human oversight of military AI systems and the procurement of tools like Palantir's. Officials said some Pentagon personnel knew within hours that the U.S. had hit the school, and the investigation described a cascade of preventable failures. Commentators note that the underlying problem may be automation bias — excessive trust in AI outputs — meaning more accurate models could actually worsen overreliance, and fixes must live in workflow and interface design rather than the model layer.

hackernews · devonnull · Sep 22, 19:03 · [Discussion](https://news.ycombinator.com/item?id=49806430)

**Background**: Militaries increasingly use AI systems to sift through massive datasets, identify potential targets, and accelerate strike decisions; well-known examples include Israel's Lavender system and the U.S. Project Maven. Accountability in autonomous or AI-assisted weapons is legally and ethically complex, since it requires identifying who is responsible, under which norms, and before which authority. Automation bias is a documented human-factors phenomenon in which operators over-trust automated recommendations, especially under time pressure or staffing shortages.

<details><summary>References</summary>
<ul>
<li><a href="https://gizmodo.com/pentagon-investigators-say-overreliance-on-palantir-ai-tech-contributed-to-u-s-strike-that-killed-123-iranian-children-2000814477">Pentagon Investigators Say Overreliance on Palantir AI Tech...</a></li>
<li><a href="https://thetesserapress.com/articles/pentagon-says-overreliance-on-ai-contributed-to-missile-strike-on-iran">Pentagon Links Overreliance on AI to Iran School Missile Strike...</a></li>
<li><a href="https://www.militarytimes.com/news/your-military/2026/09/16/ai-military-targeting-may-move-faster-than-humans-can-authenticate-critics-warn/">AI military targeting may move faster than humans can authenticate...</a></li>

</ul>
</details>

**Discussion**: Commenters largely pushed back on framing AI as the culprit, arguing it serves as a scapegoat that absolves humans of responsibility; several noted the deeper problem is people offloading targeting work to AI or being pressured to do so. Others criticized sanitized language like "deadliest American military targeting error" for mass murder, and pointed to a broader pattern of demanding a fall guy for criminal acts.

**Tags**: `#AI ethics`, `#military AI`, `#accountability`, `#policy`, `#news`

---

<a id="item-11"></a>
## [TypeSafe AI Unveils Jev, a 'System One' Decision Model](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 8.0/10

TypeSafe AI has released Jev, the first of its new 'System One' model category, which accepts text input but returns typed probabilistic outputs — categories, yes/no answers, ratings, and confidence scores — instead of generated text. Jev charges only for input tokens at $0.042 per million, making it cheaper than OpenAI's GPT-5 Nano. By reframing LLM-style inference as a decision function rather than a text generator, Jev could reshape how developers build classification, spam detection, labeling, and ranking systems, offering dramatically lower cost and latency than traditional LLMs. It also signals a broader industry shift toward specialized, task-specific models that integrate directly into software pipelines. Jev supports three question types: 'Noul' yes/no questions returning a Bernoulli-style confidence between 0 and 1, choice questions returning a probability distribution over provided options, and score questions returning a floating-point value along a numeric range. Questions are evaluated in parallel, but the model is currently weak on numbers, dates, and adversarial content, and it offers no explanation for its decisions.

rss · Simon Willison · Sep 21, 23:09

**Background**: Traditional large language models (LLMs) generate free-form text and are billed per input and output token, with output usually costing more. TypeSafe AI's 'System One' name borrows from Daniel Kahneman's distinction between fast intuitive thinking (System 1) and slow deliberate reasoning (System 2), positioning Jev as a fast, cheap decision layer rather than a reasoning engine. Jev is transformer-based but is explicitly not a language model, as it never produces prose.

<details><summary>References</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/">TypeSafe AI Releases Jev: A System One Model ... - MarkTechPost</a></li>
<li><a href="https://www.requesty.ai/blog/typesafe-jev-explained">TypeSafe Jev explained: how it works, LLM differences and... | Requesty</a></li>
<li><a href="https://docs.llmgateway.io/features/system-one">Get typed , probabilistic decisions instead of generated text with the...</a></li>

</ul>
</details>

**Discussion**: Commentators, including Simon Willison and Maggie Appleton, have debated the naming, with Appleton preferring 'decision models' over 'System One models.' A Hacker News discussion confirmed that 'Noul' is short for Bernoulli, and some users expressed discomfort that Jev represents a further regression toward opaque black-box machine learning, since it returns only numbers with no justification.

**Tags**: `#LLM`, `#AI Models`, `#Decision Models`, `#TypeSafe AI`, `#Probabilistic Inference`

---

<a id="item-12"></a>
## [Xiaomi releases MiMo-V2.6 multimodal model with $3.5M RL training cost](https://www.reddit.com/r/MachineLearning/comments/1wn36d4/xiaomi_releases_mimov26_frontier_intelligence_all/) ⭐️ 8.0/10

Xiaomi has released MiMo-V2.6, a frontier multimodal AI model whose total reinforcement learning training cost was disclosed as $3.5 million, accompanied by a live benchmark dashboard and a 'built in public' development approach. The MiMo-V2.6-Pro variant scores 46.32 on the Artificial Analysis Intelligence Index, surpassing Kimi K3 and Qwen3.8 Max to become the strongest open-source model to date. The disclosure of a concrete $3.5M RL training cost and a live benchmark dashboard brings unusual transparency to frontier model development, which is typically kept secret. If MiMo-V2.6-Pro truly leads open-source models, it could shift competitive dynamics among Chinese AI labs and give developers a strong new open-weight option. The MiMo-V2.6 series keeps the API pricing of the V2.5 series, and the lineup includes MiMo-V2.6-Pro, MiMo-V2.6-Flash, and MiMo-V2.6-Pro-UltraSpeed, with monthly or annual subscription plans available. The model is accessible through platforms such as OpenRouter, which lists eight Xiaomi models.

reddit · r/MachineLearning · /u/we_are_mammals · Sep 22, 07:56

**Background**: MiMo is Xiaomi's in-house large language model family, and V2.6 is its latest multimodal iteration capable of handling multiple data types such as text and images. Reinforcement learning (RL) is a training technique where a model learns from reward signals rather than labeled examples, and it is often computationally expensive, making the disclosed $3.5M cost a notable data point. The Artificial Analysis Intelligence Index is a composite benchmark that aggregates multiple evaluation tasks to rank model capability.

<details><summary>References</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo - V 2 . 6 | Xiaomi</a></li>
<li><a href="https://openrouter.ai/xiaomi">Xiaomi API and Models | OpenRouter</a></li>
<li><a href="https://mimo.mi.com/models/en-US/mimo-v2.6-pro">Xiaomi MiMo Home</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Machine Learning`, `#Multimodal`, `#Xiaomi`, `#Model Release`

---

<a id="item-13"></a>
## [Complex KDA Extends Kimi Delta Attention Expressivity](https://www.reddit.com/r/MachineLearning/comments/1wn5uv9/understanding_and_enhancing_kimi_delta_attention_r/) ⭐️ 8.0/10

A new paper titled "Complex KDA: Understanding and Enhancing the Expressivity of Kimi Delta Attention" introduces Complex KDA (CKDA), a modification of Kimi Delta Attention that extends the gate range to [-1,1] and the delta rule learning rate to [0,2]. The authors prove that this form can express any orthogonal diagonal-plus-rank-one matrix and track the S3, S4, and A5 groups, but not S5, with experiments showing stable training and competitive language modeling performance. This work deepens the theoretical understanding of linear attention mechanisms by connecting Kimi Delta Attention to group theory, showing precisely which symmetries it can and cannot represent. It could guide the design of more expressive yet efficient attention architectures for long-context and multimodal models. The key insight is that the full diagonal gate in KDA can act as a reflection, enabling 2D rotations in a single step, but only when the gate range is extended to [-1,1] and the delta rule learning rate to [0,2]. CKDA successfully learns S3 and S4 groups and shows promising results on audio continuation, though it cannot track S5.

reddit · r/MachineLearning · /u/Yossarian_1234 · Sep 22, 10:34

**Background**: Kimi Delta Attention (KDA) is an expressive linear attention module that extends Gated DeltaNet (GDN) with a finer-grained gating mechanism, designed for efficient long-context modeling. Gated DeltaNet itself improves upon Mamba2 by incorporating the delta rule with input-dependent gating to enhance memory retention and selectivity. The delta rule is a classic error-correction learning rule that adapts weights based on the error between actual and desired outputs, and its learning rate controls the size of each update.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2510.26692">Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://arxiv.org/abs/2412.06464">[2412.06464] Gated Delta Networks: Improving Mamba2 with Delta Rule</a></li>
<li><a href="https://jianyuh.github.io/attention/2025/12/13/KDA.html">Linear Attention : Kimi Delta Attention | Jianyu Huang</a></li>

</ul>
</details>

**Tags**: `#attention mechanisms`, `#deep learning theory`, `#expressivity`, `#group theory`, `#Kimi Delta Attention`

---

<a id="item-14"></a>
## [US Proposes AI Incident Reporting Channel With China](https://t.me/zaihuapd/43985) ⭐️ 8.0/10

The United States proposed establishing an AI incident notification channel with China during a September 20 meeting in New York, aimed at reporting AI-related events that meet a national security threshold. US Treasury Secretary Bessent said the move is intended to improve transparency between the two countries, and the two sides also plan regular US-China AI dialogue on shared risks. This is a significant geopolitical development in AI governance, as it could create a novel bilateral mechanism for managing AI risks at the national security level between the world's two leading AI powers. If realized, it could improve global AI safety and transparency, though it remains only a proposal with no formal agreement yet. The proposal has not yet become a bilateral agreement or treaty, and China's official statement confirmed discussions on AI-related topics but did not explicitly accept the specific mechanism. The notification system would create a formalized communication pathway specifically for AI incidents that rise to a national security threshold.

telegram · zaihuapd · Sep 22, 11:34

**Background**: AI incident reporting is an emerging governance concept: for example, US legislation such as the AI Incident Reporting Act would require developers of high-capability models to report dangerous discoveries within seven days. The US-China talks come amid growing unease about AI security risks, including warnings from Anthropic researchers that AI could pose catastrophic threats within the decade, and ahead of a high-stakes Trump-Xi summit.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/us-treasury-ai-notification-china/">US Treasury proposes AI incident notification mechanism after talks...</a></li>
<li><a href="https://dnyuz.com/2026/09/21/u-s-proposes-ai-incident-alert-system-in-talks-with-china/">U.S. proposes AI incident alert system in talks with China – DNYUZ</a></li>
<li><a href="https://www.ft.com/content/d29d769e-039c-4d11-9152-e63ccd397b32?syn-25a6b1a6=1">Scott Bessent hails US - China AI dialogue ahead of Trump-Xi meeting</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#US-China relations`, `#AI safety`, `#international policy`, `#national security`

---

<a id="item-15"></a>
## [China Probes DeepSeek and Moonshot Over Data Leaks to Claude](https://www.theinformation.com/articles/china-probes-deepseek-moonshot-potential-data-leaks-anthropic) ⭐️ 8.0/10

China's internet regulator is investigating DeepSeek and Moonshot AI after Anthropic alleged in a 154-page report published on September 10 that seven Chinese companies improperly forwarded sensitive user data to its Claude models. The report specifically cited DeepSeek forwarding requests from an engineer working on a police surveillance system to Claude. This case sits at the intersection of AI regulation, data privacy, and cross-border data flows, and could set precedents for how Chinese authorities police domestic AI firms accused of leaking sensitive data to foreign models. It also escalates tensions between Anthropic and Chinese AI developers, with potential compliance and reputational consequences for DeepSeek and Moonshot. Anthropic's report names seven Chinese companies and alleges large-scale violations of its Claude usage terms, with the DeepSeek example involving a police surveillance engineer's request. The investigation is being conducted by China's internet regulator, though the source is a brief Telegram post with limited public discussion.

telegram · zaihuapd · Sep 22, 14:37

**Background**: DeepSeek is a Hangzhou-based AI company owned by the hedge fund High-Flyer that develops open-weight large language models. Moonshot AI (月之暗面), named after Pink Floyd's album, is a Chinese AI startup known for its Kimi models with very long context windows. Anthropic is the US company behind the Claude family of AI models, which are widely used via API and consumer apps.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://www.moonshot.ai/">Welcome to Moonshot AI . Our mission is to seek the optimal...</a></li>
<li><a href="https://www.anthropic.com/claude/sonnet">Claude Sonnet \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#data privacy`, `#DeepSeek`, `#Anthropic`, `#China tech policy`

---