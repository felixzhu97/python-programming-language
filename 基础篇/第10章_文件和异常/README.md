# 第 10 章 - 文件和异常

## 📖 本章概述

学习如何处理文件和异常是 Python 编程的重要技能。本章将教你如何读写文件、处理 JSON 数据以及优雅地处理程序运行时可能出现的错误。

## 🎯 学习目标

- 掌握文件的读取和写入操作
- 学习处理不同格式的数据文件
- 了解 JSON 数据的处理方法
- 掌握异常处理机制
- 学会编写健壮的程序

## 📚 主要内容

### 1. 文件操作

- 文件的打开和关闭
- 读取文件内容
- 写入文件内容
- 文件路径的处理

### 2. 异常处理

- try-except 语句
- 不同类型的异常
- else 和 finally 子句
- 抛出自定义异常

### 3. 存储数据

- JSON 格式介绍
- json.dump()和 json.load()
- 数据的序列化和反序列化
- 配置文件的处理

### 4. 实际应用

- 日志文件的处理
- 配置文件的读写
- 数据备份和恢复
- 用户输入验证

## 📄 文件说明

| 文件名                  | 描述          | 主要内容                        |
| ----------------------- | ------------- | ------------------------------- |
| `file_operations.py`    | 文件操作      | 读写文件、路径处理、文件管理    |
| `exception_handling.py` | 异常处理      | try-except、异常类型、错误处理  |
| `json_operations.py`    | JSON 数据处理 | JSON 读写、数据序列化、配置管理 |
| `exercises.py`          | 章节练习      | 10-1 到 10-13 练习题解答        |

## 🚀 快速开始

```bash
# 运行文件操作演示
python file_operations.py

# 运行异常处理演示
python exception_handling.py

# 运行JSON操作演示
python json_operations.py

# 查看练习解答
python exercises.py
```

## 💡 重要概念

### 文件操作语法

```python
# 读取文件
with open('filename.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 写入文件
with open('filename.txt', 'w', encoding='utf-8') as file:
    file.write('Hello, World!')

# 追加内容
with open('filename.txt', 'a', encoding='utf-8') as file:
    file.write('Additional content')
```

### 异常处理语法

```python
try:
    # 可能出错的代码
    result = 10 / 0
except ZeroDivisionError:
    # 处理特定异常
    print("Cannot divide by zero!")
except Exception as e:
    # 处理其他异常
    print(f"An error occurred: {e}")
else:
    # 没有异常时执行
    print("Operation successful!")
finally:
    # 无论是否有异常都执行
    print("Cleanup code here")
```

### JSON 操作语法

```python
import json

# 保存数据到JSON文件
data = {'name': 'Alice', 'age': 30}
with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)

# 从JSON文件读取数据
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
```

## 🔧 练习建议

1. **文件操作练习**

   - 创建文本文件并写入内容
   - 读取大文件并处理数据
   - 实现文件备份功能

2. **异常处理练习**

   - 处理文件不存在的情况
   - 验证用户输入数据
   - 创建自定义异常类

3. **JSON 数据练习**
   - 保存用户设置到 JSON 文件
   - 创建数据导入导出功能
   - 处理 API 返回的 JSON 数据

## 🎯 本章要点

- ✅ 使用`with`语句自动处理文件关闭
- ✅ 异常处理让程序更加健壮
- ✅ JSON 是理想的数据交换格式
- ✅ 合适的异常处理策略很重要
- ✅ 文件操作时要考虑编码问题

## 🌟 实际应用示例

### 用户偏好存储

```python
import json

class UserPreferences:
    def __init__(self, filename='preferences.json'):
        self.filename = filename
        self.preferences = self.load_preferences()

    def load_preferences(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}  # 返回默认设置

    def save_preferences(self):
        with open(self.filename, 'w') as file:
            json.dump(self.preferences, file, indent=2)

    def set_preference(self, key, value):
        self.preferences[key] = value
        self.save_preferences()
```

### 日志记录系统

```python
from datetime import datetime

class Logger:
    def __init__(self, filename='app.log'):
        self.filename = filename

    def log(self, message, level='INFO'):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {level}: {message}\n"

        try:
            with open(self.filename, 'a', encoding='utf-8') as file:
                file.write(log_entry)
        except Exception as e:
            print(f"Failed to write to log file: {e}")
```

## 🔗 相关章节

- **第 8 章** - 函数：文件处理函数的设计
- **第 9 章** - 类：文件处理类的创建
- **第 11 章** - 测试代码：测试文件操作函数
- **第 16 章** - 下载数据：实际的文件处理应用

---

> 💡 **提示**：文件操作和异常处理是实际项目中不可缺少的技能，多练习这些概念对提高编程能力很有帮助！
