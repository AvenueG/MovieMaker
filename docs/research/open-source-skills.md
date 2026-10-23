# 可借鉴 / 可直接安装的开源短剧 skill（2026-10-22 调研）

| Skill | 许可证 | 适合 | 我借鉴进新流程的做法 |
|---|---|---|---|
| [OnlyShot](https://github.com/A-cat-with-carrots/OnlyShot) | MIT | Claude Code，五步出片，集成即梦 / Seedance | 先出便宜的分镜图、确认后再出贵的视频；分段 prompt 模板（角色 / 背景 / 动作 / 镜头 / 光线 / 风格）加字数上限；镜头时长 4–10 秒变奏；敏感词替换表；先试跑几段 |
| [drama-skills](https://github.com/zenstory-ai/drama-skills) | MIT | Claude Code / Codex，10 个分工 skill，可只装需要的 | 每集只维护少量 Markdown 文件；长剧逐集处理、可断点续做；只给关键场次做导演设计，普通场次跳过；参考图、关键帧、视频提示词分开写 |
| [Hao0321/ai-short-drama](https://github.com/Hao0321/ai-short-drama) | MIT | Codex / Claude Code，从选题到制作包 | 概念阶段先做 8 维立项评分；设定圣经含能力代价和反派升级阶梯；每集记录「主转折、爽点、集尾钩子、状态变化」；固定角色 ID 保证跨集一致 |
| [suihe1/short-drama-production](https://github.com/suihe1/short-drama-production) | Apache-2.0 | Codex，带状态机和审批 | 上游一改，下游自动标记「需重审」；戏剧意图和技术执行分层；先做样片，通过再批量 |

**安装方法（Claude Code）**：把仓库克隆到 `~/.claude/skills/` 或项目的 `.claude/skills/` 目录下即可，例如 `git clone https://github.com/zenstory-ai/drama-skills ~/.claude/skills/drama-skills`。安装前建议先看一遍仓库里的 SKILL.md 和脚本。

**其他值得关注**：[higgsfield-ai-prompt-skill](https://github.com/OSideMedia/higgsfield-ai-prompt-skill)（电影感视频提示词）、[story-shot-agent](https://github.com/neopen/story-shot-agent)（剧本转逐镜提示词并保持角色一致）、[OpenMontage](https://github.com/calesthio/OpenMontage)（以后有 API key 时做全自动出片）。
