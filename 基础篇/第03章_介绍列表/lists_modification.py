#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第03章 介绍列表 - 列表修改操作
演示如何修改列表中的元素、添加元素、删除元素等操作
"""

def main():
    print("=== 列表修改操作演示 ===\n")
    
    # 1. 修改列表元素
    print("1. 修改列表元素")
    print("-" * 30)
    
    # 创建一个摩托车列表
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(f"原始列表：{motorcycles}")
    
    # 修改第一个元素
    motorcycles[0] = 'ducati'
    print(f"修改后：{motorcycles}")
    print()
    
    # 2. 在列表末尾添加元素
    print("2. 在列表末尾添加元素")
    print("-" * 30)
    
    # 使用append()方法
    motorcycles.append('honda')
    print(f"添加honda后：{motorcycles}")
    
    # 创建空列表并逐个添加元素
    empty_list = []
    empty_list.append('kawasaki')
    empty_list.append('triumph')
    print(f"空列表添加元素后：{empty_list}")
    print()
    
    # 3. 在列表中插入元素
    print("3. 在列表中插入元素")
    print("-" * 30)
    
    # 使用insert()方法在指定位置插入元素
    motorcycles.insert(0, 'ktm')
    print(f"在开头插入ktm：{motorcycles}")
    
    motorcycles.insert(2, 'bmw')
    print(f"在索引2位置插入bmw：{motorcycles}")
    print()
    
    # 4. 从列表中删除元素
    print("4. 从列表中删除元素")
    print("-" * 30)
    
    # 使用del语句删除
    print(f"删除前：{motorcycles}")
    del motorcycles[0]
    print(f"删除索引0的元素后：{motorcycles}")
    
    # 使用pop()方法删除末尾元素
    print(f"删除前：{motorcycles}")
    popped_motorcycle = motorcycles.pop()
    print(f"弹出的元素：{popped_motorcycle}")
    print(f"删除后：{motorcycles}")
    
    # 弹出列表中任何位置的元素
    first_owned = motorcycles.pop(0)
    print(f"弹出第一个元素：{first_owned}")
    print(f"剩余列表：{motorcycles}")
    print()
    
    # 5. 根据值删除元素
    print("5. 根据值删除元素")
    print("-" * 30)
    
    # 重新创建列表
    motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
    print(f"原始列表：{motorcycles}")
    
    # 使用remove()方法
    motorcycles.remove('ducati')
    print(f"删除ducati后：{motorcycles}")
    
    # 删除可能不存在的元素（安全删除）
    def safe_remove(lst, value):
        """安全地从列表中删除值"""
        try:
            lst.remove(value)
            print(f"成功删除：{value}")
        except ValueError:
            print(f"值 {value} 不在列表中")
    
    safe_remove(motorcycles, 'honda')
    safe_remove(motorcycles, 'kawasaki')  # 不存在的元素
    print(f"最终列表：{motorcycles}")
    print()
    
    # 6. 实际应用示例
    print("6. 实际应用示例")
    print("-" * 30)
    
    # 待办事项列表管理
    todo_list = []
    
    # 添加任务
    todo_list.append('完成作业')
    todo_list.append('买菜')
    todo_list.append('锻炼')
    print(f"待办事项：{todo_list}")
    
    # 插入紧急任务
    todo_list.insert(0, '回复邮件')
    print(f"插入紧急任务后：{todo_list}")
    
    # 完成任务（删除）
    completed_task = todo_list.pop(0)
    print(f"完成任务：{completed_task}")
    print(f"剩余任务：{todo_list}")
    
    # 取消任务
    todo_list.remove('锻炼')
    print(f"取消锻炼后：{todo_list}")
    print()
    
    # 7. 列表元素的多种操作
    print("7. 列表元素的多种操作")
    print("-" * 30)
    
    # 购物清单示例
    shopping_list = ['苹果', '香蕉', '牛奶']
    print(f"购物清单：{shopping_list}")
    
    # 修改商品
    shopping_list[1] = '橙子'
    print(f"修改后：{shopping_list}")
    
    # 添加商品
    shopping_list.extend(['面包', '鸡蛋'])  # 添加多个元素
    print(f"批量添加后：{shopping_list}")
    
    # 删除已购买商品
    bought_item = shopping_list.pop(0)
    print(f"已购买：{bought_item}")
    print(f"剩余商品：{shopping_list}")
    
    # 清空列表
    shopping_list.clear()
    print(f"清空后：{shopping_list}")
    print()
    
    # 8. 列表修改的注意事项
    print("8. 列表修改的注意事项")
    print("-" * 30)
    
    # 索引越界错误示例
    numbers = [1, 2, 3]
    print(f"列表：{numbers}")
    
    try:
        numbers[10] = 100  # 索引越界
    except IndexError as e:
        print(f"索引越界错误：{e}")
    
    # 删除不存在的元素
    try:
        numbers.remove(999)  # 元素不存在
    except ValueError as e:
        print(f"值错误：{e}")
    
    # 正确的做法
    if 999 in numbers:
        numbers.remove(999)
    else:
        print("元素999不在列表中")
    
    print(f"最终列表：{numbers}")


if __name__ == "__main__":
    main() 