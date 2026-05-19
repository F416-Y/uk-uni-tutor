# 中英对照思维导图指南（飞书思维笔记版）

本文件提供飞书思维笔记（Feishu MindNotes）兼容的大纲文本格式规范、节点设计约定和各类导图模板。
供 `@mindmap` 功能调用。输出内容可直接粘贴到飞书思维笔记中生成脑图。

---

## 一、飞书大纲文本格式规范

### 基本规则

- 使用 `- ` 无序列表表示每个节点
- 使用 **2 个空格** 作为一级缩进（不是 Tab）
- 根节点独占一行，**不加** `- ` 前缀
- 子节点缩进层级 = 父节点缩进 + 2 空格

### 节点标签格式

```
- [English Term]（[中文翻译]）
- [English Term] — [简短描述]
- [English Term]（[中文翻译]）(ChX.Y)
```

- **英文术语**在前（考试默认语言），**中文翻译**在括号内
- 可选附件：教案出处 `(Ch3.2)`、复杂度 `O(n log n)`、关键提示等
- 描述性节点用 `—` 分隔英文和说明

### 节点标记约定

| 标记 | 含义 | 示例 |
|------|------|------|
| `(ChX.Y)` | 教案出处 | `- Singleton（单例模式）(Ch4.1)` |
| `#TODO: ...` | 要求学生填充 | `- #TODO: 第三种类型是？` |
| `[非教案]` | 教案未覆盖的外部内容 | `- [非教案] Visitor Pattern（访问者模式）` |
| `O(...)` | 复杂度标注 | `- Quick Sort（快速排序）O(n log n) avg` |
| `**粗体**` | 重点/高频考点 | `- **Polymorphism**（多态）— 必考` |

### 连线/关系表示

在飞书大纲中，关系通过层级结构隐式表达。需要标注关系类型时：

```
- Parent（父概念）
  - Child（子概念）—— applies to（适用于）
  - Child（子概念）—— has-a（拥有关系）
```

对于跨分支关系，在节点后加注释：
```
- Observer Pattern（观察者模式）—— 关联 → Mediator Pattern（中介者模式）
```

---

## 二、节点设计规范

### 节点层级原则

- 根节点：主题名称（英文 + 中文）
- 一级分支：主要分类/步骤/对比维度（2-6 个）
- 二级分支：具体概念/方法/特征
- 三级分支：示例/细节/注意事项（按需，不超过 2 层深度）

### 颜色/样式的替代方案

飞书大纲不支持 CSS class，改用前缀标记区分节点类型：

| 原 Mermaid Class | 飞书替代方案 |
|-----------------|-------------|
| `core`（蓝色核心概念） | `**粗体**` 包裹核心概念 |
| `todo`（黄色 #TODO） | `#TODO:` 前缀 |
| `method`（绿色方法） | 节点末尾加方法特征，如 `O(n log n)` 或 `(定理)` |
| `example`（橙色示例） | `示例：` 前缀或独立子节点 |
| `external`（灰色外部） | `[非教案]` 前缀 |

---

## 三、各类型导图完整模板

### 类型 1：概念层级图 (`@mindmap <topic>`)

**示例**：`@mindmap Design Patterns`

```
Design Patterns（设计模式）
- **Creational Patterns**（创建型模式）
  - Singleton（单例模式）(Ch4.1)
    - 唯一实例
    - 全局访问点
  - Factory Method（工厂方法）(Ch4.2)
    - 子类决定实例化哪个类
  - #TODO: 还有哪种创建型模式？
- **Structural Patterns**（结构型模式）
  - Adapter（适配器）(Ch5.1)
    - 转换接口以匹配客户端期望
  - Decorator（装饰器）(Ch5.3)
    - 动态附加额外职责
  - #TODO: 补充剩余结构型模式
- **Behavioral Patterns**（行为型模式）
  - #TODO: 列举至少 3 种行为型模式
```

### 类型 2：对比图 (`@mindmap compare <A> <B>`)

**示例**：`@mindmap compare Abstract Class Interface`

```
Abstract Class vs Interface（抽象类 vs 接口）
- **Abstract Class**（抽象类）
  - 可以有字段（instance fields）
  - 可以有构造器（constructor）
  - 方法可有实现体（method body）
  - 单继承（single inheritance）
  - #TODO: Java 8+ default method 对此有何影响？
- **Interface**（接口）
  - 无实例字段（no instance fields）
  - 无构造器体（no constructor body）
  - 全部方法为抽象（all abstract）
  - 多实现（multiple implementation）
- **共同点**（Shared）
  - 都定义契约（define a contract）
  - 都是抽象机制（abstraction）
  - 都不能直接实例化（cannot instantiate）
```

### 类型 3：流程/步骤图 (`@mindmap process <topic>`)

**示例**：`@mindmap process Binary Search`

```
Binary Search（二分查找）— 流程
- 输入：有序数组 + 目标值（sorted array + target）
- 步骤 1：初始化指针
  - left = 0, right = n-1
- 步骤 2：循环判断 left <= right?
  - Yes → 继续搜索
    - mid = left + (right - left) / 2
    - 判断 arr[mid] == target?
      - 命中 → 返回 mid（找到）
      - target < arr[mid] → right = mid - 1（搜左半）
      - #TODO: target > arr[mid] → ?
  - No → 搜索空间耗尽
    - 返回 -1（未找到）
- 复杂度：O(log n) time, O(1) space
```

### 类型 4：分类图 (`@mindmap types <topic>`)

**示例**：`@mindmap types Sorting Algorithms`

```
Sorting Algorithms（排序算法）— 分类
- **Comparison-based**（基于比较）
  - Quick Sort（快速排序）O(n log n) avg
    - 分治法（Divide & Conquer）
    - 不稳定（Unstable）
  - Merge Sort（归并排序）O(n log n) always
    - 分治法（Divide & Conquer）
    - 稳定（Stable）
  - #TODO: O(n²) 的排序算法有哪些？
- **Non-comparison**（非比较）
  - Counting Sort（计数排序）
    - 前提：整数、范围已知
  - Radix Sort（基数排序）
    - 按位排序，从低位到高位
  - #TODO: 还有哪种非比较排序？
```

### 类型 5：关系图 (`@mindmap relations <topic>`)

展示概念间交叉关系，使用注释标注跨分支关联。

**示例**：`@mindmap relations SOLID Principles`

```
SOLID Principles（SOLID 原则）— 关系
- **SRP**（单一职责原则）
  - 一个类只有一个变化的原因
  - 关联 → High Cohesion（高内聚）
- **OCP**（开闭原则）
  - 对扩展开放，对修改关闭
  - 实现手段 → Strategy Pattern, Decorator Pattern
- **LSP**（里氏替换原则）
  - 子类型必须可替换基类型
  - 前提 → OCP 的基础
- **ISP**（接口隔离原则）
  - 客户端不应依赖不使用的接口
  - 关联 → SRP（接口层面）
- **DIP**（依赖倒置原则）
  - 依赖抽象，不依赖具体
  - 实现手段 → Dependency Injection, Factory Pattern
```

### 类型 6：章节全景图 (`@mindmap chapter <N>`)

基于已加载教案的章节内容自动生成。必须：
- 读取教案 Chapter N 的完整结构
- 按章节小节层级构建节点树
- 每个小节节点下挂对应的 method/example/key concept
- 教案未覆盖的部分标注 `[非教案]`

---

## 四、中英文双语处理规范

| 元素 | 语言规则 |
|------|---------|
| 根节点 | `English Name（中文名称）` |
| 子节点第一语言 | **英文原文**（考试中使用的术语） |
| 子节点中文 | 紧随英文，用全角括号 `（）` 包裹 |
| 可选附件 | 教案出处 / 复杂度 / 关键提示，紧跟中文后 |
| 描述性文字 | 英文 + ` — ` + 中文说明 |
| `#TODO` 标记 | 中文描述任务：`#TODO: 第三个特点是什么？` |
| `[非教案]` 标记 | 前缀 + 英文术语 + 中文翻译 |

---

## 五、导图生成后的交互

生成导图后，Claude 必须提供以下后续操作入口 + 使用提示：

```
💡 使用提示：将以上大纲文本粘贴到飞书思维笔记中，点击右上角「思维导图」图标即可生成脑图。

你可以：
- 输入 "@mindmap fill" 查看完整版（填充所有 #TODO）
- 输入 "@extract-template" 基于本导图提炼答题模板
- 输入 "补充节点：xxx" 在导图中添加新内容
- 输入这个导图中某个 #TODO 的答案，我会帮你检查
- 输入 "@learn <术语>" 深入学习导图中的任一术语
```

### 综合复习模式

用户说"综合复习"或"@mindmap review"时：
1. 提取对话历史中最近生成的所有导图
2. 将同课程的导图串联成更大的知识网络
3. 将所有 `#TODO` 汇总为一个复习清单，一次性展示给学生

---

## 六、学术诚信与导图

- ✅ 生成知识结构的**可视化框架**
- ✅ 用 `#TODO` 留白让学生自己填充
- ✅ 标注教案和非教案内容的边界
- ❌ 不在导图中直接呈现完整的考试答案结构
- ❌ 不将标准答案的每一步都填充完整后交给学生
- ❌ 不为学生"代画"可提交的作业图表

---

## 七、格式对照：Mermaid → 飞书大纲

| Mermaid 写法 | 飞书大纲写法 |
|-------------|-------------|
| `A["Singleton<br/>单例"] --> B["唯一实例"]` | `- Singleton（单例）` 下一行缩进 `  - 唯一实例` |
| `classDef todo fill:#FFD700` | `#TODO:` 前缀 |
| `classDef external fill:#CCC` | `[非教案]` 前缀 |
| `A -->\|"applies to"\| B` | 子节点后加 `—— applies to` |
| `subgraph Left[...]` | 同级节点分组，用 `**粗体**` 包裹组名 |
| `Decision{"条件?"}` | `- 判断：条件?` + 子节点 Yes/No 分支 |
