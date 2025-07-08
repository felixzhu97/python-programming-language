# 第 08 章 函数

## 学习目标

本章将学习 Python 中函数的概念和使用方法。函数是组织代码的重要工具，能够提高代码的复用性、可读性和可维护性。

### 核心概念

1. **函数定义**：如何创建和定义函数
2. **函数参数**：位置参数、关键字参数、默认参数、可变参数
3. **函数返回值**：return 语句的使用和多种返回值类型
4. **函数作用域**：全局变量和局部变量的概念
5. **模块化编程**：创建和使用模块
6. **函数设计原则**：编写高质量函数的最佳实践

## 文件说明

### 核心文件

| 文件名                   | 说明           | 核心内容                           |
| ------------------------ | -------------- | ---------------------------------- |
| `function_basics.py`     | 函数基础知识   | 函数定义、调用、作用域、文档字符串 |
| `function_parameters.py` | 函数参数详解   | 各种参数类型、参数解包、参数验证   |
| `function_return.py`     | 函数返回值详解 | 返回值类型、多返回值、条件返回     |
| `function_modules.py`    | 函数模块详解   | 模块导入、创建模块、模块组织       |
| `exercises.py`           | 章节练习解答   | 练习 8-1 到 8-17 的完整解答        |
| `README.md`              | 学习指导文档   | 学习路径、重要概念、最佳实践       |

### 学习路径

```
1. function_basics.py      →  掌握函数基础概念
2. function_parameters.py  →  深入理解函数参数
3. function_return.py      →  掌握函数返回值
4. function_modules.py     →  学习模块化编程
5. exercises.py           →  实践练习巩固
6. 综合项目应用           →  创建模块化程序
```

## 重要概念详解

### 1. 函数定义和调用

```python
# 基本函数定义
def greet_user(name):
    """向用户显示问候语"""
    print(f"Hello, {name}!")

# 调用函数
greet_user("Alice")
```

**要点：**

- 使用`def`关键字定义函数
- 函数名应该描述函数的功能
- 使用文档字符串说明函数用途
- 函数调用时传递必要的参数

### 2. 函数参数类型

```python
# 位置参数
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# 关键字参数
describe_pet(animal_type="dog", pet_name="Willie")

# 默认参数
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# 可变参数
def make_pizza(size, *toppings):
    print(f"Making a {size}-inch pizza with toppings:")
    for topping in toppings:
        print(f"- {topping}")

# 关键字参数
def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile
```

### 3. 函数返回值

```python
# 返回简单值
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# 返回字典
def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

# 返回多个值
def get_name_parts(full_name):
    parts = full_name.split()
    return parts[0], parts[-1]
```

### 4. 模块化编程

```python
# 导入整个模块
import math
print(math.sqrt(16))

# 导入特定函数
from math import sqrt
print(sqrt(16))

# 使用别名
import math as m
from math import sqrt as square_root
```

## 实际应用场景

### 1. 数据处理函数

```python
def clean_data(data):
    """清理数据，移除空值和无效数据"""
    return [item for item in data if item is not None and item != '']

def calculate_average(numbers):
    """计算平均值"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def format_currency(amount):
    """格式化货币显示"""
    return f"${amount:.2f}"
```

### 2. 用户界面函数

```python
def display_menu():
    """显示主菜单"""
    print("\n=== 主菜单 ===")
    print("1. 添加项目")
    print("2. 查看项目")
    print("3. 删除项目")
    print("4. 退出")

def get_user_choice():
    """获取用户选择"""
    while True:
        choice = input("请选择操作 (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        print("无效选择，请重试。")
```

### 3. 验证和处理函数

```python
def validate_email(email):
    """验证邮箱格式"""
    return '@' in email and '.' in email

def validate_age(age):
    """验证年龄"""
    try:
        age = int(age)
        return 0 <= age <= 150
    except ValueError:
        return False

def process_user_input(user_data):
    """处理用户输入数据"""
    errors = []

    if not user_data.get('name'):
        errors.append('姓名不能为空')

    if not validate_email(user_data.get('email', '')):
        errors.append('邮箱格式不正确')

    if not validate_age(user_data.get('age', '')):
        errors.append('年龄不合理')

    return len(errors) == 0, errors
```

## 函数设计原则

### 1. 单一职责原则

```python
# 好的设计：每个函数只做一件事
def calculate_tax(price, tax_rate):
    """只负责计算税费"""
    return price * tax_rate

def format_price(price):
    """只负责格式化价格"""
    return f"${price:.2f}"

def get_total_price(price, tax_rate):
    """组合使用多个函数"""
    tax = calculate_tax(price, tax_rate)
    total = price + tax
    return format_price(total)
```

### 2. 参数设计

```python
# 参数顺序：必需参数 -> 默认参数 -> *args -> **kwargs
def process_order(customer_name, items, discount=0.0, *extras, **options):
    """处理订单"""
    pass

# 使用类型提示
def calculate_area(length: float, width: float) -> float:
    """计算矩形面积"""
    return length * width
```

### 3. 错误处理

```python
def safe_divide(dividend, divisor):
    """安全的除法运算"""
    try:
        if divisor == 0:
            return None, "除数不能为零"

        result = dividend / divisor
        return result, "计算成功"

    except TypeError:
        return None, "参数必须是数字"
    except Exception as e:
        return None, f"未知错误：{e}"
```

## 模块组织最佳实践

### 1. 项目结构

```
project/
├── __init__.py
├── main.py
├── utils/
│   ├── __init__.py
│   ├── data_utils.py
│   ├── string_utils.py
│   └── validation_utils.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── product.py
└── tests/
    ├── __init__.py
    ├── test_utils.py
    └── test_models.py
```

### 2. 导入规范

```python
# 导入顺序：
# 1. 标准库
import os
import sys
from datetime import datetime

# 2. 第三方库
import requests
import numpy as np

# 3. 本地模块
from .utils import data_utils
from .models.user import User
```

### 3. 模块文档

```python
"""
模块说明文档

这个模块包含用于数据处理的实用函数。

函数：
- clean_data: 清理数据
- validate_data: 验证数据
- format_data: 格式化数据

示例：
    from utils.data_utils import clean_data
    cleaned = clean_data(raw_data)
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__all__ = ["clean_data", "validate_data", "format_data"]
```

## 常见错误及解决方案

### 1. 参数传递错误

```python
# 错误：混淆位置参数和关键字参数
# describe_pet("Harry", animal_type="hamster")  # 错误

# 正确：保持参数顺序一致
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("hamster", "Harry")  # 正确
```

### 2. 默认参数陷阱

```python
# 错误：使用可变对象作为默认参数
def append_to_list(item, target_list=[]):  # 错误
    target_list.append(item)
    return target_list

# 正确：使用None作为默认值
def append_to_list(item, target_list=None):  # 正确
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list
```

### 3. 作用域问题

```python
# 错误：在函数内修改全局变量
count = 0

def increment():
    count += 1  # 错误：UnboundLocalError

# 正确：使用global关键字
def increment():
    global count
    count += 1  # 正确
```

## 高级主题

### 1. 装饰器

```python
def log_function_call(func):
    """记录函数调用的装饰器"""
    def wrapper(*args, **kwargs):
        print(f"调用函数：{func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数返回：{result}")
        return result
    return wrapper

@log_function_call
def add_numbers(a, b):
    return a + b
```

### 2. 高阶函数

```python
def apply_operation(numbers, operation):
    """对数字列表应用操作"""
    return [operation(num) for num in numbers]

# 使用lambda函数
squares = apply_operation([1, 2, 3, 4], lambda x: x**2)
```

### 3. 闭包

```python
def create_multiplier(factor):
    """创建乘数函数"""
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
```

## 测试函数

### 1. 单元测试

```python
def test_calculate_area():
    """测试面积计算函数"""
    # 测试正常情况
    assert calculate_area(5, 3) == 15

    # 测试边界情况
    assert calculate_area(0, 5) == 0
    assert calculate_area(5, 0) == 0

    # 测试异常情况
    try:
        calculate_area(-1, 5)
        assert False, "应该抛出异常"
    except ValueError:
        pass
```

### 2. 文档测试

```python
def calculate_area(length, width):
    """
    计算矩形面积

    >>> calculate_area(5, 3)
    15
    >>> calculate_area(0, 5)
    0
    >>> calculate_area(2.5, 4)
    10.0
    """
    return length * width

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

## 性能优化

### 1. 避免重复计算

```python
# 低效：重复计算
def process_data(data):
    for item in data:
        if len(data) > 100:  # 每次都计算len(data)
            # 处理逻辑
            pass

# 高效：预先计算
def process_data(data):
    data_length = len(data)  # 只计算一次
    for item in data:
        if data_length > 100:
            # 处理逻辑
            pass
```

### 2. 使用生成器

```python
# 内存密集型
def get_squares(n):
    return [x**2 for x in range(n)]

# 内存友好型
def get_squares_generator(n):
    for x in range(n):
        yield x**2
```

## 练习建议

1. **基础练习**：从简单的函数定义开始
2. **参数练习**：掌握各种参数类型的使用
3. **返回值练习**：练习不同类型的返回值
4. **模块练习**：创建和使用自定义模块
5. **实际项目**：将学到的知识应用到实际项目中

## 扩展学习

- **函数式编程**：学习 map、filter、reduce 等函数
- **异步编程**：学习 async/await 语法
- **面向对象编程**：学习类和对象的概念
- **设计模式**：学习常见的设计模式

## 总结

第 08 章介绍了 Python 函数的核心概念，这是编写高质量 Python 代码的基础。通过掌握函数的定义、参数、返回值和模块化编程，你可以编写更加清晰、可维护和可重用的代码。

记住：

- 函数应该有单一的职责
- 使用描述性的函数名
- 编写清晰的文档字符串
- 合理设计函数参数
- 适当处理错误和异常
- 遵循模块化编程原则

继续练习这些概念，它们是后续学习类、错误处理和更高级 Python 特性的基础。
