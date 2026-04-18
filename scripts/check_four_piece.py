#!/usr/bin/env python3
"""
check_four_piece.py — expert-review-panel 输出后处理检查器

对 skill 产出的评审报告做程序化校验，强制执行 SKILL.md 里的硬承诺：
  1) 必须给出 GO / CONDITIONAL GO / NO-GO 三选一的明确裁决
  2) 问题清单至少 3 条，每条必须有 P0 / P1 / P2 严重级标签
  3) 每条问题要覆盖四件套：位置 + 证据 + 原因 + 修改方向
  4) 报告里不得残留未替换的模板占位符（{xxx}）

使用：
    python scripts/check_four_piece.py <report.md>
    cat report.md | python scripts/check_four_piece.py -

退出码：
    0 — 所有检查通过
    1 — 存在未通过项（输出 JSON 会列出详情）
    2 — 参数错误 / 文件读取失败

注意：这是"粗检"，不是内容判断。脚本能发现"格式上的失守"——
比如完全没给裁决、没打 P0/P1/P2 标签、四件套关键词密度过低、
占位符没替换。它发现不了"说的有没有道理"这种主观质量——那仍
然依赖人类或另一个 LLM 做语义评审。
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


def check_verdict(text: str) -> dict[str, Any]:
    """检查是否含 GO / CONDITIONAL GO / NO-GO 裁决。

    这是 skill 最核心的硬承诺——主席必须敢于下结论，不能以"建议
    进一步打磨"这种模糊措辞收尾。
    """
    # 注意顺序：先匹配更长的 CONDITIONAL GO 和 NO-GO，避免被 GO 先匹掉
    patterns = [
        ("CONDITIONAL GO", r"CONDITIONAL\s+GO"),
        ("NO-GO", r"NO[\s-]?GO"),
        ("GO", r"(?<![A-Z\-])GO(?![A-Z])"),
    ]
    found: list[str] = []
    for name, pat in patterns:
        if re.search(pat, text):
            found.append(name)
    if found:
        return {
            "passed": True,
            "evidence": f"found verdict(s): {found}",
        }
    return {
        "passed": False,
        "evidence": "no GO / CONDITIONAL GO / NO-GO verdict found — main chair must deliver a clear verdict",
    }


def check_severity_tags(text: str) -> dict[str, Any]:
    """检查 P0/P1/P2 严重级标签。至少 3 条带标签的问题。"""
    p0 = len(re.findall(r"\bP0\b", text))
    p1 = len(re.findall(r"\bP1\b", text))
    p2 = len(re.findall(r"\bP2\b", text))
    total = p0 + p1 + p2
    counts = {"P0": p0, "P1": p1, "P2": p2, "total": total}
    if total >= 3:
        return {
            "passed": True,
            "evidence": f"severity tag counts: {counts}",
            "counts": counts,
        }
    return {
        "passed": False,
        "evidence": f"severity tag counts: {counts} — expected ≥3 tagged issues",
        "counts": counts,
    }


def check_four_piece(text: str) -> dict[str, Any]:
    """粗检四件套（位置 / 证据 / 原因 / 修改方向）的关键词密度。

    阈值：每类至少 3 次出现。这是保底信号——低于此说明主席没执行
    "四件套"硬规定。脚本做不了"每一条都含四件套"的语义判定，只能
    保证整体密度合理。
    """
    markers: dict[str, list[str]] = {
        "位置": [
            r"位置[:：]",
            r"位于",
            r"第\s*\d+\s*(?:行|页|段|节|章|部分)",
            r"\bline\s*\d+",
            r"section\s*\d+",
        ],
        "证据": [
            r"证据[:：]",
            r"原文[:：]",
            r"引用[:：]",
            r"\bevidence\b",
            r"原文写道",
        ],
        "原因": [
            r"原因[:：]",
            r"为什么.{0,15}是问题",
            r"导致.{0,20}(?:问题|风险|后果)",
            r"\bbecause\b",
            r"原因在于",
        ],
        "修改方向": [
            r"修改方向[:：]",
            r"修改建议[:：]",
            r"建议[:：]",
            r"应(?:改为|改成|修改)",
            r"\bfix[:：]",
            r"\bsuggestion",
        ],
    }
    counts: dict[str, int] = {}
    missing: list[str] = []
    for piece, patterns in markers.items():
        total = 0
        for pat in patterns:
            total += len(re.findall(pat, text, flags=re.IGNORECASE))
        counts[piece] = total
        if total < 3:
            missing.append(f"{piece}({total})")
    if missing:
        return {
            "passed": False,
            "evidence": f"low four-piece marker density: {', '.join(missing)} (expected ≥3 each)",
            "counts": counts,
        }
    return {
        "passed": True,
        "evidence": f"four-piece marker counts: {counts}",
        "counts": counts,
    }


def _strip_code_regions(text: str) -> str:
    """去掉 fenced code blocks 和 inline code spans。

    在 Markdown 评审报告里讨论模板本身时，作者可能写出 `{xxx}` 之
    类的"引用性占位符"作为例子——这不是未替换的占位符，是在讲占
    位符这件事。做占位符检测前要先把这些代码片段剥掉。
    """
    # fenced code blocks: ```...```
    text = re.sub(r"```[\s\S]*?```", "", text)
    # inline code spans: `...`
    text = re.sub(r"`[^`\n]*`", "", text)
    return text


def check_no_placeholders(text: str) -> dict[str, Any]:
    """检查是否存在未替换的模板占位符 {xxx}（忽略代码块 / inline code）。

    SKILL.md 模板里大量使用 {...} 作为占位。如果 LLM 照搬模板忘
    了替换，就会在最终报告里留下未填充的占位符——用户看到会以为
    skill 半途崩了。但代码块 / inline code 里的 {...} 是在"讲"
    占位符而非遗留占位符，所以先剥掉这些区域再检测。
    """
    stripped = _strip_code_regions(text)
    # 找 {内容} 形式，排除明显的 JSON / f-string 模式
    placeholders = re.findall(r"\{[^{}\n\"]{2,80}\}", stripped)
    likely_template = [
        p for p in placeholders
        if not (":" in p and re.search(r'[\w\s]+":\s*', p))
        and not re.match(r"\{[a-z_]+\s*=", p)
    ]
    if likely_template:
        sample = likely_template[:5]
        return {
            "passed": False,
            "evidence": f"unreplaced template placeholders found ({len(likely_template)} total), e.g.: {sample}",
        }
    return {
        "passed": True,
        "evidence": "no unreplaced template placeholders (after stripping code regions)",
    }


def run_all_checks(text: str) -> dict[str, Any]:
    checks = {
        "verdict": check_verdict(text),
        "severity_tags": check_severity_tags(text),
        "four_piece": check_four_piece(text),
        "no_placeholders": check_no_placeholders(text),
    }
    all_passed = all(c["passed"] for c in checks.values())
    return {
        "all_passed": all_passed,
        "checks": checks,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print(
            "usage: python check_four_piece.py <report.md | ->",
            file=sys.stderr,
        )
        return 2

    arg = sys.argv[1]
    try:
        text = sys.stdin.read() if arg == "-" else Path(arg).read_text(encoding="utf-8")
    except OSError as err:
        print(f"cannot read input: {err}", file=sys.stderr)
        return 2

    result = run_all_checks(text)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["all_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
