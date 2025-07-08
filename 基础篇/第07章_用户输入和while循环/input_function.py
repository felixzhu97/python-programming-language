#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第07章 用户输入和while循环 - input()函数
演示如何使用input()函数获取用户输入
"""

def main():
    print("=== input()函数演示 ===\n")
    
    # 1. 基本的input()函数使用
    print("1. 基本的input()函数使用")
    print("-" * 30)
    
    # 注意：在实际运行时需要用户输入，这里用示例展示语法
    print("# 基本语法示例（注释掉以避免阻塞）")
    print("# name = input('请输入你的姓名：')")
    print("# print(f'你好，{name}！')")
    
    # 模拟用户输入进行演示
    simulated_name = "张三"
    print(f"模拟输入：{simulated_name}")
    print(f"你好，{simulated_name}！")
    print()
    
    # 2. input()函数的特点
    print("2. input()函数的特点")
    print("-" * 30)
    
    print("input()函数的重要特点：")
    print("1. 总是返回字符串类型")
    print("2. 会暂停程序等待用户输入")
    print("3. 用户按回车键结束输入")
    print("4. 可以提供提示信息")
    print()
    
    # 演示数据类型
    print("演示input()返回的数据类型：")
    simulated_input = "25"
    print(f"模拟输入：{simulated_input}")
    print(f"数据类型：{type(simulated_input)}")
    print(f"是否为字符串：{isinstance(simulated_input, str)}")
    print()
    
    # 3. 数值输入的处理
    print("3. 数值输入的处理")
    print("-" * 30)
    
    print("将字符串转换为数值：")
    
    # 整数转换
    age_str = "25"
    age_int = int(age_str)
    print(f"字符串 '{age_str}' 转换为整数：{age_int}")
    print(f"转换后的类型：{type(age_int)}")
    
    # 浮点数转换
    height_str = "175.5"
    height_float = float(height_str)
    print(f"字符串 '{height_str}' 转换为浮点数：{height_float}")
    print(f"转换后的类型：{type(height_float)}")
    print()
    
    # 4. 类型转换错误处理
    print("4. 类型转换错误处理")
    print("-" * 30)
    
    def safe_int_input(prompt, default=0):
        """安全的整数输入函数"""
        try:
            # 这里模拟不同的输入情况
            test_inputs = ["25", "abc", "", "-10"]
            for test_input in test_inputs:
                print(f"测试输入：'{test_input}'")
                try:
                    if test_input == "":
                        result = default
                        print(f"空输入，使用默认值：{result}")
                    else:
                        result = int(test_input)
                        print(f"转换成功：{result}")
                except ValueError:
                    print(f"转换失败，使用默认值：{default}")
                    result = default
                print(f"最终结果：{result}")
                print()
        except Exception as e:
            print(f"发生错误：{e}")
    
    safe_int_input("请输入一个整数：", 0)
    
    # 5. 输入验证
    print("5. 输入验证")
    print("-" * 30)
    
    def validate_age(age_str):
        """验证年龄输入"""
        try:
            age = int(age_str)
            if age < 0:
                return False, "年龄不能为负数"
            elif age > 150:
                return False, "年龄不能超过150岁"
            else:
                return True, f"年龄有效：{age}岁"
        except ValueError:
            return False, "请输入有效的数字"
    
    # 测试不同的年龄输入
    test_ages = ["25", "-5", "200", "abc", "30.5"]
    for test_age in test_ages:
        is_valid, message = validate_age(test_age)
        status = "✓" if is_valid else "✗"
        print(f"{status} 输入 '{test_age}': {message}")
    print()
    
    # 6. 多行输入处理
    print("6. 多行输入处理")
    print("-" * 30)
    
    print("处理多行输入的方法：")
    
    # 方法1：多次调用input()
    print("方法1：多次调用input()")
    print("# first_name = input('请输入名：')")
    print("# last_name = input('请输入姓：')")
    print("# full_name = f'{last_name}{first_name}'")
    
    # 模拟
    first_name = "小明"
    last_name = "张"
    full_name = f"{last_name}{first_name}"
    print(f"模拟结果：{full_name}")
    print()
    
    # 方法2：一次输入多个值（空格分隔）
    print("方法2：空格分隔的多个值")
    print("# user_input = input('请输入姓名和年龄（空格分隔）：')")
    print("# name, age = user_input.split()")
    
    # 模拟
    user_input = "张三 25"
    try:
        name, age = user_input.split()
        print(f"模拟输入：{user_input}")
        print(f"解析结果：姓名={name}, 年龄={age}")
    except ValueError:
        print("输入格式错误，请使用空格分隔")
    print()
    
    # 7. 输入格式化和清理
    print("7. 输入格式化和清理")
    print("-" * 30)
    
    def clean_input(text):
        """清理用户输入"""
        # 去除首尾空白
        cleaned = text.strip()
        # 转换为适当的大小写
        if cleaned:
            cleaned = cleaned.title()  # 首字母大写
        return cleaned
    
    # 测试输入清理
    test_inputs = ["  alice  ", "BOB", "charlie", "  DIANA PRINCE  "]
    print("输入清理示例：")
    for test_input in test_inputs:
        cleaned = clean_input(test_input)
        print(f"原始输入：'{test_input}' -> 清理后：'{cleaned}'")
    print()
    
    # 8. 交互式程序示例
    print("8. 交互式程序示例")
    print("-" * 30)
    
    def interactive_calculator():
        """交互式计算器（模拟版）"""
        print("简单计算器（模拟演示）")
        print("支持的操作：+, -, *, /")
        print()
        
        # 模拟不同的计算
        calculations = [
            ("10", "+", "5"),
            ("20", "-", "8"),
            ("6", "*", "7"),
            ("15", "/", "3"),
            ("10", "/", "0")  # 除零测试
        ]
        
        for num1_str, operator, num2_str in calculations:
            print(f"模拟输入：{num1_str} {operator} {num2_str}")
            
            try:
                num1 = float(num1_str)
                num2 = float(num2_str)
                
                if operator == "+":
                    result = num1 + num2
                elif operator == "-":
                    result = num1 - num2
                elif operator == "*":
                    result = num1 * num2
                elif operator == "/":
                    if num2 == 0:
                        print("错误：不能除以零！")
                        continue
                    result = num1 / num2
                else:
                    print("不支持的操作符")
                    continue
                
                print(f"结果：{num1} {operator} {num2} = {result}")
                
            except ValueError:
                print("请输入有效的数字")
            except Exception as e:
                print(f"计算错误：{e}")
            
            print()
    
    interactive_calculator()
    
    # 9. 输入历史和重试机制
    print("9. 输入历史和重试机制")
    print("-" * 30)
    
    def get_valid_input(prompt, validator, max_attempts=3):
        """获取有效输入的通用函数（模拟版）"""
        attempts = 0
        test_inputs = ["invalid", "also_invalid", "valid_input"]
        
        print(f"模拟获取有效输入：{prompt}")
        
        while attempts < max_attempts:
            # 模拟用户输入
            if attempts < len(test_inputs):
                user_input = test_inputs[attempts]
            else:
                user_input = "final_attempt"
            
            print(f"尝试 {attempts + 1}: '{user_input}'")
            
            if validator(user_input):
                print(f"输入有效：{user_input}")
                return user_input
            else:
                print("输入无效，请重试")
                attempts += 1
        
        print("达到最大尝试次数，使用默认值")
        return None
    
    # 验证函数示例
    def is_valid_email(email):
        return "@" in email and "." in email
    
    result = get_valid_input("请输入邮箱地址：", is_valid_email)
    print(f"最终结果：{result}")
    print()
    
    # 10. 输入的安全性考虑
    print("10. 输入的安全性考虑")
    print("-" * 30)
    
    def secure_input_demo():
        """安全输入演示"""
        print("输入安全性考虑：")
        print("1. 验证输入长度")
        print("2. 过滤危险字符")
        print("3. 防止注入攻击")
        print("4. 限制输入范围")
        print()
        
        dangerous_inputs = [
            "'; DROP TABLE users; --",  # SQL注入尝试
            "<script>alert('xss')</script>",  # XSS尝试
            "A" * 1000,  # 过长输入
            "../../etc/passwd",  # 路径遍历尝试
            "normal_input"  # 正常输入
        ]
        
        for dangerous_input in dangerous_inputs:
            print(f"检查输入：{dangerous_input[:50]}{'...' if len(dangerous_input) > 50 else ''}")
            
            # 长度检查
            if len(dangerous_input) > 100:
                print("  ✗ 输入过长")
                continue
            
            # 危险字符检查
            dangerous_chars = ["<", ">", "'", "\"", ";", "--"]
            has_dangerous_chars = any(char in dangerous_input for char in dangerous_chars)
            if has_dangerous_chars:
                print("  ✗ 包含危险字符")
                continue
            
            # 路径遍历检查
            if ".." in dangerous_input or "/" in dangerous_input:
                print("  ✗ 可能的路径遍历攻击")
                continue
            
            print("  ✓ 输入安全")
        print()
    
    secure_input_demo()
    
    # 11. 实用输入函数库
    print("11. 实用输入函数库")
    print("-" * 30)
    
    class InputHelper:
        """输入助手类"""
        
        @staticmethod
        def get_int(prompt, min_val=None, max_val=None, default=None):
            """获取整数输入（模拟版）"""
            test_value = 25  # 模拟输入
            print(f"{prompt}（模拟输入：{test_value}）")
            
            if min_val is not None and test_value < min_val:
                print(f"值太小，最小值为 {min_val}")
                return default if default is not None else min_val
            
            if max_val is not None and test_value > max_val:
                print(f"值太大，最大值为 {max_val}")
                return default if default is not None else max_val
            
            return test_value
        
        @staticmethod
        def get_choice(prompt, choices):
            """获取选择输入（模拟版）"""
            test_choice = choices[0] if choices else None  # 模拟选择第一个
            print(f"{prompt}")
            print(f"可选项：{', '.join(choices)}")
            print(f"模拟选择：{test_choice}")
            
            if test_choice in choices:
                return test_choice
            else:
                print("无效选择")
                return choices[0] if choices else None
        
        @staticmethod
        def get_yes_no(prompt):
            """获取是/否输入（模拟版）"""
            test_answer = "yes"  # 模拟输入
            print(f"{prompt} (y/n)（模拟输入：{test_answer}）")
            
            return test_answer.lower() in ['yes', 'y', '是', '1', 'true']
    
    # 使用输入助手
    age = InputHelper.get_int("请输入年龄（18-65）：", 18, 65, 25)
    print(f"年龄：{age}")
    
    language = InputHelper.get_choice("选择编程语言：", ["Python", "Java", "C++", "JavaScript"])
    print(f"选择的语言：{language}")
    
    confirm = InputHelper.get_yes_no("确认继续吗？")
    print(f"确认结果：{confirm}")
    print()
    
    # 12. 输入模式和最佳实践
    print("12. 输入模式和最佳实践")
    print("-" * 30)
    
    print("输入处理的最佳实践：")
    print("1. 始终验证输入")
    print("2. 提供清晰的提示信息")
    print("3. 处理异常情况")
    print("4. 提供默认值")
    print("5. 限制重试次数")
    print("6. 考虑输入的安全性")
    print("7. 提供用户友好的错误信息")
    print("8. 支持取消操作")
    print()
    
    print("常见输入模式：")
    patterns = {
        "简单输入": "name = input('姓名：')",
        "数值输入": "age = int(input('年龄：'))",
        "选择输入": "choice = input('选择 (a/b/c)：')",
        "确认输入": "confirm = input('确认吗？(y/n)：')",
        "可选输入": "email = input('邮箱（可选）：') or None",
        "循环输入": "while True: user_input = input('输入：')"
    }
    
    for pattern_name, pattern_code in patterns.items():
        print(f"{pattern_name}：{pattern_code}")
    print()
    
    print("=== input()函数演示完成 ===")
    print("注意：实际使用时需要取消注释相关代码以获取真实用户输入")


if __name__ == "__main__":
    main() 