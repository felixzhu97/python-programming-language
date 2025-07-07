#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第04章 操作列表 - range函数和数字列表
演示如何使用range()函数创建数字列表和进行数值计算
"""

def main():
    print("=== range函数和数字列表演示 ===\n")
    
    # 1. range()函数的基本使用
    print("1. range()函数的基本使用")
    print("-" * 30)
    
    # 基本的range()
    print("range(5)生成的数字:")
    for value in range(5):
        print(value)
    print()
    
    # 指定起始值和结束值
    print("range(1, 6)生成的数字:")
    for value in range(1, 6):
        print(value)
    print()
    
    # 指定步长
    print("range(2, 11, 2)生成的数字:")
    for value in range(2, 11, 2):
        print(value)
    print()
    
    # 2. 使用range()创建数字列表
    print("2. 使用range()创建数字列表")
    print("-" * 30)
    
    # 创建1到10的数字列表
    numbers = list(range(1, 11))
    print(f"1到10的数字列表：{numbers}")
    
    # 创建偶数列表
    even_numbers = list(range(2, 21, 2))
    print(f"2到20的偶数列表：{even_numbers}")
    
    # 创建奇数列表
    odd_numbers = list(range(1, 21, 2))
    print(f"1到20的奇数列表：{odd_numbers}")
    
    # 创建倒序列表
    reverse_numbers = list(range(10, 0, -1))
    print(f"10到1的倒序列表：{reverse_numbers}")
    print()
    
    # 3. 数字列表的统计函数
    print("3. 数字列表的统计函数")
    print("-" * 30)
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"数字列表：{numbers}")
    print(f"最小值：{min(numbers)}")
    print(f"最大值：{max(numbers)}")
    print(f"总和：{sum(numbers)}")
    print(f"平均值：{sum(numbers) / len(numbers):.2f}")
    print()
    
    # 4. 创建平方数列表
    print("4. 创建平方数列表")
    print("-" * 30)
    
    # 方法1：使用for循环
    squares = []
    for value in range(1, 11):
        square = value ** 2
        squares.append(square)
    
    print(f"1到10的平方数（for循环）：{squares}")
    
    # 方法2：简化版本
    squares_simple = []
    for value in range(1, 11):
        squares_simple.append(value ** 2)
    
    print(f"1到10的平方数（简化版）：{squares_simple}")
    
    # 统计信息
    print(f"平方数的最小值：{min(squares)}")
    print(f"平方数的最大值：{max(squares)}")
    print(f"平方数的总和：{sum(squares)}")
    print()
    
    # 5. 立方数列表
    print("5. 立方数列表")
    print("-" * 30)
    
    cubes = []
    for value in range(1, 11):
        cubes.append(value ** 3)
    
    print(f"1到10的立方数：{cubes}")
    print(f"立方数的最小值：{min(cubes)}")
    print(f"立方数的最大值：{max(cubes)}")
    print(f"立方数的总和：{sum(cubes)}")
    print()
    
    # 6. 数字列表的处理
    print("6. 数字列表的处理")
    print("-" * 30)
    
    # 创建一个包含多种数字的列表
    mixed_numbers = list(range(-5, 6))
    print(f"混合数字列表：{mixed_numbers}")
    
    # 筛选正数
    positive_numbers = []
    for number in mixed_numbers:
        if number > 0:
            positive_numbers.append(number)
    
    print(f"正数列表：{positive_numbers}")
    
    # 筛选负数
    negative_numbers = []
    for number in mixed_numbers:
        if number < 0:
            negative_numbers.append(number)
    
    print(f"负数列表：{negative_numbers}")
    
    # 计算绝对值
    absolute_numbers = []
    for number in mixed_numbers:
        absolute_numbers.append(abs(number))
    
    print(f"绝对值列表：{absolute_numbers}")
    print()
    
    # 7. 大数据量的处理
    print("7. 大数据量的处理")
    print("-" * 30)
    
    # 创建大量数据
    large_numbers = list(range(1, 1001))
    print(f"数据量：{len(large_numbers)}")
    print(f"前10个数：{large_numbers[:10]}")
    print(f"后10个数：{large_numbers[-10:]}")
    print(f"最小值：{min(large_numbers)}")
    print(f"最大值：{max(large_numbers)}")
    print(f"总和：{sum(large_numbers)}")
    print(f"平均值：{sum(large_numbers) / len(large_numbers):.2f}")
    print()
    
    # 8. 斐波那契数列
    print("8. 斐波那契数列")
    print("-" * 30)
    
    # 生成斐波那契数列
    fibonacci = [1, 1]
    for i in range(2, 20):
        next_fib = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(next_fib)
    
    print(f"前20个斐波那契数：{fibonacci}")
    
    # 计算黄金比例
    golden_ratios = []
    for i in range(1, len(fibonacci)):
        ratio = fibonacci[i] / fibonacci[i-1]
        golden_ratios.append(ratio)
    
    print(f"相邻两项的比值：{golden_ratios[-5:]}")  # 显示最后5个比值
    print()
    
    # 9. 质数列表
    print("9. 质数列表")
    print("-" * 30)
    
    def is_prime(n):
        """判断一个数是否为质数"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # 找出100以内的质数
    primes = []
    for number in range(2, 101):
        if is_prime(number):
            primes.append(number)
    
    print(f"100以内的质数：{primes}")
    print(f"质数个数：{len(primes)}")
    print()
    
    # 10. 数字模式
    print("10. 数字模式")
    print("-" * 30)
    
    # 等差数列
    arithmetic_sequence = []
    first_term = 3
    common_difference = 7
    
    for i in range(10):
        term = first_term + i * common_difference
        arithmetic_sequence.append(term)
    
    print(f"等差数列（首项3，公差7）：{arithmetic_sequence}")
    
    # 等比数列
    geometric_sequence = []
    first_term = 2
    common_ratio = 3
    
    for i in range(8):
        term = first_term * (common_ratio ** i)
        geometric_sequence.append(term)
    
    print(f"等比数列（首项2，公比3）：{geometric_sequence}")
    print()
    
    # 11. 数字处理函数
    print("11. 数字处理函数")
    print("-" * 30)
    
    def process_numbers(numbers):
        """处理数字列表的函数"""
        result = {
            'count': len(numbers),
            'sum': sum(numbers),
            'min': min(numbers),
            'max': max(numbers),
            'average': sum(numbers) / len(numbers),
            'even_count': sum(1 for n in numbers if n % 2 == 0),
            'odd_count': sum(1 for n in numbers if n % 2 == 1),
        }
        return result
    
    test_numbers = list(range(1, 21))
    print(f"测试数字：{test_numbers}")
    
    stats = process_numbers(test_numbers)
    print(f"统计信息：")
    for key, value in stats.items():
        if key == 'average':
            print(f"  {key}: {value:.2f}")
        else:
            print(f"  {key}: {value}")
    print()
    
    # 12. 应用实例：成绩分析
    print("12. 应用实例：成绩分析")
    print("-" * 30)
    
    # 模拟学生成绩
    import random
    random.seed(42)  # 设置随机种子，确保结果可重现
    
    scores = []
    for i in range(50):
        score = random.randint(60, 100)
        scores.append(score)
    
    print(f"50名学生的成绩（部分）：{scores[:10]}...")
    
    # 成绩分析
    print(f"最高分：{max(scores)}")
    print(f"最低分：{min(scores)}")
    print(f"平均分：{sum(scores) / len(scores):.2f}")
    
    # 成绩分布
    grade_a = sum(1 for score in scores if score >= 90)
    grade_b = sum(1 for score in scores if 80 <= score < 90)
    grade_c = sum(1 for score in scores if 70 <= score < 80)
    grade_d = sum(1 for score in scores if 60 <= score < 70)
    grade_f = sum(1 for score in scores if score < 60)
    
    print(f"成绩分布：")
    print(f"  A级 (90-100): {grade_a}人")
    print(f"  B级 (80-89):  {grade_b}人")
    print(f"  C级 (70-79):  {grade_c}人")
    print(f"  D级 (60-69):  {grade_d}人")
    print(f"  F级 (<60):    {grade_f}人")
    print()
    
    # 13. 性能对比
    print("13. 性能对比")
    print("-" * 30)
    
    import time
    
    # 比较不同创建大列表的方法
    print("创建10万个数字的列表：")
    
    # 方法1：使用for循环
    start_time = time.time()
    numbers_loop = []
    for i in range(100000):
        numbers_loop.append(i)
    end_time = time.time()
    print(f"for循环方法：{end_time - start_time:.4f}秒")
    
    # 方法2：使用list(range())
    start_time = time.time()
    numbers_range = list(range(100000))
    end_time = time.time()
    print(f"list(range())方法：{end_time - start_time:.4f}秒")
    
    # 验证结果相同
    print(f"结果相同：{numbers_loop == numbers_range}")


if __name__ == "__main__":
    main() 