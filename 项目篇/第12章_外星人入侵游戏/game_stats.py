#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
外星人入侵游戏 - 游戏统计信息
跟踪游戏的统计信息
"""

import json


class GameStats:
    """跟踪游戏的统计信息"""
    
    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # 游戏刚启动时处于非活动状态
        self.game_active = False
        
        # 在任何情况下都不应重置最高得分
        self.high_score = self.load_high_score()
    
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def load_high_score(self):
        """从文件中加载最高得分"""
        filename = 'high_score.json'
        try:
            with open(filename, 'r') as f:
                high_score = json.load(f)
                return high_score
        except FileNotFoundError:
            return 0
    
    def save_high_score(self):
        """将最高得分保存到文件中"""
        filename = 'high_score.json'
        with open(filename, 'w') as f:
            json.dump(self.high_score, f) 