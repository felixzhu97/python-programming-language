# 第 16 章 - 下载数据

## 🌐 本章概述

学习从各种数据源下载和处理数据，包括 CSV 文件、JSON 数据和 Web API，为数据分析项目准备数据。

## 🎯 学习目标

- 掌握 CSV 文件的读取和处理
- 学习 JSON 数据的解析方法
- 了解 Web API 的数据获取
- 掌握 pandas 库的数据处理
- 学习数据清洗和转换技术

## 📥 数据来源

### 文件数据

- 📄 **CSV 文件**：表格数据的标准格式
- 📋 **JSON 文件**：结构化数据交换格式
- 📊 **Excel 文件**：办公软件数据格式
- 🗃️ **数据库**：关系型数据存储

### 网络数据

- 🌐 **Web API**：实时数据接口
- 🕷️ **网页抓取**：HTML 数据提取
- 📡 **RSS 源**：新闻和更新数据
- ☁️ **云存储**：在线数据服务

## 📁 文件结构

| 文件名               | 描述       | 主要功能                    |
| -------------------- | ---------- | --------------------------- |
| `data_downloader.py` | 数据下载器 | CSV、JSON、API 数据处理演示 |

## 🚀 快速开始

```bash
# 安装依赖
pip install pandas requests matplotlib

# 运行数据下载演示
python data_downloader.py
```

## 🔧 技术实现

### CSV 数据处理

```python
import pandas as pd

# 读取CSV文件
df = pd.read_csv('data.csv', encoding='utf-8')

# 基本信息
print(df.info())
print(df.describe())

# 数据清洗
df_clean = df.dropna()  # 删除空值
df_clean = df_clean.drop_duplicates()  # 删除重复
```

### JSON 数据解析

```python
import json
import requests

# 读取本地JSON
with open('data.json', 'r') as f:
    data = json.load(f)

# 从API获取JSON
response = requests.get('https://api.example.com/data')
if response.status_code == 200:
    data = response.json()
```

### API 数据获取

```python
import requests
import time

def fetch_api_data(url, params=None):
    """安全的API数据获取"""
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"API请求失败: {e}")
        return None
```

## 📊 数据处理技巧

### 数据清洗

- 处理缺失值
- 删除重复数据
- 数据类型转换
- 异常值检测

### 数据转换

- 字符串处理
- 日期时间转换
- 分类数据编码
- 数值归一化

### 数据聚合

- 分组统计
- 数据透视表
- 时间序列重采样
- 多表连接

## 🛡️ 最佳实践

### 数据安全

- API 密钥管理
- 请求频率限制
- 错误处理机制
- 数据备份策略

### 性能优化

- 分块读取大文件
- 缓存机制使用
- 并行处理技术
- 内存使用优化

### 代码质量

- 异常处理完善
- 日志记录详细
- 函数模块化设计
- 单元测试覆盖

## 📈 实际应用

### 金融数据分析

- 股票价格数据
- 交易量分析
- 市场趋势预测
- 风险评估指标

### 社交媒体分析

- 用户行为数据
- 内容传播分析
- 情感分析
- 网络关系图

### 业务数据分析

- 销售数据分析
- 客户行为分析
- 市场调研数据
- 运营指标监控

## 🎯 学习要点

- ✅ pandas 是 Python 数据处理的核心工具
- ✅ 数据清洗是分析前的重要步骤
- ✅ API 使用需要考虑限制和错误处理
- ✅ 数据可视化帮助理解数据特征
- ✅ 自动化数据处理提高效率

## 🔗 相关章节

- **第 15 章** - 数据可视化基础：数据展示技术
- **第 17 章** - 使用 API：更多 API 应用实例
- **第 10 章** - 文件和异常：文件处理基础

---

> 📥 **提示**：数据是分析的基础，学会获取和处理各种数据源是数据科学家的必备技能！
