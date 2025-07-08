# 第 11 章 - 测试代码

## 📖 本章概述

测试是软件开发中的重要环节。本章将学习如何使用 Python 的 unittest 模块编写测试代码，确保程序的正确性和可靠性。

## 🎯 学习目标

- 理解测试的重要性和类型
- 掌握 unittest 框架的使用
- 学习测试函数和类的方法
- 了解测试驱动开发(TDD)
- 掌握 Mock 对象的使用

## 📚 主要内容

### 1. 测试基础

- 测试的概念和重要性
- unittest 模块介绍
- 测试用例的编写
- 断言方法的使用

### 2. 测试函数

- 单元测试的编写
- 测试覆盖率
- 边界条件测试
- 异常情况测试

### 3. 测试类

- 类方法的测试
- setUp 和 tearDown 方法
- 测试夹具的使用
- 测试继承关系

### 4. 高级测试技术

- Mock 对象的使用
- 参数化测试
- 测试跳过和预期失败
- 性能测试

## 📄 文件说明

| 文件名              | 描述     | 主要内容                            |
| ------------------- | -------- | ----------------------------------- |
| `test_basics.py`    | 测试基础 | unittest 基础、断言方法、测试结构   |
| `test_functions.py` | 函数测试 | 函数单元测试、Mock 使用、参数化测试 |
| `test_classes.py`   | 类测试   | 类方法测试、继承测试、复杂场景      |
| `exercises.py`      | 章节练习 | 11-1 到 11-3 练习题解答             |

## 🚀 快速开始

```bash
# 运行测试基础演示
python test_basics.py

# 运行函数测试演示
python test_functions.py

# 运行类测试演示
python test_classes.py

# 查看练习解答
python exercises.py

# 使用unittest运行测试
python -m unittest test_basics.py -v
```

## 💡 重要概念

### 基本测试结构

```python
import unittest

class TestMyFunction(unittest.TestCase):

    def setUp(self):
        """每个测试方法执行前调用"""
        self.test_data = [1, 2, 3, 4, 5]

    def test_function_behavior(self):
        """测试函数的正常行为"""
        result = my_function(self.test_data)
        self.assertEqual(result, expected_value)

    def test_edge_cases(self):
        """测试边界情况"""
        result = my_function([])
        self.assertIsNone(result)

    def tearDown(self):
        """每个测试方法执行后调用"""
        pass

if __name__ == '__main__':
    unittest.main()
```

### 常用断言方法

```python
# 相等性断言
self.assertEqual(a, b)      # a == b
self.assertNotEqual(a, b)   # a != b

# 真值断言
self.assertTrue(expr)       # expr is True
self.assertFalse(expr)      # expr is False

# 成员断言
self.assertIn(a, b)         # a in b
self.assertNotIn(a, b)      # a not in b

# 异常断言
with self.assertRaises(ValueError):
    function_that_should_raise_error()
```

## 🔧 练习建议

1. **基础测试练习**

   - 为简单函数编写测试
   - 练习不同的断言方法
   - 测试边界条件

2. **高级测试练习**

   - 测试类的方法
   - 使用 Mock 对象
   - 编写参数化测试

3. **TDD 实践**
   - 先写测试，再写代码
   - 重构代码并保持测试通过
   - 提高测试覆盖率

## 🎯 本章要点

- ✅ 测试确保代码的正确性
- ✅ unittest 是 Python 标准测试框架
- ✅ 好的测试应该快速、独立、可重复
- ✅ 测试驱动开发提高代码质量
- ✅ Mock 对象帮助测试复杂依赖

## 🌟 实际应用示例

### 银行账户测试

```python
import unittest
from unittest.mock import patch

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(100)

    def test_initial_balance(self):
        new_account = BankAccount()
        self.assertEqual(new_account.balance, 0)

    def test_deposit_positive_amount(self):
        result = self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
        self.assertEqual(result, 150)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_withdraw_sufficient_funds(self):
        result = self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)
        self.assertEqual(result, 70)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)
```

### 测试统计信息

```python
class TestStatistics:
    """测试运行统计"""

    def __init__(self):
        self.tests_run = 0
        self.tests_passed = 0
        self.tests_failed = 0

    def record_test(self, passed):
        self.tests_run += 1
        if passed:
            self.tests_passed += 1
        else:
            self.tests_failed += 1

    def get_success_rate(self):
        if self.tests_run == 0:
            return 0
        return (self.tests_passed / self.tests_run) * 100
```

## 🔗 相关章节

- **第 8 章** - 函数：测试函数的编写
- **第 9 章** - 类：测试类的方法
- **第 10 章** - 文件和异常：测试文件操作和异常处理
- **项目篇** - 实际项目中的测试应用

---

> 💡 **提示**：测试是专业软件开发的重要组成部分，养成编写测试的习惯将大大提高你的代码质量！
