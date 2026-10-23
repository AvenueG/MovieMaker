#!/usr/bin/env python3
"""短剧前期质量门：python3 check.py script <3-script.md>  |  python3 check.py shots <3-script.md> <4-shots.csv>"""
import csv, re, sys

CPS, ACT_SEC, LINE_MAX, GAP_MAX, TOL = 4.5, 2.5, 35, 20, 0.15
CLIP_LINE_MAX = 15  # 切片模式（# C01 …）单句上限，按行业标准
CUT_MIN, CUT_MAX, PEOPLE_MAX = 2, 8, 3
SIZES = ["大远景", "远景", "大全景", "全景", "中全景", "中景", "中近景", "近景", "特写", "大特写"]

def parse_script(path):
    ep = {"target": None, "cast": set(), "beats": [], "clip": False}
    scene = None
    for raw in open(path, encoding="utf-8"):
        s = raw.strip()
        m = re.match(r"#\s*([EC])\d+.*?目标\s*(\d+)\s*秒", s)
        if m: ep["target"], ep["clip"] = int(m.group(2)), m.group(1) == "C"; continue
        m = re.match(r"##\s*(S\d+).*?人物[:：](.*)$", s)
        if m:
            scene = m.group(1); ep["cast"] |= {x.strip() for x in re.split(r"[,，、]", m.group(2)) if x.strip()}; continue
        m = re.match(r"(\d+)\.\s*\[(动作|台词)\]\s*(.*)$", s)
        if not m: continue
        n, kind, body = int(m.group(1)), m.group(2), m.group(3)
        tags = set(re.findall(r"#(钩子|爽点|甜点|反转|悬念)", body))
        body = re.sub(r"\s*#\S+", "", body).strip()
        b = {"n": n, "kind": kind, "scene": scene, "tags": tags}
        if kind == "台词":
            parts = [p.strip() for p in body.split("｜")]
            b["speaker"], b["line"] = parts[0], parts[-1]
            b["sec"] = max(1.0, len(re.sub(r"[，。！？…、,.!?\s]", "", b["line"])) / CPS)
        else:
            b["text"], b["sec"] = body, ACT_SEC
        ep["beats"].append(b)
    return ep

def gates_script(ep):
    errs, beats = [], ep["beats"]
    if not ep["target"]: errs.append("缺少「# E01 … 目标 N 秒」标题")
    if not beats: return errs + ["没有解析到任何节拍"], 0
    if [b["n"] for b in beats] != list(range(1, len(beats) + 1)): errs.append("节拍编号不连续")
    total = sum(b["sec"] for b in beats)
    if ep["target"] and abs(total - ep["target"]) > ep["target"] * TOL:
        errs.append(f"估算时长 {total:.0f}s，偏离目标 {ep['target']}s ±{int(TOL*100)}%")
    if not any("钩子" in b["tags"] for b in beats[:3]): errs.append("前 3 拍内没有 #钩子")
    if ep["clip"]:
        if not beats[-1]["tags"] & {"悬念", "甜点", "爽点"}: errs.append("切片最后一拍要停在 #甜点、#爽点 或 #悬念")
    elif "悬念" not in beats[-1]["tags"]: errs.append("最后一拍没有 #悬念")
    line_max = CLIP_LINE_MAX if ep["clip"] else LINE_MAX
    for b in beats:
        if b["kind"] == "台词":
            if len(b["line"]) > line_max: errs.append(f"第 {b['n']} 拍台词超过 {line_max} 字")
            sp = b["speaker"].replace("（内心）", "").replace("(内心)", "")
            if sp not in ep["cast"] and sp not in ("旁白", "VO", "广播") and not sp.startswith("旁白"):
                errs.append(f"第 {b['n']} 拍说话人「{b['speaker']}」不在场次人物表里")
        elif "“" in b["text"]:
            errs.append(f"第 {b['n']} 拍动作里混了台词")
    for sc in sorted({b["scene"] for b in beats}):
        if not any(b["kind"] == "动作" for b in beats if b["scene"] == sc): errs.append(f"{sc} 没有动作节拍（纯对白场）")
    t, last = 0.0, 0.0
    for b in beats:
        if b["tags"] & {"钩子", "爽点", "甜点", "反转", "悬念"}:
            if t - last > GAP_MAX: errs.append(f"{last:.0f}s–{t:.0f}s 之间 {t-last:.0f}s 没有爽点 / 甜点 / 反转")
            last = t
        t += b["sec"]
    return errs, total

def gates_shots(ep, path):
    errs, rows = [], list(csv.DictReader(open(path, encoding="utf-8")))
    covered, total = [], 0.0
    names = {c for c in ep["cast"] if len(c) >= 2}
    by_n = {b["n"]: b for b in ep["beats"]}
    for r in rows:
        sid = r.get("shot", "?")
        a, _, z = r["beats"].partition("-"); a = int(a); z = int(z or a)
        rng = list(range(a, z + 1)); covered += rng
        if len({by_n[n]["scene"] for n in rng if n in by_n}) > 1: errs.append(f"镜 {sid} 跨场次")
        d = float(r["dur"]); total += d
        if not CUT_MIN <= d <= CUT_MAX: errs.append(f"镜 {sid} 时长 {d}s 不在 {CUT_MIN}–{CUT_MAX}s")
        need = sum(by_n[n]["sec"] for n in rng if n in by_n and by_n[n]["kind"] == "台词")
        if need > d: errs.append(f"镜 {sid} 台词约需 {need:.1f}s，镜头只有 {d}s")
        if not any(s in r["frame_cn"] for s in SIZES): errs.append(f"镜 {sid} 首帧提示词缺景别词")
        hit = [n for n in names if n in r["video_cn"]]
        if hit: errs.append(f"镜 {sid} 视频提示词出现角色名 {hit}，改用通用身份")
        if int(r.get("people") or 0) > PEOPLE_MAX: errs.append(f"镜 {sid} 同框超过 {PEOPLE_MAX} 人")
        for f in ("lens", "camera_pos", "composition", "eyeline"):
            if not r.get(f, "").strip(): errs.append(f"镜 {sid} 缺构图字段 {f}")
    if covered != list(range(1, len(ep["beats"]) + 1)): errs.append("镜头没有按顺序、不重不漏地覆盖全部节拍")
    if ep["target"] and abs(total - ep["target"]) > ep["target"] * TOL:
        errs.append(f"分镜总时长 {total:.0f}s，偏离目标 {ep['target']}s ±{int(TOL*100)}%")
    return errs, total

if __name__ == "__main__":
    mode, sp = sys.argv[1], sys.argv[2]
    ep = parse_script(sp)
    errs, total = gates_script(ep) if mode == "script" else gates_shots(ep, sys.argv[3])
    print(f"{'剧本' if mode == 'script' else '分镜'}：{len(ep['beats'])} 拍，约 {total:.0f} 秒")
    print("\n".join("✗ " + e for e in errs) if errs else "✓ 全部质量门通过")
    sys.exit(1 if errs else 0)
