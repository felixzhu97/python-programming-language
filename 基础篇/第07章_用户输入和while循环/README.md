# 第 07 章 用户输入和 while 循环

## 学习目标

本章将学习如何让程序与用户交互，获取用户输入，以及如何使用 while 循环来重复执行代码块。这些技能是创建真正交互式程序的基础。

### 核心概念

1. **input()函数**：获取用户输入
2. **while 循环**：基于条件重复执行代码
3. **标志变量**：控制循环的执行状态
4. **break 语句**：立即退出循环
5. **continue 语句**：跳过当前循环迭代
6. **用户输入验证**：确保输入数据的有效性

## 文件说明

### 核心文件

| 文件名              | 说明               | 核心内容                               |
| ------------------- | ------------------ | -------------------------------------- |
| `input_function.py` | input()函数详解    | 基本用法、类型转换、输入验证、错误处理 |
| `while_loops.py`    | while 循环全面教程 | 基本语法、循环控制、实际应用场景       |
| `exercises.py`      | 章节练习解答       | 练习 7-1 到 7-10 的完整解答            |
| `README.md`         | 学习指导文档       | 学习路径、重要概念、最佳实践           |

### 学习路径

```
1. input_function.py     →  掌握用户输入获取
2. while_loops.py        →  学习while循环控制
3. exercises.py          →  实践练习巩固
4. 综合应用项目           →  创建交互式程序
```

## 重要概念详解

### 1. input()函数

```python
# 基本用法
name = input("请输入您的姓名：")
print(f"你好，{name}！")

# 类型转换
age = int(input("请输入您的年龄："))
height = float(input("请输入您的身高："))
```

**要点：**

- input()函数返回的始终是字符串
- 需要进行类型转换处理数值
- 应该添加输入验证和错误处理

### 2. while 循环

```python
# 基本结构
count = 1
while count <= 5:
    print(f"这是第 {count} 次循环")
    count += 1

# 用户输入控制
message = ""
while message != 'quit':
    message = input("请输入消息（'quit'退出）：")
    if message != 'quit':
        print(f"您输入了：{message}")
```

**要点：**

- 确保循环条件最终会变为 False
- 在循环体内更新控制变量
- 避免无限循环

### 3. 标志变量

```python
# 使用标志变量控制循环
active = True
while active:
    message = input("请输入消息（'quit'退出）：")
    if message == 'quit':
        active = False
    else:
        print(f"您输入了：{message}")
```

**优点：**

- 代码更清晰易读
- 便于处理多个退出条件
- 提高代码的可维护性

### 4. break 和 continue 语句

```python
# break：立即退出循环
while True:
    message = input("请输入消息（'quit'退出）：")
    if message == 'quit':
        break
    print(f"您输入了：{message}")

# continue：跳过当前迭代
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        i += 1
        continue
    print(f"奇数：{numbers[i]}")
    i += 1
```

## 实际应用场景

### 1. 用户界面程序

```python
def main_menu():
    while True:
        print("\n=== 主菜单 ===")
        print("1. 添加任务")
        print("2. 查看任务")
        print("3. 删除任务")
        print("4. 退出")

        choice = input("请选择操作：")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            break
        else:
            print("无效选择，请重试")
```

### 2. 数据处理

```python
def process_data():
    data = []
    while True:
        value = input("请输入数据（'done'结束）：")
        if value == 'done':
            break
        try:
            data.append(float(value))
        except ValueError:
            print("请输入有效数字")

    return data
```

### 3. 游戏循环

```python
def simple_game():
    score = 0
    playing = True

    while playing:
        print(f"当前得分：{score}")
        action = input("选择动作（attack/defend/quit）：")

        if action == 'attack':
            score += 10
            print("攻击成功！+10分")
        elif action == 'defend':
            score += 5
            print("防御成功！+5分")
        elif action == 'quit':
            playing = False
        else:
            print("无效动作")

    print(f"游戏结束，最终得分：{score}")
```

## 最佳实践

### 1. 输入验证

```python
def get_valid_integer(prompt, min_val=None, max_val=None):
    """获取有效的整数输入"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"值不能小于 {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"值不能大于 {max_val}")
                continue
            return value
        except ValueError:
            print("请输入有效的整数")
```

### 2. 错误处理

```python
def safe_division():
    """安全的除法运算"""
    while True:
        try:
            dividend = float(input("请输入被除数："))
            divisor = float(input("请输入除数："))

            if divisor == 0:
                print("除数不能为零")
                continue

            result = dividend / divisor
            print(f"结果：{dividend} ÷ {divisor} = {result}")
            break

        except ValueError:
            print("请输入有效的数字")
        except Exception as e:
            print(f"发生错误：{e}")
```

### 3. 用户友好的界面

```python
def user_friendly_input():
    """用户友好的输入处理"""
    print("=== 用户信息收集 ===")
    print("提示：随时输入'quit'退出程序")

    user_data = {}

    while True:
        name = input("请输入姓名：").strip()
        if name.lower() == 'quit':
            break
        if name:
            user_data['name'] = name
            break
        print("姓名不能为空，请重新输入")

    if 'name' in user_data:
        print(f"欢迎，{user_data['name']}！")
    else:
        print("程序已退出")
```

## 常见错误及解决方案

### 1. 无限循环

```python
# 错误：忘记更新循环变量
# count = 1
# while count <= 5:
#     print(count)
#     # 忘记了 count += 1

# 正确：确保更新循环变量
count = 1
while count <= 5:
    print(count)
    count += 1
```

### 2. 类型转换错误

```python
# 错误：不处理转换异常
# age = int(input("请输入年龄："))

# 正确：添加异常处理
try:
    age = int(input("请输入年龄："))
except ValueError:
    print("请输入有效的数字")
    age = 0
```

### 3. 输入验证不足

```python
# 错误：不验证输入
# choice = input("请选择（1-3）：")

# 正确：验证输入范围
while True:
    choice = input("请选择（1-3）：")
    if choice in ['1', '2', '3']:
        break
    print("无效选择，请重试")
```

## 性能考虑

### 1. 避免在循环中重复计算

```python
# 低效：每次循环都计算
items = [1, 2, 3, 4, 5]
i = 0
while i < len(items):  # 每次都调用len()
    print(items[i])
    i += 1

# 高效：预先计算
items = [1, 2, 3, 4, 5]
length = len(items)
i = 0
while i < length:
    print(items[i])
    i += 1
```

### 2. 合适的循环选择

```python
# 已知循环次数，使用for循环
for i in range(5):
    print(i)

# 基于条件循环，使用while循环
user_input = ""
while user_input != 'quit':
    user_input = input("请输入：")
```

## 调试技巧

### 1. 添加调试输出

```python
def debug_while_loop():
    count = 0
    target = 10

    while count < target:
        print(f"调试：count={count}, target={target}")  # 调试输出
        count += 2

        if count > 20:  # 防止无限循环
            print("达到安全限制，退出循环")
            break
```

### 2. 使用断点调试

```python
import pdb

def debug_function():
    count = 0
    while count < 5:
        pdb.set_trace()  # 设置断点
        print(f"Count: {count}")
        count += 1
```

## 练习建议

1. **基础练习**：从简单的 input()和 while 循环开始
2. **逐步增加复杂度**：添加输入验证、错误处理
3. **实际项目**：创建小型的交互式程序
4. **代码重构**：优化和改进现有代码

## 扩展学习

- **异常处理**：学习更多的异常类型和处理方法
- **正则表达式**：用于复杂的输入验证
- **图形用户界面**：使用 tkinter 等库创建 GUI 程序
- **Web 界面**：使用 Flask 等框架创建 Web 应用

## 总结

第 07 章介绍了用户输入和 while 循环的核心概念，这些是创建交互式程序的基础。通过掌握 input()函数、while 循环、标志变量和循环控制语句，你可以创建能够与用户交互的程序。

记住：

- 始终验证用户输入
- 确保循环条件最终会变为 False
- 添加适当的错误处理
- 编写用户友好的界面
- 考虑性能和可维护性

继续练习这些概念，它们是后续学习函数、类和更复杂程序结构的基础。
