#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第08章 函数 - 函数返回值详解

本文件详细演示Python函数返回值的各种用法：
1. 基本返回值
2. 返回不同类型的值
3. 返回多个值
4. 条件返回
5. 提前返回
6. 返回函数
7. 返回复杂数据结构
8. 返回值的处理和验证
"""


def main():
    """主函数，演示函数返回值的各种用法"""
    print("=" * 60)
    print("第08章 函数 - 函数返回值详解")
    print("=" * 60)
    print()
    
    # 1. 基本返回值
    print("1. 基本返回值")
    print("-" * 30)
    
    def add_numbers(a, b):
        """返回两个数的和"""
        return a + b
    
    def get_greeting(name):
        """返回问候语"""
        return f"Hello, {name}!"
    
    def is_even(number):
        """检查数字是否为偶数"""
        return number % 2 == 0
    
    print("基本返回值示例：")
    print(f"3 + 5 = {add_numbers(3, 5)}")
    print(f"问候语：{get_greeting('Alice')}")
    print(f"8是偶数吗？{is_even(8)}")
    print(f"7是偶数吗？{is_even(7)}")
    print()
    
    # 2. 返回不同类型的值
    print("2. 返回不同类型的值")
    print("-" * 30)
    
    def get_user_info(user_id):
        """根据用户ID返回用户信息"""
        users = {
            1: {"name": "Alice", "age": 25, "email": "alice@example.com"},
            2: {"name": "Bob", "age": 30, "email": "bob@example.com"},
            3: {"name": "Charlie", "age": 35, "email": "charlie@example.com"}
        }
        return users.get(user_id, {})
    
    def calculate_circle_properties(radius):
        """计算圆的属性，返回字典"""
        import math
        return {
            'radius': radius,
            'diameter': 2 * radius,
            'circumference': 2 * math.pi * radius,
            'area': math.pi * radius ** 2
        }
    
    def get_prime_numbers(limit):
        """获取指定范围内的质数，返回列表"""
        primes = []
        for num in range(2, limit + 1):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        return primes
    
    print("返回不同类型的值：")
    print(f"用户信息：{get_user_info(1)}")
    print(f"圆的属性：{calculate_circle_properties(5)}")
    print(f"20以内的质数：{get_prime_numbers(20)}")
    print()
    
    # 3. 返回多个值
    print("3. 返回多个值")
    print("-" * 30)
    
    def get_name_parts(full_name):
        """分解全名，返回姓和名"""
        parts = full_name.split()
        if len(parts) >= 2:
            return parts[0], parts[-1]  # 返回元组
        return parts[0], ""
    
    def calculate_rectangle_properties(length, width):
        """计算矩形的周长和面积"""
        perimeter = 2 * (length + width)
        area = length * width
        return perimeter, area
    
    def divide_with_remainder(dividend, divisor):
        """除法运算，返回商和余数"""
        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder
    
    def get_min_max_avg(numbers):
        """返回列表的最小值、最大值和平均值"""
        if not numbers:
            return None, None, None
        return min(numbers), max(numbers), sum(numbers) / len(numbers)
    
    print("返回多个值示例：")
    first_name, last_name = get_name_parts("John Doe")
    print(f"姓：{first_name}, 名：{last_name}")
    
    perimeter, area = calculate_rectangle_properties(5, 3)
    print(f"矩形周长：{perimeter}, 面积：{area}")
    
    quotient, remainder = divide_with_remainder(17, 5)
    print(f"17 ÷ 5 = {quotient} 余 {remainder}")
    
    numbers = [1, 5, 3, 9, 2, 8]
    min_val, max_val, avg_val = get_min_max_avg(numbers)
    print(f"最小值：{min_val}, 最大值：{max_val}, 平均值：{avg_val:.2f}")
    print()
    
    # 4. 条件返回
    print("4. 条件返回")
    print("-" * 30)
    
    def get_grade_letter(score):
        """根据分数返回等级"""
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
    
    def validate_email(email):
        """验证邮箱格式"""
        if not email or '@' not in email:
            return False, "邮箱格式不正确"
        
        local, domain = email.split('@', 1)
        if not local or not domain:
            return False, "邮箱格式不正确"
        
        if '.' not in domain:
            return False, "域名格式不正确"
        
        return True, "邮箱格式正确"
    
    def calculate_discount(price, customer_type):
        """根据客户类型计算折扣"""
        if customer_type == 'vip':
            return price * 0.8, "VIP客户享受8折"
        elif customer_type == 'member':
            return price * 0.9, "会员客户享受9折"
        else:
            return price, "普通客户无折扣"
    
    print("条件返回示例：")
    scores = [95, 87, 76, 63, 42]
    for score in scores:
        print(f"分数 {score} 对应等级：{get_grade_letter(score)}")
    
    emails = ["test@example.com", "invalid-email", "user@domain.com"]
    for email in emails:
        is_valid, message = validate_email(email)
        print(f"{email}: {is_valid} - {message}")
    
    customers = [("vip", 100), ("member", 100), ("regular", 100)]
    for customer_type, price in customers:
        final_price, message = calculate_discount(price, customer_type)
        print(f"{customer_type} 客户：{message}，最终价格：{final_price}")
    print()
    
    # 5. 提前返回
    print("5. 提前返回")
    print("-" * 30)
    
    def find_first_negative(numbers):
        """查找第一个负数"""
        for i, num in enumerate(numbers):
            if num < 0:
                return i, num  # 找到后立即返回
        return None, None  # 没找到
    
    def process_user_data(user_data):
        """处理用户数据，验证失败时提前返回"""
        # 检查必需字段
        if not user_data.get('name'):
            return None, "姓名不能为空"
        
        if not user_data.get('email'):
            return None, "邮箱不能为空"
        
        # 验证邮箱格式
        email = user_data['email']
        if '@' not in email:
            return None, "邮箱格式不正确"
        
        # 验证年龄
        age = user_data.get('age', 0)
        if age < 0 or age > 150:
            return None, "年龄不合理"
        
        # 所有验证通过
        processed_data = {
            'name': user_data['name'].strip().title(),
            'email': email.lower(),
            'age': age
        }
        return processed_data, "处理成功"
    
    def factorial(n):
        """计算阶乘，使用提前返回处理边界情况"""
        if n < 0:
            return None  # 负数没有阶乘
        if n == 0 or n == 1:
            return 1  # 0! = 1! = 1
        
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    print("提前返回示例：")
    numbers = [1, 2, 3, -4, 5, -6]
    index, value = find_first_negative(numbers)
    print(f"第一个负数在索引 {index}，值为 {value}")
    
    test_users = [
        {"name": "Alice", "email": "alice@example.com", "age": 25},
        {"name": "", "email": "bob@example.com", "age": 30},
        {"name": "Charlie", "email": "invalid-email", "age": 35},
        {"name": "Diana", "email": "diana@example.com", "age": -5}
    ]
    
    for user in test_users:
        result, message = process_user_data(user)
        print(f"处理结果：{message}")
        if result:
            print(f"  数据：{result}")
    
    print(f"5的阶乘：{factorial(5)}")
    print(f"-3的阶乘：{factorial(-3)}")
    print()
    
    # 6. 返回函数
    print("6. 返回函数")
    print("-" * 30)
    
    def create_multiplier(factor):
        """创建乘法函数"""
        def multiplier(x):
            return x * factor
        return multiplier
    
    def get_operation(operation_name):
        """根据名称返回相应的运算函数"""
        operations = {
            'add': lambda x, y: x + y,
            'subtract': lambda x, y: x - y,
            'multiply': lambda x, y: x * y,
            'divide': lambda x, y: x / y if y != 0 else None
        }
        return operations.get(operation_name)
    
    def create_validator(min_val, max_val):
        """创建验证函数"""
        def validator(value):
            return min_val <= value <= max_val
        return validator
    
    print("返回函数示例：")
    double = create_multiplier(2)
    triple = create_multiplier(3)
    print(f"double(5) = {double(5)}")
    print(f"triple(4) = {triple(4)}")
    
    add_func = get_operation('add')
    multiply_func = get_operation('multiply')
    print(f"add_func(3, 4) = {add_func(3, 4)}")
    print(f"multiply_func(3, 4) = {multiply_func(3, 4)}")
    
    age_validator = create_validator(0, 150)
    print(f"age_validator(25) = {age_validator(25)}")
    print(f"age_validator(200) = {age_validator(200)}")
    print()
    
    # 7. 返回复杂数据结构
    print("7. 返回复杂数据结构")
    print("-" * 30)
    
    def analyze_text(text):
        """分析文本，返回详细统计信息"""
        words = text.split()
        word_count = {}
        
        for word in words:
            word = word.lower().strip('.,!?;:"')
            word_count[word] = word_count.get(word, 0) + 1
        
        return {
            'total_chars': len(text),
            'total_words': len(words),
            'unique_words': len(word_count),
            'word_frequency': word_count,
            'average_word_length': sum(len(word) for word in words) / len(words) if words else 0
        }
    
    def get_student_report(students):
        """生成学生报告"""
        if not students:
            return {'error': '没有学生数据'}
        
        total_students = len(students)
        all_grades = []
        
        for student in students:
            all_grades.extend(student.get('grades', []))
        
        if not all_grades:
            return {'error': '没有成绩数据'}
        
        class_stats = {
            'total_students': total_students,
            'total_grades': len(all_grades),
            'average_grade': sum(all_grades) / len(all_grades),
            'highest_grade': max(all_grades),
            'lowest_grade': min(all_grades),
            'students': []
        }
        
        for student in students:
            grades = student.get('grades', [])
            if grades:
                student_avg = sum(grades) / len(grades)
                class_stats['students'].append({
                    'name': student['name'],
                    'average': student_avg,
                    'grade_count': len(grades),
                    'highest': max(grades),
                    'lowest': min(grades)
                })
        
        return class_stats
    
    print("返回复杂数据结构示例：")
    text = "Python is great. Python is powerful. Programming with Python is fun."
    analysis = analyze_text(text)
    print("文本分析结果：")
    for key, value in analysis.items():
        if key == 'word_frequency':
            print(f"  {key}: {dict(list(value.items())[:5])}...")  # 只显示前5个
        else:
            print(f"  {key}: {value}")
    
    students = [
        {'name': 'Alice', 'grades': [85, 92, 78, 88]},
        {'name': 'Bob', 'grades': [76, 82, 85, 79, 90]},
        {'name': 'Charlie', 'grades': [94, 87, 91]}
    ]
    
    report = get_student_report(students)
    print("\n学生报告：")
    print(f"总学生数：{report['total_students']}")
    print(f"班级平均分：{report['average_grade']:.2f}")
    print(f"最高分：{report['highest_grade']}")
    print(f"最低分：{report['lowest_grade']}")
    print()
    
    # 8. 返回值的处理和验证
    print("8. 返回值的处理和验证")
    print("-" * 30)
    
    def safe_divide(a, b):
        """安全除法，返回结果和状态"""
        if b == 0:
            return None, False, "除数不能为零"
        
        try:
            result = a / b
            return result, True, "计算成功"
        except Exception as e:
            return None, False, f"计算错误：{e}"
    
    def fetch_user_data(user_id):
        """模拟获取用户数据"""
        # 模拟数据库查询
        users = {
            1: {"name": "Alice", "email": "alice@example.com", "active": True},
            2: {"name": "Bob", "email": "bob@example.com", "active": False},
            3: {"name": "Charlie", "email": "charlie@example.com", "active": True}
        }
        
        if user_id in users:
            return users[user_id], True, "用户找到"
        else:
            return None, False, "用户不存在"
    
    def process_api_response(response_data):
        """处理API响应"""
        if not response_data:
            return None, "响应数据为空"
        
        if 'error' in response_data:
            return None, f"API错误：{response_data['error']}"
        
        if 'data' not in response_data:
            return None, "响应中缺少数据字段"
        
        return response_data['data'], "处理成功"
    
    print("返回值处理示例：")
    
    # 处理可能失败的操作
    test_cases = [(10, 2), (10, 0), (15, 3)]
    for a, b in test_cases:
        result, success, message = safe_divide(a, b)
        if success:
            print(f"{a} ÷ {b} = {result}")
        else:
            print(f"{a} ÷ {b}: {message}")
    
    # 处理用户数据查询
    user_ids = [1, 2, 4]
    for user_id in user_ids:
        user_data, found, message = fetch_user_data(user_id)
        print(f"用户 {user_id}: {message}")
        if found:
            print(f"  姓名：{user_data['name']}")
            print(f"  状态：{'活跃' if user_data['active'] else '非活跃'}")
    print()
    
    # 9. 返回值的最佳实践
    print("9. 返回值的最佳实践")
    print("-" * 30)
    
    def good_function_example():
        """展示返回值的最佳实践"""
        
        # 1. 一致的返回类型
        def get_user_age(user_id):
            """返回用户年龄，失败时返回None"""
            users = {1: 25, 2: 30, 3: 35}
            return users.get(user_id)  # 始终返回int或None
        
        # 2. 有意义的返回值
        def validate_password(password):
            """验证密码，返回详细信息"""
            if len(password) < 8:
                return False, "密码长度不足8位"
            if not any(c.isupper() for c in password):
                return False, "密码需包含大写字母"
            if not any(c.islower() for c in password):
                return False, "密码需包含小写字母"
            if not any(c.isdigit() for c in password):
                return False, "密码需包含数字"
            return True, "密码强度合格"
        
        # 3. 避免返回None，使用默认值
        def get_user_preferences(user_id):
            """获取用户偏好设置"""
            preferences = {
                1: {"theme": "dark", "language": "en"},
                2: {"theme": "light", "language": "zh"}
            }
            return preferences.get(user_id, {"theme": "light", "language": "en"})
        
        return get_user_age, validate_password, get_user_preferences
    
    get_age, validate_pwd, get_prefs = good_function_example()
    
    print("返回值最佳实践示例：")
    print(f"用户1年龄：{get_age(1)}")
    print(f"用户5年龄：{get_age(5)}")
    
    passwords = ["123", "Password123", "password", "Pass123"]
    for pwd in passwords:
        is_valid, message = validate_pwd(pwd)
        print(f"'{pwd}': {is_valid} - {message}")
    
    print(f"用户1偏好：{get_prefs(1)}")
    print(f"用户5偏好：{get_prefs(5)}")
    print()
    
    print("返回值最佳实践总结：")
    print("1. 保持返回类型的一致性")
    print("2. 返回有意义的值")
    print("3. 使用元组返回多个相关值")
    print("4. 考虑使用命名元组或数据类")
    print("5. 避免返回None，考虑使用默认值")
    print("6. 提供状态信息和错误消息")
    print("7. 文档化返回值的含义")
    print("8. 使用类型提示明确返回类型")
    print()
    
    print("=== 函数返回值详解演示完成 ===")


if __name__ == "__main__":
    main() 