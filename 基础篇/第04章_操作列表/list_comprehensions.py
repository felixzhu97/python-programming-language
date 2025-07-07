#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第04章 操作列表 - 列表推导式
演示如何使用列表推导式简化代码，提高效率
"""

def main():
    print("=== 列表推导式演示 ===\n")
    
    # 1. 基本的列表推导式
    print("1. 基本的列表推导式")
    print("-" * 30)
    
    # 传统方法创建平方数列表
    squares_traditional = []
    for value in range(1, 11):
        squares_traditional.append(value ** 2)
    
    print(f"传统方法创建平方数：{squares_traditional}")
    
    # 使用列表推导式
    squares_comprehension = [value ** 2 for value in range(1, 11)]
    print(f"列表推导式创建平方数：{squares_comprehension}")
    
    # 验证结果相同
    print(f"结果相同：{squares_traditional == squares_comprehension}")
    print()
    
    # 2. 带条件的列表推导式
    print("2. 带条件的列表推导式")
    print("-" * 30)
    
    # 筛选偶数
    numbers = list(range(1, 21))
    print(f"原始数字：{numbers}")
    
    # 传统方法
    even_traditional = []
    for number in numbers:
        if number % 2 == 0:
            even_traditional.append(number)
    
    print(f"传统方法筛选偶数：{even_traditional}")
    
    # 列表推导式
    even_comprehension = [number for number in numbers if number % 2 == 0]
    print(f"列表推导式筛选偶数：{even_comprehension}")
    
    # 筛选奇数的平方
    odd_squares = [number ** 2 for number in numbers if number % 2 == 1]
    print(f"奇数的平方：{odd_squares}")
    print()
    
    # 3. 字符串处理
    print("3. 字符串处理")
    print("-" * 30)
    
    words = ['python', 'java', 'javascript', 'c++', 'go', 'rust']
    print(f"编程语言：{words}")
    
    # 转换为大写
    uppercase_words = [word.upper() for word in words]
    print(f"大写形式：{uppercase_words}")
    
    # 获取长度
    word_lengths = [len(word) for word in words]
    print(f"单词长度：{word_lengths}")
    
    # 筛选长度大于3的单词
    long_words = [word for word in words if len(word) > 3]
    print(f"长度大于3的单词：{long_words}")
    
    # 首字母大写
    title_words = [word.title() for word in words]
    print(f"首字母大写：{title_words}")
    
    # 添加前缀
    prefixed_words = [f"Language: {word}" for word in words]
    print(f"添加前缀：{prefixed_words}")
    print()
    
    # 4. 数学运算
    print("4. 数学运算")
    print("-" * 30)
    
    numbers = list(range(1, 11))
    print(f"数字列表：{numbers}")
    
    # 各种数学运算
    squares = [x ** 2 for x in numbers]
    print(f"平方数：{squares}")
    
    cubes = [x ** 3 for x in numbers]
    print(f"立方数：{cubes}")
    
    reciprocals = [1/x for x in numbers]
    print(f"倒数：{reciprocals}")
    
    # 复杂表达式
    complex_expr = [x ** 2 + 2*x + 1 for x in numbers]
    print(f"x²+2x+1：{complex_expr}")
    
    # 三角函数
    import math
    angles = [math.pi * x / 180 for x in range(0, 91, 15)]  # 角度转弧度
    sin_values = [math.sin(angle) for angle in angles]
    print(f"sin值：{[round(sin, 3) for sin in sin_values]}")
    print()
    
    # 5. 条件表达式（三元运算符）
    print("5. 条件表达式（三元运算符）")
    print("-" * 30)
    
    numbers = [-5, -3, -1, 0, 1, 3, 5]
    print(f"数字列表：{numbers}")
    
    # 将负数转换为0，正数保持不变
    non_negative = [x if x >= 0 else 0 for x in numbers]
    print(f"非负数列表：{non_negative}")
    
    # 标记正负数
    signs = ['positive' if x > 0 else 'negative' if x < 0 else 'zero' for x in numbers]
    print(f"正负标记：{signs}")
    
    # 绝对值
    absolute_values = [abs(x) for x in numbers]
    print(f"绝对值：{absolute_values}")
    print()
    
    # 6. 嵌套列表推导式
    print("6. 嵌套列表推导式")
    print("-" * 30)
    
    # 创建二维列表（矩阵）
    matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(f"3x3乘法表：{matrix}")
    
    # 展开二维列表
    flattened = [item for row in matrix for item in row]
    print(f"展开后：{flattened}")
    
    # 创建坐标点
    coordinates = [(x, y) for x in range(3) for y in range(3)]
    print(f"坐标点：{coordinates}")
    
    # 筛选条件
    filtered_coords = [(x, y) for x in range(5) for y in range(5) if x + y == 4]
    print(f"x+y=4的坐标：{filtered_coords}")
    print()
    
    # 7. 处理多个列表
    print("7. 处理多个列表")
    print("-" * 30)
    
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    
    # 组合信息
    info = [f"{name} is {age} years old" for name, age in zip(names, ages)]
    print(f"个人信息：{info}")
    
    # 两个列表的笛卡尔积
    colors = ['red', 'blue']
    sizes = ['small', 'large']
    combinations = [f"{color} {size}" for color in colors for size in sizes]
    print(f"颜色尺寸组合：{combinations}")
    print()
    
    # 8. 字典推导式
    print("8. 字典推导式")
    print("-" * 30)
    
    # 创建字典
    squares_dict = {x: x**2 for x in range(1, 6)}
    print(f"平方数字典：{squares_dict}")
    
    # 从列表创建字典
    words = ['apple', 'banana', 'cherry']
    word_lengths_dict = {word: len(word) for word in words}
    print(f"单词长度字典：{word_lengths_dict}")
    
    # 条件过滤
    filtered_dict = {k: v for k, v in squares_dict.items() if v > 10}
    print(f"值大于10的字典：{filtered_dict}")
    print()
    
    # 9. 集合推导式
    print("9. 集合推导式")
    print("-" * 30)
    
    # 创建集合
    squares_set = {x**2 for x in range(-5, 6)}
    print(f"平方数集合：{squares_set}")
    
    # 去重
    numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique_numbers = {x for x in numbers_with_duplicates}
    print(f"去重后的数字：{unique_numbers}")
    
    # 字符串字符去重
    text = "hello world"
    unique_chars = {char for char in text if char.isalpha()}
    print(f"唯一字符：{unique_chars}")
    print()
    
    # 10. 生成器表达式
    print("10. 生成器表达式")
    print("-" * 30)
    
    # 生成器表达式（使用圆括号）
    squares_gen = (x**2 for x in range(1, 11))
    print(f"生成器对象：{squares_gen}")
    
    # 转换为列表
    squares_list = list(squares_gen)
    print(f"生成器生成的列表：{squares_list}")
    
    # 内存效率对比
    import sys
    
    # 列表推导式
    list_comp = [x**2 for x in range(1000)]
    print(f"列表推导式内存占用：{sys.getsizeof(list_comp)} bytes")
    
    # 生成器表达式
    gen_exp = (x**2 for x in range(1000))
    print(f"生成器表达式内存占用：{sys.getsizeof(gen_exp)} bytes")
    print()
    
    # 11. 实际应用示例
    print("11. 实际应用示例")
    print("-" * 30)
    
    # 学生成绩处理
    students = [
        {'name': '张三', 'score': 85},
        {'name': '李四', 'score': 92},
        {'name': '王五', 'score': 78},
        {'name': '赵六', 'score': 96},
        {'name': '钱七', 'score': 67}
    ]
    
    print(f"学生信息：{students}")
    
    # 提取姓名
    names = [student['name'] for student in students]
    print(f"学生姓名：{names}")
    
    # 提取成绩
    scores = [student['score'] for student in students]
    print(f"学生成绩：{scores}")
    
    # 筛选优秀学生
    excellent_students = [student['name'] for student in students if student['score'] >= 90]
    print(f"优秀学生：{excellent_students}")
    
    # 成绩等级
    grades = [
        {'name': student['name'], 'grade': 'A' if student['score'] >= 90 else 'B' if student['score'] >= 80 else 'C'}
        for student in students
    ]
    print(f"成绩等级：{grades}")
    print()
    
    # 12. 性能对比
    print("12. 性能对比")
    print("-" * 30)
    
    import time
    
    # 创建大列表进行性能测试
    n = 100000
    
    # 传统for循环
    start_time = time.time()
    traditional = []
    for i in range(n):
        traditional.append(i ** 2)
    end_time = time.time()
    print(f"传统for循环：{end_time - start_time:.4f}秒")
    
    # 列表推导式
    start_time = time.time()
    comprehension = [i ** 2 for i in range(n)]
    end_time = time.time()
    print(f"列表推导式：{end_time - start_time:.4f}秒")
    
    # 验证结果相同
    print(f"结果相同：{traditional == comprehension}")
    print()
    
    # 13. 最佳实践
    print("13. 最佳实践")
    print("-" * 30)
    
    # 保持简洁性
    print("好的列表推导式示例：")
    simple_squares = [x**2 for x in range(10)]
    print(f"简单平方数：{simple_squares}")
    
    # 避免过于复杂的表达式
    print("避免过于复杂的表达式：")
    # 不推荐：太复杂
    # complex_bad = [x**2 + 2*x + 1 if x % 2 == 0 else x**3 - x for x in range(10) if x > 5]
    
    # 推荐：分步骤
    filtered_numbers = [x for x in range(10) if x > 5]
    processed_numbers = [x**2 + 2*x + 1 if x % 2 == 0 else x**3 - x for x in filtered_numbers]
    print(f"分步骤处理：{processed_numbers}")
    
    # 适当使用变量名
    words = ['python', 'java', 'c++']
    uppercase_words = [word.upper() for word in words]  # 清晰的变量名
    print(f"清晰的变量名：{uppercase_words}")


if __name__ == "__main__":
    main() 