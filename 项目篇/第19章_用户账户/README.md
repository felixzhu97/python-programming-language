# 第 19 章 - 用户账户

## 👤 本章概述

在 Web 应用中添加用户认证系统，包括用户注册、登录、权限管理和个人资料功能，构建完整的用户管理体系。

## 🎯 学习目标

- 掌握用户认证系统的设计
- 学习密码加密和安全处理
- 了解会话管理机制
- 掌握权限控制方法
- 学习用户体验优化

## 🔐 核心功能

### 用户认证

- 👤 **用户注册**：新用户账户创建
- 🔑 **用户登录**：身份验证和会话建立
- 🚪 **用户登出**：安全的会话终止
- 🔄 **密码重置**：安全的密码找回机制

### 权限管理

- 🛡️ **访问控制**：页面和功能的权限验证
- 👑 **用户角色**：不同权限级别的用户分类
- 🔒 **数据隔离**：用户只能访问自己的数据
- 📋 **操作日志**：用户操作的审计追踪

### 个人资料

- 📝 **资料编辑**：用户信息的修改功能
- 📸 **头像上传**：个性化头像设置
- ⚙️ **偏好设置**：个人使用习惯配置
- 📊 **活动统计**：用户行为数据展示

## 📁 文件结构

| 文件名                   | 描述         | 主要功能               |
| ------------------------ | ------------ | ---------------------- |
| `user_authentication.py` | 用户认证系统 | 完整的用户管理系统演示 |

## 🚀 快速开始

```bash
# 运行用户认证系统演示
python user_authentication.py

# 系统会自动创建演示数据和用户账户
```

## 🔧 技术实现

### 密码安全

```python
import hashlib
import secrets

class PasswordManager:
    @staticmethod
    def hash_password(password, salt=None):
        """安全的密码哈希"""
        if salt is None:
            salt = secrets.token_hex(16)

        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000  # 迭代次数
        )
        return salt + password_hash.hex()

    @staticmethod
    def verify_password(password, hashed):
        """验证密码"""
        salt = hashed[:32]
        stored_hash = hashed[32:]

        new_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000
        )
        return new_hash.hex() == stored_hash
```

### 会话管理

```python
import jwt
from datetime import datetime, timedelta

class SessionManager:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def create_token(self, user_id):
        """创建JWT令牌"""
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(hours=24),
            'iat': datetime.utcnow()
        }
        return jwt.encode(payload, self.secret_key, algorithm='HS256')

    def verify_token(self, token):
        """验证JWT令牌"""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
```

### 权限装饰器

```python
from functools import wraps

def login_required(func):
    """登录验证装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper

def role_required(role):
    """角色权限装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.has_role(role):
                return abort(403)  # Forbidden
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

## 🛡️ 安全特性

### 密码策略

- 最小长度要求
- 复杂度验证
- 常见密码检查
- 密码历史记录

### 防护机制

- SQL 注入防护
- XSS 攻击防护
- CSRF 令牌验证
- 暴力破解防护

### 会话安全

- 安全的会话 ID
- 会话超时机制
- 同源策略检查
- 安全的 Cookie 设置

## 📊 用户数据管理

### 数据模型

```python
class User:
    def __init__(self):
        self.id = None
        self.username = None
        self.email = None
        self.password_hash = None
        self.created_at = None
        self.last_login = None
        self.is_active = True
        self.role = 'user'
```

### 数据验证

```python
import re

def validate_email(email):
    """邮箱格式验证"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_username(username):
    """用户名验证"""
    if len(username) < 3 or len(username) > 20:
        return False
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False
    return True
```

## 🎨 用户界面

### 登录界面

- 简洁的登录表单
- 记住登录状态
- 第三方登录选项
- 密码找回链接

### 注册界面

- 分步骤注册流程
- 实时验证反馈
- 隐私政策同意
- 邮箱验证机制

### 个人中心

- 用户信息展示
- 活动历史记录
- 安全设置选项
- 数据导出功能

## 📈 用户分析

### 用户行为

- 登录频率统计
- 活跃时间分析
- 功能使用情况
- 用户留存率

### 安全监控

- 异常登录检测
- 多设备登录监控
- 失败登录统计
- 安全事件报告

## 🌟 高级功能

### 第三方登录

- OAuth2.0 集成
- 社交账号绑定
- 统一身份认证
- 单点登录(SSO)

### 两步验证

- 短信验证码
- 邮箱验证码
- 时间基础令牌
- 硬件密钥支持

## 🎯 学习要点

- ✅ 用户认证是 Web 应用的基础功能
- ✅ 密码安全存储至关重要
- ✅ 会话管理影响用户体验
- ✅ 权限控制保护系统安全
- ✅ 用户体验和安全需要平衡

## 🔗 相关章节

- **第 18 章** - Django 入门：Web 应用基础框架
- **第 20 章** - 设置样式和部署：应用美化和上线
- **第 10 章** - 文件和异常：安全的文件处理

---

> 👤 **提示**：用户认证系统是现代 Web 应用的核心，既要保证安全性，也要提供良好的用户体验！
