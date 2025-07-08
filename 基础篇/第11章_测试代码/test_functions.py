#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第11章 测试代码 - 测试函数
演示如何测试各种类型的函数

主要内容：
1. 测试返回值的函数
2. 测试有参数的函数
3. 测试异常情况
4. 使用Mock对象测试
"""

import unittest
import unittest.mock as mock
import tempfile
import os
from io import StringIO


# ==================== 被测试的函数 ====================

def calculate_area(length, width):
    """计算矩形面积"""
    if length <= 0 or width <= 0:
        raise ValueError("长度和宽度必须大于0")
    return length * width


def factorial(n):
    """计算阶乘"""
    if n < 0:
        raise ValueError("不能计算负数的阶乘")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def process_text(text, uppercase=False, remove_spaces=False):
    """处理文本"""
    if not isinstance(text, str):
        raise TypeError("输入必须是字符串")
    
    result = text
    if uppercase:
        result = result.upper()
    if remove_spaces:
        result = result.replace(' ', '')
    
    return result


def read_file_content(filename):
    """读取文件内容"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"文件 {filename} 不存在")


def send_email(to_address, subject, body):
    """模拟发送邮件"""
    if not to_address or '@' not in to_address:
        raise ValueError("无效的邮件地址")
    
    print(f"发送邮件到: {to_address}")
    print(f"主题: {subject}")
    return True


def print_message(message):
    """打印消息"""
    print(f"消息: {message}")


# ==================== 测试类 ====================

class TestCalculateFunctions(unittest.TestCase):
    """测试计算函数"""
    
    def test_calculate_area_positive(self):
        """测试正数面积计算"""
        result = calculate_area(5, 3)
        self.assertEqual(result, 15)
    
    def test_calculate_area_zero(self):
        """测试零值输入"""
        with self.assertRaises(ValueError):
            calculate_area(0, 5)
    
    def test_factorial_base_cases(self):
        """测试阶乘基础情况"""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
    
    def test_factorial_negative(self):
        """测试负数阶乘"""
        with self.assertRaises(ValueError):
            factorial(-1)


class TestTextProcessing(unittest.TestCase):
    """测试文本处理函数"""
    
    def test_process_text_default(self):
        """测试默认参数"""
        result = process_text("Hello World")
        self.assertEqual(result, "Hello World")
    
    def test_process_text_uppercase(self):
        """测试大写转换"""
        result = process_text("Hello World", uppercase=True)
        self.assertEqual(result, "HELLO WORLD")
    
    def test_process_text_invalid_input(self):
        """测试无效输入"""
        with self.assertRaises(TypeError):
            process_text(123)


class TestFileOperations(unittest.TestCase):
    """测试文件操作函数"""
    
    def setUp(self):
        """创建临时文件"""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8')
        self.temp_filename = self.temp_file.name
        self.temp_file.write("测试内容")
        self.temp_file.close()
    
    def tearDown(self):
        """清理临时文件"""
        if os.path.exists(self.temp_filename):
            os.unlink(self.temp_filename)
    
    def test_read_existing_file(self):
        """测试读取存在的文件"""
        content = read_file_content(self.temp_filename)
        self.assertEqual(content, "测试内容")
    
    def test_read_nonexistent_file(self):
        """测试读取不存在的文件"""
        with self.assertRaises(FileNotFoundError):
            read_file_content("nonexistent_file.txt")


class TestEmailFunction(unittest.TestCase):
    """测试邮件发送函数"""
    
    @mock.patch('builtins.print')
    def test_send_email_valid(self, mock_print):
        """测试发送有效邮件"""
        result = send_email('test@example.com', '测试主题', '测试内容')
        self.assertTrue(result)
        self.assertEqual(mock_print.call_count, 2)
    
    def test_send_email_invalid_address(self):
        """测试无效邮件地址"""
        with self.assertRaises(ValueError):
            send_email('invalid-email', '主题', '内容')


class TestSideEffectFunctions(unittest.TestCase):
    """测试有副作用的函数"""
    
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_print_message(self, mock_stdout):
        """测试打印函数"""
        test_message = "测试消息"
        print_message(test_message)
        
        output = mock_stdout.getvalue()
        self.assertIn(test_message, output)


class TestParameterizedTests(unittest.TestCase):
    """演示参数化测试"""
    
    def test_multiple_area_calculations(self):
        """使用subTest进行参数化测试"""
        test_cases = [
            (1, 1, 1),
            (2, 3, 6),
            (5, 4, 20),
        ]
        
        for length, width, expected in test_cases:
            with self.subTest(length=length, width=width):
                result = calculate_area(length, width)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main() 