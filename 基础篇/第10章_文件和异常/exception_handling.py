#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第10章 文件和异常 - 异常处理详解

本文件详细演示Python中的异常处理机制，包括：
1. 异常的基本概念
2. try-except语句的使用
3. 常见异常类型
4. 异常信息的获取
5. else和finally子句
6. 自定义异常
7. 异常链和上下文
8. 实际应用中的异常处理策略

异常处理是编写健壮程序的重要技能，它能让程序在遇到错误时优雅地处理而不是崩溃。
"""

import sys
import traceback
import logging
from pathlib import Path


def main():
    """主函数，演示异常处理"""
    print("=" * 60)
    print("第10章 文件和异常 - 异常处理详解")
    print("=" * 60)
    print()
    
    # 1. 异常的基本概念
    print("1. 异常的基本概念")
    print("-" * 30)
    
    # 没有异常处理的代码
    print("没有异常处理的代码（会导致程序崩溃）：")
    try:
        # 这里我们在try块中演示，实际不会崩溃
        result = 10 / 0
    except ZeroDivisionError:
        print("除零错误！程序本应在此崩溃")
    
    # 有异常处理的代码
    print("\n有异常处理的代码：")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("捕获到除零错误，程序继续运行")
    
    print("程序继续执行...")
    print()
    
    # 2. try-except语句的基本用法
    print("2. try-except语句的基本用法")
    print("-" * 30)
    
    # 处理单个异常
    print("处理单个异常：")
    try:
        number = int(input("请输入一个数字（直接回车使用默认值5）：") or "5")
        result = 100 / number
        print(f"100 / {number} = {result}")
    except ValueError:
        print("错误：输入的不是有效数字")
    except ZeroDivisionError:
        print("错误：不能除以零")
    
    # 处理多个异常
    print("\n处理多个异常：")
    try:
        filename = input("请输入文件名（直接回车使用默认值'nonexistent.txt'）：") or "nonexistent.txt"
        with open(filename, 'r') as file:
            content = file.read()
        number = int(content)
        result = 100 / number
    except (ValueError, ZeroDivisionError) as e:
        print(f"数值错误：{e}")
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
    except Exception as e:
        print(f"其他错误：{e}")
    
    print()
    
    # 3. 常见异常类型
    print("3. 常见异常类型")
    print("-" * 30)
    
    def demonstrate_exception(exception_type):
        """演示不同类型的异常"""
        print(f"演示 {exception_type.__name__}：")
        
        try:
            if exception_type == ValueError:
                int("abc")
            elif exception_type == TypeError:
                "string" + 5
            elif exception_type == IndexError:
                my_list = [1, 2, 3]
                print(my_list[10])
            elif exception_type == KeyError:
                my_dict = {"a": 1, "b": 2}
                print(my_dict["c"])
            elif exception_type == AttributeError:
                my_string = "hello"
                my_string.non_existent_method()
            elif exception_type == FileNotFoundError:
                with open("nonexistent_file.txt", 'r') as file:
                    pass
            elif exception_type == PermissionError:
                # 模拟权限错误
                raise PermissionError("权限被拒绝")
            elif exception_type == ZeroDivisionError:
                10 / 0
        except exception_type as e:
            print(f"  捕获到异常：{e}")
            print(f"  异常类型：{type(e).__name__}")
        print()
    
    # 演示各种异常类型
    exception_types = [
        ValueError, TypeError, IndexError, KeyError,
        AttributeError, FileNotFoundError, PermissionError, ZeroDivisionError
    ]
    
    for exc_type in exception_types:
        demonstrate_exception(exc_type)
    
    # 4. 异常信息的获取
    print("4. 异常信息的获取")
    print("-" * 30)
    
    try:
        # 创建一个复杂的错误情况
        data = {"users": [{"name": "Alice", "age": 25}]}
        user_age = data["users"][5]["age"]  # 索引超出范围
    except Exception as e:
        print(f"异常类型：{type(e).__name__}")
        print(f"异常信息：{e}")
        print(f"异常参数：{e.args}")
        
        # 获取详细的错误信息
        print("\n详细错误信息：")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(f"异常类型：{exc_type}")
        print(f"异常值：{exc_value}")
        
        # 打印堆栈跟踪
        print("\n堆栈跟踪：")
        traceback.print_exc()
    
    print()
    
    # 5. else和finally子句
    print("5. else和finally子句")
    print("-" * 30)
    
    def divide_numbers(a, b):
        """演示else和finally子句"""
        try:
            result = a / b
        except ZeroDivisionError:
            print("错误：除数不能为零")
            return None
        except TypeError:
            print("错误：参数必须是数字")
            return None
        else:
            # 只有在没有异常时才执行
            print(f"计算成功：{a} / {b} = {result}")
            return result
        finally:
            # 无论是否有异常都会执行
            print("清理资源...")
    
    print("正常情况：")
    divide_numbers(10, 2)
    
    print("\n异常情况：")
    divide_numbers(10, 0)
    
    print("\n类型错误：")
    divide_numbers("10", 2)
    print()
    
    # 6. 自定义异常
    print("6. 自定义异常")
    print("-" * 30)
    
    class CustomError(Exception):
        """自定义异常基类"""
        pass
    
    class ValidationError(CustomError):
        """验证错误"""
        def __init__(self, message, field=None):
            super().__init__(message)
            self.field = field
    
    class BusinessLogicError(CustomError):
        """业务逻辑错误"""
        def __init__(self, message, error_code=None):
            super().__init__(message)
            self.error_code = error_code
    
    class UserNotFoundError(BusinessLogicError):
        """用户不存在错误"""
        def __init__(self, user_id):
            super().__init__(f"用户 {user_id} 不存在", error_code="USER_NOT_FOUND")
            self.user_id = user_id
    
    def validate_user_data(user_data):
        """验证用户数据"""
        if not isinstance(user_data, dict):
            raise ValidationError("用户数据必须是字典格式")
        
        if "name" not in user_data:
            raise ValidationError("缺少必填字段：name", field="name")
        
        if "age" not in user_data:
            raise ValidationError("缺少必填字段：age", field="age")
        
        if not isinstance(user_data["age"], int) or user_data["age"] < 0:
            raise ValidationError("年龄必须是非负整数", field="age")
        
        if user_data["age"] > 150:
            raise ValidationError("年龄不能超过150岁", field="age")
    
    def find_user(user_id):
        """查找用户"""
        # 模拟数据库查询
        users = {1: "Alice", 2: "Bob", 3: "Charlie"}
        if user_id not in users:
            raise UserNotFoundError(user_id)
        return users[user_id]
    
    # 测试自定义异常
    print("测试自定义异常：")
    
    # 验证错误
    try:
        validate_user_data({"name": "Alice"})  # 缺少age字段
    except ValidationError as e:
        print(f"验证错误：{e}")
        if e.field:
            print(f"错误字段：{e.field}")
    
    try:
        validate_user_data({"name": "Bob", "age": -5})  # 年龄无效
    except ValidationError as e:
        print(f"验证错误：{e}")
    
    # 业务逻辑错误
    try:
        user = find_user(999)  # 用户不存在
    except UserNotFoundError as e:
        print(f"业务错误：{e}")
        print(f"错误代码：{e.error_code}")
        print(f"用户ID：{e.user_id}")
    
    print()
    
    # 7. 异常链和上下文
    print("7. 异常链和上下文")
    print("-" * 30)
    
    def process_data(data):
        """处理数据，演示异常链"""
        try:
            # 模拟数据处理
            if not data:
                raise ValueError("数据不能为空")
            
            result = 100 / data
            return result
        except ValueError as e:
            # 重新抛出异常，保留原始异常信息
            raise BusinessLogicError("数据处理失败") from e
        except ZeroDivisionError as e:
            # 使用raise ... from None来隐藏原始异常
            raise BusinessLogicError("计算错误") from None
    
    # 测试异常链
    print("异常链示例：")
    try:
        result = process_data("")  # 空数据
    except BusinessLogicError as e:
        print(f"业务异常：{e}")
        print(f"原因：{e.__cause__}")
        print(f"上下文：{e.__context__}")
    
    try:
        result = process_data(0)  # 零值
    except BusinessLogicError as e:
        print(f"业务异常：{e}")
        print(f"原因：{e.__cause__}")
    
    print()
    
    # 8. 文件操作中的异常处理
    print("8. 文件操作中的异常处理")
    print("-" * 30)
    
    def safe_file_read(filename):
        """安全地读取文件"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print(f"文件 {filename} 不存在")
            return None
        except PermissionError:
            print(f"没有权限读取文件 {filename}")
            return None
        except UnicodeDecodeError:
            print(f"文件 {filename} 编码错误")
            return None
        except Exception as e:
            print(f"读取文件时发生未知错误：{e}")
            return None
    
    def safe_file_write(filename, content):
        """安全地写入文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
                return True
        except PermissionError:
            print(f"没有权限写入文件 {filename}")
            return False
        except OSError as e:
            print(f"写入文件时发生系统错误：{e}")
            return False
        except Exception as e:
            print(f"写入文件时发生未知错误：{e}")
            return False
    
    # 测试文件操作异常处理
    print("测试文件操作异常处理：")
    
    # 读取不存在的文件
    content = safe_file_read("nonexistent.txt")
    
    # 写入文件
    if safe_file_write("test_file.txt", "Hello, World!"):
        print("文件写入成功")
        
        # 读取刚写入的文件
        content = safe_file_read("test_file.txt")
        if content:
            print(f"文件内容：{content}")
    
    print()
    
    # 9. 使用日志记录异常
    print("9. 使用日志记录异常")
    print("-" * 30)
    
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('error.log'),
            logging.StreamHandler()
        ]
    )
    
    def risky_operation(x, y):
        """可能出错的操作"""
        logger = logging.getLogger(__name__)
        
        try:
            logger.info(f"开始执行操作：{x} / {y}")
            result = x / y
            logger.info(f"操作成功：结果为 {result}")
            return result
        except ZeroDivisionError as e:
            logger.error(f"除零错误：{e}", exc_info=True)
            raise
        except Exception as e:
            logger.critical(f"未知错误：{e}", exc_info=True)
            raise
    
    # 测试日志记录
    print("测试日志记录：")
    try:
        risky_operation(10, 2)
    except Exception:
        pass
    
    try:
        risky_operation(10, 0)
    except Exception:
        pass
    
    print()
    
    # 10. 异常处理的最佳实践
    print("10. 异常处理的最佳实践")
    print("-" * 30)
    
    class DatabaseError(Exception):
        """数据库异常"""
        pass
    
    class User:
        """用户类"""
        def __init__(self, user_id, name, email):
            self.user_id = user_id
            self.name = name
            self.email = email
    
    class UserService:
        """用户服务类，演示异常处理最佳实践"""
        
        def __init__(self):
            self.users = {
                1: User(1, "Alice", "alice@example.com"),
                2: User(2, "Bob", "bob@example.com")
            }
        
        def get_user(self, user_id):
            """获取用户"""
            if not isinstance(user_id, int):
                raise TypeError("用户ID必须是整数")
            
            if user_id <= 0:
                raise ValueError("用户ID必须是正整数")
            
            user = self.users.get(user_id)
            if not user:
                raise UserNotFoundError(user_id)
            
            return user
        
        def create_user(self, name, email):
            """创建用户"""
            # 验证输入
            if not name or not isinstance(name, str):
                raise ValidationError("用户名不能为空且必须是字符串")
            
            if not email or "@" not in email:
                raise ValidationError("邮箱格式不正确")
            
            # 检查邮箱是否已存在
            for user in self.users.values():
                if user.email == email:
                    raise ValidationError("邮箱已存在")
            
            # 创建用户
            user_id = max(self.users.keys(), default=0) + 1
            user = User(user_id, name, email)
            self.users[user_id] = user
            
            return user
        
        def update_user(self, user_id, name=None, email=None):
            """更新用户信息"""
            user = self.get_user(user_id)  # 可能抛出异常
            
            if name is not None:
                if not isinstance(name, str) or not name:
                    raise ValidationError("用户名必须是非空字符串")
                user.name = name
            
            if email is not None:
                if not email or "@" not in email:
                    raise ValidationError("邮箱格式不正确")
                
                # 检查邮箱是否已被其他用户使用
                for other_user in self.users.values():
                    if other_user.user_id != user_id and other_user.email == email:
                        raise ValidationError("邮箱已被其他用户使用")
                
                user.email = email
            
            return user
        
        def delete_user(self, user_id):
            """删除用户"""
            user = self.get_user(user_id)  # 可能抛出异常
            del self.users[user_id]
            return True
    
    # 测试最佳实践
    print("异常处理最佳实践演示：")
    
    user_service = UserService()
    
    # 正常操作
    try:
        user = user_service.get_user(1)
        print(f"获取用户成功：{user.name} ({user.email})")
    except Exception as e:
        print(f"获取用户失败：{e}")
    
    # 异常操作
    operations = [
        lambda: user_service.get_user("invalid"),  # 类型错误
        lambda: user_service.get_user(-1),         # 值错误
        lambda: user_service.get_user(999),        # 用户不存在
        lambda: user_service.create_user("", "test@example.com"),  # 空用户名
        lambda: user_service.create_user("Test", "invalid-email"),  # 邮箱格式错误
        lambda: user_service.create_user("Test", "alice@example.com"),  # 邮箱已存在
    ]
    
    for i, operation in enumerate(operations, 1):
        try:
            result = operation()
            print(f"操作 {i} 成功：{result}")
        except (TypeError, ValueError, ValidationError, UserNotFoundError) as e:
            print(f"操作 {i} 失败：{type(e).__name__}: {e}")
        except Exception as e:
            print(f"操作 {i} 发生意外错误：{e}")
    
    print()
    
    # 11. 上下文管理器中的异常处理
    print("11. 上下文管理器中的异常处理")
    print("-" * 30)
    
    class DatabaseConnection:
        """数据库连接上下文管理器"""
        
        def __init__(self, connection_string):
            self.connection_string = connection_string
            self.connection = None
        
        def __enter__(self):
            print(f"连接到数据库：{self.connection_string}")
            # 模拟连接
            self.connection = f"Connection to {self.connection_string}"
            return self.connection
        
        def __exit__(self, exc_type, exc_value, traceback):
            if exc_type is not None:
                print(f"操作过程中发生异常：{exc_type.__name__}: {exc_value}")
                print("回滚事务...")
            else:
                print("提交事务...")
            
            print("关闭数据库连接")
            self.connection = None
            
            # 返回False表示不抑制异常
            return False
    
    # 测试上下文管理器中的异常处理
    print("正常情况：")
    try:
        with DatabaseConnection("postgresql://localhost:5432/mydb") as conn:
            print("执行数据库操作...")
            # 模拟成功的操作
            print("操作成功")
    except Exception as e:
        print(f"外部捕获异常：{e}")
    
    print("\n异常情况：")
    try:
        with DatabaseConnection("postgresql://localhost:5432/mydb") as conn:
            print("执行数据库操作...")
            # 模拟失败的操作
            raise DatabaseError("数据库操作失败")
    except DatabaseError as e:
        print(f"外部捕获异常：{e}")
    
    print()
    
    # 12. 清理资源
    print("12. 清理资源")
    print("-" * 30)
    
    # 清理测试文件
    test_files = ["test_file.txt", "error.log"]
    for file in test_files:
        try:
            Path(file).unlink()
            print(f"删除文件：{file}")
        except FileNotFoundError:
            print(f"文件不存在：{file}")
    
    print()
    
    print("异常处理最佳实践总结：")
    print("1. 只捕获你能处理的异常")
    print("2. 使用具体的异常类型而不是Exception")
    print("3. 在异常处理中提供有用的信息")
    print("4. 使用finally或上下文管理器确保资源清理")
    print("5. 记录异常信息用于调试")
    print("6. 不要忽略异常")
    print("7. 使用自定义异常表达业务逻辑")
    print("8. 异常链保留原始错误信息")
    print("9. 验证输入参数")
    print("10. 优雅地处理错误情况")
    print()
    
    print("=== 异常处理演示完成 ===")


if __name__ == "__main__":
    main() 