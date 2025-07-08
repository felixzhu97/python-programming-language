#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第20章 - 设置样式和部署
演示Web应用的样式美化和部署流程

主要内容：
1. CSS样式设计
2. Bootstrap集成
3. 静态文件管理
4. 部署准备
5. 生产环境配置
"""

import os
import shutil
from datetime import datetime


class WebStyleManager:
    """Web样式管理器"""
    
    def __init__(self):
        self.project_dir = "web_project_demo"
        self.setup_project_structure()
    
    def setup_project_structure(self):
        """创建项目结构"""
        print("创建Web项目结构...")
        
        # 创建目录结构
        dirs = [
            self.project_dir,
            f"{self.project_dir}/static",
            f"{self.project_dir}/static/css",
            f"{self.project_dir}/static/js", 
            f"{self.project_dir}/static/images",
            f"{self.project_dir}/templates",
            f"{self.project_dir}/config"
        ]
        
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)
        
        print(f"项目结构已创建: {self.project_dir}/")
    
    def create_css_styles(self):
        """创建CSS样式文件"""
        print("创建CSS样式文件...")
        
        # 主样式文件
        main_css = """
/* 主样式文件 - main.css */

/* 全局样式 */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f8f9fa;
}

/* 容器样式 */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* 头部样式 */
.header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 1rem 0;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.header h1 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}

.nav {
    display: flex;
    justify-content: center;
    list-style: none;
    margin-top: 1rem;
}

.nav li {
    margin: 0 1rem;
}

.nav a {
    color: white;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    transition: background-color 0.3s;
}

.nav a:hover {
    background-color: rgba(255,255,255,0.2);
}

/* 主内容区域 */
.main-content {
    padding: 2rem 0;
    min-height: 60vh;
}

.card {
    background: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
    transition: transform 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

/* 按钮样式 */
.btn {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    background: #667eea;
    color: white;
    text-decoration: none;
    border-radius: 5px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
    font-size: 1rem;
}

.btn:hover {
    background: #5a6fd8;
}

.btn-success {
    background: #28a745;
}

.btn-success:hover {
    background: #218838;
}

.btn-danger {
    background: #dc3545;
}

.btn-danger:hover {
    background: #c82333;
}

/* 表单样式 */
.form-group {
    margin-bottom: 1.5rem;
}

.form-label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 600;
}

.form-input {
    width: 100%;
    padding: 0.75rem;
    border: 2px solid #e9ecef;
    border-radius: 5px;
    font-size: 1rem;
    transition: border-color 0.3s;
}

.form-input:focus {
    outline: none;
    border-color: #667eea;
}

/* 底部样式 */
.footer {
    background: #343a40;
    color: white;
    text-align: center;
    padding: 2rem 0;
    margin-top: 3rem;
}

/* 响应式设计 */
@media (max-width: 768px) {
    .nav {
        flex-direction: column;
        align-items: center;
    }
    
    .nav li {
        margin: 0.25rem 0;
    }
    
    .header h1 {
        font-size: 2rem;
    }
    
    .container {
        padding: 0 15px;
    }
}

/* 动画效果 */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.fade-in {
    animation: fadeIn 0.6s ease-out;
}

/* 工具类 */
.text-center {
    text-align: center;
}

.text-primary {
    color: #667eea;
}

.mb-3 {
    margin-bottom: 1rem;
}

.mt-3 {
    margin-top: 1rem;
}
"""
        
        with open(f"{self.project_dir}/static/css/main.css", 'w', encoding='utf-8') as f:
            f.write(main_css)
        
        print("CSS样式文件已创建")
    
    def create_html_templates(self):
        """创建HTML模板"""
        print("创建HTML模板...")
        
        # 基础模板
        base_template = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>学习笔记应用</title>
    <link rel="stylesheet" href="static/css/main.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <header class="header">
        <div class="container">
            <h1>学习笔记</h1>
            <nav>
                <ul class="nav">
                    <li><a href="/">首页</a></li>
                    <li><a href="/topics">主题列表</a></li>
                    <li><a href="/add_topic">添加主题</a></li>
                    <li><a href="/profile">个人中心</a></li>
                </ul>
            </nav>
        </div>
    </header>
    
    <main class="main-content">
        <div class="container">
            <div class="content fade-in">
                <!-- 页面内容将在这里显示 -->
                <div class="card">
                    <h2 class="text-center text-primary">欢迎使用学习笔记应用</h2>
                    <p class="text-center">记录您的学习历程，管理知识点</p>
                    
                    <div class="row mt-3">
                        <div class="col-md-4">
                            <div class="card">
                                <h3>快速开始</h3>
                                <p>创建您的第一个学习主题</p>
                                <a href="/add_topic" class="btn btn-success">开始创建</a>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="card">
                                <h3>浏览主题</h3>
                                <p>查看所有已创建的学习主题</p>
                                <a href="/topics" class="btn">浏览主题</a>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="card">
                                <h3>个人中心</h3>
                                <p>管理您的账户和设置</p>
                                <a href="/profile" class="btn">个人中心</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
    
    <footer class="footer">
        <div class="container">
            <p>&copy; 2024 学习笔记应用. 使用 Python 和现代Web技术构建.</p>
        </div>
    </footer>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="static/js/main.js"></script>
</body>
</html>
"""
        
        with open(f"{self.project_dir}/templates/index.html", 'w', encoding='utf-8') as f:
            f.write(base_template)
        
        print("HTML模板已创建")
    
    def create_javascript(self):
        """创建JavaScript文件"""
        print("创建JavaScript文件...")
        
        main_js = """
// 主JavaScript文件 - main.js

// DOM加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    console.log('学习笔记应用已加载');
    
    // 初始化功能
    initializeApp();
});

function initializeApp() {
    // 添加平滑滚动
    addSmoothScrolling();
    
    // 初始化表单验证
    initializeFormValidation();
    
    // 添加交互效果
    addInteractiveEffects();
    
    // 初始化主题切换
    initializeThemeToggle();
}

function addSmoothScrolling() {
    // 为所有内部链接添加平滑滚动
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

function initializeFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
                showAlert('请填写所有必填字段', 'danger');
            }
        });
    });
}

function validateForm(form) {
    const requiredFields = form.querySelectorAll('[required]');
    let isValid = true;
    
    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            field.classList.add('is-invalid');
            isValid = false;
        } else {
            field.classList.remove('is-invalid');
        }
    });
    
    return isValid;
}

function addInteractiveEffects() {
    // 卡片悬停效果
    const cards = document.querySelectorAll('.card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // 按钮点击效果
    const buttons = document.querySelectorAll('.btn');
    
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            // 创建涟漪效果
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
}

function initializeThemeToggle() {
    // 主题切换功能
    const themeToggle = document.createElement('button');
    themeToggle.innerHTML = '🌙';
    themeToggle.className = 'theme-toggle';
    themeToggle.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: #667eea;
        color: white;
        border: none;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        cursor: pointer;
        font-size: 20px;
        z-index: 1000;
        transition: all 0.3s;
    `;
    
    document.body.appendChild(themeToggle);
    
    themeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-theme');
        this.innerHTML = document.body.classList.contains('dark-theme') ? '☀️' : '🌙';
    });
}

function showAlert(message, type = 'info') {
    // 创建警告框
    const alert = document.createElement('div');
    alert.className = `alert alert-${type} alert-dismissible fade show`;
    alert.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // 添加到页面顶部
    const container = document.querySelector('.container');
    if (container) {
        container.insertBefore(alert, container.firstChild);
        
        // 自动消失
        setTimeout(() => {
            alert.remove();
        }, 5000);
    }
}

// 工具函数
const utils = {
    // 防抖函数
    debounce: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    // 格式化日期
    formatDate: function(date) {
        return new Intl.DateTimeFormat('zh-CN', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        }).format(new Date(date));
    },
    
    // Ajax请求封装
    ajax: function(url, options = {}) {
        const defaultOptions = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        };
        
        const config = { ...defaultOptions, ...options };
        
        return fetch(url, config)
            .then(response => response.json())
            .catch(error => {
                console.error('请求失败:', error);
                showAlert('网络请求失败', 'danger');
            });
    }
};

// 导出工具函数
window.utils = utils;
"""
        
        with open(f"{self.project_dir}/static/js/main.js", 'w', encoding='utf-8') as f:
            f.write(main_js)
        
        print("JavaScript文件已创建")
    
    def create_deployment_config(self):
        """创建部署配置文件"""
        print("创建部署配置文件...")
        
        # requirements.txt
        requirements = """
Django==4.2.7
gunicorn==21.2.0
whitenoise==6.6.0
psycopg2-binary==2.9.9
python-decouple==3.8
dj-database-url==2.1.0
"""
        
        with open(f"{self.project_dir}/requirements.txt", 'w') as f:
            f.write(requirements.strip())
        
        # Procfile (for Heroku)
        procfile = "web: gunicorn learning_log.wsgi --log-file -"
        
        with open(f"{self.project_dir}/Procfile", 'w') as f:
            f.write(procfile)
        
        # Docker配置
        dockerfile = """
FROM python:3.11-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \\
    gcc \\
    postgresql-client \\
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 收集静态文件
RUN python manage.py collectstatic --noinput

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "learning_log.wsgi:application"]
"""
        
        with open(f"{self.project_dir}/Dockerfile", 'w') as f:
            f.write(dockerfile)
        
        # docker-compose.yml
        docker_compose = """
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - DATABASE_URL=postgresql://user:password@db:5432/learning_log
    depends_on:
      - db
    volumes:
      - static_volume:/app/static

  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=learning_log
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
      - static_volume:/static
    depends_on:
      - web

volumes:
  postgres_data:
  static_volume:
"""
        
        with open(f"{self.project_dir}/docker-compose.yml", 'w') as f:
            f.write(docker_compose)
        
        print("部署配置文件已创建")
    
    def create_deployment_guide(self):
        """创建部署指南"""
        print("创建部署指南...")
        
        guide = """
# Web应用部署指南

## 项目结构
```
web_project_demo/
├── static/
│   ├── css/
│   │   └── main.css
│   ├── js/
│   │   └── main.js
│   └── images/
├── templates/
│   └── index.html
├── config/
├── requirements.txt
├── Procfile
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 本地开发

### 1. 环境准备
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\\Scripts\\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 开发服务器
```bash
# 运行开发服务器
python manage.py runserver

# 访问应用
# http://127.0.0.1:8000
```

## 生产环境部署

### 方法1: Heroku部署

1. 安装Heroku CLI
2. 登录Heroku: `heroku login`
3. 创建应用: `heroku create your-app-name`
4. 设置环境变量:
   ```bash
   heroku config:set DEBUG=False
   heroku config:set SECRET_KEY=your-secret-key
   ```
5. 部署: `git push heroku main`

### 方法2: Docker部署

```bash
# 构建镜像
docker build -t learning-log .

# 运行容器
docker run -p 8000:8000 learning-log

# 或使用docker-compose
docker-compose up -d
```

### 方法3: VPS部署

1. 服务器准备:
   ```bash
   # 更新系统
   sudo apt update && sudo apt upgrade

   # 安装Python和依赖
   sudo apt install python3 python3-pip nginx postgresql

   # 创建数据库用户
   sudo -u postgres createuser --interactive
   sudo -u postgres createdb learning_log
   ```

2. 应用部署:
   ```bash
   # 克隆代码
   git clone your-repo-url
   cd learning-log

   # 安装依赖
   pip3 install -r requirements.txt

   # 数据库迁移
   python3 manage.py migrate

   # 收集静态文件
   python3 manage.py collectstatic

   # 启动Gunicorn
   gunicorn --bind 0.0.0.0:8000 learning_log.wsgi
   ```

3. Nginx配置:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location /static/ {
           alias /path/to/your/static/files/;
       }

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

## 性能优化

### 1. 静态文件优化
- 使用CDN托管静态文件
- 启用文件压缩
- 设置适当的缓存头

### 2. 数据库优化
- 添加适当的索引
- 使用数据库连接池
- 启用查询缓存

### 3. 应用优化
- 使用缓存系统（Redis/Memcached）
- 启用数据库查询优化
- 使用异步任务处理（Celery）

## 监控和维护

### 1. 日志管理
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### 2. 健康检查
- 设置应用健康检查端点
- 监控服务器资源使用
- 设置告警机制

### 3. 备份策略
- 定期备份数据库
- 备份用户上传的文件
- 测试恢复流程

## 安全配置

### 1. Django安全设置
```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

### 2. 服务器安全
- 配置防火墙
- 启用SSL证书
- 定期更新系统

## 故障排除

### 常见问题:
1. 静态文件404 - 检查STATIC_URL和STATICFILES_DIRS配置
2. 数据库连接失败 - 检查数据库配置和网络连接
3. 502/503错误 - 检查应用服务器状态

### 调试工具:
- Django Debug Toolbar (开发环境)
- Sentry (错误监控)
- New Relic (性能监控)
"""
        
        with open(f"{self.project_dir}/DEPLOYMENT.md", 'w', encoding='utf-8') as f:
            f.write(guide)
        
        print("部署指南已创建")
    
    def show_project_summary(self):
        """显示项目总结"""
        print("\n" + "=" * 60)
        print("第20章 - Web应用样式和部署项目已完成")
        print("=" * 60)
        
        print("\n已创建的文件:")
        for root, dirs, files in os.walk(self.project_dir):
            level = root.replace(self.project_dir, '').count(os.sep)
            indent = ' ' * 2 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 2 * (level + 1)
            for file in files:
                print(f"{subindent}{file}")
        
        print(f"\n项目特性:")
        print("✅ 响应式CSS设计")
        print("✅ Bootstrap集成")
        print("✅ JavaScript交互效果")
        print("✅ Docker容器化")
        print("✅ Heroku部署配置")
        print("✅ Nginx生产环境配置")
        print("✅ 安全和性能优化指南")
        
        print(f"\n下一步:")
        print(f"1. cd {self.project_dir}")
        print("2. 根据DEPLOYMENT.md指南部署应用")
        print("3. 自定义样式和功能")


def main():
    """主函数"""
    print("=" * 60)
    print("第20章 - 设置样式和部署演示")
    print("=" * 60)
    
    style_manager = WebStyleManager()
    
    try:
        print("\n开始创建Web应用项目...")
        
        # 创建各种文件
        style_manager.create_css_styles()
        style_manager.create_html_templates()
        style_manager.create_javascript()
        style_manager.create_deployment_config()
        style_manager.create_deployment_guide()
        
        # 显示项目总结
        style_manager.show_project_summary()
        
        print("\n项目创建完成！")
        print("这个演示展示了完整的Web应用开发流程，包括:")
        print("- 现代CSS样式设计")
        print("- JavaScript交互功能")
        print("- 多种部署方案")
        print("- 生产环境配置")
        print("- 性能和安全优化")
        
    except Exception as e:
        print(f"创建项目时出错: {e}")
    
    input("\n按回车键退出...")


if __name__ == '__main__':
    main() 