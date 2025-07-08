#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第09章 类 - 类的继承详解

本文件详细演示Python类的继承机制，包括：
1. 继承的基本概念
2. 子类的定义和实例化
3. 重写父类方法
4. super()函数的使用
5. 多重继承
6. 方法解析顺序(MRO)
7. 抽象基类
8. 实际应用示例

继承是面向对象编程的核心特性之一，它允许我们基于现有类创建新类。
"""


def main():
    """主函数，演示类的继承"""
    print("=" * 60)
    print("第09章 类 - 类的继承详解")
    print("=" * 60)
    print()
    
    # 1. 继承的基本概念
    print("1. 继承的基本概念")
    print("-" * 30)
    
    class Animal:
        """动物基类"""
        
        def __init__(self, name, species):
            """初始化动物属性"""
            self.name = name
            self.species = species
            self.is_alive = True
        
        def eat(self):
            """吃东西"""
            print(f"{self.name} is eating.")
        
        def sleep(self):
            """睡觉"""
            print(f"{self.name} is sleeping.")
        
        def make_sound(self):
            """发出声音"""
            print(f"{self.name} makes a sound.")
        
        def info(self):
            """显示动物信息"""
            print(f"Name: {self.name}, Species: {self.species}")
    
    # 定义子类
    class Dog(Animal):
        """狗类，继承自Animal"""
        
        def make_sound(self):
            """重写父类方法"""
            print(f"{self.name} barks: Woof! Woof!")
        
        def fetch(self):
            """狗特有的行为"""
            print(f"{self.name} is fetching the ball.")
    
    class Cat(Animal):
        """猫类，继承自Animal"""
        
        def make_sound(self):
            """重写父类方法"""
            print(f"{self.name} meows: Meow! Meow!")
        
        def climb_tree(self):
            """猫特有的行为"""
            print(f"{self.name} is climbing a tree.")
    
    # 使用继承
    print("创建动物实例：")
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Persian")
    
    # 调用继承的方法
    print("\n调用继承的方法：")
    dog.info()
    dog.eat()
    dog.sleep()
    
    cat.info()
    cat.eat()
    cat.sleep()
    
    # 调用重写的方法
    print("\n调用重写的方法：")
    dog.make_sound()
    cat.make_sound()
    
    # 调用子类特有的方法
    print("\n调用子类特有的方法：")
    dog.fetch()
    cat.climb_tree()
    print()
    
    # 2. 使用super()函数
    print("2. 使用super()函数")
    print("-" * 30)
    
    class Vehicle:
        """交通工具基类"""
        
        def __init__(self, make, model, year):
            """初始化交通工具属性"""
            self.make = make
            self.model = model
            self.year = year
            self.mileage = 0
        
        def start_engine(self):
            """启动引擎"""
            print(f"The {self.year} {self.make} {self.model}'s engine is starting.")
        
        def stop_engine(self):
            """停止引擎"""
            print(f"The {self.year} {self.make} {self.model}'s engine is stopping.")
        
        def drive(self, distance):
            """行驶"""
            self.mileage += distance
            print(f"Driving {distance} miles. Total mileage: {self.mileage}")
    
    class Car(Vehicle):
        """汽车类"""
        
        def __init__(self, make, model, year, doors=4):
            """初始化汽车属性"""
            super().__init__(make, model, year)  # 调用父类的__init__
            self.doors = doors
            self.trunk_capacity = 15  # 行李箱容量（立方英尺）
        
        def open_trunk(self):
            """打开行李箱"""
            print(f"Opening the trunk of the {self.make} {self.model}.")
        
        def start_engine(self):
            """重写启动引擎方法"""
            super().start_engine()  # 调用父类方法
            print("Car-specific startup sequence completed.")
    
    class Motorcycle(Vehicle):
        """摩托车类"""
        
        def __init__(self, make, model, year, engine_size):
            """初始化摩托车属性"""
            super().__init__(make, model, year)
            self.engine_size = engine_size  # 引擎排量
            self.has_sidecar = False
        
        def wheelie(self):
            """翘头行驶"""
            print(f"The {self.make} {self.model} is doing a wheelie!")
        
        def start_engine(self):
            """重写启动引擎方法"""
            super().start_engine()
            print(f"The {self.engine_size}cc engine is ready to roar!")
    
    # 使用super()的示例
    print("使用super()的示例：")
    car = Car("Toyota", "Camry", 2023, doors=4)
    motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2023, 749)
    
    print("\n汽车操作：")
    car.start_engine()
    car.drive(50)
    car.open_trunk()
    car.stop_engine()
    
    print("\n摩托车操作：")
    motorcycle.start_engine()
    motorcycle.drive(30)
    motorcycle.wheelie()
    motorcycle.stop_engine()
    print()
    
    # 3. 多层继承
    print("3. 多层继承")
    print("-" * 30)
    
    class ElectricVehicle(Vehicle):
        """电动车类"""
        
        def __init__(self, make, model, year, battery_capacity):
            """初始化电动车属性"""
            super().__init__(make, model, year)
            self.battery_capacity = battery_capacity  # 电池容量(kWh)
            self.charge_level = 100  # 电量百分比
        
        def charge(self, hours):
            """充电"""
            charge_rate = 10  # 每小时充电10%
            charge_added = min(hours * charge_rate, 100 - self.charge_level)
            self.charge_level += charge_added
            print(f"Charged for {hours} hours. Battery level: {self.charge_level}%")
        
        def start_engine(self):
            """电动车启动"""
            if self.charge_level > 0:
                print(f"Electric motor of {self.make} {self.model} is starting silently.")
            else:
                print("Cannot start: Battery is empty!")
        
        def drive(self, distance):
            """电动车行驶"""
            battery_usage = distance * 0.3  # 每英里消耗0.3%电量
            if self.charge_level >= battery_usage:
                super().drive(distance)
                self.charge_level -= battery_usage
                print(f"Battery level after driving: {self.charge_level:.1f}%")
            else:
                print("Cannot drive: Insufficient battery!")
    
    class ElectricCar(ElectricVehicle):
        """电动汽车类"""
        
        def __init__(self, make, model, year, battery_capacity, doors=4):
            """初始化电动汽车属性"""
            super().__init__(make, model, year, battery_capacity)
            self.doors = doors
            self.autopilot = False
        
        def enable_autopilot(self):
            """启用自动驾驶"""
            self.autopilot = True
            print(f"Autopilot enabled on {self.make} {self.model}")
        
        def disable_autopilot(self):
            """禁用自动驾驶"""
            self.autopilot = False
            print(f"Autopilot disabled on {self.make} {self.model}")
    
    # 多层继承示例
    print("多层继承示例：")
    tesla = ElectricCar("Tesla", "Model S", 2023, 100, doors=4)
    
    print(f"创建了 {tesla.year} {tesla.make} {tesla.model}")
    tesla.start_engine()
    tesla.drive(20)
    tesla.charge(2)
    tesla.enable_autopilot()
    tesla.drive(15)
    print()
    
    # 4. 多重继承
    print("4. 多重继承")
    print("-" * 30)
    
    class Flyable:
        """可飞行的混入类"""
        
        def __init__(self):
            self.altitude = 0
        
        def take_off(self):
            """起飞"""
            self.altitude = 1000
            print("Taking off...")
        
        def land(self):
            """降落"""
            self.altitude = 0
            print("Landing...")
        
        def fly(self, distance):
            """飞行"""
            if self.altitude > 0:
                print(f"Flying {distance} miles at {self.altitude} feet.")
            else:
                print("Cannot fly: Not airborne!")
    
    class Swimmable:
        """可游泳的混入类"""
        
        def __init__(self):
            self.depth = 0
        
        def dive(self, depth):
            """潜水"""
            self.depth = depth
            print(f"Diving to {depth} feet deep.")
        
        def surface(self):
            """浮出水面"""
            self.depth = 0
            print("Surfacing...")
        
        def swim(self, distance):
            """游泳"""
            print(f"Swimming {distance} miles.")
    
    class Duck(Animal, Flyable, Swimmable):
        """鸭子类 - 多重继承示例"""
        
        def __init__(self, name):
            """初始化鸭子属性"""
            Animal.__init__(self, name, "Duck")
            Flyable.__init__(self)
            Swimmable.__init__(self)
        
        def make_sound(self):
            """鸭子叫声"""
            print(f"{self.name} quacks: Quack! Quack!")
        
        def show_abilities(self):
            """展示能力"""
            print(f"{self.name} can walk, fly, and swim!")
    
    # 多重继承示例
    print("多重继承示例：")
    duck = Duck("Donald")
    
    print("鸭子的基本信息：")
    duck.info()
    duck.show_abilities()
    
    print("\n鸭子的各种行为：")
    duck.make_sound()
    duck.eat()
    
    print("\n飞行能力：")
    duck.take_off()
    duck.fly(5)
    duck.land()
    
    print("\n游泳能力：")
    duck.swim(2)
    duck.dive(10)
    duck.surface()
    print()
    
    # 5. 方法解析顺序(MRO)
    print("5. 方法解析顺序(MRO)")
    print("-" * 30)
    
    class A:
        def method(self):
            print("Method from class A")
    
    class B(A):
        def method(self):
            print("Method from class B")
            super().method()
    
    class C(A):
        def method(self):
            print("Method from class C")
            super().method()
    
    class D(B, C):
        def method(self):
            print("Method from class D")
            super().method()
    
    # 查看MRO
    print("方法解析顺序(MRO)：")
    print(f"Duck MRO: {Duck.__mro__}")
    print(f"D类 MRO: {D.__mro__}")
    
    print("\n调用D类的方法：")
    d = D()
    d.method()
    print()
    
    # 6. 抽象基类
    print("6. 抽象基类")
    print("-" * 30)
    
    from abc import ABC, abstractmethod
    
    class Shape(ABC):
        """抽象图形基类"""
        
        def __init__(self, name):
            self.name = name
        
        @abstractmethod
        def area(self):
            """计算面积 - 抽象方法"""
            pass
        
        @abstractmethod
        def perimeter(self):
            """计算周长 - 抽象方法"""
            pass
        
        def display_info(self):
            """显示图形信息"""
            print(f"{self.name}: Area = {self.area():.2f}, Perimeter = {self.perimeter():.2f}")
    
    class Rectangle(Shape):
        """矩形类"""
        
        def __init__(self, width, height):
            super().__init__("Rectangle")
            self.width = width
            self.height = height
        
        def area(self):
            """计算矩形面积"""
            return self.width * self.height
        
        def perimeter(self):
            """计算矩形周长"""
            return 2 * (self.width + self.height)
    
    class Circle(Shape):
        """圆形类"""
        
        def __init__(self, radius):
            super().__init__("Circle")
            self.radius = radius
        
        def area(self):
            """计算圆形面积"""
            import math
            return math.pi * self.radius ** 2
        
        def perimeter(self):
            """计算圆形周长"""
            import math
            return 2 * math.pi * self.radius
    
    # 使用抽象基类
    print("抽象基类示例：")
    
    # 不能直接实例化抽象类
    # shape = Shape("Generic")  # 这会报错
    
    rectangle = Rectangle(5, 3)
    circle = Circle(4)
    
    shapes = [rectangle, circle]
    
    for shape in shapes:
        shape.display_info()
    print()
    
    # 7. 实际应用：员工管理系统
    print("7. 实际应用：员工管理系统")
    print("-" * 30)
    
    class Employee:
        """员工基类"""
        
        def __init__(self, name, employee_id, department):
            """初始化员工属性"""
            self.name = name
            self.employee_id = employee_id
            self.department = department
            self.base_salary = 0
        
        def get_info(self):
            """获取员工信息"""
            return {
                'name': self.name,
                'id': self.employee_id,
                'department': self.department,
                'salary': self.calculate_salary()
            }
        
        def calculate_salary(self):
            """计算薪资 - 基础实现"""
            return self.base_salary
        
        def work(self):
            """工作 - 基础实现"""
            print(f"{self.name} is working.")
    
    class Developer(Employee):
        """开发人员类"""
        
        def __init__(self, name, employee_id, programming_languages):
            super().__init__(name, employee_id, "Engineering")
            self.programming_languages = programming_languages
            self.base_salary = 80000
            self.projects_completed = 0
        
        def calculate_salary(self):
            """计算开发人员薪资"""
            bonus = self.projects_completed * 2000
            return self.base_salary + bonus
        
        def work(self):
            """开发人员工作"""
            print(f"{self.name} is coding in {', '.join(self.programming_languages)}.")
        
        def complete_project(self):
            """完成项目"""
            self.projects_completed += 1
            print(f"{self.name} completed a project! Total: {self.projects_completed}")
    
    class Manager(Employee):
        """经理类"""
        
        def __init__(self, name, employee_id, team_size):
            super().__init__(name, employee_id, "Management")
            self.team_size = team_size
            self.base_salary = 100000
            self.team_members = []
        
        def calculate_salary(self):
            """计算经理薪资"""
            team_bonus = self.team_size * 5000
            return self.base_salary + team_bonus
        
        def work(self):
            """经理工作"""
            print(f"{self.name} is managing a team of {self.team_size} people.")
        
        def add_team_member(self, employee):
            """添加团队成员"""
            self.team_members.append(employee)
            self.team_size = len(self.team_members)
            print(f"Added {employee.name} to {self.name}'s team.")
        
        def conduct_meeting(self):
            """举行会议"""
            print(f"{self.name} is conducting a team meeting.")
            for member in self.team_members:
                print(f"  - {member.name} is attending")
    
    class Intern(Developer):
        """实习生类"""
        
        def __init__(self, name, employee_id, programming_languages, university):
            super().__init__(name, employee_id, programming_languages)
            self.university = university
            self.base_salary = 20000  # 实习生薪资较低
            self.learning_progress = 0
        
        def calculate_salary(self):
            """计算实习生薪资"""
            # 实习生没有项目奖金，但有学习进度奖金
            learning_bonus = self.learning_progress * 500
            return self.base_salary + learning_bonus
        
        def work(self):
            """实习生工作"""
            print(f"{self.name} (intern from {self.university}) is learning and coding.")
        
        def learn(self, skill):
            """学习新技能"""
            self.learning_progress += 1
            print(f"{self.name} learned {skill}. Progress: {self.learning_progress}")
    
    # 员工管理系统示例
    print("员工管理系统示例：")
    
    # 创建员工
    developer = Developer("Alice", "DEV001", ["Python", "JavaScript"])
    manager = Manager("Bob", "MGR001", 0)
    intern = Intern("Charlie", "INT001", ["Python"], "MIT")
    
    # 建立团队关系
    manager.add_team_member(developer)
    manager.add_team_member(intern)
    
    employees = [developer, manager, intern]
    
    print("\n员工信息：")
    for emp in employees:
        info = emp.get_info()
        print(f"{info['name']} ({info['id']}): Department: {info['department']}, Salary: ${info['salary']}")
    
    print("\n员工工作：")
    for emp in employees:
        emp.work()
    
    print("\n项目和学习进展：")
    developer.complete_project()
    developer.complete_project()
    
    intern.learn("Django")
    intern.learn("React")
    
    print("\n举行团队会议：")
    manager.conduct_meeting()
    
    print("\n更新后的薪资：")
    for emp in employees:
        info = emp.get_info()
        print(f"{info['name']}: ${info['salary']}")
    print()
    
    # 8. 继承的最佳实践
    print("8. 继承的最佳实践")
    print("-" * 30)
    
    class BaseSensor:
        """传感器基类 - 演示良好的继承设计"""
        
        def __init__(self, sensor_id, location):
            self.sensor_id = sensor_id
            self.location = location
            self.is_active = True
            self.readings = []
        
        def activate(self):
            """激活传感器"""
            self.is_active = True
            print(f"Sensor {self.sensor_id} activated.")
        
        def deactivate(self):
            """停用传感器"""
            self.is_active = False
            print(f"Sensor {self.sensor_id} deactivated.")
        
        def record_reading(self, value):
            """记录读数"""
            if self.is_active:
                import datetime
                timestamp = datetime.datetime.now()
                self.readings.append({'value': value, 'timestamp': timestamp})
                self._process_reading(value)
            else:
                print(f"Sensor {self.sensor_id} is not active!")
        
        def _process_reading(self, value):
            """处理读数 - 由子类重写"""
            print(f"Recording value: {value}")
        
        def get_latest_reading(self):
            """获取最新读数"""
            if self.readings:
                return self.readings[-1]
            return None
        
        def get_average_reading(self):
            """获取平均读数"""
            if not self.readings:
                return 0
            return sum(r['value'] for r in self.readings) / len(self.readings)
    
    class TemperatureSensor(BaseSensor):
        """温度传感器"""
        
        def __init__(self, sensor_id, location, unit='C'):
            super().__init__(sensor_id, location)
            self.unit = unit
            self.alert_threshold = {'min': -10, 'max': 40}
        
        def _process_reading(self, temperature):
            """处理温度读数"""
            super()._process_reading(f"{temperature}°{self.unit}")
            self._check_alerts(temperature)
        
        def _check_alerts(self, temperature):
            """检查温度警报"""
            if temperature < self.alert_threshold['min']:
                print(f"⚠️  LOW TEMPERATURE ALERT: {temperature}°{self.unit}")
            elif temperature > self.alert_threshold['max']:
                print(f"⚠️  HIGH TEMPERATURE ALERT: {temperature}°{self.unit}")
        
        def set_alert_threshold(self, min_temp, max_temp):
            """设置警报阈值"""
            self.alert_threshold = {'min': min_temp, 'max': max_temp}
    
    class HumiditySensor(BaseSensor):
        """湿度传感器"""
        
        def __init__(self, sensor_id, location):
            super().__init__(sensor_id, location)
            self.calibration_offset = 0
        
        def _process_reading(self, humidity):
            """处理湿度读数"""
            calibrated_humidity = humidity + self.calibration_offset
            super()._process_reading(f"{calibrated_humidity}%")
            self._check_humidity_level(calibrated_humidity)
        
        def _check_humidity_level(self, humidity):
            """检查湿度级别"""
            if humidity < 30:
                print("💧 Low humidity detected")
            elif humidity > 70:
                print("💧 High humidity detected")
        
        def calibrate(self, offset):
            """校准传感器"""
            self.calibration_offset = offset
            print(f"Humidity sensor calibrated with offset: {offset}%")
    
    # 继承最佳实践示例
    print("传感器系统示例：")
    
    temp_sensor = TemperatureSensor("T001", "Living Room")
    humidity_sensor = HumiditySensor("H001", "Living Room")
    
    print("\n设置传感器：")
    temp_sensor.set_alert_threshold(-5, 35)
    humidity_sensor.calibrate(2)
    
    print("\n记录读数：")
    temp_sensor.record_reading(22)
    temp_sensor.record_reading(38)  # 触发高温警报
    temp_sensor.record_reading(-8)  # 触发低温警报
    
    humidity_sensor.record_reading(45)
    humidity_sensor.record_reading(75)  # 高湿度
    
    print("\n传感器统计：")
    print(f"Temperature average: {temp_sensor.get_average_reading():.1f}°{temp_sensor.unit}")
    print(f"Humidity average: {humidity_sensor.get_average_reading():.1f}%")
    print()
    
    print("继承的最佳实践总结：")
    print("1. 使用继承表示'is-a'关系")
    print("2. 优先使用组合而非继承")
    print("3. 保持继承层次简单")
    print("4. 使用super()调用父类方法")
    print("5. 重写方法时保持一致的接口")
    print("6. 使用抽象基类定义接口")
    print("7. 避免过深的继承层次")
    print("8. 考虑使用混入(Mixin)类")
    print()
    
    print("=== 类的继承详解演示完成 ===")


if __name__ == "__main__":
    main() 