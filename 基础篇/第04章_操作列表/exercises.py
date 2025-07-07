#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第04章 操作列表 - 练习题解答
包含书中第04章的所有练习题及其解答
"""

def main():
    print("=== 第04章 操作列表 - 练习题解答 ===\n")
    
    # 练习 4-1: 比萨
    print("练习 4-1: 比萨")
    print("-" * 20)
    pizzas = ['margherita', 'pepperoni', 'hawaiian']
    print(f"比萨列表：{pizzas}")
    
    for pizza in pizzas:
        print(f"I like {pizza} pizza.")
    
    print("I really love pizza!")
    print()
    
    # 练习 4-2: 动物
    print("练习 4-2: 动物")
    print("-" * 20)
    animals = ['dog', 'cat', 'rabbit']
    print(f"动物列表：{animals}")
    
    for animal in animals:
        print(f"A {animal} would make a great pet.")
    
    print("Any of these animals would make a great pet!")
    print()
    
    # 练习 4-3: 数到20
    print("练习 4-3: 数到20")
    print("-" * 20)
    for number in range(1, 21):
        print(number)
    print()
    
    # 练习 4-4: 一百万
    print("练习 4-4: 一百万")
    print("-" * 20)
    million = list(range(1, 1000001))
    print(f"创建了包含{len(million)}个数字的列表")
    print(f"前10个数字：{million[:10]}")
    print(f"后10个数字：{million[-10:]}")
    print()
    
    # 练习 4-5: 计算1~1000000的总和
    print("练习 4-5: 计算1~1000000的总和")
    print("-" * 20)
    million = list(range(1, 1000001))
    print(f"最小值：{min(million)}")
    print(f"最大值：{max(million)}")
    print(f"总和：{sum(million)}")
    print()
    
    # 练习 4-6: 奇数
    print("练习 4-6: 奇数")
    print("-" * 20)
    odd_numbers = list(range(1, 21, 2))
    print(f"1到20的奇数：{odd_numbers}")
    
    for odd in odd_numbers:
        print(odd)
    print()
    
    # 练习 4-7: 3的倍数
    print("练习 4-7: 3的倍数")
    print("-" * 20)
    multiples_of_3 = list(range(3, 31, 3))
    print(f"3到30的3的倍数：{multiples_of_3}")
    
    for multiple in multiples_of_3:
        print(multiple)
    print()
    
    # 练习 4-8: 立方
    print("练习 4-8: 立方")
    print("-" * 20)
    cubes = []
    for value in range(1, 11):
        cubes.append(value ** 3)
    
    print(f"1到10的立方：{cubes}")
    
    for cube in cubes:
        print(cube)
    print()
    
    # 练习 4-9: 立方推导式
    print("练习 4-9: 立方推导式")
    print("-" * 20)
    cubes_comprehension = [value ** 3 for value in range(1, 11)]
    print(f"使用列表推导式创建立方：{cubes_comprehension}")
    print()
    
    # 练习 4-10: 切片
    print("练习 4-10: 切片")
    print("-" * 20)
    my_list = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6']
    print(f"原始列表：{my_list}")
    print(f"前三个元素：{my_list[:3]}")
    print(f"中间三个元素：{my_list[1:4]}")
    print(f"后三个元素：{my_list[-3:]}")
    print()
    
    # 练习 4-11: 我的比萨和你的比萨
    print("练习 4-11: 我的比萨和你的比萨")
    print("-" * 20)
    my_pizzas = ['margherita', 'pepperoni', 'hawaiian']
    friend_pizzas = my_pizzas[:]  # 复制列表
    
    print(f"我的比萨：{my_pizzas}")
    print(f"朋友的比萨：{friend_pizzas}")
    
    # 添加新的比萨
    my_pizzas.append('veggie')
    friend_pizzas.append('meat lovers')
    
    print(f"我的比萨（添加后）：{my_pizzas}")
    print(f"朋友的比萨（添加后）：{friend_pizzas}")
    
    print("我喜欢的比萨：")
    for pizza in my_pizzas:
        print(f"  {pizza}")
    
    print("我朋友喜欢的比萨：")
    for pizza in friend_pizzas:
        print(f"  {pizza}")
    print()
    
    # 练习 4-12: 使用多个循环
    print("练习 4-12: 使用多个循环")
    print("-" * 20)
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:]
    
    my_foods.append('cannoli')
    friend_foods.append('ice cream')
    
    print("我喜欢的食物：")
    for food in my_foods:
        print(f"  {food}")
    
    print("我朋友喜欢的食物：")
    for food in friend_foods:
        print(f"  {food}")
    print()
    
    # 练习 4-13: 自助餐
    print("练习 4-13: 自助餐")
    print("-" * 20)
    basic_foods = ('pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream')
    print(f"基本食物菜单：{basic_foods}")
    
    print("原始菜单：")
    for food in basic_foods:
        print(f"  {food}")
    
    # 尝试修改元组（会报错）
    try:
        basic_foods[0] = 'burger'
    except TypeError as e:
        print(f"尝试修改元组时出错：{e}")
    
    # 重新定义菜单
    basic_foods = ('burger', 'fries', 'carrot cake', 'cannoli', 'ice cream')
    print(f"修改后的菜单：{basic_foods}")
    
    print("修改后的菜单：")
    for food in basic_foods:
        print(f"  {food}")
    print()
    
    # 额外练习：高级列表操作
    print("额外练习：高级列表操作")
    print("-" * 30)
    
    # 练习1：数据分析
    print("练习1：数据分析")
    temperatures = [22, 25, 19, 24, 28, 21, 26, 23, 27, 20]
    print(f"温度数据：{temperatures}")
    print(f"最高温度：{max(temperatures)}")
    print(f"最低温度：{min(temperatures)}")
    print(f"平均温度：{sum(temperatures) / len(temperatures):.1f}")
    
    # 筛选高温天气
    hot_days = [temp for temp in temperatures if temp > 25]
    print(f"高温天气（>25°C）：{hot_days}")
    
    # 练习2：字符串处理
    print("\n练习2：字符串处理")
    words = ['python', 'java', 'javascript', 'html', 'css']
    print(f"编程语言：{words}")
    
    # 转换为大写
    uppercase_words = [word.upper() for word in words]
    print(f"大写形式：{uppercase_words}")
    
    # 筛选长度大于4的单词
    long_words = [word for word in words if len(word) > 4]
    print(f"长度大于4的单词：{long_words}")
    
    # 练习3：嵌套列表
    print("\n练习3：嵌套列表")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"矩阵：{matrix}")
    
    # 展开矩阵
    flattened = [num for row in matrix for num in row]
    print(f"展开后：{flattened}")
    
    # 对角线元素
    diagonal = [matrix[i][i] for i in range(len(matrix))]
    print(f"对角线元素：{diagonal}")
    
    # 练习4：数据统计
    print("\n练习4：数据统计")
    scores = [85, 92, 78, 96, 88, 73, 90, 87, 94, 82]
    print(f"成绩列表：{scores}")
    
    # 成绩分级
    def get_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    
    grades = [get_grade(score) for score in scores]
    print(f"成绩等级：{grades}")
    
    # 统计各等级数量
    grade_counts = {}
    for grade in grades:
        grade_counts[grade] = grade_counts.get(grade, 0) + 1
    
    print(f"等级统计：{grade_counts}")
    
    # 练习5：切片应用
    print("\n练习5：切片应用")
    data = list(range(1, 21))
    print(f"数据：{data}")
    
    # 前半部分
    first_half = data[:10]
    print(f"前半部分：{first_half}")
    
    # 后半部分
    second_half = data[10:]
    print(f"后半部分：{second_half}")
    
    # 偶数索引的元素
    even_indices = data[::2]
    print(f"偶数索引的元素：{even_indices}")
    
    # 奇数索引的元素
    odd_indices = data[1::2]
    print(f"奇数索引的元素：{odd_indices}")
    
    # 倒序
    reversed_data = data[::-1]
    print(f"倒序：{reversed_data}")
    
    # 练习6：元组应用
    print("\n练习6：元组应用")
    
    # 学生信息
    students = [
        ('Alice', 20, 'Math'),
        ('Bob', 21, 'Physics'),
        ('Charlie', 19, 'Chemistry')
    ]
    
    print("学生信息：")
    for name, age, major in students:
        print(f"  {name}，{age}岁，专业：{major}")
    
    # 坐标计算
    points = [(0, 0), (3, 4), (1, 1), (2, 2)]
    print(f"坐标点：{points}")
    
    # 计算距离原点的距离
    distances = [((x**2 + y**2)**0.5) for x, y in points]
    print(f"距离原点的距离：{[round(d, 2) for d in distances]}")
    
    # 练习7：综合应用
    print("\n练习7：综合应用")
    
    # 商品信息
    products = [
        ('苹果', 5.5, 10),
        ('香蕉', 3.2, 15),
        ('橙子', 4.8, 8),
        ('葡萄', 8.9, 12)
    ]
    
    print("商品信息：")
    total_value = 0
    for name, price, quantity in products:
        value = price * quantity
        total_value += value
        print(f"  {name}：{price}元/斤，{quantity}斤，总价：{value}元")
    
    print(f"总价值：{total_value}元")
    
    # 筛选高价商品
    expensive_products = [name for name, price, quantity in products if price > 5]
    print(f"高价商品（>5元/斤）：{expensive_products}")
    
    # 库存排序
    sorted_by_quantity = sorted(products, key=lambda x: x[2], reverse=True)
    print("按库存排序（从高到低）：")
    for name, price, quantity in sorted_by_quantity:
        print(f"  {name}：{quantity}斤")
    
    print("\n第04章练习完成！")


if __name__ == "__main__":
    main() 