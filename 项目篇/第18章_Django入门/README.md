# 第 18 章 - Django 入门

## 🌐 本章概述

学习 Django Web 框架的基础知识，创建学习笔记 Web 应用，掌握模型、视图、模板的 MVT 架构模式。

## 🎯 学习目标

- 理解 Django 的 MVT 架构
- 掌握 Django 项目的创建和配置
- 学习模型定义和数据库操作
- 了解视图函数和 URL 路由
- 掌握模板系统的使用

## 🏗️ 项目特性

### 核心功能

- 📝 **学习主题管理**：创建、编辑、删除主题
- 📄 **学习条目**：每个主题下的详细笔记
- 🔍 **搜索功能**：快速查找学习内容
- 📊 **统计信息**：学习进度和数据统计
- 💾 **数据导出**：导出学习笔记为文件

### 技术特性

- 🗄️ **SQLite 数据库**：轻量级数据存储
- 🔄 **CRUD 操作**：完整的数据操作功能
- 🎨 **响应式界面**：适配各种设备
- 🔒 **数据验证**：输入数据的验证机制
- 📱 **现代 UI**：简洁美观的用户界面

## 📁 文件结构

| 文件名                    | 描述            | 主要功能              |
| ------------------------- | --------------- | --------------------- |
| `learning_log_project.py` | Django 风格应用 | 学习笔记 Web 应用演示 |

## 🚀 快速开始

```bash
# 安装依赖
pip install django

# 运行Web应用
python learning_log_project.py

# 访问应用
# 打开浏览器访问: http://localhost:8000
```

## 🏗️ 架构设计

### MVT 模式

```python
# Model - 数据模型
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

# View - 视图逻辑
def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)

# Template - 模板展示
# topics.html 模板文件
```

### URL 路由

```python
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
]
```

## 🛠️ 核心功能

### 数据模型

- 学习主题(Topic)模型
- 学习条目(Entry)模型
- 数据关系定义
- 数据验证规则

### 视图函数

- 主页显示
- 主题列表
- 主题详情
- 添加新主题
- 编辑条目

### 模板系统

- 基础模板继承
- 动态内容渲染
- 表单处理
- 静态文件管理

## 📊 数据库设计

### 主题表(Topic)

```sql
CREATE TABLE topic (
    id INTEGER PRIMARY KEY,
    text VARCHAR(200) NOT NULL,
    date_added DATETIME NOT NULL
);
```

### 条目表(Entry)

```sql
CREATE TABLE entry (
    id INTEGER PRIMARY KEY,
    topic_id INTEGER NOT NULL,
    text TEXT NOT NULL,
    date_added DATETIME NOT NULL,
    FOREIGN KEY (topic_id) REFERENCES topic (id)
);
```

## 🎨 前端特性

### 响应式设计

- Bootstrap 框架集成
- 移动端适配
- 现代化界面
- 用户体验优化

### 交互功能

- 表单验证
- Ajax 异步请求
- 搜索过滤
- 分页显示

## 🔧 开发工具

### Django 管理

```python
# 数据库迁移
python manage.py makemigrations
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser

# 运行开发服务器
python manage.py runserver
```

### 调试和测试

- Django 调试工具栏
- 单元测试框架
- 日志记录系统
- 性能监控

## 🌟 最佳实践

### 代码组织

- 应用模块化设计
- 设置文件分离
- 静态文件管理
- 模板继承结构

### 安全考虑

- CSRF 保护
- SQL 注入防护
- XSS 攻击防护
- 用户输入验证

### 性能优化

- 数据库查询优化
- 缓存机制使用
- 静态文件压缩
- 异步任务处理

## 📈 扩展功能

### 用户系统

- 用户注册登录
- 权限管理
- 个人资料
- 社交功能

### 高级特性

- 搜索引擎集成
- 文件上传功能
- 邮件通知系统
- API 接口开发

## 🎯 学习要点

- ✅ Django 是 Python 最流行的 Web 框架
- ✅ MVT 架构清晰分离关注点
- ✅ ORM 简化数据库操作
- ✅ 模板系统支持继承和复用
- ✅ Django 提供丰富的内置功能

## 🔗 相关章节

- **第 19 章** - 用户账户：用户认证系统
- **第 20 章** - 设置样式和部署：应用美化和部署
- **第 9 章** - 类：面向对象编程基础

---

> 🌐 **提示**：Django 是功能强大的 Web 框架，掌握 Django 开发能让你快速构建专业的 Web 应用！
