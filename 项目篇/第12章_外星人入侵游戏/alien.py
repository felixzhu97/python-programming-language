#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
外星人入侵游戏 - 外星人类
表示单个外星人的类
"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, ai_game):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # 加载外星人图像并设置其rect属性
        try:
            self.image = pygame.image.load('images/alien.bmp')
        except pygame.error:
            # 如果图像文件不存在，创建一个简单的矩形作为外星人
            self.image = pygame.Surface((40, 30))
            self.image.fill((0, 150, 0))
        
        self.rect = self.image.get_rect()
        
        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        """向右或向左移动外星人"""
        self.x += (self.settings.alien_speed * 
                  self.settings.fleet_direction)
        self.rect.x = self.x 