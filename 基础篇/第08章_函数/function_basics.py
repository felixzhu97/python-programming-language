#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第08章 函数 - 函数基础知识

本文件演示Python函数的基础知识，包括：
1. 函数定义和调用
2. 函数参数
3. 函数作用域
4. 文档字符串
5. 函数命名规范
6. 实际应用示例

函数是组织代码的重要方式，能够提高代码的复用性和可维护性。
"""


def main():
    """主函数，演示函数基础知识"""
    print("=" * 60)
    print("第08章 函数 - 函数基础知识")
    print("=" * 60)
    print()
    
    # 1. 函数定义和调用
    print("1. 函数定义和调用")
    print("-" * 30)
    
    # 定义一个简单的函数
    def greet_user():
        """向用户显示简单的问候语"""
        print("Hello!")
    
    # 调用函数
    print("调用greet_user()函数：")
    greet_user()
    print()
    
    # 定义一个带参数的函数
    def greet_user_with_name(username):
        """向用户显示个性化的问候语"""
        print(f"Hello, {username}!")
    
    # 调用带参数的函数
    print("调用greet_user_with_name()函数：")
    greet_user_with_name("Alice")
    greet_user_with_name("Bob")
    print()
    
    # 2. 函数参数详解
    print("2. 函数参数详解")
    print("-" * 30)
    
    # 位置参数
    def describe_pet(animal_type, pet_name):
        """显示宠物的信息"""
        print(f"I have a {animal_type}.")
        print(f"My {animal_type}'s name is {pet_name}.")
    
    print("使用位置参数：")
    describe_pet("hamster", "Harry")
    describe_pet("dog", "Willie")
    print()
    
    # 关键字参数
    print("使用关键字参数：")
    describe_pet(animal_type="hamster", pet_name="Harry")
    describe_pet(pet_name="Willie", animal_type="dog")
    print()
    
    # 3. 默认参数值
    print("3. 默认参数值")
    print("-" * 30)
    
    def describe_pet_with_default(pet_name, animal_type="dog"):
        """显示宠物的信息，默认为狗"""
        print(f"I have a {animal_type}.")
        print(f"My {animal_type}'s name is {pet_name}.")
    
    print("使用默认参数值：")
    describe_pet_with_default("Willie")  # 使用默认值
    describe_pet_with_default("Harry", "hamster")  # 覆盖默认值
    describe_pet_with_default(pet_name="Max")  # 使用关键字参数
    describe_pet_with_default(animal_type="cat", pet_name="Whiskers")
    print()
    
    # 4. 避免参数错误的技巧
    print("4. 避免参数错误的技巧")
    print("-" * 30)
    
    def safe_describe_pet(pet_name, animal_type="dog"):
        """安全地显示宠物信息，包含参数验证"""
        # 参数验证
        if not pet_name:
            print("错误：宠物名称不能为空")
            return
        
        if not animal_type:
            print("错误：动物类型不能为空")
            return
        
        # 标准化输入
        pet_name = pet_name.strip().title()
        animal_type = animal_type.strip().lower()
        
        print(f"I have a {animal_type}.")
        print(f"My {animal_type}'s name is {pet_name}.")
    
    print("带参数验证的函数：")
    safe_describe_pet("max", "Cat")
    safe_describe_pet("", "dog")  # 空名称
    safe_describe_pet("Buddy")  # 使用默认类型
    print()
    
    # 5. 函数作用域
    print("5. 函数作用域")
    print("-" * 30)
    
    # 全局变量
    global_var = "这是全局变量"
    
    def demonstrate_scope():
        """演示变量作用域"""
        # 局部变量
        local_var = "这是局部变量"
        
        print(f"函数内部访问全局变量：{global_var}")
        print(f"函数内部访问局部变量：{local_var}")
    
    print("作用域演示：")
    demonstrate_scope()
    print(f"函数外部访问全局变量：{global_var}")
    # print(f"函数外部访问局部变量：{local_var}")  # 这会出错
    print()
    
    # 6. 修改全局变量
    print("6. 修改全局变量")
    print("-" * 30)
    
    counter = 0
    
    def increment_counter():
        """使用global关键字修改全局变量"""
        global counter
        counter += 1
        print(f"计数器值：{counter}")
    
    print("修改全局变量：")
    print(f"初始值：{counter}")
    increment_counter()
    increment_counter()
    print(f"最终值：{counter}")
    print()
    
    # 7. 函数文档字符串
    print("7. 函数文档字符串")
    print("-" * 30)
    
    def calculate_area(length, width):
        """
        计算矩形的面积
        
        参数：
        length (float): 矩形的长度
        width (float): 矩形的宽度
        
        返回：
        float: 矩形的面积
        
        示例：
        >>> calculate_area(5, 3)
        15
        """
        return length * width
    
    print("带文档字符串的函数：")
    area = calculate_area(5, 3)
    print(f"面积：{area}")
    print(f"函数文档：{calculate_area.__doc__}")
    print()
    
    # 8. 函数命名规范
    print("8. 函数命名规范")
    print("-" * 30)
    
    def get_user_name():
        """获取用户名称（动词开头）"""
        return "John Doe"
    
    def is_valid_email(email):
        """检查邮箱是否有效（布尔函数用is开头）"""
        return "@" in email and "." in email
    
    def calculate_total_price(price, tax_rate):
        """计算总价格（动词开头，描述性）"""
        return price * (1 + tax_rate)
    
    print("函数命名规范示例：")
    print(f"用户名：{get_user_name()}")
    print(f"邮箱有效性：{is_valid_email('test@example.com')}")
    print(f"总价格：{calculate_total_price(100, 0.08)}")
    print()
    
    # 9. 实际应用示例
    print("9. 实际应用示例")
    print("-" * 30)
    
    def format_name(first_name, last_name, middle_name=""):
        """格式化姓名"""
        if middle_name:
            full_name = f"{first_name} {middle_name} {last_name}"
        else:
            full_name = f"{first_name} {last_name}"
        return full_name.title()
    
    def calculate_age(birth_year, current_year=2024):
        """计算年龄"""
        return current_year - birth_year
    
    def validate_password(password):
        """验证密码强度"""
        if len(password) < 8:
            return False, "密码长度至少8位"
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        
        if not (has_upper and has_lower and has_digit):
            return False, "密码必须包含大小写字母和数字"
        
        return True, "密码强度合格"
    
    print("实际应用示例：")
    print(f"格式化姓名：{format_name('john', 'doe')}")
    print(f"格式化姓名（带中间名）：{format_name('john', 'doe', 'smith')}")
    print(f"计算年龄：{calculate_age(1990)}")
    
    is_valid, message = validate_password("Abc123")
    print(f"密码验证：{is_valid}, {message}")
    
    is_valid, message = validate_password("SecurePass123")
    print(f"密码验证：{is_valid}, {message}")
    print()
    
    # 10. 函数调用的最佳实践
    print("10. 函数调用的最佳实践")
    print("-" * 30)
    
    def process_order(customer_name, items, discount=0.0, tax_rate=0.08, delivery=False):
        """处理订单的复杂函数"""
        subtotal = sum(item['price'] * item['quantity'] for item in items)
        
        # 应用折扣
        discounted_total = subtotal * (1 - discount)
        
        # 计算税费
        tax = discounted_total * tax_rate
        
        # 计算总价
        total = discounted_total + tax
        
        # 配送费
        if delivery:
            total += 5.99
        
        return {
            'customer': customer_name,
            'subtotal': subtotal,
            'discount': discount,
            'tax': tax,
            'delivery_fee': 5.99 if delivery else 0,
            'total': total
        }
    
    # 示例订单
    items = [
        {'name': 'T-shirt', 'price': 19.99, 'quantity': 2},
        {'name': 'Jeans', 'price': 49.99, 'quantity': 1}
    ]
    
    # 使用关键字参数提高可读性
    order = process_order(
        customer_name="Alice Johnson",
        items=items,
        discount=0.1,  # 10% 折扣
        delivery=True
    )
    
    print("订单处理示例：")
    for key, value in order.items():
        print(f"{key}: {value}")
    print()
    
    # 11. 函数的错误处理
    print("11. 函数的错误处理")
    print("-" * 30)
    
    def safe_divide(dividend, divisor):
        """安全的除法运算"""
        try:
            if divisor == 0:
                return None, "除数不能为零"
            
            result = dividend / divisor
            return result, "计算成功"
        
        except TypeError:
            return None, "参数必须是数字"
        except Exception as e:
            return None, f"未知错误：{e}"
    
    # 测试错误处理
    test_cases = [
        (10, 2),
        (10, 0),
        ("10", 2),
        (10, "2")
    ]
    
    print("错误处理示例：")
    for dividend, divisor in test_cases:
        result, message = safe_divide(dividend, divisor)
        print(f"{dividend} ÷ {divisor} = {result} ({message})")
    print()
    
    # 12. 函数性能考虑
    print("12. 函数性能考虑")
    print("-" * 30)
    
    import time
    
    def slow_function(n):
        """模拟慢速函数"""
        time.sleep(0.001)  # 模拟耗时操作
        return n * n
    
    def fast_function(n):
        """快速函数"""
        return n * n
    
    # 性能测试
    start_time = time.time()
    for i in range(100):
        slow_function(i)
    slow_time = time.time() - start_time
    
    start_time = time.time()
    for i in range(100):
        fast_function(i)
    fast_time = time.time() - start_time
    
    print(f"慢速函数耗时：{slow_time:.4f}秒")
    print(f"快速函数耗时：{fast_time:.4f}秒")
    print(f"性能差异：{slow_time/fast_time:.2f}倍")
    print()
    
    # 13. 函数设计原则
    print("13. 函数设计原则")
    print("-" * 30)
    
    def good_function_example():
        """好的函数设计示例"""
        # 1. 单一职责原则
        def calculate_tax(price, tax_rate):
            """只负责计算税费"""
            return price * tax_rate
        
        def format_currency(amount):
            """只负责格式化货币"""
            return f"${amount:.2f}"
        
        # 2. 函数组合
        def display_price_with_tax(price, tax_rate):
            """组合使用多个函数"""
            tax = calculate_tax(price, tax_rate)
            total = price + tax
            return f"原价：{format_currency(price)}, 税费：{format_currency(tax)}, 总价：{format_currency(total)}"
        
        return display_price_with_tax(100, 0.08)
    
    print("函数设计原则示例：")
    print(good_function_example())
    print()
    
    print("函数设计原则总结：")
    print("1. 单一职责原则：每个函数只做一件事")
    print("2. 函数名称应该清晰描述功能")
    print("3. 参数数量应该适中（建议不超过5个）")
    print("4. 避免副作用：不要修改全局状态")
    print("5. 返回值应该一致且可预测")
    print("6. 添加适当的文档字符串")
    print("7. 处理边界情况和错误")
    print("8. 保持函数简短（一般不超过20行）")
    print()
    
    print("=== 函数基础知识演示完成 ===")


if __name__ == "__main__":
    main() 