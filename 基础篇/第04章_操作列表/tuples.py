#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第04章 操作列表 - 元组
演示元组的创建、使用和与列表的区别
"""

def main():
    print("=== 元组演示 ===\n")
    
    # 1. 创建元组
    print("1. 创建元组")
    print("-" * 30)
    
    # 使用圆括号创建元组
    dimensions = (200, 50)
    print(f"矩形尺寸：{dimensions}")
    print(f"元组类型：{type(dimensions)}")
    
    # 访问元组元素
    print(f"长度：{dimensions[0]}")
    print(f"宽度：{dimensions[1]}")
    
    # 创建包含多种数据类型的元组
    mixed_tuple = ('Alice', 25, 175.5, True)
    print(f"混合类型元组：{mixed_tuple}")
    
    # 单元素元组（注意逗号）
    single_element = (42,)
    print(f"单元素元组：{single_element}")
    print(f"单元素元组类型：{type(single_element)}")
    
    # 不加逗号的不是元组
    not_tuple = (42)
    print(f"不是元组：{not_tuple}")
    print(f"不是元组的类型：{type(not_tuple)}")
    
    # 不使用圆括号也可以创建元组
    coordinates = 10, 20
    print(f"坐标：{coordinates}")
    print(f"坐标类型：{type(coordinates)}")
    print()
    
    # 2. 元组的不可变性
    print("2. 元组的不可变性")
    print("-" * 30)
    
    dimensions = (200, 50)
    print(f"原始尺寸：{dimensions}")
    
    # 尝试修改元组元素（会报错）
    try:
        dimensions[0] = 250
    except TypeError as e:
        print(f"错误：{e}")
    
    # 但可以重新定义整个元组
    dimensions = (250, 60)
    print(f"重新定义后的尺寸：{dimensions}")
    print()
    
    # 3. 遍历元组
    print("3. 遍历元组")
    print("-" * 30)
    
    # 遍历所有元素
    colors = ('red', 'green', 'blue', 'yellow')
    print(f"颜色元组：{colors}")
    
    print("遍历颜色：")
    for color in colors:
        print(f"  {color}")
    
    # 使用索引遍历
    print("使用索引遍历：")
    for i in range(len(colors)):
        print(f"  索引{i}：{colors[i]}")
    
    # 使用enumerate遍历
    print("使用enumerate遍历：")
    for index, color in enumerate(colors):
        print(f"  第{index+1}个颜色：{color}")
    print()
    
    # 4. 元组解包
    print("4. 元组解包")
    print("-" * 30)
    
    # 基本解包
    point = (10, 20)
    x, y = point
    print(f"点坐标：{point}")
    print(f"x坐标：{x}")
    print(f"y坐标：{y}")
    
    # 多变量解包
    person = ('Alice', 25, 'Engineer')
    name, age, job = person
    print(f"个人信息：{person}")
    print(f"姓名：{name}")
    print(f"年龄：{age}")
    print(f"职业：{job}")
    
    # 交换变量值
    a, b = 1, 2
    print(f"交换前：a={a}, b={b}")
    a, b = b, a
    print(f"交换后：a={a}, b={b}")
    
    # 函数返回多个值
    def get_name_age():
        return "Bob", 30
    
    name, age = get_name_age()
    print(f"函数返回：姓名={name}, 年龄={age}")
    print()
    
    # 5. 元组的方法
    print("5. 元组的方法")
    print("-" * 30)
    
    numbers = (1, 2, 3, 2, 4, 2, 5)
    print(f"数字元组：{numbers}")
    
    # count()方法：统计元素出现次数
    count_2 = numbers.count(2)
    print(f"数字2出现次数：{count_2}")
    
    # index()方法：查找元素索引
    index_3 = numbers.index(3)
    print(f"数字3的索引：{index_3}")
    
    # 查找不存在的元素
    try:
        index_6 = numbers.index(6)
    except ValueError as e:
        print(f"查找6的错误：{e}")
    
    # 元组长度
    print(f"元组长度：{len(numbers)}")
    print()
    
    # 6. 元组 vs 列表
    print("6. 元组 vs 列表")
    print("-" * 30)
    
    # 性能比较
    import time
    
    # 创建大量数据
    list_data = list(range(1000000))
    tuple_data = tuple(range(1000000))
    
    # 测试访问性能
    start_time = time.time()
    for i in range(1000):
        _ = list_data[i]
    list_time = time.time() - start_time
    
    start_time = time.time()
    for i in range(1000):
        _ = tuple_data[i]
    tuple_time = time.time() - start_time
    
    print(f"列表访问时间：{list_time:.6f}秒")
    print(f"元组访问时间：{tuple_time:.6f}秒")
    
    # 内存占用比较
    import sys
    list_size = sys.getsizeof(list_data)
    tuple_size = sys.getsizeof(tuple_data)
    
    print(f"列表内存占用：{list_size} bytes")
    print(f"元组内存占用：{tuple_size} bytes")
    print(f"元组节省内存：{list_size - tuple_size} bytes")
    print()
    
    # 7. 元组的实际应用
    print("7. 元组的实际应用")
    print("-" * 30)
    
    # 存储配置信息
    database_config = ('localhost', 5432, 'mydb', 'user', 'password')
    host, port, db_name, username, password = database_config
    print(f"数据库配置：")
    print(f"  主机：{host}")
    print(f"  端口：{port}")
    print(f"  数据库：{db_name}")
    print(f"  用户名：{username}")
    print(f"  密码：{password}")
    
    # 存储坐标点
    points = [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]
    print(f"坐标点：{points}")
    
    print("坐标点列表：")
    for point in points:
        x, y = point
        print(f"  ({x}, {y})")
    
    # 存储RGB颜色值
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'purple': (128, 0, 128)
    }
    
    print("RGB颜色值：")
    for color_name, rgb in colors.items():
        r, g, b = rgb
        print(f"  {color_name}: RGB({r}, {g}, {b})")
    print()
    
    # 8. 嵌套元组
    print("8. 嵌套元组")
    print("-" * 30)
    
    # 存储学生信息
    students = (
        ('Alice', 20, ('Math', 'Physics')),
        ('Bob', 21, ('Chemistry', 'Biology')),
        ('Charlie', 19, ('English', 'History'))
    )
    
    print("学生信息：")
    for student in students:
        name, age, subjects = student
        print(f"  姓名：{name}")
        print(f"  年龄：{age}")
        print(f"  科目：{subjects}")
        print()
    
    # 矩阵表示
    matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    print("矩阵：")
    for row in matrix:
        print(f"  {row}")
    
    # 访问矩阵元素
    print(f"矩阵[1][2] = {matrix[1][2]}")
    print()
    
    # 9. 命名元组
    print("9. 命名元组")
    print("-" * 30)
    
    from collections import namedtuple
    
    # 定义命名元组
    Point = namedtuple('Point', ['x', 'y'])
    Person = namedtuple('Person', ['name', 'age', 'job'])
    
    # 创建命名元组实例
    p1 = Point(10, 20)
    p2 = Point(x=30, y=40)
    
    print(f"点1：{p1}")
    print(f"点2：{p2}")
    print(f"点1的x坐标：{p1.x}")
    print(f"点1的y坐标：{p1.y}")
    
    # 创建人员信息
    person1 = Person('Alice', 25, 'Engineer')
    person2 = Person('Bob', 30, 'Doctor')
    
    print(f"人员1：{person1}")
    print(f"人员2：{person2}")
    print(f"人员1姓名：{person1.name}")
    print(f"人员1年龄：{person1.age}")
    
    # 命名元组的方法
    print(f"人员1转换为字典：{person1._asdict()}")
    
    # 替换字段值
    person1_older = person1._replace(age=26)
    print(f"人员1年龄+1：{person1_older}")
    print()
    
    # 10. 元组作为字典键
    print("10. 元组作为字典键")
    print("-" * 30)
    
    # 使用坐标作为键
    chess_board = {
        (0, 0): 'rook',
        (0, 1): 'knight',
        (0, 2): 'bishop',
        (0, 3): 'queen',
        (0, 4): 'king'
    }
    
    print("象棋棋盘：")
    for position, piece in chess_board.items():
        x, y = position
        print(f"  位置({x}, {y})：{piece}")
    
    # 成绩记录
    grades = {
        ('Alice', 'Math'): 95,
        ('Alice', 'Physics'): 88,
        ('Bob', 'Math'): 92,
        ('Bob', 'Physics'): 85
    }
    
    print("成绩记录：")
    for key, grade in grades.items():
        name, subject = key
        print(f"  {name}的{subject}成绩：{grade}")
    print()
    
    # 11. 元组的高级应用
    print("11. 元组的高级应用")
    print("-" * 30)
    
    # 函数参数解包
    def print_point(x, y, z=0):
        print(f"点坐标：({x}, {y}, {z})")
    
    point_2d = (10, 20)
    point_3d = (10, 20, 30)
    
    print_point(*point_2d)
    print_point(*point_3d)
    
    # 多重赋值
    data = (1, 2, 3, 4, 5)
    first, second, *rest = data
    print(f"第一个：{first}")
    print(f"第二个：{second}")
    print(f"其余的：{rest}")
    
    # 忽略不需要的值
    person_data = ('Alice', 25, 'Engineer', 'New York')
    name, age, _, city = person_data
    print(f"姓名：{name}")
    print(f"年龄：{age}")
    print(f"城市：{city}")
    print()
    
    # 12. 元组的最佳实践
    print("12. 元组的最佳实践")
    print("-" * 30)
    
    # 何时使用元组
    print("使用元组的场景：")
    print("1. 存储不会改变的数据")
    print("2. 函数返回多个值")
    print("3. 作为字典的键")
    print("4. 存储配置信息")
    print("5. 坐标和几何数据")
    
    # 何时使用列表
    print("\n使用列表的场景：")
    print("1. 需要修改数据")
    print("2. 数据量会变化")
    print("3. 需要排序")
    print("4. 需要频繁插入/删除")
    
    # 性能考虑
    print("\n性能考虑：")
    print("1. 元组访问速度稍快")
    print("2. 元组内存占用更少")
    print("3. 元组可以作为字典键")
    print("4. 元组创建速度更快")
    
    # 示例：何时选择元组
    # 配置信息 - 使用元组
    config = ('localhost', 8080, 'production')
    
    # 购物车 - 使用列表
    shopping_cart = ['apple', 'banana', 'orange']
    
    # 坐标点 - 使用元组
    position = (100, 200)
    
    # 学生名单 - 使用列表
    students = ['Alice', 'Bob', 'Charlie']
    
    print(f"\n示例：")
    print(f"配置信息（元组）：{config}")
    print(f"购物车（列表）：{shopping_cart}")
    print(f"坐标点（元组）：{position}")
    print(f"学生名单（列表）：{students}")


if __name__ == "__main__":
    main() 