#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第11章 测试代码 - 练习题
《Python编程：从入门到实践》第11章练习题解答

练习11-1：城市和国家
练习11-2：人口数量
练习11-3：雇员
"""

import unittest
import sys


# ==================== 练习11-1和11-2: 城市和国家 ====================

def city_country(city, country, population=None):
    """
    返回形如 'Santiago, Chile' 或 'Santiago, Chile - population 5000000' 的字符串
    """
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"


class TestCityCountry(unittest.TestCase):
    """测试city_country函数"""
    
    def test_city_country(self):
        """测试城市和国家信息（练习11-1）"""
        result = city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')
        
        result = city_country('beijing', 'china')
        self.assertEqual(result, 'Beijing, China')
        
        result = city_country('new york', 'usa')
        self.assertEqual(result, 'New York, Usa')
    
    def test_city_country_population(self):
        """测试包含人口数量的城市信息（练习11-2）"""
        result = city_country('santiago', 'chile', 5000000)
        self.assertEqual(result, 'Santiago, Chile - population 5000000')
        
        result = city_country('beijing', 'china', 21000000)
        self.assertEqual(result, 'Beijing, China - population 21000000')
        
        result = city_country('tokyo', 'japan', 14000000)
        self.assertEqual(result, 'Tokyo, Japan - population 14000000')


# ==================== 练习11-3: 雇员 ====================

class Employee:
    """雇员类"""
    
    def __init__(self, first_name, last_name, annual_salary):
        """初始化员工信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, amount=5000):
        """给员工加薪，默认加薪5000"""
        if amount < 0:
            raise ValueError("加薪金额不能为负数")
        self.annual_salary += amount
    
    def get_full_name(self):
        """获取员工全名"""
        return f"{self.first_name} {self.last_name}"


class TestEmployee(unittest.TestCase):
    """测试Employee类"""
    
    def setUp(self):
        """创建供测试方法使用的Employee实例"""
        self.employee = Employee('张', '三', 60000)
    
    def test_give_default_raise(self):
        """测试默认加薪"""
        original_salary = self.employee.annual_salary
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, original_salary + 5000)
    
    def test_give_custom_raise(self):
        """测试自定义加薪金额"""
        original_salary = self.employee.annual_salary
        raise_amount = 10000
        self.employee.give_raise(raise_amount)
        self.assertEqual(self.employee.annual_salary, original_salary + raise_amount)
    
    def test_employee_attributes(self):
        """测试员工属性"""
        self.assertEqual(self.employee.first_name, '张')
        self.assertEqual(self.employee.last_name, '三')
        self.assertEqual(self.employee.annual_salary, 60000)
        self.assertEqual(self.employee.get_full_name(), '张 三')
    
    def test_negative_raise(self):
        """测试负数加薪（额外测试）"""
        with self.assertRaises(ValueError):
            self.employee.give_raise(-1000)
    
    def test_zero_raise(self):
        """测试零加薪（额外测试）"""
        original_salary = self.employee.annual_salary
        self.employee.give_raise(0)
        self.assertEqual(self.employee.annual_salary, original_salary)


# ==================== 额外练习：完整的测试示例 ====================

def get_formatted_name(first, last, middle=''):
    """生成整洁的姓名"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


class TestGetFormattedName(unittest.TestCase):
    """测试get_formatted_name函数"""
    
    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_middle_last_name(self):
        """能够正确处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


class AnonymousSurvey:
    """收集匿名调查问卷答案的类"""
    
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
    
    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)
    
    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    
    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


# ==================== 数学函数测试练习 ====================

def add_numbers(a, b):
    """加法函数"""
    return a + b


def multiply_numbers(a, b):
    """乘法函数"""
    return a * b


def divide_numbers(a, b):
    """除法函数"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def is_even(number):
    """判断数字是否为偶数"""
    return number % 2 == 0


def calculate_average(numbers):
    """计算数字列表的平均值"""
    if not numbers:
        raise ValueError("列表不能为空")
    return sum(numbers) / len(numbers)


class TestMathFunctions(unittest.TestCase):
    """测试数学函数"""
    
    def test_add_positive_numbers(self):
        """测试正数加法"""
        self.assertEqual(add_numbers(3, 4), 7)
        self.assertEqual(add_numbers(10, 15), 25)
    
    def test_add_negative_numbers(self):
        """测试负数加法"""
        self.assertEqual(add_numbers(-3, -4), -7)
        self.assertEqual(add_numbers(-5, 3), -2)
    
    def test_multiply_numbers(self):
        """测试乘法"""
        self.assertEqual(multiply_numbers(3, 4), 12)
        self.assertEqual(multiply_numbers(-2, 5), -10)
        self.assertEqual(multiply_numbers(0, 100), 0)
    
    def test_divide_numbers(self):
        """测试除法"""
        self.assertEqual(divide_numbers(10, 2), 5)
        self.assertAlmostEqual(divide_numbers(1, 3), 0.333333, places=5)
    
    def test_divide_by_zero(self):
        """测试除零错误"""
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)
    
    def test_is_even(self):
        """测试偶数判断"""
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(-3))
    
    def test_calculate_average(self):
        """测试平均值计算"""
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)
        self.assertAlmostEqual(calculate_average([1.5, 2.5]), 2.0)
    
    def test_calculate_average_empty_list(self):
        """测试空列表平均值"""
        with self.assertRaises(ValueError):
            calculate_average([])


# ==================== 字符串处理测试练习 ====================

def reverse_string(text):
    """反转字符串"""
    return text[::-1]


def count_words(text):
    """统计文本中的单词数"""
    if not text.strip():
        return 0
    return len(text.split())


def capitalize_words(text):
    """将文本中每个单词的首字母大写"""
    return ' '.join(word.capitalize() for word in text.split())


class TestStringFunctions(unittest.TestCase):
    """测试字符串处理函数"""
    
    def test_reverse_string(self):
        """测试字符串反转"""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")
    
    def test_count_words(self):
        """测试单词计数"""
        self.assertEqual(count_words("hello world"), 2)
        self.assertEqual(count_words("Python programming is fun"), 4)
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_words("   "), 0)
        self.assertEqual(count_words("single"), 1)
    
    def test_capitalize_words(self):
        """测试单词首字母大写"""
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python programming"), "Python Programming")
        self.assertEqual(capitalize_words(""), "")


# ==================== 主程序 ====================

def run_specific_tests():
    """运行特定的测试示例"""
    print("=" * 60)
    print("第11章 测试代码 - 练习演示")
    print("=" * 60)
    
    print("\n1. 测试城市国家函数：")
    print(f"city_country('beijing', 'china') = '{city_country('beijing', 'china')}'")
    print(f"city_country('tokyo', 'japan', 14000000) = '{city_country('tokyo', 'japan', 14000000)}'")
    
    print("\n2. 测试员工类：")
    emp = Employee('李', '四', 50000)
    print(f"员工: {emp.get_full_name()}, 初始年薪: {emp.annual_salary}")
    emp.give_raise()
    print(f"默认加薪后: {emp.annual_salary}")
    emp.give_raise(8000)
    print(f"加薪8000后: {emp.annual_salary}")
    
    print("\n3. 运行城市国家测试：")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCityCountry)
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        run_specific_tests()
    else:
        unittest.main()


"""
练习说明：

练习11-1：城市和国家
编写一个函数，它接受两个形参：一个城市名和一个国家名。这个函数返回一个格式为
City, Country（如Santiago, Chile）的字符串。将这个函数存储在一个名为city_functions.py的模块中。

练习11-2：人口数量
修改前面的函数，使其包含第三个必不可少的形参population，并返回一个格式为
City, Country - population xxx的字符串，如Santiago, Chile - population 5000000。
将这个函数存储在一个名为city_functions.py的模块中。

练习11-3：雇员
编写一个名为Employee的类，其方法__init__()接受名、姓和年薪，并将它们都存储在属性中。
编写一个名为give_raise()的方法，它默认将年薪增加5000美元，但也能够接受其他的年薪增加量。

运行方法：
1. 运行所有练习：python exercises.py
2. 运行特定测试：python -m unittest exercises.TestEmployee
3. 详细输出：python -m unittest -v exercises
""" 