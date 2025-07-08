#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第10章 文件和异常 - JSON操作详解

本文件详细演示Python中JSON数据的处理，包括：
1. JSON的基本概念和用途
2. JSON数据的读取和写入
3. Python对象与JSON的转换
4. 自定义JSON编码器和解码器
5. JSON数据的验证和错误处理
6. 处理大型JSON文件
7. JSON格式化和美化
8. 实际应用场景

JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，
在Web开发、API通信、配置文件等场景中广泛使用。
"""

import json
import os
from pathlib import Path
from datetime import datetime, date
from decimal import Decimal
from typing import Any, Dict, List


def main():
    """主函数，演示JSON操作"""
    print("=" * 60)
    print("第10章 文件和异常 - JSON操作详解")
    print("=" * 60)
    print()
    
    # 1. JSON基本概念和语法
    print("1. JSON基本概念和语法")
    print("-" * 30)
    
    # JSON支持的数据类型
    print("JSON支持的数据类型：")
    json_data = {
        "string": "Hello, World!",           # 字符串
        "number": 42,                        # 数字
        "float": 3.14,                       # 浮点数
        "boolean": True,                     # 布尔值
        "null": None,                        # null值
        "array": [1, 2, 3, "four", True],   # 数组
        "object": {                          # 对象
            "nested": "value",
            "count": 10
        }
    }
    
    print("Python字典（将转换为JSON）：")
    for key, value in json_data.items():
        print(f"  {key}: {value} ({type(value).__name__})")
    
    # 转换为JSON字符串
    json_string = json.dumps(json_data, indent=2)
    print(f"\nJSON字符串：\n{json_string}")
    
    # 从JSON字符串转换回Python对象
    parsed_data = json.loads(json_string)
    print(f"\n从JSON解析的数据：{parsed_data}")
    print(f"数据类型：{type(parsed_data)}")
    print()
    
    # 2. JSON文件的读取和写入
    print("2. JSON文件的读取和写入")
    print("-" * 30)
    
    # 写入JSON文件
    user_data = {
        "users": [
            {
                "id": 1,
                "name": "Alice",
                "email": "alice@example.com",
                "age": 25,
                "is_active": True,
                "skills": ["Python", "JavaScript", "SQL"]
            },
            {
                "id": 2,
                "name": "Bob",
                "email": "bob@example.com",
                "age": 30,
                "is_active": False,
                "skills": ["Java", "C++", "Docker"]
            }
        ]
    }
    
    # 写入JSON文件
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(user_data, file, indent=2, ensure_ascii=False)
    
    print("已写入JSON文件：users.json")
    
    # 读取JSON文件
    with open("users.json", "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
    
    print("从文件读取的数据：")
    for user in loaded_data["users"]:
        print(f"  ID: {user['id']}, 姓名: {user['name']}, 邮箱: {user['email']}")
    print()
    
    # 3. JSON序列化选项
    print("3. JSON序列化选项")
    print("-" * 30)
    
    sample_data = {
        "name": "测试用户",
        "values": [1, 2, 3, 4, 5],
        "metadata": {
            "created_at": "2023-01-01",
            "version": 1.0
        }
    }
    
    # 不同的序列化选项
    print("默认序列化（紧凑格式）：")
    compact_json = json.dumps(sample_data)
    print(compact_json)
    
    print("\n美化格式（带缩进）：")
    pretty_json = json.dumps(sample_data, indent=2)
    print(pretty_json)
    
    print("\n指定分隔符：")
    custom_json = json.dumps(sample_data, separators=(',', ': '), indent=2)
    print(custom_json)
    
    print("\n保留非ASCII字符：")
    unicode_json = json.dumps(sample_data, ensure_ascii=False, indent=2)
    print(unicode_json)
    
    print("\n排序键：")
    sorted_json = json.dumps(sample_data, sort_keys=True, indent=2)
    print(sorted_json)
    print()
    
    # 4. 处理不支持的数据类型
    print("4. 处理不支持的数据类型")
    print("-" * 30)
    
    # 自定义JSON编码器
    class CustomJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            elif isinstance(obj, date):
                return obj.isoformat()
            elif isinstance(obj, Decimal):
                return float(obj)
            elif isinstance(obj, set):
                return list(obj)
            elif hasattr(obj, '__dict__'):
                return obj.__dict__
            return super().default(obj)
    
    # 测试自定义编码器
    class User:
        def __init__(self, name, email, created_at):
            self.name = name
            self.email = email
            self.created_at = created_at
    
    complex_data = {
        "user": User("Alice", "alice@example.com", datetime.now()),
        "date": date.today(),
        "decimal": Decimal("10.50"),
        "set": {1, 2, 3, 4, 5},
        "timestamp": datetime.now()
    }
    
    print("包含复杂数据类型的对象：")
    try:
        # 这会失败，因为datetime不能直接序列化
        json.dumps(complex_data)
    except TypeError as e:
        print(f"标准编码器失败：{e}")
    
    # 使用自定义编码器
    custom_json = json.dumps(complex_data, cls=CustomJSONEncoder, indent=2)
    print(f"\n使用自定义编码器：\n{custom_json}")
    print()
    
    # 5. 自定义JSON解码器
    print("5. 自定义JSON解码器")
    print("-" * 30)
    
    def custom_object_hook(obj):
        """自定义对象钩子"""
        if 'created_at' in obj:
            try:
                obj['created_at'] = datetime.fromisoformat(obj['created_at'])
            except ValueError:
                pass
        return obj
    
    # 测试自定义解码器
    json_with_date = '{"name": "Alice", "created_at": "2023-01-01T10:30:00"}'
    
    print("原始JSON：")
    print(json_with_date)
    
    print("\n标准解码：")
    standard_decoded = json.loads(json_with_date)
    print(f"created_at 类型：{type(standard_decoded['created_at'])}")
    print(f"created_at 值：{standard_decoded['created_at']}")
    
    print("\n自定义解码：")
    custom_decoded = json.loads(json_with_date, object_hook=custom_object_hook)
    print(f"created_at 类型：{type(custom_decoded['created_at'])}")
    print(f"created_at 值：{custom_decoded['created_at']}")
    print()
    
    # 6. JSON数据验证
    print("6. JSON数据验证")
    print("-" * 30)
    
    def validate_user_data(data):
        """验证用户数据"""
        required_fields = ["name", "email", "age"]
        errors = []
        
        if not isinstance(data, dict):
            errors.append("数据必须是字典格式")
            return errors
        
        # 检查必填字段
        for field in required_fields:
            if field not in data:
                errors.append(f"缺少必填字段：{field}")
        
        # 验证字段类型和值
        if "name" in data:
            if not isinstance(data["name"], str) or not data["name"].strip():
                errors.append("名称必须是非空字符串")
        
        if "email" in data:
            if not isinstance(data["email"], str) or "@" not in data["email"]:
                errors.append("邮箱格式无效")
        
        if "age" in data:
            if not isinstance(data["age"], int) or data["age"] < 0:
                errors.append("年龄必须是非负整数")
        
        return errors
    
    # 测试数据验证
    test_cases = [
        {"name": "Alice", "email": "alice@example.com", "age": 25},  # 有效
        {"name": "", "email": "invalid-email", "age": -5},           # 无效
        {"name": "Bob"},                                             # 缺少字段
        "invalid data"                                               # 错误类型
    ]
    
    for i, test_data in enumerate(test_cases, 1):
        print(f"测试案例 {i}: {test_data}")
        errors = validate_user_data(test_data)
        if errors:
            print(f"  验证失败：{errors}")
        else:
            print("  验证通过")
    print()
    
    # 7. 处理大型JSON文件
    print("7. 处理大型JSON文件")
    print("-" * 30)
    
    # 创建大型JSON文件
    large_data = {
        "metadata": {
            "version": "1.0",
            "created_at": datetime.now().isoformat(),
            "total_records": 1000
        },
        "records": []
    }
    
    # 生成大量数据
    for i in range(1000):
        record = {
            "id": i + 1,
            "name": f"User{i+1}",
            "email": f"user{i+1}@example.com",
            "score": i * 0.1
        }
        large_data["records"].append(record)
    
    # 写入大型JSON文件
    with open("large_data.json", "w", encoding="utf-8") as file:
        json.dump(large_data, file, cls=CustomJSONEncoder)
    
    print("已创建大型JSON文件：large_data.json")
    
    # 流式处理大型JSON文件
    def process_large_json(filename, chunk_size=100):
        """分块处理大型JSON文件"""
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        records = data.get("records", [])
        total_records = len(records)
        
        print(f"处理 {total_records} 条记录，每块 {chunk_size} 条")
        
        for i in range(0, total_records, chunk_size):
            chunk = records[i:i+chunk_size]
            print(f"处理第 {i//chunk_size + 1} 块，包含 {len(chunk)} 条记录")
            
            # 模拟处理
            avg_score = sum(record["score"] for record in chunk) / len(chunk)
            print(f"  平均分数：{avg_score:.2f}")
    
    process_large_json("large_data.json")
    print()
    
    # 8. JSON配置文件
    print("8. JSON配置文件")
    print("-" * 30)
    
    # 创建配置文件
    config_data = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "database": "myapp",
            "username": "admin",
            "password": "secret",
            "pool_size": 10
        },
        "logging": {
            "level": "INFO",
            "file": "app.log",
            "max_size": "10MB",
            "backup_count": 5
        },
        "features": {
            "enable_cache": True,
            "cache_ttl": 300,
            "enable_debug": False
        }
    }
    
    # 写入配置文件
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(config_data, file, indent=2)
    
    print("已创建配置文件：config.json")
    
    # 读取配置文件
    class Config:
        def __init__(self, config_file):
            self.config_file = config_file
            self.config = self.load_config()
        
        def load_config(self):
            """加载配置文件"""
            try:
                with open(self.config_file, "r", encoding="utf-8") as file:
                    return json.load(file)
            except FileNotFoundError:
                print(f"配置文件 {self.config_file} 不存在")
                return {}
            except json.JSONDecodeError as e:
                print(f"配置文件格式错误：{e}")
                return {}
        
        def get(self, key, default=None):
            """获取配置值"""
            keys = key.split(".")
            value = self.config
            
            for k in keys:
                if isinstance(value, dict) and k in value:
                    value = value[k]
                else:
                    return default
            
            return value
        
        def set(self, key, value):
            """设置配置值"""
            keys = key.split(".")
            current = self.config
            
            for k in keys[:-1]:
                if k not in current:
                    current[k] = {}
                current = current[k]
            
            current[keys[-1]] = value
        
        def save(self):
            """保存配置文件"""
            with open(self.config_file, "w", encoding="utf-8") as file:
                json.dump(self.config, file, indent=2)
    
    # 测试配置管理
    config = Config("config.json")
    
    print("配置管理测试：")
    print(f"数据库主机：{config.get('database.host')}")
    print(f"数据库端口：{config.get('database.port')}")
    print(f"日志级别：{config.get('logging.level')}")
    print(f"缓存启用：{config.get('features.enable_cache')}")
    
    # 修改配置
    config.set("features.enable_debug", True)
    config.set("logging.level", "DEBUG")
    config.save()
    
    print("已更新配置文件")
    print()
    
    # 9. JSON API响应处理
    print("9. JSON API响应处理")
    print("-" * 30)
    
    # 模拟API响应
    api_responses = [
        {
            "status": "success",
            "data": {
                "user": {
                    "id": 1,
                    "name": "Alice",
                    "email": "alice@example.com"
                },
                "profile": {
                    "bio": "Python developer",
                    "location": "San Francisco"
                }
            }
        },
        {
            "status": "error",
            "error": {
                "code": "USER_NOT_FOUND",
                "message": "用户不存在"
            }
        }
    ]
    
    def process_api_response(response_json):
        """处理API响应"""
        try:
            response = json.loads(response_json) if isinstance(response_json, str) else response_json
            
            if response.get("status") == "success":
                data = response.get("data", {})
                user = data.get("user", {})
                print(f"成功：用户 {user.get('name')} ({user.get('email')})")
            elif response.get("status") == "error":
                error = response.get("error", {})
                print(f"错误：{error.get('code')} - {error.get('message')}")
            else:
                print("未知响应格式")
        
        except json.JSONDecodeError as e:
            print(f"JSON解析错误：{e}")
        except Exception as e:
            print(f"处理响应时发生错误：{e}")
    
    # 测试API响应处理
    print("API响应处理测试：")
    for i, response in enumerate(api_responses, 1):
        print(f"响应 {i}：", end="")
        process_api_response(response)
    print()
    
    # 10. JSON Schema验证（概念演示）
    print("10. JSON Schema验证（概念演示）")
    print("-" * 30)
    
    # 定义JSON Schema
    user_schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string", "minLength": 1},
            "email": {"type": "string", "format": "email"},
            "age": {"type": "integer", "minimum": 0, "maximum": 150},
            "skills": {
                "type": "array",
                "items": {"type": "string"}
            }
        },
        "required": ["name", "email", "age"]
    }
    
    def validate_against_schema(data, schema):
        """简单的Schema验证（概念演示）"""
        errors = []
        
        if schema["type"] == "object":
            if not isinstance(data, dict):
                errors.append("数据必须是对象")
                return errors
            
            # 检查必填字段
            for field in schema.get("required", []):
                if field not in data:
                    errors.append(f"缺少必填字段：{field}")
            
            # 验证字段
            for field, field_schema in schema.get("properties", {}).items():
                if field in data:
                    field_errors = validate_field(data[field], field_schema, field)
                    errors.extend(field_errors)
        
        return errors
    
    def validate_field(value, field_schema, field_name):
        """验证单个字段"""
        errors = []
        
        if field_schema["type"] == "string":
            if not isinstance(value, str):
                errors.append(f"{field_name} 必须是字符串")
            elif "minLength" in field_schema and len(value) < field_schema["minLength"]:
                errors.append(f"{field_name} 长度不能小于 {field_schema['minLength']}")
        
        elif field_schema["type"] == "integer":
            if not isinstance(value, int):
                errors.append(f"{field_name} 必须是整数")
            elif "minimum" in field_schema and value < field_schema["minimum"]:
                errors.append(f"{field_name} 不能小于 {field_schema['minimum']}")
            elif "maximum" in field_schema and value > field_schema["maximum"]:
                errors.append(f"{field_name} 不能大于 {field_schema['maximum']}")
        
        elif field_schema["type"] == "array":
            if not isinstance(value, list):
                errors.append(f"{field_name} 必须是数组")
        
        return errors
    
    # 测试Schema验证
    test_users = [
        {"name": "Alice", "email": "alice@example.com", "age": 25, "skills": ["Python"]},
        {"name": "", "email": "invalid", "age": -5},
        {"name": "Bob", "email": "bob@example.com"}
    ]
    
    print("Schema验证测试：")
    for i, user in enumerate(test_users, 1):
        print(f"用户 {i}: {user}")
        errors = validate_against_schema(user, user_schema)
        if errors:
            print(f"  验证失败：{errors}")
        else:
            print("  验证通过")
    print()
    
    # 11. 清理临时文件
    print("11. 清理临时文件")
    print("-" * 30)
    
    temp_files = [
        "users.json", "large_data.json", "config.json"
    ]
    
    for filename in temp_files:
        try:
            os.remove(filename)
            print(f"删除文件：{filename}")
        except FileNotFoundError:
            print(f"文件不存在：{filename}")
    
    print()
    
    print("JSON操作最佳实践：")
    print("1. 使用适当的编码（UTF-8）")
    print("2. 处理JSON解析异常")
    print("3. 验证JSON数据结构")
    print("4. 使用自定义编码器处理复杂对象")
    print("5. 对大型JSON文件使用流式处理")
    print("6. 美化JSON输出以便调试")
    print("7. 使用JSON Schema验证数据")
    print("8. 保护敏感信息（如密码）")
    print("9. 版本化JSON数据结构")
    print("10. 考虑性能和内存使用")
    print()
    
    print("=== JSON操作演示完成 ===")


if __name__ == "__main__":
    main() 