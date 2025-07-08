#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第09章 类 - 类的高级特性

本文件演示Python类的高级特性，包括：
1. 属性装饰器(@property)
2. 类方法和静态方法
3. 特殊方法(魔术方法)
4. 描述符(descriptor)
5. 元类(metaclass)
6. 上下文管理器
7. 类的装饰器
8. 数据类(dataclass)

这些高级特性可以让我们编写更加优雅和强大的面向对象代码。
"""


def main():
    """主函数，演示类的高级特性"""
    print("=" * 60)
    print("第09章 类 - 类的高级特性")
    print("=" * 60)
    print()
    
    # 1. 属性装饰器(@property)
    print("1. 属性装饰器(@property)")
    print("-" * 30)
    
    class Circle:
        """圆形类 - 演示属性装饰器"""
        
        def __init__(self, radius):
            """初始化圆形"""
            self._radius = radius  # 私有属性
        
        @property
        def radius(self):
            """获取半径"""
            return self._radius
        
        @radius.setter
        def radius(self, value):
            """设置半径"""
            if value <= 0:
                raise ValueError("半径必须大于0")
            self._radius = value
        
        @radius.deleter
        def radius(self):
            """删除半径"""
            print("删除半径属性")
            del self._radius
        
        @property
        def area(self):
            """计算面积（只读属性）"""
            import math
            return math.pi * self._radius ** 2
        
        @property
        def diameter(self):
            """计算直径（只读属性）"""
            return 2 * self._radius
        
        @property
        def circumference(self):
            """计算周长（只读属性）"""
            import math
            return 2 * math.pi * self._radius
    
    # 使用属性装饰器
    print("属性装饰器示例：")
    circle = Circle(5)
    
    print(f"半径: {circle.radius}")
    print(f"面积: {circle.area:.2f}")
    print(f"直径: {circle.diameter}")
    print(f"周长: {circle.circumference:.2f}")
    
    # 修改半径
    circle.radius = 10
    print(f"\n修改半径后:")
    print(f"半径: {circle.radius}")
    print(f"面积: {circle.area:.2f}")
    
    # 尝试设置无效值
    try:
        circle.radius = -5
    except ValueError as e:
        print(f"错误: {e}")
    
    # 尝试修改只读属性
    try:
        circle.area = 100
    except AttributeError as e:
        print(f"错误: {e}")
    print()
    
    # 2. 类方法和静态方法的深入应用
    print("2. 类方法和静态方法的深入应用")
    print("-" * 30)
    
    class Person:
        """人类 - 演示类方法和静态方法"""
        
        population = 0  # 类属性
        
        def __init__(self, name, birth_year):
            """初始化人的属性"""
            self.name = name
            self.birth_year = birth_year
            Person.population += 1
        
        @classmethod
        def get_population(cls):
            """获取人口数量"""
            return cls.population
        
        @classmethod
        def from_string(cls, person_str):
            """从字符串创建Person实例"""
            name, birth_year = person_str.split('-')
            return cls(name, int(birth_year))
        
        @classmethod
        def create_baby(cls, name):
            """创建今年出生的婴儿"""
            import datetime
            current_year = datetime.date.today().year
            return cls(name, current_year)
        
        @staticmethod
        def is_adult(birth_year):
            """判断是否成年（静态方法）"""
            import datetime
            current_year = datetime.date.today().year
            return current_year - birth_year >= 18
        
        @staticmethod
        def calculate_age(birth_year):
            """计算年龄"""
            import datetime
            current_year = datetime.date.today().year
            return current_year - birth_year
        
        def get_age(self):
            """获取年龄（实例方法）"""
            return self.calculate_age(self.birth_year)
        
        def is_adult_instance(self):
            """判断是否成年（实例方法）"""
            return self.is_adult(self.birth_year)
    
    # 使用类方法和静态方法
    print("类方法和静态方法示例：")
    
    # 使用普通构造函数
    person1 = Person("Alice", 1990)
    
    # 使用类方法创建实例
    person2 = Person.from_string("Bob-1985")
    person3 = Person.create_baby("Charlie")
    
    print(f"总人口: {Person.get_population()}")
    
    # 使用静态方法
    print(f"1990年出生的人是否成年: {Person.is_adult(1990)}")
    print(f"2020年出生的人是否成年: {Person.is_adult(2020)}")
    
    # 结合使用
    people = [person1, person2, person3]
    for person in people:
        print(f"{person.name} ({person.birth_year}): {person.get_age()}岁, "
              f"成年: {person.is_adult_instance()}")
    print()
    
    # 3. 特殊方法(魔术方法)
    print("3. 特殊方法(魔术方法)")
    print("-" * 30)
    
    class Vector:
        """向量类 - 演示特殊方法"""
        
        def __init__(self, x, y):
            """初始化向量"""
            self.x = x
            self.y = y
        
        def __str__(self):
            """字符串表示"""
            return f"Vector({self.x}, {self.y})"
        
        def __repr__(self):
            """官方字符串表示"""
            return f"Vector({self.x}, {self.y})"
        
        def __add__(self, other):
            """向量加法"""
            if isinstance(other, Vector):
                return Vector(self.x + other.x, self.y + other.y)
            return NotImplemented
        
        def __sub__(self, other):
            """向量减法"""
            if isinstance(other, Vector):
                return Vector(self.x - other.x, self.y - other.y)
            return NotImplemented
        
        def __mul__(self, scalar):
            """标量乘法"""
            if isinstance(scalar, (int, float)):
                return Vector(self.x * scalar, self.y * scalar)
            return NotImplemented
        
        def __rmul__(self, scalar):
            """右乘"""
            return self.__mul__(scalar)
        
        def __eq__(self, other):
            """相等比较"""
            if isinstance(other, Vector):
                return self.x == other.x and self.y == other.y
            return False
        
        def __len__(self):
            """向量长度"""
            return int((self.x ** 2 + self.y ** 2) ** 0.5)
        
        def __getitem__(self, index):
            """索引访问"""
            if index == 0:
                return self.x
            elif index == 1:
                return self.y
            else:
                raise IndexError("Vector index out of range")
        
        def __setitem__(self, index, value):
            """索引设置"""
            if index == 0:
                self.x = value
            elif index == 1:
                self.y = value
            else:
                raise IndexError("Vector index out of range")
        
        def __iter__(self):
            """迭代器"""
            return iter([self.x, self.y])
        
        def __call__(self):
            """使实例可调用"""
            return (self.x ** 2 + self.y ** 2) ** 0.5
    
    # 使用特殊方法
    print("特殊方法示例：")
    
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print(f"v1: {v1}")
    print(f"v2: {v2}")
    
    # 算术运算
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"3 * v1 = {3 * v1}")
    
    # 比较运算
    print(f"v1 == v2: {v1 == v2}")
    print(f"v1 == Vector(3, 4): {v1 == Vector(3, 4)}")
    
    # 长度和索引
    print(f"len(v1): {len(v1)}")
    print(f"v1[0]: {v1[0]}, v1[1]: {v1[1]}")
    
    # 迭代和调用
    print(f"迭代v1: {list(v1)}")
    print(f"调用v1(): {v1()}")
    print()
    
    # 4. 描述符(descriptor)
    print("4. 描述符(descriptor)")
    print("-" * 30)
    
    class Validator:
        """验证器描述符"""
        
        def __init__(self, min_value=None, max_value=None):
            self.min_value = min_value
            self.max_value = max_value
        
        def __set_name__(self, owner, name):
            """设置属性名"""
            self.name = name
        
        def __get__(self, instance, owner):
            """获取属性值"""
            if instance is None:
                return self
            return instance.__dict__.get(self.name)
        
        def __set__(self, instance, value):
            """设置属性值"""
            if self.min_value is not None and value < self.min_value:
                raise ValueError(f"{self.name} must be >= {self.min_value}")
            if self.max_value is not None and value > self.max_value:
                raise ValueError(f"{self.name} must be <= {self.max_value}")
            instance.__dict__[self.name] = value
    
    class Temperature:
        """温度类 - 使用描述符验证"""
        
        celsius = Validator(min_value=-273.15, max_value=None)
        fahrenheit = Validator(min_value=-459.67, max_value=None)
        
        def __init__(self, celsius=0):
            self.celsius = celsius
        
        @property
        def fahrenheit(self):
            """摄氏度转华氏度"""
            return self.celsius * 9/5 + 32
        
        @fahrenheit.setter
        def fahrenheit(self, value):
            """华氏度转摄氏度"""
            self.celsius = (value - 32) * 5/9
    
    # 使用描述符
    print("描述符示例：")
    
    temp = Temperature(25)
    print(f"摄氏度: {temp.celsius}°C")
    print(f"华氏度: {temp.fahrenheit}°F")
    
    # 验证器生效
    try:
        temp.celsius = -300  # 低于绝对零度
    except ValueError as e:
        print(f"错误: {e}")
    
    temp.fahrenheit = 100
    print(f"华氏度100°F = 摄氏度{temp.celsius:.1f}°C")
    print()
    
    # 5. 上下文管理器
    print("5. 上下文管理器")
    print("-" * 30)
    
    class FileManager:
        """文件管理器 - 上下文管理器"""
        
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode
            self.file = None
        
        def __enter__(self):
            """进入上下文"""
            print(f"打开文件: {self.filename}")
            self.file = open(self.filename, self.mode)
            return self.file
        
        def __exit__(self, exc_type, exc_value, traceback):
            """退出上下文"""
            if self.file:
                print(f"关闭文件: {self.filename}")
                self.file.close()
            if exc_type is not None:
                print(f"处理异常: {exc_type.__name__}: {exc_value}")
            return False  # 不抑制异常
    
    class Timer:
        """计时器上下文管理器"""
        
        def __init__(self, name="Operation"):
            self.name = name
            self.start_time = None
        
        def __enter__(self):
            """开始计时"""
            import time
            self.start_time = time.time()
            print(f"开始计时: {self.name}")
            return self
        
        def __exit__(self, exc_type, exc_value, traceback):
            """结束计时"""
            import time
            end_time = time.time()
            duration = end_time - self.start_time
            print(f"结束计时: {self.name}, 耗时: {duration:.4f}秒")
            return False
    
    # 使用上下文管理器
    print("上下文管理器示例：")
    
    # 创建临时文件进行演示
    with FileManager("temp.txt", "w") as f:
        f.write("Hello, World!")
    
    with FileManager("temp.txt", "r") as f:
        content = f.read()
        print(f"文件内容: {content}")
    
    # 计时器
    with Timer("数据处理"):
        import time
        time.sleep(0.1)  # 模拟耗时操作
    
    # 清理临时文件
    import os
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")
    print()
    
    # 6. 类装饰器
    print("6. 类装饰器")
    print("-" * 30)
    
    def singleton(cls):
        """单例装饰器"""
        instances = {}
        def get_instance(*args, **kwargs):
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
            return instances[cls]
        return get_instance
    
    def logged(cls):
        """日志装饰器"""
        original_init = cls.__init__
        
        def new_init(self, *args, **kwargs):
            print(f"创建 {cls.__name__} 实例")
            original_init(self, *args, **kwargs)
        
        cls.__init__ = new_init
        return cls
    
    @singleton
    class DatabaseConnection:
        """数据库连接（单例）"""
        
        def __init__(self, host, port):
            self.host = host
            self.port = port
            print(f"连接到数据库: {host}:{port}")
        
        def query(self, sql):
            print(f"执行查询: {sql}")
    
    @logged
    class Product:
        """产品类（带日志）"""
        
        def __init__(self, name, price):
            self.name = name
            self.price = price
    
    # 使用类装饰器
    print("类装饰器示例：")
    
    # 单例模式
    db1 = DatabaseConnection("localhost", 5432)
    db2 = DatabaseConnection("localhost", 5432)
    print(f"db1 is db2: {db1 is db2}")  # 应该是True
    
    # 日志装饰器
    product = Product("Laptop", 1500)
    print(f"产品: {product.name}, 价格: {product.price}")
    print()
    
    # 7. 数据类(dataclass)
    print("7. 数据类(dataclass)")
    print("-" * 30)
    
    from dataclasses import dataclass, field
    from typing import List
    
    @dataclass
    class Point:
        """点类（数据类）"""
        x: float
        y: float
        
        def distance_to(self, other):
            """计算到另一个点的距离"""
            return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
    @dataclass
    class Student:
        """学生类（数据类）"""
        name: str
        age: int
        grades: List[float] = field(default_factory=list)
        average: float = field(init=False)
        
        def __post_init__(self):
            """初始化后处理"""
            self.average = sum(self.grades) / len(self.grades) if self.grades else 0
        
        def add_grade(self, grade):
            """添加成绩"""
            self.grades.append(grade)
            self.average = sum(self.grades) / len(self.grades)
    
    @dataclass(frozen=True)
    class ImmutablePoint:
        """不可变点类"""
        x: float
        y: float
    
    # 使用数据类
    print("数据类示例：")
    
    # 基本数据类
    p1 = Point(1.0, 2.0)
    p2 = Point(4.0, 6.0)
    print(f"p1: {p1}")
    print(f"p2: {p2}")
    print(f"距离: {p1.distance_to(p2):.2f}")
    
    # 带默认值的数据类
    student = Student("Alice", 20, [85, 90, 88])
    print(f"学生: {student}")
    print(f"平均分: {student.average:.1f}")
    
    student.add_grade(92)
    print(f"添加成绩后平均分: {student.average:.1f}")
    
    # 不可变数据类
    immutable_p = ImmutablePoint(1.0, 2.0)
    print(f"不可变点: {immutable_p}")
    
    try:
        immutable_p.x = 5.0  # 这会报错
    except AttributeError as e:
        print(f"错误: {e}")
    print()
    
    # 8. 元类(metaclass)
    print("8. 元类(metaclass)")
    print("-" * 30)
    
    class SingletonMeta(type):
        """单例元类"""
        _instances = {}
        
        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]
    
    class Logger(metaclass=SingletonMeta):
        """日志记录器（使用元类实现单例）"""
        
        def __init__(self):
            self.logs = []
        
        def log(self, message):
            """记录日志"""
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.logs.append(f"[{timestamp}] {message}")
            print(f"[{timestamp}] {message}")
        
        def get_logs(self):
            """获取所有日志"""
            return self.logs
    
    class AttributeTracker(type):
        """属性跟踪元类"""
        
        def __new__(cls, name, bases, attrs):
            # 添加属性跟踪
            attrs['_attribute_access_count'] = {}
            
            # 包装所有方法
            for key, value in attrs.items():
                if callable(value) and not key.startswith('_'):
                    attrs[key] = cls._wrap_method(value, key)
            
            return super().__new__(cls, name, bases, attrs)
        
        @staticmethod
        def _wrap_method(method, method_name):
            """包装方法以跟踪访问"""
            def wrapper(self, *args, **kwargs):
                if method_name not in self._attribute_access_count:
                    self._attribute_access_count[method_name] = 0
                self._attribute_access_count[method_name] += 1
                return method(self, *args, **kwargs)
            return wrapper
    
    class TrackedClass(metaclass=AttributeTracker):
        """被跟踪的类"""
        
        def method_a(self):
            """方法A"""
            print("调用方法A")
        
        def method_b(self):
            """方法B"""
            print("调用方法B")
        
        def get_access_stats(self):
            """获取访问统计"""
            return self._attribute_access_count
    
    # 使用元类
    print("元类示例：")
    
    # 单例元类
    logger1 = Logger()
    logger2 = Logger()
    print(f"logger1 is logger2: {logger1 is logger2}")
    
    logger1.log("测试消息1")
    logger2.log("测试消息2")
    print(f"日志数量: {len(logger1.get_logs())}")
    
    # 属性跟踪元类
    tracked = TrackedClass()
    tracked.method_a()
    tracked.method_a()
    tracked.method_b()
    print(f"方法调用统计: {tracked.get_access_stats()}")
    print()
    
    print("高级特性总结：")
    print("1. @property - 将方法转换为属性")
    print("2. @classmethod/@staticmethod - 类方法和静态方法")
    print("3. 特殊方法 - 自定义对象行为")
    print("4. 描述符 - 控制属性访问")
    print("5. 上下文管理器 - 资源管理")
    print("6. 类装饰器 - 修改类行为")
    print("7. 数据类 - 简化数据存储类")
    print("8. 元类 - 控制类的创建过程")
    print()
    
    print("=== 类的高级特性演示完成 ===")


if __name__ == "__main__":
    main() 