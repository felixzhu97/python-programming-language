"""
第02章 变量和简单数据类型 - 练习题

这里包含了书中第二章的练习题解答。
"""

print("=== 练习 2-1: 简单消息 ===")
# 将一条消息赋给变量，并将其打印出来
message = "Hello, Python learner!"
print(message)

print("\n=== 练习 2-2: 多条简单消息 ===")
# 将一条消息赋给变量，并将其打印出来；再将变量的值修改为一条新消息，并将其打印出来
message = "Hello, Python learner!"
print(message)

message = "Welcome to the world of Python programming!"
print(message)

print("\n=== 练习 2-3: 个人消息 ===")
# 用变量表示一个人的姓名，并向其显示一条消息
person_name = "张伟"
message = f"你好，{person_name}，今天你想学习Python吗？"
print(message)

print("\n=== 练习 2-4: 调整名字的大小写 ===")
# 用变量表示一个人的姓名，再以小写、大写和首字母大写的方式显示这个人的姓名
name = "alice johnson"
print(f"小写：{name.lower()}")
print(f"大写：{name.upper()}")
print(f"首字母大写：{name.title()}")

print("\n=== 练习 2-5: 名言 ===")
# 找一句你钦佩的名人说的名言，将其和说话者的姓名打印出来
famous_person = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
message = f'{famous_person} once said, "{quote}"'
print(message)

print("\n=== 练习 2-6: 名言2 ===")
# 重复练习2-5，但用变量famous_person表示名人的姓名，再创建要显示的消息并将其赋给变量message
famous_person = "Steve Jobs"
quote = "Stay hungry, stay foolish."
message = f'{famous_person} once said, "{quote}"'
print(message)

print("\n=== 练习 2-7: 删除人名中的空白字符 ===")
# 用变量表示一个人的姓名，并在其开头和末尾都包含一些空白字符
name = "\t  Ada Lovelace  \n"
print(f"原始姓名：'{name}'")
print(f"使用lstrip()：'{name.lstrip()}'")
print(f"使用rstrip()：'{name.rstrip()}'")
print(f"使用strip()：'{name.strip()}'")

print("\n=== 练习 2-8: 数字8 ===")
# 编写4个表达式，它们分别使用加法、减法、乘法和除法运算，但结果都是数字8
print("加法：5 + 3 =", 5 + 3)
print("减法：10 - 2 =", 10 - 2)
print("乘法：2 * 4 =", 2 * 4)
print("除法：16 / 2 =", 16 / 2)

print("\n=== 练习 2-9: 最喜欢的数字 ===")
# 用一个变量来表示你最喜欢的数字，再使用这个变量创建一条消息，指出你最喜欢的数字，然后将这条消息打印出来
favorite_number = 7
message = f"我最喜欢的数字是 {favorite_number}！"
print(message)

print("\n=== 练习 2-10: 添加注释 ===")
# 选择你编写的两个程序，在每个程序中都至少添加一条注释

# 这是一个问候程序
user_name = "小明"  # 存储用户姓名
greeting = f"欢迎你，{user_name}！"  # 创建问候消息
print(greeting)  # 显示问候消息

# 这是一个简单的计算器
num1 = 10  # 第一个数字
num2 = 5   # 第二个数字
result = num1 + num2  # 计算两数之和
print(f"{num1} + {num2} = {result}")  # 显示计算结果

print("\n=== 练习 2-11: Python之禅 ===")
# 在Python终端会话中执行命令import this，并粗略地浏览一下其他指导原则
import this

print("\n=== 额外练习：综合应用 ===")

# 个人信息卡片
first_name = "李"
last_name = "明"
age = 25
city = "北京"
occupation = "软件工程师"

# 使用f-string创建个人信息
full_name = f"{first_name}{last_name}"
info_card = f"""
个人信息卡片
===========
姓名：{full_name.title()}
年龄：{age}岁
城市：{city}
职业：{occupation}
"""

print(info_card)

# 简单的购物计算
item_name = "Python编程书籍"
item_price = 89.90
quantity = 2
discount_rate = 0.15  # 15%折扣

original_total = item_price * quantity
discount_amount = original_total * discount_rate
final_total = original_total - discount_amount

print(f"商品：{item_name}")
print(f"单价：¥{item_price:.2f}")
print(f"数量：{quantity}")
print(f"原价总计：¥{original_total:.2f}")
print(f"折扣金额：¥{discount_amount:.2f}")
print(f"最终总计：¥{final_total:.2f}")

print("\n所有练习完成！") 