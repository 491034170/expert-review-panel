# expert-review-panel — Output Anatomy

This file explains what a strong output should look like.

## Minimum useful structure

A good expert-review-panel response should usually contain:

1. Review overview
2. Priority-sorted issue list
3. Expert-by-expert detailed comments
4. Debate highlights
5. Final chair verdict

## What the quick-action section should do

The fast-action section should help the user answer:
- What is the most dangerous problem?
- What must be fixed first?
- Can this be submitted now?

A weak output says:
- "Overall it is good but could be improved."

A strong output says:
- "NO-GO because the core causal claim is not supported by the evidence and would likely fail external review."

## Example of a useful issue entry

```text
P0 | 方法部分第 3 段
位置：方法部分第 3 段
证据：原文直接把横截面问卷相关性结果写成“说明 X 导致 Y”。
原因：相关性不等于因果，这会让核心结论在外审中被直接质疑。
修改方向：把因果措辞改为相关性表述；如果要主张因果，需要补充识别策略或重新降级结论强度。
```

Why this is good:
- the location is concrete
- the evidence is quoted / specific
- the reason explains the risk
- the fix direction is actionable

## Example of a weak issue entry

```text
The logic is not rigorous enough and could be improved.
```

Why this is weak:
- no location
- no evidence
- no explicit reason
- no actionable revision direction

## What the final verdict should do

The verdict should not be decorative. It should directly answer whether the current draft is ready.

Examples:

```text
GO — no blocker-level issues remain for the stated submission context.
```

```text
CONDITIONAL GO — can proceed only if the two P0 issues below are fixed first.
```

```text
NO-GO — the current draft contains structural problems that make submission premature.
```

## Good chair language

Good chair synthesis:
- merges duplicates
- removes weak critiques
- explains which problems are truly blocking
- distinguishes cosmetic issues from structural ones

A strong chair section should make the user feel:
- "I know exactly what to fix next."

## Best use of the P0 / P1 / P2 system

- **P0** = blocker / fatal if unaddressed
- **P1** = major weakness that seriously hurts competitiveness
- **P2** = useful but secondary improvement

If everything is tagged P1, the prioritization failed.
If nothing is tagged P0 in a clearly broken draft, the panel was too soft.

## What users should look for when judging output quality

Ask these questions:
- Did the report identify specific fatal flaws?
- Are critiques tied to concrete evidence?
- Is the final verdict decisive?
- Does the output give an order of operations for revision?

If the answer is “no,” the output may look long but still be low-value.
