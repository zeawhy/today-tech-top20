#!/usr/bin/env python3
import os
import re
import json
import datetime
from pathlib import Path

# Configuration
SUMMARIES_DIR = "./data/summaries"
OUTPUT_JSON_PATH = "./data/news.json"

def parse_horizon_markdown(filepath):
    """
    Parses a single Horizon daily summary markdown file (ZH or EN).
    Returns a list of dicts: {url, title, score, source_line, summary, background, discussion}
    """
    if not os.path.exists(filepath):
        return []
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    articles = []
    
    # Split content by the article marker, which is <a id="item-..."></a> followed by ##
    # Or simply split by the ## headers since each article starts with ##
    raw_sections = re.split(r'(?=<a id="item-\d+"></a>\n##|##\s*\[)', content)
    
    # The first section is the header and table of contents, we skip it
    for section in raw_sections[1:]:
        section = section.strip()
        if not section:
            continue
            
        # Match title, url and score from header: ## [Title](URL) ⭐️ Score/10
        # Example: ## [OpenAI GPT-5](https://openai.com) ⭐️ 9.9/10
        header_match = re.search(
            r'^##\s*\[(.*?)\]\((.*?)\)\s*(?:⭐|⭐️)\s*([0-9.]+)/10', 
            section, 
            re.MULTILINE
        )
        if not header_match:
            # Try alternate match if the ⭐️ symbol is missing or different
            header_match = re.search(r'^##\s*\[(.*?)\]\((.*?)\)\s*.*?([0-9.]+)/10', section, re.MULTILINE)
            
        if not header_match:
            continue
            
        title = header_match.group(1).strip()
        url = header_match.group(2).strip()
        score = float(header_match.group(3))
        
        # Split section into lines to parse details
        lines = section.split("\n")
        
        # Extract metadata and text sections
        summary_lines = []
        source_line = ""
        background = ""
        discussion = ""
        
        # State machine for parsing section body
        in_summary = True
        
        for line in lines[1:]: # Skip the header line
            line_str = line.strip()
            if not line_str:
                if summary_lines and in_summary:
                    # Let's keep empty lines in summary if they are not trailing
                    summary_lines.append("")
                continue
                
            # Check for source line (contains U+00B7 middle dot separator ' · ')
            if " · " in line_str and not line_str.startswith("**") and not line_str.startswith("-"):
                source_line = line_str
                in_summary = False
                continue
                
            # Check for Background section
            # English: **Background**: ...
            # Chinese: **背景**: ... or **背景信息**: ...
            bg_match = re.match(r'^\*\*(?:Background|背景|背景信息)\*\*:\s*(.*)', line_str, re.IGNORECASE)
            if bg_match:
                background = bg_match.group(1).strip()
                in_summary = False
                continue
                
            # Check for Discussion section
            # English: **Discussion**: ...
            # Chinese: **社区讨论**: ...
            disc_match = re.match(r'^\*\*(?:Discussion|社区讨论)\*\*:\s*(.*)', line_str, re.IGNORECASE)
            if disc_match:
                discussion = disc_match.group(1).strip()
                in_summary = False
                continue
                
            # Check for reference list (ignore details tag)
            if line_str.startswith("<details>") or line_str.startswith("</details>") or line_str.startswith("<li>"):
                in_summary = False
                continue
                
            # If we are still in summary, collect text
            if in_summary:
                summary_lines.append(line)
                
        # Clean up summary lines
        summary = "\n".join(summary_lines).strip()
        
        articles.append({
            "title": title,
            "url": url,
            "score": score,
            "source_line": source_line,
            "summary": summary,
            "background": background,
            "discussion": discussion
        })
        
    return articles

def detect_category(title, summary, source_line):
    """Smart category detection based on content keywords and source."""
    text = (title + " " + summary + " " + source_line).lower()
    
    if any(k in text for k in ["ai", "llm", "gpt", "model", "transformer", "neural", "deep learning", "agent", "claude", "llama", "deepseek"]):
        return "AI"
    elif any(k in text for k in ["rust", "golang", "typescript", "npm", "vite", "git", "cli", "compiler", "bundler", "developer", "framework", "api", "docker"]):
        return "Dev"
    elif any(k in text for k in ["ipo", "funding", "arr", "acquisition", "venture capital", "startup", "ceo", "dollar", "sec", "finance", "business"]):
        return "Startup"
    elif any(k in text for k in ["chip", "hardware", "cpu", "gpu", "oled", "display", "headset", "apple vision", "nvidia", "amd", "intel", "quantum"]):
        return "Hardware"
    elif any(k in text for k in ["physics", "biology", "alphafold", "chemistry", "ion", "rna", "dna", "science", "nature", "cell", "scientific"]):
        return "Science"
        
    return "AI" # Default

def parse_source_name(source_line):
    """Extracts a neat source name from a source line (e.g. 'rss · Simon Willison' -> 'Simon Willison')."""
    if not source_line:
        return "Horizon"
    parts = [p.strip() for p in source_line.split("·")]
    if len(parts) >= 2:
        # Check if first part is 'rss' or 'github' or 'reddit' and return the second part
        first = parts[0].lower()
        if first in ["rss", "github", "reddit"] and parts[1]:
            return parts[1]
        return parts[0].capitalize()
    return parts[0]

def main():
    print("=" * 60)
    print("           TODAY TECH TOP 20 - HORIZON INTEGRATION           ")
    print("=" * 60)
    
    # Ensure summaries directory exists
    os.makedirs(SUMMARIES_DIR, exist_ok=True)
    
    # 1. Check if we have any files in data/summaries matching horizon-*-zh.md or *-summary-zh.md
    files_in_dir = os.listdir(SUMMARIES_DIR)
    zh_files = [f for f in files_in_dir if (f.startswith("horizon-") and f.endswith("-zh.md")) or f.endswith("-summary-zh.md")]
    
    if not zh_files:
        print("No Horizon daily summaries found in ./data/summaries/.")
        print("Creating mock daily summaries for testing...")
        
        # Create a mock zh summary
        today_str = datetime.date.today().isoformat()
        zh_mock = f"""# Horizon 每日速递 - {today_str}
> 从 128 条内容中筛选出 2 条重要资讯。

1. [OpenAI 发布 GPT-5 模型](#item-1) ⭐️ 9.9/10
2. [Vite 7.0 正式版发布](#item-2) ⭐️ 8.9/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-5 模型](https://openai.com) ⭐️ 9.9/10

OpenAI 今日发布了其下一代大模型 GPT-5。该模型在逻辑推理和多步骤自主执行（Agent）层面实现了飞跃。

rss · OpenAI Blog · 16:00

**背景**: GPT-5 解决了大语言模型无法自主进行深度思考的顽疾。
**社区讨论**: 网友普遍对于其自主执行代码的能力感到兴奋，但也有安全担忧。

---

<a id="item-2"></a>
## [Vite 7.0 正式版发布](https://vite.dev) ⭐️ 8.9/10

Vite 7.0 默认采用 Rust 编写的打包器 Rolldown，编译和热更新速度提升高达 5 倍。

github · Vite · 14:30

**背景**: Rolldown 是 Vue 团队为了替代 Rollup 编写 of Rust 移植版本。
"""
        en_mock = f"""# Horizon Daily - {today_str}
> From 128 items, 2 important content pieces were selected

1. [OpenAI Releases GPT-5 Model](#item-1) ⭐️ 9.9/10
2. [Vite 7.0 Released](#item-2) ⭐️ 8.9/10

---

<a id="item-1"></a>
## [OpenAI Releases GPT-5 Model](https://openai.com) ⭐️ 9.9/10

OpenAI officially unveiled GPT-5, showing massive improvements in reasoning and autonomous agent planning.

rss · OpenAI Blog · 16:00

**Background**: GPT-5 addresses the limitations of previous models in deep multi-step planning.
**Discussion**: Users are generally excited about local-first execution, though safety is still debated.

---

<a id="item-2"></a>
## [Vite 7.0 Released](https://vite.dev) ⭐️ 8.9/10

Vite 7.0 now uses Rust-based bundler Rolldown by default, achieving up to 5x faster hot reload times.

github · Vite · 14:30

**Background**: Rolldown is the Rust rewrite of Rollup initiated by the Vue core team.
"""
        
        with open(os.path.join(SUMMARIES_DIR, f"horizon-{today_str}-zh.md"), "w", encoding="utf-8") as f:
            f.write(zh_mock)
        with open(os.path.join(SUMMARIES_DIR, f"horizon-{today_str}-en.md"), "w", encoding="utf-8") as f:
            f.write(en_mock)
            
        print("Mock files created successfully.")
        files_in_dir = os.listdir(SUMMARIES_DIR)
        zh_files = [f for f in files_in_dir if (f.startswith("horizon-") and f.endswith("-zh.md")) or f.endswith("-summary-zh.md")]

    # Get the latest date
    zh_files.sort()
    latest_zh_filename = zh_files[-1]
    
    # Extract date and determine English file name
    if latest_zh_filename.startswith("horizon-"):
        date_str = latest_zh_filename[8:18]
        latest_en_filename = f"horizon-{date_str}-en.md"
    else:
        date_str = latest_zh_filename[:10]
        latest_en_filename = f"{date_str}-summary-en.md"
    
    print(f"Targeting date: {date_str}")
    
    zh_filepath = os.path.join(SUMMARIES_DIR, latest_zh_filename)
    en_filepath = os.path.join(SUMMARIES_DIR, latest_en_filename)
    
    # Parse files
    zh_items = parse_horizon_markdown(zh_filepath)
    en_items = parse_horizon_markdown(en_filepath)
    
    print(f"Parsed {len(zh_items)} Chinese articles.")
    print(f"Parsed {len(en_items)} English articles.")
    
    # Combine results by URL
    combined_articles = []
    
    # Map English articles by URL for quick lookup
    en_by_url = {item["url"]: item for item in en_items}
    
    article_id = 1
    for zh_item in zh_items:
        url = zh_item["url"]
        en_item = en_by_url.get(url, None)
        
        title_zh = zh_item["title"]
        title_en = en_item["title"] if en_item else title_zh
        
        summary_zh = zh_item["summary"]
        summary_en = en_item["summary"] if en_item else summary_zh
        
        # Build clean takeaways from the summary or background
        takeaways = []
        if zh_item["background"]:
            takeaways.append(f"背景信息: {zh_item['background']}")
        if zh_item["discussion"]:
            takeaways.append(f"社区反馈: {zh_item['discussion']}")
            
        # If no bullet points yet, split summary into sentences and use first two
        if not takeaways:
            sentences = [s.strip() for s in re.split(r'[。！；!?;]', summary_zh) if s.strip()]
            takeaways = sentences[:3]
            
        # Compose full detailed HTML/Markdown summary
        full_zh = summary_zh
        if zh_item["background"]:
            full_zh += f"\n\n**背景**: {zh_item['background']}"
        if zh_item["discussion"]:
            full_zh += f"\n\n**社区讨论**: {zh_item['discussion']}"
            
        full_en = summary_en
        if en_item and en_item["background"]:
            full_en += f"\n\n**Background**: {en_item['background']}"
        if en_item and en_item["discussion"]:
            full_en += f"\n\n**Discussion**: {en_item['discussion']}"
            
        category = detect_category(title_zh, summary_zh, zh_item["source_line"])
        source_name = parse_source_name(zh_item["source_line"])
        
        # ISO timestamp
        publish_time = f"{date_str}T12:00:00Z"
        # If time is in source line (e.g. 14:30), parse it
        time_match = re.search(r'(\d{2}:\d{2})', zh_item["source_line"])
        if time_match:
            publish_time = f"{date_str}T{time_match.group(1)}:00Z"
            
        combined_articles.append({
            "id": str(article_id),
            "title": title_zh,
            "importance_score": zh_item["score"],
            "source": source_name,
            "url": url,
            "category": category,
            "publish_time": publish_time,
            "summary_zh": full_zh,
            "summary_en": full_en,
            "takeaways": takeaways
        })
        article_id += 1
        
    # Write output JSON
    os.makedirs(os.path.dirname(OUTPUT_JSON_PATH), exist_ok=True)
    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(combined_articles, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully compiled {len(combined_articles)} articles into {OUTPUT_JSON_PATH}!")
    print("Done!")

if __name__ == "__main__":
    main()
