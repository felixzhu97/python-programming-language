#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第03章 介绍列表 - 练习题解答
包含书中第03章的所有练习题及其解答
"""

def main():
    print("=== 第03章 介绍列表 - 练习题解答 ===\n")
    
    # 练习 3-1: 姓名
    print("练习 3-1: 姓名")
    print("-" * 20)
    names = ['alice', 'bob', 'charlie']
    print(f"姓名列表：{names}")
    for name in names:
        print(f"你好，{name.title()}！")
    print()
    
    # 练习 3-2: 问候语
    print("练习 3-2: 问候语")
    print("-" * 20)
    names = ['alice', 'bob', 'charlie']
    print(f"姓名列表：{names}")
    for name in names:
        print(f"{name.title()}，你好！希望你今天过得愉快。")
    print()
    
    # 练习 3-3: 自己的列表
    print("练习 3-3: 自己的列表")
    print("-" * 20)
    # 想想你喜欢的通勤方式
    transportations = ['摩托车', '汽车', '自行车']
    print(f"我喜欢的交通工具：{transportations}")
    for transport in transportations:
        print(f"我想拥有一辆{transport}。")
    print()
    
    # 练习 3-4: 嘉宾名单
    print("练习 3-4: 嘉宾名单")
    print("-" * 20)
    guest_list = ['爱因斯坦', '居里夫人', '达芬奇']
    print(f"邀请名单：{guest_list}")
    for guest in guest_list:
        print(f"尊敬的{guest}，诚挚邀请您参加我的晚宴。")
    print()
    
    # 练习 3-5: 修改嘉宾名单
    print("练习 3-5: 修改嘉宾名单")
    print("-" * 20)
    guest_list = ['爱因斯坦', '居里夫人', '达芬奇']
    print(f"原始邀请名单：{guest_list}")
    
    # 假设居里夫人无法参加
    unavailable_guest = guest_list[1]
    print(f"{unavailable_guest}无法参加晚宴。")
    
    # 替换为牛顿
    guest_list[1] = '牛顿'
    print(f"更新后的邀请名单：{guest_list}")
    
    # 发送新邀请
    for guest in guest_list:
        print(f"尊敬的{guest}，诚挚邀请您参加我的晚宴。")
    print()
    
    # 练习 3-6: 添加嘉宾
    print("练习 3-6: 添加嘉宾")
    print("-" * 20)
    guest_list = ['爱因斯坦', '牛顿', '达芬奇']
    print(f"原始邀请名单：{guest_list}")
    print("好消息！我找到了一个更大的餐桌。")
    
    # 在列表开头添加一位嘉宾
    guest_list.insert(0, '苏格拉底')
    print(f"在开头添加苏格拉底：{guest_list}")
    
    # 在列表中间添加一位嘉宾
    guest_list.insert(2, '孔子')
    print(f"在中间添加孔子：{guest_list}")
    
    # 在列表末尾添加一位嘉宾
    guest_list.append('莎士比亚')
    print(f"在末尾添加莎士比亚：{guest_list}")
    
    # 发送邀请
    for guest in guest_list:
        print(f"尊敬的{guest}，诚挚邀请您参加我的晚宴。")
    print()
    
    # 练习 3-7: 缩减嘉宾名单
    print("练习 3-7: 缩减嘉宾名单")
    print("-" * 20)
    guest_list = ['苏格拉底', '爱因斯坦', '孔子', '牛顿', '达芬奇', '莎士比亚']
    print(f"原始邀请名单：{guest_list}")
    print("很遗憾，新餐桌无法及时到达，只能邀请两位嘉宾。")
    
    # 删除嘉宾直到只剩两位
    while len(guest_list) > 2:
        removed_guest = guest_list.pop()
        print(f"抱歉，{removed_guest}，我无法邀请您参加晚宴。")
    
    print(f"最终邀请名单：{guest_list}")
    # 向剩余的嘉宾发送邀请
    for guest in guest_list:
        print(f"尊敬的{guest}，您仍然被邀请参加我的晚宴。")
    
    # 清空列表
    del guest_list[0]
    del guest_list[0]
    print(f"清空后的列表：{guest_list}")
    print()
    
    # 练习 3-8: 放眼世界
    print("练习 3-8: 放眼世界")
    print("-" * 20)
    places = ['巴黎', '东京', '纽约', '罗马', '悉尼']
    print(f"想要访问的地方：{places}")
    print(f"按字母顺序排序：{sorted(places)}")
    print(f"原始列表：{places}")
    print(f"按字母逆序排序：{sorted(places, reverse=True)}")
    print(f"原始列表：{places}")
    
    # 反转列表
    places.reverse()
    print(f"反转后：{places}")
    
    # 再次反转，恢复原始顺序
    places.reverse()
    print(f"再次反转：{places}")
    
    # 永久性排序
    places.sort()
    print(f"永久性排序：{places}")
    
    # 永久性逆序排序
    places.sort(reverse=True)
    print(f"永久性逆序排序：{places}")
    print()
    
    # 练习 3-9: 晚餐嘉宾
    print("练习 3-9: 晚餐嘉宾")
    print("-" * 20)
    guest_list = ['爱因斯坦', '居里夫人', '达芬奇', '牛顿', '孔子']
    print(f"邀请了 {len(guest_list)} 位嘉宾参加晚宴。")
    print()
    
    # 练习 3-10: 尝试使用各个函数
    print("练习 3-10: 尝试使用各个函数")
    print("-" * 30)
    
    # 创建一个包含各种元素的列表
    my_list = ['苹果', '香蕉', '橙子', '草莓', '葡萄']
    print(f"原始列表：{my_list}")
    
    # 使用len()函数
    print(f"列表长度：{len(my_list)}")
    
    # 使用append()方法
    my_list.append('芒果')
    print(f"添加芒果后：{my_list}")
    
    # 使用insert()方法
    my_list.insert(2, '猕猴桃')
    print(f"插入猕猴桃后：{my_list}")
    
    # 使用remove()方法
    my_list.remove('香蕉')
    print(f"删除香蕉后：{my_list}")
    
    # 使用pop()方法
    popped_fruit = my_list.pop()
    print(f"弹出的水果：{popped_fruit}")
    print(f"弹出后的列表：{my_list}")
    
    # 使用sort()方法
    my_list.sort()
    print(f"排序后：{my_list}")
    
    # 使用reverse()方法
    my_list.reverse()
    print(f"反转后：{my_list}")
    
    # 使用sorted()函数
    print(f"临时排序：{sorted(my_list)}")
    print(f"原始列表：{my_list}")
    
    # 使用del语句
    del my_list[0]
    print(f"删除第一个元素后：{my_list}")
    print()
    
    # 额外练习：列表推导式预览
    print("额外练习：列表推导式预览")
    print("-" * 30)
    
    # 创建数字列表
    numbers = [1, 2, 3, 4, 5]
    print(f"原始数字列表：{numbers}")
    
    # 使用列表推导式创建平方数列表
    squares = [x**2 for x in numbers]
    print(f"平方数列表：{squares}")
    
    # 筛选偶数
    evens = [x for x in numbers if x % 2 == 0]
    print(f"偶数列表：{evens}")
    
    # 字符串处理
    words = ['python', 'java', 'c++', 'javascript']
    print(f"编程语言：{words}")
    
    # 转换为大写
    uppercase_words = [word.upper() for word in words]
    print(f"大写形式：{uppercase_words}")
    
    # 筛选长度大于3的单词
    long_words = [word for word in words if len(word) > 3]
    print(f"长度大于3的单词：{long_words}")
    print()
    
    # 总结
    print("总结：列表操作要点")
    print("-" * 20)
    print("1. 使用[]创建列表")
    print("2. 使用索引访问元素")
    print("3. 使用append()添加元素")
    print("4. 使用insert()插入元素")
    print("5. 使用remove()删除指定值")
    print("6. 使用pop()删除并返回元素")
    print("7. 使用del删除指定位置的元素")
    print("8. 使用sort()永久排序")
    print("9. 使用sorted()临时排序")
    print("10. 使用reverse()反转列表")
    print("11. 使用len()获取列表长度")


if __name__ == "__main__":
    main() 