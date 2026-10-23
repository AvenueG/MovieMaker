# RUNBOOK

命令都在仓库根目录运行。写在这里不等于已经执行过，也不构成执行授权。

## 质量门

```
python3 .claude/skills/short-drama-preprod/scripts/check.py script projects/<剧名>/E01/script.md
python3 .claude/skills/short-drama-preprod/scripts/check.py shots projects/<剧名>/E01/script.md projects/<剧名>/E01/shots.csv
```

最后一行是「✓ 全部质量门通过」才算过；有 ✗ 就逐条修。2026-10-23 在《你欠我一条命》E01 剧本和 E02 分镜上验证可用。

## 新开一部剧

1. 建 `projects/<剧名>/0-idea.md`（用户的一句话，原样保存）和 `state.md`（格式照抄已有剧的 state.md）。
2. 用户给了灵感输入台的项目卡：原样存成 `0-项目卡.md`，按 SKILL.md「模块交接」从人设块开始，不再走阶段 0–1。
3. 没有项目卡时，问用户有没有现成设定。有的话以用户的为准，没有才按 SKILL.md 阶段 0 出标签、阶段 1 出 3 张概念卡。
4. 每个阶段写完停下，等用户确认再进下一步。概念由用户选。
5. 在 NOW.md 加一行。

## 用 agent 写一集

前提：该剧的整季 `2-season.md` 已被用户确认。

1. 调 `screenwriter`：告诉它剧名目录、集号，写 `outline.md` 和 `script.md`，并自跑质量门。
2. 调 `reviewer`：只给它 `script.md` 和 `2-season.md`，写 `review.md`。
3. 低于该剧及格线（state.md 第三行，默认 75）：把 review.md 的改法交回 screenwriter 改一次，再让 reviewer 审一次，结果追加到 review.md。
4. 默认不做分镜；用户明确要时再调 `storyboarder`，并跑 shots 质量门。
5. 更新该剧 state.md、NOW.md，导出 json（见下）。

## 和网页互通

- 给网页：`python3 .claude/skills/short-drama-preprod/scripts/studio_sync.py to-studio projects/<剧名> projects/<剧名>/<剧名>-项目.json`，用户在网页左下角点「导入项目」选这个文件。
- 从网页拿回：用户在网页点「导出项目文件」把 json 发来，然后运行 `studio_sync.py from-studio <文件> projects/<剧名>`。只覆盖有改动的文件，旧版本自动备份到 `projects/<剧名>/_imports/<时间>/`。之后在 state.md 把被改过的阶段标「待确认」，下游标「需重审」。

## 更新网页工具

改 `studio/studio.html` 或 `studio/gate-checker.html` 后，在 claude.ai 里用同一个文件重新发布到 MAP.md 里的链接，并用模拟数据试一遍主要流程。
