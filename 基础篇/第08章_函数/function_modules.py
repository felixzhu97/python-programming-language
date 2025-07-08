#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第08章 函数 - 函数模块详解

本文件演示Python模块的使用和创建：
1. 导入整个模块
2. 导入特定函数
3. 使用as关键字给函数指定别名
4. 导入模块中的所有函数
5. 创建自定义模块
6. 模块的组织和最佳实践
7. 包的概念和使用
"""

import math
import random
import datetime
from typing import List, Dict, Any


def main():
    """主函数，演示模块的使用"""
    print("=" * 60)
    print("第08章 函数 - 函数模块详解")
    print("=" * 60)
    print()
    
    # 1. 导入整个模块
    print("1. 导入整个模块")
    print("-" * 30)
    
    # 使用math模块
    print("math模块示例：")
    print(f"π的值：{math.pi}")
    print(f"e的值：{math.e}")
    print(f"sqrt(16) = {math.sqrt(16)}")
    print(f"sin(π/2) = {math.sin(math.pi/2)}")
    print(f"log(10) = {math.log(10)}")
    print(f"factorial(5) = {math.factorial(5)}")
    print()
    
    # 使用random模块
    print("random模块示例：")
    print(f"随机整数（1-10）：{random.randint(1, 10)}")
    print(f"随机浮点数（0-1）：{random.random()}")
    
    colors = ['red', 'blue', 'green', 'yellow', 'purple']
    print(f"随机选择颜色：{random.choice(colors)}")
    
    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)
    print(f"打乱后的数字：{numbers}")
    print()
    
    # 使用datetime模块
    print("datetime模块示例：")
    now = datetime.datetime.now()
    print(f"当前时间：{now}")
    print(f"格式化时间：{now.strftime('%Y-%m-%d %H:%M:%S')}")
    
    today = datetime.date.today()
    print(f"今天日期：{today}")
    
    # 计算天数差
    future_date = datetime.date(2024, 12, 31)
    days_diff = (future_date - today).days
    print(f"距离2024年12月31日还有：{days_diff}天")
    print()
    
    # 2. 导入特定函数
    print("2. 导入特定函数")
    print("-" * 30)
    
    # 从模块中导入特定函数
    from math import sqrt, pow, ceil, floor
    from random import randint, choice
    from datetime import datetime, timedelta
    
    print("导入特定函数示例：")
    print(f"sqrt(25) = {sqrt(25)}")
    print(f"pow(2, 3) = {pow(2, 3)}")
    print(f"ceil(4.2) = {ceil(4.2)}")
    print(f"floor(4.8) = {floor(4.8)}")
    print(f"随机数：{randint(1, 100)}")
    print(f"随机选择：{choice(['apple', 'banana', 'orange'])}")
    
    # 计算一周后的日期
    one_week_later = datetime.now() + timedelta(days=7)
    print(f"一周后：{one_week_later.strftime('%Y-%m-%d')}")
    print()
    
    # 3. 使用as关键字给函数指定别名
    print("3. 使用as关键字给函数指定别名")
    print("-" * 30)
    
    import math as m
    from datetime import datetime as dt
    from random import randint as random_int
    
    print("使用别名示例：")
    print(f"使用m.pi：{m.pi}")
    print(f"使用m.cos(0)：{m.cos(0)}")
    print(f"当前时间（dt）：{dt.now()}")
    print(f"随机整数（random_int）：{random_int(1, 50)}")
    print()
    
    # 4. 模块中的所有函数（不推荐）
    print("4. 导入模块中的所有函数")
    print("-" * 30)
    
    # 注意：通常不推荐使用 from module import *
    # 这里只是演示，实际开发中应避免使用
    print("from module import * 的问题：")
    print("1. 可能导致命名冲突")
    print("2. 使代码难以理解和维护")
    print("3. 影响代码的可读性")
    print("4. 难以追踪函数的来源")
    print()
    
    # 5. 自定义模块示例
    print("5. 自定义模块示例")
    print("-" * 30)
    
    # 创建一个简单的计算器模块功能
    class Calculator:
        """简单的计算器类，演示模块化编程"""
        
        @staticmethod
        def add(a, b):
            """加法"""
            return a + b
        
        @staticmethod
        def subtract(a, b):
            """减法"""
            return a - b
        
        @staticmethod
        def multiply(a, b):
            """乘法"""
            return a * b
        
        @staticmethod
        def divide(a, b):
            """除法"""
            if b == 0:
                raise ValueError("除数不能为零")
            return a / b
        
        @staticmethod
        def power(base, exponent):
            """幂运算"""
            return base ** exponent
        
        @staticmethod
        def square_root(number):
            """平方根"""
            if number < 0:
                raise ValueError("不能计算负数的平方根")
            return number ** 0.5
    
    # 使用自定义的计算器
    calc = Calculator()
    print("自定义计算器示例：")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"2^8 = {calc.power(2, 8)}")
    print(f"√16 = {calc.square_root(16)}")
    print()
    
    # 6. 实用工具模块
    print("6. 实用工具模块")
    print("-" * 30)
    
    class StringUtils:
        """字符串工具类"""
        
        @staticmethod
        def capitalize_words(text):
            """将每个单词的首字母大写"""
            return ' '.join(word.capitalize() for word in text.split())
        
        @staticmethod
        def reverse_string(text):
            """反转字符串"""
            return text[::-1]
        
        @staticmethod
        def count_words(text):
            """计算单词数量"""
            return len(text.split())
        
        @staticmethod
        def remove_duplicates(text):
            """移除重复的字符"""
            return ''.join(dict.fromkeys(text))
        
        @staticmethod
        def is_palindrome(text):
            """检查是否为回文"""
            cleaned = ''.join(char.lower() for char in text if char.isalnum())
            return cleaned == cleaned[::-1]
    
    class ListUtils:
        """列表工具类"""
        
        @staticmethod
        def find_duplicates(lst):
            """查找重复元素"""
            seen = set()
            duplicates = set()
            for item in lst:
                if item in seen:
                    duplicates.add(item)
                else:
                    seen.add(item)
            return list(duplicates)
        
        @staticmethod
        def chunk_list(lst, chunk_size):
            """将列表分块"""
            chunks = []
            for i in range(0, len(lst), chunk_size):
                chunks.append(lst[i:i + chunk_size])
            return chunks
        
        @staticmethod
        def flatten_list(nested_list):
            """展平嵌套列表"""
            result = []
            for item in nested_list:
                if isinstance(item, list):
                    result.extend(ListUtils.flatten_list(item))
                else:
                    result.append(item)
            return result
        
        @staticmethod
        def get_unique_elements(lst):
            """获取唯一元素，保持顺序"""
            seen = set()
            unique = []
            for item in lst:
                if item not in seen:
                    seen.add(item)
                    unique.append(item)
            return unique
    
    # 使用工具模块
    print("字符串工具示例：")
    text = "hello world python programming"
    print(f"首字母大写：{StringUtils.capitalize_words(text)}")
    print(f"反转字符串：{StringUtils.reverse_string(text)}")
    print(f"单词数量：{StringUtils.count_words(text)}")
    print(f"移除重复字符：{StringUtils.remove_duplicates('hello')}")
    print(f"是否回文：{StringUtils.is_palindrome('A man a plan a canal Panama')}")
    
    print("\n列表工具示例：")
    numbers = [1, 2, 3, 2, 4, 5, 1, 6]
    print(f"原列表：{numbers}")
    print(f"重复元素：{ListUtils.find_duplicates(numbers)}")
    print(f"分块（大小3）：{ListUtils.chunk_list(numbers, 3)}")
    print(f"唯一元素：{ListUtils.get_unique_elements(numbers)}")
    
    nested = [1, [2, 3], [4, [5, 6]], 7]
    print(f"嵌套列表：{nested}")
    print(f"展平列表：{ListUtils.flatten_list(nested)}")
    print()
    
    # 7. 模块化的数据处理
    print("7. 模块化的数据处理")
    print("-" * 30)
    
    class DataProcessor:
        """数据处理器"""
        
        @staticmethod
        def clean_data(data):
            """清理数据"""
            if isinstance(data, list):
                return [item for item in data if item is not None and item != '']
            elif isinstance(data, dict):
                return {k: v for k, v in data.items() if v is not None and v != ''}
            return data
        
        @staticmethod
        def normalize_data(data):
            """标准化数据"""
            if not data:
                return data
            
            if isinstance(data, list) and all(isinstance(x, (int, float)) for x in data):
                min_val = min(data)
                max_val = max(data)
                range_val = max_val - min_val
                if range_val == 0:
                    return [0] * len(data)
                return [(x - min_val) / range_val for x in data]
            
            return data
        
        @staticmethod
        def aggregate_data(data, operation='sum'):
            """聚合数据"""
            if not data:
                return None
            
            if isinstance(data, list) and all(isinstance(x, (int, float)) for x in data):
                if operation == 'sum':
                    return sum(data)
                elif operation == 'mean':
                    return sum(data) / len(data)
                elif operation == 'max':
                    return max(data)
                elif operation == 'min':
                    return min(data)
                elif operation == 'count':
                    return len(data)
            
            return None
    
    class DataValidator:
        """数据验证器"""
        
        @staticmethod
        def validate_email(email):
            """验证邮箱"""
            return isinstance(email, str) and '@' in email and '.' in email
        
        @staticmethod
        def validate_phone(phone):
            """验证电话号码"""
            return isinstance(phone, str) and phone.replace('-', '').replace(' ', '').isdigit()
        
        @staticmethod
        def validate_age(age):
            """验证年龄"""
            return isinstance(age, int) and 0 <= age <= 150
        
        @staticmethod
        def validate_user_data(user_data):
            """验证用户数据"""
            errors = []
            
            if not user_data.get('name'):
                errors.append('姓名不能为空')
            
            if not DataValidator.validate_email(user_data.get('email', '')):
                errors.append('邮箱格式不正确')
            
            if not DataValidator.validate_age(user_data.get('age', -1)):
                errors.append('年龄不合理')
            
            if user_data.get('phone') and not DataValidator.validate_phone(user_data['phone']):
                errors.append('电话号码格式不正确')
            
            return len(errors) == 0, errors
    
    # 使用数据处理模块
    print("数据处理示例：")
    raw_data = [1, 2, None, 4, 5, '', 7, 8, 9, 10]
    cleaned = DataProcessor.clean_data(raw_data)
    print(f"原始数据：{raw_data}")
    print(f"清理后：{cleaned}")
    
    normalized = DataProcessor.normalize_data(cleaned)
    print(f"标准化：{normalized}")
    
    print(f"聚合（求和）：{DataProcessor.aggregate_data(cleaned, 'sum')}")
    print(f"聚合（平均）：{DataProcessor.aggregate_data(cleaned, 'mean')}")
    
    # 验证用户数据
    test_users = [
        {'name': 'Alice', 'email': 'alice@example.com', 'age': 25, 'phone': '123-456-7890'},
        {'name': '', 'email': 'invalid-email', 'age': 200, 'phone': 'not-a-phone'},
        {'name': 'Bob', 'email': 'bob@example.com', 'age': 30}
    ]
    
    print("\n用户数据验证：")
    for i, user in enumerate(test_users):
        is_valid, errors = DataValidator.validate_user_data(user)
        print(f"用户{i+1}：{'有效' if is_valid else '无效'}")
        if errors:
            for error in errors:
                print(f"  - {error}")
    print()
    
    # 8. 模块组织最佳实践
    print("8. 模块组织最佳实践")
    print("-" * 30)
    
    def demonstrate_module_organization():
        """演示模块组织的最佳实践"""
        print("模块组织的最佳实践：")
        print("1. 模块名称应该简短、全小写")
        print("2. 相关功能应该组织在同一个模块中")
        print("3. 模块应该有清晰的文档字符串")
        print("4. 避免循环导入")
        print("5. 使用__init__.py文件创建包")
        print("6. 公共接口应该在__all__中定义")
        print()
        
        print("典型的项目结构：")
        print("project/")
        print("├── __init__.py")
        print("├── main.py")
        print("├── utils/")
        print("│   ├── __init__.py")
        print("│   ├── string_utils.py")
        print("│   ├── list_utils.py")
        print("│   └── data_utils.py")
        print("├── models/")
        print("│   ├── __init__.py")
        print("│   ├── user.py")
        print("│   └── product.py")
        print("└── tests/")
        print("    ├── __init__.py")
        print("    ├── test_utils.py")
        print("    └── test_models.py")
        print()
        
        print("导入的最佳实践：")
        print("1. 标准库导入")
        print("2. 第三方库导入")
        print("3. 本地应用导入")
        print("4. 按字母顺序排列")
        print("5. 避免使用 from module import *")
        print("6. 使用绝对导入而非相对导入")
    
    demonstrate_module_organization()
    
    # 9. 创建配置模块
    print("9. 创建配置模块")
    print("-" * 30)
    
    class Config:
        """配置管理类"""
        
        # 应用配置
        APP_NAME = "Python学习项目"
        VERSION = "1.0.0"
        DEBUG = True
        
        # 数据库配置
        DATABASE_URL = "sqlite:///app.db"
        DATABASE_POOL_SIZE = 5
        
        # 邮件配置
        MAIL_SERVER = "smtp.example.com"
        MAIL_PORT = 587
        MAIL_USE_TLS = True
        
        # 缓存配置
        CACHE_TYPE = "simple"
        CACHE_DEFAULT_TIMEOUT = 300
        
        @classmethod
        def get_config(cls):
            """获取所有配置"""
            config = {}
            for attr in dir(cls):
                if not attr.startswith('_') and not callable(getattr(cls, attr)):
                    config[attr] = getattr(cls, attr)
            return config
        
        @classmethod
        def update_config(cls, **kwargs):
            """更新配置"""
            for key, value in kwargs.items():
                if hasattr(cls, key):
                    setattr(cls, key, value)
    
    print("配置模块示例：")
    config = Config.get_config()
    print("当前配置：")
    for key, value in config.items():
        print(f"  {key}: {value}")
    
    # 更新配置
    Config.update_config(DEBUG=False, VERSION="1.1.0")
    print(f"\n更新后 DEBUG: {Config.DEBUG}")
    print(f"更新后 VERSION: {Config.VERSION}")
    print()
    
    # 10. 模块测试
    print("10. 模块测试")
    print("-" * 30)
    
    def test_calculator():
        """测试计算器模块"""
        calc = Calculator()
        
        # 测试加法
        assert calc.add(2, 3) == 5, "加法测试失败"
        
        # 测试减法
        assert calc.subtract(10, 4) == 6, "减法测试失败"
        
        # 测试乘法
        assert calc.multiply(3, 4) == 12, "乘法测试失败"
        
        # 测试除法
        assert calc.divide(15, 3) == 5, "除法测试失败"
        
        # 测试除零异常
        try:
            calc.divide(10, 0)
            assert False, "除零异常测试失败"
        except ValueError:
            pass
        
        print("✓ 计算器模块测试通过")
    
    def test_string_utils():
        """测试字符串工具模块"""
        # 测试首字母大写
        assert StringUtils.capitalize_words("hello world") == "Hello World"
        
        # 测试反转字符串
        assert StringUtils.reverse_string("hello") == "olleh"
        
        # 测试单词计数
        assert StringUtils.count_words("hello world python") == 3
        
        # 测试回文检查
        assert StringUtils.is_palindrome("A man a plan a canal Panama") == True
        
        print("✓ 字符串工具模块测试通过")
    
    print("模块测试：")
    test_calculator()
    test_string_utils()
    print()
    
    print("模块使用总结：")
    print("1. 导入模块时优先使用 import module_name")
    print("2. 需要频繁使用时可以使用 from module import function")
    print("3. 避免使用 from module import *")
    print("4. 使用有意义的别名")
    print("5. 将相关功能组织在一个模块中")
    print("6. 编写文档字符串")
    print("7. 添加适当的测试")
    print("8. 遵循PEP 8命名规范")
    print()
    
    print("=== 函数模块详解演示完成 ===")


if __name__ == "__main__":
    main() 