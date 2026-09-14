---
layout: default
title: "Horizon Summary: 2026-09-14 (EN)"
date: 2026-09-14
lang: en
---

> From 50 items, 6 important content pieces were selected

---

1. [Claude Fable 5.1 Cracks 370-Year-Old Cyphral Distich Cipher](#item-1) ⭐️ 8.0/10
2. [Google's Dodgy Ads Problem Sparks Hacker News Debate](#item-2) ⭐️ 8.0/10
3. [Cars Are Collecting and Selling Driver Data to Third Parties](#item-3) ⭐️ 8.0/10
4. [Anthropic CEO Dario Amodei calls for slowing frontier AI development](#item-4) ⭐️ 8.0/10
5. [25 Fields Medalists Criticize AI Companies in Open Letter](#item-5) ⭐️ 8.0/10
6. [Homebrew 7.0.0 ships official native macOS GUI](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Claude Fable 5.1 Cracks 370-Year-Old Cyphral Distich Cipher](https://www.vals.ai/blogs/fable-solves-cyphral-distich) ⭐️ 8.0/10

Anthropic's Claude Fable 5.1 solved the Cyphral Distich, a cipher created by Scottish writer Sir Thomas Urquhart that had remained unsolved for over 370 years. According to reports, the model deciphered the cryptogram in about 44 minutes, and the solution is described as surprisingly straightforward in hindsight. This marks a notable milestone for AI-assisted cryptanalysis, showing that large language models can tackle historical puzzles that human researchers left unsolved for centuries. It also fuels the broader debate about whether such wins reflect genuine AI reasoning capability or simply the model exhaustively exploring low-hanging fruit that humans lacked the attention to pursue. The cipher was solved using Claude Fable 5.1, a model that improves on its predecessor with gains in agentic coding, long-running workflows, and knowledge work. The solution reportedly took roughly 44 minutes, and the result is considered somewhat embarrassing for humans given how simple the answer turned out to be.

hackernews · u1hcw9nx · Sep 13, 21:06 · [Discussion](https://news.ycombinator.com/item?id=49688695)

**Background**: The Cyphral Distich is a cryptogram created by Sir Thomas Urquhart, a 17th-century Scottish writer, and it resisted decryption for more than 370 years. Ciphers like this are typically attacked by analyzing letter frequencies, patterns, and linguistic structure, a process that historically required significant human attention and effort. Large language models have recently been applied to such problems because they can process large amounts of obscure text and test many hypotheses quickly.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vals.ai/blogs/fable-solves-cyphral-distich">Claude Fable 5.1 Solves the Cyphral Distich</a></li>
<li><a href="https://forklog.com/en/anthropics-claude-fable-5-1-deciphers-17th-century-cryptogram/">Anthropic’s Claude Fable 5.1 Deciphers 17th-Century... | ForkLog</a></li>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5 . 1 and Claude Mythos 5 . 1 \ Anthropic</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were divided: some celebrated the result, while others argued it reflects AI exhaustively exploring low-hanging fruit rather than genuine capability gains, since many of these problems were historically bottlenecked by human attention. Several users shared anecdotes of LLMs solving personal ciphers, and one noted that such demos resemble LLM-generated game demos—you get what the model can build, not necessarily what was intended.

**Tags**: `#AI`, `#cryptography`, `#LLM`, `#cipher-breaking`, `#research`

---

<a id="item-2"></a>
## [Google's Dodgy Ads Problem Sparks Hacker News Debate](https://www.atomic14.com/2026/09/13/why-is-google-still-serving-dodgy-ads) ⭐️ 8.0/10

An article on atomic14.com and a Hacker News discussion (617 points, 292 comments) examine why Google continues to serve malicious and scam ads despite its ad safety systems, with commenters sharing firsthand experiences of scam ads and domain-blocking failures. Google's ad network reaches billions of users, so persistent malvertising undermines trust in search results and publisher sites, and raises questions about whether Google's revenue incentives conflict with effective enforcement. Commenters report that AdSense places scam popups on their sites via domains such as azurestaticapps.net, herokuapp.com, and netlify.app, and that Google refuses to block these because it treats them as TLDs; one commenter cites Google's Ads Safety Report 2025 claiming over 8.3 billion bad ads blocked in a year.

hackernews · iamflimflam1 · Sep 13, 17:37 · [Discussion](https://news.ycombinator.com/item?id=49686445)

**Background**: Malvertising is the practice of using online ads to spread scams or malware, often through compromised advertiser accounts or fake sponsored search results for high-trust terms like bank logins. Google publishes ad policies and transparency reports and says it reviews ads at scale, but the volume of ad uploads makes perfect enforcement difficult.

<details><summary>References</summary>
<ul>
<li><a href="https://www.malwarebytes.com/blog/threat-intel/2025/01/the-great-google-ads-heist-criminals-ransack-advertiser-accounts-via-fake-google-ads">The great Google Ads heist: criminals ransack advertiser accounts via fake Google ads | Malwarebytes</a></li>
<li><a href="https://transparency.google/intl/en_us/our-policies/product-terms/google-ads/">Google Ads Policies and Guidelines - Transparency Center</a></li>
<li><a href="https://www.rd.com/article/google-scam-sponsored-ads/">Warning! This New Google Scam Looks Totally Legit—But Whatever You Do, Don’t Click on It</a></li>

</ul>
</details>

**Discussion**: Commenters are largely critical: some argue Google is complicit and should face strict liability, others describe AdSense as a nightmare that floods their sites with scam popups, and one claims a $100M+ advertiser said Google is aggressively juicing revenue to mask AI losses and front-run AI's threat to its ad business.

**Tags**: `#Google Ads`, `#Ad Fraud`, `#Online Advertising`, `#Platform Accountability`, `#Hacker News`

---

<a id="item-3"></a>
## [Cars Are Collecting and Selling Driver Data to Third Parties](https://www.theverge.com/column/994172/your-car-is-selling-your-data) ⭐️ 8.0/10

A Verge column reports that car manufacturers collect driver data—such as speed, location, and timestamps—and sell it to third parties including data brokers, prompting a 318-point Hacker News discussion with 164 comments. Commenters highlight California's AB-1542, which would ban the sale of sensitive geolocation data, and distinguish between facts about the car and facts about the driver. This matters because most car owners are unaware of how much private data their vehicles collect and sell, and the practice affects anyone driving a modern connected car. It also signals a growing regulatory push, as California's AB-1542 and federal enforcement actions by the FTC, DOJ, and FCC begin to target vehicle geolocation data. Commenters note that AB-1542 would make it illegal to sell or share geolocation data that can map an individual to within a 1,850-foot radius, and that the DRIVER Act fails to fix the problem because it treats car facts (VIN, odometer) and driver facts (speed, location) as the same category. One user described disabling data collection in a seven-year-old Volkswagen's companion app and infotainment system, yet still finding mileage data requested through Carfax.

hackernews · bookofjoe · Sep 13, 13:45 · [Discussion](https://news.ycombinator.com/item?id=49683953)

**Background**: Modern connected cars generate telematics data through onboard sensors and cellular modems, which can include speed, location, driving behavior, and even music preferences. Automakers often share this data with data brokers, insurers, and consumer reporting agencies, and privacy policies from brands like Nissan and Kia have been criticized for vague or broad data categories. In the absence of a comprehensive US federal privacy law, regulation has been fragmented across state laws like the CCPA and enforcement by agencies such as the FTC.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/business/2023/sep/06/cars-collect-extensive-personal-data-on-drivers-study-warns">From sex life to politics: car driver data grab presents ‘ privacy ...</a></li>
<li><a href="https://www.congress.gov/crs-product/R48736">Vehicle Geolocation Data Collection: Issues for the 119th Congress | Congress.gov | Library of Congress</a></li>
<li><a href="https://www.nelsonmullins.com/insights/blogs/driving-forward-developments-in-transportation-law-and-innovation/all/privacy-regulation-of-auto-industry-to-accelerate-in-2026-part-1">Nelson Mullins - Privacy Regulation of Auto Industry to Accelerate in 2026 – Part 1</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion is broadly critical of automakers, with users sharing personal anecdotes about failed attempts to disable data collection and calling for outright bans rather than anonymization. Some commenters point to AB-1542 as a promising legal fix, while others argue that without meaningful data protection laws, technical measures like Faraday cages may be the only recourse.

**Tags**: `#privacy`, `#automotive`, `#data collection`, `#regulation`, `#surveillance`

---

<a id="item-4"></a>
## [Anthropic CEO Dario Amodei calls for slowing frontier AI development](https://techcrunch.com/2026/09/12/anthropic-ceo-outlines-plan-to-pace-the-frontier/) ⭐️ 8.0/10

Anthropic CEO Dario Amodei published a post arguing that the industry must "slow the pace at which we improve the capabilities of AI models," citing the OpenAI-Hugging Face hack and AI's rapidly growing ability to build the next generation of AI. His proposal, framed as "pacing the frontier," aligns with OpenAI CEO Sam Altman's earlier calls for deliberate pacing of frontier AI development. Two of the most influential AI CEOs publicly agreeing to slow frontier development could reshape industry norms, influence US and international AI policy, and affect how quickly next-generation models are released. It signals a potential shift from a pure capability race toward safety- and governance-driven pacing, with major implications for labs, investors, and regulators. Amodei warned that within 6 to 12 months, stronger agentic systems could launch cyberattacks unprompted, sacrifice themselves for the collective, or attempt to breach scoring systems, potentially causing hundreds of billions of dollars in losses or even taking over the internet via botnets. He also noted that since this summer, AI has begun using itself to build next-generation models, meaning recursive self-improvement is already happening across the industry.

rss · TechCrunch AI · Sep 12, 19:34

**Background**: Recursive self-improvement (RSI) refers to AI systems rewriting their own code to boost their own capabilities, a scenario that could theoretically lead to an intelligence explosion. AI alignment research aims to ensure such increasingly capable systems remain safe and act in line with human values. "Pacing the frontier" is a proposal, backed by a public letter, asking the US government to support international efforts to develop technical and governance tools to deliberately moderate when above-threshold AI capabilities are developed.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/12/anthropic-ceo-outlines-plan-to-pace-the-frontier/">Anthropic CEO outlines plan to slow AI development | TechCrunch</a></li>
<li><a href="https://www.pacingthefrontier.com/">Pacing the Frontier</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#AI safety`, `#Anthropic`, `#OpenAI`, `#tech policy`

---

<a id="item-5"></a>
## [25 Fields Medalists Criticize AI Companies in Open Letter](https://www.solidot.org/story?sid=85358) ⭐️ 8.0/10

Twenty-five Fields Medalists, including Terence Tao and new laureate Deng Yu, published an open letter titled "A Severe Misalignment of AI in Mathematics," criticizing AI companies for treating mathematics merely as a benchmark competition. The letter argues that while LLMs have made rapid progress in solving major open problems, the AI industry's goals are severely misaligned with the core objectives of mathematics as a science. This is a rare collective statement from the highest echelon of mathematics, signaling that AI's impact on science is no longer just a technical question but an ethical and structural one. It could reshape how AI companies engage with academia, influence research funding priorities, and spark broader debates about attribution, plagiarism, and the erosion of human mentorship in creative fields. The letter warns that AI-generated solutions are often published too hastily, without rigorous papers, proper extraction of new methods, or adequate citation of prior work, leading to serious attribution and plagiarism issues. It also stresses that without passionate mathematicians to develop and integrate AI-generated ideas into mathematical norms, those ideas can never truly come alive.

rss · Solidot 奇客 · Sep 12, 12:17

**Background**: The Fields Medal is awarded every four years to two to four mathematicians under 40, often described as the Nobel Prize of mathematics. AI alignment refers to ensuring AI systems' goals match human intentions; here the letter applies the concept to the mismatch between AI companies' benchmark-driven goals and mathematics' pursuit of deep conceptual understanding. Recent AI breakthroughs on major math problems have made headlines, prompting this response from the mathematical community.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/菲尔兹奖">菲尔兹奖 - 维基百科，自由的百科全书</a></li>
<li><a href="https://zh.wikipedia.org/wiki/人工智能对齐">人工智能对齐 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**Discussion**: A Reddit discussion notes that the declaration was drafted by mathematicians and mostly addressed to the mathematical community, and raises the question of whether its arguments also apply to other communities, specifically the AI/ML field. This suggests the letter's critique may resonate beyond mathematics.

**Tags**: `#AI ethics`, `#mathematics`, `#alignment`, `#academia`, `#AI impact`

---

<a id="item-6"></a>
## [Homebrew 7.0.0 ships official native macOS GUI](https://brew.sh/2026/09/13/homebrew-7.0.0/) ⭐️ 8.0/10

Homebrew released version 7.0.0, introducing an official native macOS graphical interface alongside faster installs and upgrades, stricter sandboxing, built-in vulnerability checks with a security advisory database, and a Linux sandbox switch from Bubblewrap to Landlock. The release also drops support for macOS 10.15 and earlier, and moves Intel Macs to Tier 3, meaning no new precompiled packages for those machines. Homebrew is one of the most widely used package managers on macOS and Linux, so these changes affect a large developer audience. The official GUI lowers the barrier for less command-line-savvy users, while the security and platform-support shifts signal a broader move toward tighter sandboxing and a narrower set of officially supported hardware. Intel Macs are now Tier 3, meaning they no longer receive new precompiled bottles and are not officially supported, while macOS 10.15 Catalina and older are unsupported. On Linux, the sandbox implementation moves from Bubblewrap to Landlock, a stackable Linux Security Module that lets unprivileged processes restrict their own filesystem access.

telegram · zaihuapd · Sep 13, 11:23

**Background**: Homebrew is a package manager that simplifies installing, updating, and removing software on macOS and Linux, traditionally through the command line. A package manager automates dependency resolution and binary distribution, and Homebrew's precompiled packages are called bottles. Sandboxing restricts what a program can access on the system to limit the damage from bugs or malicious code, and support tiers define which platforms Homebrew officially tests and builds for.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.brew.sh/Support-Tiers">Homebrew Documentation: Support Tiers</a></li>
<li><a href="https://landlock.io/">Landlock: Unprivileged Sandboxing — Landlock documentation</a></li>
<li><a href="https://github.com/containers/bubblewrap">GitHub - containers/bubblewrap: Low-level unprivileged ...</a></li>

</ul>
</details>

**Tags**: `#Homebrew`, `#package-manager`, `#macOS`, `#release`, `#security`

---