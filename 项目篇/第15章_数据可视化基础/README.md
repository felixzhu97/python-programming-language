# 第 15 章 - 数据可视化基础

## 📊 本章概述

数据可视化是将复杂数据转化为直观图表的重要技能。本章使用 matplotlib 库学习各种图表的创建和定制。

## 🎯 学习目标

- 掌握 matplotlib 的基本使用
- 学习创建各种类型的图表
- 了解图表的美化和定制
- 掌握数据可视化的最佳实践
- 学习交互式图表的创建

## 📈 图表类型

### 基础图表

- 📈 **折线图**：趋势和变化展示
- 🎯 **散点图**：数据关系分析
- 📊 **柱状图**：分类数据比较
- 🥧 **饼图**：比例关系展示
- 📊 **直方图**：数据分布显示

### 高级图表

- 🔥 **热力图**：矩阵数据可视化
- ⏰ **时间序列图**：时间相关数据
- 📊 **组合图表**：多种图表结合
- 🎨 **样式定制**：专业图表设计
- 🖱️ **交互式图表**：用户交互功能

## 📁 文件结构

| 文件名                 | 描述           | 主要功能                |
| ---------------------- | -------------- | ----------------------- |
| `matplotlib_basics.py` | 数据可视化演示 | 11 种图表类型的完整演示 |

## 🚀 快速开始

```bash
# 安装依赖
pip install matplotlib numpy pandas seaborn

# 运行可视化演示
python matplotlib_basics.py
```

## 🔧 技术要点

### 基础绘图

```python
import matplotlib.pyplot as plt
import numpy as np

# 创建图表
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='数据')
plt.xlabel('X轴标签')
plt.ylabel('Y轴标签')
plt.title('图表标题')
plt.legend()
plt.show()
```

### 样式定制

```python
# 设置样式
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
```

### 子图布局

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot(x, y1)
axes[0, 1].scatter(x, y2)
axes[1, 0].bar(categories, values)
axes[1, 1].pie(sizes, labels=labels)
```

## 📊 实战示例

### 销售数据分析

- 月度销售趋势图
- 产品销量对比
- 区域销售分布
- 客户年龄分析

### 科学数据展示

- 实验结果对比
- 数据相关性分析
- 统计分布图
- 误差条图表

## 🎨 美化技巧

### 颜色搭配

- 使用专业配色方案
- 保持颜色一致性
- 考虑色盲友好

### 布局设计

- 合理的图表比例
- 清晰的标签和标题
- 适当的留白空间

### 交互功能

- 鼠标悬停显示数据
- 缩放和平移功能
- 动态更新数据

## 🎯 学习要点

- ✅ matplotlib 是 Python 数据可视化的核心库
- ✅ 选择合适的图表类型很重要
- ✅ 图表美化提升专业性
- ✅ 交互性增强用户体验
- ✅ 数据故事比图表本身更重要

## 🔗 相关章节

- **第 16 章** - 下载数据：实际数据的可视化
- **第 17 章** - 使用 API：动态数据可视化
- **项目实战** - 数据分析项目应用

---

> 📊 **提示**：数据可视化是数据科学的重要技能，好的图表能让复杂数据一目了然！
