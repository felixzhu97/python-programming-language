# 第 11 章 测试代码

## 学习目标

通过本章的学习，您将能够：

1. 理解为什么需要测试代码
2. 掌握 Python 的 unittest 模块
3. 学会编写测试函数和测试类
4. 了解测试驱动开发（TDD）的基本概念
5. 使用 Mock 对象进行测试
6. 组织和运行测试套件

## 文件说明

### 核心文件

1. **test_basics.py** - 测试基础知识

   - unittest 模块基础用法
   - 常用断言方法
   - 测试组织和执行
   - 高级测试特性（setUp、tearDown 等）

2. **test_functions.py** - 函数测试

   - 测试返回值的函数
   - 测试有参数的函数
   - 测试异常情况
   - 使用 Mock 对象测试外部依赖

3. **test_classes.py** - 类测试

   - 测试类的初始化
   - 测试类的方法和属性
   - 测试继承关系
   - 使用 setUp 和 tearDown 管理测试状态

4. **exercises.py** - 章节练习
   - 练习 11-1：城市和国家
   - 练习 11-2：人口数量
   - 练习 11-3：雇员类测试
   - 额外练习题

## 重要概念

### 1. 单元测试

单元测试是对程序中最小可测试单元的检查和验证，通常是一个函数或方法。

### 2. 测试用例（Test Case）

一个测试用例是一个独立的测试单元，用来检查特定输入下的特定响应。

### 3. 测试套件（Test Suite）

测试套件是多个测试用例的集合。

### 4. 断言（Assertion）

断言是测试中的检查点，用来验证程序的行为是否符合预期。

## 常用断言方法

| 断言方法                        | 作用                  |
| ------------------------------- | --------------------- |
| `assertEqual(a, b)`             | 检查 a == b           |
| `assertNotEqual(a, b)`          | 检查 a != b           |
| `assertTrue(x)`                 | 检查 bool(x) is True  |
| `assertFalse(x)`                | 检查 bool(x) is False |
| `assertIs(a, b)`                | 检查 a is b           |
| `assertIsNot(a, b)`             | 检查 a is not b       |
| `assertIsNone(x)`               | 检查 x is None        |
| `assertIsNotNone(x)`            | 检查 x is not None    |
| `assertIn(a, b)`                | 检查 a in b           |
| `assertNotIn(a, b)`             | 检查 a not in b       |
| `assertRaises(exc, fun, *args)` | 检查异常              |
| `assertAlmostEqual(a, b)`       | 检查近似相等          |
| `assertGreater(a, b)`           | 检查 a > b            |
| `assertLess(a, b)`              | 检查 a < b            |

## 运行测试的方法

### 1. 运行单个文件的所有测试

```bash
python test_basics.py
python -m unittest test_basics
```

### 2. 运行特定测试类

```bash
python -m unittest test_basics.TestBasicFunctions
```

### 3. 运行特定测试方法

```bash
python -m unittest test_basics.TestBasicFunctions.test_add_positive_numbers
```

### 4. 详细输出

```bash
python -m unittest -v test_basics
```

### 5. 发现并运行所有测试

```bash
python -m unittest discover
python -m unittest discover -s . -p "test_*.py"
```

## 测试最佳实践

### 1. 测试组织

- 每个测试方法只测试一个功能
- 使用描述性的测试方法名
- 将相关测试组织在同一个测试类中

### 2. 测试覆盖

- 测试正常情况和边界条件
- 测试异常情况
- 测试各种输入类型

### 3. 测试独立性

- 每个测试应该独立运行
- 使用 setUp 和 tearDown 管理测试状态
- 不要依赖其他测试的结果

### 4. 使用 Mock

- 对外部依赖使用 Mock 对象
- 模拟网络请求、文件操作等
- 专注于测试自己的代码逻辑

## 高级特性

### 1. 参数化测试

使用`subTest`进行参数化测试：

```python
def test_multiple_cases(self):
    test_cases = [(1, 2, 3), (4, 5, 9)]
    for a, b, expected in test_cases:
        with self.subTest(a=a, b=b):
            self.assertEqual(add(a, b), expected)
```

### 2. 跳过测试

```python
@unittest.skip("暂时跳过")
def test_feature(self):
    pass

@unittest.skipIf(condition, "条件跳过")
def test_conditional(self):
    pass
```

### 3. 预期失败

```python
@unittest.expectedFailure
def test_known_bug(self):
    self.assertEqual(1, 2)  # 已知会失败
```

## 测试驱动开发（TDD）

TDD 的基本流程：

1. **红色**：编写一个失败的测试
2. **绿色**：编写最少的代码使测试通过
3. **重构**：改进代码质量，保持测试通过

## 常见错误

1. **测试依赖性**：测试之间相互依赖
2. **测试范围过大**：一个测试测试太多功能
3. **忽略边界条件**：只测试正常情况
4. **缺少异常测试**：没有测试错误处理
5. **硬编码数据**：在测试中使用固定的外部数据

## 实际应用

测试在实际开发中的重要作用：

1. **确保代码质量**：及早发现 bug
2. **重构保障**：安全地修改代码
3. **文档作用**：测试代码展示如何使用 API
4. **回归测试**：确保新功能不破坏现有功能
5. **持续集成**：自动化测试流程

## 练习建议

1. 从简单函数开始练习编写测试
2. 逐步过渡到复杂类的测试
3. 练习使用 Mock 对象
4. 尝试测试驱动开发方法
5. 关注测试覆盖率，但不要盲目追求 100%

通过系统学习和实践这些测试技能，您将能够编写更可靠、更易维护的 Python 代码。
