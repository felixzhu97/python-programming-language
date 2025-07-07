#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第05章 if语句 - 条件测试
演示各种条件测试的用法和布尔表达式
"""

def main():
    print("=== 条件测试演示 ===\n")
    
    # 1. 基本条件测试
    print("1. 基本条件测试")
    print("-" * 30)
    
    car = 'bmw'
    print(f"car = '{car}'")
    print(f"car == 'bmw': {car == 'bmw'}")
    print(f"car == 'audi': {car == 'audi'}")
    print(f"car == 'BMW': {car == 'BMW'}")
    print()
    
    # 2. 检查是否相等时忽略大小写
    print("2. 忽略大小写的比较")
    print("-" * 30)
    
    car = 'Audi'
    print(f"car = '{car}'")
    print(f"car.lower() == 'audi': {car.lower() == 'audi'}")
    print(f"原始值未变：car = '{car}'")
    print()
    
    # 3. 检查是否不相等
    print("3. 检查是否不相等")
    print("-" * 30)
    
    requested_topping = 'mushrooms'
    print(f"requested_topping = '{requested_topping}'")
    
    if requested_topping != 'anchovies':
        print("Hold the anchovies!")
    
    print(f"requested_topping != 'anchovies': {requested_topping != 'anchovies'}")
    print(f"requested_topping != 'mushrooms': {requested_topping != 'mushrooms'}")
    print()
    
    # 4. 数值比较
    print("4. 数值比较")
    print("-" * 30)
    
    age = 18
    print(f"age = {age}")
    print(f"age == 18: {age == 18}")
    print(f"age == 20: {age == 20}")
    print(f"age != 18: {age != 18}")
    print(f"age < 21: {age < 21}")
    print(f"age <= 18: {age <= 18}")
    print(f"age > 16: {age > 16}")
    print(f"age >= 18: {age >= 18}")
    print()
    
    # 5. 使用and和or检查多个条件
    print("5. 使用and和or检查多个条件")
    print("-" * 30)
    
    age_0 = 22
    age_1 = 18
    
    print(f"age_0 = {age_0}, age_1 = {age_1}")
    print(f"age_0 >= 21 and age_1 >= 21: {age_0 >= 21 and age_1 >= 21}")
    print(f"age_0 >= 21 or age_1 >= 21: {age_0 >= 21 or age_1 >= 21}")
    
    # 更复杂的条件
    print(f"age_0 > 20 and age_1 < 20: {age_0 > 20 and age_1 < 20}")
    print(f"age_0 == 22 or age_1 == 22: {age_0 == 22 or age_1 == 22}")
    print()
    
    # 6. 检查特定值是否包含在列表中
    print("6. 检查值是否在列表中")
    print("-" * 30)
    
    requested_toppings = ['mushrooms', 'onions', 'pineapple']
    print(f"requested_toppings = {requested_toppings}")
    
    print(f"'mushrooms' in requested_toppings: {'mushrooms' in requested_toppings}")
    print(f"'pepperoni' in requested_toppings: {'pepperoni' in requested_toppings}")
    
    # 字符串包含检查
    message = "Hello, Python world!"
    print(f"message = '{message}'")
    print(f"'Python' in message: {'Python' in message}")
    print(f"'Java' in message: {'Java' in message}")
    print()
    
    # 7. 检查特定值是否不包含在列表中
    print("7. 检查值是否不在列表中")
    print("-" * 30)
    
    banned_users = ['andrew', 'carolina', 'david']
    user = 'marie'
    
    print(f"banned_users = {banned_users}")
    print(f"user = '{user}'")
    
    if user not in banned_users:
        print(f"{user.title()} can post a message.")
    
    print(f"user not in banned_users: {user not in banned_users}")
    print(f"'andrew' not in banned_users: {'andrew' not in banned_users}")
    print()
    
    # 8. 布尔表达式
    print("8. 布尔表达式")
    print("-" * 30)
    
    game_active = True
    can_edit = False
    
    print(f"game_active = {game_active}")
    print(f"can_edit = {can_edit}")
    print(f"not game_active: {not game_active}")
    print(f"not can_edit: {not can_edit}")
    
    # 布尔值的运算
    print(f"game_active and can_edit: {game_active and can_edit}")
    print(f"game_active or can_edit: {game_active or can_edit}")
    print()
    
    # 9. 复杂条件测试
    print("9. 复杂条件测试")
    print("-" * 30)
    
    # 学生信息
    name = "Alice"
    age = 20
    grade = 85
    is_active = True
    courses = ['Math', 'Physics', 'Chemistry']
    
    print(f"学生信息：")
    print(f"  姓名：{name}")
    print(f"  年龄：{age}")
    print(f"  成绩：{grade}")
    print(f"  是否在校：{is_active}")
    print(f"  选修课程：{courses}")
    
    # 各种条件测试
    print(f"\n条件测试结果：")
    print(f"姓名是Alice：{name == 'Alice'}")
    print(f"年龄大于18：{age > 18}")
    print(f"成绩及格：{grade >= 60}")
    print(f"成绩优秀：{grade >= 90}")
    print(f"学生在校且成绩及格：{is_active and grade >= 60}")
    print(f"学生不在校或成绩不及格：{not is_active or grade < 60}")
    print(f"选修了数学：{'Math' in courses}")
    print(f"没有选修英语：{'English' not in courses}")
    print()
    
    # 10. 条件测试的优先级
    print("10. 条件测试的优先级")
    print("-" * 30)
    
    # 演示运算符优先级
    a, b, c = 5, 10, 15
    print(f"a = {a}, b = {b}, c = {c}")
    
    # 比较运算符优先级高于逻辑运算符
    result1 = a < b and b < c
    result2 = (a < b) and (b < c)
    print(f"a < b and b < c: {result1}")
    print(f"(a < b) and (b < c): {result2}")
    print(f"结果相同：{result1 == result2}")
    
    # not 的优先级
    result3 = not a > b
    result4 = not (a > b)
    print(f"not a > b: {result3}")
    print(f"not (a > b): {result4}")
    print(f"结果相同：{result3 == result4}")
    
    # 复杂表达式
    result5 = a < b or not c > b and a != 0
    result6 = (a < b) or ((not (c > b)) and (a != 0))
    print(f"复杂表达式：{result5}")
    print(f"加括号后：{result6}")
    print(f"结果相同：{result5 == result6}")
    print()
    
    # 11. 实际应用示例
    print("11. 实际应用示例")
    print("-" * 30)
    
    # 用户权限检查
    username = "admin"
    password = "123456"
    is_logged_in = True
    user_role = "administrator"
    
    print(f"用户认证信息：")
    print(f"  用户名：{username}")
    print(f"  密码：{'*' * len(password)}")
    print(f"  已登录：{is_logged_in}")
    print(f"  用户角色：{user_role}")
    
    # 权限检查
    can_access_admin = is_logged_in and user_role == "administrator"
    can_edit_content = is_logged_in and (user_role == "administrator" or user_role == "editor")
    can_view_content = is_logged_in or user_role == "guest"
    
    print(f"\n权限检查结果：")
    print(f"可以访问管理页面：{can_access_admin}")
    print(f"可以编辑内容：{can_edit_content}")
    print(f"可以查看内容：{can_view_content}")
    
    # 商品库存检查
    print(f"\n商品库存检查：")
    product_name = "iPhone"
    stock_quantity = 5
    min_stock = 10
    is_on_sale = True
    price = 999.99
    
    in_stock = stock_quantity > 0
    low_stock = stock_quantity < min_stock
    affordable = price < 1000
    good_deal = is_on_sale and affordable
    
    print(f"商品：{product_name}")
    print(f"库存：{stock_quantity}")
    print(f"有库存：{in_stock}")
    print(f"库存不足：{low_stock}")
    print(f"价格合适：{affordable}")
    print(f"好的交易：{good_deal}")
    print()
    
    # 12. 条件测试的最佳实践
    print("12. 条件测试的最佳实践")
    print("-" * 30)
    
    # 使用括号提高可读性
    age = 25
    income = 50000
    credit_score = 750
    
    # 不好的写法
    eligible_bad = age >= 18 and income > 30000 or credit_score > 700 and age < 65
    
    # 好的写法
    eligible_good = (age >= 18 and income > 30000) or (credit_score > 700 and age < 65)
    
    print(f"年龄：{age}")
    print(f"收入：{income}")
    print(f"信用评分：{credit_score}")
    print(f"不清晰的条件：{eligible_bad}")
    print(f"清晰的条件：{eligible_good}")
    
    # 使用变量存储复杂条件
    is_adult = age >= 18
    has_good_income = income > 30000
    has_good_credit = credit_score > 700
    is_senior = age >= 65
    
    eligible_clear = (is_adult and has_good_income) or (has_good_credit and not is_senior)
    print(f"最清晰的写法：{eligible_clear}")
    
    print("\n条件测试总结：")
    print("1. 使用 == 检查相等，!= 检查不相等")
    print("2. 使用 <, <=, >, >= 进行数值比较")
    print("3. 使用 and, or, not 组合条件")
    print("4. 使用 in 和 not in 检查列表包含")
    print("5. 使用括号提高表达式可读性")
    print("6. 将复杂条件分解为简单变量")


if __name__ == "__main__":
    main() 