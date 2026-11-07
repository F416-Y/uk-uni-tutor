# UK Uni Tutor

面向中文母语留学生的英国本科作业苏格拉底式辅导 Skill（适用于 Claude Code、Codex 等支持 Skills 的 Agent）。通过阶梯式提问、`#TODO` 填空和学科专属引导模板，帮助学生**独立完成作业**，不给答案，只给方法。

**适用对象**：在英国就读 CS/SE/数学/统计/工科等本科课程、以英文教案学习但更习惯中文思考的中国留学生。

---

## 主要功能

- [x] **苏格拉底式辅导** — 绝不直接给答案，通过反问引导学生自己推导
- [x] **阶梯式帮助 (L0–L3+)** — 从元认知反问到 `#TODO` 填空，逐级加深提示
- [x] **教案驱动模式** (`@load-syllabus`) — 加载英文课程教案后，所有辅导严格基于教案内容
- [x] **术语学习助手** (`@learn`) — 结构化术语卡片 + 记忆技巧 + 抽认卡导出 (Anki CSV) + 术语小测
- [x] **逻辑答题模板提炼** (`@extract-template`) — 从例题答案中提炼可复用的答题框架
- [x] **中英思维导图生成** (`@mindmap`) — 生成飞书思维笔记兼容的大纲文本，粘贴一键转脑图
- [x] **软件工程专项** — 调试策略、算法设计、设计模式、单元测试、Git 操作、代码审查
- [x] **多学科适配** — 学术论文 / 数学与统计 / 编程作业 / 实验报告 / 项目报告
- [x] **学术诚信红线** — 内置英国大学学术规范，严格拒绝代写和疑似学术不端请求
- [x] **中文回复 + 英文原文引用** — 回复用中文，教案/术语/方法名保留英文原文

---

## 快速开始

### 1. 安装

```bash
# 使用 Skills CLI 安装到当前 Agent
npx skills add F416-Y/uk-uni-tutor -g -y
```

安装后重新启动 Agent，Skill 将自动加载。也可以直接下载仓库，将整个目录放入对应 Agent 的 skills 目录，并保留目录名 `uk-uni-tutor`。

### 2. 运行要求

- 支持 Skills 的 Agent，例如 Claude Code 或 Codex
- Python 3.8+，仅在使用 `scripts/` 下的练习题或教案解析脚本时需要
- 不需要上传教案，也不需要联网服务

### 3. 加载教案（可选但推荐）

直接粘贴教案文本，或指定文件路径：

```
@load-syllabus
<粘贴完整教案内容>
```

```
@load-syllabus file:./path/to/syllabus.txt
```

Claude 将自动提取课程结构、章节知识点和例题解法模式，之后所有辅导都严格基于教案内容。

### 4. 核心命令速览

| 命令 | 作用 |
|------|------|
| `@learn <术语>` | 学习术语：结构化卡片 + 记忆技巧 |
| `@extract-template` | 从文本中提炼答题框架 |
| `@mindmap <主题>` | 生成飞书思维导图大纲 |
| `@mindmap compare <A> <B>` | 生成概念对比图 |
| `@mindmap chapter <N>` | 基于教案生成章节全景图 |
| `@load-syllabus` | 加载教案 |
| `@exit-syllabus` | 退出教案模式 |

---

## 详细使用示例

### 场景一：辅导编程作业（Debug 递归函数）

> **学生**：我的递归函数一直栈溢出，不知道哪里出问题了。

> **Claude**：我理解你的困惑是：递归函数运行时抛出了 stack overflow 错误，但你不确定是终止条件的问题还是递归调用的问题。对吗？
>
> 我们先理清逻辑再碰代码。根据你教案中 'Recursion' 的方法，每个递归函数必须有两个部分：
> 1. **Base case（基准情况）**：什么时候停止递归？
> 2. **Recursive case（递归情况）**：怎么把问题缩小后再调用自己？
>
> #TODO: 用自然语言写出你的 base case 条件。它真的能在所有输入下被触发吗？
>
> 如果 base case 写对了但问题还在，试试在函数第一行加一句 `print(f"called with n={n}")`，看看实际调用了多少次。你预计应该调用多少次？

### 场景二：记忆软件工程术语

> **学生**：@learn dependency injection

> **Claude**：## Dependency Injection（依赖注入）

| 维度 | 内容 |
|------|------|
| **定义** | 将对象的依赖项从外部传入，而非对象内部自行创建。 |
| **记忆技巧** | `inject-`（注入）— 就像打针，药不是身体自己造的，而是从外部推进去的。 |
| **代码示例** | `class OrderService { constructor(private paymentGateway: PaymentGateway) {} }` — 这里 `paymentGateway` 不是 `OrderService` 自己 new 的，而是从构造器"注入"的。#TODO: 补全构造器参数的类型声明 |
| **对比** | vs Service Locator：DI 是被动接收依赖，Service Locator 是主动去要。DI 使依赖关系更透明。 |

**考试应用**：
> 考题（简答）："Explain the Dependency Inversion Principle (DIP) and how Dependency Injection implements it. (6 marks)"
>
> #TODO: 从 (1) DIP 定义 (2) DI 如何实现 DIP (3) 一个具体例子 三个维度作答，每维 2 marks。

### 场景三：生成思维导图并复习

> **学生**：@mindmap Sorting Algorithms

Claude 输出飞书大纲文本：

```
Sorting Algorithms（排序算法）

- Comparison-based（基于比较）
  - Quick Sort（快速排序）— O(n log n) avg
    - 分治法
    - 不稳定排序
  - Merge Sort（归并排序）— O(n log n) always
    - 分治法
    - 稳定排序
  - #TODO: O(n²) 的排序算法有哪些？

- Non-comparison（非比较）
  - Counting Sort（计数排序）
  - Radix Sort（基数排序）
```

💡 **使用提示**：将以上大纲文本粘贴到飞书思维笔记中，点击右上角「思维导图」图标即可生成脑图。

> **学生**：@mindmap fill

Claude 填充所有 `#TODO` 后输出完整版。

---

## 文件结构

```
uk-uni-tutor/
├── SKILL.md                              # 核心 Skill 定义文件（辅导逻辑、命令协议、阶梯定义）
├── README.md                             # 本文件
├── .gitignore                            # Git 忽略规则
│
├── references/                           # 参考资料（Skill 运行时按需查阅）
│   ├── academic-integrity.md             # 英国大学学术诚信规范
│   ├── harvard-referencing.md            # Harvard 引用格式指南
│   ├── socratic-prompts.md               # 按学科分类的苏格拉底式提问模板
│   ├── common-mistakes.md                # 各学科常见错误排查清单
│   ├── software-engineering-guide.md     # 软件工程专项参考资料（调试/设计模式/测试/Git）
│   ├── terminology-guide.md              # 术语表 + 考试答题模板 + 英文词根列表
│   ├── template-examples.md              # 预设逻辑答题模板范例（归纳法/反证法/假设检验等）
│   ├── mindmap-guide.md                  # 飞书思维导图大纲格式规范与模板
│   └── syllabus_index.json               # 本地生成的教案索引，不应公开提交
│
└── scripts/                              # 辅助脚本
    ├── parse_syllabus.py                 # 教案文件解析与知识点提取
    └── generate_practice.py              # 随机生成练习题（数学/编程）
```

### 各文件作用

| 文件 | 说明 |
|------|------|
| `SKILL.md` | Skill 的"大脑"：定义了从 L0 到 L3+ 的阶梯式帮助逻辑、`@learn`/`@mindmap`/`@extract-template` 等命令的完整协议，以及各学科（essay/数学/编程/实验报告/软件工程）的辅导流程。 |
| `references/academic-integrity.md` | 学术诚信红线：抄袭类型、勾结（collusion）、合同作弊（contract cheating）、AI 使用边界。SKILL.md 中的「铁律」直接引用此文件。 |
| `references/harvard-referencing.md` | Harvard 引用格式速查：in-text citation 和 reference list 的排版规则，按文献类型（书籍/期刊/网站等）分类。 |
| `references/socratic-prompts.md` | 按 8 个维度（Essay/数学/编程/实验报告/跨学科通用/软件工程/术语学习/模板与导图）组织的提问句式。SKILL.md 的"关键引导语"均来源于此。 |
| `references/common-mistakes.md` | 各学科高频错误排查：数学（代数/微积分/线性代数/统计）、编程（Python/算法/OOP）、软件工程（空指针/并发/循环依赖/测试覆盖率）。 |
| `references/software-engineering-guide.md` | 软件工程专项资料：二分注释调试法、SOLID 原则 + 设计模式速查、AAA 测试模式、Conventional Commits、圈复杂度。 |
| `references/terminology-guide.md` | 50+ 软件工程术语中英对照表、考试简答题 4 段式模板、30+ 英文词根/前缀/后缀记忆表。 |
| `references/template-examples.md` | 8 个预设答题模板：数学归纳法、反证法、直接推导、批判性评价 Essay、对比 Essay、算法设计与分析、Bug 诊断与修复、假设检验报告。 |
| `references/mindmap-guide.md` | 飞书思维笔记大纲文本格式规范、6 种导图类型的完整模板示例、中英双语节点设计约定。 |
| `scripts/parse_syllabus.py` | 解析英文教案文件（.md/.txt），提取章节结构和知识点关键词，支持 `--bilingual` 模式生成中英检索映射。 |
| `scripts/generate_practice.py` | 按学科生成随机练习题：数学 8 类题型 + 编程 7 类题型，每道题带 `#TODO` 留白。 |

---

## 依赖与环境要求

### 必需

- **[Claude Code](https://claude.ai/code)** — Skill 运行平台，需要有效的 Anthropic API 订阅
- **操作系统**：macOS / Linux / Windows（Claude Code 支持的全部平台）

### 可选

- **飞书账号**（免费版即可）— 将 `@mindmap` 生成的大纲文本粘贴到飞书思维笔记中生成可视化脑图
- **Anki**（免费）— 导入 `@learn` 生成的 CSV 抽认卡文件用于间隔重复记忆
- **Python 3.8+** — 仅在使用 `scripts/` 目录下的脚本时需要
- **教案文件**（.md / .txt / .pdf）— `@load-syllabus` 加载后启用教案驱动模式（不使用教案时 Skill 以通用模式运行）

## 隐私、版权与学术诚信

- 本 Skill 不会自动上传聊天记录、教案或用户文件。公开分享前，请删除个人信息、课程内部材料、版权教案和他人数据。
- `references/syllabus_index.json` 只适合在本地根据自己的教案生成，不应提交到公开仓库。
- Skill 只提供提问、分析框架和自检提示，不代写作业、不替用户完成可提交代码，也不绕过学校的学术诚信规则。

---

## 许可证

本项目基于 [MIT License](https://opensource.org/licenses/MIT) 开源。

---

## 贡献指南

欢迎提交 Issue 和 Pull Request。

- **Bug 反馈**：请在 Issue 中描述复现步骤和预期行为
- **功能建议**：请先开 Issue 讨论，确认设计方向后再提交 PR
- **学科扩展**：如需为其他学科（物理/化学/经济等）增加提问模板，请参考 `references/socratic-prompts.md` 的结构

---

## 相关链接

- GitHub 仓库：[https://github.com/F416-Y/uk-uni-tutor](https://github.com/F416-Y/uk-uni-tutor)
- Claude Code 官方文档：[https://docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code)
