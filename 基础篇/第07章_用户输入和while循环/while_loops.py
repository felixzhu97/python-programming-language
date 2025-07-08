#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第07章 用户输入和while循环 - while循环
演示while循环的各种用法和应用场景
"""

def main():
    print("=== while循环演示 ===\n")
    
    # 1. while循环的基本语法
    print("1. while循环的基本语法")
    print("-" * 30)
    
    print("基本语法：")
    print("while condition:")
    print("    # 循环体")
    print("    # 更新条件变量")
    print()
    
    # 简单的计数循环
    print("简单计数循环：")
    current_number = 1
    while current_number <= 5:
        print(f"当前数字：{current_number}")
        current_number += 1
    print("循环结束")
    print()
    
    # 2. while循环 vs for循环
    print("2. while循环 vs for循环")
    print("-" * 30)
    
    print("for循环（已知次数）：")
    for i in range(1, 6):
        print(f"for循环：{i}")
    
    print("\nwhile循环（条件控制）：")
    i = 1
    while i <= 5:
        print(f"while循环：{i}")
        i += 1
    print()
    
    # 3. 用户输入控制的循环
    print("3. 用户输入控制的循环")
    print("-" * 30)
    
    print("模拟用户输入控制的循环：")
    
    # 模拟用户输入序列
    simulated_inputs = ["continue", "go", "stop"]
    input_index = 0
    
    message = ""
    while message != "stop":
        # 模拟用户输入
        if input_index < len(simulated_inputs):
            message = simulated_inputs[input_index]
            input_index += 1
        else:
            message = "stop"  # 防止无限循环
        
        print(f"模拟输入：{message}")
        
        if message == "stop":
            print("程序结束")
        else:
            print(f"你输入了：{message}")
    print()
    
    # 4. 使用标志变量
    print("4. 使用标志变量")
    print("-" * 30)
    
    print("使用标志变量控制循环：")
    
    active = True
    simulated_commands = ["help", "status", "quit"]
    command_index = 0
    
    while active:
        # 模拟用户命令
        if command_index < len(simulated_commands):
            command = simulated_commands[command_index]
            command_index += 1
        else:
            command = "quit"
        
        print(f"模拟命令：{command}")
        
        if command == "quit":
            active = False
            print("退出程序")
        elif command == "help":
            print("可用命令：help, status, quit")
        elif command == "status":
            print("系统状态：正常")
        else:
            print("未知命令")
    print()
    
    # 5. break语句
    print("5. break语句")
    print("-" * 30)
    
    print("使用break跳出循环：")
    
    # 寻找特定数字
    numbers = [1, 3, 5, 7, 9, 6, 11, 13]
    target = 6
    index = 0
    found = False
    
    while index < len(numbers):
        current = numbers[index]
        print(f"检查数字：{current}")
        
        if current == target:
            print(f"找到目标数字 {target} 在位置 {index}")
            found = True
            break
        
        index += 1
    
    if not found:
        print(f"未找到目标数字 {target}")
    print()
    
    # 6. continue语句
    print("6. continue语句")
    print("-" * 30)
    
    print("使用continue跳过当前迭代：")
    
    # 只打印奇数
    number = 0
    while number < 10:
        number += 1
        
        if number % 2 == 0:
            continue  # 跳过偶数
        
        print(f"奇数：{number}")
    print()
    
    # 7. 无限循环和防护
    print("7. 无限循环和防护")
    print("-" * 30)
    
    print("防止无限循环的方法：")
    
    # 方法1：设置最大迭代次数
    count = 0
    max_iterations = 5
    
    while True:
        count += 1
        print(f"迭代 {count}")
        
        if count >= max_iterations:
            print("达到最大迭代次数，退出循环")
            break
    print()
    
    # 方法2：超时控制
    import time
    
    print("超时控制示例：")
    start_time = time.time()
    timeout = 0.1  # 0.1秒超时
    iterations = 0
    
    while True:
        iterations += 1
        current_time = time.time()
        
        if current_time - start_time > timeout:
            print(f"超时退出，执行了 {iterations} 次迭代")
            break
        
        # 模拟一些工作
        time.sleep(0.01)
    print()
    
    # 8. 嵌套while循环
    print("8. 嵌套while循环")
    print("-" * 30)
    
    print("嵌套while循环示例（打印乘法表）：")
    
    i = 1
    while i <= 3:  # 外层循环
        j = 1
        while j <= 3:  # 内层循环
            result = i * j
            print(f"{i} × {j} = {result}")
            j += 1
        print(f"第 {i} 行完成")
        i += 1
    print()
    
    # 9. while循环处理列表
    print("9. while循环处理列表")
    print("-" * 30)
    
    # 逐个处理列表元素
    numbers = [1, 2, 3, 4, 5]
    print(f"原始列表：{numbers}")
    
    while numbers:  # 当列表不为空时
        current = numbers.pop(0)  # 移除第一个元素
        print(f"处理元素：{current}")
    
    print(f"处理后的列表：{numbers}")
    print()
    
    # 在两个列表之间移动元素
    unconfirmed_users = ['alice', 'brian', 'candace']
    confirmed_users = []
    
    print("用户确认过程：")
    print(f"未确认用户：{unconfirmed_users}")
    print(f"已确认用户：{confirmed_users}")
    print()
    
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print(f"正在验证用户：{current_user.title()}")
        confirmed_users.append(current_user)
    
    print("\n确认完成：")
    print(f"未确认用户：{unconfirmed_users}")
    print(f"已确认用户：{confirmed_users}")
    print()
    
    # 10. 删除列表中的特定值
    print("10. 删除列表中的特定值")
    print("-" * 30)
    
    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(f"原始宠物列表：{pets}")
    
    # 删除所有的'cat'
    while 'cat' in pets:
        pets.remove('cat')
        print(f"删除一只cat后：{pets}")
    
    print(f"最终宠物列表：{pets}")
    print()
    
    # 11. 用字典存储用户输入
    print("11. 用字典存储用户输入")
    print("-" * 30)
    
    print("模拟调查问卷：")
    
    responses = {}
    polling_active = True
    
    # 模拟用户响应
    simulated_responses = [
        ("Alice", "Python"),
        ("Bob", "Java"),
        ("Charlie", "C++"),
        ("quit", "")
    ]
    response_index = 0
    
    while polling_active:
        # 模拟用户输入
        if response_index < len(simulated_responses):
            name, language = simulated_responses[response_index]
            response_index += 1
        else:
            name, language = "quit", ""
        
        print(f"模拟输入 - 姓名：{name}")
        
        if name == "quit":
            polling_active = False
            print("调查结束")
        else:
            print(f"模拟输入 - 喜欢的语言：{language}")
            responses[name] = language
            print(f"感谢 {name} 参与调查！")
    
    print("\n调查结果：")
    for name, language in responses.items():
        print(f"{name} 喜欢 {language}")
    print()
    
    # 12. while循环的性能考虑
    print("12. while循环的性能考虑")
    print("-" * 30)
    
    print("性能优化示例：")
    
    # 低效的方法：重复计算长度
    data = list(range(1000))
    start_time = time.time()
    
    i = 0
    while i < len(data):  # 每次都计算len(data)
        # 处理数据
        i += 1
    
    inefficient_time = time.time() - start_time
    
    # 高效的方法：预先计算长度
    start_time = time.time()
    
    i = 0
    data_length = len(data)  # 只计算一次
    while i < data_length:
        # 处理数据
        i += 1
    
    efficient_time = time.time() - start_time
    
    print(f"低效方法用时：{inefficient_time:.6f}秒")
    print(f"高效方法用时：{efficient_time:.6f}秒")
    print(f"性能提升：{inefficient_time/efficient_time:.2f}倍")
    print()
    
    # 13. while循环的错误处理
    print("13. while循环的错误处理")
    print("-" * 30)
    
    def safe_division_loop():
        """安全的除法循环"""
        print("安全除法计算器（模拟版）")
        
        calculations = [
            ("10", "2"),
            ("15", "0"),  # 除零错误
            ("abc", "5"),  # 类型错误
            ("20", "4"),
            ("quit", "")
        ]
        
        calc_index = 0
        active = True
        
        while active:
            try:
                # 模拟用户输入
                if calc_index < len(calculations):
                    num1_str, num2_str = calculations[calc_index]
                    calc_index += 1
                else:
                    num1_str, num2_str = "quit", ""
                
                print(f"模拟输入 - 除数：{num1_str}")
                
                if num1_str == "quit":
                    active = False
                    print("退出计算器")
                    continue
                
                print(f"模拟输入 - 被除数：{num2_str}")
                
                num1 = float(num1_str)
                num2 = float(num2_str)
                
                if num2 == 0:
                    print("错误：不能除以零！")
                    continue
                
                result = num1 / num2
                print(f"结果：{num1} ÷ {num2} = {result}")
                
            except ValueError:
                print("错误：请输入有效的数字！")
            except Exception as e:
                print(f"发生未知错误：{e}")
            
            print()
    
    safe_division_loop()
    
    # 14. 实际应用：游戏循环
    print("14. 实际应用：游戏循环")
    print("-" * 30)
    
    def number_guessing_game():
        """数字猜测游戏（模拟版）"""
        import random
        
        print("数字猜测游戏")
        print("我想了一个1到10之间的数字，你来猜！")
        
        secret_number = random.randint(1, 10)
        print(f"（提示：答案是 {secret_number}）")
        
        # 模拟用户猜测
        guesses = [5, 8, secret_number]
        guess_index = 0
        attempts = 0
        max_attempts = 3
        
        while guess_index < len(guesses) and attempts < max_attempts:
            attempts += 1
            guess = guesses[guess_index]
            guess_index += 1
            
            print(f"第 {attempts} 次猜测：{guess}")
            
            if guess == secret_number:
                print(f"恭喜！你猜对了！答案是 {secret_number}")
                print(f"你用了 {attempts} 次尝试")
                break
            elif guess < secret_number:
                print("太小了，再试试！")
            else:
                print("太大了，再试试！")
        else:
            print(f"游戏结束！答案是 {secret_number}")
    
    number_guessing_game()
    print()
    
    # 15. while循环的调试技巧
    print("15. while循环的调试技巧")
    print("-" * 30)
    
    print("调试while循环的技巧：")
    print("1. 添加调试输出")
    print("2. 检查循环条件")
    print("3. 验证变量更新")
    print("4. 设置迭代计数器")
    print("5. 使用断点调试")
    print()
    
    def debug_while_loop():
        """带调试信息的while循环"""
        target = 15
        current = 1
        iteration = 0
        max_iterations = 20
        
        print(f"寻找目标值：{target}")
        
        while current < target:
            iteration += 1
            
            # 调试输出
            print(f"调试 - 迭代 {iteration}: current={current}, target={target}")
            
            # 防止无限循环
            if iteration > max_iterations:
                print("警告：达到最大迭代次数，可能存在无限循环")
                break
            
            # 更新变量
            current += 2  # 只处理奇数
            
            # 条件检查
            if current >= target:
                print(f"找到目标：{current}")
        
        print(f"循环结束，总迭代次数：{iteration}")
    
    debug_while_loop()
    print()
    
    # 16. while循环的最佳实践
    print("16. while循环的最佳实践")
    print("-" * 30)
    
    print("while循环的最佳实践：")
    print("1. 确保循环条件最终会变为False")
    print("2. 在循环体内更新条件变量")
    print("3. 考虑使用break和continue")
    print("4. 添加适当的错误处理")
    print("5. 避免在循环中进行耗时操作")
    print("6. 使用有意义的变量名")
    print("7. 为复杂循环添加注释")
    print("8. 考虑是否可以用for循环替代")
    print()
    
    print("常见的while循环模式：")
    patterns = {
        "计数循环": "while count < limit:",
        "用户输入": "while user_input != 'quit':",
        "标志控制": "while active:",
        "列表处理": "while items:",
        "条件等待": "while not condition_met:",
        "无限循环": "while True:"
    }
    
    for pattern_name, pattern_code in patterns.items():
        print(f"{pattern_name}：{pattern_code}")
    print()
    
    print("=== while循环演示完成 ===")


if __name__ == "__main__":
    main() 