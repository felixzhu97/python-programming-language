# 第 05 章 if 语句

## 章节简介

本章学习如何使用条件测试和 if 语句来根据不同的条件执行不同的操作。if 语句是编程中最重要的控制结构之一，它让程序能够根据条件做出决策。

## 学习目标

通过本章学习，您将能够：

1. 理解和使用条件测试
2. 掌握 if 语句的基本语法
3. 使用 if-else 和 if-elif-else 语句
4. 在列表和循环中使用条件语句
5. 处理空列表和多个条件
6. 编写复杂的条件逻辑

## 文件说明

### 1. conditional_tests.py

- **内容**：条件测试和布尔表达式的全面演示
- **重点**：
  - 比较运算符（==、!=、<、>、<=、>=）
  - 逻辑运算符（and、or、not）
  - 成员运算符（in、not in）
  - 字符串比较和大小写处理
  - 复杂条件表达式的构建
- **实际应用**：
  - 用户权限验证
  - 商品库存检查
  - 数据验证和过滤

### 2. if_statements.py

- **内容**：if 语句的各种形式和用法
- **重点**：
  - 简单 if 语句
  - if-else 语句
  - if-elif-else 语句链
  - 多条件测试
  - 在循环中使用 if 语句
  - 处理空列表
- **实际应用**：
  - 用户登录系统
  - 成绩评级系统
  - 商品折扣计算
  - 天气穿衣建议

### 3. exercises.py

- **内容**：第 5 章所有练习题的完整解答
- **包含练习**：
  - 练习 5-1：条件测试
  - 练习 5-2：更多的条件测试
  - 练习 5-3：外星人颜色 #1
  - 练习 5-4：外星人颜色 #2
  - 练习 5-5：外星人颜色 #3
  - 练习 5-6：人生的不同阶段
  - 练习 5-7：喜欢的水果
  - 练习 5-8：以特殊方式跟管理员打招呼
  - 练习 5-9：处理没有用户的情形
  - 练习 5-10：检查用户名
  - 练习 5-11：序数
- **额外练习**：
  - 学生成绩管理系统
  - 购物车结算系统
  - 游戏角色状态系统

## 核心概念

### 1. 条件测试

条件测试是返回 True 或 False 的表达式：

```python
# 基本比较
age = 18
print(age == 18)  # True
print(age >= 21)  # False

# 字符串比较
name = 'Alice'
print(name == 'Alice')  # True
print(name.lower() == 'alice')  # True

# 列表成员检查
fruits = ['apple', 'banana', 'orange']
print('apple' in fruits)  # True
print('grape' not in fruits)  # True
```

### 2. 逻辑运算符

- **and**：两个条件都为 True 时返回 True
- **or**：至少一个条件为 True 时返回 True
- **not**：反转布尔值

```python
age = 25
has_license = True

# 使用and
print(age >= 18 and has_license)  # True

# 使用or
print(age < 16 or age > 65)  # False

# 使用not
print(not has_license)  # False
```

### 3. if 语句的形式

#### 简单 if 语句

```python
if condition:
    # 执行的代码
```

#### if-else 语句

```python
if condition:
    # 条件为True时执行
else:
    # 条件为False时执行
```

#### if-elif-else 语句

```python
if condition1:
    # 条件1为True时执行
elif condition2:
    # 条件2为True时执行
else:
    # 所有条件都为False时执行
```

### 4. 处理列表的条件检查

```python
# 检查列表是否为空
items = []
if items:
    print("列表有内容")
else:
    print("列表为空")

# 检查特定值
requested_items = ['apple', 'banana']
available_items = ['apple', 'orange', 'grape']

for item in requested_items:
    if item in available_items:
        print(f"有{item}")
    else:
        print(f"没有{item}")
```

## 最佳实践

### 1. 代码可读性

- 使用有意义的变量名
- 保持条件表达式简洁
- 适当使用括号明确优先级

```python
# 好的例子
is_adult = age >= 18
has_permission = user_type == 'admin'
if is_adult and has_permission:
    print("允许访问")

# 不好的例子
if age >= 18 and user_type == 'admin':
    print("允许访问")
```

### 2. 避免过深的嵌套

```python
# 避免过深嵌套
if user_logged_in:
    if user_has_permission:
        if resource_available:
            print("访问成功")
        else:
            print("资源不可用")
    else:
        print("权限不足")
else:
    print("请先登录")

# 更好的方式
if not user_logged_in:
    print("请先登录")
    return

if not user_has_permission:
    print("权限不足")
    return

if not resource_available:
    print("资源不可用")
    return

print("访问成功")
```

### 3. 使用 elif 而不是多个 if

```python
# 使用elif（推荐）
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'

# 避免使用多个if
if score >= 90:
    grade = 'A'
if score >= 80:
    grade = 'B'  # 这会覆盖之前的值
if score >= 70:
    grade = 'C'
```

### 4. 处理边界条件

```python
def calculate_discount(amount):
    if amount <= 0:
        return 0  # 处理负数或零
    elif amount >= 1000:
        return amount * 0.1
    elif amount >= 500:
        return amount * 0.05
    else:
        return 0
```

## 常见错误

### 1. 赋值 vs 比较

```python
# 错误：使用赋值符号
if age = 18:  # SyntaxError
    print("成年了")

# 正确：使用比较符号
if age == 18:
    print("成年了")
```

### 2. 浮点数比较

```python
# 不推荐：直接比较浮点数
if 0.1 + 0.2 == 0.3:  # False
    print("相等")

# 推荐：使用误差范围
if abs(0.1 + 0.2 - 0.3) < 0.0001:  # True
    print("相等")
```

### 3. 空列表和 None 的区别

```python
# 空列表
items = []
if items:  # False
    print("有内容")

# None
items = None
if items:  # False
    print("有内容")

# 区别对待
if items is None:
    print("未初始化")
elif not items:
    print("空列表")
else:
    print("有内容")
```

## 实际应用场景

### 1. 用户输入验证

```python
def validate_age(age):
    if not isinstance(age, int):
        return False, "年龄必须是整数"
    if age < 0:
        return False, "年龄不能为负数"
    if age > 150:
        return False, "年龄不能超过150岁"
    return True, "年龄有效"
```

### 2. 权限控制

```python
def check_permission(user_role, action):
    if user_role == 'admin':
        return True
    elif user_role == 'user' and action in ['read', 'create']:
        return True
    elif user_role == 'guest' and action == 'read':
        return True
    else:
        return False
```

### 3. 数据处理

```python
def process_data(data):
    if not data:
        return "没有数据"

    valid_data = []
    for item in data:
        if item is not None and item != '':
            valid_data.append(item)

    if not valid_data:
        return "没有有效数据"

    return f"处理了{len(valid_data)}条数据"
```

## 运行说明

1. 运行条件测试演示：

   ```bash
   python conditional_tests.py
   ```

2. 运行 if 语句演示：

   ```bash
   python if_statements.py
   ```

3. 运行练习题：
   ```bash
   python exercises.py
   ```

## 扩展阅读

- Python 官方文档：控制流程
- 布尔代数基础
- 代码可读性和最佳实践
- 单元测试中的条件断言

通过本章的学习，您已经掌握了 Python 中条件判断的核心技能，这为后续学习字典、函数和类等高级特性奠定了坚实基础。
