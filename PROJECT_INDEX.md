# PROJECT_INDEX

**定位**：MovieMaker 是 nebula 的 AI 短剧前期工作室：从一句话到整季、逐集大纲和剧本（可选分镜），用 Claude Code 的 skill 和分工 agent 写作，用网页「短剧创作台」查看和手改。不含出图、出视频、配音和剪辑（用户没有生成类 API key）。

**当前摘要**（详情见 [NOW.md](docs/context/NOW.md)）：两部剧在做。《你欠我一条命》E01、E02 剧本待确认；《一口变凡人》等用户提供原概念。

## 任务 → 读哪里

这是按需路由，不是必读清单。

| 要做的事 | 先读 | 需要时再读 |
|---|---|---|
| 接着上次的进度 | [NOW.md](docs/context/NOW.md) | 对应剧的 `projects/<剧名>/state.md` |
| 写或改某部剧的某一阶段 | `projects/<剧名>/state.md` | [SKILL.md](.claude/skills/short-drama-preprod/SKILL.md) 对应阶段一节；`2-season.md` 的人物表和分集行 |
| 新开一部剧 | [SKILL.md](.claude/skills/short-drama-preprod/SKILL.md) 阶段 0–1；[RUNBOOK](docs/context/RUNBOOK.md)「新开一部剧」 | |
| 调用 agent 写一集 / 审片 | [RUNBOOK](docs/context/RUNBOOK.md)「用 agent 写一集」 | `.claude/agents/<名字>.md` |
| 跑质量门 | [RUNBOOK](docs/context/RUNBOOK.md)「质量门」 | `check.py` 里对应的 `gates_*` 函数 |
| 和网页创作台互导 | [RUNBOOK](docs/context/RUNBOOK.md)「和网页互通」 | `studio_sync.py` |
| 改网页创作台或检查器 | [MAP.md](docs/context/MAP.md)「网页工具」 | `studio/studio.html` 里相关函数（用搜索定位） |
| 改质量门阈值 | [DECISIONS.md](docs/context/DECISIONS.md)「质量门」 | 三处同步，见 MAP |
| 审片标准 | SKILL.md「审片打分」一节 | [review-rubrics.md](docs/research/review-rubrics.md)（广告片、电影节标准） |
| 为什么这样做、能不能换做法 | [DECISIONS.md](docs/context/DECISIONS.md) | [docs/research/](docs/research/) |
| 已知问题和风险 | [RISKS.md](docs/context/RISKS.md) | |
| 追溯以前做过什么 | [history/README.md](history/README.md)（先搜索） | |
| 参考旧样片 | [MAP.md](docs/context/MAP.md)「样片」 | `samples/` |
