#!/usr/bin/env python3
import os
import re
import json
import datetime

# Configuration
BRIEFINGS_DIR = "./briefings"
OUTPUT_JSON_PATH = "./data/news.json"

def parse_briefing_markdown(md_content):
    """
    Parses Horizon-style markdown briefings into a list of structured news dicts.
    
    Expected format in Markdown:
    ## [Score] Title
    - Source: Source Name
    - URL: https://example.com
    - Category: AI / Dev / Startup / Hardware / Science
    - Publish Time: ISO string (optional)
    
    ### Core Takeaways
    - Bullet point 1
    - Bullet point 2
    
    ### AI Summary (ZH)
    Chinese summary text...
    
    ### AI Summary (EN)
    English summary text...
    
    ---
    """
    articles = []
    
    # Split by horizontal rule separator (or double line breaks followed by headers)
    raw_sections = re.split(r'\n---\n|\n###+ ---\n', md_content)
    
    article_id_counter = 1
    for section in raw_sections:
        section = section.strip()
        if not section:
            continue
            
        # Match header: ## [Score] Title
        header_match = re.search(r'^##\s*\[([0-9.]+)\]\s*(.*)', section, re.MULTILINE)
        if not header_match:
            continue
            
        score = float(header_match.group(1))
        title = header_match.group(2).strip()
        
        # Match metadata lines
        source_match = re.search(r'^-\s*Source:\s*(.*)', section, re.MULTILINE | re.IGNORECASE)
        url_match = re.search(r'^-\s*URL:\s*(.*)', section, re.MULTILINE | re.IGNORECASE)
        category_match = re.search(r'^-\s*Category:\s*(.*)', section, re.MULTILINE | re.IGNORECASE)
        time_match = re.search(r'^-\s*Publish\s*Time:\s*(.*)', section, re.MULTILINE | re.IGNORECASE)
        
        source = source_match.group(1).strip() if source_match else "Unknown"
        url = url_match.group(1).strip() if url_match else "#"
        category = category_match.group(1).strip() if category_match else "AI"
        
        # Categories mapping to standard front-end values (AI, Dev, Startup, Hardware, Science)
        cat_upper = category.upper()
        if "AI" in cat_upper or "MACHINE" in cat_upper:
            category = "AI"
        elif "DEV" in cat_upper or "TOOL" in cat_upper or "COD" in cat_upper:
            category = "Dev"
        elif "STARTUP" in cat_upper or "BUSINESS" in cat_upper or "FIN" in cat_upper or "CORP" in cat_upper:
            category = "Startup"
        elif "HARD" in cat_upper or "CHIP" in cat_upper or "DEVICE" in cat_upper or "VR" in cat_upper:
            category = "Hardware"
        elif "SCI" in cat_upper or "BIO" in cat_upper or "CHEM" in cat_upper or "PHYS" in cat_upper:
            category = "Science"
        else:
            category = "AI" # default fallback
            
        publish_time = time_match.group(1).strip() if time_match else datetime.datetime.utcnow().isoformat() + "Z"
        
        # Parse bullet points / takeaways
        takeaways = []
        takeaways_match = re.search(r'###\s*(?:Core Takeaways|核心要点|要点)(.*?)(?=###|\Z)', section, re.DOTALL | re.IGNORECASE)
        if takeaways_match:
            pts = re.findall(r'^\s*[-*+]\s*(.*)', takeaways_match.group(1), re.MULTILINE)
            takeaways = [p.strip() for p in pts if p.strip()]
            
        # Parse Chinese summary
        summary_zh = ""
        summary_zh_match = re.search(r'###\s*(?:AI Summary \(ZH\)|AI 总结|中文总结)(.*?)(?=###|\Z)', section, re.DOTALL | re.IGNORECASE)
        if summary_zh_match:
            summary_zh = summary_zh_match.group(1).strip()
            
        # Parse English summary
        summary_en = ""
        summary_en_match = re.search(r'###\s*(?:AI Summary \(EN\)|英文总结|英文摘要)(.*?)(?=###|\Z)', section, re.DOTALL | re.IGNORECASE)
        if summary_en_match:
            summary_en = summary_en_match.group(1).strip()
            
        # Fallback if specific sections are missing but we have body text
        if not summary_zh and not summary_en:
            # Look for generic body content
            body_match = re.search(r'-\s*Category:.*?\n\n(.*)', section, re.DOTALL)
            if body_match:
                summary_zh = body_match.group(1).strip()
                
        # Clean up summaries (remove markdown bolding or references if any)
        summary_zh = re.sub(r'\n+', '\n', summary_zh)
        summary_en = re.sub(r'\n+', '\n', summary_en)
        
        articles.append({
          "id": str(article_id_counter),
          "title": title,
          "importance_score": score,
          "source": source,
          "url": url,
          "category": category,
          "publish_time": publish_time,
          "summary_zh": summary_zh or "无中文总结",
          "summary_en": summary_en or title,
          "takeaways": takeaways or ["核心要点已在文章中包含。"]
        })
        article_id_counter += 1
        
    return articles

def write_demo_markdown():
    """Generates a demo markdown file in the briefings folder for test run."""
    os.makedirs(BRIEFINGS_DIR, exist_ok=True)
    demo_md_content = """# Horizon Daily Tech Briefing - 2026-07-03

## [9.9] OpenAI Announces 'GPT-5' with Native Autonomy and Web Interactions
- Source: OpenAI Blog
- URL: https://openai.com/blog/gpt-5-announcement
- Category: AI
- Publish Time: 2026-07-03T16:00:00Z

### Core Takeaways
- GPT-5 introduces full agentic autonomy out of the box, executing code local-first.
- Achieved a 95% success rate on complex web-navigation and multi-app tasks.
- Released via a public beta program starting today with reduced token pricing.

### AI Summary (ZH)
OpenAI 今日正式公布了其下一代旗舰大模型 GPT-5。该模型在自主执行能力和网页交互层面实现了质的突破，支持跨软件和网页环境下的多步骤规划与执行。OpenAI 称，GPT-5 能无缝使用本地终端、主流开发工具并自主完成复杂的系统调试任务，标志着人工智能从“对话助手”迈向了“自主智能体”时代。

### AI Summary (EN)
OpenAI has officially introduced GPT-5, demonstrating significant advances in autonomous task completion and browser interaction. The new flagship model excels at complex planning, tool invocation, and terminal execution, shifting the paradigm from conversation to proactive action.

---

## [8.8] Next.js 16 Drops: Complete Dynamic Routing Overhaul and React 20 Stable support
- Source: Vercel
- URL: https://nextjs.org/blog/next-16
- Category: Dev
- Publish Time: 2026-07-03T14:30:00Z

### Core Takeaways
- Unveiled a revamped routing paradigm featuring zero-runtime dynamic rendering rules.
- Native build step integration with Rolldown, cutting dev compile times by 70%.
- Full out-of-the-box compatibility with React 20 Server Components features.

### AI Summary (ZH)
Vercel 团队发布了 Next.js 16 版本，完成了自 App Router 推出以来最大幅度的动态路由重构。新版本引入了零运行时动态渲染系统，并在底层全面整合了 Rolldown 以加速编译，开发环境启动速度提升近 3 倍。此外，新版也率先支持了 React 20 稳定版的最新特性。

### AI Summary (EN)
Vercel has released Next.js 16, which completely redesigns its routing engine and natively utilizes Rolldown for bundler tooling. This update dramatically reduces startup delays and fully integrates React 20 stable features.
"""
    test_filepath = os.path.join(BRIEFINGS_DIR, "briefing_latest.md")
    with open(test_filepath, "w", encoding="utf-8") as f:
        f.write(demo_md_content)
    print(f"Created demo markdown briefing at: {test_filepath}")

def main():
    print("=" * 60)
    print("           TODAY TECH TOP 20 - DATA SYNC PIPELINE            ")
    print("=" * 60)
    
    # 1. Generate demo markdown if briefing directory doesn't exist
    if not os.path.exists(BRIEFINGS_DIR) or not os.listdir(BRIEFINGS_DIR):
        print("Briefings directory empty or missing. Writing a demo briefing for testing...")
        write_demo_markdown()
        
    # 2. Find latest markdown file in briefings/
    files = [os.path.join(BRIEFINGS_DIR, f) for f in os.listdir(BRIEFINGS_DIR) if f.endswith(".md")]
    if not files:
        print("Error: No markdown files found to sync.")
        return
        
    latest_file = max(files, key=os.path.getmtime)
    print(f"Processing latest briefing: {latest_file}")
    
    # 3. Parse content
    with open(latest_file, "r", encoding="utf-8") as f:
        md_content = f.read()
        
    articles_list = parse_briefing_markdown(md_content)
    
    # 4. Save to json
    os.makedirs(os.path.dirname(OUTPUT_JSON_PATH), exist_ok=True)
    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(articles_list, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully compiled {len(articles_list)} articles into {OUTPUT_JSON_PATH}!")
    print("Done! Web dashboard is now updated.")

if __name__ == "__main__":
    main()
