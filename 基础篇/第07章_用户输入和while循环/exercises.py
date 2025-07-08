#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第07章 用户输入和while循环 - 练习题解答

本文件包含《Python编程：从入门到实践》第7章的所有练习题解答。
涵盖input()函数、while循环、标志变量、break和continue语句等内容。

练习题列表：
7-1. 汽车租赁
7-2. 餐厅订位
7-3. 10的整数倍
7-4. 比萨配料
7-5. 电影票
7-6. 三种出路
7-7. 无限循环
7-8. 熟食店
7-9. 没有熟食店
7-10. 梦想的度假胜地
"""

import time
import random


def main():
    """运行所有练习题"""
    print("=" * 60)
    print("第07章 用户输入和while循环 - 练习题解答")
    print("=" * 60)
    print()
    
    # 练习 7-1: 汽车租赁
    exercise_7_1()
    
    # 练习 7-2: 餐厅订位
    exercise_7_2()
    
    # 练习 7-3: 10的整数倍
    exercise_7_3()
    
    # 练习 7-4: 比萨配料
    exercise_7_4()
    
    # 练习 7-5: 电影票
    exercise_7_5()
    
    # 练习 7-6: 三种出路
    exercise_7_6()
    
    # 练习 7-7: 无限循环
    exercise_7_7()
    
    # 练习 7-8: 熟食店
    exercise_7_8()
    
    # 练习 7-9: 没有熟食店
    exercise_7_9()
    
    # 练习 7-10: 梦想的度假胜地
    exercise_7_10()
    
    # 额外练习：复杂应用
    extra_exercises()


def exercise_7_1():
    """
    练习7-1：汽车租赁
    编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，
    如"Let me see if I can find you a Subaru"。
    """
    print("练习 7-1: 汽车租赁")
    print("-" * 30)
    
    # 模拟用户输入
    car_models = ["Subaru", "Toyota", "Honda", "BMW", "Mercedes"]
    selected_car = random.choice(car_models)
    
    print(f"模拟用户输入：{selected_car}")
    print(f"Let me see if I can find you a {selected_car}.")
    print()
    
    # 真实版本（注释掉以避免阻塞）
    # car = input("What kind of car would you like to rent? ")
    # print(f"Let me see if I can find you a {car}.")


def exercise_7_2():
    """
    练习7-2：餐厅订位
    编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，
    指出没有空桌；否则指出有空桌。
    """
    print("练习 7-2: 餐厅订位")
    print("-" * 30)
    
    # 模拟不同的用餐人数
    party_sizes = [2, 6, 8, 10, 12, 4]
    
    for size in party_sizes:
        print(f"模拟输入用餐人数：{size}")
        
        if size > 8:
            print("抱歉，没有空桌可以容纳这么多人。")
        else:
            print("有空桌，请跟我来。")
        print()
    
    # 真实版本（注释掉以避免阻塞）
    # party_size = int(input("How many people are in your dinner party? "))
    # if party_size > 8:
    #     print("Sorry, there are no available tables.")
    # else:
    #     print("Your table is ready.")


def exercise_7_3():
    """
    练习7-3：10的整数倍
    让用户输入一个数字，并指出该数字是否是10的整数倍。
    """
    print("练习 7-3: 10的整数倍")
    print("-" * 30)
    
    # 模拟不同的数字
    test_numbers = [10, 25, 50, 33, 100, 7, 30]
    
    for number in test_numbers:
        print(f"模拟输入数字：{number}")
        
        if number % 10 == 0:
            print(f"{number} 是10的整数倍。")
        else:
            print(f"{number} 不是10的整数倍。")
        print()
    
    # 真实版本（注释掉以避免阻塞）
    # number = int(input("请输入一个数字："))
    # if number % 10 == 0:
    #     print(f"{number} 是10的整数倍。")
    # else:
    #     print(f"{number} 不是10的整数倍。")


def exercise_7_4():
    """
    练习7-4：比萨配料
    编写一个循环，提示用户输入一系列的比萨配料，直到其输入'quit'为值。
    每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料。
    """
    print("练习 7-4: 比萨配料")
    print("-" * 30)
    
    # 模拟用户输入的配料
    toppings_input = ["pepperoni", "mushrooms", "cheese", "olives", "quit"]
    
    print("请输入比萨配料（输入'quit'结束）：")
    
    for topping in toppings_input:
        print(f"模拟输入：{topping}")
        
        if topping == 'quit':
            print("感谢您的订购！")
            break
        else:
            print(f"我们会在比萨中添加 {topping}。")
    print()
    
    # 真实版本（注释掉以避免阻塞）
    # print("请输入比萨配料（输入'quit'结束）：")
    # while True:
    #     topping = input("配料：")
    #     if topping == 'quit':
    #         break
    #     else:
    #         print(f"我们会在比萨中添加 {topping}。")


def exercise_7_5():
    """
    练习7-5：电影票
    有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；
    3-12岁的观众为10美元；超过12岁的观众为15美元。
    请编写一个循环，在其中询问用户的年龄，并指出其票价。
    """
    print("练习 7-5: 电影票")
    print("-" * 30)
    
    # 模拟不同年龄的观众
    ages_input = [2, 5, 8, 12, 15, 25, 45, "quit"]
    
    print("电影票价格计算器（输入'quit'结束）：")
    
    for age_input in ages_input:
        print(f"模拟输入年龄：{age_input}")
        
        if age_input == "quit":
            print("感谢使用票价计算器！")
            break
        
        age = int(age_input)
        
        if age < 3:
            price = 0
            print(f"年龄 {age} 岁，票价免费！")
        elif age <= 12:
            price = 10
            print(f"年龄 {age} 岁，票价 ${price}")
        else:
            price = 15
            print(f"年龄 {age} 岁，票价 ${price}")
        print()
    
    # 真实版本（注释掉以避免阻塞）
    # print("电影票价格计算器（输入'quit'结束）：")
    # while True:
    #     age_input = input("请输入年龄：")
    #     if age_input == 'quit':
    #         break
    #     
    #     age = int(age_input)
    #     if age < 3:
    #         print("票价：免费")
    #     elif age <= 12:
    #         print("票价：$10")
    #     else:
    #         print("票价：$15")


def exercise_7_6():
    """
    练习7-6：三种出路
    以另一种方式完成练习7-4或7-5，在程序中采用三种方法之一来结束循环：
    在while语句中使用条件测试来结束循环；使用变量来控制循环；使用break语句来结束循环。
    """
    print("练习 7-6: 三种出路")
    print("-" * 30)
    
    # 方法1：在while语句中使用条件测试
    print("方法1：条件测试结束循环")
    toppings = ["pepperoni", "mushrooms", "quit"]
    i = 0
    while i < len(toppings) and toppings[i] != 'quit':
        topping = toppings[i]
        print(f"模拟输入：{topping}")
        print(f"我们会在比萨中添加 {topping}。")
        i += 1
    print("方法1完成\n")
    
    # 方法2：使用变量控制循环
    print("方法2：变量控制循环")
    toppings = ["cheese", "olives", "quit"]
    i = 0
    active = True
    while active and i < len(toppings):
        topping = toppings[i]
        print(f"模拟输入：{topping}")
        if topping == 'quit':
            active = False
        else:
            print(f"我们会在比萨中添加 {topping}。")
        i += 1
    print("方法2完成\n")
    
    # 方法3：使用break语句
    print("方法3：break语句结束循环")
    toppings = ["bacon", "tomato", "quit"]
    i = 0
    while i < len(toppings):
        topping = toppings[i]
        print(f"模拟输入：{topping}")
        if topping == 'quit':
            break
        print(f"我们会在比萨中添加 {topping}。")
        i += 1
    print("方法3完成\n")


def exercise_7_7():
    """
    练习7-7：无限循环
    编写一个没有结束条件的循环，并运行它（要结束该循环，可按Ctrl+C，
    也可关闭显示输出的窗口）。
    """
    print("练习 7-7: 无限循环")
    print("-" * 30)
    
    print("无限循环示例（为了演示，我们限制只运行10次）：")
    
    # 为了演示，我们限制循环次数
    count = 0
    max_count = 10
    
    while True:
        count += 1
        print(f"这是第 {count} 次循环...")
        
        # 为了演示，我们在10次后退出
        if count >= max_count:
            print("为了演示，我们在这里停止无限循环")
            break
        
        # 添加短暂延迟以便观察
        time.sleep(0.1)
    
    print("注意：真正的无限循环会持续运行，直到程序被终止")
    print()


def exercise_7_8():
    """
    练习7-8：熟食店
    创建一个名为sandwich_orders的列表，在其中包含各种三明治的名字；
    再创建一个名为finished_sandwiches的空列表。
    遍历列表sandwich_orders，对于其中的每种三明治，都打印一条消息，
    如I made your tuna sandwich，并将其移到列表finished_sandwiches。
    所有三明治都制作好后，打印一条消息，将这些三明治列出来。
    """
    print("练习 7-8: 熟食店")
    print("-" * 30)
    
    # 待制作的三明治列表
    sandwich_orders = [
        "tuna sandwich",
        "ham sandwich", 
        "turkey sandwich",
        "veggie sandwich",
        "club sandwich"
    ]
    
    # 已完成的三明治列表
    finished_sandwiches = []
    
    print("开始制作三明治...")
    print(f"待制作：{sandwich_orders}")
    print()
    
    # 制作三明治
    while sandwich_orders:
        current_sandwich = sandwich_orders.pop(0)
        print(f"I made your {current_sandwich}.")
        finished_sandwiches.append(current_sandwich)
        
        # 添加短暂延迟以便观察
        time.sleep(0.5)
    
    print()
    print("所有三明治都制作完成！")
    print("已完成的三明治：")
    for sandwich in finished_sandwiches:
        print(f"- {sandwich}")
    print()


def exercise_7_9():
    """
    练习7-9：没有熟食店
    使用为完成练习7-8而创建的列表，但在其中添加'pastrami'。
    在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香熏牛肉卖完了；
    再使用一个while循环将列表中的所有'pastrami'都删除。
    确认最终的列表中不包含'pastrami'。
    """
    print("练习 7-9: 没有熟食店")
    print("-" * 30)
    
    # 待制作的三明治列表（包含多个pastrami）
    sandwich_orders = [
        "tuna sandwich",
        "pastrami",
        "ham sandwich", 
        "pastrami",
        "turkey sandwich",
        "pastrami",
        "veggie sandwich",
        "club sandwich"
    ]
    
    # 已完成的三明治列表
    finished_sandwiches = []
    
    print("熟食店公告：很抱歉，五香熏牛肉(pastrami)已经卖完了！")
    print(f"原始订单：{sandwich_orders}")
    print()
    
    # 移除所有pastrami
    print("正在移除所有pastrami订单...")
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
        print("移除了一个pastrami订单")
    
    print(f"更新后的订单：{sandwich_orders}")
    print()
    
    # 制作剩余的三明治
    print("开始制作剩余的三明治...")
    while sandwich_orders:
        current_sandwich = sandwich_orders.pop(0)
        print(f"I made your {current_sandwich}.")
        finished_sandwiches.append(current_sandwich)
        
        # 添加短暂延迟以便观察
        time.sleep(0.5)
    
    print()
    print("所有可制作的三明治都完成了！")
    print("已完成的三明治：")
    for sandwich in finished_sandwiches:
        print(f"- {sandwich}")
    
    # 确认没有pastrami
    print(f"\n确认：finished_sandwiches中没有pastrami: {'pastrami' not in finished_sandwiches}")
    print()


def exercise_7_10():
    """
    练习7-10：梦想的度假胜地
    编写一个程序，调查用户梦想的度假胜地。使用类似于"If you could visit one place in the world, where would you go?"
    的提示，并编写一个循环，让用户可以输入任意数量的度假胜地。
    每当用户输入新的度假胜地时，都在屏幕上打印一条类似于"I'd love to go to 巴黎!"的消息。
    """
    print("练习 7-10: 梦想的度假胜地")
    print("-" * 30)
    
    # 模拟用户输入的度假胜地
    dream_destinations = [
        "Paris",
        "Tokyo", 
        "New York",
        "London",
        "Sydney",
        "quit"
    ]
    
    print("If you could visit one place in the world, where would you go?")
    print("(输入'quit'结束调查)")
    print()
    
    visited_destinations = []
    
    for destination in dream_destinations:
        print(f"模拟输入：{destination}")
        
        if destination.lower() == 'quit':
            print("感谢您参与我们的调查！")
            break
        
        visited_destinations.append(destination)
        print(f"I'd love to go to {destination}!")
        print()
    
    # 显示调查结果
    if visited_destinations:
        print("调查结果 - 梦想的度假胜地：")
        for i, dest in enumerate(visited_destinations, 1):
            print(f"{i}. {dest}")
    print()
    
    # 真实版本（注释掉以避免阻塞）
    # print("If you could visit one place in the world, where would you go?")
    # print("(输入'quit'结束调查)")
    # 
    # while True:
    #     destination = input("度假胜地：")
    #     if destination == 'quit':
    #         break
    #     print(f"I'd love to go to {destination}!")


def extra_exercises():
    """额外的复杂练习"""
    print("额外练习：复杂应用")
    print("-" * 30)
    
    # 1. 用户登录系统
    print("1. 用户登录系统")
    print("-" * 20)
    
    # 模拟用户数据库
    users = {
        "admin": "password123",
        "user1": "mypass",
        "user2": "secret"
    }
    
    # 模拟登录尝试
    login_attempts = [
        ("admin", "wrongpass"),
        ("admin", "password123"),
        ("user1", "mypass"),
        ("unknown", "test")
    ]
    
    max_attempts = 3
    
    for username, password in login_attempts:
        print(f"模拟登录尝试 - 用户名：{username}, 密码：{password}")
        
        if username in users and users[username] == password:
            print(f"登录成功！欢迎 {username}")
        else:
            print("登录失败：用户名或密码错误")
        print()
    
    # 2. 菜单驱动程序
    print("2. 菜单驱动程序")
    print("-" * 20)
    
    menu_choices = ["1", "2", "3", "4", "quit"]
    
    for choice in menu_choices:
        print("\n=== 计算器菜单 ===")
        print("1. 加法")
        print("2. 减法")
        print("3. 乘法")
        print("4. 除法")
        print("quit. 退出")
        
        print(f"模拟选择：{choice}")
        
        if choice == "quit":
            print("感谢使用计算器！")
            break
        elif choice in ["1", "2", "3", "4"]:
            operations = {
                "1": ("加法", lambda x, y: x + y),
                "2": ("减法", lambda x, y: x - y),
                "3": ("乘法", lambda x, y: x * y),
                "4": ("除法", lambda x, y: x / y if y != 0 else "错误：除零")
            }
            
            op_name, op_func = operations[choice]
            print(f"选择了 {op_name}")
            
            # 模拟计算
            num1, num2 = 10, 5
            result = op_func(num1, num2)
            print(f"计算：{num1} {op_name} {num2} = {result}")
        else:
            print("无效选择，请重试")
    
    # 3. 数据统计
    print("\n3. 数据统计")
    print("-" * 20)
    
    # 模拟数据输入
    numbers_input = ["10", "20", "30", "40", "50", "done"]
    numbers = []
    
    print("请输入数字进行统计（输入'done'结束）：")
    
    for num_input in numbers_input:
        print(f"模拟输入：{num_input}")
        
        if num_input == "done":
            break
        
        try:
            number = float(num_input)
            numbers.append(number)
            print(f"添加数字：{number}")
        except ValueError:
            print("请输入有效的数字")
    
    if numbers:
        print(f"\n统计结果：")
        print(f"输入的数字：{numbers}")
        print(f"总数：{len(numbers)}")
        print(f"最大值：{max(numbers)}")
        print(f"最小值：{min(numbers)}")
        print(f"平均值：{sum(numbers) / len(numbers):.2f}")
        print(f"总和：{sum(numbers)}")
    
    print("\n=== 额外练习完成 ===")


if __name__ == "__main__":
    main() 