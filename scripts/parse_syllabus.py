#!/usr/bin/env python3
"""
Parse an English syllabus file (.txt or .md) and extract its chapter/section structure.
Designed for the uk-uni-tutor Skill's bilingual (Chinese user + English syllabus) workflow.

Usage:
  python parse_syllabus.py syllabus.txt              # print extracted structure to stdout
  python parse_syllabus.py syllabus.md --json         # output as JSON
  python parse_syllabus.py syllabus.txt --validate    # check if the file has detectable structure
  python parse_syllabus.py syllabus.md --bilingual    # output with Chinese labels for zh-mapping prep

The script detects common syllabus patterns:
  - Numbered chapters: "Chapter 1", "Ch. 1", "Week 1"
  - Markdown headings: "# Chapter Title", "## Section"
  - Numbered sections: "1.1 Title", "2.3.1 Title"
  - Keywords: "Definition", "Theorem", "Example", "Exercise", "Formula", "Method", "Algorithm"

Output is designed to be used as a starting point for manual refinement --
review and adjust the extracted structure before loading it into syllabus-driven tutoring mode.
The --bilingual flag adds Chinese labels to help build zh_mapping entries.
"""

import argparse
import json
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Chinese label mappings for --bilingual output
# ---------------------------------------------------------------------------

ZH_LABELS = {
    "chapter": "章节",
    "week": "第{num}周",
    "heading": "标题",
    "concept": "概念",
    "method": "方法",
    "example": "例题",
    "exercise": "练习",
    "definition": "定义",
    "theorem": "定理",
    "formula": "公式",
    "step": "步骤",
}

# Common math/programming term translations for quick reference
COMMON_ZH_TERMS: dict[str, str] = {
    "limit": "极限",
    "derivative": "导数",
    "integral": "积分",
    "function": "函数",
    "theorem": "定理",
    "equation": "方程",
    "probability": "概率",
    "distribution": "分布",
    "matrix": "矩阵",
    "vector": "向量",
    "sequence": "数列",
    "series": "级数",
    "chain rule": "链式法则",
    "power rule": "幂法则",
    "product rule": "乘积法则",
    "algorithm": "算法",
    "recursion": "递归",
    "iteration": "迭代",
    "complexity": "复杂度",
    "binary search": "二分查找",
    "linked list": "链表",
    "sorting": "排序",
    "graph": "图",
    "tree": "树",
    "hash table": "哈希表",
}


# ---------------------------------------------------------------------------
# Chapter/section detection
# ---------------------------------------------------------------------------

def detect_chapter_patterns(text: str) -> list[dict]:
    """Detect chapter/section boundaries using common English patterns."""
    chapters = []
    lines = text.split("\n")

    patterns = [
        # "Chapter 1: Title" or "Chapter 1 - Title" or "Ch. 1 Title"
        (r"^(?:Chapter|Ch\.?)\s*(\d+)\s*[:.\-]?\s*(.+)", "chapter"),
        # "Week 1: Title"
        (r"^Week\s*(\d+)\s*[:.\-]?\s*(.+)", "week"),
        # "Lecture 1: Title"
        (r"^Lecture\s*(\d+)\s*[:.\-]?\s*(.+)", "week"),
        # "# Chapter Title" or "## 1.1 Section Title" or "### Subsection" (markdown)
        (r"^(#{1,3})\s*(?:(\d+(?:\.\d+)*)\s*)?(.+)", "markdown_heading"),
    ]

    for i, line in enumerate(lines):
        line_stripped = line.strip()
        if not line_stripped:
            continue

        for pattern, ptype in patterns:
            m = re.match(pattern, line_stripped, re.IGNORECASE)
            if m:
                if ptype == "chapter":
                    chapters.append({
                        "type": "chapter",
                        "number": int(m.group(1)),
                        "title": m.group(2).strip(),
                        "line": i + 1,
                    })
                elif ptype == "week":
                    chapters.append({
                        "type": "week",
                        "number": int(m.group(1)),
                        "title": m.group(2).strip(),
                        "line": i + 1,
                    })
                elif ptype == "markdown_heading":
                    level = len(m.group(1))
                    num_str = m.group(2)
                    title = m.group(3).strip()
                    if level <= 2:
                        chapters.append({
                            "type": "heading",
                            "level": level,
                            "number": num_str,
                            "title": title,
                            "line": i + 1,
                        })
                break

    return chapters


# ---------------------------------------------------------------------------
# Keyword extraction
# ---------------------------------------------------------------------------

def extract_keywords(text: str) -> dict:
    """Extract Definition/Theorem/Example/Exercise/Formula keywords with line numbers."""
    keywords = {
        "definitions": [],
        "theorems": [],
        "examples": [],
        "exercises": [],
        "formulas": [],
    }

    patterns = {
        "definitions": r"(?:^|\n)[^\n]*\b(?:Definition|Def\.?)\s*\d*[.:]?\s*([^\n]+)",
        "theorems": r"(?:^|\n)[^\n]*\b(?:Theorem|Thm\.?|Lemma|Corollary|Proposition)\s*\d*[.:]?\s*([^\n]+)",
        "examples": r"(?:^|\n)[^\n]*\b(?:Example|Ex\.?)\s*\d*[.:]?\s*([^\n]+)",
        "exercises": r"(?:^|\n)[^\n]*\b(?:Exercise|Problem|Question|Q\d+)\s*\d*[.:]?\s*([^\n]+)",
        "formulas": r"(?:^|\n)[^\n]*\b(?:Formula|Equation|Eq\.?)\s*\d*[.:]?\s*([^\n]+)",
    }

    for key, pattern in patterns.items():
        for m in re.finditer(pattern, text, re.IGNORECASE):
            line_num = text[: m.start()].count("\n") + 1
            keywords[key].append({
                "line": line_num,
                "content": m.group(1).strip() if m.lastindex else m.group(0).strip(),
            })

    return keywords


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------

def compute_line_ranges(chapters: list[dict], total_lines: int) -> list[dict]:
    """Add line_range field to each chapter based on boundaries between sections."""
    for i, ch in enumerate(chapters):
        start = ch["line"]
        end = chapters[i + 1]["line"] - 1 if i + 1 < len(chapters) else total_lines
        ch["line_range"] = f"{start}-{end}"
    return chapters


def suggest_zh_terms(keywords: dict) -> list[dict]:
    """Suggest Chinese translations for detected English terms."""
    suggestions = []
    for category, items in keywords.items():
        for item in items:
            content_lower = item["content"].lower()
            for en, zh in COMMON_ZH_TERMS.items():
                if en in content_lower:
                    suggestions.append({
                        "english_term": en,
                        "zh_suggestion": zh,
                        "found_in": item["content"][:60],
                        "line": item["line"],
                    })
    # Deduplicate
    seen = set()
    unique = []
    for s in suggestions:
        key = (s["english_term"], s["zh_suggestion"])
        if key not in seen:
            seen.add(key)
            unique.append(s)
    return unique


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def format_bilingual(text: str) -> None:
    """Parse and print with Chinese labels for easier zh_mapping construction."""
    chapters = detect_chapter_patterns(text)
    lines = text.split("\n")
    total_lines = len(lines)
    chapters = compute_line_ranges(chapters, total_lines)
    kw = extract_keywords(text)
    zh_suggestions = suggest_zh_terms(kw)

    _safe_print("=== Syllabus Parse (Bilingual Mode / 双语模式) ===\n")
    _safe_print(f"Total lines / 总行数: {total_lines}")
    _safe_print(f"Chapters detected / 检测到的章节: {len(chapters)}\n")

    for ch in chapters:
        lr = ch.get("line_range", "?")
        num = ch.get("number", "?")
        title = ch.get("title", "(untitled)")
        ptype = ch["type"]
        if ptype == "week":
            _safe_print(f"  [Line {lr}] Week {num}: '{title}'")
        elif ptype == "chapter":
            _safe_print(f"  [Line {lr}] Chapter {num}: '{title}'")
        else:
            _safe_print(f"  [Line {lr}] [{ptype}] '{title}'")

    _safe_print(f"\n--- Keyword Summary / 关键词摘要 ---")
    zh_cat = {
        "definitions": "Definitions / 定义",
        "theorems": "Theorems / 定理",
        "examples": "Examples / 例题",
        "exercises": "Exercises / 练习",
        "formulas": "Formulas / 公式",
    }
    for key, label in zh_cat.items():
        items = kw.get(key, [])
        if items:
            _safe_print(f"  [{label}]: {len(items)} found")
            for item in items[:3]:
                _safe_print(f"    Line {item['line']}: {item['content'][:80]}")
            if len(items) > 3:
                _safe_print(f"    ... and {len(items) - 3} more")

    if zh_suggestions:
        _safe_print(f"\n--- Zh-Mapping Suggestions (add to zh_mapping in syllabus_index.json) ---")
        for s in zh_suggestions:
            _safe_print(f'  "{s["zh_suggestion"]}": "{s["english_term"]}",   # found in: {s["found_in"]}')

    _safe_print(f"\n--- Next Steps / 后续步骤 ---")
    _safe_print(f"  1. Review the extracted structure above")
    _safe_print(f"  2. Add zh_mapping entries for key terms in syllabus_index.json")
    _safe_print(f"  3. Re-run with --json to get machine-readable output")
    _safe_print(f"  4. Load the refined index with @load-syllabus")


def format_plain(text: str, filepath: Path) -> None:
    """Standard English output format."""
    chapters = detect_chapter_patterns(text)
    lines = text.split("\n")
    total_lines = len(lines)
    chapters = compute_line_ranges(chapters, total_lines)
    kw = extract_keywords(text)

    print(f"=== Syllabus Parse: {filepath.name} ===\n")
    print(f"Total lines: {total_lines}")
    print(f"Chapters/Sections detected: {len(chapters)}\n")

    for ch in chapters:
        num = ch.get("number", "?")
        title = ch.get("title", "(untitled)")
        lr = ch.get("line_range", "?")
        print(f"  [Line {lr}] Ch.{num}: {title}")

    print(f"\n--- Keyword Summary ---")
    for key, items in kw.items():
        if items:
            print(f"  {key}: {len(items)} found")
            for item in items[:3]:
                print(f"    Line {item['line']}: {item['content'][:80]}")
            if len(items) > 3:
                print(f"    ... and {len(items) - 3} more")

    print(f"\n--- Next Steps ---")
    print(f"  1. Review the extracted structure above.")
    print(f"  2. Re-run with --json to get machine-readable output.")
    print(f"  3. Manually refine the JSON into references/syllabus_index.json.")
    print(f"  4. Load the refined index with @load-syllabus.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _safe_print(*args, **kwargs):
    """Print with encoding-safe fallback for Windows GBK terminals."""
    try:
        print(*args, **kwargs)
    except UnicodeEncodeError:
        # Fallback: replace non-ASCII chars
        safe_args = []
        for a in args:
            if isinstance(a, str):
                safe_args.append(a.encode('ascii', errors='replace').decode('ascii'))
            else:
                safe_args.append(a)
        print(*safe_args, **kwargs)


def main():
    # Attempt to reconfigure stdout for UTF-8; fall back gracefully on Windows
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

    parser = argparse.ArgumentParser(
        description="Parse an English syllabus file and extract its chapter/keyword structure."
    )
    parser.add_argument("file", type=str, help="Path to syllabus file (.txt or .md)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--validate", action="store_true", help="Only validate structure, no full parse")
    parser.add_argument("--bilingual", action="store_true",
                        help="Output with Chinese labels for zh_mapping construction")
    args = parser.parse_args()

    filepath = Path(args.file)
    if not filepath.exists():
        print(f"[!] File not found / 文件未找到: {args.file}", file=sys.stderr)
        sys.exit(1)

    text = filepath.read_text(encoding="utf-8")
    lines = text.split("\n")
    total_lines = len(lines)

    chapters = detect_chapter_patterns(text)
    chapters = compute_line_ranges(chapters, total_lines)

    if args.validate:
        if chapters:
            print(f"[OK] Detected {len(chapters)} chapter(s)/section(s):")
            for ch in chapters:
                chtype = ch["type"]
                title = ch.get("title", "")
                print(f"  Line {ch['line']}: [{chtype}] {title}")
        else:
            print("[WARN] No chapter/section patterns detected.")
            print("       Expected patterns: 'Chapter N', 'Week N', '# Heading'")
        print(f"\nTotal lines: {total_lines}")
        return

    if args.bilingual:
        format_bilingual(text)
        return

    kw = extract_keywords(text)
    result = {
        "file": str(filepath.resolve()),
        "total_lines": total_lines,
        "chapters": chapters,
        "keyword_counts": {k: len(v) for k, v in kw.items()},
        "keywords": kw,
    }

    if args.json:
        suggestions = suggest_zh_terms(kw)
        if suggestions:
            result["zh_mapping_suggestions"] = suggestions
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        format_plain(text, filepath)


if __name__ == "__main__":
    main()
