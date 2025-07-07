"""
第02章 变量和简单数据类型 - 数字

Python提供了强大的数字处理功能，包括整数、浮点数和复数。
"""

print("=== 整数运算 ===")

# 基本算术运算
print("加法：2 + 3 =", 2 + 3)
print("减法：3 - 2 =", 3 - 2)
print("乘法：2 * 3 =", 2 * 3)
print("除法：3 / 2 =", 3 / 2)
print("整数除法：7 // 2 =", 7 // 2)
print("取余：7 % 2 =", 7 % 2)

# 幂运算
print("\n幂运算：")
print("3 ** 2 =", 3 ** 2)
print("3 ** 3 =", 3 ** 3)
print("10 ** 6 =", 10 ** 6)

# 运算优先级
print("\n运算优先级：")
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)

print("\n=== 浮点数 ===")

# 浮点数运算
print("0.1 + 0.1 =", 0.1 + 0.1)
print("0.2 + 0.2 =", 0.2 + 0.2)
print("2 * 0.1 =", 2 * 0.1)
print("2 * 0.2 =", 2 * 0.2)

# 浮点数精度问题
print("\n浮点数精度问题：")
print("0.2 + 0.1 =", 0.2 + 0.1)
print("3 * 0.1 =", 3 * 0.1)
print("注意：这是计算机表示浮点数的方式导致的，很正常！")

print("\n=== 整数和浮点数混合运算 ===")

# 任何包含浮点数的运算都会返回浮点数
print("4 / 2 =", 4 / 2)  # 即使结果是整数，也返回浮点数
print("1 + 2.0 =", 1 + 2.0)
print("2 * 3.0 =", 2 * 3.0)
print("3.0 ** 2 =", 3.0 ** 2)

print("\n=== 数字中的下划线 ===")

# 使用下划线提高大数字的可读性
universe_age = 14_000_000_000
print(f"宇宙年龄：{universe_age}年")

# Python会忽略下划线
large_number = 1_000_000
another_way = 10_00_000
yet_another = 1000000

print(f"1_000_000 = {large_number}")
print(f"10_00_000 = {another_way}")
print(f"1000000 = {yet_another}")
print(f"都相等吗？{large_number == another_way == yet_another}")

print("\n=== 多重赋值 ===")

# 同时给多个变量赋值
x, y, z = 0, 0, 0
print(f"x = {x}, y = {y}, z = {z}")

# 多个变量赋相同值
a = b = c = 100
print(f"a = {a}, b = {b}, c = {c}")

print("\n=== 常量 ===")

# Python约定用全大写表示常量
MAX_CONNECTIONS = 5000
PI = 3.14159265359
SPEED_OF_LIGHT = 299_792_458  # 米/秒

print(f"最大连接数：{MAX_CONNECTIONS}")
print(f"圆周率：{PI}")
print(f"光速：{SPEED_OF_LIGHT} 米/秒")

print("\n=== 数学函数 ===")

# 内置数学函数
numbers = [1, 2, 3, 4, 5, -2, -5, 3.7, -3.7]

print(f"列表：{numbers}")
print(f"最小值：{min(numbers)}")
print(f"最大值：{max(numbers)}")
print(f"求和：{sum(numbers)}")
print(f"绝对值示例：abs(-5) = {abs(-5)}")
print(f"四舍五入：round(3.7) = {round(3.7)}")
print(f"向下取整：round(3.7) = {round(3.2)}")

print("\n=== 类型转换 ===")

# 数字类型转换
integer_num = 42
float_num = 3.14
string_num = "123"

print(f"整数转浮点数：int({integer_num}) -> float() = {float(integer_num)}")
print(f"浮点数转整数：float({float_num}) -> int() = {int(float_num)}")
print(f"字符串转整数：'{string_num}' -> int() = {int(string_num)}")
print(f"整数转字符串：{integer_num} -> str() = '{str(integer_num)}'")

print("\n=== 数字格式化 ===")

# 格式化数字输出
price = 19.99
quantity = 3
total = price * quantity

print(f"单价：${price:.2f}")
print(f"数量：{quantity}")
print(f"总计：${total:.2f}")

# 科学计数法
big_number = 1234567890
print(f"大数字：{big_number:e}")
print(f"大数字（保留2位小数）：{big_number:.2e}")

print("\n=== 复数（高级） ===")

# 复数示例
complex_num = 3 + 4j
print(f"复数：{complex_num}")
print(f"实部：{complex_num.real}")
print(f"虚部：{complex_num.imag}")
print(f"模长：{abs(complex_num)}")

print("\n=== 练习示例 ===")

# 计算圆的面积和周长
radius = 5
area = PI * radius ** 2
circumference = 2 * PI * radius

print(f"半径为{radius}的圆：")
print(f"面积：{area:.2f}")
print(f"周长：{circumference:.2f}")

# 温度转换
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit}°F")

print("\n程序执行完成！") 