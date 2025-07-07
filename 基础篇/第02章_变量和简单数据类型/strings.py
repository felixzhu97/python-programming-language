"""
第02章 变量和简单数据类型 - 字符串

字符串是Python中最常用的数据类型之一，用于处理文本数据。
"""

print("=== 字符串基础 ===")

# 创建字符串的不同方式
single_quote = 'Hello World'
double_quote = "Hello World"
triple_quote = """这是一个
多行字符串"""

print(single_quote)
print(double_quote)
print(triple_quote)

# 字符串中包含引号
quote_in_string = "我喜欢'Python'编程语言"
apostrophe_in_string = '他说："Python很棒！"'
print(quote_in_string)
print(apostrophe_in_string)

print("\n=== 修改字符串大小写 ===")

name = "ada lovelace"

# 首字母大写
print(f"title()方法：{name.title()}")

# 全部大写
print(f"upper()方法：{name.upper()}")

# 全部小写
print(f"lower()方法：{name.lower()}")

# 首字母大写（句子格式）
print(f"capitalize()方法：{name.capitalize()}")

print("\n=== 在字符串中使用变量（f-string） ===")

first_name = "ada"
last_name = "lovelace"

# f-string格式化
full_name = f"{first_name} {last_name}"
print(f"完整姓名：{full_name}")

# 更复杂的f-string示例
age = 197  # 假设的年龄
message = f"Hello, {full_name.title()}! 你今年{age}岁了。"
print(message)

# f-string中使用表达式
a, b = 10, 20
print(f"{a} + {b} = {a + b}")

print("\n=== 添加空白字符 ===")

# 制表符和换行符
print("Languages:")
print("\tPython")
print("\tC")
print("\tJavaScript")

print("\n带换行符的字符串：")
print("Languages:\nPython\nC\nJavaScript")

# 组合使用制表符和换行符
print("\n格式化输出：")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

print("\n=== 删除空白字符 ===")

# 处理意外的空白字符
favorite_language = "  python  "
print(f"原始字符串：'{favorite_language}'")

# 删除右侧空白
print(f"rstrip()：'{favorite_language.rstrip()}'")

# 删除左侧空白
print(f"lstrip()：'{favorite_language.lstrip()}'")

# 删除两侧空白
print(f"strip()：'{favorite_language.strip()}'")

# 永久删除空白（重新赋值）
favorite_language = favorite_language.strip()
print(f"永久删除后：'{favorite_language}'")

print("\n=== 其他常用字符串方法 ===")

text = "Python Programming Language"

# 字符串长度
print(f"字符串长度：{len(text)}")

# 查找子字符串
print(f"'Python'在字符串中的位置：{text.find('Python')}")
print(f"字符串是否以'Python'开头：{text.startswith('Python')}")
print(f"字符串是否以'Language'结尾：{text.endswith('Language')}")

# 替换字符串
new_text = text.replace("Python", "Java")
print(f"替换后：{new_text}")

# 分割字符串
words = text.split()
print(f"分割成单词：{words}")

# 连接字符串
joined = "-".join(words)
print(f"用'-'连接：{joined}")

print("\n=== 字符串格式化的其他方法 ===")

# format()方法（Python 3.6之前的方式）
template = "我的名字是{}，我{}岁了。"
formatted = template.format("张三", 25)
print(f"format()方法：{formatted}")

# 带索引的format()
template2 = "我的名字是{0}，我{1}岁了，{0}是个好名字。"
formatted2 = template2.format("李四", 30)
print(f"带索引的format()：{formatted2}")

# 百分号格式化（更旧的方式）
old_style = "我的名字是%s，我%d岁了。" % ("王五", 28)
print(f"百分号格式化：{old_style}")

print("\n=== 转义字符 ===")

# 常用转义字符示例
print("转义字符示例：")
print("换行符演示：")
print("第一行\n第二行")

print("\n制表符演示：")
print("列1\t列2\t列3")

print("\n反斜杠：")
print("这是一个\\反斜杠")

print("\n引号处理：")
print("单引号：She said, 'Hello'")
print('双引号：He said, "Hello"')

# 原始字符串（r-string）
raw_string = r"这是原始字符串\n不会解释转义字符"
print(f"原始字符串：{raw_string}")

print("\n=== 常见字符串错误和解决方案 ===")

# 正确处理引号
correct = "I can't do this"  # 正确的方式
print(f"正确处理撇号：{correct}")

# 或者使用转义
escaped = 'I can\'t do this'
print(f"使用转义：{escaped}")

print("\n程序执行完成！") 