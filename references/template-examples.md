# 逻辑答题模板范例

本文件提供英国本科常见考试题型的预设答题模板，供 `@extract-template` 功能参考。
每个模板标注适用场景、逻辑结构（中英对照）和空白框架。

---

## 一、数学/证明题

### 模板 1: Proof by Induction（数学归纳法）

**适用场景**：证明形如 "For all n >= 1, P(n) holds" 的命题。

**模板结构（中英对照）**：

| 步骤 | English Name | 中文 | 逻辑作用 |
|------|-------------|------|---------|
| 1 | Base Case | 基础情况 | 证明 n=1（或最小起始值）时命题成立 |
| 2 | Induction Hypothesis | 归纳假设 | 假设 n=k 时命题成立 |
| 3 | Induction Step | 归纳步骤 | 从 n=k 的假设推出 n=k+1 时命题成立 |
| 4 | Conclusion | 结论 | 由数学归纳法原理，命题对所有 n>=1 成立 |

**常用句式/关键词**：
- Base case: "When n = 1, LHS = ... = RHS. Therefore P(1) holds."
- Induction hypothesis: "Assume P(k) is true for some k >= 1, i.e. [命题表达式]"
- Induction step: "Consider n = k+1. LHS = ... [利用归纳假设] ... = RHS"

**完整模板框架**：

```
证明：P(n): [命题内容]

--- Base Case (n = 1) ---
LHS = #TODO: 代入 n=1 计算左边
RHS = #TODO: 代入 n=1 计算右边
Therefore, P(1) holds.

--- Induction Hypothesis ---
Assume P(k) is true, i.e. #TODO: 写出 k 时的等式

--- Induction Step (n = k+1) ---
Consider n = k+1:
LHS = #TODO: 展开表达式，利用归纳假设
    = #TODO: 化简
    = RHS
Therefore, P(k+1) holds.

--- Conclusion ---
By the principle of mathematical induction, P(n) holds for all n >= 1.
```

### 模板 2: Proof by Contradiction（反证法）

**适用场景**：证明"不存在"、"唯一性"、"无解"等命题。

| 步骤 | English Name | 中文 | 逻辑作用 |
|------|-------------|------|---------|
| 1 | Assume Negation | 假设否定 | 假设结论不成立（即命题的反面） |
| 2 | Logical Derivation | 逻辑推导 | 从假设出发，结合已知条件推导 |
| 3 | Contradiction | 矛盾 | 导出一个与已知事实/条件矛盾的结论 |
| 4 | Conclusion | 结论 | 矛盾说明假设不成立，因此原命题成立 |

**常用句式**：
- "Suppose, for contradiction, that [反面陈述]."
- "From this assumption, it follows that..."
- "But this contradicts [已知事实/条件], because..."
- "Therefore, our assumption must be false. Hence [原命题]."

### 模板 3: Direct Derivation / Solve-and-Explain（直接推导题）

**适用场景**：计算题、化简题、证明等式/不等式。

| 步骤 | English Name | 中文 | 逻辑作用 |
|------|-------------|------|---------|
| 1 | Identify Given & Goal | 明确已知和目标 | 写出已知条件和需要求解/证明的结论 |
| 2 | Select Method/Theorem | 选择方法/定理 | 解释为什么选择这个定理/方法 |
| 3 | Step-by-step Derivation | 分步推导 | 每步推导注明依据（定理/公式编号） |
| 4 | Verification | 验证/检验 | 代入原式检验或讨论解的合理性 |

---

## 二、Essay / 论述题

### 模板 4: Critical Evaluation Essay（批判性评价）

**适用场景**：Essay question 包含 "Critically evaluate...", "To what extent do you agree...", "Discuss..."。

| 步骤 | English Name | 中文 | 逻辑作用 |
|------|-------------|------|---------|
| 1 | Thesis Statement | 论点声明 | 明确自己的立场（不是中立描述） |
| 2 | Argument For | 正方论证 | 支持立场的最强论据 + evidence |
| 3 | Counterargument | 反方论证 | 承认反面观点并引用其证据 |
| 4 | Rebuttal | 反驳 | 指出反面观点的局限性或前提问题 |
| 5 | Synthesis & Conclusion | 综合结论 | 综合双方后重申立场，含 nuance（不是简单支持/反对） |

**常用句式**：
- Thesis: "This essay argues that... while acknowledging that..."
- Counterargument: "However, [Author] contends that... This perspective is valid insofar as..."
- Rebuttal: "Nevertheless, this argument overlooks the fact that..."
- Conclusion: "On balance, therefore, the evidence suggests that..."

### 模板 5: Compare and Contrast Essay（比较对比）

**适用场景**："Compare and contrast A and B"。

| 步骤 | English Name | 中文 |
|------|-------------|------|
| 1 | Define A and B | 定义双方 |
| 2 | Point 1: Similarity / Difference | 对比维度 1 |
| 3 | Point 2: Similarity / Difference | 对比维度 2 |
| 4 | Point 3: Similarity / Difference | 对比维度 3 |
| 5 | Overall Assessment | 综合评价（哪个更优/何时用哪个） |

---

## 三、编程/算法题

### 模板 6: Algorithm Design & Analysis（算法设计与分析）

**适用场景**："Design an algorithm to solve..." / "What is the time complexity..."

| 步骤 | English Name | 中文 | 逻辑作用 |
|------|-------------|------|---------|
| 1 | Problem Restatement | 问题重述 | 用自己的话重述问题，明确 input/output |
| 2 | Approach / Intuition | 算法思路 | 用 2-3 句话说明核心思想（不写代码） |
| 3 | Algorithm (Pseudocode / Code) | 算法（伪代码/代码） | 写出伪代码或带注释的关键代码段 |
| 4 | Complexity Analysis | 复杂度分析 | 时间 + 空间，分别给出 worst-case |
| 5 | Justification / Correctness | 正确性论证 | 解释为什么算法对任何输入都给出正确结果 |
| 6 | Edge Cases | 边界情况 | 列出 2-3 个边界情况并说明算法如何处理 |

### 模板 7: Bug Diagnosis & Fix（Bug 诊断与修复）

**适用场景**：考试给出一段有 bug 的代码，要求 find + explain + fix。

| 步骤 | English Name | 中文 |
|------|-------------|------|
| 1 | Expected vs Actual | 预期行为 vs 实际行为 |
| 2 | Bug Location | 定位 bug（第几行，什么条件触发） |
| 3 | Root Cause Analysis | 根因分析（为什么错，不是怎么改） |
| 4 | Proposed Fix | 修复方案（正确代码写法） |
| 5 | Test After Fix | 修复后的测试验证 |

---

## 四、统计/数据分析

### 模板 8: Hypothesis Testing Report（假设检验报告）

**适用场景**：统计题要求 complete a hypothesis test。

| 步骤 | English Name | 中文 |
|------|-------------|------|
| 1 | State Hypotheses | 声明 H0 和 H1 |
| 2 | Significance Level & Test | 显著性水平和选择的检验方法 |
| 3 | Assumptions Check | 假设条件检查（normality/independence/等方差） |
| 4 | Test Statistic Calculation | 检验统计量计算（写出公式和代入） |
| 5 | p-value / Critical Value | p 值或临界值 |
| 6 | Decision & Conclusion in Context | 统计决策 + 实际语境下的结论 |

---

## 五、提炼原则总结

辅导 `@extract-template` 时遵循：

1. **从具体到抽象**：保留原文中的具体例子作为示例，同时提取可跨题复用的逻辑骨架
2. **中英对照**：每个逻辑块的英文名（便于考试中使用）+ 中文说明（便于理解）
3. **空白框架不可直接填入答案**：用 `#TODO` 替代所有原文具体内容
4. **高频句式不给完整句**：只给句式骨架和关键词
5. **引用教案**：如果模板源于教案内容，注明具体章节和例题编号
6. **不超过 7 个逻辑步骤**：超过则建议拆分为子模板
