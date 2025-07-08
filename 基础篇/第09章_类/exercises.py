#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第09章 类 - 练习题解答

本文件包含《Python编程：从入门到实践》第9章类的所有练习题解答，
以及额外的高级练习题，帮助深入理解类的概念和应用。

练习题涵盖：
1. 类的基本定义和使用
2. 类的属性和方法
3. 类的继承
4. 实际应用项目
5. 高级特性应用
"""


def main():
    """主函数，运行所有练习题"""
    print("=" * 60)
    print("第09章 类 - 练习题解答")
    print("=" * 60)
    print()
    
    # 练习9-1：餐厅
    print("练习9-1：餐厅")
    print("-" * 30)
    
    class Restaurant:
        """餐厅类"""
        
        def __init__(self, restaurant_name, cuisine_type):
            """初始化餐厅属性"""
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        
        def describe_restaurant(self):
            """描述餐厅"""
            print(f"餐厅名称：{self.restaurant_name}")
            print(f"菜系类型：{self.cuisine_type}")
        
        def open_restaurant(self):
            """开门营业"""
            print(f"{self.restaurant_name} 现在开门营业！")
    
    # 创建餐厅实例
    restaurant = Restaurant("金龙餐厅", "中式料理")
    print(f"餐厅名称：{restaurant.restaurant_name}")
    print(f"菜系类型：{restaurant.cuisine_type}")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
    print()
    
    # 练习9-2：三家餐厅
    print("练习9-2：三家餐厅")
    print("-" * 30)
    
    restaurants = [
        Restaurant("意大利之家", "意大利菜"),
        Restaurant("寿司之神", "日本菜"),
        Restaurant("香格里拉", "印度菜")
    ]
    
    for restaurant in restaurants:
        restaurant.describe_restaurant()
        print()
    
    # 练习9-3：用户
    print("练习9-3：用户")
    print("-" * 30)
    
    class User:
        """用户类"""
        
        def __init__(self, first_name, last_name, **kwargs):
            """初始化用户属性"""
            self.first_name = first_name
            self.last_name = last_name
            self.profile = kwargs
        
        def describe_user(self):
            """描述用户"""
            print(f"用户姓名：{self.first_name} {self.last_name}")
            if self.profile:
                print("用户信息：")
                for key, value in self.profile.items():
                    print(f"  {key}: {value}")
        
        def greet_user(self):
            """问候用户"""
            print(f"你好，{self.first_name} {self.last_name}！")
    
    # 创建用户实例
    user = User("张", "三", age=25, city="北京", occupation="程序员")
    user.describe_user()
    user.greet_user()
    print()
    
    # 练习9-4：就餐人数
    print("练习9-4：就餐人数")
    print("-" * 30)
    
    class Restaurant:
        """餐厅类（改进版）"""
        
        def __init__(self, restaurant_name, cuisine_type):
            """初始化餐厅属性"""
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.number_served = 0
        
        def describe_restaurant(self):
            """描述餐厅"""
            print(f"餐厅名称：{self.restaurant_name}")
            print(f"菜系类型：{self.cuisine_type}")
            print(f"已服务顾客数：{self.number_served}")
        
        def open_restaurant(self):
            """开门营业"""
            print(f"{self.restaurant_name} 现在开门营业！")
        
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
    
    # 测试餐厅类
    restaurant = Restaurant("美味餐厅", "中式料理")
    restaurant.describe_restaurant()
    
    # 修改就餐人数
    restaurant.number_served = 50
    restaurant.describe_restaurant()
    
    # 使用方法设置就餐人数
    restaurant.set_number_served(100)
    restaurant.describe_restaurant()
    
    # 增加就餐人数
    restaurant.increment_number_served(20)
    restaurant.describe_restaurant()
    print()
    
    # 练习9-5：尝试登录次数
    print("练习9-5：尝试登录次数")
    print("-" * 30)
    
    class User:
        """用户类（改进版）"""
        
        def __init__(self, first_name, last_name, **kwargs):
            """初始化用户属性"""
            self.first_name = first_name
            self.last_name = last_name
            self.profile = kwargs
            self.login_attempts = 0
        
        def describe_user(self):
            """描述用户"""
            print(f"用户姓名：{self.first_name} {self.last_name}")
            print(f"登录尝试次数：{self.login_attempts}")
            if self.profile:
                print("用户信息：")
                for key, value in self.profile.items():
                    print(f"  {key}: {value}")
        
        def greet_user(self):
            """问候用户"""
            print(f"你好，{self.first_name} {self.last_name}！")
        
        def increment_login_attempts(self):
            """增加登录尝试次数"""
            self.login_attempts += 1
        
        def reset_login_attempts(self):
            """重置登录尝试次数"""
            self.login_attempts = 0
    
    # 测试用户类
    user = User("李", "四", age=30, city="上海")
    user.describe_user()
    
    # 模拟登录尝试
    for i in range(3):
        user.increment_login_attempts()
        print(f"登录尝试 {i+1}")
    
    user.describe_user()
    user.reset_login_attempts()
    print("重置登录尝试次数")
    user.describe_user()
    print()
    
    # 练习9-6：冰淇淋小店
    print("练习9-6：冰淇淋小店")
    print("-" * 30)
    
    class IceCreamStand(Restaurant):
        """冰淇淋小店类"""
        
        def __init__(self, restaurant_name, cuisine_type="冰淇淋"):
            """初始化冰淇淋小店"""
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = []
        
        def show_flavors(self):
            """显示可供应的口味"""
            if self.flavors:
                print(f"{self.restaurant_name} 提供以下口味：")
                for flavor in self.flavors:
                    print(f"  - {flavor}")
            else:
                print("暂时没有可供应的口味")
    
    # 创建冰淇淋小店
    ice_cream_stand = IceCreamStand("甜蜜时光")
    ice_cream_stand.flavors = ["香草", "巧克力", "草莓", "薄荷", "芒果"]
    ice_cream_stand.describe_restaurant()
    ice_cream_stand.show_flavors()
    print()
    
    # 练习9-7：管理员
    print("练习9-7：管理员")
    print("-" * 30)
    
    class Admin(User):
        """管理员类"""
        
        def __init__(self, first_name, last_name, **kwargs):
            """初始化管理员"""
            super().__init__(first_name, last_name, **kwargs)
            self.privileges = []
        
        def show_privileges(self):
            """显示管理员权限"""
            if self.privileges:
                print(f"管理员 {self.first_name} {self.last_name} 拥有以下权限：")
                for privilege in self.privileges:
                    print(f"  - {privilege}")
            else:
                print("管理员暂时没有权限")
    
    # 创建管理员
    admin = Admin("王", "五", age=35, city="广州", role="系统管理员")
    admin.privileges = ["添加用户", "删除用户", "修改用户信息", "查看系统日志", "管理数据库"]
    admin.describe_user()
    admin.show_privileges()
    print()
    
    # 练习9-8：权限
    print("练习9-8：权限")
    print("-" * 30)
    
    class Privileges:
        """权限类"""
        
        def __init__(self, privileges=None):
            """初始化权限"""
            self.privileges = privileges or []
        
        def show_privileges(self):
            """显示权限"""
            if self.privileges:
                print("权限列表：")
                for privilege in self.privileges:
                    print(f"  - {privilege}")
            else:
                print("暂时没有权限")
        
        def add_privilege(self, privilege):
            """添加权限"""
            if privilege not in self.privileges:
                self.privileges.append(privilege)
                print(f"已添加权限：{privilege}")
            else:
                print(f"权限已存在：{privilege}")
        
        def remove_privilege(self, privilege):
            """移除权限"""
            if privilege in self.privileges:
                self.privileges.remove(privilege)
                print(f"已移除权限：{privilege}")
            else:
                print(f"权限不存在：{privilege}")
    
    class Admin(User):
        """管理员类（改进版）"""
        
        def __init__(self, first_name, last_name, **kwargs):
            """初始化管理员"""
            super().__init__(first_name, last_name, **kwargs)
            self.privileges = Privileges()
        
        def show_privileges(self):
            """显示管理员权限"""
            print(f"管理员 {self.first_name} {self.last_name} 的权限：")
            self.privileges.show_privileges()
    
    # 测试权限系统
    admin = Admin("赵", "六", age=40, city="深圳")
    
    # 添加权限
    admin.privileges.add_privilege("添加用户")
    admin.privileges.add_privilege("删除用户")
    admin.privileges.add_privilege("修改用户信息")
    admin.privileges.add_privilege("查看系统日志")
    
    admin.show_privileges()
    
    # 移除权限
    admin.privileges.remove_privilege("删除用户")
    admin.show_privileges()
    print()
    
    # 练习9-9：电瓶升级
    print("练习9-9：电瓶升级")
    print("-" * 30)
    
    class Car:
        """汽车类"""
        
        def __init__(self, make, model, year):
            """初始化汽车属性"""
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0
        
        def get_descriptive_name(self):
            """返回汽车的描述性名称"""
            return f"{self.year} {self.make} {self.model}"
        
        def read_odometer(self):
            """显示汽车的里程"""
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
    
    class Battery:
        """电瓶类"""
        
        def __init__(self, battery_size=75):
            """初始化电瓶属性"""
            self.battery_size = battery_size
        
        def describe_battery(self):
            """描述电瓶"""
            print(f"This car has a {self.battery_size}-kWh battery.")
        
        def get_range(self):
            """返回电瓶的续航里程"""
            if self.battery_size == 75:
                range_miles = 260
            elif self.battery_size == 100:
                range_miles = 315
            else:
                range_miles = int(self.battery_size * 3.5)
            
            print(f"This car can go about {range_miles} miles on a full charge.")
        
        def upgrade_battery(self):
            """升级电瓶"""
            if self.battery_size != 100:
                self.battery_size = 100
                print("电瓶已升级到100kWh")
            else:
                print("电瓶已经是最新版本")
    
    class ElectricCar(Car):
        """电动汽车类"""
        
        def __init__(self, make, model, year):
            """初始化电动汽车"""
            super().__init__(make, model, year)
            self.battery = Battery()
        
        def describe_battery(self):
            """描述电瓶"""
            self.battery.describe_battery()
        
        def fill_gas_tank(self):
            """电动汽车没有油箱"""
            print("This car doesn't need a gas tank!")
    
    # 测试电瓶升级
    my_tesla = ElectricCar('tesla', 'model s', 2019)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
    
    # 升级电瓶
    my_tesla.battery.upgrade_battery()
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
    print()
    
    # 额外练习：学生管理系统
    print("额外练习：学生管理系统")
    print("-" * 30)
    
    class Student:
        """学生类"""
        
        def __init__(self, name, student_id, grade):
            """初始化学生"""
            self.name = name
            self.student_id = student_id
            self.grade = grade
            self.courses = {}
        
        def add_course(self, course_name, score):
            """添加课程成绩"""
            self.courses[course_name] = score
            print(f"已为 {self.name} 添加课程 {course_name}，成绩：{score}")
        
        def get_average_score(self):
            """计算平均分"""
            if not self.courses:
                return 0
            return sum(self.courses.values()) / len(self.courses)
        
        def display_info(self):
            """显示学生信息"""
            print(f"姓名：{self.name}")
            print(f"学号：{self.student_id}")
            print(f"年级：{self.grade}")
            print(f"课程数：{len(self.courses)}")
            print(f"平均分：{self.get_average_score():.2f}")
    
    class GraduateStudent(Student):
        """研究生类"""
        
        def __init__(self, name, student_id, grade, supervisor):
            """初始化研究生"""
            super().__init__(name, student_id, grade)
            self.supervisor = supervisor
            self.research_topic = None
        
        def set_research_topic(self, topic):
            """设置研究课题"""
            self.research_topic = topic
            print(f"已为 {self.name} 设置研究课题：{topic}")
        
        def display_info(self):
            """显示研究生信息"""
            super().display_info()
            print(f"导师：{self.supervisor}")
            print(f"研究课题：{self.research_topic or '未设置'}")
    
    # 测试学生管理系统
    student = Student("张三", "2023001", "大三")
    student.add_course("数学", 85)
    student.add_course("英语", 90)
    student.add_course("计算机", 88)
    student.display_info()
    print()
    
    grad_student = GraduateStudent("李四", "2023G001", "研一", "王教授")
    grad_student.add_course("高等数学", 92)
    grad_student.add_course("机器学习", 89)
    grad_student.set_research_topic("深度学习在自然语言处理中的应用")
    grad_student.display_info()
    print()
    
    # 额外练习：图书管理系统
    print("额外练习：图书管理系统")
    print("-" * 30)
    
    class Book:
        """图书类"""
        
        def __init__(self, title, author, isbn, copies=1):
            """初始化图书"""
            self.title = title
            self.author = author
            self.isbn = isbn
            self.total_copies = copies
            self.available_copies = copies
            self.borrowed_by = []
        
        def is_available(self):
            """检查是否可借"""
            return self.available_copies > 0
        
        def borrow(self, borrower_name):
            """借书"""
            if self.is_available():
                self.available_copies -= 1
                self.borrowed_by.append(borrower_name)
                print(f"《{self.title}》已借给 {borrower_name}")
                return True
            else:
                print(f"《{self.title}》暂时无法借阅")
                return False
        
        def return_book(self, borrower_name):
            """还书"""
            if borrower_name in self.borrowed_by:
                self.available_copies += 1
                self.borrowed_by.remove(borrower_name)
                print(f"{borrower_name} 已归还《{self.title}》")
                return True
            else:
                print(f"{borrower_name} 没有借阅《{self.title}》")
                return False
        
        def display_info(self):
            """显示图书信息"""
            print(f"书名：{self.title}")
            print(f"作者：{self.author}")
            print(f"ISBN：{self.isbn}")
            print(f"总册数：{self.total_copies}")
            print(f"可借册数：{self.available_copies}")
            if self.borrowed_by:
                print(f"借阅者：{', '.join(self.borrowed_by)}")
    
    class Library:
        """图书馆类"""
        
        def __init__(self, name):
            """初始化图书馆"""
            self.name = name
            self.books = {}
        
        def add_book(self, book):
            """添加图书"""
            self.books[book.isbn] = book
            print(f"已添加图书：《{book.title}》")
        
        def find_book(self, isbn):
            """查找图书"""
            return self.books.get(isbn)
        
        def list_books(self):
            """列出所有图书"""
            print(f"{self.name} 的图书清单：")
            for book in self.books.values():
                status = "可借" if book.is_available() else "已借完"
                print(f"  《{book.title}》- {book.author} ({status})")
        
        def borrow_book(self, isbn, borrower_name):
            """借书"""
            book = self.find_book(isbn)
            if book:
                return book.borrow(borrower_name)
            else:
                print("未找到该图书")
                return False
        
        def return_book(self, isbn, borrower_name):
            """还书"""
            book = self.find_book(isbn)
            if book:
                return book.return_book(borrower_name)
            else:
                print("未找到该图书")
                return False
    
    # 测试图书管理系统
    library = Library("市图书馆")
    
    # 添加图书
    books = [
        Book("Python编程", "Eric Matthes", "978-1593279288", 3),
        Book("算法导论", "Thomas H. Cormen", "978-0262033848", 2),
        Book("设计模式", "Erich Gamma", "978-0201633610", 1)
    ]
    
    for book in books:
        library.add_book(book)
    
    library.list_books()
    print()
    
    # 借书操作
    library.borrow_book("978-1593279288", "张三")
    library.borrow_book("978-1593279288", "李四")
    library.borrow_book("978-0262033848", "王五")
    
    print("\n借书后的图书状态：")
    library.list_books()
    
    # 还书操作
    library.return_book("978-1593279288", "张三")
    
    print("\n还书后的图书状态：")
    library.list_books()
    print()
    
    # 额外练习：银行账户系统
    print("额外练习：银行账户系统")
    print("-" * 30)
    
    class BankAccount:
        """银行账户基类"""
        
        def __init__(self, account_number, owner_name, initial_balance=0):
            """初始化账户"""
            self.account_number = account_number
            self.owner_name = owner_name
            self._balance = initial_balance
            self.transaction_history = []
        
        def deposit(self, amount):
            """存款"""
            if amount > 0:
                self._balance += amount
                self._record_transaction("存款", amount)
                print(f"存款 {amount} 元成功，当前余额：{self._balance} 元")
                return True
            else:
                print("存款金额必须大于0")
                return False
        
        def withdraw(self, amount):
            """取款"""
            if amount > 0:
                if amount <= self._balance:
                    self._balance -= amount
                    self._record_transaction("取款", -amount)
                    print(f"取款 {amount} 元成功，当前余额：{self._balance} 元")
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
        
        def _record_transaction(self, transaction_type, amount):
            """记录交易"""
            import datetime
            self.transaction_history.append({
                'type': transaction_type,
                'amount': amount,
                'balance': self._balance,
                'timestamp': datetime.datetime.now()
            })
        
        def print_statement(self):
            """打印账户对账单"""
            print(f"\n{self.owner_name} 的账户对账单")
            print(f"账户号码：{self.account_number}")
            print(f"当前余额：{self._balance} 元")
            print("交易记录：")
            for transaction in self.transaction_history[-10:]:  # 只显示最近10笔
                print(f"  {transaction['timestamp'].strftime('%Y-%m-%d %H:%M:%S')} "
                      f"{transaction['type']} {abs(transaction['amount'])} 元 "
                      f"余额：{transaction['balance']} 元")
    
    class SavingsAccount(BankAccount):
        """储蓄账户"""
        
        def __init__(self, account_number, owner_name, initial_balance=0, interest_rate=0.02):
            """初始化储蓄账户"""
            super().__init__(account_number, owner_name, initial_balance)
            self.interest_rate = interest_rate
        
        def calculate_interest(self):
            """计算利息"""
            interest = self._balance * self.interest_rate
            self.deposit(interest)
            print(f"利息 {interest:.2f} 元已存入账户")
    
    class CheckingAccount(BankAccount):
        """支票账户"""
        
        def __init__(self, account_number, owner_name, initial_balance=0, overdraft_limit=1000):
            """初始化支票账户"""
            super().__init__(account_number, owner_name, initial_balance)
            self.overdraft_limit = overdraft_limit
        
        def withdraw(self, amount):
            """取款（可透支）"""
            if amount > 0:
                if amount <= self._balance + self.overdraft_limit:
                    self._balance -= amount
                    self._record_transaction("取款", -amount)
                    print(f"取款 {amount} 元成功，当前余额：{self._balance} 元")
                    if self._balance < 0:
                        print(f"账户已透支 {abs(self._balance)} 元")
                    return True
                else:
                    print(f"超过透支限额，最多可取款 {self._balance + self.overdraft_limit} 元")
                    return False
            else:
                print("取款金额必须大于0")
                return False
    
    # 测试银行账户系统
    savings = SavingsAccount("S001", "张三", 1000)
    checking = CheckingAccount("C001", "李四", 500, 1000)
    
    print("储蓄账户操作：")
    savings.deposit(500)
    savings.withdraw(200)
    savings.calculate_interest()
    savings.print_statement()
    
    print("\n支票账户操作：")
    checking.deposit(300)
    checking.withdraw(1200)  # 透支
    checking.withdraw(500)   # 超过透支限额
    checking.deposit(100)
    checking.print_statement()
    
    print("\n=== 第09章类的练习题解答完成 ===")


if __name__ == "__main__":
    main() 