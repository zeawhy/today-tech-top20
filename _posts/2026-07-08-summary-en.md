---
layout: default
title: "Horizon Summary: 2026-07-08 (EN)"
date: 2026-07-08
lang: en
---

> From 42 items, 16 important content pieces were selected

---

1. [Tenda Firmware Backdoor Allows Unauthorized Admin Access](#item-1) ⭐️ 9.0/10
2. [OpenAI Announces Public Release of GPT-5.6 Sol, Terra, Luna](#item-2) ⭐️ 9.0/10
3. [GitLost Attack Tricks GitHub AI into Leaking Private Repos](#item-3) ⭐️ 8.0/10
4. [EU Chat Control Proposals Threaten Privacy and Encryption](#item-4) ⭐️ 8.0/10
5. [SICP Video Lectures from 1986 Still Relevant Today](#item-5) ⭐️ 8.0/10
6. [Kokoro: Local CPU-Friendly High-Quality TTS](#item-6) ⭐️ 8.0/10
7. [sqlite-utils 4.0 Adds Schema Migrations, Nested Transactions](#item-7) ⭐️ 8.0/10
8. [Anthropic Projects $1B Profit in Q3 2026](#item-8) ⭐️ 8.0/10
9. [Mozilla CTO AMA on Open Source AI Report](#item-9) ⭐️ 8.0/10
10. [Constraining Fine-Tuning to Trusted LoRA Subspace](#item-10) ⭐️ 8.0/10
11. [Anthropic Launches Claude Cowork for Autonomous Background Tasks](#item-11) ⭐️ 8.0/10
12. [DeepSeek Develops Own AI Chip to Reduce Reliance on Nvidia and Huawei](#item-12) ⭐️ 8.0/10
13. [Alibaba Orders All Employees to Uninstall Claude by July 10](#item-13) ⭐️ 8.0/10
14. [Huawei 5G Flagship Returns Overseas with 1100 Mbps Peak Speed](#item-14) ⭐️ 8.0/10
15. [Critical Android Remote Root Exploit Chain Exposed](#item-15) ⭐️ 8.0/10
16. [Meituan OWL Model Session Data Leak Reported](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Tenda Firmware Backdoor Allows Unauthorized Admin Access](https://kb.cert.org/vuls/id/213560) ⭐️ 9.0/10

CERT/CC disclosed CVE-2026-11405, a hidden authentication backdoor in multiple Tenda router firmware versions, including FH1201, W15E, AC10, AC5, and AC6. The backdoor bypasses password checks via an undocumented admin login path in /bin/httpd. This vulnerability affects millions of Tenda devices worldwide, granting attackers full administrative access without a valid password. It undermines trust in IoT manufacturers and highlights the need for open-source firmware alternatives like OpenWRT. The backdoor password is hardcoded as 'rzadmin' and the username is not validated, so any username works. No patch is currently available from Tenda, leaving users with no official fix.

hackernews · miniBill · Jul 8, 00:08 · [Discussion](https://news.ycombinator.com/item?id=48825749)

**Background**: A backdoor is a hidden method to bypass normal authentication in a system. Hardcoded credentials are embedded in firmware and can be extracted by attackers, leading to unauthorized access. IoT devices often lack regular security updates, making such vulnerabilities especially dangerous.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/319872/20260707/tenda-firmware-backdoor-lets-anyone-log-admin-regardless-password.htm">Tenda Firmware Backdoor Lets Anyone Log In as Admin ...</a></li>
<li><a href="https://thehackernews.com/2026/07/certcc-warns-of-hidden-admin-backdoor.html">CERT/CC Warns of Hidden Admin Backdoor in Tenda Router Firmware</a></li>
<li><a href="https://www.how2shout.com/news/tenda-router-backdoor-cve-2026-11405-no-patch.html">Tenda Routers Have a Hidden Backdoor With No Patch — What to ...</a></li>

</ul>
</details>

**Discussion**: Community members expressed frustration with manufacturers' security practices, with one user stating they would only use OpenWRT on routers. Another noted the backdoor password 'rzadmin' was publicly disclosed in a 2022 writeup, and comparisons were drawn to the LKWPETER incident.

**Tags**: `#security`, `#backdoor`, `#firmware`, `#IoT`, `#vulnerability`

---

<a id="item-2"></a>
## [OpenAI Announces Public Release of GPT-5.6 Sol, Terra, Luna](https://x.com/OpenAI/status/2074704958419792299) ⭐️ 9.0/10

OpenAI announced that GPT-5.6 Sol, Terra, and Luna will be publicly released on Thursday, July 9, 2026, with global preview access expansion. This release marks a significant advancement in AI capabilities, offering three tiers of models—frontier reasoning (Sol), balanced performance (Terra), and cost-efficient speed (Luna)—catering to diverse developer and enterprise needs. Sol is built for frontier reasoning and long-horizon agentic work, Terra offers GPT-5.5-competitive performance at 2x lower cost, and Luna is the fastest, most affordable member of the family.

telegram · zaihuapd · Jul 8, 04:17

**Background**: GPT-5.6 is the latest generation of OpenAI's large language model series. The three models—Sol, Terra, and Luna—are named after celestial bodies, reflecting their different roles: Sol as the flagship, Terra as the balanced option, and Luna as the lightweight variant.

<details><summary>References</summary>
<ul>
<li><a href="https://community.openai.com/t/introducing-gpt-5-6-series-sol-terra-and-luna/1384931">Introducing GPT-5.6 series: Sol, Terra and Luna</a></li>
<li><a href="https://www.explainx.ai/blog/gpt-5-6-release-date-features-benchmarks-2026">GPT-5.6: Public Launch July 9 — Sol, Terra, Luna - explainx.ai</a></li>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-5.6`, `#AI`, `#release`

---

<a id="item-3"></a>
## [GitLost Attack Tricks GitHub AI into Leaking Private Repos](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/) ⭐️ 8.0/10

Researchers demonstrated a prompt injection attack called GitLost that tricks GitHub's AI agent into leaking private repository data by embedding malicious instructions in public issues or comments. This attack highlights a fundamental security flaw in agentic AI systems, analogous to SQL injection in web applications, and could affect any AI agent that processes untrusted content while having access to sensitive data. The attack works by placing a prompt injection payload in a public GitHub issue that the AI agent reads; the payload instructs the agent to exfiltrate private repository contents. The researchers bypassed GitHub's guardrails with a simple word like "Additionally" to override system instructions.

hackernews · ColinEberhardt · Jul 8, 05:25 · [Discussion](https://news.ycombinator.com/item?id=48827858)

**Background**: Prompt injection is a cybersecurity exploit where malicious inputs cause unintended behavior in large language models (LLMs). Agentic AI systems are semi-autonomous AI that can perceive, reason, and act; they often have access to sensitive data and can be tricked by indirect prompt injection from web content.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is Agentic AI? | IBM</a></li>

</ul>
</details>

**Discussion**: Commenters debated responsibility: some argued it's a user configuration issue, while others noted that prompt injection is a fundamental flaw in LLMs that cannot be fixed by guardrails alone. The discussion drew parallels to SQL injection, with some saying prompt injection is even more fatal.

**Tags**: `#prompt injection`, `#AI security`, `#GitHub`, `#agentic AI`, `#vulnerability research`

---

<a id="item-4"></a>
## [EU Chat Control Proposals Threaten Privacy and Encryption](https://fightchatcontrol.eu/chat-control-overview) ⭐️ 8.0/10

The EU is advancing two legislative proposals, Chat Control 1.0 and 2.0, that would mandate scanning of private communications for child sexual abuse material, with Chat Control 2.0 explicitly targeting end-to-end encrypted messages. These proposals could fundamentally undermine encryption and privacy for all EU citizens, setting a dangerous precedent for mass surveillance without judicial oversight. Chat Control 1.0 expired in April 2025 but the EU Council revived it within 90 days, while Chat Control 2.0 would require client-side scanning of encrypted messages, effectively bypassing end-to-end encryption.

hackernews · gasull · Jul 7, 14:23 · [Discussion](https://news.ycombinator.com/item?id=48818311)

**Background**: Chat Control refers to EU legislative efforts to combat child sexual abuse material by mandating communication platforms to scan user messages. The proposals have been criticized for enabling mass surveillance and violating fundamental rights, with the EU Council's own Legal Service warning they breach Article 7 of the EU Charter of Fundamental Rights.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://fightchatcontrol.eu/chat-control-overview">Chat Control 1.0 vs 2.0 - Fight Chat Control</a></li>
<li><a href="https://byteiota.com/eu-council-chat-control-1-revival-2026/">EU Council Revives Chat Control 1.0 After Parliament Killed It</a></li>

</ul>
</details>

**Discussion**: Commenters express strong opposition, arguing that the proposals are a pretext for surveillance and that real child protection requires better policing, not mass scanning. Some note that the voluntary nature for providers still allows client-side scanning, which undermines encryption.

**Tags**: `#privacy`, `#encryption`, `#EU legislation`, `#surveillance`, `#digital rights`

---

<a id="item-5"></a>
## [SICP Video Lectures from 1986 Still Relevant Today](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video_galleries/video-lectures/) ⭐️ 8.0/10

MIT has made available the classic 1986 video lectures for the course Structure and Interpretation of Computer Programs (SICP), taught by Hal Abelson and Gerald Jay Sussman, originally produced for Hewlett-Packard employees. SICP is a foundational computer science text, and these lectures provide a timeless introduction to programming fundamentals, abstraction, and Lisp, influencing generations of programmers and remaining highly relevant for self-learners. The lectures are professionally produced by Hewlett-Packard Television and consist of 20 videos covering the entire course. The audio quality is noted as poor by some viewers, but the content remains excellent.

hackernews · gjvc · Jul 7, 23:57 · [Discussion](https://news.ycombinator.com/item?id=48825664)

**Background**: SICP, also known as the "Wizard Book," was used as MIT's introductory computer science textbook from 1984 to 2007. It teaches fundamental principles such as recursion, abstraction, modularity, and programming language design, using the Lisp dialect Scheme. The lectures offer a complementary, more accessible way to engage with the material compared to the book alone.

<details><summary>References</summary>
<ul>
<li><a href="https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video_galleries/video-lectures/">Video Lectures | Structure and Interpretation of Computer Programs | Electrical Engineering and Computer Science | MIT OpenCourseWare</a></li>
<li><a href="https://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs">Structure and Interpretation of Computer Programs</a></li>
<li><a href="https://www.youtube.com/playlist?list=PL8FE88AA54363BC46">SICP Lectures - YouTube</a></li>

</ul>
</details>

**Discussion**: Commenters recommend using Racket with the sicp package as a modern alternative to MIT Scheme for following along. Some find the lectures more effective than the book alone, and one user credits SICP for launching a career in Clojure. A question about relevance to systems programming is raised, and audio quality is a common complaint.

**Tags**: `#SICP`, `#computer science education`, `#Lisp`, `#programming fundamentals`, `#MIT OCW`

---

<a id="item-6"></a>
## [Kokoro: Local CPU-Friendly High-Quality TTS](https://ariya.io/2026/03/local-cpu-friendly-high-quality-tts-text-to-speech-with-kokoro/) ⭐️ 8.0/10

Kokoro, an open-weight TTS model with 82 million parameters, enables high-quality text-to-speech on local CPUs without requiring expensive GPUs. It supports multiple languages, voices, and input formats including EPUB and PDF. This makes high-quality TTS accessible to users without dedicated GPUs, lowering the barrier for accessibility tools, offline applications, and privacy-preserving voice synthesis. It challenges the assumption that good TTS requires cloud or high-end hardware. Kokoro's lightweight architecture delivers quality comparable to larger models while being faster and more cost-efficient. However, it struggles with single-word utterances and homographs (words with same spelling but different pronunciations), though users can manually add IPA pronunciation guides.

hackernews · speckx · Jul 7, 18:24 · [Discussion](https://news.ycombinator.com/item?id=48821576)

**Background**: Text-to-speech (TTS) systems convert written text into spoken audio. Traditional high-quality TTS often requires powerful GPUs or cloud services, limiting accessibility. Kokoro is part of a trend toward efficient, local-first AI models that run on consumer hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/hexgrad/kokoro">GitHub - hexgrad/kokoro: https://hf.co/hexgrad/Kokoro-82M</a></li>
<li><a href="https://github.com/nazdridoy/kokoro-tts">GitHub - nazdridoy/kokoro-tts: A CLI text-to-speech tool ...</a></li>
<li><a href="https://kokorottsai.com/">Kokoro TTS: Advanced AI Text-to-Speech Model with 82M parameters</a></li>

</ul>
</details>

**Discussion**: Community members praise Kokoro for its accessibility and quality, especially for those without NVIDIA GPUs. Some note its limitations with homographs and single words, but appreciate the ability to add custom IPA guides. Others are integrating it into reader apps and podcasts.

**Tags**: `#TTS`, `#accessibility`, `#open-source`, `#machine learning`, `#CPU-friendly`

---

<a id="item-7"></a>
## [sqlite-utils 4.0 Adds Schema Migrations, Nested Transactions](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything) ⭐️ 8.0/10

sqlite-utils 4.0 has been released, introducing database schema migrations, nested transactions via a new db.atomic() method, and support for compound foreign keys. This major update brings essential database management features to a widely-used SQLite utility, enabling developers to safely evolve database schemas and handle complex transactions more easily. Migrations are defined in Python files using the sqlite-utils library, leveraging the table.transform() method for schema changes that go beyond SQLite's limited ALTER TABLE. The release also includes breaking changes detailed in an upgrade guide.

rss · Simon Willison · Jul 7, 19:32

**Background**: SQLite is a lightweight, embedded database engine that does not natively support robust schema migrations or nested transactions. sqlite-utils is a Python library and CLI tool that simplifies working with SQLite databases. The new migration system tracks applied changes and applies pending ones automatically.

<details><summary>References</summary>
<ul>
<li><a href="https://sqlite-utils.datasette.io/en/latest/migrations.html">Database migrations - sqlite-utils</a></li>
<li><a href="https://simonwillison.net/2026/Jul/7/sqlite-utils-4/">sqlite-utils 4.0, now with database schema migrations</a></li>
<li><a href="https://github.com/simonw/sqlite-migrate">GitHub - simonw/sqlite-migrate: A simple database migration ... GitHub - simonw/sqlite-utils: Python CLI utility and library ... sqlite-utils 4.0rc1 adds migrations and nested transactions Managing Database Versions and Migrations in SQLite sqlite-utils 4.0rc1 adds migrations and nested transactions</a></li>

</ul>
</details>

**Tags**: `#sqlite`, `#database`, `#python`, `#migrations`, `#open source`

---

<a id="item-8"></a>
## [Anthropic Projects $1B Profit in Q3 2026](https://newsletter.semianalysis.com/p/anthropic-3q26-profit-over-1b-the) ⭐️ 8.0/10

Anthropic is projected to achieve over $1 billion in profit by Q3 2026, according to exclusive financial analysis from Semianalysis, signaling strong financial health ahead of a potential IPO. This projection positions Anthropic as a major player in the AI industry, potentially reshaping the competitive landscape and attracting significant investor interest for its IPO. The analysis is based on exclusive financial data from a reputable source, Semianalysis, and highlights Anthropic's profitability and market position, though specific revenue breakdowns are not provided.

rss · Semianalysis · Jul 8, 06:04

**Background**: Anthropic is an AI safety company known for developing the Claude model series. Profitability is a key metric for tech companies considering an IPO, as it demonstrates sustainable business growth.

**Tags**: `#Anthropic`, `#AI`, `#IPO`, `#financials`, `#industry analysis`

---

<a id="item-9"></a>
## [Mozilla CTO AMA on Open Source AI Report](https://www.reddit.com/r/MachineLearning/comments/1upxdvc/raffi_krikorian_cto_mozilla_ama_on_the_state_of/) ⭐️ 8.0/10

Mozilla CTO Raffi Krikorian will host an AMA on July 14, 2025, to discuss the inaugural State of Open Source AI report, covering hidden costs of 'free' models, enterprise adoption, China's influence, and developer trust. This AMA provides direct insight from a major open-source advocate on the real-world challenges and opportunities in open-source AI, which is critical for developers and enterprises making strategic decisions. The report is based on a survey of over 950 developers and focuses on production realities, including the 'agentic harness' layer where competition is shifting from models to infrastructure.

reddit · r/MachineLearning · /u/raffikrikorian · Jul 7, 14:51

**Background**: Open-source AI models like Llama and Mistral are widely used, but deploying them in production often incurs hidden costs for security, privacy, and integration. The 'agentic harness' refers to the software infrastructure surrounding an LLM that manages context, memory, and tool use, which is becoming the key differentiator.

<details><summary>References</summary>
<ul>
<li><a href="https://www.startuphub.ai/ai-news/ai-research/2026/mozilla-ai-future-the-open-source-counter-manifesto">Mozilla AI Future: The Open Source Counter-Manifesto | StartupHub.ai</a></li>
<li><a href="https://opendatascience.com/what-is-an-agent-harness-the-architecture-behind-reliable-agentic-ai/">What is an Agent Harness? The Architecture Behind Agentic AI</a></li>
<li><a href="https://www.entrepreneur.com/science-technology/this-is-the-hidden-ai-tax-that-founders-need-to-budget-for/504341">This Is the Hidden ‘AI Tax’ That Founders Need to Budget For</a></li>

</ul>
</details>

**Tags**: `#open source AI`, `#Mozilla`, `#enterprise AI`, `#developer trust`, `#AI ecosystem`

---

<a id="item-10"></a>
## [Constraining Fine-Tuning to Trusted LoRA Subspace](https://www.reddit.com/r/MachineLearning/comments/1uq68li/what_if_a_model_could_only_learn_what_trusted/) ⭐️ 8.0/10

A new paper proposes constraining fine-tuning to a subspace learned from trusted LoRA adapters, preventing the model from learning malicious updates that lie outside this subspace. This approach offers a novel defense against fine-tuning poisoning attacks, which are a growing security concern as models are fine-tuned on user-provided or external data. By geometrically restricting the model's update space, it can block backdoors without needing to detect poisoned data. The method was tested on 196 public LoRA adapters, including adaptive attacks designed to bypass the defense, and achieved a sharp drop in attack success while preserving useful adaptation on tasks covered by the adapter pool.

reddit · r/MachineLearning · /u/Bright_Warning_8406 · Jul 7, 20:00

**Background**: LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning technique that updates a model by adding small, trainable low-rank matrices instead of modifying all parameters. Fine-tuning poisoning attacks inject malicious data into the training set to introduce hidden behaviors or backdoors. Existing defenses often focus on detecting poisoned samples or reducing their impact, but this work takes a different approach by constraining the model's update space.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/deep-learning/low-rank-adaptation-lora/">Low Rank Adaptation (LoRA) - GeeksforGeeks</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#security`, `#fine-tuning`, `#LoRA`, `#adversarial robustness`

---

<a id="item-11"></a>
## [Anthropic Launches Claude Cowork for Autonomous Background Tasks](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) ⭐️ 8.0/10

Anthropic has launched Claude Cowork, a new feature for Pro, Max, Team, and Enterprise users that allows the AI to autonomously complete complex multi-step tasks in the background across desktop, web, and mobile platforms. This marks a significant step toward practical AI agents that can handle real-world office work asynchronously, potentially boosting productivity for professionals and changing how users interact with AI assistants. Tasks run on Anthropic's servers and continue even if the user closes their computer; the desktop version can read and write local files and control the browser, and users can set scheduled tasks and manage them via projects.

telegram · zaihuapd · Jul 8, 03:50

**Background**: Claude is a family of large language models developed by Anthropic, trained using constitutional AI for ethical compliance. Claude Cowork extends the assistant's capabilities from simple Q&A to autonomous execution of multi-step workflows, such as generating Excel spreadsheets with formulas or creating presentations.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/cowork">Claude Cowork | Claude by Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Cowork">Claude Cowork</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#Claude`, `#autonomous agents`, `#product launch`

---

<a id="item-12"></a>
## [DeepSeek Develops Own AI Chip to Reduce Reliance on Nvidia and Huawei](https://t.me/zaihuapd/42423) ⭐️ 8.0/10

DeepSeek, a Chinese AI company, is developing its own AI inference chip to reduce dependence on Nvidia and Huawei chips. The project started about a year ago and is still in early stages, with the company actively recruiting chip design engineers. This move could help DeepSeek achieve greater hardware independence amid US export restrictions on advanced AI chips to China. It also signals a broader trend of Chinese AI companies investing in custom silicon to secure their supply chains and reduce geopolitical risks. The chip is focused on inference, the stage where a trained model generates responses for users, rather than training. DeepSeek has begun contacting chip design, foundry, and memory companies, and has been privately recruiting chip design engineers in recent months.

telegram · zaihuapd · Jul 8, 05:20

**Background**: DeepSeek previously relied on Nvidia H800 and Huawei Ascend chips for its models. US export controls have restricted China's access to advanced AI chips, prompting Chinese companies to develop their own alternatives. AI inference chips are specialized hardware designed to run trained AI models efficiently, as opposed to training chips which are used to train models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NVIDIA_H800_GPU">NVIDIA H800 GPU</a></li>
<li><a href="https://tech-insider.org/huawei-ascend-950pr-ai-chip-nvidia-china-2026/">Huawei Ascend 950PR: The 1.56 PFLOP AI Chip vs Nvidia [2026]</a></li>
<li><a href="https://uvation.com/articles/ai-inference-chips-latest-rankings-who-leads-the-race">AI Inference Chips 2025: Rankings & Leaders - uvation.com</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#DeepSeek`, `#semiconductors`, `#China tech`, `#inference hardware`

---

<a id="item-13"></a>
## [Alibaba Orders All Employees to Uninstall Claude by July 10](https://t.me/zaihuapd/42424) ⭐️ 8.0/10

Alibaba has internally ordered all employees to uninstall Anthropic products including Claude Sonnet, Opus, Fable, and Claude Code by July 10, 2026, reversing its previous policy of reimbursing employees for using external AI models. This ban signals escalating tensions in AI competition and intellectual property disputes, potentially setting a precedent for other Chinese tech companies to restrict foreign AI tools and impacting enterprise AI usage policies globally. The ban follows Anthropic's allegations that Alibaba used approximately 25,000 fake accounts to interact with Claude over 28 million times between April 22 and June 5, 2026, for model distillation. Alibaba had previously reimbursed employees for using Claude, GPT, Gemini, and other external models.

telegram · zaihuapd · Jul 8, 06:09

**Background**: Model distillation is a technique where a smaller model is trained to mimic a larger, more capable model, often by using the larger model's outputs. Anthropic's Claude models are advanced AI assistants, and Claude Code is an agentic coding tool. The ban reflects growing concerns over intellectual property theft and unauthorized use of AI models in the competitive AI landscape.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/sites/jonmarkman/2026/06/26/anthropic-says-alibaba-used-25000-fake-accounts-to-distill-claude/">Anthropic Says Alibaba Used 25,000 Fake Accounts To Distill ...</a></li>
<li><a href="https://www.explainx.ai/blog/anthropic-alibaba-claude-distillation-25000-fake-accounts-2026">Anthropic vs Alibaba — 25K Fake Claude Accounts, Distillation ...</a></li>
<li><a href="https://www.timesnownews.com/technology-science/anthropic-faces-backlash-after-hidden-claude-code-sparks-spying-allegations-article-154862268">Anthropic Faces Backlash After Hidden Claude Code Sparks ...</a></li>

</ul>
</details>

**Tags**: `#Alibaba`, `#Claude`, `#Anthropic`, `#AI policy`, `#enterprise`

---

<a id="item-14"></a>
## [Huawei 5G Flagship Returns Overseas with 1100 Mbps Peak Speed](https://finance.sina.com.cn/tech/roll/2026-07-08/doc-inihapna8035781.shtml) ⭐️ 8.0/10

Huawei's Pura 90 Pro Max international version natively supports 5G, achieving peak download speeds exceeding 1100 Mbps in overseas tests, marking the official return of Huawei 5G flagships to global markets after seven years of US sanctions. This signals Huawei's successful breakthrough in 5G chip supply and its ability to compete globally again, potentially reshaping the high-end smartphone market landscape and challenging established players like Apple and Samsung. The device displays a 5G icon and uses Huawei's 5A communication technology, which is not a new network standard but a suite of advanced communication features. The return follows the Mate 60 series' domestic breakthrough in 2023 and the HarmonyOS 6.0.0.125 update that enabled 5A technology.

telegram · zaihuapd · Jul 8, 12:17

**Background**: Since 2019, US sanctions prevented Huawei from sourcing 5G chips and components, forcing its flagships to use 4G. In 2023, the Mate 60 series surprised the market with a domestically produced 5G-capable chip. Huawei's 5A technology, introduced in early 2026, enhances connectivity without requiring new network infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/0/901/311.htm">华为官网详解“5A”先进通信技术：不等同于 5G-A / 5.5G，不涉及额外资...</a></li>
<li><a href="https://consumer.huawei.com/cn/support/content/zh-cn16081318/">华为5A相关问题汇总 | 华为官网 - HUAWEI</a></li>
<li><a href="https://www.sohu.com/a/973505944_121784105">2.26GB大更新！Mate60系列获鸿蒙6.0.0.125升级，5A通信正式上车_支持_...</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#5G`, `#smartphone`, `#technology`, `#telecommunications`

---

<a id="item-15"></a>
## [Critical Android Remote Root Exploit Chain Exposed](https://www.coolapk.com/feed/72700258?s=ZGQ2MTVlZjYxMDYyNTM3ZzZhNGUzOThjega1640) ⭐️ 8.0/10

Nebula Security researchers revealed a remote root exploit chain called IonStack that compromises Android 17 and earlier devices via a single malicious link, combining a Firefox browser vulnerability and a 15-year-old Linux kernel bug. Proof-of-concept code has been published on GitHub. This is the first publicly demonstrated remote root exploit for Android 17, allowing attackers to gain persistent root access and full device control without user interaction beyond clicking a link. It poses an immediate risk to millions of Android users, especially those on older devices or unpatched browsers. The exploit chain uses a Firefox browser vulnerability (likely CVE-2024-29943 or similar) for initial code execution, then escalates privileges via a Linux kernel use-after-free bug (CVE-2024-1086) affecting kernels v5.14 to v6.6. Google Pixel devices have been successfully tested, and the Linux kernel fix is already available.

telegram · zaihuapd · Jul 8, 13:01

**Background**: Android devices rely on a layered security model, with the Linux kernel providing isolation between apps and the system. Remote root exploits are rare because they require chaining multiple vulnerabilities across different components. The IonStack exploit demonstrates a browser-to-kernel attack, bypassing Android's sandbox and SELinux protections.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/android-17-root-1-click/">First-Ever 1- Click Android 17 Exploit Allows Attackers to ...</a></li>
<li><a href="https://github.com/Notselwyn/CVE-2024-1086">GitHub - Notselwyn/CVE-2024-1086: Universal local privilege ...</a></li>
<li><a href="https://vulners.com/githubexploit/F91A4BDD-E880-59C9-B6CE-8DDBFB8AB668">Exploit for Out-of-bounds Write in Mozilla Firefox - exploit ...</a></li>

</ul>
</details>

**Tags**: `#Android`, `#security`, `#vulnerability`, `#root exploit`, `#Linux kernel`

---

<a id="item-16"></a>
## [Meituan OWL Model Session Data Leak Reported](https://github.com/gumusserv/ProducerBenchV2/blob/83cad6007ef3fe8df33386e8f43738fe62337e16/parsed_source_data/data/) ⭐️ 8.0/10

Meituan's OWL (LongCat) free test model on OpenRouter reportedly leaked session data, which appeared in a public GitHub repository before being taken down. The leak was discovered by a Discord bot token scanner that detected exposed tokens. This incident highlights the security risks of using public AI models for sensitive conversations, as session logs can become new sensitive data assets. It serves as a critical reminder for users to avoid inputting API keys, private keys, or proprietary data into such models. The leaked data appeared in a GitHub repository at least as early as July 7, 2026, 23:32:33 Beijing time. The repository was later made inaccessible, and the exposed tokens were reportedly reset by the Discord bot token scanner.

telegram · zaihuapd · Jul 8, 13:35

**Background**: Meituan's LongCat-2.0 is a 1.6 trillion parameter MoE model, MIT-licensed, trained on domestic Chinese chips, and was anonymously tested as 'Owl Alpha' on OpenRouter. OpenRouter is a unified API platform providing access to hundreds of LLMs. Discord bot token scanners automatically detect and revoke exposed tokens in public repositories.

<details><summary>References</summary>
<ul>
<li><a href="https://aitoolsrecap.com/Blog/longcat-2-meituan-open-source-chinese-chips-2026">LongCat-2.0: The 1.6T Open-Source AI That Was Secretly ...</a></li>
<li><a href="https://openrouter.ai/openrouter">OpenRouter API and Models | OpenRouter</a></li>
<li><a href="https://top.gg/bot/842154960397008896">Add Token Scanner Discord Bot | The #1 Discord Bot and ...</a></li>

</ul>
</details>

**Tags**: `#data leakage`, `#AI security`, `#privacy`, `#LLM`, `#Meituan`

---