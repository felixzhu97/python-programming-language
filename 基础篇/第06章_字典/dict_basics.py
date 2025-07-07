#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第06章 字典 - 字典基础操作
演示字典的创建、访问、修改和删除操作
"""

def main():
    print("=== 字典基础操作演示 ===\n")
    
    # 1. 创建字典
    print("1. 创建字典")
    print("-" * 30)
    
    # 简单的字典
    alien_0 = {'color': 'green', 'points': 5}
    print(f"外星人信息：{alien_0}")
    print(f"字典类型：{type(alien_0)}")
    print()
    
    # 不同数据类型的字典
    mixed_dict = {
        'name': 'Alice',
        'age': 25,
        'height': 1.65,
        'is_student': True,
        'courses': ['Math', 'Physics'],
        'address': {'city': 'Beijing', 'zip': '100000'}
    }
    print(f"混合类型字典：{mixed_dict}")
    print()
    
    # 空字典
    empty_dict = {}
    print(f"空字典：{empty_dict}")
    print(f"空字典长度：{len(empty_dict)}")
    print()
    
    # 2. 访问字典中的值
    print("2. 访问字典中的值")
    print("-" * 30)
    
    # 直接访问
    print(f"外星人颜色：{alien_0['color']}")
    print(f"外星人得分：{alien_0['points']}")
    print()
    
    # 获取新玩家的得分
    new_points = alien_0['points']
    print(f"你刚获得了{new_points}个点！")
    print()
    
    # 使用get()方法
    print("使用get()方法访问：")
    print(f"颜色：{alien_0.get('color')}")
    print(f"速度：{alien_0.get('speed', '没有速度信息')}")
    print()
    
    # 3. 添加键值对
    print("3. 添加键值对")
    print("-" * 30)
    
    print(f"添加前的字典：{alien_0}")
    
    # 添加新的键值对
    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    print(f"添加坐标后：{alien_0}")
    print()
    
    # 4. 修改字典中的值
    print("4. 修改字典中的值")
    print("-" * 30)
    
    print(f"修改前的外星人：{alien_0}")
    
    # 修改外星人的颜色
    alien_0['color'] = 'yellow'
    print(f"外星人现在是{alien_0['color']}色的。")
    print()
    
    # 追踪外星人的位置
    print("外星人移动演示：")
    alien_0['speed'] = 'medium'
    print(f"原始位置：x={alien_0['x_position']}")
    
    # 根据速度移动外星人
    if alien_0['speed'] == 'slow':
        x_increment = 1
    elif alien_0['speed'] == 'medium':
        x_increment = 2
    else:  # fast
        x_increment = 3
    
    alien_0['x_position'] += x_increment
    print(f"新位置：x={alien_0['x_position']}")
    print()
    
    # 5. 删除键值对
    print("5. 删除键值对")
    print("-" * 30)
    
    print(f"删除前的字典：{alien_0}")
    
    # 使用del语句删除
    del alien_0['points']
    print(f"删除points后：{alien_0}")
    
    # 使用pop()方法删除
    speed = alien_0.pop('speed')
    print(f"删除的速度：{speed}")
    print(f"删除speed后：{alien_0}")
    
    # 使用popitem()删除最后一个键值对
    last_item = alien_0.popitem()
    print(f"删除的最后一项：{last_item}")
    print(f"删除最后一项后：{alien_0}")
    print()
    
    # 6. 字典的复制
    print("6. 字典的复制")
    print("-" * 30)
    
    original = {'a': 1, 'b': 2, 'c': 3}
    print(f"原始字典：{original}")
    
    # 浅拷贝
    shallow_copy = original.copy()
    print(f"浅拷贝：{shallow_copy}")
    
    # 使用dict()构造器复制
    dict_copy = dict(original)
    print(f"dict()复制：{dict_copy}")
    
    # 修改原始字典
    original['d'] = 4
    print(f"修改后原始字典：{original}")
    print(f"拷贝字典不变：{shallow_copy}")
    print()
    
    # 7. 字典的长度和成员检查
    print("7. 字典的长度和成员检查")
    print("-" * 30)
    
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'
    }
    
    print(f"编程语言偏好：{favorite_languages}")
    print(f"字典长度：{len(favorite_languages)}")
    print()
    
    # 检查键是否存在
    print("检查键是否存在：")
    print(f"'jen' in favorite_languages: {'jen' in favorite_languages}")
    print(f"'alice' in favorite_languages: {'alice' in favorite_languages}")
    print()
    
    # 检查值是否存在
    print("检查值是否存在：")
    print(f"'python' in favorite_languages.values(): {'python' in favorite_languages.values()}")
    print(f"'java' in favorite_languages.values(): {'java' in favorite_languages.values()}")
    print()
    
    # 8. 字典的keys()、values()和items()
    print("8. 字典的keys()、values()和items()")
    print("-" * 30)
    
    print(f"原字典：{favorite_languages}")
    print()
    
    # 获取所有键
    keys = favorite_languages.keys()
    print(f"所有键：{list(keys)}")
    print(f"键的类型：{type(keys)}")
    print()
    
    # 获取所有值
    values = favorite_languages.values()
    print(f"所有值：{list(values)}")
    print(f"值的类型：{type(values)}")
    print()
    
    # 获取所有键值对
    items = favorite_languages.items()
    print(f"所有键值对：{list(items)}")
    print(f"键值对的类型：{type(items)}")
    print()
    
    # 9. 字典的更新
    print("9. 字典的更新")
    print("-" * 30)
    
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    
    print(f"字典1：{dict1}")
    print(f"字典2：{dict2}")
    
    # 使用update()方法
    dict1.update(dict2)
    print(f"更新后的字典1：{dict1}")
    print()
    
    # 使用字典推导式更新
    dict3 = {'d': 5, 'e': 6}
    dict1.update({k: v for k, v in dict3.items()})
    print(f"再次更新后的字典1：{dict1}")
    print()
    
    # 10. 字典的清空
    print("10. 字典的清空")
    print("-" * 30)
    
    test_dict = {'x': 1, 'y': 2, 'z': 3}
    print(f"清空前：{test_dict}")
    
    test_dict.clear()
    print(f"清空后：{test_dict}")
    print()
    
    # 11. 嵌套字典
    print("11. 嵌套字典")
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
    
    print("用户信息：")
    for username, user_info in users.items():
        print(f"\n用户名：{username}")
        full_name = f"{user_info['first']} {user_info['last']}"
        location = user_info['location']
        print(f"全名：{full_name.title()}")
        print(f"位置：{location.title()}")
    print()
    
    # 12. 字典的实际应用示例
    print("12. 字典的实际应用示例")
    print("-" * 30)
    
    # 学生成绩管理
    def student_grade_system():
        """学生成绩管理系统"""
        students = {
            'Alice': {'math': 95, 'physics': 87, 'chemistry': 92},
            'Bob': {'math': 78, 'physics': 82, 'chemistry': 75},
            'Charlie': {'math': 88, 'physics': 91, 'chemistry': 85}
        }
        
        print("学生成绩管理系统")
        print("=" * 20)
        
        # 添加新学生
        students['David'] = {'math': 90, 'physics': 85, 'chemistry': 88}
        
        # 计算每个学生的平均分
        for name, scores in students.items():
            average = sum(scores.values()) / len(scores)
            print(f"{name}: 平均分 {average:.1f}")
            
            # 找出最高分科目
            best_subject = max(scores, key=scores.get)
            print(f"  最佳科目: {best_subject} ({scores[best_subject]}分)")
        
        # 计算每科的平均分
        print("\n各科平均分:")
        subjects = ['math', 'physics', 'chemistry']
        for subject in subjects:
            subject_scores = [scores[subject] for scores in students.values()]
            avg_score = sum(subject_scores) / len(subject_scores)
            print(f"{subject}: {avg_score:.1f}")
    
    student_grade_system()
    print()
    
    # 购物车系统
    def shopping_cart_system():
        """购物车系统"""
        cart = {}
        
        print("购物车系统")
        print("=" * 20)
        
        # 添加商品
        def add_item(item, price, quantity=1):
            if item in cart:
                cart[item]['quantity'] += quantity
            else:
                cart[item] = {'price': price, 'quantity': quantity}
        
        # 添加一些商品
        add_item('apple', 5.0, 3)
        add_item('banana', 3.0, 6)
        add_item('orange', 4.0, 2)
        add_item('apple', 5.0, 2)  # 增加苹果数量
        
        # 显示购物车
        print("购物车内容:")
        total = 0
        for item, details in cart.items():
            subtotal = details['price'] * details['quantity']
            total += subtotal
            print(f"{item}: ¥{details['price']} × {details['quantity']} = ¥{subtotal:.2f}")
        
        print(f"\n总计: ¥{total:.2f}")
        
        # 删除商品
        if 'banana' in cart:
            del cart['banana']
            print("已删除banana")
        
        # 重新计算总计
        total = sum(details['price'] * details['quantity'] for details in cart.values())
        print(f"删除后总计: ¥{total:.2f}")
    
    shopping_cart_system()
    print()
    
    # 13. 字典的性能特点
    print("13. 字典的性能特点")
    print("-" * 30)
    
    import time
    
    # 创建大字典测试性能
    large_dict = {f'key_{i}': i for i in range(10000)}
    
    # 测试访问性能
    start_time = time.time()
    for i in range(1000):
        value = large_dict.get(f'key_{i}')
    end_time = time.time()
    
    print(f"字典访问1000次用时：{(end_time - start_time) * 1000:.2f}毫秒")
    print("字典的平均访问时间复杂度为O(1)")
    print()
    
    # 14. 字典的常见用法总结
    print("14. 字典的常见用法总结")
    print("-" * 30)
    
    print("字典的常见用法：")
    print("1. 存储相关联的信息")
    print("2. 建立映射关系")
    print("3. 计数和统计")
    print("4. 缓存计算结果")
    print("5. 配置设置")
    print("6. 数据库记录的表示")
    print("7. 实现简单的查找表")
    print()
    
    # 计数示例
    text = "hello world hello python"
    word_count = {}
    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1
    
    print(f"单词计数：{word_count}")


if __name__ == "__main__":
    main() 