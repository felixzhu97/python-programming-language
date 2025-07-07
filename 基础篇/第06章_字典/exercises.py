#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第06章 字典 - 练习题解答
包含第6章所有练习题的详细解答
"""

def main():
    print("=== 第06章 字典 - 练习题解答 ===\n")
    
    # 练习 6-1：人
    print("练习 6-1：人")
    print("-" * 30)
    
    person = {
        'first_name': '张',
        'last_name': '三',
        'age': 25,
        'city': '北京'
    }
    
    print(f"姓名：{person['first_name']}{person['last_name']}")
    print(f"年龄：{person['age']}")
    print(f"城市：{person['city']}")
    print()
    
    # 练习 6-2：喜欢的数字
    print("练习 6-2：喜欢的数字")
    print("-" * 30)
    
    favorite_numbers = {
        '张三': 7,
        '李四': 42,
        '王五': 13,
        '赵六': 88,
        '钱七': 3
    }
    
    for name, number in favorite_numbers.items():
        print(f"{name}喜欢的数字是{number}。")
    print()
    
    # 练习 6-3：词汇表
    print("练习 6-3：词汇表")
    print("-" * 30)
    
    glossary = {
        'string': '字符串，用于存储文本数据',
        'list': '列表，用于存储多个有序的元素',
        'dictionary': '字典，用于存储键值对数据',
        'loop': '循环，用于重复执行代码块',
        'function': '函数，用于封装可重复使用的代码'
    }
    
    for term, definition in glossary.items():
        print(f"{term}: {definition}")
    print()
    
    # 练习 6-4：词汇表2
    print("练习 6-4：词汇表2")
    print("-" * 30)
    
    # 添加更多词汇
    glossary['variable'] = '变量，用于存储数据的容器'
    glossary['boolean'] = '布尔值，只能是True或False'
    glossary['tuple'] = '元组，不可变的有序元素集合'
    glossary['set'] = '集合，存储唯一元素的无序集合'
    glossary['class'] = '类，用于创建对象的模板'
    
    # 使用更好的格式打印
    print("编程词汇表：")
    print("=" * 50)
    for term, definition in glossary.items():
        print(f"\n{term.upper()}:")
        print(f"  {definition}")
    print()
    
    # 练习 6-5：河流
    print("练习 6-5：河流")
    print("-" * 30)
    
    rivers = {
        'nile': 'egypt',
        'amazon': 'brazil',
        'yangtze': 'china',
        'mississippi': 'united states',
        'yellow': 'china'
    }
    
    # 显示河流和流经的国家
    for river, country in rivers.items():
        print(f"The {river.title()} runs through {country.title()}.")
    
    print("\n河流列表：")
    for river in rivers.keys():
        print(f"  {river.title()}")
    
    print("\n国家列表：")
    for country in set(rivers.values()):
        print(f"  {country.title()}")
    print()
    
    # 练习 6-6：调查
    print("练习 6-6：调查")
    print("-" * 30)
    
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'
    }
    
    people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'alice', 'bob']
    
    for person in people_to_poll:
        if person in favorite_languages:
            print(f"{person.title()}，感谢你参与了我们的调查！")
        else:
            print(f"{person.title()}，请参与我们的调查！")
    print()
    
    # 练习 6-7：人
    print("练习 6-7：人")
    print("-" * 30)
    
    people = []
    
    person1 = {
        'first_name': '张',
        'last_name': '三',
        'age': 25,
        'city': '北京'
    }
    
    person2 = {
        'first_name': '李',
        'last_name': '四',
        'age': 30,
        'city': '上海'
    }
    
    person3 = {
        'first_name': '王',
        'last_name': '五',
        'age': 28,
        'city': '广州'
    }
    
    people.extend([person1, person2, person3])
    
    for person in people:
        print(f"姓名：{person['first_name']}{person['last_name']}")
        print(f"年龄：{person['age']}")
        print(f"城市：{person['city']}")
        print()
    
    # 练习 6-8：宠物
    print("练习 6-8：宠物")
    print("-" * 30)
    
    pets = []
    
    pet1 = {
        'name': '旺财',
        'type': '狗',
        'owner': '张三'
    }
    
    pet2 = {
        'name': '咪咪',
        'type': '猫',
        'owner': '李四'
    }
    
    pet3 = {
        'name': '小白',
        'type': '兔子',
        'owner': '王五'
    }
    
    pets.extend([pet1, pet2, pet3])
    
    for pet in pets:
        print(f"宠物名：{pet['name']}")
        print(f"类型：{pet['type']}")
        print(f"主人：{pet['owner']}")
        print()
    
    # 练习 6-9：喜欢的地方
    print("练习 6-9：喜欢的地方")
    print("-" * 30)
    
    favorite_places = {
        '张三': ['北京', '上海', '杭州'],
        '李四': ['成都', '重庆'],
        '王五': ['广州', '深圳', '珠海', '厦门']
    }
    
    for name, places in favorite_places.items():
        print(f"{name}喜欢的地方：")
        for place in places:
            print(f"  {place}")
        print()
    
    # 练习 6-10：喜欢的数字
    print("练习 6-10：喜欢的数字")
    print("-" * 30)
    
    favorite_numbers = {
        '张三': [7, 14, 21],
        '李四': [42],
        '王五': [13, 26, 39],
        '赵六': [88, 99],
        '钱七': [3, 6, 9, 12]
    }
    
    for name, numbers in favorite_numbers.items():
        print(f"{name}喜欢的数字：")
        for number in numbers:
            print(f"  {number}")
        print()
    
    # 练习 6-11：城市
    print("练习 6-11：城市")
    print("-" * 30)
    
    cities = {
        'beijing': {
            'country': 'china',
            'population': 21540000,
            'fact': 'Beijing is the capital of China'
        },
        'tokyo': {
            'country': 'japan',
            'population': 37400000,
            'fact': 'Tokyo is the most populous metropolitan area in the world'
        },
        'new york': {
            'country': 'united states',
            'population': 8400000,
            'fact': 'New York City is known as the Big Apple'
        }
    }
    
    for city, info in cities.items():
        print(f"城市：{city.title()}")
        print(f"  国家：{info['country'].title()}")
        print(f"  人口：{info['population']:,}")
        print(f"  趣事：{info['fact']}")
        print()
    
    # 练习 6-12：扩展
    print("练习 6-12：扩展")
    print("-" * 30)
    
    # 扩展前面的练习，添加更多内容
    
    # 扩展词汇表
    extended_glossary = {
        # 基础概念
        'variable': '变量，用于存储数据的容器',
        'string': '字符串，用于存储文本数据',
        'integer': '整数，用于存储整数值',
        'float': '浮点数，用于存储小数',
        'boolean': '布尔值，只能是True或False',
        
        # 数据结构
        'list': '列表，用于存储多个有序的元素',
        'tuple': '元组，不可变的有序元素集合',
        'set': '集合，存储唯一元素的无序集合',
        'dictionary': '字典，用于存储键值对数据',
        
        # 控制结构
        'if': 'if语句，用于条件判断',
        'for': 'for循环，用于遍历序列',
        'while': 'while循环，用于重复执行直到条件为假',
        'break': 'break语句，用于跳出循环',
        'continue': 'continue语句，用于跳过当前循环迭代',
        
        # 函数相关
        'function': '函数，用于封装可重复使用的代码',
        'parameter': '参数，函数定义时的变量',
        'argument': '实参，调用函数时传递的值',
        'return': 'return语句，用于从函数返回值',
        
        # 面向对象
        'class': '类，用于创建对象的模板',
        'object': '对象，类的实例',
        'method': '方法，定义在类中的函数',
        'attribute': '属性，对象的变量',
        'inheritance': '继承，子类从父类获取属性和方法',
        
        # 异常处理
        'exception': '异常，程序运行时发生的错误',
        'try': 'try语句，用于异常处理',
        'except': 'except语句，用于捕获异常',
        'finally': 'finally语句，无论是否异常都会执行',
        
        # 文件操作
        'file': '文件，用于存储数据的容器',
        'open': 'open函数，用于打开文件',
        'read': 'read方法，用于读取文件内容',
        'write': 'write方法，用于写入文件内容',
        'close': 'close方法，用于关闭文件',
        
        # 模块和包
        'module': '模块，包含Python代码的文件',
        'package': '包，包含多个模块的文件夹',
        'import': 'import语句，用于导入模块',
        'from': 'from语句，用于从模块导入特定内容'
    }
    
    print("扩展的编程词汇表：")
    print("=" * 60)
    
    # 按类别显示
    categories = {
        '基础概念': ['variable', 'string', 'integer', 'float', 'boolean'],
        '数据结构': ['list', 'tuple', 'set', 'dictionary'],
        '控制结构': ['if', 'for', 'while', 'break', 'continue'],
        '函数相关': ['function', 'parameter', 'argument', 'return'],
        '面向对象': ['class', 'object', 'method', 'attribute', 'inheritance'],
        '异常处理': ['exception', 'try', 'except', 'finally'],
        '文件操作': ['file', 'open', 'read', 'write', 'close'],
        '模块和包': ['module', 'package', 'import', 'from']
    }
    
    for category, terms in categories.items():
        print(f"\n{category}:")
        print("-" * 30)
        for term in terms:
            if term in extended_glossary:
                print(f"{term.upper()}: {extended_glossary[term]}")
    print()
    
    # 额外练习：复杂的数据结构
    print("额外练习：复杂的数据结构")
    print("-" * 30)
    
    # 学生管理系统
    students = {
        'student_001': {
            'name': '张小明',
            'age': 18,
            'grade': '高三',
            'subjects': {
                'math': {'score': 95, 'teacher': '李老师'},
                'physics': {'score': 87, 'teacher': '王老师'},
                'chemistry': {'score': 92, 'teacher': '赵老师'}
            },
            'activities': ['篮球社', '编程社'],
            'address': {
                'street': '学府路123号',
                'city': '北京',
                'zip': '100000'
            }
        },
        'student_002': {
            'name': '李小红',
            'age': 17,
            'grade': '高二',
            'subjects': {
                'math': {'score': 78, 'teacher': '李老师'},
                'english': {'score': 95, 'teacher': '刘老师'},
                'history': {'score': 88, 'teacher': '陈老师'}
            },
            'activities': ['文学社', '志愿者'],
            'address': {
                'street': '文化路456号',
                'city': '上海',
                'zip': '200000'
            }
        }
    }
    
    print("学生管理系统：")
    print("=" * 40)
    
    for student_id, student_info in students.items():
        print(f"\n学生ID：{student_id}")
        print(f"姓名：{student_info['name']}")
        print(f"年龄：{student_info['age']}")
        print(f"年级：{student_info['grade']}")
        
        print("科目成绩：")
        total_score = 0
        subject_count = 0
        for subject, details in student_info['subjects'].items():
            score = details['score']
            teacher = details['teacher']
            print(f"  {subject}: {score}分 (任课老师: {teacher})")
            total_score += score
            subject_count += 1
        
        average_score = total_score / subject_count if subject_count > 0 else 0
        print(f"平均分：{average_score:.1f}")
        
        print("课外活动：")
        for activity in student_info['activities']:
            print(f"  - {activity}")
        
        address = student_info['address']
        print(f"地址：{address['street']}, {address['city']}, {address['zip']}")
    
    # 统计信息
    print("\n统计信息：")
    print("-" * 20)
    
    total_students = len(students)
    print(f"总学生数：{total_students}")
    
    # 按年级统计
    grade_count = {}
    for student_info in students.values():
        grade = student_info['grade']
        grade_count[grade] = grade_count.get(grade, 0) + 1
    
    print("按年级统计：")
    for grade, count in grade_count.items():
        print(f"  {grade}: {count}人")
    
    # 按城市统计
    city_count = {}
    for student_info in students.values():
        city = student_info['address']['city']
        city_count[city] = city_count.get(city, 0) + 1
    
    print("按城市统计：")
    for city, count in city_count.items():
        print(f"  {city}: {count}人")
    
    # 最受欢迎的活动
    activity_count = {}
    for student_info in students.values():
        for activity in student_info['activities']:
            activity_count[activity] = activity_count.get(activity, 0) + 1
    
    print("活动参与统计：")
    for activity, count in activity_count.items():
        print(f"  {activity}: {count}人")
    
    print("\n=== 第06章练习完成 ===")
    print("主要学习了：")
    print("1. 字典的基本操作")
    print("2. 字典的遍历方法")
    print("3. 嵌套数据结构")
    print("4. 字典在实际项目中的应用")
    print("5. 复杂数据结构的设计和操作")


if __name__ == "__main__":
    main() 