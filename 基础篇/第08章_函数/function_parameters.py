#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第08章 函数 - 函数参数详解

本文件详细演示Python函数参数的各种类型和用法：
1. 位置参数（Positional Arguments）
2. 关键字参数（Keyword Arguments）
3. 默认参数（Default Parameters）
4. 可变位置参数（*args）
5. 可变关键字参数（**kwargs）
6. 参数解包
7. 参数验证
8. 实际应用示例
"""


def main():
    """主函数，演示函数参数的各种用法"""
    print("=" * 60)
    print("第08章 函数 - 函数参数详解")
    print("=" * 60)
    print()
    
    # 1. 位置参数
    print("1. 位置参数（Positional Arguments）")
    print("-" * 30)
    
    def greet_person(first_name, last_name):
        """使用位置参数问候用户"""
        print(f"Hello, {first_name} {last_name}!")
    
    print("位置参数示例：")
    greet_person("John", "Doe")
    greet_person("Alice", "Smith")
    
    # 位置参数的顺序很重要
    def subtract(a, b):
        """减法运算"""
        return a - b
    
    print(f"10 - 3 = {subtract(10, 3)}")
    print(f"3 - 10 = {subtract(3, 10)}")
    print()
    
    # 2. 关键字参数
    print("2. 关键字参数（Keyword Arguments）")
    print("-" * 30)
    
    def describe_pet(animal_type, pet_name, age=None):
        """描述宠物信息"""
        description = f"I have a {animal_type} named {pet_name}."
        if age is not None:
            description += f" It is {age} years old."
        print(description)
    
    print("关键字参数示例：")
    describe_pet("dog", "Max")
    describe_pet(pet_name="Whiskers", animal_type="cat")
    describe_pet(animal_type="bird", pet_name="Tweety", age=2)
    describe_pet(age=5, pet_name="Buddy", animal_type="dog")
    print()
    
    # 3. 默认参数
    print("3. 默认参数（Default Parameters）")
    print("-" * 30)
    
    def create_user_profile(name, age=25, city="Unknown", email=None):
        """创建用户资料"""
        profile = {
            'name': name,
            'age': age,
            'city': city,
            'email': email
        }
        return profile
    
    print("默认参数示例：")
    print(create_user_profile("Alice"))
    print(create_user_profile("Bob", 30))
    print(create_user_profile("Charlie", city="New York"))
    print(create_user_profile("Diana", 28, "Los Angeles", "diana@email.com"))
    print()
    
    # 4. 默认参数的陷阱
    print("4. 默认参数的陷阱")
    print("-" * 30)
    
    # 错误的方式：可变对象作为默认参数
    def append_to_list_wrong(item, target_list=[]):
        """错误的默认参数使用（会产生副作用）"""
        target_list.append(item)
        return target_list
    
    # 正确的方式：使用None作为默认值
    def append_to_list_correct(item, target_list=None):
        """正确的默认参数使用"""
        if target_list is None:
            target_list = []
        target_list.append(item)
        return target_list
    
    print("错误的默认参数使用：")
    print(append_to_list_wrong("apple"))
    print(append_to_list_wrong("banana"))  # 会包含之前的"apple"
    
    print("\n正确的默认参数使用：")
    print(append_to_list_correct("apple"))
    print(append_to_list_correct("banana"))  # 只包含"banana"
    print()
    
    # 5. 可变位置参数（*args）
    print("5. 可变位置参数（*args）")
    print("-" * 30)
    
    def calculate_sum(*numbers):
        """计算任意数量数字的和"""
        total = sum(numbers)
        print(f"计算 {numbers} 的和：{total}")
        return total
    
    def make_pizza(size, *toppings):
        """制作披萨，可以添加任意数量的配料"""
        print(f"制作一个{size}寸的披萨")
        if toppings:
            print("配料：")
            for topping in toppings:
                print(f"- {topping}")
        else:
            print("没有添加配料")
        print()
    
    print("可变位置参数示例：")
    calculate_sum(1, 2, 3)
    calculate_sum(1, 2, 3, 4, 5)
    
    make_pizza(12)
    make_pizza(16, "pepperoni")
    make_pizza(14, "mushrooms", "green peppers", "extra cheese")
    print()
    
    # 6. 可变关键字参数（**kwargs）
    print("6. 可变关键字参数（**kwargs）")
    print("-" * 30)
    
    def build_profile(first, last, **user_info):
        """构建用户资料字典"""
        profile = {'first_name': first, 'last_name': last}
        for key, value in user_info.items():
            profile[key] = value
        return profile
    
    def create_car(make, model, **options):
        """创建汽车信息"""
        car = {'make': make, 'model': model}
        for key, value in options.items():
            car[key] = value
        
        print(f"创建汽车：{make} {model}")
        if options:
            print("选配：")
            for key, value in options.items():
                print(f"- {key}: {value}")
        print()
        return car
    
    print("可变关键字参数示例：")
    user_profile = build_profile("Albert", "Einstein", 
                                location="Princeton", 
                                field="Physics",
                                age=76)
    print(user_profile)
    
    my_car = create_car("Toyota", "Camry", 
                       color="blue", 
                       year=2023, 
                       has_sunroof=True)
    print()
    
    # 7. 混合使用各种参数类型
    print("7. 混合使用各种参数类型")
    print("-" * 30)
    
    def complex_function(required_arg, default_arg="default", *args, **kwargs):
        """演示混合参数类型的函数"""
        print(f"必需参数：{required_arg}")
        print(f"默认参数：{default_arg}")
        if args:
            print(f"可变位置参数：{args}")
        if kwargs:
            print(f"可变关键字参数：{kwargs}")
        print()
    
    print("混合参数类型示例：")
    complex_function("必需值")
    complex_function("必需值", "自定义默认值")
    complex_function("必需值", "自定义默认值", "额外参数1", "额外参数2")
    complex_function("必需值", "自定义默认值", "额外参数", 
                    option1="值1", option2="值2")
    print()
    
    # 8. 参数解包
    print("8. 参数解包")
    print("-" * 30)
    
    def add_three_numbers(a, b, c):
        """加三个数字"""
        return a + b + c
    
    def display_user_info(name, age, city):
        """显示用户信息"""
        print(f"姓名：{name}, 年龄：{age}, 城市：{city}")
    
    # 使用列表/元组解包
    numbers = [1, 2, 3]
    print(f"解包列表：{add_three_numbers(*numbers)}")
    
    user_data = ("Alice", 25, "New York")
    print("解包元组：")
    display_user_info(*user_data)
    
    # 使用字典解包
    user_dict = {"name": "Bob", "age": 30, "city": "Los Angeles"}
    print("解包字典：")
    display_user_info(**user_dict)
    print()
    
    # 9. 参数验证
    print("9. 参数验证")
    print("-" * 30)
    
    def validate_age(age):
        """验证年龄"""
        if not isinstance(age, int):
            raise TypeError("年龄必须是整数")
        if age < 0:
            raise ValueError("年龄不能为负数")
        if age > 150:
            raise ValueError("年龄不能超过150岁")
        return True
    
    def create_person(name, age, email=None):
        """创建人员信息（带参数验证）"""
        # 验证姓名
        if not isinstance(name, str) or not name.strip():
            raise ValueError("姓名必须是非空字符串")
        
        # 验证年龄
        validate_age(age)
        
        # 验证邮箱
        if email is not None and "@" not in email:
            raise ValueError("邮箱格式不正确")
        
        return {
            'name': name.strip(),
            'age': age,
            'email': email
        }
    
    print("参数验证示例：")
    try:
        person1 = create_person("Alice", 25, "alice@example.com")
        print(f"创建成功：{person1}")
        
        person2 = create_person("Bob", 30)
        print(f"创建成功：{person2}")
        
        # 测试错误情况
        person3 = create_person("", 25)  # 空姓名
    except ValueError as e:
        print(f"验证错误：{e}")
    
    try:
        person4 = create_person("Charlie", -5)  # 负年龄
    except ValueError as e:
        print(f"验证错误：{e}")
    print()
    
    # 10. 函数装饰器中的参数处理
    print("10. 函数装饰器中的参数处理")
    print("-" * 30)
    
    def log_function_call(func):
        """记录函数调用的装饰器"""
        def wrapper(*args, **kwargs):
            print(f"调用函数：{func.__name__}")
            print(f"位置参数：{args}")
            print(f"关键字参数：{kwargs}")
            result = func(*args, **kwargs)
            print(f"返回值：{result}")
            print()
            return result
        return wrapper
    
    @log_function_call
    def multiply(x, y):
        """乘法运算"""
        return x * y
    
    @log_function_call
    def greet(name, greeting="Hello"):
        """问候函数"""
        return f"{greeting}, {name}!"
    
    print("装饰器中的参数处理：")
    multiply(3, 4)
    greet("Alice")
    greet("Bob", greeting="Hi")
    
    # 11. 实际应用：数据处理函数
    print("11. 实际应用：数据处理函数")
    print("-" * 30)
    
    def process_student_data(name, *grades, **info):
        """处理学生数据"""
        if not grades:
            average = 0
        else:
            average = sum(grades) / len(grades)
        
        student = {
            'name': name,
            'grades': grades,
            'average': average,
            'grade_count': len(grades)
        }
        
        # 添加额外信息
        for key, value in info.items():
            student[key] = value
        
        return student
    
    def generate_report(*students, format_type="simple"):
        """生成学生报告"""
        print(f"学生报告（{format_type}格式）")
        print("-" * 40)
        
        for student in students:
            if format_type == "simple":
                print(f"{student['name']}: 平均分 {student['average']:.2f}")
            elif format_type == "detailed":
                print(f"姓名：{student['name']}")
                print(f"成绩：{student['grades']}")
                print(f"平均分：{student['average']:.2f}")
                print(f"成绩数量：{student['grade_count']}")
                # 显示额外信息
                for key, value in student.items():
                    if key not in ['name', 'grades', 'average', 'grade_count']:
                        print(f"{key}：{value}")
                print()
    
    # 创建学生数据
    student1 = process_student_data("Alice", 85, 92, 78, 88, 
                                   class_="10A", age=16)
    student2 = process_student_data("Bob", 76, 82, 85, 79, 90,
                                   class_="10B", age=17)
    student3 = process_student_data("Charlie", 94, 87, 91,
                                   class_="10A", age=16)
    
    # 生成报告
    generate_report(student1, student2, student3)
    generate_report(student1, student2, student3, format_type="detailed")
    
    # 12. 参数类型提示
    print("12. 参数类型提示")
    print("-" * 30)
    
    from typing import List, Dict, Optional, Union
    
    def calculate_statistics(numbers: List[Union[int, float]]) -> Dict[str, float]:
        """计算数字列表的统计信息"""
        if not numbers:
            return {'count': 0, 'sum': 0, 'average': 0, 'min': 0, 'max': 0}
        
        return {
            'count': len(numbers),
            'sum': sum(numbers),
            'average': sum(numbers) / len(numbers),
            'min': min(numbers),
            'max': max(numbers)
        }
    
    def format_user_name(first_name: str, last_name: str, 
                        middle_name: Optional[str] = None) -> str:
        """格式化用户姓名"""
        if middle_name:
            return f"{first_name} {middle_name} {last_name}"
        return f"{first_name} {last_name}"
    
    print("类型提示示例：")
    stats = calculate_statistics([1, 2, 3, 4, 5])
    print(f"统计信息：{stats}")
    
    name1 = format_user_name("John", "Doe")
    name2 = format_user_name("Jane", "Smith", "Marie")
    print(f"格式化姓名：{name1}, {name2}")
    print()
    
    # 13. 参数最佳实践
    print("13. 参数最佳实践")
    print("-" * 30)
    
    def good_function_design(required_param: str, 
                           optional_param: str = "default",
                           *args: int,
                           **kwargs: str) -> Dict:
        """展示好的函数设计原则"""
        # 1. 参数顺序：必需参数 -> 默认参数 -> *args -> **kwargs
        # 2. 使用类型提示
        # 3. 适当的默认值
        # 4. 清晰的参数名
        
        result = {
            'required': required_param,
            'optional': optional_param,
            'args': args,
            'kwargs': kwargs
        }
        
        # 参数验证
        if not required_param:
            raise ValueError("必需参数不能为空")
        
        return result
    
    print("函数设计最佳实践：")
    print("1. 参数顺序：必需参数 -> 默认参数 -> *args -> **kwargs")
    print("2. 使用描述性的参数名")
    print("3. 为参数提供类型提示")
    print("4. 验证参数的有效性")
    print("5. 使用None作为可变对象的默认值")
    print("6. 限制参数数量（通常不超过5个）")
    print("7. 使用关键字参数提高可读性")
    print("8. 文档化参数的含义和类型")
    print()
    
    print("=== 函数参数详解演示完成 ===")


if __name__ == "__main__":
    main() 