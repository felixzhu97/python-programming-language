"""
第01章 起步 - Python之禅

The Zen of Python, by Tim Peters
展示Python的设计哲学和指导原则
"""

import this

print("\n" + "="*50)
print("Python之禅教导我们编写优美、简洁的代码")
print("="*50)

# 一些体现Python哲学的简单示例
print("\n美丽胜过丑陋 (Beautiful is better than ugly)")
print("明了胜过晦涩 (Explicit is better than implicit)")
print("简洁胜过复杂 (Simple is better than complex)")
print("可读性很重要 (Readability counts)")

# 简洁的Python代码示例
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]  # 简洁明了的列表推导式
print(f"\n数字: {numbers}")
print(f"平方: {squares}")

# 可读性良好的代码
def greet_user(username):
    """向用户显示简单的问候语"""
    print(f"Hello, {username.title()}!")

greet_user("alice")
greet_user("bob") 