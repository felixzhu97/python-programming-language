#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
外星人入侵游戏 - 飞船类
管理飞船的行为
"""

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """管理飞船的类"""
    
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # 加载飞船图像并获取其外接矩形
        try:
            self.image = pygame.image.load('images/ship.bmp')
        except pygame.error:
            # 如果图像文件不存在，创建一个简单的矩形作为飞船
            self.image = pygame.Surface((50, 30))
            self.image.fill((0, 100, 200))
        
        self.rect = self.image.get_rect()
        
        # 对于每艘新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        
        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # 根据self.x更新rect对象
        self.rect.x = self.x
    
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """让飞船在屏幕底端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x) 