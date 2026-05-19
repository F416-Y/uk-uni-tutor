# 软件工程辅导指南

本文件提供软件工程常见主题的参考资料，用于辅导时的概念确认和方法提示。
所有术语保留英文原文，配合中文解释。辅导时按需查阅。

---

## 一、调试策略 (Debugging Strategies)

### 二分注释法 (Binary Comment-out Method)

将代码一分为二，注释掉一半运行，逐步缩小 bug 位置：

```
步骤：
1. 注释掉后半段代码，运行程序
2. bug 还存在 → bug 在前半段 → 继续二分前半段
3. bug 消失   → bug 在后半段 → 继续二分后半段
4. 重复直到定位到 1-2 行
```

### 普通调试流程

| 阶段 | 英文 | 中文 | 操作 |
|------|------|------|------|
| 隔离 | Isolate | 隔离问题 | 找到精确的错误触发位置（哪个函数、哪一行、什么输入） |
| 假设 | Hypothesise | 提出假设 | "我认为错误原因是 X，因为……" |
| 验证 | Test | 验证假设 | 加 print / 断点 / 修改一行 → 运行 → 看是否符合预期 |
| 修复 | Fix | 修复 | 修改代码 → 运行全部测试 → 确认不引入新 bug |
| 复盘 | Reflect | 反思 | "为什么我会犯这个错？下次怎么避免？" |

### 常见调试工具对照

| 语言 | print/style="color:red">logging | 断点 (Breakpoint) |
|------|-----------|-------------------|
| Python | `print(f"DEBUG: {var=}")` / `logging.debug()` | `breakpoint()` (Python 3.7+) / `import pdb; pdb.set_trace()` |
| Java | `System.out.println("DEBUG: " + var)` / `java.util.logging` | IDE breakpoint / `assert` |
| JavaScript | `console.log({var})` / `console.trace()` | `debugger;` / Chrome DevTools |
| C/C++ | `printf("DEBUG: %d\n", var)` / `fprintf(stderr, ...)` | GDB: `break <line>; run; print <var>` |

### 辅导要点

- 永远让学生先描述 Expected Behaviour vs Actual Behaviour
- 不要帮学生看代码找 bug——让他们先二分注释缩小范围
- 诊断出 bug 后，让学生自己解释"为什么会犯这个错"，不做裁决

---

## 二、设计模式 (Design Patterns)

### 常用模式及适用场景

| 模式 (Pattern) | 意图 (Intent) | 适用场景 (中文) |
|---------------|---------------|----------------|
| **Singleton** | Ensure a class has only one instance | 全局配置、日志器、数据库连接池。注意：过度使用会引入全局状态 |
| **Factory Method** | Define an interface for creating an object, but let subclasses decide which class to instantiate | 不确定运行时需要哪种具体类型时；创建逻辑需要集中管理 |
| **Abstract Factory** | Provide an interface for creating families of related objects | 需要创建一组相关的对象（如不同 OS 的 UI 组件） |
| **Builder** | Separate the construction of a complex object from its representation | 对象构造参数多、步骤复杂；需要不同配置生成不同变体 |
| **Strategy** | Define a family of algorithms, encapsulate each one, and make them interchangeable | 同一行为有多种算法（如不同排序方式、不同支付方式） |
| **Observer** | Define a one-to-many dependency so that when one object changes state, all dependents are notified | 事件监听、发布-订阅系统、MVC 中的 View 观察 Model |
| **Decorator** | Attach additional responsibilities to an object dynamically | 需要在不修改原类的前提下增加功能（如给输入流加缓冲、加密） |
| **Adapter** | Convert the interface of a class into another interface clients expect | 复用旧代码但接口不兼容；对接第三方库 |
| **Facade** | Provide a unified interface to a set of interfaces in a subsystem | 子系统复杂，需要简化的入口；分层架构中层间通信 |
| **Command** | Encapsulate a request as an object | 撤销/重做、任务队列、宏命令录制 |
| **Dependency Injection** | Dependencies are provided to a class rather than the class creating them | 解耦、可测试性（mock 依赖注入）、遵循 DIP 原则 |

### SOLID 原则速查

| 缩写 | 原则 (English) | 中文 |
|------|---------------|------|
| **S** | Single Responsibility Principle | 一个类只做一件事 |
| **O** | Open/Closed Principle | 对扩展开放，对修改关闭 |
| **L** | Liskov Substitution Principle | 子类可以替代父类而不破坏程序 |
| **I** | Interface Segregation Principle | 接口应该小而专，不应强迫 client 依赖不需要的方法 |
| **D** | Dependency Inversion Principle | 依赖抽象而非具体实现 |

### 辅导要点

- 让学生先描述 Context（上下文）、Constraints（约束）、What varies（变化点）
- 提问"回忆教案中 XX pattern 的 intent 是什么？"，不给类图
- 确认学生自己画出 UML 草图后再讨论设计细节

---

## 三、单元测试 (Unit Testing)

### Arrange-Act-Assert (AAA) 模式

```
@Test
void test_methodName_scenario_expectedBehaviour() {
    // Arrange（准备）：设置测试数据和 mock 对象
    Calculator calc = new Calculator();

    // Act（执行）：调用被测方法
    int result = calc.add(2, 3);

    // Assert（断言）：验证结果是否符合预期
    assertEquals(5, result);
}
```

### 测试用例设计矩阵

| 类别 | 英文 | 示例 |
|------|------|------|
| 正常情况 | Happy Path / Normal Case | 传入典型输入 (2, 3)，期望正确结果 5 |
| 边界情况 | Edge Case / Boundary | 空列表、null、0、负数、最大/最小值 |
| 异常情况 | Error Case / Exception | 传入非法参数期望抛出 IllegalArgumentException |
| 并发场景 | Concurrency | 多线程同时调用是否线程安全 |

### 测试命名规范

```
test_[methodName]_[scenario]_[expectedBehaviour]

示例：
  test_add_negativeNumbers_returnsCorrectSum
  test_divide_byZero_throwsArithmeticException
  test_findById_emptyList_returnsEmptyOptional
```

### FIRST 原则

| 字母 | 原则 (English) | 含义 (中文) |
|------|---------------|-----------|
| **F** | Fast | 测试应该快速运行（秒级，不依赖网络/数据库） |
| **I** | Independent | 测试之间不依赖，可以任意顺序运行 |
| **R** | Repeatable | 每次运行结果一致（不依赖外部状态/时间） |
| **S** | Self-Validating | 测试自己判断 pass/fail（用断言，不用人眼检查） |
| **T** | Timely | 在写实现代码前或同时写测试（TDD） |

### 辅导要点

- **先写测试，后写实现**——即使学生不习惯
- 测试名要可见意图：test_[method]_[scenario]_[expectedResult]
- 一个 test 只测一个 behaviour
- 覆盖率工具：JaCoCo (Java)、coverage.py (Python)、Istanbul (JS)

---

## 四、Git 提交规范 (Git Conventional Commits)

### Conventional Commits 格式

```
<type>(<scope>): <short description>

[optional body — what and why, not how]

[optional footer — BREAKING CHANGE, issue references]
```

### 常用 Type

| Type | 含义 (中文) | 使用场景 |
|------|-----------|---------|
| `feat` | 新功能 | 新增一个 feature / endpoint / 页面 |
| `fix` | 修复 bug | 修正一个逻辑/空指针/异常 |
| `refactor` | 重构 | 改代码结构但不改外部行为 |
| `test` | 测试 | 添加或修改测试 |
| `docs` | 文档 | README、注释、API 文档 |
| `style` | 格式 | 缩进、空格、分号（不影响逻辑） |
| `chore` | 杂务 | 依赖更新、构建脚本、CI 配置 |
| `perf` | 性能优化 | 提升性能的改动 |

### 示例

```
feat(login): add OAuth2 authentication via Google

Users can now sign in with their Google account. A new OAuth2Config
class handles the redirect and token exchange flow.

Closes #42
```

```
fix(api): correct null pointer when user profile is empty

Previously, calling GET /users/{id}/profile for a newly registered
user caused NPE because profile was null. Now returns empty Profile
object.

Fixes #137
```

### Git Branching 常见策略

| 策略 | 描述 |
|------|------|
| Git Flow | main + develop + feature/* + release/* + hotfix/* |
| GitHub Flow | main + feature/*（一个 PR 一个 branch，review 后 squish merge） |
| Trunk-Based | 所有人都往 main 提交小改动，用 feature flag 控制未完成的功能 |

### 辅导要点

- 让学生先跑 `git status` / `git log --oneline` / `git diff` 看状态
- 绝不帮学生跑任何 git 命令——只提示命令名称
- 提交前让学生自己说出"我改了什么 + 为什么"

---

## 五、代码复杂度 (Code Complexity)

### 圈复杂度 (Cyclomatic Complexity)

```
CC = E - N + 2P （或简单数法：if/for/while/case/catch/&&/|| 的数量 + 1）

CC 评估：
  1-5  : 简单，容易测试
  6-10 : 较复杂，建议拆函数
  11-20: 复杂，必须拆解
  20+  : 高风险，强烈建议重构
```

### 其他指标

| 指标 | 英文 | 含义 | 合理范围 |
|------|------|------|---------|
| 函数长度 | Method Lines | 一个函数/方法的行数 | < 20 行（理想）；< 50 行（可接受） |
| 参数数量 | Parameter Count | 函数形参个数 | < 4 个 |
| 嵌套层级 | Nesting Depth | if/for 的最深层数 | < 4 层 |
| 扇入 | Fan-in | 被多少其他模块调用 | 越高越好（复用率高） |
| 扇出 | Fan-out | 依赖多少其他模块 | < 7（超过说明职责过多） |
| 类耦合度 | Coupling Between Objects | 一个类依赖其他类的数量 | < 10 |

### Uncle Bob's Clean Code 核心规则（辅导引用）

1. 函数应该小，且只做一件事 (Functions should do one thing)
2. 命名要精确表达意图 (Names should reveal intent)
3. 注释应该解释 WHY，不是 WHAT（好的命名已经说明了 WHAT）
4. 不写重复代码 (DRY - Don't Repeat Yourself)
5. 错误处理不要打乱正常逻辑 (Error handling is one thing)

### 辅导要点

- 让学生数自己的圈复杂度——"你这个函数有几个 if/for/while？"
- 变量名是否自注释 (self-documenting)："x1、data、tmp——这些变量名的含义是什么？"
- magic number → 定义为命名常量

---

## 六、引用说明

辅导时在 SE 相关场景下查阅本文件，按以下方式引用：

```
根据 [[references/software-engineering-guide.md]] 中 [章节] 的 [概念]，
你应该 [中文指导]。因为该指南指出："[关键英文原文]"，意思是 [中文解释]。
```

示例：
> 根据软件工程指南中「单元测试」的 FIRST 原则，你的测试应该满足 Independent（独立）——测试之间不共享状态。你现在的 test B 依赖 test A 的 side effect 吗？
