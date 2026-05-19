# 术语学习指南

本文件提供软件工程常见术语表、考试简答题答题模板、以及常见英文词根前缀列表。
用于术语学习模式（`@learn`）的辅助参考。辅导时按需查阅。

---

## 一、软件工程常见术语表

### 面向对象编程 (Object-Oriented Programming)

| English Term | 中文译名 | 简短定义 |
|-------------|---------|---------|
| **Abstraction** | 抽象 | Hiding complex implementation details and exposing only essential features |
| **Encapsulation** | 封装 | Bundling data with methods that operate on that data, and restricting direct access to internal state |
| **Inheritance** | 继承 | A mechanism where a class derives properties and behaviour from a parent class |
| **Polymorphism** | 多态 | The ability of an object to take many forms; same interface, different underlying implementations |
| **Interface** | 接口 | A contract that defines a set of method signatures without implementation |
| **Abstract Class** | 抽象类 | A class that cannot be instantiated; may contain both abstract methods and concrete methods |
| **Method Overloading** | 方法重载 | Multiple methods with the same name but different parameter lists (compile-time polymorphism) |
| **Method Overriding** | 方法重写 | Subclass provides a specific implementation of a method defined in the parent class (runtime polymorphism) |

### 设计原则 (Design Principles)

| English Term | 中文译名 | 简短定义 |
|-------------|---------|---------|
| **Single Responsibility Principle (SRP)** | 单一职责原则 | A class should have only one reason to change |
| **Open/Closed Principle (OCP)** | 开闭原则 | Software entities should be open for extension but closed for modification |
| **Liskov Substitution Principle (LSP)** | 里氏替换原则 | Subtypes must be substitutable for their base types without altering correctness |
| **Interface Segregation Principle (ISP)** | 接口隔离原则 | Clients should not be forced to depend on interfaces they do not use |
| **Dependency Inversion Principle (DIP)** | 依赖倒置原则 | Depend upon abstractions, not concretions |
| **DRY (Don't Repeat Yourself)** | 不重复原则 | Every piece of knowledge must have a single, unambiguous representation |
| **KISS (Keep It Simple, Stupid)** | 保持简单 | Most systems work best if they are kept simple rather than made complicated |
| **YAGNI (You Aren't Gonna Need It)** | 你不会需要它 | Don't implement something until it is actually needed |

### 设计模式 (Design Patterns)

| English Term | 中文译名 | 简短定义 |
|-------------|---------|---------|
| **Singleton** | 单例模式 | Ensures a class has only one instance and provides a global point of access to it |
| **Factory Method** | 工厂方法 | Defines an interface for creating an object, but lets subclasses decide which class to instantiate |
| **Abstract Factory** | 抽象工厂 | Provides an interface for creating families of related or dependent objects |
| **Builder** | 建造者模式 | Separates the construction of a complex object from its representation |
| **Strategy** | 策略模式 | Defines a family of algorithms, encapsulates each one, and makes them interchangeable |
| **Observer** | 观察者模式 | Defines a one-to-many dependency so that when one object changes state, all dependents are notified |
| **Decorator** | 装饰器模式 | Attaches additional responsibilities to an object dynamically |
| **Adapter** | 适配器模式 | Converts the interface of a class into another interface clients expect |
| **Facade** | 外观模式 | Provides a unified interface to a set of interfaces in a subsystem |
| **Command** | 命令模式 | Encapsulates a request as an object |
| **Dependency Injection** | 依赖注入 | Dependencies are provided to a class rather than the class creating them |
| **MVC (Model-View-Controller)** | 模型-视图-控制器 | Separates application into data (Model), UI (View), and logic (Controller) layers |

### 测试与质量 (Testing & Quality)

| English Term | 中文译名 | 简短定义 |
|-------------|---------|---------|
| **Unit Test** | 单元测试 | Testing individual units/functions of source code in isolation |
| **Integration Test** | 集成测试 | Testing combined parts of an application to check if they work together |
| **TDD (Test-Driven Development)** | 测试驱动开发 | Writing tests before writing the code that makes the tests pass |
| **Mock Object** | 模拟对象 | A simulated object that mimics the behaviour of a real object in controlled ways |
| **Code Coverage** | 代码覆盖率 | A measure of how much source code is executed during testing |
| **Regression Test** | 回归测试 | Re-running tests to ensure new changes haven't broken existing functionality |
| **CI/CD** | 持续集成/持续部署 | Continuous Integration / Continuous Delivery — automating build, test, and deployment |

### 架构与设计 (Architecture & Design)

| English Term | 中文译名 | 简短定义 |
|-------------|---------|---------|
| **Microservices** | 微服务 | An architectural style where an application is composed of small, independent services |
| **MVC** | 模型-视图-控制器 | Separates application into data, UI, and logic layers |
| **RESTful API** | RESTful 接口 | An API that conforms to REST architectural constraints (stateless, resource-based) |
| **Coupling** | 耦合 | The degree of interdependence between software modules (lower is better) |
| **Cohesion** | 内聚 | The degree to which elements within a module belong together (higher is better) |
| **Technical Debt** | 技术债务 | The implied cost of additional rework caused by choosing an easy solution now instead of a better approach |
| **Refactoring** | 重构 | Restructuring existing code without changing its external behaviour |

### 并发 (Concurrency)

| English Term | 中文译名 | 简短定义 |
|-------------|---------|---------|
| **Thread** | 线程 | The smallest unit of execution within a process |
| **Race Condition** | 竞态条件 | When the behaviour of software depends on the timing or sequence of uncontrollable events |
| **Deadlock** | 死锁 | A situation where two or more threads are blocked forever, each waiting for the other |
| **Mutex** | 互斥锁 | A mutual exclusion object that prevents multiple threads from accessing a shared resource simultaneously |
| **Semaphore** | 信号量 | A variable used to control access to a common resource by multiple threads |
| **Atomic Operation** | 原子操作 | An operation that runs completely independently and is uninterruptible |

### 数据与算法 (Data & Algorithms)

| English Term | 中文译名 | 简短定义 |
|-------------|---------|---------|
| **Big O Notation** | 大 O 表示法 | Describes the upper bound of an algorithm's time or space complexity |
| **Hash Table** | 哈希表 | A data structure that maps keys to values using a hash function for fast lookup |
| **Binary Search Tree** | 二叉搜索树 | A tree where each node's left subtree contains only smaller values, right subtree only larger values |
| **Graph** | 图 | A collection of nodes (vertices) and edges connecting pairs of nodes |
| **Recursion** | 递归 | A method where the solution depends on solutions to smaller instances of the same problem |
| **Dynamic Programming** | 动态规划 | Breaking down a problem into simpler subproblems and caching results to avoid recomputation |

### 版本控制 (Version Control)

| English Term | 中文译名 | 简短定义 |
|-------------|---------|---------|
| **Commit** | 提交 | A snapshot of changes saved to the repository history |
| **Branch** | 分支 | A parallel version of the codebase that diverges from the main line of development |
| **Merge** | 合并 | Integrating changes from one branch into another |
| **Pull Request (PR)** | 拉取请求 | A request to merge changes from one branch into another, typically used for code review |
| **Conflict** | 冲突 | When two branches have made different changes to the same part of a file |
| **Stash** | 暂存 | Temporarily saving uncommitted changes to work on something else |

---

## 二、考试简答题答题模板

### 通用 4 段式模板

对于"Explain / Describe / Discuss [Term X]"类型的简答题（通常 4-6 marks），按以下结构作答：

```
1. Definition（定义）—— 1-2 marks
   直接给出精确定义，最好用术语的英文原文开头。
   模板："[English Term] refers to [definition]. 即 [中文解释]。"

2. Key Features / Characteristics（特点）—— 1-2 marks
   列出 2-3 个关键特征或组成部分。
   模板："It has the following key characteristics: (1) ... (2) ... (3) ..."

3. Example / Application（例子/应用）—— 1-2 marks
   给出一个具体例子或应用场景。
   模板："For example, in [场景], [术语] is used to [做什么]因为 [原因]。"
   如果是代码相关的术语，可附 2-3 行伪代码或简化的代码片段。

4. Pros & Cons / Comparison（优缺点/对比，可选）—— 1-2 marks
   如果题目要求 evaluate 或 compare，增加此段。
   模板："Compared to [对比对象], [术语] offers [优点] but may suffer from [缺点]."
```

### 填空/选择题策略

- 填空题的答案通常是**英文原词**（非中文翻译），注意大小写和拼写
- 选择题常考的是**概念区分**（如 overload vs override, abstract class vs interface, composition vs inheritance）
- 关注 each / every / always / never 等限定词——它们往往标志绝对性判断

### 高分要点

- 用**术语的英文原文**作答——英国大学考试通常要求精确使用专业术语
- 关键词（keywords/technical terms）是得分点——即使完整句子语法有瑕疵
- 例子要**具体**——不要说"常用于软件开发"，说"在 Java 的 Collections.sort() 中，传入不同的 Comparator 实现即 Strategy Pattern"
- 如果题目分值高（6+ marks），必须考虑反面观点（counterargument / limitations）

---

## 三、常见英文词根/前缀/后缀

### 面向对象/编程相关

| 词根/词缀 | 含义 | 示例 |
|-----------|------|------|
| **poly-** | many / 多 | polymorphism (多种形态), polygon (多边形) |
| **morph-** | form / 形态 | polymorphism, metamorphosis (变形) |
| **encapsul-** | enclose / 包裹 | encapsulation (封装), capsule (胶囊) |
| **inherit-** | receive from predecessor / 继承 | inheritance, heritage |
| **abstract-** | drawn away from concrete / 抽离 | abstraction, abstract (摘要) |
| **inter-** | between / 之间 | interface, interaction, internet |
| **instant-** | immediate / 立即 | instantiate (实例化), instance (实例) |
| **depend-** | rely on / 依赖 | dependency, independent |
| **inject-** | throw in / 注入 | injection, reject (拒绝), project (投射) |

### 算法/数据结构相关

| 词根/词缀 | 含义 | 示例 |
|-----------|------|------|
| **bi-** | two / 二 | binary (二进制), bisect (二分) |
| **re-** | again / 再次 | recursion (递归), reentrant (可重入的), refactor (重构) |
| **curs-** | run / 跑 | recursion, cursor (光标), excursion (远足) |
| **graph-** | write, draw / 写、画 | graph, graphic, autograph |
| **travers-** | go across / 穿越 | traverse (遍历), traversal |
| **iter-** | again / 重复 | iterate (迭代), reiterate (重申) |
| **algo-** | pain, work / 劳作 | algorithm (算法) |
| **complex-** | twisted together / 缠绕 | complexity (复杂度), complex |

### 通用学术词根

| 词根/词缀 | 含义 | 示例 |
|-----------|------|------|
| **-tion / -sion** | noun suffix / 名词后缀，表动作或状态 | abstraction, implementation, execution |
| **-ity** | noun suffix / 名词后缀，表性质 | modularity, scalability, maintainability |
| **-able / -ible** | adjective suffix / 形容词后缀，表"可以……的" | reusable, testable, extensible |
| **con-** | together / 一起 | concurrency, concurrent, convention |
| **de-** | down, away / 向下、分离 | decouple (解耦), decompose (分解), debug (调试) |
| **micro-** | small / 微小 | microservice, microarchitecture |
| **archi-** | chief, principal / 主要的 | architecture (架构), architect |

### 记忆技巧使用指南

辅导中给出记忆技巧时：
- 优先用词根分解法（最有普适性，能帮学生举一反三）
- 如果学生熟悉该术语的实际使用场景，用代码示意法
- 如果术语较抽象、词根不明显，用故事联想法
- 如果学生已学过类似术语，用对比记忆法

---

## 四、引用说明

辅导时在术语学习场景下查阅本文件，按以下方式引用：

```
根据 [[references/terminology-guide.md]] 中 [章节] 的 [内容]，
[中文指导]。
```

示例：
> 根据术语学习指南中「考试简答题答题模板」，你应该按 Definition → Key Features → Example → Pros/Cons 四段式作答。先写出 definition 的英文原文，再用中文解释。#TODO: 写出第一段 definition 部分。
