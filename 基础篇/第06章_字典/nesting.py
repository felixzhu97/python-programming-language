#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第06章 字典 - 嵌套结构
演示字典、列表和嵌套结构的复杂应用
"""

def main():
    print("=== 嵌套结构演示 ===\n")
    
    # 1. 字典列表（多个字典组成的列表）
    print("1. 字典列表（多个字典组成的列表）")
    print("-" * 30)
    
    # 创建一个外星人列表
    alien_0 = {'color': 'green', 'points': 5}
    alien_1 = {'color': 'yellow', 'points': 10}
    alien_2 = {'color': 'red', 'points': 15}
    
    aliens = [alien_0, alien_1, alien_2]
    
    print("外星人列表：")
    for alien in aliens:
        print(alien)
    print()
    
    # 创建更大的外星人舰队
    print("创建大外星人舰队：")
    aliens = []
    
    # 创建30个绿色外星人
    for alien_number in range(30):
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
        aliens.append(new_alien)
    
    # 显示前5个外星人
    print("前5个外星人：")
    for alien in aliens[:5]:
        print(alien)
    print("...")
    
    print(f"外星人总数：{len(aliens)}")
    print()
    
    # 修改外星人
    print("修改外星人舰队：")
    for alien in aliens[:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10
            break
    
    # 显示修改后的前5个外星人
    print("修改后的前5个外星人：")
    for alien in aliens[:5]:
        print(alien)
    print("...")
    print()
    
    # 2. 在字典中存储列表
    print("2. 在字典中存储列表")
    print("-" * 30)
    
    # 存储所点披萨的信息
    pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
    }
    
    # 概述所点的披萨
    print(f"你点了一个{pizza['crust']}面皮的披萨，")
    print("配料有：")
    for topping in pizza['toppings']:
        print(f"  {topping}")
    print()
    
    # 更复杂的示例：存储多个人的语言偏好
    favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell'],
    }
    
    print("每个人的语言偏好：")
    for name, languages in favorite_languages.items():
        print(f"\n{name.title()}的喜欢的语言是：")
        for language in languages:
            print(f"  {language.title()}")
    print()
    
    # 3. 在字典中存储字典
    print("3. 在字典中存储字典")
    print("-" * 30)
    
    users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
        },
        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
        }
    }
    
    print("用户详细信息：")
    for username, user_info in users.items():
        print(f"\n用户名：{username}")
        full_name = f"{user_info['first']} {user_info['last']}"
        location = user_info['location']
        print(f"  全名：{full_name.title()}")
        print(f"  位置：{location.title()}")
    print()
    
    # 4. 复杂的嵌套结构
    print("4. 复杂的嵌套结构")
    print("-" * 30)
    
    # 学校管理系统
    school = {
        'name': 'Python高中',
        'address': {
            'street': '编程大道123号',
            'city': '代码城',
            'zip': '100001'
        },
        'classes': {
            'class_1a': {
                'teacher': '张老师',
                'students': [
                    {'name': '小明', 'age': 16, 'subjects': ['数学', '物理', '化学']},
                    {'name': '小红', 'age': 15, 'subjects': ['数学', '英语', '历史']},
                    {'name': '小刚', 'age': 16, 'subjects': ['数学', '物理', '编程']}
                ]
            },
            'class_1b': {
                'teacher': '李老师',
                'students': [
                    {'name': '小花', 'age': 15, 'subjects': ['数学', '生物', '化学']},
                    {'name': '小强', 'age': 16, 'subjects': ['数学', '物理', '编程']}
                ]
            }
        }
    }
    
    print(f"学校名称：{school['name']}")
    print(f"学校地址：{school['address']['street']}, {school['address']['city']}")
    print()
    
    print("班级信息：")
    for class_name, class_info in school['classes'].items():
        print(f"\n{class_name}班：")
        print(f"  老师：{class_info['teacher']}")
        print(f"  学生：")
        for student in class_info['students']:
            print(f"    {student['name']}（{student['age']}岁）")
            print(f"    科目：{', '.join(student['subjects'])}")
    print()
    
    # 5. 实际应用：电商系统
    print("5. 实际应用：电商系统")
    print("-" * 30)
    
    ecommerce_system = {
        'users': {
            'user_001': {
                'name': '张三',
                'email': 'zhangsan@example.com',
                'address': {
                    'street': '北京路123号',
                    'city': '北京',
                    'zip': '100000'
                },
                'orders': [
                    {
                        'order_id': 'ORD001',
                        'date': '2023-01-15',
                        'items': [
                            {'name': '苹果', 'price': 5.0, 'quantity': 3},
                            {'name': '香蕉', 'price': 3.0, 'quantity': 2}
                        ],
                        'total': 21.0,
                        'status': 'delivered'
                    },
                    {
                        'order_id': 'ORD002',
                        'date': '2023-01-20',
                        'items': [
                            {'name': '橙子', 'price': 4.0, 'quantity': 5}
                        ],
                        'total': 20.0,
                        'status': 'shipped'
                    }
                ]
            },
            'user_002': {
                'name': '李四',
                'email': 'lisi@example.com',
                'address': {
                    'street': '上海路456号',
                    'city': '上海',
                    'zip': '200000'
                },
                'orders': [
                    {
                        'order_id': 'ORD003',
                        'date': '2023-01-22',
                        'items': [
                            {'name': '葡萄', 'price': 8.0, 'quantity': 1},
                            {'name': '西瓜', 'price': 12.0, 'quantity': 1}
                        ],
                        'total': 20.0,
                        'status': 'processing'
                    }
                ]
            }
        }
    }
    
    print("电商系统数据：")
    for user_id, user_data in ecommerce_system['users'].items():
        print(f"\n用户ID：{user_id}")
        print(f"姓名：{user_data['name']}")
        print(f"邮箱：{user_data['email']}")
        print(f"地址：{user_data['address']['street']}, {user_data['address']['city']}")
        
        print("订单历史：")
        for order in user_data['orders']:
            print(f"  订单号：{order['order_id']}")
            print(f"  日期：{order['date']}")
            print(f"  状态：{order['status']}")
            print(f"  商品：")
            for item in order['items']:
                print(f"    {item['name']}: ¥{item['price']} × {item['quantity']}")
            print(f"  总计：¥{order['total']}")
    print()
    
    # 6. 嵌套结构的操作
    print("6. 嵌套结构的操作")
    print("-" * 30)
    
    # 添加新用户
    new_user = {
        'name': '王五',
        'email': 'wangwu@example.com',
        'address': {
            'street': '广州路789号',
            'city': '广州',
            'zip': '510000'
        },
        'orders': []
    }
    
    ecommerce_system['users']['user_003'] = new_user
    print(f"添加新用户：{new_user['name']}")
    
    # 为用户添加新订单
    new_order = {
        'order_id': 'ORD004',
        'date': '2023-01-25',
        'items': [
            {'name': '芒果', 'price': 10.0, 'quantity': 2}
        ],
        'total': 20.0,
        'status': 'processing'
    }
    
    ecommerce_system['users']['user_003']['orders'].append(new_order)
    print(f"为用户{new_user['name']}添加新订单：{new_order['order_id']}")
    
    # 修改订单状态
    ecommerce_system['users']['user_003']['orders'][0]['status'] = 'shipped'
    print(f"订单状态更新为：{ecommerce_system['users']['user_003']['orders'][0]['status']}")
    print()
    
    # 7. 嵌套结构的搜索和统计
    print("7. 嵌套结构的搜索和统计")
    print("-" * 30)
    
    # 统计总订单数
    total_orders = 0
    for user_data in ecommerce_system['users'].values():
        total_orders += len(user_data['orders'])
    print(f"总订单数：{total_orders}")
    
    # 统计总销售额
    total_sales = 0
    for user_data in ecommerce_system['users'].values():
        for order in user_data['orders']:
            total_sales += order['total']
    print(f"总销售额：¥{total_sales}")
    
    # 按城市统计用户
    city_stats = {}
    for user_data in ecommerce_system['users'].values():
        city = user_data['address']['city']
        if city in city_stats:
            city_stats[city] += 1
        else:
            city_stats[city] = 1
    
    print("按城市统计用户：")
    for city, count in city_stats.items():
        print(f"  {city}: {count}个用户")
    print()
    
    # 8. 嵌套结构的深拷贝
    print("8. 嵌套结构的深拷贝")
    print("-" * 30)
    
    import copy
    
    # 浅拷贝
    shallow_copy = ecommerce_system.copy()
    print("浅拷贝创建完成")
    
    # 深拷贝
    deep_copy = copy.deepcopy(ecommerce_system)
    print("深拷贝创建完成")
    
    # 修改原始数据
    ecommerce_system['users']['user_001']['name'] = '张三三'
    
    print(f"原始数据：{ecommerce_system['users']['user_001']['name']}")
    print(f"浅拷贝：{shallow_copy['users']['user_001']['name']}")
    print(f"深拷贝：{deep_copy['users']['user_001']['name']}")
    print()
    
    # 9. 嵌套结构的JSON操作
    print("9. 嵌套结构的JSON操作")
    print("-" * 30)
    
    import json
    
    # 转换为JSON字符串
    json_string = json.dumps(deep_copy, ensure_ascii=False, indent=2)
    print("JSON字符串（前200字符）：")
    print(json_string[:200] + "...")
    
    # 从JSON字符串还原
    restored_data = json.loads(json_string)
    print(f"从JSON还原的数据类型：{type(restored_data)}")
    print(f"还原后的用户数量：{len(restored_data['users'])}")
    print()
    
    # 10. 嵌套结构的验证
    print("10. 嵌套结构的验证")
    print("-" * 30)
    
    def validate_user_data(user_data):
        """验证用户数据的完整性"""
        required_fields = ['name', 'email', 'address', 'orders']
        
        for field in required_fields:
            if field not in user_data:
                return False, f"缺少必需字段：{field}"
        
        # 验证地址信息
        address = user_data['address']
        required_address_fields = ['street', 'city', 'zip']
        for field in required_address_fields:
            if field not in address:
                return False, f"地址缺少必需字段：{field}"
        
        # 验证订单信息
        for order in user_data['orders']:
            required_order_fields = ['order_id', 'date', 'items', 'total', 'status']
            for field in required_order_fields:
                if field not in order:
                    return False, f"订单缺少必需字段：{field}"
        
        return True, "数据验证通过"
    
    # 验证所有用户数据
    print("用户数据验证：")
    for user_id, user_data in ecommerce_system['users'].items():
        is_valid, message = validate_user_data(user_data)
        status = "✓" if is_valid else "✗"
        print(f"{status} {user_id}: {message}")
    print()
    
    # 11. 嵌套结构的性能优化
    print("11. 嵌套结构的性能优化")
    print("-" * 30)
    
    import time
    
    # 创建大量嵌套数据
    large_nested_data = {}
    for i in range(1000):
        large_nested_data[f'user_{i}'] = {
            'name': f'用户{i}',
            'data': {
                'scores': [j for j in range(100)],
                'metadata': {
                    'created': f'2023-01-{(i % 28) + 1:02d}',
                    'updated': f'2023-02-{(i % 28) + 1:02d}'
                }
            }
        }
    
    # 测试访问性能
    start_time = time.time()
    for user_id, user_data in large_nested_data.items():
        # 访问嵌套数据
        scores = user_data['data']['scores']
        created = user_data['data']['metadata']['created']
    end_time = time.time()
    
    print(f"访问1000个嵌套结构用时：{(end_time - start_time) * 1000:.2f}毫秒")
    print()
    
    # 12. 嵌套结构的最佳实践
    print("12. 嵌套结构的最佳实践")
    print("-" * 30)
    
    print("嵌套结构的最佳实践：")
    print("1. 保持结构简单和一致")
    print("2. 使用有意义的键名")
    print("3. 考虑数据的访问模式")
    print("4. 适当使用深拷贝")
    print("5. 验证数据完整性")
    print("6. 注意性能影响")
    print("7. 考虑使用类来封装复杂结构")
    print("8. 文档化数据结构")
    print()
    
    # 13. 嵌套结构的实用函数
    print("13. 嵌套结构的实用函数")
    print("-" * 30)
    
    def get_nested_value(data, keys, default=None):
        """安全地获取嵌套字典的值"""
        for key in keys:
            if isinstance(data, dict) and key in data:
                data = data[key]
            else:
                return default
        return data
    
    def set_nested_value(data, keys, value):
        """设置嵌套字典的值"""
        for key in keys[:-1]:
            if key not in data:
                data[key] = {}
            data = data[key]
        data[keys[-1]] = value
    
    def flatten_dict(data, parent_key='', sep='_'):
        """扁平化嵌套字典"""
        items = []
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                items.extend(flatten_dict(value, new_key, sep=sep).items())
            else:
                items.append((new_key, value))
        return dict(items)
    
    # 测试实用函数
    test_data = {
        'user': {
            'profile': {
                'name': '测试用户',
                'age': 25
            },
            'settings': {
                'theme': 'dark',
                'notifications': True
            }
        }
    }
    
    # 获取嵌套值
    name = get_nested_value(test_data, ['user', 'profile', 'name'])
    print(f"获取嵌套值：{name}")
    
    # 设置嵌套值
    set_nested_value(test_data, ['user', 'profile', 'location'], '北京')
    print(f"设置后的数据：{test_data}")
    
    # 扁平化字典
    flattened = flatten_dict(test_data)
    print(f"扁平化后的字典：{flattened}")


if __name__ == "__main__":
    main() 