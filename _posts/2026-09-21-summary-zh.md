---
layout: default
title: "Horizon Summary: 2026-09-21 (ZH)"
date: 2026-09-21
lang: zh
---

> 从 85 条内容中筛选出 5 条重要资讯。

---

1. [陶哲轩发问：AI 时代还需要人类数学家吗？](#item-1) ⭐️ 9.0/10
2. [Qwen Image 2.1：7B 开源权重文生图模型，原生支持透明通道](#item-2) ⭐️ 8.0/10
3. [斯诺登档案的最终去向：一次回顾性分析](#item-3) ⭐️ 8.0/10
4. [LLMentalist 效应：大语言模型的智能只是冷读术吗？](#item-4) ⭐️ 8.0/10
5. [月之暗面与微软、亚马逊、谷歌洽谈 Kimi K3 收入分成](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [陶哲轩发问：AI 时代还需要人类数学家吗？](https://terrytao.wordpress.com/2026/09/19/why-do-we-need-human-mathematicians-anymore/) ⭐️ 9.0/10

菲尔兹奖得主、加州大学洛杉矶分校数学教授陶哲轩（Terence Tao）发表了一篇题为《为什么我们还需要人类数学家？》的博客文章，探讨在 AI 系统于定理证明和数学发现方面能力日益增强的背景下，人类数学家是否仍然不可或缺。该文章迅速成为讨论焦点，在 Hacker News 上获得 216 分和 203 条评论。 这一问题直击数学界乃至更广泛知识工作领域的核心：当 AI 自动化越来越多的认知任务时，人类应如何适应。陶哲轩的权威地位意味着他对这一问题的论述很可能会影响数学家、资助机构和 AI 研究者对人类与机器分工的思考方式。 这篇文章是一篇哲学性反思，而非技术成果；它引发的讨论涵盖直觉与形式化符号的对比、数学机构的可及性，以及数学是否存在有限待解问题等话题。陶哲轩还曾在 2026 年国际数学家大会上单独讨论过 AI 与做数学的意义。

hackernews · auggierose · 9月20日 10:49 · [社区讨论](https://news.ycombinator.com/item?id=49774521)

**背景**: 陶哲轩是当今世界最著名的数学家之一，研究领域横跨分析、数论和组合数学，并且一直积极评论 AI 在数学中日益增长的作用。自动定理证明是一个由来已久的子领域，旨在让计算机程序证明数学命题；近年来的 AI 系统已开始产出新颖成果，其中包括代数几何中的一个定理，美国数学学会会长称其“严谨、正确且优雅”。这些进展引发了关于证明过剩、验证以及人类理解在正确输出之外还有何价值的争论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Terence_Tao">Terence Tao - Wikipedia</a></li>
<li><a href="https://www.simonsfoundation.org/2026/08/13/fields-medalist-terence-tao-on-artificial-intelligence-and-why-we-do-math/">Watch: Fields Medalist Terence Tao on Artificial Intelligence and Why ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认同人类理解仍然不可或缺，有人引用博尔赫斯的《巴别图书馆》指出，生成的知识只有在人类能够验证和理解时才算数。也有人主张数学应转向直觉与可及性，而非用符号体系设置门槛；还有人指出解决问题总会带来新问题，因此数学绝非 AI 能够简单完成的有限任务。

**标签**: `#mathematics`, `#AI`, `#philosophy`, `#future of work`, `#Terry Tao`

---

<a id="item-2"></a>
## [Qwen Image 2.1：7B 开源权重文生图模型，原生支持透明通道](https://qwen.ai/blog?id=qwen-image-2.1) ⭐️ 8.0/10

Qwen 发布了 Qwen Image 2.1，这是一个 7B 的开源权重文生图与图像编辑模型，相比前代 Qwen-Image 1 的 20B 参数大幅缩小。它引入了原生透明通道（RGBA 输出）和业界领先的文本渲染能力，并在发布首日就获得了 ComfyUI 的原生支持。 该模型更小的体积让高质量本地图像生成更加普及，而其原生透明通道和出色的文本渲染能力填补了大多数开源权重竞品尚未解决的空白。不过，相比此前采用 Apache 许可的 Qwen 模型，其更严格的许可证可能会限制商业应用。 生成 Transformer 采用 7B 参数、32 层单流 DiT 架构，可原生生成透明 RGBA 图像，这一能力在开源权重模型中似乎只有 Qwen 团队在着力解决。模型已在 Hugging Face 和 GitHub 上发布，并提供了用于文生图和图像编辑的 ComfyUI 工作流。

hackernews · jmillikin · 9月20日 13:09 · [社区讨论](https://news.ycombinator.com/item?id=49775499)

**背景**: 文生图模型根据文本提示生成图像，而开源权重模型允许用户在本地运行并检查或修改其权重。Qwen 是阿里巴巴的 AI 模型系列，此前的 Qwen 图像模型采用宽松的 Apache 2.0 许可证。原生透明意味着模型直接输出带 alpha 通道的图像，无需额外的背景去除工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen-Image-2.1">Qwen / Qwen - Image - 2 . 1 · Hugging Face</a></li>
<li><a href="https://github.com/QwenLM/Qwen-Image-2.1">GitHub - QwenLM/ Qwen - Image - 2 . 1 : Qwen 's most powerful...</a></li>
<li><a href="https://www.goenhance.ai/image-models/qwen-image-2-1">Qwen - Image - 2 . 1 : Open-Weight AI Image and Editing Model</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该模型 7B 的小体积、原生透明通道以及相比其他开源权重方案显著提升的文本渲染能力。主要担忧在于相比此前采用 Apache 许可的 Qwen 模型，其许可证更为严格，但部分用户认为文本渲染能力足以让人忽略这一限制。此外还有关于如何在本地运行该模型以及与本地代码生成能力对比的讨论。

**标签**: `#AI`, `#image-generation`, `#open-weights`, `#Qwen`, `#text-to-image`

---

<a id="item-3"></a>
## [斯诺登档案的最终去向：一次回顾性分析](https://libroot.org/posts/what-happened-to-the-snowden-archive) ⭐️ 8.0/10

libroot.org 上发表的一篇文章探讨了斯诺登档案的最终去向，分析了其发布历史、所引发的法律与伦理困境，以及为何只有一小部分泄露文件最终被公之于众。该文在聚合平台上引发了热烈讨论，获得 492 分和 329 条评论。 斯诺登档案重塑了全球关于大规模监控、隐私以及国家安全与新闻自由之间平衡的讨论，因此理解其大部分内容为何至今未公开，对新闻业、举报政策及未来的泄密事件都具有重要意义。相关讨论也凸显了过去十年公众对斯诺登和监控态度的转变。 斯诺登泄露的文件中只有一小部分被公开，主要原因是需要编辑以保护个人信息，以及记者面临的持续法律风险。社区成员指出，该档案已在 GitHub 上部分镜像，一些人主张未来应像国家档案规则那样，在特定期限后自动解密并公开这些材料。

hackernews · EXHades · 9月20日 22:35 · [社区讨论](https://news.ycombinator.com/item?id=49780820)

**背景**: 2013 年，前美国国家安全局（NSA）承包商爱德华·斯诺登泄露了大量绝密文件，揭露了美国国家安全局及其盟友实施的大规模监控项目。他将文件分享给包括格伦·格林沃尔德和劳拉·珀特阿斯在内的记者，后者通过《卫报》、《华盛顿邮报》以及后来的 The Intercept 等媒体发表了相关报道。斯诺登此后流亡俄罗斯并至今滞留，在美国面临间谍罪指控。自那以后，档案缓慢且选择性的发布方式一直是争论的焦点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Snowden_disclosures">Snowden disclosures - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Edward_Snowden">Edward Snowden - Wikipedia</a></li>
<li><a href="https://github.com/iamcryptoki/snowden-archive">GitHub - iamcryptoki/ snowden -archive: A collection of all...</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：一些人认为档案应在隐去个人信息后全部公开，另一些人则为出于法律和伦理风险而采取的谨慎发布方式辩护。有人指出公众兴趣已经减弱，奥弗顿窗口发生偏移，斯诺登流亡俄罗斯使他在部分人眼中不再像烈士。还有人推荐阅读 The Intercept 深入的斯诺登档案系列报道，因其内容详实。

**标签**: `#Snowden`, `#journalism`, `#national security`, `#privacy`, `#whistleblowing`

---

<a id="item-4"></a>
## [LLMentalist 效应：大语言模型的智能只是冷读术吗？](https://softwarecrisis.dev/letters/llmentalist/) ⭐️ 8.0/10

2023 年发表在 softwarecrisis.dev 上的一篇文章认为，聊天式大语言模型所表现出的智能是一种错觉，并将其行为与灵媒和通灵者使用的冷读术相类比。该文在 Hacker News 上引发了 272 条评论的讨论，争论大语言模型究竟是真的智能，还是仅仅在模仿理解。 这一类比挑战了人们普遍持有的假设，即流畅的聊天机器人回复代表着真正的推理或理解，并促使 AI 界审视大语言模型的行为在多大程度上只是统计上的泛泛而谈，而非真正的洞察。这场讨论涉及图灵测试、拟人化以及我们定义智能的标准，影响着研究人员、开发者以及每天与这些系统交互的用户。 文章特别针对聊天式大语言模型，指出验证性陈述和福勒效应等技巧让聊天机器人和通灵者都能给出看似极其具体、实则统计上泛泛的答案。文章还提到 AI 研究素有忽视其他领域的名声，并认为这种对通灵骗术的重新实现很可能是无意之举。

hackernews · jalev · 9月20日 12:20 · [社区讨论](https://news.ycombinator.com/item?id=49775104)

**背景**: 冷读术是假通灵者使用的一种技巧，通过高概率猜测和对信号的快速反应，在客户未察觉的情况下巧妙套取信息。福勒效应（又称巴纳姆效应）是指人们倾向于认为模糊、笼统的人格描述高度准确地适用于自己。文章认为，聊天式大语言模型正是利用了这些相同的心理机制，制造出一种与通灵骗术如出一辙的智能错觉。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://softwarecrisis.dev/letters/llmentalist/">The LLMentalist Effect: how chat-based Large Language Models replicate the mechanisms of a psychic's con</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cold_reading">Cold reading - Wikipedia</a></li>
<li><a href="https://www.baldurbjarnason.com/2023/links-july-4/">'The LLMentalist Effect', and other links</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：有人指出图灵本人曾说过，一旦机器能通过他的测试，机器智能的问题就会变得无关紧要；也有人批评作者把一个非常开放的问题当成了已有定论。一些人指出，人类如此轻易地高估机器的智能，颇具讽刺意味；还有一位评论者干脆表示，他不在乎大语言模型是否“智能”或是否“真的在推理”。

**标签**: `#LLM`, `#AI`, `#intelligence`, `#philosophy`, `#cold-reading`

---

<a id="item-5"></a>
## [月之暗面与微软、亚马逊、谷歌洽谈 Kimi K3 收入分成](https://t.me/zaihuapd/43950) ⭐️ 8.0/10

据消息人士透露，月之暗面正就 Kimi K3 模型与微软、亚马逊、谷歌谈判收入分成，初期寻求最高 30% 的分成比例。若谈成，这将是中国 AI 公司与美国云巨头之间的首个大型模型收入分成协议，不过谈判仍处早期，核心细节未定，各方均拒绝置评。 若协议达成，将成为中国 AI 公司与美国超大规模云厂商之间的首个大型收入分成安排，可能重塑前沿模型在全球的分发与变现方式。这也表明，即便中美科技关系紧张，美国云厂商仍可能愿意托管并销售领先的中国开源权重模型。 Kimi K3 于 2026 年 7 月发布，总参数达 2.8 万亿，是迄今最大的开源权重模型，也是全球首个开源 3T 级模型，具备原生多模态能力和 100 万 token 上下文窗口。据称月之暗面的年度经常性收入在 6 月中旬已突破 3 亿美元，而 30% 只是初期报价，并非最终确定条款。

telegram · zaihuapd · 9月21日 06:44

**背景**: 月之暗面是一家中国 AI 初创公司，旗下 Kimi 系列开源权重大语言模型通过网页、API 和 Kimi Code 命令行代理对外提供。收入分成是云计算行业常见的合作模式，即模型开发者从云厂商销售该模型访问权所得收入中抽取一定比例。Kimi K3 的前代 K2 是万亿参数级开源模型，曾与 DeepSeek-V3 竞争，而 K3 将这一路线扩展到 2.8 万亿参数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.moonshot.ai/">Moonshot AI</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3">moonshotai/Kimi-K3 - Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (AI) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#business`, `#cloud-computing`, `#China`, `#partnership`

---