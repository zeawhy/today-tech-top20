---
layout: default
title: "Horizon Summary: 2026-07-11 (EN)"
date: 2026-07-11
lang: en
---

> From 39 items, 14 important content pieces were selected

---

1. [GPT-5.6 Sol Ultra Proves Cycle Double Cover Conjecture](#item-1) ⭐️ 9.0/10
2. [Humanoid Robot Performs World-First Live Pig Gallbladder Surgery](#item-2) ⭐️ 9.0/10
3. [SGLang v0.5.15 Boosts GLM-5.2 on Blackwell GPUs](#item-3) ⭐️ 8.0/10
4. [Einstein's relativity governs chemical bonds in heavy elements](#item-4) ⭐️ 8.0/10
5. [QuadRF Open-Source Tool Detects Drones and WiFi Through Walls](#item-5) ⭐️ 8.0/10
6. [Apple Sues OpenAI for Trade Secret Theft](#item-6) ⭐️ 8.0/10
7. [SpaceX plans 100,000 more Starlink satellites for 100x bandwidth](#item-7) ⭐️ 8.0/10
8. [Scarf moves from Haskell to Python after 7 years](#item-8) ⭐️ 8.0/10
9. [China Imposes Temporary Ban on Helium Exports](#item-9) ⭐️ 8.0/10
10. [EU May Fine Meta $12 Billion for Addictive Design](#item-10) ⭐️ 8.0/10
11. [SK Hynix ADR Surges 14% on Nasdaq Debut, Raises $26.5B](#item-11) ⭐️ 8.0/10
12. [SK Hynix CEO Warns of Worst Memory Shortage by 2027](#item-12) ⭐️ 8.0/10
13. [SpaceXAI and Cursor Launch Grok 4.5](#item-13) ⭐️ 8.0/10
14. [Six U-Boot Bootloader Flaws Allow Code Execution Before OS Boot](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GPT-5.6 Sol Ultra Proves Cycle Double Cover Conjecture](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf) ⭐️ 9.0/10

OpenAI's GPT-5.6 Sol Ultra has generated a proof of the Cycle Double Cover Conjecture, a long-standing open problem in graph theory, as announced in a preprint released on July 10, 2026. This marks the first time an AI has produced a proof of a major unsolved conjecture, demonstrating AI's growing capability in advanced mathematical reasoning and potentially accelerating discovery in theoretical fields. The proof is notably concise, suggesting a clever insight that experts had missed, and OpenAI released both the prompt and the full proof PDF for public scrutiny.

hackernews · scrlk · Jul 10, 18:29 · [Discussion](https://news.ycombinator.com/item?id=48863490)

**Background**: The Cycle Double Cover Conjecture asks whether every bridgeless undirected graph has a collection of cycles such that each edge appears exactly twice. It has been open since the 1970s and is a central problem in graph theory. GPT-5.6 Sol Ultra is OpenAI's most advanced model, released in July 2026, with state-of-the-art performance in coding, science, and reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cycle_double_cover_conjecture">Cycle double cover conjecture</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT‑5.6: Frontier intelligence that scales with your ambition</a></li>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT‑5.6 Sol: a next-generation model - OpenAI</a></li>

</ul>
</details>

**Discussion**: The community is impressed but notes that the proof is extremely concise, suggesting a clever trick rather than a deep theory-building proof. Some commenters highlight that the prompt required extensive hand-holding, indicating that AI still needs guidance for such tasks. Others are curious about the success rate of frontier models on unsolved problems.

**Tags**: `#AI`, `#mathematics`, `#graph theory`, `#OpenAI`, `#research`

---

<a id="item-2"></a>
## [Humanoid Robot Performs World-First Live Pig Gallbladder Surgery](https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/) ⭐️ 9.0/10

Surgeons remotely operated a Unitree G1 humanoid robot to perform the world's first laparoscopic cholecystectomy on live pigs, with results published in Nature. This is the first use of a general-purpose humanoid robot for live surgery, offering a low-cost alternative to specialized surgical robots like the da Vinci system, potentially expanding access to remote and resource-limited settings. The Unitree G1 robot costs $13,500 for the base model and about $67,000 with dexterous hands, far less than the $500,000+ for da Vinci systems. It stands 1.5 meters tall and weighs 27 kg, making it compact for various environments.

telegram · zaihuapd · Jul 11, 02:29

**Background**: Laparoscopic cholecystectomy is a minimally invasive surgery to remove the gallbladder, commonly performed for gallstones. Teleoperated robotic surgery allows surgeons to operate remotely with precision. The Unitree G1 is a general-purpose humanoid robot with 23-43 degrees of freedom, designed for AI research and dynamic tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.unitree.com/g1/">Humanoid robot G1_Humanoid Robot Functions_Humanoid Robot ... - unitree</a></li>
<li><a href="https://medicalxpress.com/news/2026-07-surgeons-teleoperated-humanoid-robots-surgery.html">Surgeons use teleoperated humanoid robots to perform live...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Laparoscopic_cholecystectomy">Laparoscopic cholecystectomy</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#surgery`, `#humanoid robot`, `#medical technology`, `#AI`

---

<a id="item-3"></a>
## [SGLang v0.5.15 Boosts GLM-5.2 on Blackwell GPUs](https://github.com/sgl-project/sglang/releases/tag/v0.5.15) ⭐️ 8.0/10

SGLang v0.5.15 introduces Spec V2 speculative decoding by default and IndexShare MTP optimization, delivering over 500 tokens/second/user on 8x B300 GPUs for GLM-5.2 NVFP4. The release also adds support for new models like Hunyuan 3 and Qwen3.6 NVFP4, and enables breakable CUDA Graph by default. These optimizations significantly reduce inference latency and cost for large language models, especially for long-context scenarios, making production serving more efficient. The improvements in speculative decoding and attention indexing set a new performance bar for open-source LLM serving engines. Spec V2 achieves zero-overhead scheduling via CUDA-graphable DSA draft-extend and fused metadata ops, yielding +11% end-to-end TPS. IndexShare MTP reuses the indexer top-k across draft steps, reducing draft-step cost by up to 1.9x at long context. TopK V2 fuses top-k selection with page-table transform, supporting runtime k up to 2048.

github · Fridge003 · Jul 10, 22:58

**Background**: SGLang is an open-source inference engine for large language models, known for its high performance and support for advanced features like speculative decoding. Blackwell GPUs (e.g., B300, GB300) are NVIDIA's latest architecture optimized for AI workloads. NVFP4 is a 4-bit floating-point quantization format that reduces memory usage while maintaining model quality.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.sglang.io/docs/advanced_features/speculative_decoding">Speculative Decoding - SGLang Documentation</a></li>
<li><a href="https://www.lmsys.org/blog/2026-06-15-next-generation-speculative-decoding-dflash-v2/">The next generation of speculative decoding: DFlash and Spec V2</a></li>
<li><a href="https://huggingface.co/nvidia/GLM-5.2-NVFP4">nvidia/GLM-5.2-NVFP4 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#GPU optimization`, `#speculative decoding`, `#SGLang`, `#Blackwell`

---

<a id="item-4"></a>
## [Einstein's relativity governs chemical bonds in heavy elements](https://www.brown.edu/news/2026-07-09/chemical-bonds-relativity) ⭐️ 8.0/10

New research published in Science demonstrates that relativistic effects, as described by Einstein's theory of relativity, fundamentally govern the chemical bonding in heavy elements such as bismuth. This finding deepens our understanding of heavy-element chemistry and could enable the design of safer materials, such as using non-toxic bismuth as a replacement for lead in solar cells and other applications. The study highlights spin-orbit coupling, where an electron's spin and orbit are no longer independent, as a key relativistic effect influencing sigma and pi bonds in heavy elements.

hackernews · hhs · Jul 10, 22:30 · [Discussion](https://news.ycombinator.com/item?id=48866134)

**Background**: Relativistic effects become significant for heavy elements because their inner electrons travel at speeds close to the speed of light, altering atomic and molecular properties. For example, gold's yellow color and mercury's liquid state at room temperature are both consequences of relativity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Relativistic_quantum_chemistry">Relativistic quantum chemistry - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted that relativistic effects on heavy elements are already known (e.g., gold's color, mercury's liquidity), but appreciated the new focus on chemical bonding. Some questioned the practical use of bismuth in solar cells, as lead is not commonly used in mass-produced panels.

**Tags**: `#physics`, `#chemistry`, `#relativity`, `#heavy elements`, `#materials science`

---

<a id="item-5"></a>
## [QuadRF Open-Source Tool Detects Drones and WiFi Through Walls](https://www.jeffgeerling.com/blog/2026/quadrf-can-spot-drones-and-see-wifi-through-my-wall/) ⭐️ 8.0/10

Jeff Geerling demonstrated QuadRF, an open-source RF visualization tool built on a Raspberry Pi 5 and FPGA, that can detect drones in flight and map WiFi signals through walls using phased-array beamforming. QuadRF democratizes advanced RF sensing technology, previously limited to government agencies, enabling hobbyists and security researchers to visualize wireless signals and detect hidden devices or drones. The system uses a phased-array antenna with picosecond-level timing for beamforming, and can route captured signals to SDR programs for decoding. It is fully open-source, allowing users to customize the UI and processing.

hackernews · speckx · Jul 10, 15:59 · [Discussion](https://news.ycombinator.com/item?id=48861717)

**Background**: Radio frequency (RF) signals can penetrate common building materials like drywall and concrete. Phased-array systems use multiple antennas to steer beams electronically, enabling direction finding and imaging. QuadRF combines a Raspberry Pi 5 with an FPGA for real-time signal processing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.hackster.io/news/quadrf-the-open-source-rf-camera-that-lets-you-see-wi-fi-signals-141ad91f2a2d">QuadRF: The Open Source RF Camera That Lets You See Wi-Fi Signals - Hackster.io</a></li>
<li><a href="https://scalerf.com/updates/">QuadRF Updates</a></li>
<li><a href="https://www.crowdsupply.com/scale-rf/quadrf">QuadRF | Crowd Supply</a></li>

</ul>
</details>

**Discussion**: QuadRF creator mrtnmcc engaged with the community, answering questions and noting UI improvements based on Jeff's feedback. Commenters discussed potential applications like sound localization and checking for hidden RF transmitters, while acknowledging that government agencies likely have similar capabilities.

**Tags**: `#RF`, `#open-source`, `#drone detection`, `#WiFi`, `#hardware`

---

<a id="item-6"></a>
## [Apple Sues OpenAI for Trade Secret Theft](https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/) ⭐️ 8.0/10

Apple filed a lawsuit against OpenAI, two former employees, and io Products in the U.S. District Court for the Northern District of California on July 10, 2026, alleging systematic theft of trade secrets related to hardware design, manufacturing processes, and supply chain information. This lawsuit could have major implications for the AI industry, potentially hindering OpenAI's hardware ambitions and setting a precedent for trade secret enforcement between tech giants. It also raises concerns about data security for businesses using OpenAI's models. Apple claims that former employee Chang Liu accessed internal networks and downloaded dozens of hardware files after leaving, and that OpenAI hardware head Tang Yew Tan instructed new hires to avoid scrutiny when leaving Apple. OpenAI allegedly used confidential Apple hardware information when approaching Apple suppliers.

hackernews · stock_toaster · Jul 10, 20:47 · [Discussion](https://news.ycombinator.com/item?id=48865019)

**Background**: Trade secret theft occurs when confidential business information is improperly acquired or used. Apple and OpenAI are both major players in AI and hardware, with Apple known for its tight security and OpenAI expanding into consumer hardware. The lawsuit echoes previous cases like Waymo vs. Uber, which had severe consequences for the accused.

**Discussion**: Community comments express strong condemnation of OpenAI, with users calling the evidence damning and suggesting this could be the end of OpenAI's hardware efforts. Some warn businesses against using OpenAI models due to IP theft risks, while others highlight the broader issue of generative AI companies built on copyright violation.

**Tags**: `#Apple`, `#OpenAI`, `#lawsuit`, `#trade secrets`, `#AI ethics`

---

<a id="item-7"></a>
## [SpaceX plans 100,000 more Starlink satellites for 100x bandwidth](https://www.zdnet.com/home-and-office/networking/spacex-wants-to-launch-100000-more-starlink-satellites/) ⭐️ 8.0/10

SpaceX has announced plans to launch up to 100,000 additional Starlink satellites, aiming to increase total network bandwidth by 100 times. This would expand the current constellation from roughly 6,000 satellites to over 100,000. If realized, this expansion could provide near-universal, high-speed internet access globally, including direct-to-cellphone service. However, it raises serious concerns about space debris, astronomical observations, and the monopolization of low Earth orbit by a single company. The plan is part of SpaceX's second-generation Starlink constellation, which requires regulatory approval from the FCC. The satellites would operate in very low Earth orbit (below 400 km) to reduce latency and improve deorbiting, but the sheer number increases collision risks.

hackernews · CrankyBear · Jul 10, 17:51 · [Discussion](https://news.ycombinator.com/item?id=48863064)

**Background**: Starlink is a low Earth orbit satellite constellation developed by SpaceX to provide high-speed, low-latency internet to remote and underserved areas. Currently, over 6,000 satellites are in orbit, serving about 160 countries. The proposed expansion to 100,000 satellites would dwarf existing megaconstellations and raise unprecedented orbital debris concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Starlink">Starlink - Wikipedia</a></li>
<li><a href="https://www.space.com/spacex-starlink-satellites.html">Starlink satellites : Facts, tracking and impact on astronomy | Space</a></li>
<li><a href="https://time.com/article/2026/04/16/space-debris-satellites-growing-risk/">The Looming Risk of Too Many Satellites and Debris in Space</a></li>

</ul>
</details>

**Discussion**: Community comments reflect mixed feelings: some users express sadness over the privatization of the night sky and environmental impact, while others highlight the practical benefits for remote areas and global cellphone coverage. Skepticism about SpaceX's ability to deliver on promises is also voiced, referencing past delays.

**Tags**: `#SpaceX`, `#Starlink`, `#satellite internet`, `#space debris`, `#broadband`

---

<a id="item-8"></a>
## [Scarf moves from Haskell to Python after 7 years](https://avi.press/posts/2026-07-10-after-7-years-in-production-scarf-has-reluctantly-moved-away-from-haskell.html) ⭐️ 8.0/10

Scarf, an open-source intelligence platform, has decided to migrate its production codebase from Haskell to Python after 7 years, citing slow compile times that hindered rapid iteration with LLM agents. This move highlights a growing tension between the safety of strong type systems and the speed required for AI-driven development, potentially influencing language choices for agentic workflows. The decision was driven by the need for fast compile times to support parallel LLM agent iterations; Haskell's cold compile times were deemed too slow for this use case.

hackernews · aviaviavi · Jul 10, 13:30 · [Discussion](https://news.ycombinator.com/item?id=48859673)

**Background**: Haskell is a statically typed functional programming language known for its strong type system and high reliability, but it has notoriously slow compile times. LLM agents often require rapid code generation and testing loops, making compile speed critical. Scarf provides analytics for open-source software usage, including tracking by AI agents.

<details><summary>References</summary>
<ul>
<li><a href="https://about.scarf.sh/">Open source intelligence for the agentic era | Scarf</a></li>
<li><a href="https://litellm.vercel.app/docs/a2a_iteration_budgets">Agent Iteration Budgets | liteLLM</a></li>
<li><a href="https://www.emergentmind.com/topics/large-language-model-llm-agent">LLM Agent : Iterative Reasoning & Action</a></li>

</ul>
</details>

**Discussion**: The community is divided: some argue that strong type systems are essential to constrain LLM outputs, while others find type systems less necessary with AI assistance. Some Haskell users report success with agentic development, suggesting compile times may not be universally prohibitive.

**Tags**: `#Haskell`, `#type systems`, `#LLM`, `#software engineering`, `#programming languages`

---

<a id="item-9"></a>
## [China Imposes Temporary Ban on Helium Exports](https://wms.mofcom.gov.cn/zcfb/wmgl/art/2026/art_2a795a0d55df4cada91c9fbd2a2cc13a.html) ⭐️ 8.0/10

On July 10, 2026, China's Ministry of Commerce and General Administration of Customs announced a temporary ban on helium exports (HS code 2804290010), effective immediately, citing the Foreign Trade Law. This ban could disrupt global helium supply chains, impacting semiconductor manufacturing, medical imaging (MRI), and scientific research, potentially driving up prices worldwide. The ban applies to helium with HS code 2804290010, effective from July 10, 2026, with no specified end date; future adjustments will be announced separately.

telegram · zaihuapd · Jul 10, 13:27

**Background**: Helium is a critical non-renewable resource used in cryogenics, pressurization, and as a shielding gas in welding. China is a significant producer, and export restrictions can tighten global supply, especially given rising demand from tech industries.

**Tags**: `#trade policy`, `#helium`, `#supply chain`, `#semiconductor`, `#critical materials`

---

<a id="item-10"></a>
## [EU May Fine Meta $12 Billion for Addictive Design](https://www.theverge.com/policy/963872/meta-eu-addictive-design-200b-fine-risk-digital-services-act-dsa) ⭐️ 8.0/10

The European Commission has preliminarily found that Meta's Facebook and Instagram violate the Digital Services Act through addictive design features like infinite scroll and autoplay, potentially leading to a fine of up to $12 billion. This marks one of the largest potential fines under the DSA and could force Meta to redesign its platforms, setting a precedent for how social media companies address addictive design globally. The EU criticizes Meta's existing time-limiting tools as ineffective and demands default disabling of addictive features, effective screen time breaks, and reduced engagement-driven algorithms. The fine would represent 6% of Meta's global annual revenue.

telegram · zaihuapd · Jul 10, 14:47

**Background**: The Digital Services Act (DSA) is an EU regulation that imposes strict obligations on very large online platforms to mitigate systemic risks, including risks to mental health. Addictive design patterns, such as infinite scroll and personalized recommendations, are designed to maximize user engagement but have been linked to negative psychological effects.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_Services_Act">Digital Services Act</a></li>

</ul>
</details>

**Tags**: `#Meta`, `#EU regulation`, `#Digital Services Act`, `#addictive design`, `#privacy`

---

<a id="item-11"></a>
## [SK Hynix ADR Surges 14% on Nasdaq Debut, Raises $26.5B](https://www.aljazeera.com/economy/2026/7/10/south-koreas-sk-hynix-raises-26-5bn-in-record-breaking-us-ipo) ⭐️ 8.0/10

SK Hynix's American Depositary Receipt (ADR) began trading on the Nasdaq on July 10, 2026, priced at $149 per share, raising approximately $26.5 billion. The ADR surged 14% on its first day, opening at around $170. This is the largest foreign IPO in U.S. history, surpassing Alibaba's $25 billion record in 2014, and underscores the surging demand for high-bandwidth memory (HBM) chips driven by AI. The strong debut signals investor confidence in the semiconductor sector's AI growth story. The offering was oversubscribed more than 7 times, reflecting intense investor interest. SK Hynix is the world's largest manufacturer of HBM chips, which are critical for AI graphics processors from Nvidia and AMD.

telegram · zaihuapd · Jul 10, 16:02

**Background**: An American Depositary Receipt (ADR) is a negotiable certificate issued by a U.S. bank representing a specified number of shares in a foreign company, allowing the company to trade on U.S. exchanges. High-bandwidth memory (HBM) is a 3D-stacked DRAM technology that provides ultra-wide bandwidth and low power consumption, essential for AI and high-performance computing workloads. SK Hynix's IPO proceeds will likely be used to expand HBM production capacity.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.zhiding.cn/2026/0709/3192818.shtml">高带宽内存：它是什么，为何至关重要--人工智能-至顶网</a></li>
<li><a href="https://www.hstong.com/sns/status/long/16347870644145372">躺平说投资 | 中概股与 美 国 存 托 凭 证 ADR | 华盛通</a></li>

</ul>
</details>

**Tags**: `#IPO`, `#semiconductors`, `#AI`, `#HBM`, `#SK Hynix`

---

<a id="item-12"></a>
## [SK Hynix CEO Warns of Worst Memory Shortage by 2027](https://www.reuters.com/world/asia-pacific/sk-hynix-ceo-sees-worst-ever-memory-supply-shortage-2027-says-demand-outstrip-2026-07-10/) ⭐️ 8.0/10

SK Hynix CEO Kwak Noh-Jung warned that the global memory industry will face its worst-ever supply shortage by 2027, with demand outstripping supply even after expansion, and the shortage may persist beyond 2030. This prediction signals a structural shift in the memory market driven by AI demand, which could disrupt supply chains for computers, cars, and consumer electronics for years. SK Hynix is considering overseas wafer fab locations in the US, Japan, and Southeast Asia, prioritizing land, electricity, and labor costs. The company reported a record operating profit of 47 trillion won ($31 billion) in 2025.

telegram · zaihuapd · Jul 11, 00:45

**Background**: Memory chips (DRAM and NAND Flash) are essential components in computers, smartphones, and AI servers. The industry has historically experienced boom-and-bust cycles, but the current AI-driven demand surge is creating a structural shortage that may last longer than typical cycles.

<details><summary>References</summary>
<ul>
<li><a href="https://www.studioglobal.ai/zh-cn/discover/answers/search-6a51ba2c19402d8e33c08142">SK海力士、英伟达、美光CEO集体发声：AI内存结构性短缺将成新常态 | ...</a></li>
<li><a href="https://www.163.com/dy/article/L1I1H0BL0519QIKK.html">告别周期性宿命！SK海力士CEO预警存储芯片短缺将延续至下一个十年，集...</a></li>
<li><a href="https://finance.sina.com.cn/roll/2026-07-11/doc-inihkyia6742015.shtml">SK海力士CEO预计存储芯片短缺将持续到下一个十年</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#memory`, `#supply chain`, `#SK Hynix`, `#industry forecast`

---

<a id="item-13"></a>
## [SpaceXAI and Cursor Launch Grok 4.5](https://t.me/zaihuapd/42484) ⭐️ 8.0/10

SpaceXAI and Cursor have jointly released Grok 4.5, their first model since SpaceX's $60 billion acquisition of Cursor, claiming top performance on the Harvey legal benchmark and double the token efficiency of leading models. This release signals a major push into specialized AI for high-stakes professional domains like coding, law, and finance, potentially reshaping competition among AI model providers. Grok 4.5 runs at 80 tokens per second and is priced at $2 per million input tokens, with a focus on coding, legal, and financial services tasks as well as enhanced cybersecurity capabilities.

telegram · zaihuapd · Jul 11, 01:44

**Background**: Cursor is an AI-powered code editor and development environment valued at $29.3 billion before its acquisition by SpaceX in June 2026. The Harvey Legal Agent Benchmark is an open-source benchmark for evaluating LLM agents on real legal work. Token efficiency refers to how many tokens a model uses to generate a response, affecting cost and speed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark">Introducing Harvey’s Legal Agent Benchmark</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(company)">Cursor (company)</a></li>
<li><a href="https://medium.com/@kailash.thiyagarajan/improving-llm-efficiency-a-deep-dive-into-tokenization-attention-and-key-value-caching-83d7239310be">Improving LLM Efficiency : A Deep Dive into Tokenization... | Medium</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Grok 4.5`, `#SpaceXAI`, `#Cursor`, `#LLM`

---

<a id="item-14"></a>
## [Six U-Boot Bootloader Flaws Allow Code Execution Before OS Boot](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

Binarly disclosed six vulnerabilities in U-Boot's FIT signature verification, including two critical remote code execution flaws and four denial-of-service flaws, affecting versions since 2013.07. These vulnerabilities allow attackers to execute malicious code before the operating system boots, bypassing firmware security and enabling stealthy persistent attacks. They affect numerous embedded devices and BMCs that support remote firmware updates. The two critical flaws (BRLY-2026-037 and BRLY-2026-038) enable arbitrary code execution, while the other four cause denial of service. Patches have been accepted by U-Boot maintainers but require downstream vendors to integrate and distribute.

telegram · zaihuapd · Jul 11, 08:32

**Background**: U-Boot is a widely used open-source bootloader for embedded devices, responsible for loading the operating system. FIT (Flattened Image Tree) is a format for packaging kernel, device tree, and other binaries, with signature verification to ensure authenticity. The vulnerabilities reside in the signature verification code, allowing attackers to bypass checks and execute arbitrary code during boot.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/u-boot-fit-signature-verification/">Six U - Boot FIT Signature Verification Flaws Enable Code Execution...</a></li>
<li><a href="https://docs.u-boot-project.org/en/latest/usage/fit/signature.html">U - Boot FIT Signature Verification — Das U - Boot unknown version...</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#bootloader`, `#firmware`, `#U-Boot`

---