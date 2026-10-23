# 概念 → 大纲 → 剧本 → 分镜：开源工具推荐（2026-10-22）

> 只覆盖前期四段。Star 数为调研当天页面数据。所有工具都还没有部署，等你确认。

## 推荐组合

**编剧方法用 screenwriting-skills，分镜用 shuohao-skills 的分镜模块，由 short-drama-studio 负责逐级把关。**
前者让概念、大纲、剧本的质量有专业方法论支撑；后者是目前唯一带脚本化质量关卡的开源分镜流程；我们自己的流程负责“上一步确认了才做下一步”，控制 token。

## 按阶段

| 阶段 | 首选 | 备选 |
|---|---|---|
| 概念 / 一句话 | screenwriting-skills：`sw-premise-theme`（logline 测试）、`sw-industry-business`（pitch） | Hao0321/ai-short-drama 的 8 维立项评分（已吸收进 short-drama-studio） |
| 大纲 | screenwriting-skills：`sw-story-structure`（Save the Cat、九节拍）、`sw-series-structure`（试播集节拍表）、`sw-chinese-series-practice`（分集大纲） | shuohao-skills `novel-outline`（偏小说改编） |
| 剧本 | screenwriting-skills：`sw-dialogue`、`sw-scene-craft`、`sw-character-conflict` | drama-skills `short-drama-write`；shuohao-skills `novel-script`（带每集时长估算和角色台词本） |
| 分镜 | shuohao-skills：`novel-staging`（站位）+ `novel-storyboard`（分段、切镜、关键帧，18 项质量检查） | seedance-storyboard（按 15 秒切 3–5 镜，适合 Seedance）；drama-skills `short-drama-storyboard` |

## 工具详情

| 工具 | Star | 许可证 | 说明 | 注意 |
|---|---|---|---|---|
| [shuohao-skills](https://github.com/eternityspring/shuohao-skills) | 4.9k | Apache-2.0 | 中文短剧 skill 集：大纲、角色、场景道具、剧本、站位、分镜，每步有脚本检查的质量关卡（大纲 14 项、剧本 10 项、分镜 18 项） | 以小说改编为主，原创 IP 需要先写一个“故事底稿”喂给它；需要 Node 18+；作者只在 macOS 上测过 |
| [screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills) | 1.7k | MIT | 26 个编剧方法论 skill（Field、Snyder、McKee、Truby 等，含中国剧集和韩日编剧传统），正文中文 | 偏方法论，不直接产出分镜；按需调用单个 skill 更省 token |
| [drama-skills](https://github.com/zenstory-ai/drama-skills) | 未记录 | MIT | 10 个分工 skill，可只装 develop、write、storyboard 三个 | 和 shuohao 功能重叠，二选一即可 |
| [seedance-storyboard](https://github.com/cclank/lanshu-awesome-ai-video-kit) | 未记录 | MIT | 把剧本切成适配 Seedance 15 秒上限的镜头组，含常见错误检查表 | 只管分镜，适合以后用即梦 / Seedance 出片时再装 |
| [screen-creative-skills](https://github.com/GongLingRui/screen-creative-skills) | 393 | MIT | 31 个 skill，强在故事分析和剧本评估（script-evaluator、ip-evaluator） | 没有分镜；适合做评审补充 |

## 部署方式

- **在你自己的 Claude Code 里**（推荐）：
  - screenwriting-skills：`/plugin marketplace add jtydhr88/screenwriting-skills`，然后 `/plugin install screenwriting@screenwriting-skills`
  - shuohao-skills：克隆仓库后运行它自带的安装脚本（会自动识别 Claude Code）
- **在这个项目里由我来用**：我把选中 skill 的核心方法读一遍，合并进 short-drama-studio，通过技能卡片给你保存。好处是只有一个技能、不重复加载，更省 token。

## 来源

[shuohao-skills](https://github.com/eternityspring/shuohao-skills) · [screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills) · [drama-skills](https://github.com/zenstory-ai/drama-skills) · [lanshu-awesome-ai-video-kit](https://github.com/cclank/lanshu-awesome-ai-video-kit) · [screen-creative-skills](https://github.com/GongLingRui/screen-creative-skills) · [Micro-Drama-Skills](https://github.com/zhaihao118/Micro-Drama-Skills)（需要 Gemini API，暂不推荐）
