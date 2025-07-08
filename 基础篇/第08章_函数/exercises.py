#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第08章 函数 - 练习题解答

本文件包含《Python编程：从入门到实践》第8章的所有练习题解答。
涵盖函数定义、参数传递、返回值、模块使用等内容。

练习题列表：
8-1. 消息
8-2. 喜欢的图书
8-3. T恤
8-4. 大号T恤
8-5. 城市
8-6. 城市名
8-7. 专辑
8-8. 用户专辑
8-9. 消息
8-10. 发送消息
8-11. 存档的消息
8-12. 三明治
8-13. 用户资料
8-14. 汽车
8-15. 打印模型
8-16. 导入
8-17. 为导入的函数指定别名
"""


def main():
    """运行所有练习题"""
    print("=" * 60)
    print("第08章 函数 - 练习题解答")
    print("=" * 60)
    print()
    
    # 练习 8-1: 消息
    exercise_8_1()
    
    # 练习 8-2: 喜欢的图书
    exercise_8_2()
    
    # 练习 8-3: T恤
    exercise_8_3()
    
    # 练习 8-4: 大号T恤
    exercise_8_4()
    
    # 练习 8-5: 城市
    exercise_8_5()
    
    # 练习 8-6: 城市名
    exercise_8_6()
    
    # 练习 8-7: 专辑
    exercise_8_7()
    
    # 练习 8-8: 用户专辑
    exercise_8_8()
    
    # 练习 8-9: 消息
    exercise_8_9()
    
    # 练习 8-10: 发送消息
    exercise_8_10()
    
    # 练习 8-11: 存档的消息
    exercise_8_11()
    
    # 练习 8-12: 三明治
    exercise_8_12()
    
    # 练习 8-13: 用户资料
    exercise_8_13()
    
    # 练习 8-14: 汽车
    exercise_8_14()
    
    # 练习 8-15: 打印模型
    exercise_8_15()
    
    # 练习 8-16: 导入
    exercise_8_16()
    
    # 练习 8-17: 为导入的函数指定别名
    exercise_8_17()
    
    # 额外练习：高级函数应用
    extra_exercises()


def exercise_8_1():
    """
    练习8-1：消息
    编写一个名为display_message()的函数，它打印一个句子，指出你在本章学习的内容。
    调用这个函数，确认显示的消息正确无误。
    """
    print("练习 8-1: 消息")
    print("-" * 30)
    
    def display_message():
        """显示本章学习内容的消息"""
        print("在本章中，我学习了如何编写函数！")
        print("函数让我能够将代码组织成可重用的块。")
        print("我学会了如何定义函数、传递参数、返回值以及使用模块。")
    
    print("调用display_message()函数：")
    display_message()
    print()


def exercise_8_2():
    """
    练习8-2：喜欢的图书
    编写一个名为favorite_book()的函数，其中包含一个名为title的参数。
    这个函数打印一条消息，如One of my favorite books is Alice in Wonderland。
    调用这个函数，并将一本图书的名称作为实参传递给它。
    """
    print("练习 8-2: 喜欢的图书")
    print("-" * 30)
    
    def favorite_book(title):
        """显示最喜欢的图书"""
        print(f"One of my favorite books is {title}.")
    
    print("调用favorite_book()函数：")
    favorite_book("Alice in Wonderland")
    favorite_book("To Kill a Mockingbird")
    favorite_book("1984")
    print()


def exercise_8_3():
    """
    练习8-3：T恤
    编写一个名为make_shirt()的函数，它接受一个尺寸以及要印到T恤上的字样。
    这个函数应该打印一个句子，概述T恤的尺寸和字样。
    使用位置实参调用这个函数来制作一件T恤；再使用关键字实参调用这个函数来制作一件T恤。
    """
    print("练习 8-3: T恤")
    print("-" * 30)
    
    def make_shirt(size, message):
        """制作T恤"""
        print(f"制作一件{size}尺寸的T恤，上面印着：'{message}'")
    
    print("使用位置实参：")
    make_shirt("M", "Python is awesome!")
    make_shirt("L", "Code like a ninja")
    
    print("\n使用关键字实参：")
    make_shirt(size="S", message="Hello World")
    make_shirt(message="Keep coding", size="XL")
    print()


def exercise_8_4():
    """
    练习8-4：大号T恤
    修改函数make_shirt()，使其在默认情况下制作一件印有"I love Python"字样的大号T恤。
    调用这个函数来制作如下T恤：一件印有默认字样的大号T恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺寸无关紧要）。
    """
    print("练习 8-4: 大号T恤")
    print("-" * 30)
    
    def make_shirt(size="L", message="I love Python"):
        """制作T恤，默认为大号，印有'I love Python'"""
        print(f"制作一件{size}尺寸的T恤，上面印着：'{message}'")
    
    print("使用默认值：")
    make_shirt()  # 大号，默认字样
    
    print("\n覆盖默认尺寸：")
    make_shirt("M")  # 中号，默认字样
    
    print("\n覆盖默认字样：")
    make_shirt("S", "Python rocks!")  # 小号，自定义字样
    
    print("\n使用关键字参数：")
    make_shirt(message="Code every day", size="XL")
    print()


def exercise_8_5():
    """
    练习8-5：城市
    编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。
    这个函数应该打印一个简单的句子，如Reykjavik is in Iceland。
    给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，其中至少有一座城市不属于默认国家。
    """
    print("练习 8-5: 城市")
    print("-" * 30)
    
    def describe_city(city, country="China"):
        """描述城市"""
        print(f"{city} is in {country}.")
    
    print("调用describe_city()函数：")
    describe_city("Beijing")  # 使用默认国家
    describe_city("Shanghai")  # 使用默认国家
    describe_city("New York", "USA")  # 指定不同国家
    describe_city("Tokyo", "Japan")  # 指定不同国家
    describe_city("London", "UK")  # 指定不同国家
    print()


def exercise_8_6():
    """
    练习8-6：城市名
    编写一个名为city_country()的函数，它接受城市的名字以及该城市所属的国家。
    这个函数应该返回一个格式类似于下面这样的字符串：
    "Santiago, Chile"
    至少使用三个城市-国家对调用这个函数，并打印它返回的值。
    """
    print("练习 8-6: 城市名")
    print("-" * 30)
    
    def city_country(city, country):
        """返回城市-国家的格式化字符串"""
        return f"{city}, {country}"
    
    print("调用city_country()函数：")
    print(city_country("Santiago", "Chile"))
    print(city_country("Beijing", "China"))
    print(city_country("Paris", "France"))
    print(city_country("Tokyo", "Japan"))
    print(city_country("New York", "USA"))
    print()


def exercise_8_7():
    """
    练习8-7：专辑
    编写一个名为make_album()的函数，它构建一个描述音乐专辑的字典。
    这个函数应该接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
    使用这个函数制作三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
    
    给函数make_album()添加一个可选形参，以便能够存储专辑包含的歌曲数。
    如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。
    调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
    """
    print("练习 8-7: 专辑")
    print("-" * 30)
    
    def make_album(artist, title, songs=None):
        """构建描述音乐专辑的字典"""
        album = {
            'artist': artist,
            'title': title
        }
        if songs is not None:
            album['songs'] = songs
        return album
    
    print("调用make_album()函数：")
    album1 = make_album("Taylor Swift", "1989")
    album2 = make_album("Ed Sheeran", "÷ (Divide)")
    album3 = make_album("Adele", "25", 11)
    
    print(album1)
    print(album2)
    print(album3)
    
    # 更多示例
    print("\n更多专辑示例：")
    albums = [
        make_album("The Beatles", "Abbey Road", 17),
        make_album("Pink Floyd", "The Dark Side of the Moon", 10),
        make_album("Queen", "Bohemian Rhapsody"),
        make_album("Michael Jackson", "Thriller", 9)
    ]
    
    for album in albums:
        if 'songs' in album:
            print(f"{album['artist']} - {album['title']} ({album['songs']} songs)")
        else:
            print(f"{album['artist']} - {album['title']}")
    print()


def exercise_8_8():
    """
    练习8-8：用户专辑
    在为完成练习8-7编写的程序中，编写一个while循环，让用户输入一个专辑的歌手和名称。
    获取这些信息后，使用它们来调用函数make_album()并将创建的字典打印出来。
    在这个while循环中，务必要提供退出途径。
    """
    print("练习 8-8: 用户专辑")
    print("-" * 30)
    
    def make_album(artist, title, songs=None):
        """构建描述音乐专辑的字典"""
        album = {
            'artist': artist,
            'title': title
        }
        if songs is not None:
            album['songs'] = songs
        return album
    
    # 模拟用户输入
    user_inputs = [
        ("Taylor Swift", "Folklore"),
        ("The Weeknd", "After Hours"),
        ("Billie Eilish", "Happier Than Ever"),
        ("quit", "")
    ]
    
    print("用户专辑收集程序（模拟版）：")
    print("提示：输入'quit'退出程序")
    
    input_index = 0
    while input_index < len(user_inputs):
        artist, title = user_inputs[input_index]
        input_index += 1
        
        print(f"\n模拟输入歌手名：{artist}")
        if artist.lower() == 'quit':
            print("感谢使用专辑收集程序！")
            break
        
        print(f"模拟输入专辑名：{title}")
        if title.lower() == 'quit':
            print("感谢使用专辑收集程序！")
            break
        
        album = make_album(artist, title)
        print(f"创建的专辑：{album}")
    
    print("\n注意：实际版本会要求用户真实输入")
    print()


def exercise_8_9():
    """
    练习8-9：消息
    创建一个包含一系列短消息的列表，并将其传递给一个名为show_messages()的函数，
    这个函数打印列表中的每条消息。
    """
    print("练习 8-9: 消息")
    print("-" * 30)
    
    def show_messages(messages):
        """显示消息列表中的每条消息"""
        print("显示所有消息：")
        for message in messages:
            print(f"- {message}")
    
    # 创建消息列表
    messages = [
        "Hello, how are you?",
        "Python is a great programming language!",
        "Functions make code more organized.",
        "Don't forget to test your code.",
        "Keep learning and practicing!"
    ]
    
    print("调用show_messages()函数：")
    show_messages(messages)
    print()


def exercise_8_10():
    """
    练习8-10：发送消息
    在你为完成练习8-9而编写的程序中，编写一个名为send_messages()的函数，
    将每条消息都打印出来并移到一个名为sent_messages的列表中。
    调用函数send_messages()，再打印两个列表，确认消息移动正确。
    """
    print("练习 8-10: 发送消息")
    print("-" * 30)
    
    def send_messages(messages, sent_messages):
        """发送消息并将其移动到已发送列表"""
        print("正在发送消息...")
        while messages:
            current_message = messages.pop(0)
            print(f"发送消息：{current_message}")
            sent_messages.append(current_message)
        print("所有消息已发送！")
    
    # 创建消息列表
    messages = [
        "Hello, how are you?",
        "Python is a great programming language!",
        "Functions make code more organized.",
        "Don't forget to test your code.",
        "Keep learning and practicing!"
    ]
    
    sent_messages = []
    
    print("发送前：")
    print(f"待发送消息：{messages}")
    print(f"已发送消息：{sent_messages}")
    
    send_messages(messages, sent_messages)
    
    print("\n发送后：")
    print(f"待发送消息：{messages}")
    print(f"已发送消息：{sent_messages}")
    print()


def exercise_8_11():
    """
    练习8-11：存档的消息
    从你为完成练习8-10而编写的程序开始，在调用函数send_messages()时，
    向它传递消息列表的副本。调用函数send_messages()后，打印两个列表，
    确认原始列表保留了所有消息。
    """
    print("练习 8-11: 存档的消息")
    print("-" * 30)
    
    def send_messages(messages, sent_messages):
        """发送消息并将其移动到已发送列表"""
        print("正在发送消息...")
        while messages:
            current_message = messages.pop(0)
            print(f"发送消息：{current_message}")
            sent_messages.append(current_message)
        print("所有消息已发送！")
    
    # 创建消息列表
    original_messages = [
        "Hello, how are you?",
        "Python is a great programming language!",
        "Functions make code more organized.",
        "Don't forget to test your code.",
        "Keep learning and practicing!"
    ]
    
    sent_messages = []
    
    print("发送前：")
    print(f"原始消息：{original_messages}")
    print(f"已发送消息：{sent_messages}")
    
    # 传递列表的副本
    send_messages(original_messages[:], sent_messages)
    
    print("\n发送后：")
    print(f"原始消息：{original_messages}")  # 原始列表应该保持不变
    print(f"已发送消息：{sent_messages}")
    print()


def exercise_8_12():
    """
    练习8-12：三明治
    编写一个函数，它接受顾客要在三明治中添加的一系列食材。
    这个函数只有一个形参（它收集函数调用中提供的所有食材），
    并打印一条消息，对顾客点的三明治进行概述。
    调用这个函数三次，每次都提供不同数量的实参。
    """
    print("练习 8-12: 三明治")
    print("-" * 30)
    
    def make_sandwich(*ingredients):
        """制作三明治"""
        print("制作三明治，包含以下食材：")
        if ingredients:
            for ingredient in ingredients:
                print(f"- {ingredient}")
        else:
            print("- 没有添加任何食材")
        print("三明治制作完成！\n")
    
    print("调用make_sandwich()函数：")
    make_sandwich("ham", "cheese", "lettuce")
    make_sandwich("turkey", "avocado", "tomato", "mayo", "mustard")
    make_sandwich("peanut butter", "jelly")
    make_sandwich()  # 空三明治
    print()


def exercise_8_13():
    """
    练习8-13：用户资料
    复制前面的程序user_profile.py，在其中调用build_profile()来创建有关你的资料；
    调用这个函数时，指定你的名和姓，以及三个描述你的键-值对。
    """
    print("练习 8-13: 用户资料")
    print("-" * 30)
    
    def build_profile(first, last, **user_info):
        """构建用户资料字典"""
        profile = {
            'first_name': first,
            'last_name': last
        }
        for key, value in user_info.items():
            profile[key] = value
        return profile
    
    print("创建用户资料：")
    
    # 创建我的资料
    my_profile = build_profile("Zhang", "Wei",
                              location="Beijing",
                              field="Software Engineering",
                              hobby="Programming",
                              favorite_language="Python")
    
    print("我的资料：")
    for key, value in my_profile.items():
        print(f"{key}: {value}")
    
    # 创建其他用户资料
    print("\n其他用户资料：")
    user1 = build_profile("Alice", "Johnson",
                         age=28,
                         city="New York",
                         occupation="Data Scientist")
    
    user2 = build_profile("Bob", "Smith",
                         age=35,
                         city="Los Angeles",
                         occupation="Web Developer",
                         years_experience=10)
    
    for user in [user1, user2]:
        print(f"\n{user['first_name']} {user['last_name']}的资料：")
        for key, value in user.items():
            if key not in ['first_name', 'last_name']:
                print(f"  {key}: {value}")
    print()


def exercise_8_14():
    """
    练习8-14：汽车
    编写一个函数，将一辆汽车的信息存储在一个字典中。
    这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
    这样调用这个函数：提供必需的信息，以及两个名称-值对，如颜色和选装配件。
    这个函数必须能够像下面这样进行调用：
    car = make_car('subaru', 'outback', color='blue', tow_package=True)
    打印返回的字典，确认正确地处理了所有的信息。
    """
    print("练习 8-14: 汽车")
    print("-" * 30)
    
    def make_car(manufacturer, model, **car_info):
        """创建汽车信息字典"""
        car = {
            'manufacturer': manufacturer,
            'model': model
        }
        for key, value in car_info.items():
            car[key] = value
        return car
    
    print("创建汽车信息：")
    
    # 按照题目要求的调用方式
    car1 = make_car('subaru', 'outback', color='blue', tow_package=True)
    print("汽车1信息：")
    print(car1)
    
    # 更多示例
    car2 = make_car('toyota', 'camry', 
                   color='red', 
                   year=2023, 
                   sunroof=True,
                   automatic=True)
    
    car3 = make_car('honda', 'civic',
                   color='black',
                   year=2022,
                   mileage=15000,
                   fuel_type='gasoline')
    
    print("\n更多汽车信息：")
    cars = [car2, car3]
    for i, car in enumerate(cars, 2):
        print(f"\n汽车{i}信息：")
        print(f"制造商：{car['manufacturer']}")
        print(f"型号：{car['model']}")
        for key, value in car.items():
            if key not in ['manufacturer', 'model']:
                print(f"{key}：{value}")
    print()


def exercise_8_15():
    """
    练习8-15：打印模型
    将示例printing_models.py中的函数放在另一个名为printing_functions.py的文件中。
    在printing_models.py的开头编写一条import语句，并修改这个文件以使用导入的函数。
    """
    print("练习 8-15: 打印模型")
    print("-" * 30)
    
    # 模拟printing_functions.py模块的内容
    class PrintingFunctions:
        """打印功能模块"""
        
        @staticmethod
        def print_models(unprinted_designs, completed_models):
            """模拟打印每个设计，直到没有未打印的设计为止
            打印每个设计后，都将其移到列表completed_models中
            """
            while unprinted_designs:
                current_design = unprinted_designs.pop()
                print(f"Printing model: {current_design}")
                completed_models.append(current_design)
        
        @staticmethod
        def show_completed_models(completed_models):
            """显示打印好的所有模型"""
            print("\nThe following models have been printed:")
            for completed_model in completed_models:
                print(completed_model)
    
    # 模拟使用导入的函数
    print("模拟从printing_functions模块导入函数：")
    
    # 创建未打印设计列表
    unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
    completed_models = []
    
    print("原始设计列表：")
    print(f"待打印：{unprinted_designs}")
    print(f"已完成：{completed_models}")
    
    # 使用导入的函数
    PrintingFunctions.print_models(unprinted_designs, completed_models)
    PrintingFunctions.show_completed_models(completed_models)
    
    print(f"\n处理后的列表：")
    print(f"待打印：{unprinted_designs}")
    print(f"已完成：{completed_models}")
    print()


def exercise_8_16():
    """
    练习8-16：导入
    选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一个文件中。
    在主程序文件中，使用下述各种方法导入这个函数，再调用它：
    import module_name
    from module_name import function_name
    from module_name import function_name as fn
    import module_name as mn
    from module_name import *
    """
    print("练习 8-16: 导入")
    print("-" * 30)
    
    # 模拟一个独立的模块
    class MathOperations:
        """数学运算模块"""
        
        @staticmethod
        def calculate_area(length, width):
            """计算矩形面积"""
            return length * width
        
        @staticmethod
        def calculate_perimeter(length, width):
            """计算矩形周长"""
            return 2 * (length + width)
    
    print("演示不同的导入方式：")
    
    # 方法1: import module_name
    print("\n1. import module_name 方式：")
    math_ops = MathOperations()
    area1 = math_ops.calculate_area(5, 3)
    print(f"面积：{area1}")
    
    # 方法2: from module_name import function_name
    print("\n2. from module_name import function_name 方式：")
    calculate_area_func = MathOperations.calculate_area
    area2 = calculate_area_func(4, 6)
    print(f"面积：{area2}")
    
    # 方法3: from module_name import function_name as fn
    print("\n3. from module_name import function_name as fn 方式：")
    calc_area = MathOperations.calculate_area
    area3 = calc_area(7, 2)
    print(f"面积：{area3}")
    
    # 方法4: import module_name as mn
    print("\n4. import module_name as mn 方式：")
    math_module = MathOperations()
    area4 = math_module.calculate_area(3, 8)
    print(f"面积：{area4}")
    
    # 方法5: from module_name import *
    print("\n5. from module_name import * 方式：")
    print("注意：这种方式不推荐使用，因为可能导致命名冲突")
    all_area = MathOperations.calculate_area(6, 4)
    all_perimeter = MathOperations.calculate_perimeter(6, 4)
    print(f"面积：{all_area}")
    print(f"周长：{all_perimeter}")
    print()


def exercise_8_17():
    """
    练习8-17：为导入的函数指定别名
    选择练习8-15中的一个函数，并使用as关键字为其指定别名。
    """
    print("练习 8-17: 为导入的函数指定别名")
    print("-" * 30)
    
    # 模拟printing_functions.py模块的内容
    class PrintingFunctions:
        """打印功能模块"""
        
        @staticmethod
        def print_models(unprinted_designs, completed_models):
            """模拟打印每个设计"""
            while unprinted_designs:
                current_design = unprinted_designs.pop()
                print(f"Printing model: {current_design}")
                completed_models.append(current_design)
        
        @staticmethod
        def show_completed_models(completed_models):
            """显示打印好的所有模型"""
            print("\nThe following models have been printed:")
            for completed_model in completed_models:
                print(completed_model)
    
    # 为函数指定别名
    print("为导入的函数指定别名：")
    
    # from printing_functions import print_models as pm
    pm = PrintingFunctions.print_models
    
    # from printing_functions import show_completed_models as show
    show = PrintingFunctions.show_completed_models
    
    # 使用别名调用函数
    unprinted_designs = ['iphone case', 'car model', 'keychain']
    completed_models = []
    
    print("使用别名调用函数：")
    print(f"待打印设计：{unprinted_designs}")
    
    pm(unprinted_designs, completed_models)  # 使用别名pm
    show(completed_models)  # 使用别名show
    
    print(f"\n处理后的列表：")
    print(f"待打印设计：{unprinted_designs}")
    print(f"已完成设计：{completed_models}")
    print()


def extra_exercises():
    """额外的高级练习"""
    print("额外练习：高级函数应用")
    print("-" * 30)
    
    # 1. 函数装饰器
    print("1. 函数装饰器")
    print("-" * 20)
    
    def timing_decorator(func):
        """计时装饰器"""
        import time
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"函数 {func.__name__} 执行时间：{end_time - start_time:.4f}秒")
            return result
        return wrapper
    
    @timing_decorator
    def calculate_factorial(n):
        """计算阶乘"""
        if n <= 1:
            return 1
        return n * calculate_factorial(n - 1)
    
    print("使用装饰器：")
    result = calculate_factorial(5)
    print(f"5! = {result}")
    print()
    
    # 2. 高阶函数
    print("2. 高阶函数")
    print("-" * 20)
    
    def apply_operation(numbers, operation):
        """对数字列表应用操作"""
        return [operation(num) for num in numbers]
    
    def square(x):
        return x ** 2
    
    def cube(x):
        return x ** 3
    
    def double(x):
        return x * 2
    
    numbers = [1, 2, 3, 4, 5]
    print(f"原始数字：{numbers}")
    print(f"平方：{apply_operation(numbers, square)}")
    print(f"立方：{apply_operation(numbers, cube)}")
    print(f"翻倍：{apply_operation(numbers, double)}")
    print()
    
    # 3. 闭包
    print("3. 闭包")
    print("-" * 20)
    
    def create_multiplier(factor):
        """创建乘数函数"""
        def multiplier(x):
            return x * factor
        return multiplier
    
    def create_counter(start=0):
        """创建计数器函数"""
        count = start
        def counter():
            nonlocal count
            count += 1
            return count
        return counter
    
    double_func = create_multiplier(2)
    triple_func = create_multiplier(3)
    
    print(f"double_func(5) = {double_func(5)}")
    print(f"triple_func(4) = {triple_func(4)}")
    
    counter1 = create_counter(10)
    counter2 = create_counter(100)
    
    print(f"counter1(): {counter1()}")
    print(f"counter1(): {counter1()}")
    print(f"counter2(): {counter2()}")
    print(f"counter2(): {counter2()}")
    print()
    
    # 4. 递归函数
    print("4. 递归函数")
    print("-" * 20)
    
    def fibonacci(n):
        """计算斐波那契数列"""
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    def factorial(n):
        """递归计算阶乘"""
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    
    def gcd(a, b):
        """计算最大公约数"""
        if b == 0:
            return a
        return gcd(b, a % b)
    
    print("递归函数示例：")
    print(f"fibonacci(8) = {fibonacci(8)}")
    print(f"factorial(6) = {factorial(6)}")
    print(f"gcd(48, 18) = {gcd(48, 18)}")
    print()
    
    # 5. 函数式编程
    print("5. 函数式编程")
    print("-" * 20)
    
    # 使用lambda函数
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 过滤偶数
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"偶数：{even_numbers}")
    
    # 计算平方
    squares = list(map(lambda x: x ** 2, numbers))
    print(f"平方：{squares}")
    
    # 求和
    from functools import reduce
    total = reduce(lambda x, y: x + y, numbers)
    print(f"求和：{total}")
    
    # 链式操作
    result = reduce(lambda x, y: x + y, 
                   map(lambda x: x ** 2, 
                       filter(lambda x: x % 2 == 0, numbers)))
    print(f"偶数的平方和：{result}")
    print()
    
    print("=== 额外练习完成 ===")


if __name__ == "__main__":
    main() 