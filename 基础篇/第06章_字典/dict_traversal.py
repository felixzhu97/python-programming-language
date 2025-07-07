#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第06章 字典 - 遍历字典
演示如何遍历字典的键、值和键值对
"""

def main():
    print("=== 遍历字典演示 ===\n")
    
    # 基础数据
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'
    }
    
    # 1. 遍历所有键值对
    print("1. 遍历所有键值对")
    print("-" * 30)
    
    print("使用items()方法：")
    for name, language in favorite_languages.items():
        print(f"{name.title()}的喜欢的语言是{language.title()}。")
    print()
    
    # 直接遍历（默认遍历键）
    print("直接遍历（默认遍历键）：")
    for name in favorite_languages:
        language = favorite_languages[name]
        print(f"{name.title()}的喜欢的语言是{language.title()}。")
    print()
    
    # 2. 遍历字典中的所有键
    print("2. 遍历字典中的所有键")
    print("-" * 30)
    
    print("使用keys()方法：")
    for name in favorite_languages.keys():
        print(f"姓名：{name.title()}")
    print()
    
    # 检查特定的键
    friends = ['phil', 'sarah']
    print("检查朋友们的编程语言偏好：")
    for name in favorite_languages.keys():
        if name in friends:
            language = favorite_languages[name]
            print(f"  {name.title()}，我知道你最喜欢{language.title()}！")
    print()
    
    # 检查特定的人是否在字典中
    if 'erin' not in favorite_languages.keys():
        print("Erin，请告诉我们你最喜欢的语言！")
    print()
    
    # 3. 按顺序遍历字典中的所有键
    print("3. 按顺序遍历字典中的所有键")
    print("-" * 30)
    
    print("按字母顺序遍历姓名：")
    for name in sorted(favorite_languages.keys()):
        print(f"{name.title()}，感谢你参与调查！")
    print()
    
    # 4. 遍历字典中的所有值
    print("4. 遍历字典中的所有值")
    print("-" * 30)
    
    print("使用values()方法：")
    print("调查中提到的语言：")
    for language in favorite_languages.values():
        print(f"  {language.title()}")
    print()
    
    # 去重的值遍历
    print("去重的语言列表：")
    for language in set(favorite_languages.values()):
        print(f"  {language.title()}")
    print()
    
    # 5. 复杂的遍历场景
    print("5. 复杂的遍历场景")
    print("-" * 30)
    
    # 多维数据遍历
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
    
    # 6. 使用enumerate()遍历字典
    print("6. 使用enumerate()遍历字典")
    print("-" * 30)
    
    print("带索引的遍历：")
    for index, (name, language) in enumerate(favorite_languages.items()):
        print(f"{index + 1}. {name.title()}: {language.title()}")
    print()
    
    # 7. 条件遍历
    print("7. 条件遍历")
    print("-" * 30)
    
    # 只遍历符合条件的项
    print("只显示使用Python的用户：")
    for name, language in favorite_languages.items():
        if language == 'python':
            print(f"  {name.title()}")
    print()
    
    # 使用字典推导式进行筛选
    python_users = {name: language for name, language in favorite_languages.items() 
                   if language == 'python'}
    print(f"Python用户字典：{python_users}")
    print()
    
    # 8. 嵌套结构的遍历
    print("8. 嵌套结构的遍历")
    print("-" * 30)
    
    # 字典中包含列表
    pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
    }
    
    print(f"你点了一个{pizza['crust']}面皮的披萨，")
    print("配料有：")
    for topping in pizza['toppings']:
        print(f"  {topping}")
    print()
    
    # 更复杂的嵌套结构
    many_users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
            'hobbies': ['physics', 'violin', 'sailing']
        },
        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
            'hobbies': ['chemistry', 'reading', 'research']
        }
    }
    
    print("用户详细信息（包含爱好）：")
    for username, user_info in many_users.items():
        print(f"\n用户名：{username}")
        full_name = f"{user_info['first']} {user_info['last']}"
        location = user_info['location']
        hobbies = user_info['hobbies']
        
        print(f"  全名：{full_name.title()}")
        print(f"  位置：{location.title()}")
        print(f"  爱好：")
        for hobby in hobbies:
            print(f"    - {hobby.title()}")
    print()
    
    # 9. 实际应用：数据分析和统计
    print("9. 实际应用：数据分析和统计")
    print("-" * 30)
    
    # 销售数据分析
    sales_data = {
        'January': [1200, 1500, 1800, 2000],
        'February': [1100, 1400, 1600, 1900],
        'March': [1300, 1600, 1900, 2200],
        'April': [1400, 1700, 2000, 2300]
    }
    
    print("月度销售数据分析：")
    total_sales = 0
    for month, weekly_sales in sales_data.items():
        monthly_total = sum(weekly_sales)
        monthly_average = monthly_total / len(weekly_sales)
        total_sales += monthly_total
        
        print(f"{month}:")
        print(f"  总销售额：¥{monthly_total}")
        print(f"  周平均销售额：¥{monthly_average:.2f}")
        print(f"  每周销售额：{weekly_sales}")
    
    print(f"\n总销售额：¥{total_sales}")
    print(f"月平均销售额：¥{total_sales / len(sales_data):.2f}")
    print()
    
    # 10. 多个字典的遍历
    print("10. 多个字典的遍历")
    print("-" * 30)
    
    # 创建一个外星人列表
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
    
    # 修改前3个外星人
    for alien in aliens[:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10
    
    # 显示修改后的前5个外星人
    print("\n修改后的前5个外星人：")
    for alien in aliens[:5]:
        print(alien)
    print("...")
    
    print(f"\n外星人总数：{len(aliens)}")
    print()
    
    # 11. 字典的高级遍历技巧
    print("11. 字典的高级遍历技巧")
    print("-" * 30)
    
    grades = {
        'Alice': 85,
        'Bob': 90,
        'Charlie': 78,
        'Diana': 92,
        'Eve': 88
    }
    
    # 找到最高分
    highest_score = max(grades.values())
    print(f"最高分：{highest_score}")
    
    # 找到最高分的学生
    for name, score in grades.items():
        if score == highest_score:
            print(f"最高分学生：{name}")
            break
    
    # 使用key参数找到最高分学生
    best_student = max(grades, key=grades.get)
    print(f"最高分学生（使用key参数）：{best_student}")
    
    # 按分数排序
    print("\n按分数排序：")
    sorted_students = sorted(grades.items(), key=lambda x: x[1], reverse=True)
    for rank, (name, score) in enumerate(sorted_students, 1):
        print(f"{rank}. {name}: {score}")
    print()
    
    # 12. 字典推导式与遍历
    print("12. 字典推导式与遍历")
    print("-" * 30)
    
    # 基于现有字典创建新字典
    squared_grades = {name: score ** 2 for name, score in grades.items()}
    print(f"成绩平方字典：{squared_grades}")
    
    # 筛选字典
    high_achievers = {name: score for name, score in grades.items() if score >= 85}
    print(f"高分学生：{high_achievers}")
    
    # 字典键值互换
    score_to_name = {score: name for name, score in grades.items()}
    print(f"分数到姓名的映射：{score_to_name}")
    print()
    
    # 13. 遍历的性能考虑
    print("13. 遍历的性能考虑")
    print("-" * 30)
    
    import time
    
    # 创建大字典
    large_dict = {f'key_{i}': i for i in range(10000)}
    
    # 测试不同遍历方式的性能
    print("性能测试（10000个元素）：")
    
    # 方法1：items()
    start_time = time.time()
    for key, value in large_dict.items():
        pass
    end_time = time.time()
    print(f"items()方法：{(end_time - start_time) * 1000:.2f}毫秒")
    
    # 方法2：keys()
    start_time = time.time()
    for key in large_dict.keys():
        value = large_dict[key]
    end_time = time.time()
    print(f"keys()方法：{(end_time - start_time) * 1000:.2f}毫秒")
    
    # 方法3：直接遍历
    start_time = time.time()
    for key in large_dict:
        value = large_dict[key]
    end_time = time.time()
    print(f"直接遍历：{(end_time - start_time) * 1000:.2f}毫秒")
    print()
    
    # 14. 遍历的最佳实践
    print("14. 遍历的最佳实践")
    print("-" * 30)
    
    print("字典遍历的最佳实践：")
    print("1. 需要键值对时使用items()")
    print("2. 只需要键时使用keys()或直接遍历")
    print("3. 只需要值时使用values()")
    print("4. 需要排序时使用sorted()")
    print("5. 需要索引时使用enumerate()")
    print("6. 需要筛选时使用条件判断或字典推导式")
    print("7. 处理大数据时注意性能")
    print("8. 遍历时修改字典要小心")
    print()
    
    # 遍历时修改字典的安全做法
    print("遍历时修改字典的安全做法：")
    test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print(f"原始字典：{test_dict}")
    
    # 错误做法（可能导致RuntimeError）
    # for key in test_dict:
    #     if test_dict[key] % 2 == 0:
    #         del test_dict[key]  # 这可能会出错
    
    # 正确做法：先收集要删除的键
    keys_to_remove = []
    for key, value in test_dict.items():
        if value % 2 == 0:
            keys_to_remove.append(key)
    
    for key in keys_to_remove:
        del test_dict[key]
    
    print(f"删除偶数值后：{test_dict}")
    print()
    
    # 或者使用字典推导式
    test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    test_dict = {key: value for key, value in test_dict.items() if value % 2 != 0}
    print(f"使用字典推导式删除偶数值：{test_dict}")


if __name__ == "__main__":
    main() 