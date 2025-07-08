# 第 17 章 - 使用 API

## 🌐 本章概述

学习如何使用 Web API 获取实时数据，包括 GitHub API、天气 API 等，掌握 API 调用、数据处理和错误处理的最佳实践。

## 🎯 学习目标

- 掌握 REST API 的基本概念
- 学习 requests 库的使用方法
- 了解 API 认证和安全
- 掌握 JSON 数据的处理
- 学习 API 调用的最佳实践

## 🔌 API 类型

### 公共 API

- 🐙 **GitHub API**：代码仓库和用户数据
- 🌤️ **天气 API**：实时天气和预报数据
- 📰 **新闻 API**：最新新闻和文章
- 💱 **汇率 API**：实时汇率和金融数据

### 社交媒体 API

- 🐦 **Twitter API**：推文和用户数据
- 📘 **Facebook API**：社交网络数据
- 📷 **Instagram API**：图片和视频数据
- 💼 **LinkedIn API**：职业网络数据

## 📁 文件结构

| 文件名        | 描述     | 主要功能                               |
| ------------- | -------- | -------------------------------------- |
| `api_demo.py` | API 演示 | GitHub、天气、JSONPlaceholder API 使用 |

## 🚀 快速开始

```bash
# 安装依赖
pip install requests matplotlib

# 运行API演示
python api_demo.py
```

## 🔧 核心技术

### 基本 API 调用

```python
import requests
import json

def api_request(url, params=None, headers=None):
    """标准API请求函数"""
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # 检查HTTP错误
        return response.json()
    except requests.RequestException as e:
        print(f"API请求失败: {e}")
        return None
```

### 认证处理

```python
# API密钥认证
headers = {
    'Authorization': f'token {api_key}',
    'User-Agent': 'MyApp/1.0'
}

# OAuth认证
import requests_oauthlib
oauth = requests_oauthlib.OAuth1Session(
    client_key, client_secret,
    resource_owner_key, resource_owner_secret
)
```

### 分页处理

```python
def fetch_all_pages(base_url, params):
    """获取所有分页数据"""
    all_data = []
    page = 1

    while True:
        params['page'] = page
        data = api_request(base_url, params)

        if not data or len(data) == 0:
            break

        all_data.extend(data)
        page += 1

    return all_data
```

## 🛡️ 错误处理

### HTTP 状态码处理

```python
def handle_response(response):
    """处理API响应"""
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        raise Exception("认证失败")
    elif response.status_code == 403:
        raise Exception("权限不足")
    elif response.status_code == 404:
        raise Exception("资源不存在")
    elif response.status_code == 429:
        raise Exception("请求过于频繁")
    else:
        raise Exception(f"API错误: {response.status_code}")
```

### 重试机制

```python
import time
from functools import wraps

def retry_on_failure(max_retries=3, delay=1):
    """API重试装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise e
                    time.sleep(delay * (2 ** attempt))  # 指数退避
            return None
        return wrapper
    return decorator
```

## 📊 数据处理

### JSON 数据解析

```python
def extract_user_info(github_user_data):
    """提取GitHub用户信息"""
    return {
        'login': github_user_data.get('login'),
        'name': github_user_data.get('name'),
        'public_repos': github_user_data.get('public_repos'),
        'followers': github_user_data.get('followers'),
        'created_at': github_user_data.get('created_at')
    }
```

### 数据缓存

```python
import pickle
from datetime import datetime, timedelta

class APICache:
    def __init__(self, cache_duration=3600):  # 1小时缓存
        self.cache = {}
        self.cache_duration = cache_duration

    def get(self, key):
        if key in self.cache:
            data, timestamp = self.cache[key]
            if datetime.now() - timestamp < timedelta(seconds=self.cache_duration):
                return data
        return None

    def set(self, key, data):
        self.cache[key] = (data, datetime.now())
```

## 🌟 实际应用

### GitHub 仓库分析

- 仓库统计信息
- 贡献者分析
- 代码语言分布
- 提交历史趋势

### 天气数据分析

- 实时天气获取
- 历史天气数据
- 天气预报处理
- 气候趋势分析

### 社交媒体监控

- 关键词监控
- 用户行为分析
- 内容传播分析
- 情感分析

## 📈 API 设计原则

### RESTful 设计

- 使用 HTTP 方法语义
- 资源导向的 URL 设计
- 状态无关的请求
- 统一的接口规范

### 限流和配额

- 请求频率限制
- 并发请求控制
- 用户配额管理
- 优雅降级处理

## 🎯 学习要点

- ✅ API 是现代应用的重要数据来源
- ✅ 错误处理和重试机制至关重要
- ✅ 认证和安全不能忽视
- ✅ 缓存可以提高性能和用户体验
- ✅ 遵循 API 使用条款和限制

## 🔗 相关章节

- **第 16 章** - 下载数据：其他数据获取方法
- **第 18 章** - Django 入门：创建自己的 API
- **第 10 章** - 文件和异常：错误处理基础

---

> 🌐 **提示**：API 是连接应用和数据的桥梁，掌握 API 使用技能能让你获取丰富的在线数据资源！
