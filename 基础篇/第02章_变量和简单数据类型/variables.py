"""
第02章 变量和简单数据类型 - 变量

变量是Python编程的基础概念，用于存储和引用数据。
"""

print("=== 变量基础 ===")

# 简单的变量赋值
message = "Hello Python world!"
print(message)

# 变量值可以改变
message = "Hello Python Crash Course world!"
print(message)

# 使用变量在字符串中
name = "Alice"
age = 25
print(f"我的名字是{name}，今年{age}岁。")

print("\n=== 变量命名规则 ===")

# 正确的变量命名
student_name = "张三"          # 使用下划线分隔单词
student_age = 20
user_email = "zhang@example.com"
total_score = 95.5

print(f"学生姓名：{student_name}")
print(f"学生年龄：{student_age}")
print(f"邮箱地址：{user_email}")
print(f"总分：{total_score}")

# 变量命名最佳实践示例
first_name = "李"
last_name = "明"
full_name = f"{first_name}{last_name}"
print(f"全名：{full_name}")

print("\n=== 多重赋值 ===")

# 同时给多个变量赋值
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# 给多个变量赋相同的值
a = b = c = 0
print(f"a={a}, b={b}, c={c}")

print("\n=== 常量（约定俗成的命名） ===")

# Python没有真正的常量，但使用全大写表示常量
MAX_CONNECTIONS = 5000
PI = 3.14159
COMPANY_NAME = "Python学习公司"

print(f"最大连接数：{MAX_CONNECTIONS}")
print(f"圆周率：{PI}")
print(f"公司名称：{COMPANY_NAME}")

print("\n=== 变量类型 ===")

# Python会自动推断变量类型
text = "这是字符串"
number = 42
float_number = 3.14
is_student = True

print(f"text的类型：{type(text)}")
print(f"number的类型：{type(number)}")
print(f"float_number的类型：{type(float_number)}")
print(f"is_student的类型：{type(is_student)}")

print("\n=== 变量作为标签的概念 ===")

# 变量更像是标签，而不是盒子
original_list = [1, 2, 3]
another_reference = original_list
another_reference.append(4)

print(f"原始列表：{original_list}")
print(f"另一个引用：{another_reference}")
print("两个变量指向同一个对象！") 