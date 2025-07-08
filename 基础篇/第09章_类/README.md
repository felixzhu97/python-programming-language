# 第 09 章 - 类

## 📖 本章概述

面向对象编程(OOP)是 Python 的重要特性之一。本章将学习如何使用类来创建对象，实现代码的封装、继承和多态。

## 🎯 学习目标

- 理解面向对象编程的基本概念
- 掌握类和对象的定义与使用
- 学习属性和方法的创建
- 了解继承和方法重写
- 掌握 Python 标准库中的类使用

## 📚 主要内容

### 1. 类的基础

- 类的定义和实例化
- 属性和方法
- `__init__`方法的使用
- `self`参数的理解

### 2. 使用类和实例

- 创建实例
- 访问属性和调用方法
- 修改属性值
- 给属性设置默认值

### 3. 继承

- 子类的定义
- 方法重写
- `super()`函数的使用
- 多层继承

### 4. 高级特性

- 类变量和实例变量
- 静态方法和类方法
- 私有属性和方法
- 特殊方法(魔法方法)

## 📄 文件说明

| 文件名                 | 描述     | 主要内容                    |
| ---------------------- | -------- | --------------------------- |
| `class_basics.py`      | 类的基础 | 类定义、实例化、基本用法    |
| `class_inheritance.py` | 继承机制 | 继承、方法重写、super()使用 |
| `class_advanced.py`    | 高级特性 | 类变量、静态方法、特殊方法  |
| `exercises.py`         | 章节练习 | 9-1 到 9-15 练习题解答      |

## 🚀 快速开始

```bash
# 运行类基础演示
python class_basics.py

# 运行继承机制演示
python class_inheritance.py

# 运行高级特性演示
python class_advanced.py

# 查看练习解答
python exercises.py
```

## 💡 重要概念

### 类定义语法

```python
class ClassName:
    """类的文档字符串"""

    def __init__(self, parameter):
        """初始化方法"""
        self.attribute = parameter

    def method_name(self):
        """实例方法"""
        return self.attribute
```

### 继承语法

```python
class ChildClass(ParentClass):
    """子类继承父类"""

    def __init__(self, parameter, new_parameter):
        super().__init__(parameter)
        self.new_attribute = new_parameter

    def method_name(self):
        """重写父类方法"""
        # 可以调用父类方法
        super().method_name()
        # 添加新功能
        return modified_result
```

## 🔧 练习建议

1. **基础练习**

   - 创建简单的类(如 Person、Car)
   - 练习属性的设置和获取
   - 编写实例方法

2. **继承练习**

   - 创建父类和子类
   - 练习方法重写
   - 使用 super()调用父类方法

3. **实战练习**
   - 设计餐厅点餐系统
   - 创建游戏角色类
   - 实现银行账户系统

## 🎯 本章要点

- ✅ 类是创建对象的蓝图
- ✅ `__init__`方法用于初始化实例
- ✅ 继承可以避免代码重复
- ✅ 方法重写可以自定义子类行为
- ✅ 面向对象编程让代码更加模块化

## 🌟 实际应用示例

### 汽车类示例

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
```

## 🔗 相关章节

- **第 8 章** - 函数：面向对象编程的基础
- **第 10 章** - 文件和异常：类的实际应用
- **第 12-14 章** - 游戏项目：类在大型项目中的应用

---

> 💡 **提示**：面向对象编程是现代软件开发的重要思想，掌握好类的使用对成为优秀程序员至关重要！
