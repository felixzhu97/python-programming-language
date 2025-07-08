#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第11章 测试代码 - 测试类
演示如何测试各种类和对象

主要内容：
1. 测试类的初始化
2. 测试类的方法
3. 测试类的属性
4. 测试继承关系
5. 使用setUp和tearDown
"""

import unittest
from unittest.mock import patch, MagicMock


# ==================== 被测试的类 ====================

class BankAccount:
    """银行账户类"""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        """存款"""
        if amount <= 0:
            raise ValueError("存款金额必须大于0")
        self.balance += amount
        self.transaction_history.append(f"存款: +{amount}")
        return self.balance
    
    def withdraw(self, amount):
        """取款"""
        if amount <= 0:
            raise ValueError("取款金额必须大于0")
        if amount > self.balance:
            raise ValueError("余额不足")
        self.balance -= amount
        self.transaction_history.append(f"取款: -{amount}")
        return self.balance
    
    def get_balance(self):
        """获取余额"""
        return self.balance
    
    def get_transaction_history(self):
        """获取交易历史"""
        return self.transaction_history.copy()


class Employee:
    """员工类"""
    
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, amount=5000):
        """加薪"""
        if amount < 0:
            raise ValueError("加薪金额不能为负数")
        self.annual_salary += amount
    
    def get_full_name(self):
        """获取全名"""
        return f"{self.first_name} {self.last_name}"
    
    def get_monthly_salary(self):
        """获取月薪"""
        return self.annual_salary / 12


class Calculator:
    """计算器类"""
    
    def __init__(self):
        self.result = 0
        self.history = []
    
    def add(self, value):
        """加法"""
        self.result += value
        self.history.append(f"+ {value} = {self.result}")
        return self.result
    
    def subtract(self, value):
        """减法"""
        self.result -= value
        self.history.append(f"- {value} = {self.result}")
        return self.result
    
    def multiply(self, value):
        """乘法"""
        self.result *= value
        self.history.append(f"* {value} = {self.result}")
        return self.result
    
    def divide(self, value):
        """除法"""
        if value == 0:
            raise ZeroDivisionError("除数不能为零")
        self.result /= value
        self.history.append(f"/ {value} = {self.result}")
        return self.result
    
    def clear(self):
        """清零"""
        self.result = 0
        self.history.clear()
    
    def get_history(self):
        """获取计算历史"""
        return self.history.copy()


class Temperature:
    """温度转换类"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        if value < -459.67:
            raise ValueError("温度不能低于绝对零度")
        self._celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        return self._celsius + 273.15


# ==================== 测试类 ====================

class TestBankAccount(unittest.TestCase):
    """测试银行账户类"""
    
    def setUp(self):
        """每个测试前创建银行账户实例"""
        self.account = BankAccount("123456", 1000)
    
    def test_initial_balance(self):
        """测试初始余额"""
        self.assertEqual(self.account.get_balance(), 1000)
        self.assertEqual(self.account.account_number, "123456")
    
    def test_deposit_valid_amount(self):
        """测试有效存款"""
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500)
        self.assertEqual(self.account.get_balance(), 1500)
    
    def test_deposit_invalid_amount(self):
        """测试无效存款"""
        with self.assertRaises(ValueError):
            self.account.deposit(0)
        
        with self.assertRaises(ValueError):
            self.account.deposit(-100)
    
    def test_withdraw_valid_amount(self):
        """测试有效取款"""
        new_balance = self.account.withdraw(300)
        self.assertEqual(new_balance, 700)
        self.assertEqual(self.account.get_balance(), 700)
    
    def test_withdraw_insufficient_funds(self):
        """测试余额不足"""
        with self.assertRaises(ValueError):
            self.account.withdraw(1500)
    
    def test_withdraw_invalid_amount(self):
        """测试无效取款金额"""
        with self.assertRaises(ValueError):
            self.account.withdraw(0)
        
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)
    
    def test_transaction_history(self):
        """测试交易历史"""
        self.account.deposit(200)
        self.account.withdraw(100)
        
        history = self.account.get_transaction_history()
        self.assertEqual(len(history), 2)
        self.assertIn("存款: +200", history)
        self.assertIn("取款: -100", history)


class TestEmployee(unittest.TestCase):
    """测试员工类"""
    
    def setUp(self):
        """每个测试前创建员工实例"""
        self.employee = Employee("张", "三", 60000)
    
    def test_employee_initialization(self):
        """测试员工初始化"""
        self.assertEqual(self.employee.first_name, "张")
        self.assertEqual(self.employee.last_name, "三")
        self.assertEqual(self.employee.annual_salary, 60000)
    
    def test_give_default_raise(self):
        """测试默认加薪"""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 65000)
    
    def test_give_custom_raise(self):
        """测试自定义加薪"""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 70000)
    
    def test_give_negative_raise(self):
        """测试负数加薪"""
        with self.assertRaises(ValueError):
            self.employee.give_raise(-1000)
    
    def test_get_full_name(self):
        """测试获取全名"""
        full_name = self.employee.get_full_name()
        self.assertEqual(full_name, "张 三")
    
    def test_get_monthly_salary(self):
        """测试获取月薪"""
        monthly_salary = self.employee.get_monthly_salary()
        self.assertAlmostEqual(monthly_salary, 5000, places=2)


class TestCalculator(unittest.TestCase):
    """测试计算器类"""
    
    def setUp(self):
        """每个测试前创建计算器实例"""
        self.calc = Calculator()
    
    def test_initial_state(self):
        """测试初始状态"""
        self.assertEqual(self.calc.result, 0)
        self.assertEqual(len(self.calc.get_history()), 0)
    
    def test_addition(self):
        """测试加法"""
        result = self.calc.add(5)
        self.assertEqual(result, 5)
        self.assertEqual(self.calc.result, 5)
    
    def test_subtraction(self):
        """测试减法"""
        self.calc.add(10)
        result = self.calc.subtract(3)
        self.assertEqual(result, 7)
    
    def test_multiplication(self):
        """测试乘法"""
        self.calc.add(4)
        result = self.calc.multiply(3)
        self.assertEqual(result, 12)
    
    def test_division(self):
        """测试除法"""
        self.calc.add(12)
        result = self.calc.divide(3)
        self.assertEqual(result, 4)
    
    def test_division_by_zero(self):
        """测试除零错误"""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(0)
    
    def test_clear(self):
        """测试清零"""
        self.calc.add(10)
        self.calc.clear()
        self.assertEqual(self.calc.result, 0)
        self.assertEqual(len(self.calc.get_history()), 0)
    
    def test_calculation_chain(self):
        """测试连续计算"""
        self.calc.add(10)
        self.calc.multiply(2)
        self.calc.subtract(5)
        
        self.assertEqual(self.calc.result, 15)
        history = self.calc.get_history()
        self.assertEqual(len(history), 3)


class TestTemperature(unittest.TestCase):
    """测试温度转换类"""
    
    def setUp(self):
        """每个测试前创建温度实例"""
        self.temp = Temperature(0)
    
    def test_celsius_initialization(self):
        """测试摄氏度初始化"""
        self.assertEqual(self.temp.celsius, 0)
    
    def test_celsius_to_fahrenheit(self):
        """测试摄氏度转华氏度"""
        self.temp.celsius = 100
        self.assertAlmostEqual(self.temp.fahrenheit, 212, places=1)
        
        self.temp.celsius = 0
        self.assertAlmostEqual(self.temp.fahrenheit, 32, places=1)
    
    def test_fahrenheit_to_celsius(self):
        """测试华氏度转摄氏度"""
        self.temp.fahrenheit = 212
        self.assertAlmostEqual(self.temp.celsius, 100, places=1)
        
        self.temp.fahrenheit = 32
        self.assertAlmostEqual(self.temp.celsius, 0, places=1)
    
    def test_celsius_to_kelvin(self):
        """测试摄氏度转开尔文"""
        self.temp.celsius = 0
        self.assertAlmostEqual(self.temp.kelvin, 273.15, places=2)
        
        self.temp.celsius = 100
        self.assertAlmostEqual(self.temp.kelvin, 373.15, places=2)
    
    def test_absolute_zero_celsius(self):
        """测试摄氏度绝对零度"""
        with self.assertRaises(ValueError):
            self.temp.celsius = -274
    
    def test_absolute_zero_fahrenheit(self):
        """测试华氏度绝对零度"""
        with self.assertRaises(ValueError):
            self.temp.fahrenheit = -460


class TestClassProperties(unittest.TestCase):
    """测试类属性和特殊情况"""
    
    def test_object_equality(self):
        """测试对象相等性"""
        account1 = BankAccount("123", 100)
        account2 = BankAccount("123", 100)
        
        # 不同的实例
        self.assertIsNot(account1, account2)
        
        # 但账户号相同
        self.assertEqual(account1.account_number, account2.account_number)
    
    def test_object_attributes(self):
        """测试对象属性"""
        emp = Employee("李", "四", 50000)
        
        # 测试属性存在
        self.assertTrue(hasattr(emp, 'first_name'))
        self.assertTrue(hasattr(emp, 'last_name'))
        self.assertTrue(hasattr(emp, 'annual_salary'))
        
        # 测试属性类型
        self.assertIsInstance(emp.first_name, str)
        self.assertIsInstance(emp.annual_salary, (int, float))


# ==================== 主程序 ====================

def demonstrate_class_testing():
    """演示类测试"""
    print("=" * 60)
    print("第11章 测试代码 - 类测试演示")
    print("=" * 60)
    
    print("\n1. 创建测试对象：")
    account = BankAccount("123456", 1000)
    print(f"银行账户: {account.account_number}, 余额: {account.get_balance()}")
    
    employee = Employee("张", "三", 60000)
    print(f"员工: {employee.get_full_name()}, 年薪: {employee.annual_salary}")
    
    print("\n2. 运行银行账户测试：")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBankAccount)
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        demonstrate_class_testing()
    else:
        unittest.main() 