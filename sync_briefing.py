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
                    summary_lines.append("")
                continue
                
            # Check for source line (contains U+00B7 middle dot separator ' · ')
            if " · " in line_str and not line_str.startswith("**") and not line_str.startswith("-"):
                source_line = line_str
                in_summary = False
                continue
                
            # Check for Background section
            bg_match = re.match(r'^\*\*(?:Background|背景|背景信息)\*\*:\s*(.*)', line_str, re.IGNORECASE)
            if bg_match:
                background = bg_match.group(1).strip()
                in_summary = False
                continue
                
            # Check for Discussion section
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
    """Extracts a neat source name from a source line."""
    if not source_line:
        return "Horizon"
    parts = [p.strip() for p in source_line.split("·")]
    if len(parts) >= 2:
        first = parts[0].lower()
        if first in ["rss", "github", "reddit"] and parts[1]:
            return parts[1]
        return parts[0].capitalize()
    return parts[0]

def create_fallback_mock_data():
    today_str = datetime.date.today().isoformat()
    return [
      {
        "id": "1",
        "title": "OpenAI 发布 GPT-5 模型与原生 Agent 系统",
        "importance_score": 9.9,
        "source": "OpenAI Blog",
        "url": "https://openai.com",
        "category": "AI",
        "publish_time": f"{today_str}T16:00:00Z",
        "summary_zh": "OpenAI 正式发布了其下一代大模型 GPT-5。该模型在逻辑推理和多步骤自主执行（Agent）层面实现了飞跃。\n\n**背景**: GPT-5 解决了大语言模型无法自主进行深度思考的顽疾。\n\n**社区讨论**: 网友普遍对于其自主执行代码的能力感到兴奋，但也有安全担忧。",
        "summary_en": "OpenAI officially unveiled GPT-5, showing massive improvements in reasoning and autonomous agent planning.\n\n**Background**: GPT-5 addresses the limitations of previous models in deep multi-step planning.\n\n**Discussion**: Users are generally excited about local-first execution, though safety is still debated.",
        "takeaways": [
          "背景信息: GPT-5 解决了大语言模型无法自主进行深度思考的顽疾。",
          "社区反馈: 网友普遍对于其自主执行代码的能力感到兴奋，但也有安全担忧。"
        ]
      },
      {
        "id": "2",
        "title": "Vite 7.0 正式版发布：基于 Rust 的全新构建内核",
        "importance_score": 8.9,
        "source": "Vite",
        "url": "https://vite.dev",
        "category": "Dev",
        "publish_time": f"{today_str}T14:30:00Z",
        "summary_zh": "Vite 7.0 默认采用 Rust 编写的打包器 Rolldown，编译和热更新速度提升高达 5 倍。\n\n**背景**: Rolldown 是 Vue 团队为了替代 Rollup 编写的 Rust 移植版本。",
        "summary_en": "Vite 7.0 now uses Rust-based bundler Rolldown by default, achieving up to 5x faster hot reload times.\n\n**Background**: Rolldown is the Rust rewrite of Rollup initiated by the Vue core team.",
        "takeaways": [
          "背景信息: Rolldown 是 Vue 团队为了替代 Rollup 编写的 Rust 移植版本。"
        ]
      }
    ]

def main():
    print("=" * 60)
    print("           TODAY TECH TOP 20 - HORIZON INTEGRATION           ")
    print("=" * 60)
    
    os.makedirs(SUMMARIES_DIR, exist_ok=True)
    
    files_in_dir = os.listdir(SUMMARIES_DIR)
    zh_files = [f for f in files_in_dir if (f.startswith("horizon-") and f.endswith("-zh.md")) or f.endswith("-summary-zh.md")]
    
    # Sort files in descending order (newest first)
    zh_files.sort(reverse=True)
    
    combined_articles = []
    seen_urls = set()
    article_id = 1
    
    print(f"Found {len(zh_files)} summary markdown files.")
    
    for latest_zh_filename in zh_files:
        if latest_zh_filename.startswith("horizon-"):
            date_str = latest_zh_filename[8:18]
            latest_en_filename = f"horizon-{date_str}-en.md"
        else:
            date_str = latest_zh_filename[:10]
            latest_en_filename = f"{date_str}-summary-en.md"
            
        zh_filepath = os.path.join(SUMMARIES_DIR, latest_zh_filename)
        en_filepath = os.path.join(SUMMARIES_DIR, latest_en_filename)
        
        zh_items = parse_horizon_markdown(zh_filepath)
        en_items = parse_horizon_markdown(en_filepath)
        en_by_url = {item["url"]: item for item in en_items}
        
        for zh_item in zh_items:
            url = zh_item["url"]
            if url in seen_urls:
                continue
            seen_urls.add(url)
            
            en_item = en_by_url.get(url, None)
            
            title_zh = zh_item["title"]
            summary_zh = zh_item["summary"]
            summary_en = en_item["summary"] if en_item else summary_zh
            
            takeaways = []
            if zh_item["background"]:
                takeaways.append(f"背景信息: {zh_item['background']}")
            if zh_item["discussion"]:
                takeaways.append(f"社区反馈: {zh_item['discussion']}")
                
            if not takeaways:
                sentences = [s.strip() for s in re.split(r'[。！；!?;]', summary_zh) if s.strip()]
                takeaways = sentences[:3]
                
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
            
            publish_time = f"{date_str}T12:00:00Z"
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
            
        # Stop collecting if we reached 20 items
        if len(combined_articles) >= 20:
            break

    # Guard against empty list: fallback to existing news.json or fallback mock data
    if not combined_articles:
        print("Warning: No articles could be extracted from markdown files.")
        if os.path.exists(OUTPUT_JSON_PATH):
            try:
                with open(OUTPUT_JSON_PATH, "r", encoding="utf-8") as f:
                    old_data = json.load(f)
                if old_data and isinstance(old_data, list) and len(old_data) > 0:
                    print("Preserving existing news.json data.")
                    combined_articles = old_data
            except Exception as e:
                pass
                
        if not combined_articles:
            print("Generating fallback mock data...")
            combined_articles = create_fallback_mock_data()

    os.makedirs(os.path.dirname(OUTPUT_JSON_PATH), exist_ok=True)
    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(combined_articles, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully compiled {len(combined_articles)} articles into {OUTPUT_JSON_PATH}!")
    print("Done!")

if __name__ == "__main__":
    main()
