---
layout: default
title: "Horizon Summary: 2026-07-21 (ZH)"
date: 2026-07-21
lang: zh
---

> 从 76 条内容中筛选出 16 条重要资讯。

---

1. [苹果赢得 CSAM 扫描诉讼，法官批评隐私权衡](#item-1) ⭐️ 8.0/10
2. [Jane Street 的高效增量计算库 Incremental](#item-2) ⭐️ 8.0/10
3. [Claude Code 团队炉边谈话：65% PR 通过 Claude Tag 完成](#item-3) ⭐️ 8.0/10
4. [AI 编码代理让逆向工程变得廉价](#item-4) ⭐️ 8.0/10
5. [Ben Thompson 提议美国立法将 AI 数据收集合法化](#item-5) ⭐️ 8.0/10
6. [Sam Altman 2022 年邮件披露开源策略](#item-6) ⭐️ 8.0/10
7. [数据中心用电量预计 2035 年翻四倍](#item-7) ⭐️ 8.0/10
8. [美国威胁因知识产权盗窃制裁中国 AI 模型](#item-8) ⭐️ 8.0/10
9. [Deezer：每日上传音乐超 50%为 AI 生成](#item-9) ⭐️ 8.0/10
10. [Anthropic 15 亿美元版权和解获批](#item-10) ⭐️ 8.0/10
11. [欧盟拟共享生物识别数据换取美国免签](#item-11) ⭐️ 8.0/10
12. [智谱建成全国产芯片大型数据中心](#item-12) ⭐️ 8.0/10
13. [谷歌开发 Gemini 专用 AI 芯片 Frozen v2](#item-13) ⭐️ 8.0/10
14. [Cloudflare 内部 DNS 服务正式上线](#item-14) ⭐️ 8.0/10
15. [台积电或于 2026 年将高端制程涨价 5%-10%](#item-15) ⭐️ 8.0/10
16. [谷歌发布 Gemini 3.5 Flash，Pro 版下月推出](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [苹果赢得 CSAM 扫描诉讼，法官批评隐私权衡](https://blog.ericgoldman.org/archives/2026/07/apple-defeats-liability-for-not-scanning-icloud-for-csam-but-the-judge-was-not-pleased-amy-v-apple.htm) ⭐️ 8.0/10

美国法院裁定苹果无需为未扫描 iCloud 中的儿童性虐待材料（CSAM）承担责任，驳回了针对该公司的诉讼。法官对结果表示不满，称隐私保护使受害儿童成为附带损害。 该裁决确立了法律先例，即科技公司可能无需扫描加密云服务中的非法内容，强化了隐私与儿童安全之间的紧张关系。它可能影响未来关于加密和内容审核的立法及企业政策。 苹果此前曾提议在设备端进行 CSAM 扫描，但因隐私争议而放弃。法院指出，端到端加密本质上阻止了服务器端扫描，而苹果当前的 iCloud 加密默认并非完全端到端。

hackernews · speckx · 7月21日 14:31 · [社区讨论](https://news.ycombinator.com/item?id=48992870)

**背景**: 儿童性虐待材料（CSAM）指描绘儿童性虐待的非法图片和视频。科技公司面临检测和报告 CSAM 的压力，但端到端加密阻止服务提供商访问内容。苹果的 iCloud 使用加密，但需要高级数据保护（ADP）才能实现完全端到端加密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5mac.com/guides/csam/">CSAM : Apple's efforts to detect Child Sexual Abuse Materials - 9to5Mac</a></li>
<li><a href="https://www.lawfaremedia.org/article/apple-client-side-scanning-system">The Apple Client-Side Scanning System | Lawfare</a></li>

</ul>
</details>

**社区讨论**: 评论者大多支持该裁决，认为这是隐私的胜利，一些人认为当公司同时控制应用和服务器时，真正的端到端加密是不可能的。其他人则指出这一悲剧性的权衡，承认隐私保护可能阻碍 CSAM 检测。

**标签**: `#privacy`, `#encryption`, `#Apple`, `#CSAM`, `#legal`

---

<a id="item-2"></a>
## [Jane Street 的高效增量计算库 Incremental](https://github.com/janestreet/incremental) ⭐️ 8.0/10

Jane Street 发布了 Incremental，这是一个 OCaml 库，能够通过自动仅重新计算输入变化时计算图中受影响的部分，实现高效的增量计算。 该库将增量计算的能力引入 OCaml，使开发者能够构建响应式应用和系统（如构建工具或金融模型），避免完全重新计算，从而节省时间和资源。 Incremental 类似于 JavaScript 框架（如 Vue、SolidJS）中的响应式编程信号，但专为 OCaml 的函数式编程范式设计。它使用有向无环图（DAG）来建模依赖关系并高效传播变化。

hackernews · handfuloflight · 7月21日 03:50 · [社区讨论](https://news.ycombinator.com/item?id=48987822)

**背景**: 增量计算是一种在输入变化时重用先前结果来计算新输出的技术，避免重复工作。这一概念广泛应用于构建系统（如 Make、Bazel）和响应式编程。Jane Street 的 Incremental 库实现了 Umut Acar 提出的自调整计算概念，并经过多年实际使用中的七次实现迭代演化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/janestreet/incremental">GitHub - janestreet/incremental: A library for incremental computations</a></li>
<li><a href="https://www.janestreet.com/tech-talks/seven-implementations-of-incremental/">Seven Implementations of Incremental - Jane Street</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 Incremental 与 JavaScript 信号的相似性，有人提到它在 Vue 和 SolidJS 等框架中的应用。另一位评论者回忆高盛几十年前在金融工具定价中使用了类似方法，凸显了增量计算在金融领域的悠久历史。

**标签**: `#incremental computation`, `#reactive programming`, `#Jane Street`, `#OCaml`, `#build systems`

---

<a id="item-3"></a>
## [Claude Code 团队炉边谈话：65% PR 通过 Claude Tag 完成](https://simonwillison.net/2026/Jul/21/cat-and-thariq/#atom-everything) ⭐️ 8.0/10

Simon Willison 与 Anthropic 的 Claude Code 团队进行了一场炉边谈话，透露 Claude Tag 现在处理了该团队 65%的产品工程拉取请求，并且针对 Fable 5 等新模型，Claude Code 的系统提示词已缩减 80%。 这些指标展示了 Anthropic 内部对 AI 编码代理的信任度日益成熟，为更广泛的 AI 工程社区提供了生产力提升和最佳实践演变的具体证据。 该团队先向员工发布功能，仅保留能证明用户留存的功能；关键变更仍需人工审查，但外层代码已采用自动化审查。对于最新模型，不再建议在系统提示词中添加示例。

rss · Simon Willison · 7月21日 12:54

**背景**: Claude Code 是 Anthropic 的 AI 编码代理，于 2025 年初与 Claude 3.7 Sonnet 一同发布。Claude Tag 是一个 Slack 集成，允许用户在频道中@提及 Claude 以进行协作编码。AI Engineer World's Fair 是一个专注于 AI 工程实践的会议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI)</a></li>
<li><a href="https://claude.com/product/tag">Claude in Slack: Tag @ Claude in any thread | Claude by Anthropic</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude Code`, `#Anthropic`, `#coding agents`, `#AI engineering`

---

<a id="item-4"></a>
## [AI 编码代理让逆向工程变得廉价](https://simonwillison.net/2026/Jul/20/cheap-reverse-engineering/#atom-everything) ⭐️ 8.0/10

AI 编码代理大幅降低了逆向工程家用设备未文档化 API 所需的成本和精力，使得自动化项目即使对爱好者也变得可行。 这一转变改变了家庭自动化的投资回报率计算，降低了入门门槛，减轻了未来维护的心理负担，可能加速定制智能家居解决方案的普及。 文章指出，在代理出现之前，逆向工程和维护未文档化 API 的努力往往超过收益；现在，尝试和失败的低成本使得实验无风险。

rss · Simon Willison · 7月20日 19:24

**背景**: 逆向工程涉及分析设备的网络流量或固件以理解其协议，通常用于在没有官方支持的情况下控制设备。未文档化的 API 在消费级智能家居设备中很常见，这些 API 可能随时更改，需要持续维护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.agentre-bench.ai/">AgentRE-Bench — LLM Reverse Engineering Benchmark</a></li>
<li><a href="https://www.linkedin.com/pulse/i-used-ai-coding-agent-my-phone-reverse-engineer-smart-daniel-potts-ovd4c">I Used an AI Coding Agent on My Phone to Reverse - Engineer ...</a></li>
<li><a href="https://stevessmarthomeguide.com/smart-home-apis/">Understanding Smart Home APIs</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#reverse engineering`, `#software engineering`, `#home automation`, `#cost of code`

---

<a id="item-5"></a>
## [Ben Thompson 提议美国立法将 AI 数据收集合法化](https://simonwillison.net/2026/Jul/20/afraid-of-chinese-models/#atom-everything) ⭐️ 8.0/10

Ben Thompson 提议美国应通过一项法律，明确将 AI 训练的数据收集视为合理使用，并禁止禁止蒸馏的服务条款，以帮助美国开放模型与中国模型竞争。他还指出，阿里巴巴以开放权重形式发布了 Qwen 3.8 Max，可能受到习近平最近鼓励开源的讲话影响。 该提案解决了 AI 领域的一个关键矛盾：使用未经授权数据训练的实验室往往禁止他人蒸馏其模型。如果实施，它可能为美国开放模型与中国模型创造公平竞争环境，并重塑 AI 训练的版权政策。 蒸馏是指通过查询较大模型的 API 来训练较小模型的过程，技术上几乎无法阻止。Qwen 3.8 Max 是一个 2.4 万亿参数的模型，几乎与 Kimi K3 的 2.8 万亿参数相当。

rss · Simon Willison · 7月20日 17:09

**背景**: 知识蒸馏是一种机器学习技术，较小的“学生”模型从较大的“教师”模型的输出中学习。开放权重模型允许用户下载并在本地运行模型，但不包含完整的训练代码或数据。美国版权局最近就 AI 训练是否构成合理使用发表了意见，一些法院会考虑公共利益。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told – Open Source Initiative</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_intelligence_and_copyright">Artificial intelligence and copyright - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#open models`, `#distillation`, `#copyright`, `#Chinese AI`

---

<a id="item-6"></a>
## [Sam Altman 2022 年邮件披露开源策略](https://simonwillison.net/2026/Jul/20/sam-altman/#atom-everything) ⭐️ 8.0/10

在 Musk v. Altman 诉讼中曝光的一封 Sam Altman 于 2022 年发给 OpenAI 董事会的邮件显示，OpenAI 计划发布一个可在消费级硬件上运行的、能力接近 GPT-3 的开源模型，以抢先于 Stability AI 等竞争对手，并阻止新进入者。 这封邮件罕见地揭示了 OpenAI 内部关于开源模型的战略思考，凸显了竞争压力如何影响那些关乎 AI 可及性、伦理和市场格局的决策。 该邮件日期为 2022 年 10 月 1 日，是 2026 年 Musk v. Altman 法律案件的一部分。Altman 特别提到要在“Stability 或其他公司”之前发布模型，这里指的是 Stability AI 的 StableLM 系列。

rss · Simon Willison · 7月20日 03:47

**背景**: GPT-3 是 OpenAI 于 2020 年发布的大型语言模型，以生成类人文本的能力著称。在邮件撰写时，GPT-Neo 和 OPT 等开源替代品正在出现，但均未达到 GPT-3 的能力水平。在消费级硬件上运行此类模型是一项重大的技术挑战，需要优化和量化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-3">GPT-3 - Wikipedia</a></li>
<li><a href="https://github.com/Stability-AI/StableLM">Stability - AI /StableLM: StableLM: Stability AI Language Models ...</a></li>
<li><a href="https://www.local-llm.net/learn/what-is-local-ai/">What Is Local AI? The Complete Guide to Running AI... | local - llm .net</a></li>

</ul>
</details>

**标签**: `#open-source`, `#ai-ethics`, `#openai`, `#sam-altman`, `#generative-ai`

---

<a id="item-7"></a>
## [数据中心用电量预计 2035 年翻四倍](https://techcrunch.com/2026/07/21/data-centers-expected-to-use-4x-more-electricity-by-2035/) ⭐️ 8.0/10

一项新预测显示，到 2033 年新建的数据中心可能消耗相当于印度当前总用电量的电力，到 2035 年其电力需求将翻四倍。 能源消耗的激增对能源基础设施、AI 可扩展性和全球可持续发展努力构成重大挑战，可能使电网承压并增加碳排放。 该预测涵盖到 2033 年新建的数据中心，与印度用电量的比较凸显了预期增长的巨大规模。

rss · TechCrunch AI · 7月21日 18:06

**背景**: 数据中心是容纳计算机系统及相关组件（如电信和存储）的设施。它们对云计算、AI 训练和数字服务至关重要，但能源消耗极高。

**标签**: `#data centers`, `#energy consumption`, `#AI infrastructure`, `#sustainability`

---

<a id="item-8"></a>
## [美国威胁因知识产权盗窃制裁中国 AI 模型](https://techcrunch.com/2026/07/21/us-threatens-sanctions-against-chinese-ai-models-over-ip-theft/) ⭐️ 8.0/10

美国财政部长斯科特·贝森特表示，如果发现中国开源 AI 模型建立在对美国公司的知识产权盗窃之上，特朗普政府可能对其进行制裁。 这加剧了美中科技紧张局势，并可能通过限制中国开源模型的分布来重塑全球 AI 格局，影响世界各地的开发者和企业。 贝森特特别提到了“蒸馏”做法——即一个模型基于另一个模型的输出进行训练——作为潜在的知识产权盗窃形式。据报道，政府正在考虑将中国 AI 实验室列入制裁名单，并让美国公司对安全漏洞承担责任。

rss · TechCrunch AI · 7月21日 15:37

**背景**: 开源 AI 模型因其透明性和较低成本而变得流行，但在训练数据方面仍可能是黑箱。美国此前已对向中国出口先进 AI 芯片实施管制，此次制裁威胁代表了技术竞争的新战线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.businessinsider.com/treasury-secretary-chinese-ai-open-source-sanctions-kimi-k3-2026-7">Treasury Secretary says its 'unacceptable' that Chinese open source AI models may have been built on 'IP theft'</a></li>
<li><a href="https://www.cnbc.com/2026/07/21/bessent-china-ai-sanctions.html">Bessent says U.S. could sanction China over AI model 'theft'</a></li>
<li><a href="https://the-decoder.com/trump-administration-reportedly-builds-a-slow-motion-ban-on-chinese-ai-models-through-sanctions-and-soft-pressure/">Trump administration reportedly builds a slow-motion ban on Chinese AI models through sanctions and soft pressure</a></li>

</ul>
</details>

**标签**: `#AI`, `#geopolitics`, `#sanctions`, `#open source`, `#policy`

---

<a id="item-9"></a>
## [Deezer：每日上传音乐超 50%为 AI 生成](https://techcrunch.com/2026/07/21/music-streamer-deezer-says-more-than-50-of-daily-uploads-are-ai-generated/) ⭐️ 8.0/10

Deezer 报告称，6 月份每天有超过 9 万首 AI 生成的曲目上传到其平台，占每日上传总量的 50%以上。 这一数据量化了主流流媒体平台上 AI 生成内容的巨大规模，凸显了音乐行业在版权、内容策展和审核方面面临的紧迫挑战。 Deezer 开发了一款 AI 音乐检测器，2025 年已识别超过 1340 万首 AI 曲目，并向用户免费提供该检测工具，支持多个平台。

rss · TechCrunch AI · 7月21日 13:27

**背景**: 像 SOUNDRAW、AIVA 和 Canva 的 AI 音乐生成器这样的生成式 AI 工具，让任何人都能在几秒钟内创建免版税音乐。随着这些工具的普及，流媒体平台面临着区分人类创作和 AI 生成内容的挑战。Deezer 激进的检测方法与 Spotify 和 Apple Music 等竞争对手形成对比，后者仅对 AI 内容添加标签。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deezer.com/explore/ai-music-detector/">Free AI Music Detector by Deezer | AI Song checker</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pQdmZhc0VSRVJiN05uZlRXbXhpZ0FQAQ?hl=en-NA&gl=NA&ceid=NA:en">Google News - Deezer 's AI music detector - Overview</a></li>

</ul>
</details>

**标签**: `#AI-generated content`, `#music streaming`, `#generative AI`, `#content moderation`, `#industry impact`

---

<a id="item-10"></a>
## [Anthropic 15 亿美元版权和解获批](https://techcrunch.com/2026/07/20/anthropics-landmark-1-5b-copyright-settlement-is-approved/) ⭐️ 8.0/10

美国法院最终批准了 Anthropic 与作者之间 15 亿美元的版权和解协议，这些作者声称该公司未经许可使用其作品训练 AI 模型。 这一里程碑式的和解是 AI 时代同类案件中金额最高的，表明 AI 公司可能因使用受版权保护的训练数据而面临重大财务责任，但合理使用的核心法律问题仍未解决。 该和解为每类作品提供了赔偿，但并未就使用受版权保护的材料进行 AI 训练是否构成合理使用确立法律先例，使得更广泛的法律环境仍不确定。

rss · TechCrunch AI · 7月21日 00:12

**背景**: Anthropic 是一家 AI 安全公司，面临作者提起的集体诉讼，指控其 AI 模型使用了盗版的书籍和文章进行训练。该案是针对 AI 公司（包括 OpenAI 和 Meta）使用受版权保护数据训练大语言模型的一系列版权诉讼之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/story/anthropic-settlement-lawsuit-copyright/">Anthropic Agrees to Pay Authors at Least $1.5 Billion in AI Copyright ...</a></li>
<li><a href="https://www.linkedin.com/pulse/anthropic-settlement-ai-training-data-what-means-businesses-using-hvvme">The Anthropic Settlement & AI Training Data: What It Means for...</a></li>

</ul>
</details>

**标签**: `#AI`, `#copyright`, `#legal`, `#Anthropic`, `#settlement`

---

<a id="item-11"></a>
## [欧盟拟共享生物识别数据换取美国免签](https://edri.org/our-work/the-eu-is-about-to-sell-our-most-sensitive-data-to-the-us-for-visa-free-travel/) ⭐️ 8.0/10

欧盟委员会正与美国谈判一项“增强边境安全伙伴关系”（EBSP）框架协议，该协议要求欧盟成员国向美国当局共享生物识别数据，以换取美国公民的免签待遇。 该协议可能为大国之间的大规模监控和数据共享开创先例，可能削弱欧盟的隐私保护，并使敏感的生物识别数据面临被滥用的风险。 泄露的草案显示，欧盟几乎全盘接受了美方对生物识别数据库无限制访问的要求，包括共享基于政治观点的“风险指标”，这可能威胁言论自由。

telegram · zaihuapd · 7月20日 15:08

**背景**: 生物识别数据包括指纹和面部识别模式等独特的身体特征，一旦泄露无法更改。EBSP 框架将是首个大规模向美国边境当局共享欧盟公民生物识别数据的协议，引发了对隐私和数据安全的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://leantrustgovernance.substack.com/p/the-eu-us-biometric-data-deal-trading">How the EU – US Border Deal Rewrites Privacy</a></li>
<li><a href="https://cdt.org/insights/responding-to-the-eu-us-negotiations-on-reciprocal-data-exchanges-for-border-procedures/">Responding to the EU - US Negotiations on Reciprocal Data Exchanges...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#biometric data`, `#EU-US agreement`, `#data protection`, `#civil liberties`

---

<a id="item-12"></a>
## [智谱建成全国产芯片大型数据中心](https://www.bloomberg.com/news/articles/2026-07-20/z-ai-completes-giant-data-center-with-chinese-chips-to-train-ai) ⭐️ 8.0/10

智谱 AI 已完成一座全部采用国产芯片的大型数据中心建设，功率达 1 吉瓦，并已开始部分运营，以支持其 GLM 平台的开发。 这一里程碑展示了中国在减少对外国芯片依赖、实现 AI 自给自足方面的进展，该设施是中国 AI 实验室建造的最大规模设施之一，有望提升国内 AI 模型训练能力。 该数据中心 1 吉瓦的功率足以供应约 75 万户家庭。智谱 AI 运营着多个各拥有超万枚芯片的计算集群，这一新设施是中国同类设施中规模最大的之一。

telegram · zaihuapd · 7月20日 15:43

**背景**: 智谱 AI 是清华大学知识工程研究室（KEG Lab）孵化的 AI 公司，以其开源的 GLM（通用语言模型）系列闻名。GLM-5 旗舰版在 SWE-Bench 上得分 77.8%，是工具调用能力最强的开源模型。中国国产芯片发展正在加速，摩根士丹利预测到 2030 年中国 AI 芯片市场规模将达到 670 亿美元，国产芯片有望满足约 76%的市场需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.it007.com/article-331776-1.html">产 业_消息称智谱建成大型 AI 数 据 中 心 ： 全 部采用 国 产 芯 片 _ IT007...</a></li>
<li><a href="https://vpn07.com/tw/blog/2026-glm4-quanpingtai-anzhuang-jiaoxue-bendi-bushu.html">智 谱 GLM 全 平 台 安裝教學：清華系開源 AI 本地部署 2026</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#domestic chips`, `#China`, `#data center`, `#GLM`

---

<a id="item-13"></a>
## [谷歌开发 Gemini 专用 AI 芯片 Frozen v2](https://www.quiverquant.com/news/Google+Reportedly+Developing+%E2%80%98Frozen+v2%E2%80%99+AI+Chip+to+Boost+Gemini+Efficiency) ⭐️ 8.0/10

据报道，谷歌正在开发一款代号为 'Frozen v2' 的新型 AI 服务器芯片，将 Gemini 模型的部分能力直接写入硬件，目标是每瓦特功耗产生的 token 数达到最新 TPU 的 6 到 10 倍，计划于 2028 年部署。 该芯片可大幅提升推理效率，解决 AI 部署中的关键瓶颈，并可能削弱 GPU 在 AI 计算中的优势。这也凸显了为特定模型设计定制硬件的趋势，可能重塑 AI 硬件格局。 Frozen v2 被定位为谷歌 TPU 的补充而非替代产品，旨在缓解内部算力短缺，这种短缺已限制了 Google Cloud 为部分企业客户提供服务的能力。该芯片预计在 2028 年部署。

telegram · zaihuapd · 7月21日 01:01

**背景**: Tokens-per-watt 是衡量 AI 推理效率的关键指标，表示系统每瓦特功耗产生的输出 token 数。谷歌的 TPU 已经是专门的 AI 加速器，但 Frozen v2 更进一步，将模型特定的逻辑嵌入芯片中，可能为 Gemini 工作负载带来显著的效率提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qz.com/google-gemini-chip-frozen-tpu-efficiency-072026">Google developing Gemini-specific chip called Frozen v 2</a></li>
<li><a href="https://logicity.in/en/blog/google-s-frozen-v2-chip-embeds-gemini-in-hardware-for-6-10x-gains">Google 's Frozen v 2 chip embeds Gemini in hardware for... | Logicity</a></li>
<li><a href="https://cowlpane.com/ai/my-ai-diary-google-s-frozen-v2-chip-shakes-the-gpu-moat/">Google Frozen v 2 Chip vs GPU Moat — Cowlpane</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#Google`, `#Gemini`, `#TPU`, `#inference efficiency`

---

<a id="item-14"></a>
## [Cloudflare 内部 DNS 服务正式上线](https://blog.cloudflare.com/internal-dns/) ⭐️ 8.0/10

Cloudflare 于 2026 年 7 月 20 日宣布内部 DNS 服务正式全面上线，为企业私有网络提供权威与递归 DNS 解析，并与 Zero Trust 及全球网络集成。 该服务将公共与私有 DNS 整合至单一平台，简化了分割 DNS 管理，并将 Zero Trust 策略延伸至域名解析层，降低了企业的复杂性。 已使用 Cloudflare Gateway 的企业客户无需额外付费即可启用该服务。它支持通过 API、Terraform 及 Cloudflare WAN 部署，管理员可设定解析器策略，控制不同用户和设备可访问的内部视图。

telegram · zaihuapd · 7月21日 03:49

**背景**: 分割 DNS（split-horizon DNS）根据请求来源提供不同的 DNS 响应，通常为内部用户返回内网 IP，为外部用户返回公网 IP。传统上管理分割 DNS 需要维护独立的 DNS 服务器或视图，容易导致数据漂移和配置复杂。Cloudflare 的内部 DNS 将此功能与其 Zero Trust 及网络服务集成，提供统一控制平面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Split-horizon_DNS">Split-horizon DNS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero_trust_design">Zero trust design</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#DNS`, `#Zero Trust`, `#networking`, `#enterprise`

---

<a id="item-15"></a>
## [台积电或于 2026 年将高端制程涨价 5%-10%](https://t.me/zaihuapd/42691) ⭐️ 8.0/10

台积电正考虑在 2026 年将其所有高端工艺制程（5nm/4nm、3nm 和 2nm）提价 5%-10%，以抵消美国关税、汇率波动和供应链成本压力。该公司已向代工合作伙伴传达了更高的 2026 年报价。 此次涨价直接影响英伟达和苹果等主要客户，可能推高芯片成本，影响整个半导体生态系统。这标志着行业面临普遍的成本压力，并可能导致消费电子产品和 AI 硬件价格上涨。 涨价适用于所有高端制程，包括 5nm/4nm、3nm 和 2nm。台积电董事长魏哲家幽默地拒绝确认该计划，称“心里想的事情，嘴巴不能讲”。

telegram · zaihuapd · 7月21日 09:28

**背景**: 台积电是全球最大的专业半导体代工厂，为苹果、英伟达和 AMD 等公司制造芯片。高端制程（5nm 及以下）对高性能计算和移动设备至关重要。美国一直在考虑对进口半导体征收关税，而汇率波动（如美元/新台币）也影响台积电的收入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.elecfans.com/d/1528945.html">台 积 电 在 5 nm 及未来的 3 nm 工 艺 上依然是老大- 电 子发烧友网</a></li>
<li><a href="https://m.laoyaoba.com/n/954522">【头条】 232 半 导 体 关 税 对 国 内企 业 影 响 有限</a></li>

</ul>
</details>

**标签**: `#TSMC`, `#semiconductor`, `#pricing`, `#chip manufacturing`, `#supply chain`

---

<a id="item-16"></a>
## [谷歌发布 Gemini 3.5 Flash，Pro 版下月推出](https://t.me/zaihuapd/42699) ⭐️ 8.0/10

谷歌正式发布了 Gemini 3.5 Flash 模型，现已全球上线，并宣布性能更强的 Gemini 3.5 Pro 将于下个月推出。 此次发布标志着谷歌 AI 战略的重要一步，以 Flash 级别的成本和速度提供接近 Pro 级别的推理和编程能力，可能加速智能体 AI 在企业及开发者工作流中的采用。 Gemini 3.5 Flash 的输出速度比同类模型快 4 倍，成本大幅降低，拥有 100 万 token 的上下文窗口，支持文本、图像、视频、音频和 PDF 输入。

telegram · zaihuapd · 7月21日 15:23

**背景**: Gemini 是谷歌的多模态大语言模型系列。Flash 系列专为高效率和低延迟设计，而 Pro 系列则面向复杂推理和编程任务。智能体 AI 指能够自主执行多步骤工作流以实现目标的 AI 系统，超越了简单的文本生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3 . 5 Flash — Google DeepMind</a></li>
<li><a href="https://openrouter.ai/google/gemini-3.5-flash">Gemini 3 . 5 Flash - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/">Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber</a></li>

</ul>
</details>

**标签**: `#AI`, `#Google`, `#Gemini`, `#LLM`, `#Machine Learning`

---