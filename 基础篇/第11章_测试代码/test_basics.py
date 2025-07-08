#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第11章 测试代码 - 测试基础
演示Python中的单元测试基础知识和unittest模块的使用

主要内容：
1. unittest模块基础
2. 测试用例的编写
3. 断言方法的使用
4. 测试组织和执行
5. 测试输出和调试
"""

import unittest
import sys
from pathlib import Path

# 添加当前目录到路径，以便导入被测试的模块
sys.path.append(str(Path(__file__).parent))


# ==================== 被测试的函数 ====================

def add(a, b):
    """简单的加法函数"""
    return a + b


def multiply(a, b):
    """简单的乘法函数"""
    return a * b


def divide(a, b):
    """除法函数，包含异常处理"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def is_prime(n):
    """判断是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_formatted_name(first, last, middle=''):
    """返回格式化的姓名"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


def get_city_country(city, country, population=None):
    """返回城市和国家信息"""
    if population:
        result = f"{city}, {country} - 人口 {population}"
    else:
        result = f"{city}, {country}"
    return result


# ==================== 测试类 ====================

class TestBasicFunctions(unittest.TestCase):
    """测试基本函数的测试类"""
    
    def test_add_positive_numbers(self):
        """测试正数加法"""
        result = add(3, 5)
        self.assertEqual(result, 8)
    
    def test_add_negative_numbers(self):
        """测试负数加法"""
        result = add(-3, -5)
        self.assertEqual(result, -8)
    
    def test_add_zero(self):
        """测试零的加法"""
        result = add(5, 0)
        self.assertEqual(result, 5)
    
    def test_multiply(self):
        """测试乘法"""
        result = multiply(4, 6)
        self.assertEqual(result, 24)
    
    def test_divide_normal(self):
        """测试正常除法"""
        result = divide(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_divide_by_zero(self):
        """测试除零异常"""
        with self.assertRaises(ValueError):
            divide(10, 0)


class TestPrimeNumbers(unittest.TestCase):
    """测试质数判断函数"""
    
    def test_prime_numbers(self):
        """测试已知的质数"""
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for num in prime_numbers:
            with self.subTest(num=num):
                self.assertTrue(is_prime(num), f"{num} 应该是质数")
    
    def test_composite_numbers(self):
        """测试合数"""
        composite_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
        for num in composite_numbers:
            with self.subTest(num=num):
                self.assertFalse(is_prime(num), f"{num} 不应该是质数")
    
    def test_edge_cases(self):
        """测试边界情况"""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))


class TestNameFormatting(unittest.TestCase):
    """测试姓名格式化函数"""
    
    def test_first_last_name(self):
        """测试名字和姓氏"""
        formatted_name = get_formatted_name('john', 'doe')
        self.assertEqual(formatted_name, 'John Doe')
    
    def test_first_middle_last_name(self):
        """测试包含中间名"""
        formatted_name = get_formatted_name('john', 'doe', 'william')
        self.assertEqual(formatted_name, 'John William Doe')
    
    def test_empty_names(self):
        """测试空名字的情况"""
        formatted_name = get_formatted_name('', '')
        self.assertEqual(formatted_name, ' ')


class TestCityCountry(unittest.TestCase):
    """测试城市国家信息函数"""
    
    def test_city_country_without_population(self):
        """测试不包含人口的城市信息"""
        result = get_city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')
    
    def test_city_country_with_population(self):
        """测试包含人口的城市信息"""
        result = get_city_country('santiago', 'chile', 5000000)
        self.assertEqual(result, 'Santiago, Chile - 人口 5000000')


# ==================== 高级测试特性 ====================

class TestAdvancedFeatures(unittest.TestCase):
    """演示unittest的高级特性"""
    
    def setUp(self):
        """每个测试方法执行前都会运行"""
        self.test_data = [1, 2, 3, 4, 5]
        print("setUp: 准备测试数据")
    
    def tearDown(self):
        """每个测试方法执行后都会运行"""
        print("tearDown: 清理测试数据")
    
    @classmethod
    def setUpClass(cls):
        """整个测试类开始前运行一次"""
        print("setUpClass: 初始化测试类")
    
    @classmethod
    def tearDownClass(cls):
        """整个测试类结束后运行一次"""
        print("tearDownClass: 清理测试类")
    
    def test_list_operations(self):
        """测试列表操作"""
        self.assertIn(3, self.test_data)
        self.assertNotIn(10, self.test_data)
        self.assertEqual(len(self.test_data), 5)
    
    def test_string_operations(self):
        """测试字符串操作"""
        test_string = "Hello World"
        self.assertIn("Hello", test_string)
        self.assertTrue(test_string.startswith("Hello"))
        self.assertRegex(test_string, r"Hello \w+")
    
    def test_numeric_comparisons(self):
        """测试数值比较"""
        self.assertGreater(10, 5)
        self.assertLess(3, 7)
        self.assertAlmostEqual(3.14159, 3.14, places=2)
    
    @unittest.skip("演示跳过测试")
    def test_skipped(self):
        """这个测试会被跳过"""
        self.fail("这个测试不应该运行")
    
    @unittest.skipIf(sys.version_info < (3, 6), "需要Python 3.6+")
    def test_conditional_skip(self):
        """条件跳过测试"""
        self.assertTrue(True)
    
    @unittest.expectedFailure
    def test_expected_failure(self):
        """预期失败的测试"""
        self.assertEqual(1, 2)


# ==================== 自定义断言 ====================

class TestCustomAssertions(unittest.TestCase):
    """演示自定义断言"""
    
    def assertIsEven(self, number):
        """自定义断言：检查数字是否为偶数"""
        if number % 2 != 0:
            raise AssertionError(f"{number} 不是偶数")
    
    def assertIsOdd(self, number):
        """自定义断言：检查数字是否为奇数"""
        if number % 2 == 0:
            raise AssertionError(f"{number} 不是奇数")
    
    def test_custom_assertions(self):
        """测试自定义断言"""
        self.assertIsEven(4)
        self.assertIsOdd(5)


# ==================== 测试套件 ====================

def create_test_suite():
    """创建测试套件"""
    suite = unittest.TestSuite()
    
    # 添加特定的测试方法
    suite.addTest(TestBasicFunctions('test_add_positive_numbers'))
    suite.addTest(TestPrimeNumbers('test_prime_numbers'))
    
    # 添加整个测试类
    suite.addTest(unittest.makeSuite(TestNameFormatting))
    
    return suite


# ==================== 主程序 ====================

def demonstrate_testing_basics():
    """演示测试基础知识"""
    print("=" * 60)
    print("第11章 测试代码 - 测试基础演示")
    print("=" * 60)
    
    print("\n1. 被测试函数演示：")
    print(f"add(3, 5) = {add(3, 5)}")
    print(f"multiply(4, 6) = {multiply(4, 6)}")
    print(f"is_prime(17) = {is_prime(17)}")
    print(f"get_formatted_name('john', 'doe') = '{get_formatted_name('john', 'doe')}'")
    print(f"get_city_country('beijing', 'china', 21000000) = '{get_city_country('beijing', 'china', 21000000)}'")
    
    print("\n2. 运行特定测试类：")
    print("运行 TestBasicFunctions...")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBasicFunctions)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    # 如果直接运行此文件，执行演示
    if len(sys.argv) == 1:
        demonstrate_testing_basics()
    else:
        # 运行unittest
        unittest.main()


"""
运行测试的不同方法：

1. 运行所有测试：
   python test_basics.py

2. 运行特定测试类：
   python -m unittest test_basics.TestBasicFunctions

3. 运行特定测试方法：
   python -m unittest test_basics.TestBasicFunctions.test_add_positive_numbers

4. 详细输出：
   python -m unittest -v test_basics

5. 发现并运行所有测试：
   python -m unittest discover

常用断言方法：
- assertEqual(a, b)：检查 a == b
- assertNotEqual(a, b)：检查 a != b
- assertTrue(x)：检查 bool(x) is True
- assertFalse(x)：检查 bool(x) is False
- assertIs(a, b)：检查 a is b
- assertIsNot(a, b)：检查 a is not b
- assertIsNone(x)：检查 x is None
- assertIsNotNone(x)：检查 x is not None
- assertIn(a, b)：检查 a in b
- assertNotIn(a, b)：检查 a not in b
- assertIsInstance(a, b)：检查 isinstance(a, b)
- assertNotIsInstance(a, b)：检查 not isinstance(a, b)
- assertRaises(exc, fun, *args, **kwds)：检查异常
- assertAlmostEqual(a, b)：检查近似相等
- assertGreater(a, b)：检查 a > b
- assertLess(a, b)：检查 a < b
- assertRegex(s, r)：检查正则匹配
""" 