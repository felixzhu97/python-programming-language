# 第 10 章 文件和异常

## 章节概述

本章是 Python 程序与外部世界交互的重要内容，详细介绍了文件操作和异常处理机制。文件操作让程序能够读取和存储数据，而异常处理确保程序在遇到错误时能够优雅地处理而不是崩溃。这两个主题是编写健壮、实用的 Python 程序的基础。

## 学习目标

通过本章的学习，您将能够：

1. **掌握文件操作**

   - 读取和写入文本文件
   - 处理不同编码的文件
   - 文件路径的操作和管理
   - 二进制文件的处理

2. **理解异常处理**

   - 异常的基本概念和类型
   - try-except 语句的使用
   - else 和 finally 子句
   - 自定义异常类

3. **掌握 JSON 数据处理**

   - JSON 格式的读写
   - Python 对象与 JSON 的转换
   - 处理复杂的 JSON 数据
   - JSON 数据验证

4. **实际应用能力**
   - 数据持久化存储
   - 配置文件管理
   - 日志处理和分析
   - 错误处理策略

## 文件说明

### 1. file_operations.py

**文件操作详解**

- 文件的读取和写入方法
- 文件路径操作（os.path 和 pathlib）
- 文件和目录管理
- 不同编码的处理
- 二进制文件操作
- 临时文件和安全操作
- 批量文件处理
- 文件监控和处理

**主要内容：**

```python
# 基本文件读写
with open("filename.txt", "r", encoding="utf-8") as file:
    content = file.read()

with open("filename.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World!")

# 路径操作
from pathlib import Path
file_path = Path("data/file.txt")
if file_path.exists():
    content = file_path.read_text(encoding="utf-8")
```

### 2. exception_handling.py

**异常处理详解**

- 异常的基本概念和语法
- try-except-else-finally 语句
- 常见异常类型和处理
- 异常信息的获取和记录
- 自定义异常类
- 异常链和上下文
- 实际应用中的异常处理策略

**主要内容：**

```python
# 基本异常处理
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"除零错误：{e}")
except Exception as e:
    print(f"其他错误：{e}")
else:
    print("没有异常发生")
finally:
    print("清理资源")

# 自定义异常
class CustomError(Exception):
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code
```

### 3. json_operations.py

**JSON 操作详解**

- JSON 数据的读写
- Python 对象与 JSON 的转换
- 自定义 JSON 编码器和解码器
- JSON 数据验证和错误处理
- 处理大型 JSON 文件
- JSON 配置文件管理
- API 响应处理

**主要内容：**

```python
import json

# JSON读写
data = {"name": "Alice", "age": 25}

# 写入JSON文件
with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

# 读取JSON文件
with open("data.json", "r") as file:
    loaded_data = json.load(file)

# 自定义编码器
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
```

### 4. exercises.py

**练习题解答**

- 书中所有练习题的完整解答
- 额外的实际应用练习
- 文件处理综合项目
- 异常处理最佳实践示例

**包含练习：**

- 练习 10-1：Python 学习
- 练习 10-2：C 语言学习
- 练习 10-3：访客
- 练习 10-4：访客名单
- 练习 10-5：关于编程的调查
- 练习 10-6：加法运算
- 练习 10-7：加法计算器
- 练习 10-8：猫和狗
- 练习 10-9：沉默的猫和狗
- 练习 10-10：常见单词
- 练习 10-11：喜欢的数字
- 练习 10-12：记住喜欢的数字
- 练习 10-13：验证用户
- 额外练习：文件数据分析器
- 额外练习：日志文件处理器
- 额外练习：配置文件管理器

## 重要概念

### 1. 文件操作

#### 文件打开模式

- `'r'`：只读模式（默认）
- `'w'`：写入模式（覆盖）
- `'a'`：追加模式
- `'x'`：独占创建模式
- `'b'`：二进制模式
- `'t'`：文本模式（默认）
- `'+'`：读写模式

#### with 语句

```python
with open("file.txt", "r") as file:
    content = file.read()
# 文件自动关闭
```

#### 文件编码

- UTF-8：支持所有 Unicode 字符
- GBK：中文编码
- ASCII：英文字符
- Latin-1：西欧字符

### 2. 异常处理

#### 异常层次结构

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      |    +-- OverflowError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- ValueError
      +-- TypeError
      +-- FileNotFoundError
      +-- PermissionError
```

#### 异常处理语法

```python
try:
    # 可能出错的代码
    risky_operation()
except SpecificError as e:
    # 处理特定异常
    handle_specific_error(e)
except (Error1, Error2) as e:
    # 处理多种异常
    handle_multiple_errors(e)
except Exception as e:
    # 处理所有其他异常
    handle_general_error(e)
else:
    # 没有异常时执行
    success_operation()
finally:
    # 无论如何都执行
    cleanup_resources()
```

### 3. JSON 数据处理

#### JSON 数据类型映射

| JSON   | Python    |
| ------ | --------- |
| object | dict      |
| array  | list      |
| string | str       |
| number | int/float |
| true   | True      |
| false  | False     |
| null   | None      |

#### JSON 操作函数

- `json.dumps()`：Python 对象转 JSON 字符串
- `json.loads()`：JSON 字符串转 Python 对象
- `json.dump()`：Python 对象写入 JSON 文件
- `json.load()`：从 JSON 文件读取 Python 对象

## 最佳实践

### 1. 文件操作最佳实践

```python
# ✅ 推荐：使用with语句
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()

# ❌ 不推荐：手动关闭文件
file = open("file.txt", "r")
content = file.read()
file.close()  # 容易忘记，可能导致资源泄露

# ✅ 推荐：明确指定编码
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()

# ❌ 不推荐：使用系统默认编码
with open("file.txt", "r") as file:  # 可能导致编码问题
    content = file.read()

# ✅ 推荐：使用pathlib
from pathlib import Path
file_path = Path("data") / "file.txt"
if file_path.exists():
    content = file_path.read_text(encoding="utf-8")

# ✅ 推荐：处理文件操作异常
try:
    with open("file.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("文件不存在")
except PermissionError:
    print("没有权限访问文件")
```

### 2. 异常处理最佳实践

```python
# ✅ 推荐：捕获具体的异常类型
try:
    value = int(user_input)
except ValueError:
    print("请输入有效的数字")

# ❌ 不推荐：捕获所有异常
try:
    value = int(user_input)
except:  # 太宽泛
    print("出错了")

# ✅ 推荐：提供有用的错误信息
try:
    result = divide(a, b)
except ZeroDivisionError:
    print(f"错误：不能将 {a} 除以 0")

# ✅ 推荐：记录异常信息
import logging
try:
    risky_operation()
except Exception as e:
    logging.error(f"操作失败：{e}", exc_info=True)

# ✅ 推荐：自定义异常传达业务含义
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"余额不足：当前余额 {balance}，尝试提取 {amount}")
```

### 3. JSON 处理最佳实践

```python
# ✅ 推荐：使用适当的参数
import json

data = {"name": "张三", "age": 25}

# 美化输出
json_str = json.dumps(data, ensure_ascii=False, indent=2)

# 处理复杂对象
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

# ✅ 推荐：验证JSON数据
def validate_user_data(data):
    required_fields = ["name", "email", "age"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"缺少必填字段：{field}")

    if not isinstance(data["age"], int) or data["age"] < 0:
        raise ValueError("年龄必须是非负整数")

# ✅ 推荐：处理JSON异常
try:
    with open("config.json", "r") as file:
        config = json.load(file)
except FileNotFoundError:
    print("配置文件不存在，使用默认配置")
    config = default_config
except json.JSONDecodeError as e:
    print(f"配置文件格式错误：{e}")
    config = default_config
```

## 实际应用场景

### 1. 数据持久化

- 用户偏好设置
- 游戏存档
- 缓存数据
- 临时文件处理

### 2. 配置文件管理

- 应用程序配置
- 数据库连接信息
- API 密钥管理
- 环境变量

### 3. 日志和监控

- 错误日志记录
- 用户行为追踪
- 性能监控数据
- 审计日志

### 4. 数据交换

- API 请求和响应
- 微服务间通信
- 数据导入导出
- 配置同步

## 运行示例

### 运行所有示例

```bash
# 运行文件操作示例
python file_operations.py

# 运行异常处理示例
python exception_handling.py

# 运行JSON操作示例
python json_operations.py

# 运行练习题
python exercises.py
```

### 交互式学习

```python
# 在Python交互式环境中
import json
from pathlib import Path

# 文件操作
file_path = Path("test.txt")
file_path.write_text("Hello, World!", encoding="utf-8")
content = file_path.read_text(encoding="utf-8")
print(content)

# JSON操作
data = {"name": "Alice", "skills": ["Python", "JavaScript"]}
json_str = json.dumps(data, indent=2)
print(json_str)
```

## 常见错误和解决方案

### 1. 文件编码问题

```python
# 问题：UnicodeDecodeError
try:
    with open("file.txt", "r") as file:  # 没有指定编码
        content = file.read()
except UnicodeDecodeError:
    # 解决方案：指定正确的编码
    with open("file.txt", "r", encoding="utf-8") as file:
        content = file.read()
```

### 2. 文件路径问题

```python
# 问题：路径分隔符在不同系统上不同
import os
from pathlib import Path

# ❌ 不推荐：硬编码路径分隔符
file_path = "data\\file.txt"  # 只在Windows上工作

# ✅ 推荐：使用pathlib
file_path = Path("data") / "file.txt"  # 跨平台

# ✅ 推荐：使用os.path.join
file_path = os.path.join("data", "file.txt")
```

### 3. 异常处理过于宽泛

```python
# ❌ 不推荐：捕获所有异常
try:
    risky_operation()
except:
    print("出错了")  # 无法知道具体错误

# ✅ 推荐：捕获具体异常
try:
    risky_operation()
except FileNotFoundError:
    print("文件不存在")
except PermissionError:
    print("权限不足")
except Exception as e:
    print(f"未知错误：{e}")
```

### 4. JSON 序列化问题

```python
# 问题：某些Python对象不能直接序列化
from datetime import datetime
import json

data = {"timestamp": datetime.now()}

# ❌ 这会出错
try:
    json.dumps(data)
except TypeError:
    # ✅ 解决方案：使用自定义编码器
    class DateTimeEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            return super().default(obj)

    json_str = json.dumps(data, cls=DateTimeEncoder)
```

## 性能考虑

### 1. 大文件处理

```python
# ✅ 对于大文件，逐行读取
def process_large_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:  # 逐行处理，内存效率高
            process_line(line.strip())

# ❌ 避免一次性读取大文件
def process_large_file_bad(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()  # 可能导致内存不足
        lines = content.split('\n')
        for line in lines:
            process_line(line)
```

### 2. JSON 处理优化

```python
# ✅ 对于大型JSON，考虑流式处理
import ijson  # 第三方库，需要安装

def process_large_json(filename):
    with open(filename, 'rb') as file:
        parser = ijson.parse(file)
        for prefix, event, value in parser:
            if prefix.endswith('.item'):
                process_item(value)
```

## 安全考虑

### 1. 文件路径安全

```python
from pathlib import Path

def safe_file_access(user_path, base_dir="/safe/directory"):
    """安全的文件访问"""
    base_path = Path(base_dir).resolve()
    file_path = (base_path / user_path).resolve()

    # 确保文件在安全目录内
    if not str(file_path).startswith(str(base_path)):
        raise ValueError("不安全的文件路径")

    return file_path
```

### 2. JSON 安全

```python
import json

def safe_json_load(filename, max_size=1024*1024):  # 1MB限制
    """安全的JSON加载"""
    file_path = Path(filename)

    # 检查文件大小
    if file_path.stat().st_size > max_size:
        raise ValueError("JSON文件过大")

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
```

## 总结

第 10 章文件和异常是 Python 编程中的重要主题，通过学习本章，您将：

- 掌握文件的读写操作和路径管理
- 学会处理各种异常情况
- 理解 JSON 数据格式的处理
- 具备编写健壮程序的能力

这些技能是开发实际应用程序的基础，无论是数据处理、配置管理还是错误处理，都会频繁使用到本章的内容。

建议您：

1. 多练习文件操作，熟悉不同的读写模式
2. 学会预见和处理各种异常情况
3. 掌握 JSON 数据的处理技巧
4. 在实际项目中应用这些技能
5. 关注安全性和性能优化

记住，优秀的程序不仅要能正常工作，还要能优雅地处理各种异常情况。
