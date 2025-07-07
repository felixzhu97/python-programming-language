#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第03章 介绍列表 - 列表组织和排序
演示如何对列表进行排序、反转等组织操作
"""

def main():
    print("=== 列表组织和排序演示 ===\n")
    
    # 1. 使用sort()方法对列表进行永久性排序
    print("1. 使用sort()方法对列表进行永久性排序")
    print("-" * 50)
    
    # 字符串列表排序
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    print(f"原始列表：{cars}")
    
    cars.sort()
    print(f"按字母顺序排序：{cars}")
    
    # 按相反的字母顺序排序
    cars.sort(reverse=True)
    print(f"按相反字母顺序排序：{cars}")
    print()
    
    # 2. 使用sorted()函数对列表进行临时排序
    print("2. 使用sorted()函数对列表进行临时排序")
    print("-" * 50)
    
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    print(f"原始列表：{cars}")
    print(f"临时排序：{sorted(cars)}")
    print(f"原始列表未变：{cars}")
    print(f"临时反向排序：{sorted(cars, reverse=True)}")
    print(f"原始列表仍未变：{cars}")
    print()
    
    # 3. 数字列表排序
    print("3. 数字列表排序")
    print("-" * 30)
    
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"原始数字列表：{numbers}")
    
    # 升序排序
    numbers.sort()
    print(f"升序排序：{numbers}")
    
    # 降序排序
    numbers.sort(reverse=True)
    print(f"降序排序：{numbers}")
    
    # 使用sorted()临时排序
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"原始列表：{numbers}")
    print(f"临时升序：{sorted(numbers)}")
    print(f"临时降序：{sorted(numbers, reverse=True)}")
    print()
    
    # 4. 倒着打印列表
    print("4. 倒着打印列表")
    print("-" * 30)
    
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    print(f"原始列表：{cars}")
    
    # 使用reverse()方法永久性反转列表
    cars.reverse()
    print(f"反转后：{cars}")
    
    # 再次反转，恢复原始顺序
    cars.reverse()
    print(f"再次反转：{cars}")
    
    # 使用切片临时反转
    print(f"切片反转：{cars[::-1]}")
    print(f"原始列表未变：{cars}")
    print()
    
    # 5. 确定列表长度
    print("5. 确定列表长度")
    print("-" * 30)
    
    print(f"cars列表长度：{len(cars)}")
    print(f"空列表长度：{len([])}")
    print(f"数字列表长度：{len([1, 2, 3, 4, 5])}")
    print()
    
    # 6. 复杂排序示例
    print("6. 复杂排序示例")
    print("-" * 30)
    
    # 按长度排序
    words = ['python', 'java', 'c', 'javascript', 'go']
    print(f"原始单词列表：{words}")
    print(f"按长度排序：{sorted(words, key=len)}")
    print(f"按长度反向排序：{sorted(words, key=len, reverse=True)}")
    
    # 忽略大小写排序
    mixed_case = ['banana', 'Apple', 'cherry', 'Date']
    print(f"混合大小写列表：{mixed_case}")
    print(f"忽略大小写排序：{sorted(mixed_case, key=str.lower)}")
    print()
    
    # 7. 嵌套列表排序
    print("7. 嵌套列表排序")
    print("-" * 30)
    
    # 学生成绩列表
    students = [
        ['Alice', 85],
        ['Bob', 90],
        ['Charlie', 78],
        ['David', 92]
    ]
    print(f"学生成绩：{students}")
    
    # 按成绩排序
    students_by_score = sorted(students, key=lambda x: x[1])
    print(f"按成绩排序：{students_by_score}")
    
    # 按成绩降序排序
    students_by_score_desc = sorted(students, key=lambda x: x[1], reverse=True)
    print(f"按成绩降序排序：{students_by_score_desc}")
    
    # 按姓名排序
    students_by_name = sorted(students, key=lambda x: x[0])
    print(f"按姓名排序：{students_by_name}")
    print()
    
    # 8. 实际应用示例
    print("8. 实际应用示例")
    print("-" * 30)
    
    # 音乐播放列表管理
    playlist = [
        '周杰伦 - 青花瓷',
        'Taylor Swift - Shake It Off',
        '邓紫棋 - 光年之外',
        'Ed Sheeran - Shape of You',
        '毛不易 - 消愁'
    ]
    
    print("音乐播放列表管理：")
    print(f"原始播放列表：{playlist}")
    
    # 按字母顺序排序
    print(f"按字母顺序：{sorted(playlist)}")
    
    # 随机播放（反转）
    random_playlist = playlist.copy()
    random_playlist.reverse()
    print(f"反转播放：{random_playlist}")
    
    # 获取播放列表信息
    print(f"播放列表长度：{len(playlist)}首歌")
    print(f"第一首歌：{playlist[0]}")
    print(f"最后一首歌：{playlist[-1]}")
    print()
    
    # 9. 排序的注意事项
    print("9. 排序的注意事项")
    print("-" * 30)
    
    # 混合数据类型排序会出错
    mixed_list = [1, 'hello', 3.14, True]
    print(f"混合类型列表：{mixed_list}")
    
    try:
        sorted(mixed_list)
    except TypeError as e:
        print(f"排序错误：{e}")
    
    # 正确的做法是先转换为统一类型
    string_list = [str(item) for item in mixed_list]
    print(f"转换为字符串：{string_list}")
    print(f"字符串排序：{sorted(string_list)}")
    print()
    
    # 10. 列表组织的最佳实践
    print("10. 列表组织的最佳实践")
    print("-" * 30)
    
    # 保持原始数据不变
    original_data = [5, 2, 8, 1, 9, 3]
    print(f"原始数据：{original_data}")
    
    # 使用sorted()保持原始数据不变
    sorted_data = sorted(original_data)
    print(f"排序后的副本：{sorted_data}")
    print(f"原始数据仍为：{original_data}")
    
    # 如果需要修改原始数据，使用sort()
    original_data.sort()
    print(f"原始数据排序后：{original_data}")
    
    # 链式操作
    numbers = [5, 2, 8, 1, 9, 3]
    result = sorted(numbers, reverse=True)[:3]  # 取前3个最大值
    print(f"前3个最大值：{result}")


if __name__ == "__main__":
    main() 