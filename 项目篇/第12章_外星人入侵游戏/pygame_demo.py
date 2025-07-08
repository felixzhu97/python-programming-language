#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第12章 外星人入侵游戏 - Pygame基础演示
演示Pygame的基本概念和用法

主要内容：
1. Pygame窗口创建
2. 事件处理
3. 图形绘制
4. 游戏循环
5. 精灵（Sprite）使用
"""

import sys
import pygame


# ==================== 基础Pygame窗口 ====================

def basic_pygame_window():
    """创建一个基础的Pygame窗口"""
    print("=== 基础Pygame窗口演示 ===")
    
    # 初始化Pygame
    pygame.init()
    
    # 设置屏幕尺寸和颜色
    screen_width = 800
    screen_height = 600
    bg_color = (230, 230, 230)  # 浅灰色
    
    # 创建屏幕
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame基础窗口")
    
    # 游戏主循环
    clock = pygame.time.Clock()
    running = True
    
    while running:
        # 检查事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
        
        # 填充背景色
        screen.fill(bg_color)
        
        # 更新显示
        pygame.display.flip()
        clock.tick(60)  # 60 FPS
    
    pygame.quit()
    print("窗口已关闭")


# ==================== 事件处理演示 ====================

def event_handling_demo():
    """演示各种事件处理"""
    print("\n=== 事件处理演示 ===")
    print("按键说明：")
    print("- 方向键：移动红色方块")
    print("- 空格键：改变方块颜色")
    print("- ESC或Q：退出")
    print("- 鼠标点击：在点击位置绘制圆圈")
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("事件处理演示")
    
    # 方块属性
    rect_x = 375
    rect_y = 275
    rect_width = 50
    rect_height = 50
    rect_color = (255, 0, 0)  # 红色
    speed = 5
    
    # 颜色列表
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    color_index = 0
    
    # 圆圈列表
    circles = []
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_SPACE:
                    # 改变方块颜色
                    color_index = (color_index + 1) % len(colors)
                    rect_color = colors[color_index]
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 在鼠标点击位置添加圆圈
                mouse_x, mouse_y = event.pos
                circles.append((mouse_x, mouse_y))
        
        # 检查持续按键
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and rect_x > 0:
            rect_x -= speed
        if keys[pygame.K_RIGHT] and rect_x < 800 - rect_width:
            rect_x += speed
        if keys[pygame.K_UP] and rect_y > 0:
            rect_y -= speed
        if keys[pygame.K_DOWN] and rect_y < 600 - rect_height:
            rect_y += speed
        
        # 绘制
        screen.fill((230, 230, 230))
        
        # 绘制方块
        pygame.draw.rect(screen, rect_color, 
                        (rect_x, rect_y, rect_width, rect_height))
        
        # 绘制圆圈
        for circle_x, circle_y in circles:
            pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), 10)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()


# ==================== 简单精灵演示 ====================

class SimpleSprite(pygame.sprite.Sprite):
    """简单的精灵类演示"""
    
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 3
        self.speed_y = 2
    
    def update(self):
        """更新精灵位置"""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # 边界碰撞检测
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y = -self.speed_y


def sprite_demo():
    """精灵演示"""
    print("\n=== 精灵演示 ===")
    print("观看彩色方块在屏幕中弹跳")
    print("按ESC或Q退出")
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("精灵演示")
    
    # 创建精灵组
    all_sprites = pygame.sprite.Group()
    
    # 创建多个精灵
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
    for i in range(5):
        sprite = SimpleSprite(100 + i * 100, 100 + i * 50, colors[i])
        all_sprites.add(sprite)
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False
        
        # 更新精灵
        all_sprites.update()
        
        # 绘制
        screen.fill((0, 0, 0))  # 黑色背景
        all_sprites.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()


# ==================== 简化版飞船游戏 ====================

class SimpleBullet(pygame.sprite.Sprite):
    """简单的子弹类"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((3, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 5
    
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()


class SimpleShip(pygame.sprite.Sprite):
    """简单的飞船类"""
    
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill((0, 100, 200))
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.bottom = 580
        self.speed = 5
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed
    
    def shoot(self):
        return SimpleBullet(self.rect.centerx, self.rect.top)


def simple_ship_game():
    """简化版飞船游戏"""
    print("\n=== 简化版飞船游戏 ===")
    print("控制说明：")
    print("- 左右箭头键：移动飞船")
    print("- 空格键：发射子弹")
    print("- ESC或Q：退出")
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("简化版飞船游戏")
    
    # 创建精灵组
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    # 创建飞船
    ship = SimpleShip()
    all_sprites.add(ship)
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_SPACE:
                    bullet = ship.shoot()
                    all_sprites.add(bullet)
                    bullets.add(bullet)
        
        # 更新
        all_sprites.update()
        
        # 绘制
        screen.fill((0, 0, 50))  # 深蓝色背景
        
        # 绘制星星
        for i in range(50):
            x = (i * 37) % 800
            y = (i * 23) % 600
            pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)
        
        all_sprites.draw(screen)
        
        # 显示信息
        font = pygame.font.Font(None, 36)
        text = font.render(f"子弹数量: {len(bullets)}", True, (255, 255, 255))
        screen.blit(text, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()


# ==================== 主程序 ====================

def main():
    """主程序"""
    print("第12章 外星人入侵游戏 - Pygame基础演示")
    print("=" * 50)
    
    while True:
        print("\n请选择演示项目：")
        print("1. 基础Pygame窗口")
        print("2. 事件处理演示")
        print("3. 精灵演示")
        print("4. 简化版飞船游戏")
        print("0. 退出")
        
        choice = input("\n请输入选择 (0-4): ").strip()
        
        if choice == '1':
            basic_pygame_window()
        elif choice == '2':
            event_handling_demo()
        elif choice == '3':
            sprite_demo()
        elif choice == '4':
            simple_ship_game()
        elif choice == '0':
            print("再见！")
            break
        else:
            print("无效选择，请重试")


if __name__ == '__main__':
    main() 