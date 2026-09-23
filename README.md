<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=230&color=0d1117,0b2942,0e7490,22d3ee&text=Hi%2C%20I%27m%20Jingzhao&fontSize=54&fontColor=e6edf3&fontAlignY=36&desc=16%20y%2Fo%20%C2%B7%20Shanghai%20%C2%B7%20iterate%20%2B%20GlassPane&descSize=20&descColor=8b949e&descAlignY=56&animation=fadeIn" width="100%" />
</div>

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&pause=1300&color=22d3ee&center=true&vCenter=true&width=700&lines=16+y%2Fo+from+Shanghai+%F0%9F%8F%99;coding+between+classes;building+AI+that+reviews+its+own+code;building+agents+that+have+to+prove+it" alt="typing" />
</div>

## 👋 关于我 · About Me

- 🎓 **16 岁，上海高中生** —— 作业写完才开机，代码都在深夜和周末生长。<br>
  A 16-year-old high schooler in Shanghai — most of my code grows after homework, on weekends and at midnight.
- 🤖 **我关注的两个问题**：让 AI 像工程师一样对待自己的代码——计划、评审、修复、验证、回环；以及让它**说到做到**——一句"界面变了"必须留下可回放的证据。<br>
  The two problems I care about: making AI treat its own code like an engineer — plan, review, fix, verify, loop — and making it *prove* what it claims, with replayable evidence behind every "the UI changed".
- 🛠️ **[iterate](https://github.com/jingzhao-l/iterate-skill) 生态作者**：围绕「多轮审查-修复闭环」的三件套（skill / harness / plugin），见下方。<br>
  Author of the **iterate** ecosystem — a three-piece toolchain around the multi-round review-fix loop (skill / harness / plugin).
- 🪟 **[GlassPane](https://github.com/jingzhao-l/GlassPane) 作者**：macOS 上给 AI 代理的运行时验证引擎，Swift 写的，通过 MCP 暴露 `gp_*` 工具。<br>
  Author of **GlassPane** — a runtime verification engine for AI agents on macOS, written in Swift, exposed over MCP.
- 🔭 **最近在死磕的一件事**：让我的工具无法在"没测到"的情况下报出结论——测试隔离闸、拒绝分支必须真能拒绝、发布可复现。这类缺陷比新功能有意思得多。<br>
  Currently grinding on: making my tools unable to report a conclusion they never measured — isolation gates in test suites, guard branches that can actually refuse, reproducible releases. Boring, and much more fun than new features.

## 🚀 iterate 生态 · The iterate Ecosystem

一句话：**把「AI 写完就走」变成「AI 自己审、自己改、自己验证」**。<br>
One line: turning "AI writes and prays" into "AI reviews, fixes and verifies its own work — round after round".

<div align="center">

<img src="assets/iterate-tui.svg" alt="iterate-harness TUI convergence panel" width="880">

<sub>iterate-harness 的收敛面板：5 轮把 18 个 findings 清到 0，每个维度精确计费<br>
The iterate-harness convergence panel: 18 findings driven to zero in 5 rounds, with exact per-dimension billing</sub>

</div>

| 仓库 · Repo | 是什么 · What it is |
|---|---|
| 🧠 **[iterate-skill](https://github.com/jingzhao-l/iterate-skill)** | 面向对话式 agent 的多轮审查-修复技能：9 维度评审、双轨修复、决策日志、项目知识库<br>A skill for conversational agents: 9-dimension review, dual-track fixes, decision log, project knowledge base |
| ⚙️ **[iterate-harness](https://github.com/jingzhao-l/iterate-harness)** | 专为 iterate 打造的 coding harness（`ih` CLI + React TUI）：在 CI/PR 里无人值守地跑完整审查-修复闭环，含成本计量与阈值门禁<br>A coding harness purpose-built for iterate: runs the full review-fix loop unattended in CI/PR, with cost metering and threshold gates |
| 🖥️ **[iterate-plugin](https://github.com/jingzhao-l/iterate-plugin)** | 桌面插件：收敛仪表盘、逐轮进度、实时干预<br>Desktop plugin: convergence dashboard, round-by-round progress, live intervention |

三者共享同一套 `iterate.config.yaml` 与维度体系 —— **skill 给对话，harness 给 CI，plugin 给桌面**。<br>
All three share one config and one dimension system — **skill for chat, harness for CI, plugin for desktop**.

**一键安装 · One-liner install**<br>

- 🧠 skill → `npx iterate-skill-installer`
- ⚙️ harness → `npm install -g iterate-harness` 或 `pip install iterate-harness`
- 🖥️ plugin → `dsh plugin --profile web add github:jingzhao-l/iterate-plugin#main`

## 🪟 GlassPane · 让 agent 交出证据

一句话：**AI 代理在 macOS 上说"我点过了、界面变了"，GlassPane 要它拿出证据**。<br>
One line: when an agent on macOS claims "I clicked it and the UI changed", GlassPane makes it show the receipts.

| 能力 · Capability | 是什么 · What it is |
|---|---|
| 🔍 **证据包 · evidence packs** | 每次界面操作留下可回放的档案：操作前后的 AX 结构对比、像素对比、耗时与通道存活指标<br>Every UI operation yields a replayable pack: AX-tree diff, pixel diff, timing and channel-liveness metrics |
| 🧭 **归因 · attribution** | 分清"这次变化是这次操作造成的"还是别人造成的；判不动的时候如实说判不动，不猜<br>Separates a change caused by *this* operation from one caused by something else — and says so when it can't decide |
| ⏪ **回滚 · rollback** | 探针 SDK 的检查点可以把目标应用拉回操作前的状态（tier-1 全量 / tier-2 重放两条路径）<br>Probe-SDK checkpoints restore the target app — tier-1 full restore and tier-2 replay |
| 🔐 **权限面 · TCC surface** | 辅助功能／输入监控／屏幕录制／开发者工具四类席位：逐卡引导 + 机器实测，面板显示的是**授权主体自己**的状态<br>Four TCC seats with per-card guidance and machine-run verification — the panel shows the granting subject's own state, never a guess |
| 🤝 **接入 · wiring** | Swift 引擎 + 后台守护进程，任意 MCP 客户端（Claude / Cursor / …）通过 `gp_*` 工具驱动<br>Swift engine + launchd daemon; any MCP client drives it through the `gp_*` tools |

```bash
curl -fsSL https://raw.githubusercontent.com/jingzhao-l/GlassPane/main/install.sh | sh   # macOS 14+
```

<p align="center">
  <a href="https://www.npmjs.com/package/glasspane-mcp"><img src="https://img.shields.io/npm/v/glasspane-mcp?label=glasspane-mcp&color=CB3837&logo=npm" alt="glasspane-mcp"></a>
  <a href="https://www.npmjs.com/package/glasspane-install"><img src="https://img.shields.io/npm/v/glasspane-install?label=glasspane-install&color=CB3837&logo=npm" alt="glasspane-install"></a>
  <a href="https://github.com/jingzhao-l/GlassPane/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/jingzhao-l/GlassPane/ci.yml?label=CI&logo=githubactions" alt="CI"></a>
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT">
</p>

它自己也在吃 iterate 的狗粮：仓库里内置的 [`@iterate/kernel`](https://github.com/jingzhao-l/iterate-skill) 就是生态共用的那套内核（schema 真源 + 双语言契约），而每次大改都由 iterate 的审查-修复闭环过一遍。<br>
It also dogfoods iterate: the `@iterate/kernel` vendored inside it is the same shared kernel the rest of the ecosystem runs on (schema truth source + dual-language contracts), and each big pass goes through iterate's review-fix loop.

## 🛠️ 技术栈 · Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=py,ts,js,react,nodejs,swift,apple,bash,githubactions&theme=dark" alt="stack">

</div>

## 📥 下载量 · Downloads

全渠道累计下载（自动更新 · all-time, auto-updated），数据源见 [`downloads.json`](./downloads.json)

| 项目 · Project | 下载 · Downloads |
|---|---|
| 🌱 **生态合计 · Ecosystem total** | ![ecosystem-total](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjingzhao-l%2Fjingzhao-l%2Fmain%2Fdownloads.json&query=total&label=iterate%20total&color=22d3ee) |
| 🧠 iterate-skill（`iterate-skill-installer`） | ![skill](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjingzhao-l%2Fjingzhao-l%2Fmain%2Fdownloads.json&query=skill&label=skill&color=4285F4) |
| ⚙️ iterate-harness（npm） | ![harness-npm](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjingzhao-l%2Fjingzhao-l%2Fmain%2Fdownloads.json&query=harness_npm&label=harness%20npm&color=CB3837) |
| ⚙️ iterate-harness（PyPI） | ![harness-pypi](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjingzhao-l%2Fjingzhao-l%2Fmain%2Fdownloads.json&query=harness_pypi&label=harness%20pypi&color=3776AB) |
| 🖥️ iterate-plugin（npm） | ![plugin](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjingzhao-l%2Fjingzhao-l%2Fmain%2Fdownloads.json&query=plugin&label=plugin&color=CB3837) |

## 📊 统计 · Stats

<div align="center">

![Stats](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=jingzhao-l&theme=github_dark&v=4)
![Languages](https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=jingzhao-l&theme=github_dark&v=4)
![Profile details](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=jingzhao-l&theme=github_dark&v=4)

</div>

## 🧭 别处 · Elsewhere

| 仓库 · Repo | 一句话 · What it is |
|---|---|
| 📚 [awesome-claude-skills](https://github.com/jingzhao-l/awesome-claude-skills) | Claude Skills 精选清单<br>A curated list of Claude Skills |
| 📚 [awesome-dsh-plugin](https://github.com/jingzhao-l/awesome-dsh-plugin) | DeepSeek Harness 插件精选清单<br>A curated list of dsh plugins |
| 🔬 [mnist-snn-hardware-tradeoff](https://github.com/jingzhao-l/mnist-snn-hardware-tradeoff) | 在 Cadence 180nm 模型上做脉冲神经网络的精度-能耗折中分析（我想看看硅上的神经元的另一头）<br>SNN accuracy-vs-energy trade-off on Cadence 180nm models — the silicon end of the same curiosity |

---

<div align="center">

<img src="https://komarev.com/ghpvc/?username=jingzhao-l&style=flat-square&color=22d3ee&label=visitors" alt="visitors">
<br><br>
<sub>⭐ 如果 iterate 或 GlassPane 帮到了你，欢迎去仓库点个 Star · If either of them helps you, a star means a lot</sub>
<br><br>
<img src="https://capsule-render.vercel.app/api?type=waving&height=110&color=0d1117,0b2942,0e7490,22d3ee&section=footer" width="100%" />

</div>
