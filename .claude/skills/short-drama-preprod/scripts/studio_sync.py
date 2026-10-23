#!/usr/bin/env python3
"""项目文件夹 ⇄ 网页「短剧创作台」项目文件（.json）
  python3 studio_sync.py to-studio   <项目目录> <输出.json>
  python3 studio_sync.py from-studio <项目.json> <项目目录>   # 覆盖前把旧文件备份到 <项目目录>/_imports/<时间>/
"""
import json, os, re, shutil, sys, time

EPF = {"outline": "outline.md", "script": "script.md", "shots": "shots.csv"}

def read(p):
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""

def concept_for_page(text):
    # 1-concept.md 用「# 选定概念 / ## 片名」，网页用「# 片名」
    text = re.sub(r"^#\s*选定概念\s*\n+", "", text)
    return re.sub(r"^##\s+", "# ", text, count=1)

def to_studio(d, out):
    state = read(os.path.join(d, "state.md"))
    m = re.search(r"类型：(.+?)｜共\s*(\d+)\s*集｜每集\s*(\d+)\s*秒｜(9:16|16:9)", state)
    genre, n, secs, aspect = (m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)) if m else ("AI 甜宠短剧", 1, 60, "9:16")
    concept = concept_for_page(read(os.path.join(d, "1-concept.md")))
    idea = read(os.path.join(d, "0-idea.md")).strip() or (re.search(r"一句话故事：(.+)", concept) or [None, ""])[1]
    eps = {}
    for k in range(1, n + 1):
        e = {f: read(os.path.join(d, f"E{k:02d}", name)) for f, name in EPF.items()}
        if any(e.values()): eps[str(k)] = e
    title = (re.search(r"^#\s*(.+)", concept, re.M) or [None, os.path.basename(d.rstrip("/"))])[1].strip()
    data = {"format": "short-drama-studio", "version": 1, "title": title, "idea": idea, "genre": genre, "secs": secs, "aspect": aspect,
            "nEps": n, "concept": concept, "season": read(os.path.join(d, "2-season.md")), "eps": eps}
    json.dump(data, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"已导出「{title}」：{len(eps)} 集有内容 → {out}")

def from_studio(src, d):
    j = json.load(open(src, encoding="utf-8"))
    if j.get("format") != "short-drama-studio": sys.exit("这不是短剧创作台的项目文件")
    bak = os.path.join(d, "_imports", time.strftime("%Y%m%d-%H%M%S"))
    changed = []
    def put(rel, text):
        if not text: return
        p = os.path.join(d, rel)
        if read(p) == text or (rel == "1-concept.md" and concept_for_page(read(p)) == text): return
        if os.path.exists(p):
            os.makedirs(os.path.dirname(os.path.join(bak, rel)), exist_ok=True); shutil.copy2(p, os.path.join(bak, rel))
        os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "w", encoding="utf-8").write(text); changed.append(rel)
    put("0-idea.md", j.get("idea", "") + "\n" if j.get("idea") else "")
    put("1-concept.md", j.get("concept", ""))
    put("2-season.md", j.get("season", ""))
    for k, e in (j.get("eps") or {}).items():
        for f, name in EPF.items(): put(f"E{int(k):02d}/{name}", e.get(f, ""))
    print("改动：" + ("、".join(changed) if changed else "无") + (f"\n旧文件备份在 {bak}" if changed and os.path.isdir(bak) else ""))

if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in ("to-studio", "from-studio"): sys.exit(__doc__)
    (to_studio if sys.argv[1] == "to-studio" else from_studio)(sys.argv[2], sys.argv[3])
