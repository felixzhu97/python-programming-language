"""
第03章 介绍列表 - 列表基础

列表是Python中最重要的数据结构之一，用于存储一系列元素。
列表是有序的、可变的，可以包含不同类型的数据。
"""

print("=== 什么是列表 ===")

# 创建列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("自行车品牌列表：", bicycles)

# 列表可以包含不同类型的数据
mixed_list = ['Python', 42, 3.14, True, [1, 2, 3]]
print("混合类型列表：", mixed_list)

# 空列表
empty_list = []
print("空列表：", empty_list)

print("\n=== 访问列表元素 ===")

# 访问列表元素（索引从0开始）
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print("第一个元素：", bicycles[0])
print("第二个元素：", bicycles[1])
print("第三个元素：", bicycles[2])
print("第四个元素：", bicycles[3])

# 使用字符串方法
print("第一个品牌（首字母大写）：", bicycles[0].title())

print("\n=== 负数索引 ===")

# 负数索引从末尾开始计算
print("最后一个元素：", bicycles[-1])
print("倒数第二个元素：", bicycles[-2])
print("倒数第三个元素：", bicycles[-3])

# 在不知道列表长度时访问最后一个元素
last_bicycle = bicycles[-1]
print(f"最后一个自行车品牌是：{last_bicycle.title()}")

print("\n=== 使用列表中的值 ===")

# 在消息中使用列表元素
message = f"我的第一辆自行车是{bicycles[0].title()}。"
print(message)

# 使用列表元素进行计算
prices = [599, 799, 899, 1299]
print("自行车价格：", prices)
print(f"最便宜的自行车：${prices[0]}")
print(f"最贵的自行车：${prices[-1]}")
print(f"价格总和：${sum(prices)}")
print(f"平均价格：${sum(prices) / len(prices):.2f}")

print("\n=== 列表的长度 ===")

# 获取列表长度
print(f"自行车品牌数量：{len(bicycles)}")
print(f"价格数量：{len(prices)}")
print(f"空列表长度：{len(empty_list)}")

# 使用长度进行索引
if len(bicycles) > 0:
    last_index = len(bicycles) - 1
    print(f"最后一个元素的索引是：{last_index}")
    print(f"最后一个元素是：{bicycles[last_index]}")

print("\n=== 列表的基本操作 ===")

# 检查元素是否在列表中
print("检查元素是否存在：")
print("'trek' in bicycles:", 'trek' in bicycles)
print("'giant' in bicycles:", 'giant' in bicycles)

# 计算元素出现次数
numbers = [1, 2, 3, 2, 4, 2, 5]
print(f"\n数字列表：{numbers}")
print(f"数字2出现的次数：{numbers.count(2)}")

# 查找元素的索引
print(f"数字3的索引：{numbers.index(3)}")

print("\n=== 列表切片预览 ===")

# 简单的切片操作（第4章会详细讲解）
fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']
print("水果列表：", fruits)
print("前三个水果：", fruits[:3])
print("后两个水果：", fruits[-2:])
print("中间的水果：", fruits[1:4])

print("\n=== 实际应用示例 ===")

# 学生成绩管理
students = ['张三', '李四', '王五', '赵六']
scores = [85, 92, 78, 96]

print("学生成绩单：")
print("-" * 20)
for i in range(len(students)):
    student = students[i]
    score = scores[i]
    print(f"{student}: {score}分")

# 找出最高分学生
max_score = max(scores)
max_index = scores.index(max_score)
top_student = students[max_index]
print(f"\n最高分学生：{top_student}（{max_score}分）")

# 购物清单
shopping_list = ['牛奶', '面包', '鸡蛋', '苹果', '香蕉']
print(f"\n购物清单（共{len(shopping_list)}项）：")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")

print("\n=== 常见错误示例 ===")

# 索引错误示例
try:
    # 这会引发IndexError
    print("尝试访问不存在的索引：")
    result = bicycles[10]  # 只有4个元素，索引3是最大的
except IndexError as e:
    print(f"索引错误：{e}")
    print("正确做法：先检查列表长度或使用负数索引")

try:
    # 空列表访问
    print("\n尝试访问空列表：")
    result = empty_list[0]
except IndexError as e:
    print(f"索引错误：{e}")
    print("正确做法：先检查列表是否为空")

# 正确的访问方式
if bicycles:  # 检查列表是否非空
    print(f"\n安全访问：第一个元素是 {bicycles[0]}")
    print(f"安全访问：最后一个元素是 {bicycles[-1]}")
else:
    print("列表为空，无法访问元素")

print("\n=== 列表与字符串的关系 ===")

# 字符串转列表
sentence = "Python is awesome"
words = sentence.split()
print(f"句子：{sentence}")
print(f"单词列表：{words}")

# 列表转字符串
joined_sentence = " ".join(words)
print(f"重新连接：{joined_sentence}")

# 字符串本身也像列表一样可以索引
print(f"\n字符串索引示例：")
word = "Python"
print(f"单词：{word}")
print(f"第一个字符：{word[0]}")
print(f"最后一个字符：{word[-1]}")

print("\n列表基础知识学习完成！")
print("下一步：学习修改、添加和删除列表元素") 