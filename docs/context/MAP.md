# MAP

## 目录

| 位置 | 内容 | 备注 |
|---|---|---|
| `projects/<剧名>/` | 一部剧的全部文件：`0-idea.md` `0-tags.md` `1-concept.md` `1-deck.md` `2-season.md` `state.md` `E0n/{outline.md,script.md,review.md,shots.csv}` | 文件格式见 SKILL.md「项目目录」 |
| `projects/<剧名>/<剧名>-项目.json` | 给网页创作台导入的导出文件 | 由 `studio_sync.py to-studio` 生成，是派生物，不手改 |
| `projects/<剧名>/_废稿-*/` `E0n/v1/` `E0n/_unused/` | 作废或旧版本 | 默认不读 |
| `.claude/skills/short-drama-preprod/` | `SKILL.md` 方法；`scripts/check.py` 质量门；`scripts/studio_sync.py` 网页互导 | skill 的唯一权威副本 |
| `.claude/agents/` | `screenwriter.md` `reviewer.md` `storyboarder.md` | |
| `studio/studio.html` | 网页短剧创作台源码 | 已发布：https://claude.ai/artifact/Q3VFc8tCdBaS6dRWpUYQgk |
| `studio/input-desk.html` | 灵感输入台 v3：测口味（16 张卡点喜欢/跳过）→ 捏人 → 世界和规则 → 名场面（点选拼出 + 调味按钮 + 点台词自己改）→ 作品集（盖章、统计、导出项目卡） | 已发布：https://claude.ai/artifact/Ur2115ETGpu3yoPpXvB7mK（第 3 版）；切片质量门（12–35 秒、钩子、停在顶点、15 字/句）和 check.py 切片模式一致；作者改过的台词标记为亲手写，调味时保留原文 |
| `studio/gate-checker.html` | 网页版质量门检查器 | 已发布：https://claude.ai/artifact/NPTzXxFaCFgMEB2z7NtxgN |
| `docs/research/` | 开源方案调研、开源 skill 调研、前期工具调研、三套审片标准 | 只作参考 |
| `samples/` | 早期样片包 | 见下 |

## 样片

| 目录 | 内容 |
|---|---|
| `samples/最后一碗/` | 新加坡小贩中心短片的完整前期包；`review-viewer.html` 是交互审片页（已发布：https://claude.ai/artifact/7iW44bHUpeG9YPcCAPSXyC） |
| `samples/无契之人-ep1/` | 用户原创 IP《THE UNBOUND 无契之人》5 分钟试播集，70 镜 |
| `samples/你欠我一条命-网页试跑E01/` | 用网页提示词试跑的 E01，审片 77；`report.md` 是试跑报告 |

## 同步边界

- **三处质量门阈值必须一致**：`check.py`、`studio/gate-checker.html`、`studio/studio.html`（搜索 `gatesScript` `gatesShots`）。
- **网页 ↔ 仓库**：网页数据存在用户浏览器里（localStorage），仓库看不到。只能通过「导出项目文件 / 导入项目」的 json 交换，见 RUNBOOK。
- **改了 `studio/*.html`** 后要在 claude.ai 重新发布到同一个 Artifact 链接，否则网页还是旧版。
- **claude.ai 项目文件夹**里的 `ai-short-film/` 是本仓库建立前的旧副本（2026-10-23 搬入本仓库）。以后以仓库为准；给用户看的文件可以同时复制一份到那里。
- 早期的 `tools/check.py` 和 `tools/short-drama-preprod.SKILL.md` 是旧副本，没有搬进仓库，以 `.claude/skills/short-drama-preprod/` 为准。
