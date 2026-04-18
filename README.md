# expert-review-panel

> 一个面向作品投稿 / 答辩 / 提交前的**严审 skill**——模拟顶级期刊审稿人、VC 尽调合伙人、资深架构师、竞赛顶级评委组成的专家评审团，在你真正递出作品之前把问题全部翻出来。
>
> A Claude skill that simulates a strict, multi-expert pre-submission review panel — catching fatal flaws before your paper / proposal / pitch / code goes out the door.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Skill version](https://img.shields.io/badge/version-v1.1-blue)](./SKILL.md)
[![Claude Skill](https://img.shields.io/badge/built%20for-Claude%20Skill-8A2BE2)](https://docs.claude.com)

---

## English Quickstart

**What it does.** Most "can you review this?" feedback is uselessly gentle — *"overall good, could be clearer."* This skill does the opposite: it assembles a panel of 4–8 domain-matched experts (not a generic "writing coach"), runs them through **Independent Review → Adversarial Debate → Chair's Synthesis**, and produces:

- A full expert-by-expert report
- A priority-sorted issue list tagged **P0 / P1 / P2** (Blocker / Major / Minor)
- A decisive **GO / CONDITIONAL GO / NO-GO** verdict

Every single critique must satisfy the "four-piece rule": **location + evidence + reason + concrete fix direction**. No hand-wavy "could be improved" allowed.

**Supported work types.** Chinese & English academic papers · business plans & pitch decks · code & technical designs · competition submissions · creative writing.

**Install.**

1. Download `expert-review-panel-v1.1.skill` from Releases (or clone this repo).
2. In Claude Desktop / Claude Code: drag the `.skill` file in, or copy the folder to `~/.claude/skills/`.
3. Invoke by asking Claude anything like *"帮我严审这份论文"* / *"peer review this draft"* / *"red-team this pitch deck"*.

**Why it's different.** The real failure mode of LLM-simulated "multi-expert" panels isn't that experts argue — it's that **all experts share the same base model and miss the same blind spots together**. This skill fights that with six anti-groupthink mechanisms (blind review, Devil's Advocate hard rules, unanimous-check warnings, sycophancy detection, minority-opinion protection, chair's self-challenge). See [`references/anti-groupthink.md`](./references/anti-groupthink.md).

---

## 中文说明

### 它解决什么问题

大多数"帮我看看"式的反馈都温和得没用——泛泛地说"整体不错，可以再清晰些"。本 skill 存在的意义恰恰相反：**模拟一个由真·对口专家组成的严审委员会**，把作品摁在桌上逐段挑错，用顶级期刊审稿人、VC 尽调合伙人、资深架构师、竞赛顶级评委那种近乎冷酷的标准，在用户真正提交之前把问题全部翻出来。

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

**四条底层原则**——不是流程，是反 LLM 常见失败模式的底层对策：

1. **禁止空话套话**——每条负面意见必须满足"四件套"：位置 + 证据 + 原因 + 修改方向。
2. **动态组队，拒绝万金油**——不同作品调用不同专家库；论文 ≠ 商业方案 ≠ 代码。
3. **反群体思维**——6 条硬机制（盲评、DA 硬规则、一致通过警示、讨好型检测、少数意见保护、主席自我对抗）。
4. **最终要敢于下结论**——GO / CONDITIONAL GO / NO-GO 三选一，不准"建议进一步打磨"收尾。

**五阶段工作流**：

```
阶段 0  接收与分诊   → 搞清作品类型 + 目标场景 + 规模档位
阶段 1  独立评审     → 每位专家盲评，打 P0/P1/P2 + 置信度
阶段 2  交叉辩论     → 1-2 轮，暴露分歧，魔鬼代言人登场
阶段 3  主席裁决     → 打认识论标签、按场景校准阈值、下结论
阶段 4  输出 + 自检  → 报告交付前跑 scripts/check_four_piece.py
```

### 目录结构

```
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
└── evals/
    └── evals.json                  # 3 个测试用例
```

### 快速上手

**方式 1：本地安装到 Claude Code / Claude Desktop**

```bash
git clone https://github.com/491034170/expert-review-panel.git ~/.claude/skills/expert-review-panel
```

重启 Claude，然后对话里说"帮我严审 XX 作品"即可触发。

**方式 2：打包成 .skill 文件再分发**

```bash
cd expert-review-panel
python -m zipfile -c ../expert-review-panel.skill .
```

生成的 `.skill` 文件可以直接拖进 Claude Desktop 安装。

**GitHub Releases 中推荐提供的发布资产**

- `expert-review-panel-v1.1.skill`：版本化安装包，适合分发与归档
- `expert-review-panel.skill`：latest 别名包，适合直接安装
- `expert-review-panel-repo.tar.gz`：源码快照，适合离线备份

**方式 3：自检你自己写的评审报告**

```bash
python scripts/check_four_piece.py your-review-report.md
```

四项检查（裁决 / P0-P1-P2 标签 / 四件套密度 / 无占位符残留）全绿才算合格交付。

### 版本历史

- **v1.1**（当前）——基于 v1.0 自审结果的修补版
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

本项目在以上基础上强化了**跨作品类型的动态组队**和**中文学术 / 参赛场景的本地化**。

### 贡献

欢迎 issue 和 PR：

- 新增专家库（如医学论文、法律文书、游戏设计文档等）→ 在 `references/` 下加一个新的 `.md`，遵循"专家阵容 + 常见致命缺陷库 + 严苛度校准"三节结构。
- 新增测试用例 → 在 `evals/evals.json` 里加一条。
- 反群体思维机制改进 → PR 到 `references/anti-groupthink.md`，最好带一个真实失守案例说明为什么需要这条。

### License

[MIT](./LICENSE) — 自由用、自由改，保留版权声明即可。

---

**Built by 王鑫 · Powered by Claude Skill**
