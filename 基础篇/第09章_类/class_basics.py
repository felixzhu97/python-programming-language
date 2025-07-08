#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第09章 类 - 类的基础知识

本文件演示Python类的基础知识，包括：
1. 类的定义和实例化
2. 属性和方法
3. __init__方法
4. 类的命名规范
5. 类的文档字符串
6. 实例的创建和使用
7. 类和实例的关系
8. 简单的类设计示例

类是面向对象编程的核心概念，它们允许我们对现实世界中的事物进行建模。
"""


def main():
    """主函数，演示类的基础知识"""
    print("=" * 60)
    print("第09章 类 - 类的基础知识")
    print("=" * 60)
    print()
    
    # 1. 最简单的类
    print("1. 最简单的类")
    print("-" * 30)
    
    class Dog:
        """一个简单的狗类"""
        pass
    
    # 创建实例
    my_dog = Dog()
    print(f"创建了一个Dog实例：{my_dog}")
    print(f"实例类型：{type(my_dog)}")
    print()
    
    # 2. 添加属性和方法
    print("2. 添加属性和方法")
    print("-" * 30)
    
    class Dog:
        """一个表示狗的简单类"""
        
        def __init__(self, name, age):
            """初始化狗的属性"""
            self.name = name
            self.age = age
        
        def sit(self):
            """模拟狗蹲下"""
            print(f"{self.name} is now sitting.")
        
        def roll_over(self):
            """模拟狗打滚"""
            print(f"{self.name} rolled over!")
    
    # 创建实例
    my_dog = Dog("Willie", 6)
    print(f"我的狗叫 {my_dog.name}")
    print(f"我的狗 {my_dog.age} 岁了")
    
    # 调用方法
    my_dog.sit()
    my_dog.roll_over()
    print()
    
    # 3. 创建多个实例
    print("3. 创建多个实例")
    print("-" * 30)
    
    my_dog = Dog("Willie", 6)
    your_dog = Dog("Lucy", 3)
    
    print(f"我的狗叫 {my_dog.name}，{my_dog.age} 岁了")
    print(f"你的狗叫 {your_dog.name}，{your_dog.age} 岁了")
    
    print("\n让它们表演：")
    my_dog.sit()
    your_dog.roll_over()
    print()
    
    # 4. 修改属性值
    print("4. 修改属性值")
    print("-" * 30)
    
    class Car:
        """一个简单的汽车类"""
        
        def __init__(self, make, model, year):
            """初始化汽车属性"""
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0  # 里程表读数
        
        def get_descriptive_name(self):
            """返回汽车的描述性名称"""
            long_name = f"{self.year} {self.make} {self.model}"
            return long_name.title()
        
        def read_odometer(self):
            """打印汽车的里程"""
            print(f"This car has {self.odometer_reading} miles on it.")
        
        def update_odometer(self, mileage):
            """设置里程表读数"""
            if mileage >= self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("You can't roll back an odometer!")
        
        def increment_odometer(self, miles):
            """增加里程表读数"""
            self.odometer_reading += miles
    
    # 创建汽车实例
    my_new_car = Car('audi', 'a4', 2019)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()
    
    # 直接修改属性
    print("\n直接修改属性：")
    my_new_car.odometer_reading = 23
    my_new_car.read_odometer()
    
    # 通过方法修改属性
    print("\n通过方法修改属性：")
    my_new_car.update_odometer(23500)
    my_new_car.read_odometer()
    
    # 增加属性值
    print("\n增加属性值：")
    my_new_car.increment_odometer(100)
    my_new_car.read_odometer()
    
    # 尝试回滚里程表
    print("\n尝试回滚里程表：")
    my_new_car.update_odometer(20000)
    my_new_car.read_odometer()
    print()
    
    # 5. 更复杂的类示例
    print("5. 更复杂的类示例")
    print("-" * 30)
    
    class Restaurant:
        """一个表示餐厅的类"""
        
        def __init__(self, restaurant_name, cuisine_type):
            """初始化餐厅属性"""
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.number_served = 0
            self.is_open = False
            self.menu = []
        
        def describe_restaurant(self):
            """描述餐厅"""
            print(f"餐厅名称：{self.restaurant_name}")
            print(f"菜系类型：{self.cuisine_type}")
            print(f"已服务顾客数：{self.number_served}")
            print(f"营业状态：{'营业中' if self.is_open else '已关闭'}")
        
        def open_restaurant(self):
            """开门营业"""
            self.is_open = True
            print(f"{self.restaurant_name} 现在开门营业！")
        
        def close_restaurant(self):
            """关门停业"""
            self.is_open = False
            print(f"{self.restaurant_name} 现在关门停业！")
        
        def set_number_served(self, number):
            """设置已服务的顾客数"""
            if number >= 0:
                self.number_served = number
            else:
                print("服务顾客数不能为负数！")
        
        def increment_number_served(self, increment):
            """增加已服务的顾客数"""
            if increment >= 0:
                self.number_served += increment
            else:
                print("增加的顾客数不能为负数！")
        
        def add_to_menu(self, dish):
            """添加菜品到菜单"""
            self.menu.append(dish)
            print(f"已将 '{dish}' 添加到菜单")
        
        def display_menu(self):
            """显示菜单"""
            if self.menu:
                print(f"\n{self.restaurant_name} 的菜单：")
                for i, dish in enumerate(self.menu, 1):
                    print(f"{i}. {dish}")
            else:
                print("菜单为空")
    
    # 创建餐厅实例
    restaurant = Restaurant("Golden Dragon", "中式料理")
    
    print("餐厅信息：")
    restaurant.describe_restaurant()
    
    print("\n餐厅操作：")
    restaurant.open_restaurant()
    restaurant.set_number_served(50)
    restaurant.increment_number_served(10)
    
    # 添加菜品
    dishes = ["宫保鸡丁", "麻婆豆腐", "鱼香肉丝", "糖醋排骨"]
    for dish in dishes:
        restaurant.add_to_menu(dish)
    
    restaurant.display_menu()
    
    print("\n更新后的餐厅信息：")
    restaurant.describe_restaurant()
    print()
    
    # 6. 类的属性和方法的访问
    print("6. 类的属性和方法的访问")
    print("-" * 30)
    
    class Person:
        """一个表示人的类"""
        
        def __init__(self, name, age, email):
            """初始化人的属性"""
            self.name = name
            self.age = age
            self.email = email
            self.skills = []
        
        def introduce(self):
            """自我介绍"""
            print(f"大家好，我叫 {self.name}，今年 {self.age} 岁")
            print(f"我的邮箱是 {self.email}")
            if self.skills:
                print(f"我的技能有：{', '.join(self.skills)}")
        
        def add_skill(self, skill):
            """添加技能"""
            if skill not in self.skills:
                self.skills.append(skill)
                print(f"学会了新技能：{skill}")
            else:
                print(f"已经掌握了 {skill}")
        
        def get_age_group(self):
            """获取年龄段"""
            if self.age < 18:
                return "青少年"
            elif self.age < 65:
                return "成年人"
            else:
                return "老年人"
        
        def update_email(self, new_email):
            """更新邮箱"""
            old_email = self.email
            self.email = new_email
            print(f"邮箱已从 {old_email} 更新为 {new_email}")
    
    # 创建人的实例
    person = Person("张三", 28, "zhangsan@example.com")
    
    print("个人信息：")
    person.introduce()
    
    print(f"\n年龄段：{person.get_age_group()}")
    
    print("\n学习新技能：")
    person.add_skill("Python")
    person.add_skill("JavaScript")
    person.add_skill("Python")  # 重复添加
    
    print("\n更新信息：")
    person.update_email("zhangsan.new@example.com")
    
    print("\n最终信息：")
    person.introduce()
    print()
    
    # 7. 类的实例属性 vs 类属性
    print("7. 类的实例属性 vs 类属性")
    print("-" * 30)
    
    class Student:
        """学生类"""
        
        # 类属性
        school_name = "Python编程学院"
        total_students = 0
        
        def __init__(self, name, student_id):
            """初始化学生属性"""
            # 实例属性
            self.name = name
            self.student_id = student_id
            self.grades = {}
            
            # 更新类属性
            Student.total_students += 1
        
        def add_grade(self, subject, grade):
            """添加成绩"""
            self.grades[subject] = grade
            print(f"{self.name} 在 {subject} 的成绩是 {grade}")
        
        def get_average_grade(self):
            """计算平均成绩"""
            if not self.grades:
                return 0
            return sum(self.grades.values()) / len(self.grades)
        
        def display_info(self):
            """显示学生信息"""
            print(f"学生姓名：{self.name}")
            print(f"学号：{self.student_id}")
            print(f"学校：{self.school_name}")
            print(f"平均成绩：{self.get_average_grade():.2f}")
        
        @classmethod
        def get_total_students(cls):
            """获取学生总数"""
            return cls.total_students
        
        @classmethod
        def change_school_name(cls, new_name):
            """更改学校名称"""
            cls.school_name = new_name
    
    # 创建学生实例
    student1 = Student("李四", "S001")
    student2 = Student("王五", "S002")
    
    print(f"学校名称：{Student.school_name}")
    print(f"学生总数：{Student.get_total_students()}")
    
    # 添加成绩
    student1.add_grade("数学", 85)
    student1.add_grade("英语", 92)
    student1.add_grade("物理", 88)
    
    student2.add_grade("数学", 78)
    student2.add_grade("英语", 85)
    
    print("\n学生1信息：")
    student1.display_info()
    
    print("\n学生2信息：")
    student2.display_info()
    
    # 修改类属性
    print("\n修改学校名称：")
    Student.change_school_name("高级Python编程学院")
    
    print("\n修改后的学生信息：")
    student1.display_info()
    print()
    
    # 8. 类的方法类型
    print("8. 类的方法类型")
    print("-" * 30)
    
    class Calculator:
        """计算器类"""
        
        # 类属性
        version = "1.0.0"
        
        def __init__(self, name):
            """初始化计算器"""
            self.name = name
            self.history = []
        
        # 实例方法
        def add(self, a, b):
            """加法"""
            result = a + b
            self.history.append(f"{a} + {b} = {result}")
            return result
        
        def subtract(self, a, b):
            """减法"""
            result = a - b
            self.history.append(f"{a} - {b} = {result}")
            return result
        
        def show_history(self):
            """显示计算历史"""
            print(f"{self.name} 的计算历史：")
            for record in self.history:
                print(f"  {record}")
        
        # 类方法
        @classmethod
        def get_version(cls):
            """获取版本信息"""
            return cls.version
        
        @classmethod
        def create_scientific_calculator(cls):
            """创建科学计算器"""
            return cls("科学计算器")
        
        # 静态方法
        @staticmethod
        def is_even(number):
            """检查数字是否为偶数"""
            return number % 2 == 0
        
        @staticmethod
        def factorial(n):
            """计算阶乘"""
            if n <= 1:
                return 1
            return n * Calculator.factorial(n - 1)
    
    # 使用不同类型的方法
    calc = Calculator("我的计算器")
    
    print("实例方法：")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    calc.show_history()
    
    print("\n类方法：")
    print(f"计算器版本：{Calculator.get_version()}")
    scientific_calc = Calculator.create_scientific_calculator()
    print(f"创建了：{scientific_calc.name}")
    
    print("\n静态方法：")
    print(f"8 是偶数吗？{Calculator.is_even(8)}")
    print(f"7 是偶数吗？{Calculator.is_even(7)}")
    print(f"5! = {Calculator.factorial(5)}")
    print()
    
    # 9. 类的特殊方法
    print("9. 类的特殊方法")
    print("-" * 30)
    
    class Book:
        """图书类"""
        
        def __init__(self, title, author, pages):
            """初始化图书属性"""
            self.title = title
            self.author = author
            self.pages = pages
        
        def __str__(self):
            """返回图书的字符串表示"""
            return f"《{self.title}》by {self.author}"
        
        def __repr__(self):
            """返回图书的官方字符串表示"""
            return f"Book('{self.title}', '{self.author}', {self.pages})"
        
        def __len__(self):
            """返回图书的页数"""
            return self.pages
        
        def __eq__(self, other):
            """比较两本书是否相等"""
            if isinstance(other, Book):
                return (self.title == other.title and 
                       self.author == other.author)
            return False
        
        def __lt__(self, other):
            """比较图书页数（用于排序）"""
            if isinstance(other, Book):
                return self.pages < other.pages
            return NotImplemented
    
    # 创建图书实例
    book1 = Book("Python编程", "张三", 300)
    book2 = Book("Java编程", "李四", 450)
    book3 = Book("Python编程", "张三", 300)
    
    print("特殊方法演示：")
    print(f"str(book1): {str(book1)}")
    print(f"repr(book1): {repr(book1)}")
    print(f"len(book1): {len(book1)}")
    print(f"book1 == book3: {book1 == book3}")
    print(f"book1 == book2: {book1 == book2}")
    print(f"book1 < book2: {book1 < book2}")
    
    # 排序
    books = [book1, book2]
    books.sort()
    print(f"\n按页数排序：")
    for book in books:
        print(f"  {book} ({len(book)} 页)")
    print()
    
    # 10. 类的设计原则
    print("10. 类的设计原则")
    print("-" * 30)
    
    class BankAccount:
        """银行账户类 - 演示良好的类设计"""
        
        def __init__(self, account_number, owner_name, initial_balance=0):
            """初始化账户"""
            self.account_number = account_number
            self.owner_name = owner_name
            self._balance = initial_balance  # 使用下划线表示内部属性
            self.transaction_history = []
        
        def deposit(self, amount):
            """存款"""
            if amount > 0:
                self._balance += amount
                self.transaction_history.append(f"存款: +{amount}")
                print(f"存款成功，金额：{amount}")
                return True
            else:
                print("存款金额必须大于0")
                return False
        
        def withdraw(self, amount):
            """取款"""
            if amount > 0:
                if amount <= self._balance:
                    self._balance -= amount
                    self.transaction_history.append(f"取款: -{amount}")
                    print(f"取款成功，金额：{amount}")
                    return True
                else:
                    print("余额不足")
                    return False
            else:
                print("取款金额必须大于0")
                return False
        
        def get_balance(self):
            """获取余额"""
            return self._balance
        
        def get_account_info(self):
            """获取账户信息"""
            return {
                'account_number': self.account_number,
                'owner_name': self.owner_name,
                'balance': self._balance
            }
        
        def show_transaction_history(self):
            """显示交易历史"""
            print(f"\n{self.owner_name} 的交易历史：")
            if self.transaction_history:
                for transaction in self.transaction_history:
                    print(f"  {transaction}")
            else:
                print("  暂无交易记录")
            print(f"当前余额：{self._balance}")
    
    # 使用银行账户类
    account = BankAccount("123456789", "张三", 1000)
    
    print("银行账户操作演示：")
    print(f"账户信息：{account.get_account_info()}")
    
    print("\n进行交易：")
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)  # 余额不足
    account.deposit(-100)   # 无效金额
    
    account.show_transaction_history()
    print()
    
    print("类设计原则总结：")
    print("1. 使用描述性的类名")
    print("2. 在__init__方法中初始化所有属性")
    print("3. 使用下划线表示内部属性")
    print("4. 提供公共接口方法")
    print("5. 添加输入验证")
    print("6. 编写清晰的文档字符串")
    print("7. 遵循单一职责原则")
    print("8. 使用特殊方法增强功能")
    print()
    
    print("=== 类的基础知识演示完成 ===")


if __name__ == "__main__":
    main() 