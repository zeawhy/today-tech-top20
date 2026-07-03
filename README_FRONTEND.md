# Today Tech Top 20 - AI 科技新闻精选静态面板

这是一个专为“每日科技新闻 Top20 + AI 中文总结”设计的**高品质、无服务器（Serverless）静态展示面板**。
它具有现代精美设计（暗黑模式、毛玻璃效果、流畅动画），并且完美支持与 GitHub Actions、Vercel 及 Horizon 等抓取工具无缝对接。

---

## 🌟 核心特性

- **极致设计与微交互**：
  - 默认暗黑主题（Cyber Slate），支持一键切换明暗模式。
  - 毛玻璃卡片（Glassmorphism）和流光高亮边框。
  - 丝滑侧面抽屉（Side Drawer）动效，提供沉浸式 AI 深度内容阅读。
- **实时过滤与检索**：
  - 全文实时检索：根据标题、英文原文或中文总结瞬间筛选。
  - 按分类过滤：AI与机器学习、开发工具、商业与初创、前沿硬件、前沿科学。
  - 按重要性（AI Score 排序，突出 Top 20 中最不可错过的头条）和发布时间排序。
- **互动小工具**：
  - **收藏夹/稍后阅读**：本地持久化保存（`localStorage`）。
  - **中英双语总结切换**：在抽屉面板中，支持一键切换中英文详细总结。
  - **一键分享**：格式化复制新闻要点与中文摘要到剪贴板。

---

## 🛠 项目结构

```
today-tech-top20/
├── .github/workflows/
│   └── update_news.yml      # GitHub Actions 定时任务工作流
├── data/
│   └── news.json            # 静态数据源（由同步脚本自动生成）
├── briefings/
│   └── briefing_latest.md   # [示例] 抓取器生成的原始 Markdown 简报
├── index.html               # 主体 HTML5 结构
├── style.css                # 精致的 CSS 设计系统
├── app.js                   # 前端状态与交互控制逻辑
├── sync_briefing.py         # 同步脚本：解析 Markdown 并生成 news.json
└── README.md                # 部署与配置文档
```

---

## 🚀 部署与自动化配置指南（无服务器部署）

整个系统通过 GitHub + Vercel + GitHub Actions 实现 **100% 免费的 Serverless 闭环**：

### 第一步：创建 GitHub 仓库并上传代码
1. 将 `today-tech-top20` 文件夹推送到您的 GitHub 个人私有或公开仓库中：
   ```bash
   git init
   git add .
   git commit -m "feat: init today tech top 20 dashboard"
   git branch -M main
   git remote add origin git@github.com:您的用户名/您的仓库名.git
   git push -u origin main
   ```

### 第二步：将项目导入 Vercel 部署
1. 登录 [Vercel 官网](https://vercel.com/)。
2. 点击 **Add New** -> **Project**，导入您刚才创建的 GitHub 仓库。
3. **Framework Preset** 选择 **Other** (不需要修改任何构建命令，它只是纯静态的 HTML/CSS/JS 项目)。
4. 点击 **Deploy**，部署完成后您将获得一个专属的二级域名（如 `https://your-project.vercel.app`）。

### 第三步：配置 GitHub Actions 定时抓取
项目中的 `.github/workflows/update_news.yml` 已为您配置好定时流水线。
1. 在您的 GitHub 仓库的 **Settings** -> **Actions** -> **General** 中，确保 `Workflow permissions` 被设置为 `Read and write permissions`（允许脚本将抓取生成的 `news.json` 自动 commit 并 push 回仓库）。
2. 每当 GitHub Actions 运行并向仓库提交新的 `news.json` 时，**Vercel 会自动检测到 main 分支的 push 并触发秒级增量部署**。您的用户将在无需刷新后端服务器的情况下瞬间查看到最新新闻！

---

## 🔗 如何接入 Horizon / 自研抓取器

### 方式 A：基于 Markdown 简报（Horizon 默认输出）
如果您使用 [Horizon](https://github.com/Thysrael/Horizon)，它会在定时运行后产生一个 Markdown 格式的 daily briefing。
1. 配置您的抓取任务，将生成的最新简报 Markdown 保存到仓库下的 `briefings/` 目录下（或者配置脚本写入 `briefings/briefing_latest.md`）。
2. 流水线中的 `sync_briefing.py` 会被 GitHub Actions 自动调用。它使用预设的正则表达式，智能提取 `## [重要性评分] 标题`、`Source`、`URL`、`Core Takeaways`（要点）、`AI Summary`，并输出为 `data/news.json` 覆盖前端。

### 方式 B：直接写入 JSON
如果您想跳过 markdown 转换，可以直接修改抓取器的代码，使其在抓取/AI评分/AI总结完成后，按照 `data/news.json` 中的 schema 直接输出 JSON 数组并保存到该路径，GitHub Actions 会直接将其推送到 GitHub 并出发 Vercel 重新构建。
