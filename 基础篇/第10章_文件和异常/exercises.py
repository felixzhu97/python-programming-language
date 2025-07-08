#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第10章 文件和异常 - 练习题解答

本文件包含《Python编程：从入门到实践》第10章文件和异常的所有练习题解答，
以及额外的高级练习题，帮助深入理解文件操作和异常处理。

练习题涵盖：
1. 文件读取和处理
2. 异常处理
3. JSON数据操作
4. 综合应用项目
5. 高级文件操作
"""

import json
import os
from pathlib import Path


def main():
    """主函数，运行所有练习题"""
    print("=" * 60)
    print("第10章 文件和异常 - 练习题解答")
    print("=" * 60)
    print()
    
    # 练习10-1：Python学习
    print("练习10-1：Python学习")
    print("-" * 30)
    
    def learning_python():
        """创建包含学习Python原因的文件"""
        reasons = [
            "Python是一种易学易用的编程语言",
            "Python有丰富的第三方库",
            "Python在数据科学领域应用广泛",
            "Python语法简洁明了",
            "Python社区活跃，资源丰富"
        ]
        
        # 写入文件
        with open("learning_python.txt", "w", encoding="utf-8") as file:
            for reason in reasons:
                file.write(reason + "\n")
        
        print("已创建 learning_python.txt 文件")
        
        # 读取并显示文件内容
        print("文件内容：")
        with open("learning_python.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    
    learning_python()
    print()
    
    # 练习10-2：C语言学习
    print("练习10-2：C语言学习")
    print("-" * 30)
    
    def c_language_learning():
        """读取文件并替换内容"""
        # 首先确保文件存在
        if not Path("learning_python.txt").exists():
            learning_python()
        
        # 读取文件内容
        with open("learning_python.txt", "r", encoding="utf-8") as file:
            content = file.read()
        
        print("原始内容：")
        print(content)
        
        # 替换Python为C
        modified_content = content.replace("Python", "C")
        
        print("替换后的内容：")
        print(modified_content)
        
        # 可选：写入新文件
        with open("learning_c.txt", "w", encoding="utf-8") as file:
            file.write(modified_content)
        
        print("已创建 learning_c.txt 文件")
    
    c_language_learning()
    print()
    
    # 练习10-3：访客
    print("练习10-3：访客")
    print("-" * 30)
    
    def guest_book():
        """创建访客留言簿"""
        guests = []
        
        print("访客留言簿（输入'quit'退出）：")
        while True:
            name = input("请输入您的姓名：").strip()
            if name.lower() == 'quit':
                break
            if name:
                guests.append(name)
                print(f"你好，{name}！欢迎访问我们的网站。")
        
        # 保存访客信息到文件
        if guests:
            with open("guest_book.txt", "w", encoding="utf-8") as file:
                for guest in guests:
                    file.write(f"{guest}\n")
            
            print(f"\n已将 {len(guests)} 位访客信息保存到 guest_book.txt")
            
            # 读取并显示保存的信息
            print("保存的访客信息：")
            with open("guest_book.txt", "r", encoding="utf-8") as file:
                content = file.read()
                print(content)
        else:
            print("没有访客信息需要保存")
    
    # 模拟自动输入
    print("模拟访客输入（实际使用时会提示用户输入）：")
    mock_guests = ["张三", "李四", "王五"]
    with open("guest_book.txt", "w", encoding="utf-8") as file:
        for guest in mock_guests:
            file.write(f"{guest}\n")
            print(f"你好，{guest}！欢迎访问我们的网站。")
    
    print(f"\n已将 {len(mock_guests)} 位访客信息保存到 guest_book.txt")
    print()
    
    # 练习10-4：访客名单
    print("练习10-4：访客名单")
    print("-" * 30)
    
    def guest_list():
        """读取并显示访客名单"""
        try:
            with open("guest_book.txt", "r", encoding="utf-8") as file:
                print("访客名单：")
                for line_number, name in enumerate(file, 1):
                    print(f"{line_number}. {name.strip()}")
        except FileNotFoundError:
            print("访客名单文件不存在")
    
    guest_list()
    print()
    
    # 练习10-5：关于编程的调查
    print("练习10-5：关于编程的调查")
    print("-" * 30)
    
    def programming_poll():
        """编程调查"""
        responses = []
        
        print("编程调查（输入空行结束）：")
        
        # 模拟用户输入
        mock_responses = [
            "我喜欢Python因为它简单易学",
            "JavaScript让网页变得生动",
            "Java在企业开发中很有用",
            ""
        ]
        
        for response in mock_responses:
            if not response:
                break
            responses.append(response)
            print(f"用户输入：{response}")
        
        # 保存调查结果
        if responses:
            with open("programming_poll.txt", "w", encoding="utf-8") as file:
                for response in responses:
                    file.write(response + "\n")
            
            print(f"\n已保存 {len(responses)} 条调查回复到 programming_poll.txt")
            
            # 显示保存的内容
            print("保存的调查结果：")
            with open("programming_poll.txt", "r", encoding="utf-8") as file:
                for i, line in enumerate(file, 1):
                    print(f"{i}. {line.strip()}")
    
    programming_poll()
    print()
    
    # 练习10-6：加法运算
    print("练习10-6：加法运算")
    print("-" * 30)
    
    def addition_calculator():
        """加法计算器，处理异常"""
        while True:
            try:
                # 模拟用户输入
                first_input = input("请输入第一个数字（回车使用默认值10）：").strip() or "10"
                second_input = input("请输入第二个数字（回车使用默认值5）：").strip() or "5"
                
                first_number = int(first_input)
                second_number = int(second_input)
                
                result = first_number + second_number
                print(f"{first_number} + {second_number} = {result}")
                break
                
            except ValueError:
                print("错误：请输入有效的数字")
                # 在实际应用中，这里会继续循环
                # 为了演示，我们使用默认值
                print("使用默认值：10 + 5 = 15")
                break
    
    addition_calculator()
    print()
    
    # 练习10-7：加法计算器
    print("练习10-7：加法计算器")
    print("-" * 30)
    
    def silent_addition_calculator():
        """静默处理异常的加法计算器"""
        test_cases = [
            ("10", "5"),      # 正常情况
            ("abc", "5"),     # 第一个数无效
            ("10", "xyz"),    # 第二个数无效
            ("3.14", "2.86"), # 浮点数
        ]
        
        for first_input, second_input in test_cases:
            try:
                first_number = int(first_input)
                second_number = int(second_input)
                result = first_number + second_number
                print(f"{first_number} + {second_number} = {result}")
            except ValueError:
                print(f"无法计算：'{first_input}' + '{second_input}' （输入无效）")
    
    silent_addition_calculator()
    print()
    
    # 练习10-8：猫和狗
    print("练习10-8：猫和狗")
    print("-" * 30)
    
    def cats_and_dogs():
        """读取猫和狗的文件"""
        # 创建测试文件
        cat_content = "波斯猫\n英国短毛猫\n缅因猫\n"
        dog_content = "金毛\n拉布拉多\n德国牧羊犬\n"
        
        with open("cats.txt", "w", encoding="utf-8") as file:
            file.write(cat_content)
        
        with open("dogs.txt", "w", encoding="utf-8") as file:
            file.write(dog_content)
        
        # 读取文件
        filenames = ["cats.txt", "dogs.txt"]
        
        for filename in filenames:
            try:
                with open(filename, "r", encoding="utf-8") as file:
                    print(f"{filename} 的内容：")
                    content = file.read()
                    print(content)
            except FileNotFoundError:
                print(f"文件 {filename} 不存在")
    
    cats_and_dogs()
    print()
    
    # 练习10-9：沉默的猫和狗
    print("练习10-9：沉默的猫和狗")
    print("-" * 30)
    
    def silent_cats_and_dogs():
        """静默处理文件不存在的情况"""
        filenames = ["cats.txt", "dogs.txt", "birds.txt"]  # birds.txt不存在
        
        for filename in filenames:
            try:
                with open(filename, "r", encoding="utf-8") as file:
                    print(f"{filename} 的内容：")
                    content = file.read()
                    print(content)
            except FileNotFoundError:
                # 静默处理，不打印错误信息
                pass
    
    silent_cats_and_dogs()
    print()
    
    # 练习10-10：常见单词
    print("练习10-10：常见单词")
    print("-" * 30)
    
    def count_common_words():
        """统计文件中常见单词的出现次数"""
        # 创建测试文件
        content = """Python is a great programming language.
Python is easy to learn and use.
Many developers love Python for its simplicity.
Python has a large community and many libraries."""
        
        with open("text_file.txt", "w", encoding="utf-8") as file:
            file.write(content)
        
        try:
            with open("text_file.txt", "r", encoding="utf-8") as file:
                content = file.read().lower()
                
                # 统计常见单词
                common_words = ["the", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by", "python", "is", "a"]
                
                print("常见单词统计：")
                for word in common_words:
                    count = content.count(word)
                    if count > 0:
                        print(f"'{word}' 出现了 {count} 次")
                
        except FileNotFoundError:
            print("文件不存在")
    
    count_common_words()
    print()
    
    # 练习10-11：喜欢的数字
    print("练习10-11：喜欢的数字")
    print("-" * 30)
    
    def favorite_number():
        """存储和读取喜欢的数字"""
        favorite_num = 42
        
        # 存储到JSON文件
        with open("favorite_number.json", "w") as file:
            json.dump(favorite_num, file)
        
        print(f"已将喜欢的数字 {favorite_num} 保存到文件")
        
        # 从JSON文件读取
        with open("favorite_number.json", "r") as file:
            loaded_number = json.load(file)
        
        print(f"从文件读取的喜欢的数字是：{loaded_number}")
    
    favorite_number()
    print()
    
    # 练习10-12：记住喜欢的数字
    print("练习10-12：记住喜欢的数字")
    print("-" * 30)
    
    def remember_favorite_number():
        """智能地处理喜欢的数字"""
        filename = "favorite_number.json"
        
        try:
            # 尝试读取已存储的数字
            with open(filename, "r") as file:
                favorite_number = json.load(file)
            print(f"我知道你最喜欢的数字！是 {favorite_number}")
        
        except FileNotFoundError:
            # 如果文件不存在，询问用户
            print("请输入你最喜欢的数字（回车使用默认值42）：")
            user_input = input().strip() or "42"
            
            try:
                favorite_number = int(user_input)
                
                # 保存到文件
                with open(filename, "w") as file:
                    json.dump(favorite_number, file)
                
                print(f"我们会记住你最喜欢的数字 {favorite_number}！")
                
            except ValueError:
                print("输入的不是有效数字，使用默认值42")
                favorite_number = 42
                with open(filename, "w") as file:
                    json.dump(favorite_number, file)
    
    remember_favorite_number()
    print()
    
    # 练习10-13：验证用户
    print("练习10-13：验证用户")
    print("-" * 30)
    
    def verify_user():
        """验证用户身份"""
        filename = "username.json"
        
        try:
            # 尝试读取用户名
            with open(filename, "r", encoding="utf-8") as file:
                username = json.load(file)
            
            # 验证用户
            print(f"欢迎回来，{username}！")
            confirm = input(f"您是 {username} 吗？(y/n，回车默认为y)：").strip().lower()
            
            if confirm in ["", "y", "yes"]:
                print(f"欢迎回来，{username}！")
            else:
                # 重新获取用户名
                new_username = input("请输入您的用户名：").strip() or "新用户"
                with open(filename, "w", encoding="utf-8") as file:
                    json.dump(new_username, file)
                print(f"我们会记住您，{new_username}！")
        
        except FileNotFoundError:
            # 首次使用，获取用户名
            username = input("首次使用，请输入您的用户名（回车使用默认值'测试用户'）：").strip() or "测试用户"
            
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(username, file)
            
            print(f"我们会记住您，{username}！")
    
    # 为了演示，先创建一个用户文件
    with open("username.json", "w", encoding="utf-8") as file:
        json.dump("Alice", file)
    
    verify_user()
    print()
    
    # 额外练习：文件数据分析器
    print("额外练习：文件数据分析器")
    print("-" * 30)
    
    def file_analyzer():
        """分析文件内容"""
        # 创建测试数据
        test_data = """Python编程从入门到实践
这是一本很好的Python教程书籍
它包含了很多实际的编程示例
读者可以通过这些示例学习Python
Python是一种流行的编程语言"""
        
        with open("test_data.txt", "w", encoding="utf-8") as file:
            file.write(test_data)
        
        try:
            with open("test_data.txt", "r", encoding="utf-8") as file:
                content = file.read()
                lines = content.split('\n')
                
                # 分析结果
                stats = {
                    "总行数": len(lines),
                    "总字符数": len(content),
                    "总字数": len(content.split()),
                    "平均每行字符数": len(content) / len(lines) if lines else 0,
                    "最长行": max(lines, key=len) if lines else "",
                    "最短行": min(lines, key=len) if lines else ""
                }
                
                print("文件分析结果：")
                for key, value in stats.items():
                    if isinstance(value, float):
                        print(f"{key}: {value:.2f}")
                    else:
                        print(f"{key}: {value}")
                
                # 词频统计
                words = content.lower().split()
                word_count = {}
                for word in words:
                    # 简单清理标点
                    clean_word = word.strip('.,!?;:"()[]{}')
                    if clean_word:
                        word_count[clean_word] = word_count.get(clean_word, 0) + 1
                
                print("\n最常见的词汇（前5个）：")
                sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
                for word, count in sorted_words[:5]:
                    print(f"'{word}': {count}次")
        
        except FileNotFoundError:
            print("分析文件不存在")
        except Exception as e:
            print(f"分析过程中出现错误：{e}")
    
    file_analyzer()
    print()
    
    # 额外练习：日志文件处理器
    print("额外练习：日志文件处理器")
    print("-" * 30)
    
    def log_processor():
        """处理日志文件"""
        # 创建模拟日志文件
        log_entries = [
            "2023-01-01 10:00:00 INFO 用户登录成功 user_id=123",
            "2023-01-01 10:05:00 WARNING 密码错误尝试 user_id=456",
            "2023-01-01 10:10:00 ERROR 数据库连接失败",
            "2023-01-01 10:15:00 INFO 用户注销 user_id=123",
            "2023-01-01 10:20:00 ERROR 文件不存在 file=/data/test.txt",
            "2023-01-01 10:25:00 INFO 系统启动完成"
        ]
        
        with open("app.log", "w", encoding="utf-8") as file:
            for entry in log_entries:
                file.write(entry + "\n")
        
        try:
            # 处理日志
            log_stats = {"INFO": 0, "WARNING": 0, "ERROR": 0}
            error_messages = []
            
            with open("app.log", "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        # 解析日志级别
                        for level in log_stats.keys():
                            if level in line:
                                log_stats[level] += 1
                                if level == "ERROR":
                                    error_messages.append(line)
                                break
            
            print("日志统计：")
            for level, count in log_stats.items():
                print(f"{level}: {count} 条")
            
            print("\n错误信息：")
            for error in error_messages:
                print(f"  {error}")
            
            # 生成报告
            report = {
                "分析时间": "2023-01-01 10:30:00",
                "日志文件": "app.log",
                "统计信息": log_stats,
                "错误详情": error_messages
            }
            
            with open("log_report.json", "w", encoding="utf-8") as file:
                json.dump(report, file, ensure_ascii=False, indent=2)
            
            print("\n已生成日志分析报告：log_report.json")
        
        except Exception as e:
            print(f"处理日志文件时发生错误：{e}")
    
    log_processor()
    print()
    
    # 额外练习：配置文件管理器
    print("额外练习：配置文件管理器")
    print("-" * 30)
    
    class ConfigManager:
        """配置文件管理器"""
        
        def __init__(self, config_file="app_config.json"):
            self.config_file = config_file
            self.config = self.load_config()
        
        def load_config(self):
            """加载配置文件"""
            try:
                with open(self.config_file, "r", encoding="utf-8") as file:
                    return json.load(file)
            except FileNotFoundError:
                # 返回默认配置
                default_config = {
                    "database": {
                        "host": "localhost",
                        "port": 5432,
                        "name": "myapp"
                    },
                    "logging": {
                        "level": "INFO",
                        "file": "app.log"
                    },
                    "features": {
                        "debug_mode": False,
                        "cache_enabled": True
                    }
                }
                self.save_config(default_config)
                return default_config
            except json.JSONDecodeError as e:
                print(f"配置文件格式错误：{e}")
                return {}
        
        def save_config(self, config=None):
            """保存配置文件"""
            if config is None:
                config = self.config
            
            try:
                with open(self.config_file, "w", encoding="utf-8") as file:
                    json.dump(config, file, ensure_ascii=False, indent=2)
                return True
            except Exception as e:
                print(f"保存配置时发生错误：{e}")
                return False
        
        def get_setting(self, key_path, default=None):
            """获取配置项（支持嵌套路径，如 'database.host'）"""
            keys = key_path.split('.')
            value = self.config
            
            for key in keys:
                if isinstance(value, dict) and key in value:
                    value = value[key]
                else:
                    return default
            
            return value
        
        def set_setting(self, key_path, value):
            """设置配置项"""
            keys = key_path.split('.')
            current = self.config
            
            # 导航到正确位置
            for key in keys[:-1]:
                if key not in current:
                    current[key] = {}
                current = current[key]
            
            # 设置值
            current[keys[-1]] = value
            
            # 保存配置
            return self.save_config()
        
        def validate_config(self):
            """验证配置"""
            errors = []
            
            # 检查必要的配置项
            required_settings = [
                "database.host",
                "database.port",
                "logging.level"
            ]
            
            for setting in required_settings:
                if self.get_setting(setting) is None:
                    errors.append(f"缺少必要配置：{setting}")
            
            # 检查数据类型
            if not isinstance(self.get_setting("database.port"), int):
                errors.append("database.port 必须是整数")
            
            return errors
    
    # 测试配置管理器
    print("配置管理器测试：")
    
    config_mgr = ConfigManager()
    
    print("当前配置：")
    print(f"数据库主机：{config_mgr.get_setting('database.host')}")
    print(f"数据库端口：{config_mgr.get_setting('database.port')}")
    print(f"日志级别：{config_mgr.get_setting('logging.level')}")
    print(f"调试模式：{config_mgr.get_setting('features.debug_mode')}")
    
    # 修改配置
    config_mgr.set_setting('features.debug_mode', True)
    config_mgr.set_setting('database.port', 3306)
    
    print("\n修改后的配置：")
    print(f"数据库端口：{config_mgr.get_setting('database.port')}")
    print(f"调试模式：{config_mgr.get_setting('features.debug_mode')}")
    
    # 验证配置
    validation_errors = config_mgr.validate_config()
    if validation_errors:
        print(f"\n配置验证失败：{validation_errors}")
    else:
        print("\n配置验证通过")
    
    print()
    
    # 清理临时文件
    print("清理临时文件")
    print("-" * 30)
    
    temp_files = [
        "learning_python.txt", "learning_c.txt", "guest_book.txt",
        "programming_poll.txt", "cats.txt", "dogs.txt", "text_file.txt",
        "favorite_number.json", "username.json", "test_data.txt",
        "app.log", "log_report.json", "app_config.json"
    ]
    
    cleaned_count = 0
    for file in temp_files:
        try:
            Path(file).unlink()
            cleaned_count += 1
        except FileNotFoundError:
            pass
    
    print(f"已清理 {cleaned_count} 个临时文件")
    print()
    
    print("=== 第10章文件和异常的练习题解答完成 ===")


if __name__ == "__main__":
    main() 