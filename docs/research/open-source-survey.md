# 开源 AI 短片 / 短剧多智能体项目调研（2026-10-22）

| 项目 | Stars | 许可证 | 覆盖环节 | 支持模型 | 评价 |
|---|---|---|---|---|---|
| [OpenMontage](https://github.com/calesthio/OpenMontage) | ~70.7k | AGPLv3 | 调研、剧本、分镜、素材、配音、音乐、音效、剪辑、调色、字幕、自动审片 | 视频：Kling、Veo 3.1、Runway Gen-4、Seedance、MiniMax 等；图像：FLUX、Imagen 4、GPT Image 2、Nano Banana 2；配音：ElevenLabs 等；音乐：Suno、ElevenLabs Music | 全链路最完整，直接用 Claude Code 当导演，带预算上限和成本面板。AGPL 对商业 SaaS 有开源义务 |
| [ViMax](https://github.com/HKUDS/ViMax) (港大) | ~12.7k | MIT | 创意/剧本/小说 转 多场景视频，导演、编剧、制片 Agent | LLM：OpenAI 兼容；图像：Nano Banana、GPT Image 2；视频：Veo、Seedance 2.0 | 学术框架，MIT 可商用改造；声音、音乐支持不明确 |
| [huobao-drama](https://github.com/chatfire-AI/huobao-drama) | ~16.3k | CC BY-NC-SA（禁止商用） | 小说改编、角色场景图、分镜、批量视频、FFmpeg 合成字幕 | Seedance 2.0、MiniMax H3、万相 3.0 | 有 Docker 和桌面版，开箱即用，面向中文短剧；无配音音乐；商用需授权 |
| [BigBanana-AI-Director](https://github.com/shuyu-labs/BigBanana-AI-Director) | ~2k | 未核实 | 一句话生成整部短剧 | 未核实 | 未深入看 |
| [dramaclaw](https://github.com/dramaclaw/dramaclaw) | ~3.7k | 未核实 | 剧本到成片（剧、广告、产品视频） | 未核实 | 未深入看 |
| [Open-AI-Micro-Drama-Generator](https://github.com/Anil-matcha/Open-AI-Micro-Drama-Generator) | ~500 | MIT | 编剧、角色、分镜、帧、视频、拼接 | 全部经 MuAPI 一个 key（FLUX + Kling） | 代码简单好读，但绑定第三方平台，无声音 |

其他：Toonflow、Jellyfish、ArcReel、阿里 lumenx（小说转动画短剧）、OnlyShot（Claude Skill 版短剧流程）。

## 建议
- 最快出片：直接跑 OpenMontage，Claude Code 作为导演。今天就能出第一条。
- 做成自己的产品/创业项目：以 ViMax（MIT）为底座二次开发，补上配音、音乐、剪辑，或参考 OpenMontage 的设计自己实现。避开 huobao-drama 的禁止商用许可。

来源：GitHub 各项目主页、[github.com/topics/ai-short-drama](https://github.com/topics/ai-short-drama)、[github.com/topics/ai-filmmaking](https://github.com/topics/ai-filmmaking)、[pixo.video 开源视频管线综述](https://pixo.video/blog/open-source-ai-video-pipelines)。Star 数为抓取时页面数据。
