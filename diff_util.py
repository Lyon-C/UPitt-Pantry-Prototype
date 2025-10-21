from typing import Dict, List, Tuple

def parse_model_markdown(md: str) -> Dict[str, int]:
    result = {}
    for line in md.splitlines():
        line = line.strip().lstrip("-").strip()
        if ":" in line:
            name, count = line.split(":", 1)
            try:
                cnt = int(count.strip().split()[0])
                result[name.strip()] = cnt
            except:
                continue
    return result

def diff_counts(old: Dict[str, int], new: Dict[str, int]) -> Tuple[List[str], List[str], List[str]]:
    added = []
    removed = []
    changed = []
    for item, cnt_new in new.items():
        cnt_old = old.get(item, 0)
        if cnt_old == 0:
            added.append(item)
        elif cnt_new != cnt_old:
            changed.append(f"{item} ({cnt_old} → {cnt_new})")
    for item in old:
        if item not in new:
            removed.append(item)
    return added, removed, changed

def format_diff_md(new: Dict[str, int], added: List[str], removed: List[str], changed: List[str]) -> str:
    md = "# Shelf Report\n\n"
    md += "## Currently on shelf:\n"
    for item, cnt in new.items():
        md += f"- **{item}**: {cnt}\n"
    md += "\n## Changes since baseline:\n"
    if removed:
        md += "- Removed: " + ", ".join(removed) + "\n"
    if added:
        md += "- Added: " + ", ".join(added) + "\n"
    if changed:
        md += "- Changed: " + ", ".join(changed) + "\n"
    return md
