#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第05章 if语句 - if语句基本用法
演示if语句的各种形式和用法
"""

def main():
    print("=== if语句基本用法演示 ===\n")
    
    # 1. 简单的if语句
    print("1. 简单的if语句")
    print("-" * 30)
    
    age = 19
    print(f"年龄：{age}")
    
    if age >= 18:
        print("你已经成年了！")
        print("你可以投票了。")
    
    print("程序继续执行...")
    print()
    
    # 2. if-else语句
    print("2. if-else语句")
    print("-" * 30)
    
    age = 17
    print(f"年龄：{age}")
    
    if age >= 18:
        print("你已经成年了！")
        print("你可以投票了。")
    else:
        print("你还未成年。")
        print("等你满18岁后就可以投票了。")
    
    print()
    
    # 3. if-elif-else语句链
    print("3. if-elif-else语句链")
    print("-" * 30)
    
    age = 12
    print(f"年龄：{age}")
    
    if age < 4:
        print("你的票价是0元。")
    elif age < 18:
        print("你的票价是10元。")
    else:
        print("你的票价是15元。")
    
    # 多个elif
    print(f"\n不同年龄段的票价：")
    ages = [2, 8, 16, 25, 70]
    
    for age in ages:
        print(f"年龄{age}岁：", end="")
        if age < 4:
            price = 0
        elif age < 18:
            price = 10
        elif age < 65:
            price = 15
        else:
            price = 8
        print(f"票价{price}元")
    
    print()
    
    # 4. 测试多个条件
    print("4. 测试多个条件")
    print("-" * 30)
    
    requested_toppings = ['mushrooms', 'extra cheese']
    print(f"请求的配料：{requested_toppings}")
    
    # 使用多个if语句检查每个条件
    if 'mushrooms' in requested_toppings:
        print("添加蘑菇。")
    
    if 'pepperoni' in requested_toppings:
        print("添加意大利辣香肠。")
    
    if 'extra cheese' in requested_toppings:
        print("添加额外的奶酪。")
    
    print("制作披萨完成！")
    print()
    
    # 5. 在for循环中使用if语句
    print("5. 在for循环中使用if语句")
    print("-" * 30)
    
    requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
    print(f"订单配料：{requested_toppings}")
    
    for requested_topping in requested_toppings:
        print(f"添加{requested_topping}。")
    
    print("\n特殊处理某些配料：")
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("抱歉，我们现在没有青椒了。")
        else:
            print(f"添加{requested_topping}。")
    
    print("披萨制作完成！")
    print()
    
    # 6. 确定列表不是空的
    print("6. 确定列表不是空的")
    print("-" * 30)
    
    # 非空列表
    requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
    print(f"配料列表：{requested_toppings}")
    
    if requested_toppings:
        for requested_topping in requested_toppings:
            print(f"添加{requested_topping}。")
        print("披萨制作完成！")
    else:
        print("您确定要普通披萨吗？")
    
    print()
    
    # 空列表
    requested_toppings = []
    print(f"空配料列表：{requested_toppings}")
    
    if requested_toppings:
        for requested_topping in requested_toppings:
            print(f"添加{requested_topping}。")
        print("披萨制作完成！")
    else:
        print("您确定要普通披萨吗？")
    
    print()
    
    # 7. 使用多个列表
    print("7. 使用多个列表")
    print("-" * 30)
    
    available_toppings = ['mushrooms', 'olives', 'green peppers',
                         'pepperoni', 'pineapple', 'extra cheese']
    requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
    
    print(f"可用配料：{available_toppings}")
    print(f"请求配料：{requested_toppings}")
    print()
    
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"添加{requested_topping}。")
        else:
            print(f"抱歉，我们没有{requested_topping}。")
    
    print("披萨制作完成！")
    print()
    
    # 8. 实际应用示例：用户登录系统
    print("8. 实际应用示例：用户登录系统")
    print("-" * 30)
    
    users = {
        'admin': 'password123',
        'alice': 'alice123',
        'bob': 'bob456'
    }
    
    username = 'alice'
    password = 'alice123'
    
    print(f"尝试登录 - 用户名：{username}")
    
    if username in users:
        if users[username] == password:
            if username == 'admin':
                print("管理员登录成功！")
                print("您拥有所有权限。")
            else:
                print(f"用户{username}登录成功！")
                print("欢迎回来！")
        else:
            print("密码错误！")
    else:
        print("用户名不存在！")
    
    print()
    
    # 9. 成绩评级系统
    print("9. 成绩评级系统")
    print("-" * 30)
    
    scores = [95, 87, 76, 64, 52, 89, 91]
    print(f"学生成绩：{scores}")
    print()
    
    for i, score in enumerate(scores, 1):
        print(f"学生{i}（{score}分）：", end="")
        
        if score >= 90:
            grade = 'A'
            comment = "优秀"
        elif score >= 80:
            grade = 'B'
            comment = "良好"
        elif score >= 70:
            grade = 'C'
            comment = "中等"
        elif score >= 60:
            grade = 'D'
            comment = "及格"
        else:
            grade = 'F'
            comment = "不及格"
        
        print(f"等级{grade}，{comment}")
    
    print()
    
    # 10. 商品折扣系统
    print("10. 商品折扣系统")
    print("-" * 30)
    
    def calculate_discount(amount, is_vip=False, is_student=False):
        """计算折扣后价格"""
        original_price = amount
        discount = 0
        
        if is_vip and is_student:
            discount = 0.25  # VIP学生：75折
            category = "VIP学生"
        elif is_vip:
            discount = 0.15  # VIP：85折
            category = "VIP客户"
        elif is_student:
            discount = 0.10  # 学生：9折
            category = "学生"
        elif amount >= 1000:
            discount = 0.08  # 大额订单：92折
            category = "大额订单"
        elif amount >= 500:
            discount = 0.05  # 中额订单：95折
            category = "中额订单"
        else:
            discount = 0
            category = "普通订单"
        
        final_price = amount * (1 - discount)
        saved = amount - final_price
        
        return {
            'original_price': original_price,
            'discount': discount,
            'final_price': final_price,
            'saved': saved,
            'category': category
        }
    
    # 测试不同客户类型
    test_cases = [
        (800, False, False),
        (800, True, False),
        (800, False, True),
        (800, True, True),
        (300, False, True),
        (1200, False, False)
    ]
    
    for amount, is_vip, is_student in test_cases:
        result = calculate_discount(amount, is_vip, is_student)
        print(f"订单金额：¥{amount}")
        print(f"客户类型：{result['category']}")
        print(f"折扣：{result['discount']*100:.0f}%")
        print(f"最终价格：¥{result['final_price']:.2f}")
        print(f"节省：¥{result['saved']:.2f}")
        print("-" * 20)
    
    # 11. 天气穿衣建议系统
    print("11. 天气穿衣建议系统")
    print("-" * 30)
    
    def get_clothing_advice(temperature, is_raining=False, wind_speed=0):
        """根据天气给出穿衣建议"""
        advice = []
        
        # 根据温度
        if temperature >= 30:
            advice.append("穿短袖短裤")
            advice.append("注意防晒")
        elif temperature >= 25:
            advice.append("穿轻薄衣物")
        elif temperature >= 20:
            advice.append("穿长袖衬衫")
        elif temperature >= 15:
            advice.append("穿薄外套")
        elif temperature >= 10:
            advice.append("穿厚外套")
        elif temperature >= 0:
            advice.append("穿羽绒服")
        else:
            advice.append("穿厚重冬装")
            advice.append("注意保暖")
        
        # 根据降雨
        if is_raining:
            advice.append("带雨伞或穿雨衣")
        
        # 根据风力
        if wind_speed > 15:
            advice.append("穿防风衣物")
        elif wind_speed > 8:
            advice.append("注意防风")
        
        return advice
    
    weather_conditions = [
        (28, False, 5),
        (15, True, 3),
        (5, False, 12),
        (-5, True, 20),
        (22, False, 0)
    ]
    
    for temp, rain, wind in weather_conditions:
        print(f"温度：{temp}°C", end="")
        if rain:
            print("，下雨", end="")
        if wind > 0:
            print(f"，风速{wind}m/s", end="")
        print()
        
        advice = get_clothing_advice(temp, rain, wind)
        for tip in advice:
            print(f"  - {tip}")
        print()
    
    # 12. if语句的最佳实践
    print("12. if语句的最佳实践")
    print("-" * 30)
    
    print("最佳实践总结：")
    print("1. 保持条件简洁明了")
    print("2. 使用有意义的变量名")
    print("3. 避免过深的嵌套")
    print("4. 优先处理特殊情况")
    print("5. 使用elif而不是多个if")
    print("6. 考虑使用字典替代长的if-elif链")
    print()
    
    # 字典替代if-elif示例
    print("使用字典替代长if-elif链：")
    
    # 不推荐的方式
    def get_grade_old(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    
    # 推荐的方式（对于简单映射）
    grade_mapping = [
        (90, 'A'),
        (80, 'B'),
        (70, 'C'),
        (60, 'D'),
        (0, 'F')
    ]
    
    def get_grade_new(score):
        for threshold, grade in grade_mapping:
            if score >= threshold:
                return grade
        return 'F'
    
    test_scores = [95, 85, 75, 65, 55]
    print("成绩对比：")
    for score in test_scores:
        old_grade = get_grade_old(score)
        new_grade = get_grade_new(score)
        print(f"分数{score}：旧方法={old_grade}，新方法={new_grade}")


if __name__ == "__main__":
    main() 