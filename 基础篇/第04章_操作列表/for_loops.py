#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第04章 操作列表 - for循环遍历
演示如何使用for循环遍历列表中的每个元素
"""

def main():
    print("=== for循环遍历列表演示 ===\n")
    
    # 1. 基本的for循环
    print("1. 基本的for循环")
    print("-" * 30)
    
    # 遍历魔术师列表
    magicians = ['alice', 'david', 'carolina']
    print(f"魔术师列表：{magicians}")
    
    for magician in magicians:
        print(f"表演者：{magician.title()}")
        print(f"{magician.title()}，那真是一个了不起的魔术！")
        print(f"我期待你的下一个魔术，{magician.title()}。\n")
    
    print("谢谢大家，这真是一场精彩的魔术表演！")
    print()
    
    # 2. 循环中的常见操作
    print("2. 循环中的常见操作")
    print("-" * 30)
    
    # 字符串格式化
    animals = ['dog', 'cat', 'rabbit']
    print(f"动物列表：{animals}")
    
    for animal in animals:
        print(f"A {animal} would make a great pet.")
    
    print("Any of these animals would make a great pet!")
    print()
    
    # 3. 数字列表的遍历
    print("3. 数字列表的遍历")
    print("-" * 30)
    
    numbers = [1, 2, 3, 4, 5]
    print(f"数字列表：{numbers}")
    
    # 计算总和
    total = 0
    for number in numbers:
        total += number
        print(f"当前数字：{number}，累计和：{total}")
    
    print(f"最终总和：{total}")
    print()
    
    # 4. 列表的统计操作
    print("4. 列表的统计操作")
    print("-" * 30)
    
    scores = [85, 92, 78, 96, 88, 75, 90]
    print(f"成绩列表：{scores}")
    
    # 计算平均分
    total_score = 0
    for score in scores:
        total_score += score
    
    average = total_score / len(scores)
    print(f"平均分：{average:.2f}")
    
    # 找出最高分和最低分
    highest = scores[0]
    lowest = scores[0]
    
    for score in scores:
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
    
    print(f"最高分：{highest}")
    print(f"最低分：{lowest}")
    print()
    
    # 5. 条件筛选
    print("5. 条件筛选")
    print("-" * 30)
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"数字列表：{numbers}")
    
    # 筛选偶数
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    
    print(f"偶数：{even_numbers}")
    
    # 筛选大于5的数
    large_numbers = []
    for number in numbers:
        if number > 5:
            large_numbers.append(number)
    
    print(f"大于5的数：{large_numbers}")
    print()
    
    # 6. 字符串处理
    print("6. 字符串处理")
    print("-" * 30)
    
    words = ['python', 'java', 'javascript', 'c++', 'go']
    print(f"编程语言：{words}")
    
    # 转换为大写
    uppercase_words = []
    for word in words:
        uppercase_words.append(word.upper())
    
    print(f"大写形式：{uppercase_words}")
    
    # 计算字符串长度
    word_lengths = []
    for word in words:
        word_lengths.append(len(word))
    
    print(f"长度列表：{word_lengths}")
    
    # 筛选长度大于4的单词
    long_words = []
    for word in words:
        if len(word) > 4:
            long_words.append(word)
    
    print(f"长度大于4的单词：{long_words}")
    print()
    
    # 7. 嵌套列表的遍历
    print("7. 嵌套列表的遍历")
    print("-" * 30)
    
    # 学生信息列表
    students = [
        ['张三', 85, '数学'],
        ['李四', 92, '英语'],
        ['王五', 78, '物理'],
        ['赵六', 96, '化学']
    ]
    
    print("学生信息：")
    for student in students:
        name, score, subject = student
        print(f"姓名：{name}，成绩：{score}，科目：{subject}")
    
    # 计算平均成绩
    total_score = 0
    for student in students:
        total_score += student[1]  # 成绩在索引1
    
    average_score = total_score / len(students)
    print(f"平均成绩：{average_score:.2f}")
    print()
    
    # 8. 实际应用：购物车
    print("8. 实际应用：购物车")
    print("-" * 30)
    
    # 购物车商品列表
    shopping_cart = [
        {'name': '苹果', 'price': 5.5, 'quantity': 3},
        {'name': '香蕉', 'price': 3.2, 'quantity': 2},
        {'name': '橙子', 'price': 4.8, 'quantity': 1},
        {'name': '牛奶', 'price': 12.5, 'quantity': 2}
    ]
    
    print("购物车商品：")
    total_amount = 0
    
    for item in shopping_cart:
        name = item['name']
        price = item['price']
        quantity = item['quantity']
        subtotal = price * quantity
        
        print(f"{name}：{price:.2f}元 × {quantity} = {subtotal:.2f}元")
        total_amount += subtotal
    
    print(f"总计：{total_amount:.2f}元")
    print()
    
    # 9. 循环中的break和continue
    print("9. 循环中的break和continue")
    print("-" * 30)
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"数字列表：{numbers}")
    
    # 使用break跳出循环
    print("使用break找到第一个大于5的数：")
    for number in numbers:
        if number > 5:
            print(f"找到了：{number}")
            break
    
    # 使用continue跳过某些元素
    print("使用continue跳过偶数：")
    for number in numbers:
        if number % 2 == 0:
            continue
        print(f"奇数：{number}")
    print()
    
    # 10. 循环的最佳实践
    print("10. 循环的最佳实践")
    print("-" * 30)
    
    # 使用有意义的变量名
    pizza_toppings = ['pepperoni', 'mushrooms', 'green peppers', 'extra cheese']
    print(f"披萨配料：{pizza_toppings}")
    
    # 好的变量名
    for topping in pizza_toppings:
        print(f"I love {topping} pizza!")
    
    # 缩进的重要性
    print("\n正确的缩进：")
    for topping in pizza_toppings:
        print(f"  - {topping}")
    
    print("I really love pizza!")
    print()
    
    # 11. enumerate()函数的使用
    print("11. enumerate()函数的使用")
    print("-" * 30)
    
    fruits = ['apple', 'banana', 'orange', 'grape']
    print(f"水果列表：{fruits}")
    
    # 获取索引和值
    print("使用enumerate获取索引和值：")
    for index, fruit in enumerate(fruits):
        print(f"索引 {index}: {fruit}")
    
    # 从指定数字开始计数
    print("从1开始计数：")
    for index, fruit in enumerate(fruits, 1):
        print(f"第 {index} 个水果: {fruit}")
    print()
    
    # 12. zip()函数的使用
    print("12. zip()函数的使用")
    print("-" * 30)
    
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    cities = ['北京', '上海', '广州']
    
    print(f"姓名：{names}")
    print(f"年龄：{ages}")
    print(f"城市：{cities}")
    
    print("组合信息：")
    for name, age, city in zip(names, ages, cities):
        print(f"{name}, {age}岁, 住在{city}")


if __name__ == "__main__":
    main() 