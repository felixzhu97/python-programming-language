# 第 12 章 外星人入侵游戏

## 学习目标

通过本章的学习，您将能够：

1. 掌握 Pygame 游戏开发基础
2. 学会创建游戏窗口和处理事件
3. 理解游戏循环的概念
4. 掌握精灵（Sprite）系统的使用
5. 学会实现碰撞检测
6. 创建一个完整的射击游戏

## 文件说明

### 核心游戏文件

1. **alien_invasion.py** - 完整版外星人入侵游戏主文件

   - 包含完整的游戏逻辑
   - 支持得分系统、多关卡、按钮界面
   - 需要配套的模块文件

2. **simple_alien_invasion.py** - 简化版游戏（推荐新手）

   - 独立运行，无需额外依赖
   - 包含完整游戏功能
   - 易于理解和修改

3. **pygame_demo.py** - Pygame 基础演示
   - 窗口创建和事件处理
   - 图形绘制基础
   - 精灵系统演示
   - 简单游戏循环

### 游戏模块文件

4. **settings.py** - 游戏设置配置
5. **ship.py** - 飞船类
6. **bullet.py** - 子弹类
7. **alien.py** - 外星人类
8. **game_stats.py** - 游戏统计信息
9. **button.py** - 游戏按钮
10. **scoreboard.py** - 记分牌

## 快速开始

### 安装依赖

```bash
pip install pygame
```

### 运行演示

```bash
# 1. Pygame基础演示
python pygame_demo.py

# 2. 简化版游戏（推荐）
python simple_alien_invasion.py

# 3. 完整版游戏（需要所有模块文件）
python alien_invasion.py
```

## 游戏控制

### 简化版游戏控制

- **左右箭头键**：移动飞船
- **空格键**：发射子弹
- **P 键**：重新开始（游戏结束时）
- **Q 键**：退出游戏

### 完整版游戏控制

- **左右箭头键**：移动飞船
- **空格键**：发射子弹
- **P 键**：开始新游戏
- **Q 键**：退出游戏
- **鼠标点击**：点击"开始游戏"按钮

## Pygame 基础概念

### 1. 游戏循环

游戏的核心是主循环，包含三个基本步骤：

```python
while running:
    # 1. 处理事件
    handle_events()

    # 2. 更新游戏状态
    update()

    # 3. 绘制画面
    draw()
```

### 2. 事件处理

Pygame 通过事件系统处理用户输入：

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            fire_bullet()
```

### 3. 精灵系统

精灵是 Pygame 中表示游戏对象的类：

```python
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.rect = self.image.get_rect()

    def update(self):
        # 更新精灵状态
        pass
```

### 4. 碰撞检测

```python
# 检测两个精灵组之间的碰撞
collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
```

## 游戏开发流程

### 第一步：创建游戏窗口

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("我的游戏")
```

### 第二步：设置游戏循环

```python
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # 黑色背景
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
```

### 第三步：添加游戏对象

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # 红色
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
```

### 第四步：处理用户输入

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player.rect.x -= 5
if keys[pygame.K_RIGHT]:
    player.rect.x += 5
```

### 第五步：实现游戏逻辑

- 移动和动画
- 碰撞检测
- 得分系统
- 游戏状态管理

## 外星人入侵游戏特性

### 基本功能

- ✅ 玩家飞船控制
- ✅ 子弹发射系统
- ✅ 外星人群体移动
- ✅ 碰撞检测
- ✅ 得分系统

### 高级功能（完整版）

- ✅ 多关卡系统
- ✅ 难度递增
- ✅ 最高分记录
- ✅ 图形界面按钮
- ✅ 生命值系统

## 常见问题解决

### 1. Pygame 安装问题

```bash
# Windows
pip install pygame

# macOS
pip3 install pygame

# Linux
sudo apt-get install python3-pygame
```

### 2. 图像文件缺失

游戏会自动生成简单的几何形状作为替代：

- 飞船：蓝色矩形
- 外星人：绿色矩形
- 子弹：黄色小矩形

### 3. 性能优化

- 使用`pygame.sprite.Group()`管理大量对象
- 合理设置帧率（通常 60FPS）
- 及时删除不需要的精灵对象

## 扩展建议

### 初级扩展

1. 添加音效和背景音乐
2. 创建更多种类的外星人
3. 增加 power-up 道具
4. 添加爆炸动画效果

### 中级扩展

1. 实现多人游戏模式
2. 添加 boss 关卡
3. 创建关卡编辑器
4. 实现存档系统

### 高级扩展

1. 使用更复杂的物理引擎
2. 实现网络对战功能
3. 添加粒子效果系统
4. 创建关卡生成算法

## 学习资源

### 推荐阅读

- [Pygame 官方文档](https://www.pygame.org/docs/)
- [Real Python Pygame 教程](https://realpython.com/pygame-a-primer/)

### 相关概念

- 游戏开发模式
- 面向对象编程在游戏中的应用
- 事件驱动编程
- 实时系统设计

通过完成这个项目，您将获得游戏开发的实战经验，为后续的更复杂项目打下基础。
