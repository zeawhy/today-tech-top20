---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> 从 28 条内容中筛选出 9 条重要资讯。

---

1. [vLLM v0.25.0：Model Runner V2 成为默认，移除 PagedAttention](#item-1) ⭐️ 9.0/10
2. [人形机器人完成全球首例活猪胆囊手术](#item-2) ⭐️ 9.0/10
3. [苹果起诉 OpenAI 系统性窃取商业机密](#item-3) ⭐️ 9.0/10
4. [OpenAI 发布 GPT-5.6 系列：Sol、Terra、Luna](#item-4) ⭐️ 9.0/10
5. [ClickHouse 通过 Peering 机制将 PgBouncer 吞吐量提升 4 倍](#item-5) ⭐️ 8.0/10
6. [VultronRetriever 模型登顶 MTEB，可在 iPhone 上运行](#item-6) ⭐️ 8.0/10
7. [U-Boot 六个漏洞可在系统启动前执行恶意代码](#item-7) ⭐️ 8.0/10
8. [谷歌反对欧洲网站屏蔽，美国同类立法加速](#item-8) ⭐️ 8.0/10
9. [上海设定 2027 年脑机接口临床应用目标](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0：Model Runner V2 成为默认，移除 PagedAttention](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 9.0/10

vLLM v0.25.0 将 Model Runner V2 设为所有稠密模型的默认执行路径，移除了旧版 PagedAttention，并新增了 LLaVA-OneVision-2、GLM-5 等模型，以及流式解析引擎和通用推测解码。 此版本标志着 vLLM 的重大架构转变，提升了性能和模块化程度，通过实现更快的推理和更简便的模型集成，惠及整个 LLM 服务生态系统。 Model Runner V2 现在支持 EVS、实时嵌入、Mamba 混合模型的前缀缓存，以及带有完整 CUDA 图的动态推测解码。Transformers 后端速度已与原生 vLLM 持平，并获得了 FP8 MoE 支持。

github · khluu · 7月11日 20:06

**背景**: vLLM 是一个开源的大语言模型推理引擎，采用 PagedAttention 实现高效的 KV 缓存管理。Model Runner V2 是重新设计的执行核心，解决了技术债务并提升了模块化程度，比原有的 V1 后端更快、更灵活。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/en/v0.22.1/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://en.wikipedia.org/wiki/PagedAttention">PagedAttention</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#open-source`, `#release`, `#AI infrastructure`

---

<a id="item-2"></a>
## [人形机器人完成全球首例活猪胆囊手术](https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/) ⭐️ 9.0/10

外科医生远程操控宇树 G1 人形机器人，成功在两只活猪身上完成了腹腔镜胆囊切除术，这是通用人形机器人首次用于活体手术。研究结果已发表在《自然》期刊。 这一突破表明，低成本通用人形机器人有望在资源有限的场景（如农村、战场或空间站）中普及微创手术。它挑战了达芬奇等昂贵专用手术机器人的主导地位。 宇树 G1 基础款售价低至 13500 美元，配备灵巧手后约 67000 美元，而专用手术机器人价格在 50 万至数百万美元。该机器人高约 1.5 米、重 27 公斤，由加州大学圣地亚哥分校的研究人员远程操控。

telegram · zaihuapd · 7月11日 02:29

**背景**: 腹腔镜胆囊切除术是一种微创手术，用于切除胆囊，常用于治疗有症状的胆结石。目前机器人手术的标准系统——达芬奇手术系统，售价数十万至数百万美元，限制了其普及。像宇树 G1 这样的通用人形机器人设计用于多种任务，价格低廉，但此前从未用于活体手术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unitree_Robotics">Unitree Robotics - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Laparoscopic_cholecystectomy">Laparoscopic cholecystectomy</a></li>
<li><a href="https://www.unitree.com/g1/">Humanoid robot G1_Humanoid Robot Functions_Humanoid Robot Price | Unitree Robotics</a></li>

</ul>
</details>

**标签**: `#robotics`, `#surgery`, `#humanoid robot`, `#medical technology`, `#AI`

---

<a id="item-3"></a>
## [苹果起诉 OpenAI 系统性窃取商业机密](https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html) ⭐️ 9.0/10

2026 年 7 月 10 日，苹果在美国加州北区联邦法院起诉 OpenAI、两名前员工及 io Products，指控 OpenAI 系统性窃取苹果的产品设计、制造工艺及供应链机密，以加速其消费级硬件研发。 这起两大科技巨头之间的诉讼可能为 AI 硬件竞赛中的商业秘密保护树立先例，可能影响 OpenAI 的硬件计划及整个行业的招聘行为。 苹果指控前员工刘畅离职后仍访问内部网络并下载数十份硬件文件；OpenAI 硬件负责人陈玉丹在离职前将供应商资料发送至个人邮箱，并要求求职者携带苹果零部件参加面试。苹果还表示，目前有超过 400 名前员工在 OpenAI 工作。

telegram · zaihuapd · 7月11日 03:14

**背景**: OpenAI 于 2025 年 5 月收购了 io Products，以主导其硬件开发。io 由 Jony Ive、Scott Cannon、Evans Hankey 和 Tang Tan 于 2024 年创立，旨在打造 AI 硬件。诉讼称 OpenAI 的硬件业务因依赖窃取的商业机密而“从根上烂透了”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/cy8w379e091o">Apple sues OpenAI , its employees claiming theft of trade secrets</a></li>
<li><a href="https://www.theguardian.com/technology/2026/jul/10/apple-sues-openai-trade-secrets">Apple sues OpenAI , alleging artificial intelligence company stole trade ...</a></li>
<li><a href="https://apnews.com/article/apple-openai-lawsuit-trade-secrets-theft-6fff8833f5889d86406b89a02dd8fb16">Apple files lawsuit accusing OpenAI of stealing trade secrets</a></li>

</ul>
</details>

**标签**: `#lawsuit`, `#trade secrets`, `#Apple`, `#OpenAI`, `#AI hardware`

---

<a id="item-4"></a>
## [OpenAI 发布 GPT-5.6 系列：Sol、Terra、Luna](https://t.me/zaihuapd/42497) ⭐️ 9.0/10

OpenAI 正式发布 GPT-5.6 系列，包含三个层级：旗舰级 Sol、平衡型 Terra 和低成本 Luna。该系列引入了 max/ultra 推理、多智能体协作和程序化工具调用，在代码、知识工作、设计、科研和网络安全方面有显著提升。 此次发布标志着 AI 模型效率和能力的重大进步，通过分层定价满足不同用例，同时引入多智能体协作和程序化工具调用等高级功能，降低复杂任务的 token 消耗和成本。它为行业树立了性能成本比的新标杆。 每百万 token 定价：Sol 输入 $5 / 输出 $30，Terra 输入 $2.50 / 输出 $15，Luna 输入 $1 / 输出 $6。裸 gpt-5.6 API 别名默认指向 Sol。程序化工具调用允许模型通过代码编排工具，而非逐个 API 往返，从而提高效率。

telegram · zaihuapd · 7月11日 13:34

**背景**: GPT-5.6 是 OpenAI 最新一代大型语言模型，接替 GPT-4。多智能体协作使多个 AI 智能体能够协调完成复杂任务，而程序化工具调用（此前见于 Anthropic 的 Claude）允许模型编写代码来调用外部工具，从而降低延迟和成本。这些功能旨在让 AI 更适用于企业和研究应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>
<li><a href="https://www.vellum.ai/blog/gpt-5-6-benchmarks-explained">GPT-5.6 Sol vs Terra vs Luna: Which Tier Should You Actually Use?</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-gpt-5-6-soul-terra-luna-explained">What Is GPT-5.6? OpenAI's Soul, Terra, and Luna Model Tiers Explained | MindStudio</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#AI`, `#language models`, `#multi-agent`

---

<a id="item-5"></a>
## [ClickHouse 通过 Peering 机制将 PgBouncer 吞吐量提升 4 倍](https://clickhouse.com/blog/pgbouncer-clickhouse-managed-postgres) ⭐️ 8.0/10

ClickHouse 在 PgBouncer 中实现了一种 peering 机制，可将查询取消请求转发到正确的进程，从而在使用 so_reuseport 的多进程配置下实现高达 4 倍的吞吐量提升。 这一进展使得 PostgreSQL 连接池能够跨多个进程和机器水平扩展，同时不破坏查询取消功能，这对于高可用云部署和大规模托管数据库服务至关重要。 Peering 功能自 PgBouncer 1.19.0 起可用，使用 peer_id（最大 16383）在进程间协调取消请求。ClickHouse 的实现利用此功能，通过 so_reuseport 在单个端口后运行多个 PgBouncer 实例。

hackernews · saisrirampur · 7月11日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=48872874)

**背景**: PgBouncer 是 PostgreSQL 的轻量级连接池。当使用 so_reuseport 允许多个进程共享同一监听端口时，取消请求可能落到不拥有该会话的进程上，导致取消被忽略。Peering 通过将请求转发到正确的进程来解决此问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://manpages.debian.org/testing/pgbouncer/pgbouncer.5.en.html">pgbouncer (5) — pgbouncer — Debian testing — Debian Manpages</a></li>
<li><a href="https://dataegret.com/2024/08/handling_cancellation_request/">Handling Cancellation Request - Data Egret</a></li>
<li><a href="https://boosterkrd.github.io/2024/08/20/Handling-Cancellation-Request.html">Handling Cancellation Request | Booster’s Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者提出了替代方案如 Odyssey 和 pgdog，并询问了 Kubernetes 兼容性。一些人指出，如果每个 pod 有自己的池，则可能不需要 peering，但其他人认为多实例部署中仍有价值。

**标签**: `#PostgreSQL`, `#PgBouncer`, `#scaling`, `#connection pooling`, `#ClickHouse`

---

<a id="item-6"></a>
## [VultronRetriever 模型登顶 MTEB，可在 iPhone 上运行](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

VultronRetriever 模型系列（包括 Prime-8B、Core-4.5B 和 Flash-0.8B）已在 HuggingFace 上发布，并在 MTEB 排行榜上各自类别中排名第一，其中 Prime 模型为全球第一。 这些模型相比之前的领先者，索引存储最多缩小 16 倍，吞吐量提高 12 倍，并且可以在 iPhone 上完全离线运行，标志着边缘 AI 和高效检索领域的重大进步。 VultronRetrieverFlash-0.8B 的性能优于其规模 5 倍的模型，离线每分钟可索引多达 60 张图像。这些模型采用 Hydra 架构实现后期交互检索，在精度高的同时内存消耗仅为同类模型的一半。

reddit · r/MachineLearning · /u/madkimchi · 7月11日 15:22

**背景**: MTEB（大规模文本嵌入基准）是评估嵌入模型在检索、分类和聚类等任务上性能的标准公开排行榜。后期交互检索（如 ColBERT 所用）将查询和文档分开处理，直到最后匹配步骤，从而实现高效精准的搜索。Hydra 架构是一种模块化设计，结合了稀疏注意力、混合专家和双记忆机制，用于高效的长上下文推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB Leaderboard - a Hugging Face Space by mteb</a></li>
<li><a href="https://weaviate.io/blog/late-interaction-overview">An Overview of Late Interaction Retrieval Models... | Weaviate</a></li>
<li><a href="https://arxiv.org/abs/2508.15099">[2508.15099] Hydra: A Modular Architecture for Efficient Long-Context Reasoning</a></li>

</ul>
</details>

**标签**: `#retrieval`, `#MTEB`, `#edge AI`, `#embedding`, `#HuggingFace`

---

<a id="item-7"></a>
## [U-Boot 六个漏洞可在系统启动前执行恶意代码](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

Binarly 披露了 U-Boot 的 FIT 签名验证中的六个漏洞，其中两个可导致任意代码执行，四个可导致拒绝服务，影响自 2013.07 以来的版本。 这些漏洞（BRLY-2026-037 至 BRLY-2026-042）位于 FIT 镜像解析代码中；补丁已被上游接受，但需要厂商集成到固件更新中才能分发，已停止支持的设备将永久存在风险。

telegram · zaihuapd · 7月11日 08:32

**背景**: U-Boot 是嵌入式设备中广泛使用的开源引导程序，负责初始化硬件并加载操作系统。FIT（Flattened Image Tree）是一种用于打包启动镜像的标准格式，其签名验证确保只执行受信任的固件。这些漏洞绕过了该验证，使攻击能够在设备启动的最早阶段发生。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.binarly.io/blog/unfit-to-boot-breaking-u-boots-fit-signature-verification">Unfit to Boot: Breaking U-Boot's FIT Signature Verification</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/">New U-Boot flaws could enable stealthy firmware attacks</a></li>
<li><a href="https://thehackernews.com/2026/07/six-new-u-boot-flaws-could-let.html">Six New U-Boot Flaws Could Let Malicious Images Crash Devices ...</a></li>

</ul>
</details>

**标签**: `#security`, `#bootloader`, `#vulnerability`, `#firmware`, `#U-Boot`

---

<a id="item-8"></a>
## [谷歌反对欧洲网站屏蔽，美国同类立法加速](https://torrentfreak.com/google-opposes-site-blocking-in-europe-as-u-s-piracy-blocking-plans-gain-momentum/) ⭐️ 8.0/10

谷歌向欧盟委员会提交文件，反对扩大网站屏蔽措施，称屏蔽 DNS 解析器、IP 地址和 VPN 的做法无效且不成比例。与此同时，美国国会也在推进类似的反盗版立法，众议员 Issa 计划推动一项网站屏蔽法案。 这凸显了版权执法与互联网自由之间日益紧张的全球矛盾，谷歌等大型科技公司正在抵制广泛的屏蔽措施。其结果可能为各国政府如何平衡知识产权保护与开放互联网原则树立先例。 谷歌的文件引用了具体的误封案例，例如意大利的反盗版系统误封了 Google Drive 子域名以及托管 4200 万个域名的 Cloudflare IP 地址。谷歌尚未对美国立法公开表态，但其欧盟文件表明，它更倾向于提供更好的合法替代服务，而非扩大屏蔽。

telegram · zaihuapd · 7月11日 15:10

**背景**: 网站屏蔽是一种常见的反盗版技术，即命令 ISP 或 DNS 解析器阻止访问侵权网站。批评者认为，这类措施常导致误封，影响合法服务，且用户可通过 VPN 或替代 DNS 绕过。欧盟和美国都在考虑更新法律框架以打击在线盗版，但方法不同。

**标签**: `#internet governance`, `#copyright`, `#site blocking`, `#tech policy`, `#Google`

---

<a id="item-9"></a>
## [上海设定 2027 年脑机接口临床应用目标](https://t.me/zaihuapd/42501) ⭐️ 8.0/10

上海市科学技术委员会印发《上海市脑机接口未来产业培育行动方案（2025-2030 年）》，目标在 2027 年前实现高质量脑控，半侵入式脑机接口产品在国内率先实现临床应用，侵入式脑机接口研发取得突破。该计划推动 5 款以上侵入式、半侵入式脑机接口产品完成医疗器械型式检验和临床试验，面向失语、瘫痪等患者实现部分语言和运动功能恢复。 这是一项重要的政策里程碑，为脑机接口在中国的临床转化提供了清晰的路线图和政府支持，有望加速基于脑机接口的医疗器械开发，并将上海定位为神经技术的全球中心。具体目标和产品指标表明，中国正大力推动脑机接口从研究实验室走向实际医疗应用，惠及严重神经系统疾病患者。 该计划区分了半侵入式和侵入式脑机接口：半侵入式设备（如 ECoG）置于颅骨下但大脑组织外，在信号质量和安全性之间取得平衡；侵入式设备（如微电极阵列）穿透大脑以获取高分辨率信号，但需要手术。2027 年目标包括完成医疗器械型式检验和临床试验，这是在中国获得市场准入的强制性监管步骤。

telegram · zaihuapd · 7月11日 15:49

**背景**: 脑机接口（BCI）通过解码神经信号实现大脑与外部设备之间的直接通信。它们分为非侵入式（如 EEG 头戴设备）、半侵入式（如 ECoG）和侵入式（如犹他阵列）三种类型，信号保真度依次提高，但手术风险也随之增加。中国一直在积极投资脑机接口技术，该行动计划与国家在新兴神经技术领域领先的战略相一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/76363987">【深度解析】一文看懂脑机接口技术的现状与未来！ - 知乎</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/699343201">侵入式、半侵入式、非侵入式脑机接口，具体应该怎么选</a></li>
<li><a href="https://www.nifdc.org.cn/nifdc///xxgk/zcfg/zcjd/202607011610522105082.html">《脑机接口医疗器械产品分类界定指导原则》解读</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#policy`, `#clinical application`, `#China`, `#neurotechnology`

---