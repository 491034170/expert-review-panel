# scripts/ · expert-review-panel 工具脚本

## check_four_piece.py

评审报告输出的后处理检查器。对本 skill 产出的报告做程序化校验，确保 SKILL.md 里写的那些“必须”不是空头承诺。

### 用法

```bash
# 检查一份已保存的报告
python scripts/check_four_piece.py path/to/review-report.md

# 或通过管道
cat review-report.md | python scripts/check_four_piece.py -
```

### 它在检查什么

四个硬指标：

1. **Verdict** — 报告是否给出 `GO / CONDITIONAL GO / NO-GO` 明确裁决。主席“建议进一步打磨”等同未完成。
2. **Severity tags** — 问题清单至少含 3 条，且每条都有 `P0 / P1 / P2` 标签。
3. **Four-piece markers** — 四件套关键词（位置、证据、原因、修改方向）的整体密度，每类至少 3 次。这是粗检，不能保证每条问题逐条合规，但能发现“整体没执行四件套”的失守。
4. **No placeholders** — 报告里不得残留未替换的模板占位符 `{xxx}`。

### 退出码

- `0`：全部通过
- `1`：存在未通过项（stdout 输出 JSON 给出详情）
- `2`：参数错误 / 文件读取失败

### CI 冒烟测试

仓库里额外提供了两个样例，给 GitHub Actions 做自动化冒烟测试：

- `tests/fixtures/valid-review-report.md`：应当通过
- `tests/fixtures/invalid-review-report.md`：应当失败

对应 workflow 见：`/.github/workflows/ci.yml`

### 建议的调用时机

在主席阶段产出报告后、交付用户前，跑一次这个脚本。如果有未通过项，主席应修补再交付——这是最低限度的“自己吃自己的狗粮”。

### 已知局限

这是程序化粗检，不判断**内容质量**：
- 报告可以全部通过这四项检查，但每条意见仍然是空话；
- 四件套密度达标不代表每条问题都逐条含四件套（模型可能在某一条集中塞，其他条偷懒）；
- 占位符检查偶尔会误伤代码块内的 `{...}`。

要做语义层面的质量评估，需要另一个 LLM 评审或人工复核。
