# Today Tech Top 20 - AI 科技新闻精选（基于 Horizon 驱动的无服务器仪表盘）

这是一个整合了 **Horizon 智能科技新闻聚合器** 与 **高颜值静态展示面板** 的完整开源产品方案。

**零服务器成本**：通过 GitHub Actions 每天定时抓取 RSS、Hacker News、GitHub、Reddit 等源，使用 AI (OpenAI / DeepSeek / Gemini 等) 进行去重、打分及双语总结，输出为静态 JSON，并由 Vercel 进行全球分发。

---

## 🌟 核心组成

### 1. 🎨 前端展示面板 (`index.html`, `style.css`, `app.js`)
基于纯静态 HTML5/CSS3/Vanilla JS 构建，呈现极为精致的数码感设计：
- **暗黑主题**：支持一键切换明暗模式。
- **毛玻璃效果**：细腻的 UI 细节，带有流光边框。
- **侧边抽屉式阅读**：点击卡片滑出 AI 总结，支持**中英双语一键切换**。
- **智能检索与过滤**：支持全文关键词实时过滤、按来源/时间排序、分类快速筛选。
- **收藏夹**：本地持久化（`localStorage`）收藏，方便稍后阅读。
- **一键分享**：格式化复制新闻要点与中文摘要到剪贴板。

### 2. 🤖 后端聚合引擎 (基于 [Thysrael/Horizon](https://github.com/Thysrael/Horizon))
用 Python 开发的 AI News Radar 系统：
- **自动抓取**：定时提取 RSS、Hacker News、GitHub Trending、Reddit 热帖。
- **AI 智能评分**：根据设定提示词，对文章技术深度和新颖度打分（0-10分）。
- **AI 双语总结**：使用 LLM 自动生成核心要点（Takeaways）和中英文详细总结。
- **交付通道**：支持将 Markdown 简报发布至 GitHub Pages、发送邮件或微信/飞书 Webhook。

### 3. 🔄 数据同步脚本 (`sync_briefing.py`)
桥接 Horizon 与前端面板的纽带：
- 自动读取 Horizon 产生的最新中英文 Markdown 简报（`data/summaries/`）。
- 智能解析 Markdown 并使用 URL 作为唯一标识进行**中英文双语合并**。
- 生成结构化的 `data/news.json` 静态数据源供前端极速加载。

---

## ⚙️ 部署与自动化配置步骤

### 第一步：克隆并推送到您的 GitHub 仓库
您已经完成了这一步。代码已成功推送到您的 GitHub 仓库。

### 第二步：配置 GitHub 仓库的 API Keys (Secrets)
要让 GitHub Actions 在云端定时自动抓取，您需要提供 LLM 接口的 API Key：
1. 打开您的 GitHub 仓库页面，点击右上角的 **Settings**。
2. 依次选择左侧菜单的 **Secrets and variables** -> **Actions**。
3. 点击 **New repository secret**，添加以下密钥（根据您使用的 AI 模型选择添加）：
   - `OPENAI_API_KEY`: OpenAI 接口密钥 (如果使用 GPT 系列模型)。
   - `DEEPSEEK_API_KEY`: DeepSeek 接口密钥 (推荐，性价比较高)。
   - `GOOGLE_API_KEY`: Gemini 接口密钥。
4. **开启代码写入权限**：滚动到 Settings -> Actions -> General 页面底部，找到 **Workflow permissions**，将其勾选为 **`Read and write permissions`** 并保存（这允许定时工作流自动提交更新后的新闻数据 `news.json`）。

### 第三步：修改抓取配置 (`data/config.github.json`)
默认的抓取源和 AI 模型在 `data/config.github.json` 中配置：
1. 打开 `data/config.github.json`：
   - 在 `"ai"` 节点下，将 `"provider"` 修改为您所选的提供商（如 `"deepseek"` 或 `"openai"`），并指定具体的 `"model"` 名称。
   - 在 `"sources"` 节点下，添加或修改您关注的 **RSS 订阅源**（支持国内 RSSHub 服务）。
2. 提交修改并推送到 GitHub 仓库。

### 第四步：在 Vercel 中关联自动发布
1. 访问您已登录的 [Vercel 控制台](https://vercel.com/)，进入您之前部署的 **`today-tech-top20`** 项目。
2. 点击 **Settings** -> **Git**，关联您的 GitHub 仓库。
3. 关联成功后，每当 GitHub Actions 定时抓取并将最新的 `news.json` 提交到仓库时，Vercel 都会自动触发全球 CDN 更新，您的用户无需刷新后端服务器即可瞬间看到最新科技新闻！

---

## 💻 本地运行与开发

### 前端本地预览
在项目根目录下启动一个简易本地服务器：
```bash
# Python 3
python -m http.server 8000
```
然后打开浏览器访问 `http://localhost:8000` 即可预览高保真前端界面。

### 运行同步转换
如果您在本地通过 Horizon 产生了新的 Markdown 简报，可以手动执行转换脚本：
```bash
python sync_briefing.py
```
这会解析 `data/summaries/` 下的最新简报，并重新编译输出 `data/news.json`。
