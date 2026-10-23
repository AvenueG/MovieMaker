# MovieMaker：AI 短剧前期工作室

把一句话变成可以拍的竖屏短剧剧本：一句话 → 标签 → 概念抽卡 → 整季圣经 → 逐集大纲 → 剧本 → 审片打分 →（可选）分镜。每一步有脚本质量门和审片评分，默认每步停下等你确认。

## 怎么用

**在 claude.ai 这个项目里（推荐）**：直接用中文说要做什么，例如「接着写《你欠我一条命》第 3 集」「新开一部剧，一句话是……」。Claude 按 [AGENTS.md](AGENTS.md) 的规则和仓库里的 skill、agent 工作。

**在自己电脑上用 Claude Code**：把仓库克隆下来，在仓库根目录运行 `claude`，同样直接说中文。Claude Code 会自动读 `CLAUDE.md`（它引用 AGENTS.md）、`.claude/skills/` 和 `.claude/agents/`。

**网页短剧创作台**：`studio/studio.html`（已发布为 claude.ai 上的 Artifact）。可以导入 agent 写好的 `projects/<剧名>/<剧名>-项目.json` 查看和手改，改完导出发回来同步。网页里的修改只用网页自带的提示词，不会调用这里的 agent 和 skill。

## 目录

- `projects/`：每部剧一个文件夹，进度看各自的 `state.md`
- `.claude/skills/short-drama-preprod/`：写作方法、质量门 `check.py`、网页同步 `studio_sync.py`
- `.claude/agents/`：编剧、审片、分镜三个 agent
- `studio/`：网页创作台和质量门检查器
- `docs/context/`：当前进度、目录地图、操作手册、决定、风险
- `docs/research/`：开源方案调研和审片标准
- `samples/`：早期样片包（只作参考）
- `history/`：有价值的过程归档

文档入口：[PROJECT_INDEX.md](PROJECT_INDEX.md)。
