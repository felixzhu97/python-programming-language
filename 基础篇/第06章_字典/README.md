# 第 06 章 字典

## 章节简介

本章学习 Python 中的字典数据类型，字典是一种可变的映射类型，用于存储键值对。字典在 Python 中扮演着极其重要的角色，是处理结构化数据的核心工具。

## 学习目标

通过本章学习，您将能够：

1. 理解字典的基本概念和特性
2. 掌握字典的创建、访问、修改和删除操作
3. 学会遍历字典的各种方法
4. 使用嵌套结构处理复杂数据
5. 在实际项目中应用字典解决问题
6. 理解字典的性能特点和最佳实践

## 文件说明

### 1. dict_basics.py

- **内容**：字典的基础操作全面演示
- **重点**：
  - 字典的创建（字面量、构造函数、推导式）
  - 访问和修改字典元素
  - 添加和删除键值对
  - 字典的方法（get、keys、values、items、update 等）
  - 字典的复制和清空
  - 字典的长度和成员检查
- **实际应用**：
  - 学生成绩管理系统
  - 购物车系统
  - 用户信息存储
  - 性能测试和优化

### 2. dict_traversal.py

- **内容**：字典遍历的完整指南
- **重点**：
  - 遍历键值对（items()）
  - 遍历键（keys()）
  - 遍历值（values()）
  - 按顺序遍历（sorted()）
  - 条件遍历和筛选
  - 使用 enumerate()遍历
  - 嵌套结构的遍历
- **实际应用**：
  - 销售数据分析
  - 用户权限管理
  - 数据统计和报告
  - 性能优化技巧

### 3. nesting.py

- **内容**：嵌套数据结构的高级应用
- **重点**：
  - 字典列表（列表中包含字典）
  - 字典中存储列表
  - 字典中存储字典
  - 复杂嵌套结构的设计
  - 嵌套数据的操作和验证
  - 深拷贝和浅拷贝
  - JSON 序列化和反序列化
- **实际应用**：
  - 学校管理系统
  - 电商系统数据结构
  - 用户配置管理
  - 数据验证和处理

### 4. exercises.py

- **内容**：第 6 章所有练习题的完整解答
- **包含练习**：
  - 练习 6-1：人
  - 练习 6-2：喜欢的数字
  - 练习 6-3：词汇表
  - 练习 6-4：词汇表 2
  - 练习 6-5：河流
  - 练习 6-6：调查
  - 练习 6-7：人
  - 练习 6-8：宠物
  - 练习 6-9：喜欢的地方
  - 练习 6-10：喜欢的数字
  - 练习 6-11：城市
  - 练习 6-12：扩展
- **额外练习**：
  - 扩展词汇表系统
  - 学生管理系统
  - 复杂数据结构应用

## 核心概念

### 1. 字典的基本特性

- **可变性**：可以修改字典内容
- **无序性**：Python 3.7+保持插入顺序
- **键的唯一性**：每个键只能出现一次
- **键的不可变性**：键必须是不可变类型

```python
# 创建字典
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 访问值
print(person['name'])  # Alice
print(person.get('age'))  # 25

# 修改值
person['age'] = 26

# 添加新键值对
person['email'] = 'alice@example.com'

# 删除键值对
del person['city']
```

### 2. 字典的常用方法

#### 基本方法

- `get(key, default)`：安全获取值
- `keys()`：获取所有键
- `values()`：获取所有值
- `items()`：获取所有键值对
- `update(other)`：更新字典
- `pop(key, default)`：删除并返回值
- `popitem()`：删除并返回最后一个键值对
- `clear()`：清空字典
- `copy()`：浅拷贝

#### 高级方法

```python
# 字典推导式
squares = {x: x**2 for x in range(5)}

# 合并字典（Python 3.9+）
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = dict1 | dict2

# 使用setdefault
counts = {}
for item in ['a', 'b', 'a', 'c', 'b', 'a']:
    counts.setdefault(item, 0)
    counts[item] += 1
```

### 3. 字典的遍历模式

#### 基本遍历

```python
data = {'a': 1, 'b': 2, 'c': 3}

# 遍历键
for key in data:
    print(key)

# 遍历值
for value in data.values():
    print(value)

# 遍历键值对
for key, value in data.items():
    print(f"{key}: {value}")
```

#### 高级遍历

```python
# 按键排序遍历
for key in sorted(data.keys()):
    print(f"{key}: {data[key]}")

# 按值排序遍历
for key, value in sorted(data.items(), key=lambda x: x[1]):
    print(f"{key}: {value}")

# 条件遍历
for key, value in data.items():
    if value > 1:
        print(f"{key}: {value}")
```

### 4. 嵌套结构的设计

#### 字典列表

```python
students = [
    {'name': 'Alice', 'age': 20, 'grade': 'A'},
    {'name': 'Bob', 'age': 19, 'grade': 'B'},
    {'name': 'Charlie', 'age': 21, 'grade': 'A'}
]
```

#### 字典中的列表

```python
courses = {
    'python': ['Alice', 'Bob', 'Charlie'],
    'java': ['Bob', 'David'],
    'javascript': ['Alice', 'Eve']
}
```

#### 字典中的字典

```python
users = {
    'alice': {
        'email': 'alice@example.com',
        'age': 25,
        'preferences': {'theme': 'dark', 'language': 'en'}
    },
    'bob': {
        'email': 'bob@example.com',
        'age': 30,
        'preferences': {'theme': 'light', 'language': 'zh'}
    }
}
```

## 最佳实践

### 1. 安全访问字典

```python
# 推荐：使用get()方法
value = data.get('key', 'default_value')

# 避免：直接访问可能不存在的键
# value = data['key']  # 可能引发KeyError

# 检查键是否存在
if 'key' in data:
    value = data['key']
```

### 2. 字典的性能优化

```python
# 推荐：使用字典推导式
squares = {x: x**2 for x in range(10)}

# 避免：循环创建字典
squares = {}
for x in range(10):
    squares[x] = x**2

# 推荐：使用setdefault
counts.setdefault(key, 0)
counts[key] += 1

# 避免：频繁检查键存在
if key not in counts:
    counts[key] = 0
counts[key] += 1
```

### 3. 嵌套结构的处理

```python
# 安全获取嵌套值
def safe_get(data, keys, default=None):
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return default
    return data

# 使用
user_age = safe_get(users, ['alice', 'age'], 0)
```

### 4. 字典的比较和验证

```python
# 字典相等性比较
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # True

# 字典包含关系检查
def dict_contains(big_dict, small_dict):
    return all(key in big_dict and big_dict[key] == value
               for key, value in small_dict.items())
```

## 常见错误

### 1. 键类型错误

```python
# 错误：使用可变类型作为键
# data = {[1, 2]: 'value'}  # TypeError

# 正确：使用不可变类型
data = {(1, 2): 'value'}  # 元组可以作为键
```

### 2. 修改遍历中的字典

```python
# 错误：遍历时修改字典
data = {'a': 1, 'b': 2, 'c': 3}
# for key in data:
#     if data[key] > 1:
#         del data[key]  # RuntimeError

# 正确：先收集要删除的键
keys_to_delete = [key for key, value in data.items() if value > 1]
for key in keys_to_delete:
    del data[key]
```

### 3. 深拷贝 vs 浅拷贝

```python
import copy

# 浅拷贝：只复制第一层
original = {'a': [1, 2, 3]}
shallow = original.copy()
shallow['a'].append(4)  # 影响原始字典

# 深拷贝：递归复制所有层级
deep = copy.deepcopy(original)
deep['a'].append(5)  # 不影响原始字典
```

## 实际应用场景

### 1. 配置管理

```python
config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'name': 'mydb'
    },
    'cache': {
        'type': 'redis',
        'ttl': 3600
    },
    'logging': {
        'level': 'INFO',
        'file': 'app.log'
    }
}
```

### 2. 数据处理和分析

```python
# 数据聚合
sales_data = [
    {'product': 'A', 'amount': 100},
    {'product': 'B', 'amount': 200},
    {'product': 'A', 'amount': 150}
]

# 按产品汇总
summary = {}
for sale in sales_data:
    product = sale['product']
    amount = sale['amount']
    summary[product] = summary.get(product, 0) + amount
```

### 3. 缓存系统

```python
cache = {}

def expensive_function(param):
    if param in cache:
        return cache[param]

    # 执行耗时操作
    result = perform_calculation(param)
    cache[param] = result
    return result
```

### 4. 状态机实现

```python
state_transitions = {
    'idle': {'start': 'running', 'stop': 'idle'},
    'running': {'pause': 'paused', 'stop': 'idle'},
    'paused': {'resume': 'running', 'stop': 'idle'}
}

def transition(current_state, action):
    return state_transitions.get(current_state, {}).get(action, current_state)
```

## 性能考虑

### 1. 时间复杂度

- 访问：O(1) 平均情况
- 插入：O(1) 平均情况
- 删除：O(1) 平均情况
- 查找：O(1) 平均情况

### 2. 空间复杂度

- 字典有额外的内存开销
- 负载因子影响性能
- 大量删除操作可能导致内存碎片

### 3. 优化建议

```python
# 预分配字典大小（如果知道大概大小）
large_dict = dict.fromkeys(range(1000))

# 使用字典推导式而不是循环
data = {k: v for k, v in pairs if condition}

# 避免频繁的字典重组
# 批量操作而不是单个操作
```

## 运行说明

1. 运行字典基础操作演示：

   ```bash
   python dict_basics.py
   ```

2. 运行字典遍历演示：

   ```bash
   python dict_traversal.py
   ```

3. 运行嵌套结构演示：

   ```bash
   python nesting.py
   ```

4. 运行练习题：
   ```bash
   python exercises.py
   ```

## 扩展阅读

- Python 官方文档：字典类型
- 哈希表的实现原理
- 字典 vs 其他数据结构的性能比较
- 现代 Python 中的字典优化

通过本章的学习，您已经掌握了 Python 字典的全面知识，包括基本操作、遍历技巧、嵌套结构和实际应用。这些技能将为您后续学习函数、类和高级数据处理奠定坚实基础。
