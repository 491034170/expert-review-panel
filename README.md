# expert-review-panel

> 一个面向作品投稿 / 答辩 / 提交前的严审 Claude skill：模拟顶级期刊审稿人、VC 尽调合伙人、资深架构师、竞赛评委组成的专家评审团，在你真正递出作品之前，把最容易致命的问题先翻出来。
>
> A Claude skill for ruthless pre-submission review: papers, business plans, pitch decks, code, competition materials, and creative work — reviewed by a simulated multi-expert panel before you ship.

[![Release](https://img.shields.io/github/v/release/491034170/expert-review-panel)](https://github.com/491034170/expert-review-panel/releases/latest)
[![CI](https://github.com/491034170/expert-review-panel/actions/workflows/ci.yml/badge.svg)](https://github.com/491034170/expert-review-panel/actions/workflows/ci.yml)
[![GitHub Repo stars](https://img.shields.io/github/stars/491034170/expert-review-panel)](https://github.com/491034170/expert-review-panel/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Claude Skill](https://img.shields.io/badge/built%20for-Claude%20Skill-8A2BE2)](https://docs.claude.com)

快速链接：
- 最新发布：<https://github.com/491034170/expert-review-panel/releases/latest>
- 主技能说明：[`SKILL.md`](./SKILL.md)
- Prompt recipes：[`examples/prompt-recipes.md`](./examples/prompt-recipes.md)
- 输出解剖：[`examples/output-anatomy.md`](./examples/output-anatomy.md)
- 反群体思维设计：[`references/anti-groupthink.md`](./references/anti-groupthink.md)
- 输出自检脚本：[`scripts/check_four_piece.py`](./scripts/check_four_piece.py)
- 如果这个项目对你有帮助，欢迎点个 Star：<https://github.com/491034170/expert-review-panel/stargazers>

---

## English Quickstart

### What you get

This skill runs a strict review workflow instead of a polite “looks good overall” pass.

It produces:
- A full expert-by-expert review
- A priority-sorted issue list tagged `P0 / P1 / P2`
- A clear `GO / CONDITIONAL GO / NO-GO` verdict
- Critiques forced to follow the “four-piece rule”: `location + evidence + reason + concrete fix direction`

### Best-fit use cases

- Academic papers and thesis drafts
- Business plans and pitch decks
- Code review and technical design review
- Competition submissions and defense materials
- Creative writing and long-form content

### Example prompts

- “Peer review this abstract like a harsh SSCI reviewer.”
- “Red-team this pitch deck before investor meetings.”
- “Review this code like a security auditor and principal architect.”
- “帮我严审这份论文，看现在能不能投。”
- “这份 BP 有没有会被投资人一票否决的硬伤？”

### Install

Option 1 — download the packaged skill:
1. Open Releases: <https://github.com/491034170/expert-review-panel/releases/latest>
2. Download `expert-review-panel-<version>.skill` or `expert-review-panel.skill`
3. Drag the `.skill` file into Claude Desktop / Claude Code

Option 2 — install from source:

```bash
git clone https://github.com/491034170/expert-review-panel.git ~/.claude/skills/expert-review-panel
```

Then restart Claude and invoke it with a review request.

### Why this is different

The main failure mode of LLM-based “multi-expert review” is not disagreement — it is shared blindness. Multiple simulated experts can still miss the same flaw because they come from the same base model. This repo explicitly counters that with anti-groupthink mechanisms such as blind review, Devil’s Advocate hard rules, minority-opinion protection, unanimous-check warnings, and chair self-challenge.

See [`references/anti-groupthink.md`](./references/anti-groupthink.md).

---

## 中文说明

### 它解决什么问题

大多数“帮我看看”式反馈的问题不是不友善，而是太温和、太空泛、太像安慰。真正要命的不是“文风可以更清晰”，而是：

- 论证链条里有断点，但没人直说
- 商业计划里有一票否决项，但没人点穿
- 代码里有生产级隐患，但 review 停留在表面
- 参赛材料方向跑偏，但答辩前没人扮演真正挑刺的评委

`expert-review-panel` 的目标，就是在“正式提交之前”先做一次高压预审。

### 你会拿到什么

调用这个 skill 后，默认不是得到一段温和总结，而是得到三类可执行产物：

1. 完整专家报告：每位专家从自己的角色出发独立发言
2. 优先级问题清单：按 `P0 / P1 / P2` 排序，先改最致命的
3. 明确裁决：`GO / CONDITIONAL GO / NO-GO`

并且每条负面意见都必须尽量满足“四件套”：
- 位置
- 证据
- 原因
- 修改方向

### 适用场景

| 作品类型 | 典型场景 |
|---------|---------|
| 中文学术论文 | SCI/SSCI/CSSCI 投稿、硕博论文、期刊外审模拟 |
| 英文学术论文 | Nature/Science、顶会（NeurIPS/ACL/CVPR）、基金申请、PhD 答辩 |
| 商业方案 / PPT | A 轮路演、BP 内审、投决会前 dry-run |
| 代码 / 技术方案 | 上线前 code review、架构评审、安全审计 |
| 参赛材料 | 互联网+、挑战杯、美赛、各类 PPT 答辩 |
| 创意文案 | 剧本、长文、广告创意 |

### 核心设计

这个 skill 不是靠“多说几句狠话”来显得严格，而是靠结构化约束来减少 LLM 常见失守。

四条底层原则：

1. 禁止空话套话
   - 每条负面意见都尽量满足“四件套”：位置 + 证据 + 原因 + 修改方向。
2. 动态组队，拒绝万金油
   - 论文、BP、代码、创意稿调用的是不同专家库，不用同一套“通用点评人”糊弄全部场景。
3. 反群体思维
   - 通过盲评、DA 硬规则、一致通过警示、少数意见保护、主席自我对抗等机制，降低“一起漏判”的风险。
4. 最终必须下结论
   - 不是“建议再优化一下”，而是明确给出 `GO / CONDITIONAL GO / NO-GO`。

### 五阶段工作流

```text
阶段 0  接收与分诊   → 搞清作品类型 + 目标场景 + 规模档位
阶段 1  独立评审     → 每位专家盲评，打 P0/P1/P2 + 置信度
阶段 2  交叉辩论     → 1-2 轮，暴露分歧，魔鬼代言人登场
阶段 3  主席裁决     → 打认识论标签、按场景校准阈值、下结论
阶段 4  输出 + 自检  → 报告交付前跑 scripts/check_four_piece.py
```

### 为什么这个仓库更适合公开分发

除了 skill 本体，这个仓库还附带了一层“自己审自己”的基础设施：

- `evals/evals.json`：3 条基础测试用例
- `scripts/check_four_piece.py`：对输出进行格式层面的自动校验
- GitHub Actions CI：自动检查脚本可运行、样例报告可通过 / 可失败

这意味着它不是只有一份 prompt 文档，而是带了基本质量闸门的可维护 repo。

### 目录结构

```text
expert-review-panel/
├── SKILL.md                        # 主入口（skill YAML + 工作流）
├── references/                     # 按作品类型分库
│   ├── academic-chinese.md
│   ├── academic-english.md         # 含 PhD Supervisor / External Examiner
│   ├── business-docs.md
│   ├── code-tech.md
│   ├── competition.md
│   ├── creative-works.md
│   └── anti-groupthink.md          # 反群体思维 6 条硬机制
├── assets/                         # 输出模板
│   ├── review-report-template.md
│   ├── priority-list-template.md
│   └── verdict-template.md
├── scripts/                        # 后处理校验
│   ├── check_four_piece.py         # 四件套/裁决/标签/占位符检查
│   └── README.md
├── evals/
│   └── evals.json                  # 3 个测试用例
├── tests/
│   └── fixtures/
│       ├── valid-review-report.md   # CI 正向样例
│       └── invalid-review-report.md # CI 反向样例
└── .github/workflows/
    └── ci.yml                       # 自动校验 workflow
```

### 快速上手

#### 方式 1：从 Releases 安装 `.skill`

打开：<https://github.com/491034170/expert-review-panel/releases/latest>

推荐下载：
- `expert-review-panel-<version>.skill`：版本化安装包，适合分发与归档
- `expert-review-panel.skill`：latest 别名包，适合直接安装
- `expert-review-panel-repo.tar.gz`：源码快照，适合离线备份

#### 方式 2：本地安装到 Claude Code / Claude Desktop

```bash
git clone https://github.com/491034170/expert-review-panel.git ~/.claude/skills/expert-review-panel
```

重启 Claude，然后对话里说：
- “帮我严审这份论文”
- “这份 BP 还有哪些致命漏洞？”
- “review 一下这段代码，按生产标准来”

即可触发。

#### 方式 3：自检你自己写的评审报告

```bash
python scripts/check_four_piece.py your-review-report.md
```

四项检查全绿才算合格交付：
- 明确裁决
- P0 / P1 / P2 标签
- 四件套关键词密度
- 无模板占位符残留

### CI / 自动校验

仓库内置 GitHub Actions：
- 自动编译检查 `scripts/check_four_piece.py`
- 自动验证 `evals/evals.json` 结构
- 自动对正向样例运行校验并要求通过
- 自动对反向样例运行校验并要求失败

工作流文件见：[`.github/workflows/ci.yml`](./.github/workflows/ci.yml)

### 版本历史

- **v1.1.1**（当前）——仓库与分发层补强版
  - 新增 GitHub Actions CI workflow
  - 新增正向 / 反向样例报告，自动校验 validator 行为
  - README 首页重写，补全 releases / 安装 / 质量闸门说明
  - 修复 `check_four_piece.py` 中 `CONDITIONAL GO` 被重复识别为 `GO` 的问题
- **v1.1**——基于 v1.0 自审结果的修补版
  - DA 硬规则（援引具体证据 / 可检验反例 / 指名对象 / 反驳边界）
  - 学位论文 Supervisor + External Examiner 补齐
  - 规模档位（轻量 3 人 / 标准 4 人 / 深度 6-8 人）
  - 场景相对阈值表（顶级 / 标准 / 宽松）
  - 模板占位符硬规定
- **v1.0**——首版，含 5 阶段工作流 + 6 套专家库 + 反群体思维 playbook + 自检脚本

### 灵感来源

本 skill 设计时参考了 GitHub 上三个开源先例的思路：

- [`wan-huiyan/agent-review-panel`](https://github.com/wan-huiyan/agent-review-panel)——4–6 人对抗评审 + Supreme Judge 的工程实现
- [`andrehuang/academic-writing-agents`](https://github.com/andrehuang/academic-writing-agents)——学术写作专用 12 Agent，Review-then-Act 模式
- [`Imbad0202/academic-research-skills`](https://github.com/Imbad0202/academic-research-skills)——7 Agent 含 Devil's Advocate，0-100 评分 + Accept/Minor/Major/Reject 分层

本项目在以上基础上强化了两件事：
- 跨作品类型的动态组队
- 中文学术 / 参赛场景的本地化

### 贡献

欢迎 issue 和 PR：

- 新增专家库（如医学论文、法律文书、游戏设计文档等）→ 在 `references/` 下加一个新的 `.md`，遵循“专家阵容 + 常见致命缺陷库 + 严苛度校准”三节结构。
- 新增测试用例 → 在 `evals/evals.json` 里加一条。
- 反群体思维机制改进 → PR 到 `references/anti-groupthink.md`，最好带一个真实失守案例说明为什么需要这条。

### License

[MIT](./LICENSE) — 自由用、自由改，保留版权声明即可。

---

**Built by 王鑫 · Powered by Claude Skill**
