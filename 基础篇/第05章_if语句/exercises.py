#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第05章 if语句 - 练习题解答
包含第5章所有练习题的详细解答
"""

def main():
    print("=== 第05章 if语句 - 练习题解答 ===\n")
    
    # 练习 5-1：条件测试
    print("练习 5-1：条件测试")
    print("-" * 30)
    
    # 编写一系列条件测试
    car = 'subaru'
    
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
    print()
    
    print("Is car == 'audi'? I predict False.")
    print(car == 'audi')
    print()
    
    # 更多条件测试
    age = 25
    print("Is age >= 18? I predict True.")
    print(age >= 18)
    print()
    
    print("Is age < 18? I predict False.")
    print(age < 18)
    print()
    
    numbers = [1, 2, 3, 4, 5]
    print("Is 3 in numbers? I predict True.")
    print(3 in numbers)
    print()
    
    print("Is 10 in numbers? I predict False.")
    print(10 in numbers)
    print()
    
    name = 'Alice'
    print("Is name.lower() == 'alice'? I predict True.")
    print(name.lower() == 'alice')
    print()
    
    print("Is name == 'alice'? I predict False.")
    print(name == 'alice')
    print()
    
    score = 85
    print("Is score >= 80 and score < 90? I predict True.")
    print(score >= 80 and score < 90)
    print()
    
    print("Is score > 90 or score < 60? I predict False.")
    print(score > 90 or score < 60)
    print()
    
    # 练习 5-2：更多的条件测试
    print("练习 5-2：更多的条件测试")
    print("-" * 30)
    
    # 相等和不等测试
    print("相等和不等测试：")
    x = 10
    y = 20
    print(f"x = {x}, y = {y}")
    print(f"x == y: {x == y}")
    print(f"x != y: {x != y}")
    print()
    
    # 使用lower()函数的测试
    print("使用lower()函数的测试：")
    text = "Hello World"
    print(f"原始文本：{text}")
    print(f"text.lower() == 'hello world': {text.lower() == 'hello world'}")
    print(f"text == 'hello world': {text == 'hello world'}")
    print()
    
    # 数值比较测试
    print("数值比较测试：")
    num1 = 15
    num2 = 25
    print(f"num1 = {num1}, num2 = {num2}")
    print(f"num1 > num2: {num1 > num2}")
    print(f"num1 < num2: {num1 < num2}")
    print(f"num1 >= 15: {num1 >= 15}")
    print(f"num2 <= 25: {num2 <= 25}")
    print()
    
    # 使用关键字and和or的测试
    print("使用关键字and和or的测试：")
    a = 5
    b = 10
    c = 15
    print(f"a = {a}, b = {b}, c = {c}")
    print(f"a < b and b < c: {a < b and b < c}")
    print(f"a > b and b < c: {a > b and b < c}")
    print(f"a < b or a > c: {a < b or a > c}")
    print(f"a > b or a > c: {a > b or a > c}")
    print()
    
    # 测试特定的值是否包含在列表中
    print("测试特定的值是否包含在列表中：")
    fruits = ['apple', 'banana', 'orange', 'grape']
    print(f"水果列表：{fruits}")
    print(f"'apple' in fruits: {'apple' in fruits}")
    print(f"'mango' in fruits: {'mango' in fruits}")
    print()
    
    # 测试特定的值是否未包含在列表中
    print("测试特定的值是否未包含在列表中：")
    print(f"'mango' not in fruits: {'mango' not in fruits}")
    print(f"'apple' not in fruits: {'apple' not in fruits}")
    print()
    
    # 练习 5-3：外星人颜色 #1
    print("练习 5-3：外星人颜色 #1")
    print("-" * 30)
    
    alien_color = 'green'
    print(f"外星人颜色：{alien_color}")
    
    if alien_color == 'green':
        print("玩家获得了5个点！")
    print()
    
    # 换一种颜色测试
    alien_color = 'red'
    print(f"外星人颜色：{alien_color}")
    
    if alien_color == 'green':
        print("玩家获得了5个点！")
    print("(没有输出，因为条件为False)")
    print()
    
    # 练习 5-4：外星人颜色 #2
    print("练习 5-4：外星人颜色 #2")
    print("-" * 30)
    
    alien_color = 'green'
    print(f"外星人颜色：{alien_color}")
    
    if alien_color == 'green':
        print("玩家获得了5个点！")
    else:
        print("玩家获得了10个点！")
    print()
    
    # 换一种颜色测试
    alien_color = 'yellow'
    print(f"外星人颜色：{alien_color}")
    
    if alien_color == 'green':
        print("玩家获得了5个点！")
    else:
        print("玩家获得了10个点！")
    print()
    
    # 练习 5-5：外星人颜色 #3
    print("练习 5-5：外星人颜色 #3")
    print("-" * 30)
    
    def alien_points(color):
        """根据外星人颜色返回得分"""
        print(f"外星人颜色：{color}")
        if color == 'green':
            points = 5
            print(f"玩家获得了{points}个点！")
        elif color == 'yellow':
            points = 10
            print(f"玩家获得了{points}个点！")
        elif color == 'red':
            points = 15
            print(f"玩家获得了{points}个点！")
        else:
            points = 0
            print("未知的外星人颜色！")
        return points
    
    # 测试三种颜色
    colors = ['green', 'yellow', 'red']
    for color in colors:
        alien_points(color)
        print()
    
    # 练习 5-6：人生的不同阶段
    print("练习 5-6：人生的不同阶段")
    print("-" * 30)
    
    def life_stage(age):
        """根据年龄判断人生阶段"""
        print(f"年龄：{age}岁")
        if age < 2:
            stage = "婴儿"
        elif age < 4:
            stage = "幼儿"
        elif age < 13:
            stage = "儿童"
        elif age < 20:
            stage = "青少年"
        elif age < 65:
            stage = "成年人"
        else:
            stage = "老年人"
        
        print(f"人生阶段：{stage}")
        return stage
    
    # 测试不同年龄
    ages = [1, 3, 8, 16, 30, 70]
    for age in ages:
        life_stage(age)
        print()
    
    # 练习 5-7：喜欢的水果
    print("练习 5-7：喜欢的水果")
    print("-" * 30)
    
    favorite_fruits = ['apple', 'banana', 'orange']
    print(f"我喜欢的水果：{favorite_fruits}")
    print()
    
    # 检查特定水果
    test_fruits = ['apple', 'grape', 'banana', 'mango', 'orange']
    
    for fruit in test_fruits:
        if fruit in favorite_fruits:
            print(f"你真的很喜欢{fruit}！")
        else:
            print(f"{fruit}不在你的喜欢列表中。")
    print()
    
    # 练习 5-8：以特殊方式跟管理员打招呼
    print("练习 5-8：以特殊方式跟管理员打招呼")
    print("-" * 30)
    
    usernames = ['admin', 'alice', 'bob', 'charlie', 'david']
    print(f"用户名列表：{usernames}")
    print()
    
    for username in usernames:
        if username == 'admin':
            print(f"你好{username}，你想看到状态报告吗？")
        else:
            print(f"你好{username}，感谢你再次登录！")
    print()
    
    # 练习 5-9：处理没有用户的情形
    print("练习 5-9：处理没有用户的情形")
    print("-" * 30)
    
    # 有用户的情况
    usernames = ['admin', 'alice', 'bob']
    print(f"用户名列表：{usernames}")
    
    if usernames:
        for username in usernames:
            if username == 'admin':
                print(f"你好{username}，你想看到状态报告吗？")
            else:
                print(f"你好{username}，感谢你再次登录！")
    else:
        print("我们需要找到一些用户！")
    print()
    
    # 空用户列表的情况
    usernames = []
    print(f"空用户名列表：{usernames}")
    
    if usernames:
        for username in usernames:
            if username == 'admin':
                print(f"你好{username}，你想看到状态报告吗？")
            else:
                print(f"你好{username}，感谢你再次登录！")
    else:
        print("我们需要找到一些用户！")
    print()
    
    # 练习 5-10：检查用户名
    print("练习 5-10：检查用户名")
    print("-" * 30)
    
    current_users = ['alice', 'bob', 'charlie', 'david', 'eve']
    new_users = ['frank', 'Alice', 'BOB', 'grace', 'henry']
    
    print(f"当前用户：{current_users}")
    print(f"新用户：{new_users}")
    print()
    
    # 将当前用户名转换为小写用于比较
    current_users_lower = [user.lower() for user in current_users]
    
    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print(f"用户名'{new_user}'已被占用，请输入别的用户名！")
        else:
            print(f"用户名'{new_user}'可以使用。")
    print()
    
    # 练习 5-11：序数
    print("练习 5-11：序数")
    print("-" * 30)
    
    def get_ordinal(number):
        """返回数字的序数形式"""
        if number == 1:
            return "1st"
        elif number == 2:
            return "2nd"
        elif number == 3:
            return "3rd"
        else:
            return f"{number}th"
    
    numbers = list(range(1, 10))
    print(f"数字列表：{numbers}")
    print()
    
    for number in numbers:
        ordinal = get_ordinal(number)
        print(f"{ordinal}")
    print()
    
    # 额外练习：复杂的条件逻辑
    print("额外练习：复杂的条件逻辑")
    print("-" * 30)
    
    # 学生成绩管理系统
    def grade_system():
        """学生成绩管理系统"""
        print("学生成绩管理系统")
        print("=" * 20)
        
        students = {
            'Alice': {'math': 95, 'english': 87, 'science': 92},
            'Bob': {'math': 78, 'english': 82, 'science': 75},
            'Charlie': {'math': 88, 'english': 91, 'science': 85},
            'David': {'math': 62, 'english': 58, 'science': 65}
        }
        
        for student, scores in students.items():
            print(f"\n学生：{student}")
            print(f"成绩：{scores}")
            
            # 计算平均分
            average = sum(scores.values()) / len(scores)
            print(f"平均分：{average:.1f}")
            
            # 判断等级
            if average >= 90:
                grade = 'A'
                comment = "优秀"
            elif average >= 80:
                grade = 'B'
                comment = "良好"
            elif average >= 70:
                grade = 'C'
                comment = "中等"
            elif average >= 60:
                grade = 'D'
                comment = "及格"
            else:
                grade = 'F'
                comment = "不及格"
            
            print(f"等级：{grade} ({comment})")
            
            # 检查是否有科目不及格
            failed_subjects = [subject for subject, score in scores.items() if score < 60]
            if failed_subjects:
                print(f"不及格科目：{failed_subjects}")
            
            # 检查是否有科目优秀
            excellent_subjects = [subject for subject, score in scores.items() if score >= 90]
            if excellent_subjects:
                print(f"优秀科目：{excellent_subjects}")
    
    grade_system()
    print()
    
    # 购物车结算系统
    def shopping_cart():
        """购物车结算系统"""
        print("购物车结算系统")
        print("=" * 20)
        
        cart = {
            'apple': {'price': 5.5, 'quantity': 3},
            'banana': {'price': 3.2, 'quantity': 6},
            'orange': {'price': 4.8, 'quantity': 2},
            'milk': {'price': 12.5, 'quantity': 1}
        }
        
        print("购物车内容：")
        total = 0
        for item, details in cart.items():
            price = details['price']
            quantity = details['quantity']
            subtotal = price * quantity
            total += subtotal
            print(f"{item}: ¥{price} × {quantity} = ¥{subtotal:.2f}")
        
        print(f"\n小计：¥{total:.2f}")
        
        # 应用折扣
        discount = 0
        if total >= 100:
            discount = 0.1  # 10%折扣
            print("满100元享受9折优惠！")
        elif total >= 50:
            discount = 0.05  # 5%折扣
            print("满50元享受95折优惠！")
        
        discount_amount = total * discount
        final_total = total - discount_amount
        
        if discount > 0:
            print(f"折扣：¥{discount_amount:.2f}")
            print(f"最终金额：¥{final_total:.2f}")
        else:
            print(f"最终金额：¥{total:.2f}")
        
        # 运费计算
        if final_total >= 99:
            print("免运费！")
        else:
            shipping = 10
            print(f"运费：¥{shipping}")
            print(f"总计：¥{final_total + shipping:.2f}")
    
    shopping_cart()
    print()
    
    # 游戏角色状态系统
    def game_character():
        """游戏角色状态系统"""
        print("游戏角色状态系统")
        print("=" * 20)
        
        character = {
            'name': '勇士',
            'level': 15,
            'health': 45,
            'max_health': 100,
            'mana': 30,
            'max_mana': 80,
            'experience': 2450,
            'gold': 150
        }
        
        print(f"角色：{character['name']}")
        print(f"等级：{character['level']}")
        print(f"生命值：{character['health']}/{character['max_health']}")
        print(f"法力值：{character['mana']}/{character['max_mana']}")
        print(f"经验值：{character['experience']}")
        print(f"金币：{character['gold']}")
        print()
        
        # 健康状态检查
        health_percentage = character['health'] / character['max_health']
        if health_percentage <= 0.2:
            health_status = "危险"
            print("⚠️ 健康状态：危险！需要立即治疗！")
        elif health_percentage <= 0.5:
            health_status = "一般"
            print("⚠️ 健康状态：一般，建议治疗")
        else:
            health_status = "良好"
            print("✅ 健康状态：良好")
        
        # 法力状态检查
        mana_percentage = character['mana'] / character['max_mana']
        if mana_percentage <= 0.3:
            print("⚠️ 法力不足，建议休息恢复")
        else:
            print("✅ 法力充足")
        
        # 升级检查
        next_level_exp = character['level'] * 200
        if character['experience'] >= next_level_exp:
            print("🎉 经验值足够，可以升级！")
        else:
            needed_exp = next_level_exp - character['experience']
            print(f"还需要 {needed_exp} 经验值可升级")
        
        # 财富状态
        if character['gold'] >= 1000:
            print("💰 你很富有！")
        elif character['gold'] >= 100:
            print("💰 你有一些积蓄")
        else:
            print("💰 你需要更多金币")
    
    game_character()
    print()
    
    print("=== 第05章练习完成 ===")
    print("主要学习了：")
    print("1. 条件测试和布尔表达式")
    print("2. if、elif、else语句的使用")
    print("3. 列表和字符串的条件检查")
    print("4. 逻辑运算符的使用")
    print("5. 实际应用中的复杂条件判断")


if __name__ == "__main__":
    main() 