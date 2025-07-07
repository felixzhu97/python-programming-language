#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第04章 操作列表 - 切片和复制列表
演示如何使用切片处理列表的部分元素和复制列表
"""

def main():
    print("=== 切片和复制列表演示 ===\n")
    
    # 1. 基本切片操作
    print("1. 基本切片操作")
    print("-" * 30)
    
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(f"球员列表：{players}")
    
    # 切片前三个元素
    first_three = players[0:3]
    print(f"前三个球员：{first_three}")
    
    # 切片第2到第4个元素
    middle_players = players[1:4]
    print(f"中间球员：{middle_players}")
    
    # 从索引2开始到结束
    last_players = players[2:]
    print(f"从第3个开始的球员：{last_players}")
    
    # 从开始到索引3（不包括）
    first_players = players[:4]
    print(f"前4个球员：{first_players}")
    
    # 获取最后三个元素
    last_three = players[-3:]
    print(f"最后三个球员：{last_three}")
    print()
    
    # 2. 切片的步长
    print("2. 切片的步长")
    print("-" * 30)
    
    numbers = list(range(1, 21))
    print(f"数字列表：{numbers}")
    
    # 每隔一个元素取一个
    every_second = numbers[::2]
    print(f"每隔一个元素：{every_second}")
    
    # 每隔两个元素取一个
    every_third = numbers[::3]
    print(f"每隔两个元素：{every_third}")
    
    # 倒序切片
    reversed_numbers = numbers[::-1]
    print(f"倒序：{reversed_numbers}")
    
    # 倒序取前5个
    last_five_reversed = numbers[-5:][::-1]
    print(f"最后5个倒序：{last_five_reversed}")
    
    # 从索引1开始，每隔2个取一个，到索引10结束
    custom_slice = numbers[1:10:2]
    print(f"自定义切片：{custom_slice}")
    print()
    
    # 3. 遍历切片
    print("3. 遍历切片")
    print("-" * 30)
    
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(f"球员列表：{players}")
    
    print("前三名球员：")
    for player in players[:3]:
        print(f"  {player.title()}")
    
    print("最后两名球员：")
    for player in players[-2:]:
        print(f"  {player.title()}")
    
    print("每隔一个球员：")
    for player in players[::2]:
        print(f"  {player.title()}")
    print()
    
    # 4. 复制列表
    print("4. 复制列表")
    print("-" * 30)
    
    my_foods = ['pizza', 'falafel', 'carrot cake']
    print(f"我的食物：{my_foods}")
    
    # 正确的复制方法：使用切片
    friend_foods = my_foods[:]
    print(f"朋友的食物（切片复制）：{friend_foods}")
    
    # 添加不同的食物
    my_foods.append('cannoli')
    friend_foods.append('ice cream')
    
    print(f"我的食物（添加后）：{my_foods}")
    print(f"朋友的食物（添加后）：{friend_foods}")
    
    # 错误的复制方法：直接赋值
    wrong_copy = my_foods
    wrong_copy.append('cookies')
    
    print(f"我的食物（错误复制后）：{my_foods}")
    print(f"错误复制的列表：{wrong_copy}")
    print(f"是否为同一个对象：{my_foods is wrong_copy}")
    print()
    
    # 5. 不同的复制方法
    print("5. 不同的复制方法")
    print("-" * 30)
    
    original = [1, 2, 3, 4, 5]
    print(f"原始列表：{original}")
    
    # 方法1：切片复制
    copy1 = original[:]
    print(f"切片复制：{copy1}")
    
    # 方法2：list()函数
    copy2 = list(original)
    print(f"list()函数复制：{copy2}")
    
    # 方法3：copy()方法
    copy3 = original.copy()
    print(f"copy()方法复制：{copy3}")
    
    # 验证是否为不同对象
    print(f"切片复制是否为同一对象：{original is copy1}")
    print(f"list()复制是否为同一对象：{original is copy2}")
    print(f"copy()复制是否为同一对象：{original is copy3}")
    
    # 修改原始列表
    original.append(6)
    print(f"修改原始列表后：{original}")
    print(f"切片复制：{copy1}")
    print(f"list()函数复制：{copy2}")
    print(f"copy()方法复制：{copy3}")
    print()
    
    # 6. 深拷贝 vs 浅拷贝
    print("6. 深拷贝 vs 浅拷贝")
    print("-" * 30)
    
    # 嵌套列表
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"嵌套列表：{nested_list}")
    
    # 浅拷贝
    shallow_copy = nested_list[:]
    print(f"浅拷贝：{shallow_copy}")
    
    # 修改嵌套列表中的元素
    nested_list[0][0] = 999
    print(f"修改原始列表后：{nested_list}")
    print(f"浅拷贝：{shallow_copy}")
    print("注意：浅拷贝中的嵌套列表也被修改了！")
    
    # 深拷贝
    import copy
    nested_list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    deep_copy = copy.deepcopy(nested_list2)
    
    nested_list2[0][0] = 888
    print(f"修改原始列表2后：{nested_list2}")
    print(f"深拷贝：{deep_copy}")
    print("注意：深拷贝中的嵌套列表没有被修改！")
    print()
    
    # 7. 切片的实际应用
    print("7. 切片的实际应用")
    print("-" * 30)
    
    # 数据分析
    sales_data = [100, 120, 80, 150, 200, 180, 160, 140, 110, 130, 170, 190]
    print(f"销售数据：{sales_data}")
    
    # 第一季度数据
    q1_sales = sales_data[:3]
    print(f"第一季度销售：{q1_sales}，平均：{sum(q1_sales)/len(q1_sales):.1f}")
    
    # 第二季度数据
    q2_sales = sales_data[3:6]
    print(f"第二季度销售：{q2_sales}，平均：{sum(q2_sales)/len(q2_sales):.1f}")
    
    # 下半年数据
    second_half = sales_data[6:]
    print(f"下半年销售：{second_half}，平均：{sum(second_half)/len(second_half):.1f}")
    
    # 最近三个月
    recent_three = sales_data[-3:]
    print(f"最近三个月：{recent_three}，平均：{sum(recent_three)/len(recent_three):.1f}")
    print()
    
    # 8. 字符串切片
    print("8. 字符串切片")
    print("-" * 30)
    
    message = "Hello, Python Programming!"
    print(f"原始字符串：{message}")
    
    # 基本切片
    print(f"前5个字符：{message[:5]}")
    print(f"后12个字符：{message[-12:]}")
    print(f"中间部分：{message[7:13]}")
    
    # 每隔一个字符
    print(f"每隔一个字符：{message[::2]}")
    
    # 倒序
    print(f"倒序：{message[::-1]}")
    
    # 提取单词
    words = message.split()
    print(f"单词列表：{words}")
    print(f"前两个单词：{words[:2]}")
    print()
    
    # 9. 切片修改列表
    print("9. 切片修改列表")
    print("-" * 30)
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"原始列表：{numbers}")
    
    # 替换切片
    numbers[2:5] = [30, 40, 50]
    print(f"替换索引2-4的元素：{numbers}")
    
    # 插入元素
    numbers[5:5] = [55, 56]
    print(f"在索引5处插入：{numbers}")
    
    # 删除元素
    del numbers[3:6]
    print(f"删除索引3-5的元素：{numbers}")
    
    # 步长赋值
    numbers[::2] = [100, 200, 300, 400, 500]
    print(f"步长赋值：{numbers}")
    print()
    
    # 10. 切片的高级应用
    print("10. 切片的高级应用")
    print("-" * 30)
    
    # 数据分页
    def paginate(data, page_size=3):
        """将数据分页"""
        pages = []
        for i in range(0, len(data), page_size):
            pages.append(data[i:i + page_size])
        return pages
    
    data = list(range(1, 16))  # 1到15的数字
    print(f"原始数据：{data}")
    
    pages = paginate(data, 4)
    print(f"分页结果：")
    for i, page in enumerate(pages, 1):
        print(f"  第{i}页：{page}")
    
    # 滑动窗口
    def sliding_window(data, window_size=3):
        """滑动窗口处理数据"""
        windows = []
        for i in range(len(data) - window_size + 1):
            windows.append(data[i:i + window_size])
        return windows
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"数字序列：{numbers}")
    
    windows = sliding_window(numbers, 3)
    print(f"滑动窗口（大小3）：")
    for i, window in enumerate(windows):
        print(f"  窗口{i+1}：{window}")
    
    # 计算滑动平均
    moving_averages = [sum(window) / len(window) for window in windows]
    print(f"滑动平均：{moving_averages}")
    print()
    
    # 11. 性能考虑
    print("11. 性能考虑")
    print("-" * 30)
    
    import time
    
    # 创建大列表
    large_list = list(range(1000000))
    
    # 测试切片性能
    start_time = time.time()
    slice_result = large_list[100000:200000]
    end_time = time.time()
    print(f"切片10万个元素：{end_time - start_time:.4f}秒")
    
    # 测试列表复制性能
    start_time = time.time()
    copy_result = large_list[:]
    end_time = time.time()
    print(f"复制100万个元素：{end_time - start_time:.4f}秒")
    
    # 测试步长切片性能
    start_time = time.time()
    step_result = large_list[::100]
    end_time = time.time()
    print(f"步长切片：{end_time - start_time:.4f}秒")
    print()
    
    # 12. 切片的最佳实践
    print("12. 切片的最佳实践")
    print("-" * 30)
    
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"示例数据：{data}")
    
    # 使用有意义的变量名
    first_half = data[:5]
    second_half = data[5:]
    print(f"前半部分：{first_half}")
    print(f"后半部分：{second_half}")
    
    # 边界检查
    def safe_slice(lst, start, end):
        """安全的切片操作"""
        start = max(0, start)
        end = min(len(lst), end)
        return lst[start:end]
    
    print(f"安全切片（-5到20）：{safe_slice(data, -5, 20)}")
    
    # 使用切片而不是循环
    # 不推荐：使用循环
    result_loop = []
    for i in range(5):
        result_loop.append(data[i])
    
    # 推荐：使用切片
    result_slice = data[:5]
    
    print(f"循环结果：{result_loop}")
    print(f"切片结果：{result_slice}")
    print(f"结果相同：{result_loop == result_slice}")


if __name__ == "__main__":
    main() 