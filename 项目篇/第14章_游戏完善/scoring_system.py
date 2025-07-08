#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第14章 - 游戏得分系统和平衡调整
演示完整的得分系统、难度平衡、数据存储等

主要功能：
1. 高级得分系统
2. 成就系统
3. 数据持久化
4. 难度平衡
5. 统计分析
"""

import pygame
import json
import time
from datetime import datetime


class ScoreSystem:
    """得分系统"""
    
    def __init__(self):
        self.score = 0
        self.multiplier = 1.0
        self.streak = 0
        self.max_streak = 0
        self.combo_timer = 0
        self.level_bonus = 0
        
    def add_score(self, base_points):
        """添加分数"""
        # 计算最终分数
        final_points = int(base_points * self.multiplier)
        self.score += final_points
        
        # 更新连击
        self.streak += 1
        self.max_streak = max(self.max_streak, self.streak)
        self.combo_timer = 120  # 2秒连击时间
        
        # 连击倍数
        if self.streak >= 10:
            self.multiplier = 3.0
        elif self.streak >= 5:
            self.multiplier = 2.0
        else:
            self.multiplier = 1.0
        
        return final_points
    
    def update(self):
        """更新得分系统"""
        if self.combo_timer > 0:
            self.combo_timer -= 1
        else:
            self.streak = 0
            self.multiplier = 1.0
    
    def get_rank(self):
        """获取等级"""
        if self.score >= 100000:
            return "传奇"
        elif self.score >= 50000:
            return "大师"
        elif self.score >= 20000:
            return "专家"
        elif self.score >= 10000:
            return "高手"
        elif self.score >= 5000:
            return "新手"
        else:
            return "菜鸟"


class AchievementSystem:
    """成就系统"""
    
    def __init__(self):
        self.achievements = {
            'first_kill': {'name': '首次击杀', 'description': '击败第一个敌人', 'unlocked': False},
            'combo_master': {'name': '连击大师', 'description': '达到10连击', 'unlocked': False},
            'score_1000': {'name': '千分达人', 'description': '达到1000分', 'unlocked': False},
            'score_10000': {'name': '万分高手', 'description': '达到10000分', 'unlocked': False},
            'survivor': {'name': '生存者', 'description': '存活5分钟', 'unlocked': False},
            'perfectionist': {'name': '完美主义', 'description': '一关不掉血', 'unlocked': False}
        }
        self.newly_unlocked = []
    
    def check_achievement(self, achievement_id, condition):
        """检查成就"""
        if achievement_id in self.achievements and not self.achievements[achievement_id]['unlocked']:
            if condition:
                self.achievements[achievement_id]['unlocked'] = True
                self.newly_unlocked.append(achievement_id)
                return True
        return False
    
    def get_unlocked_count(self):
        """获取已解锁成就数量"""
        return sum(1 for ach in self.achievements.values() if ach['unlocked'])


class GameStats:
    """游戏统计"""
    
    def __init__(self):
        self.games_played = 0
        self.total_score = 0
        self.best_score = 0
        self.total_time = 0
        self.enemies_killed = 0
        self.shots_fired = 0
        self.shots_hit = 0
        self.start_time = None
        
    def start_game(self):
        """开始游戏"""
        self.start_time = time.time()
        self.games_played += 1
    
    def end_game(self, final_score):
        """结束游戏"""
        if self.start_time:
            game_time = time.time() - self.start_time
            self.total_time += game_time
            self.start_time = None
        
        self.total_score += final_score
        self.best_score = max(self.best_score, final_score)
    
    def get_accuracy(self):
        """获取命中率"""
        if self.shots_fired == 0:
            return 0
        return (self.shots_hit / self.shots_fired) * 100
    
    def get_average_score(self):
        """获取平均分数"""
        if self.games_played == 0:
            return 0
        return self.total_score / self.games_played


class GameData:
    """游戏数据管理"""
    
    def __init__(self, filename='game_data.json'):
        self.filename = filename
        self.data = {
            'scores': [],
            'achievements': {},
            'stats': {},
            'settings': {
                'sound_enabled': True,
                'difficulty': 'normal',
                'player_name': '玩家'
            }
        }
        self.load_data()
    
    def load_data(self):
        """加载数据"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print("数据文件不存在，创建新文件")
            self.save_data()
        except json.JSONDecodeError:
            print("数据文件损坏，重新创建")
            self.save_data()
    
    def save_data(self):
        """保存数据"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存数据失败: {e}")
    
    def add_score(self, score, player_name='玩家'):
        """添加分数记录"""
        score_entry = {
            'score': score,
            'player': player_name,
            'date': datetime.now().isoformat(),
            'timestamp': time.time()
        }
        self.data['scores'].append(score_entry)
        
        # 保持最高分记录（只保留前10名）
        self.data['scores'].sort(key=lambda x: x['score'], reverse=True)
        self.data['scores'] = self.data['scores'][:10]
        
        self.save_data()
    
    def get_high_scores(self, limit=5):
        """获取高分榜"""
        return self.data['scores'][:limit]
    
    def update_achievements(self, achievements):
        """更新成就"""
        self.data['achievements'] = {k: v['unlocked'] for k, v in achievements.items()}
        self.save_data()
    
    def update_stats(self, stats):
        """更新统计数据"""
        self.data['stats'] = {
            'games_played': stats.games_played,
            'total_score': stats.total_score,
            'best_score': stats.best_score,
            'total_time': stats.total_time,
            'enemies_killed': stats.enemies_killed,
            'accuracy': stats.get_accuracy()
        }
        self.save_data()


class DifficultyManager:
    """难度管理器"""
    
    def __init__(self):
        self.difficulty_settings = {
            'easy': {
                'enemy_speed': 0.5,
                'enemy_spawn_rate': 0.7,
                'player_health': 5,
                'score_multiplier': 0.8
            },
            'normal': {
                'enemy_speed': 1.0,
                'enemy_spawn_rate': 1.0,
                'player_health': 3,
                'score_multiplier': 1.0
            },
            'hard': {
                'enemy_speed': 1.5,
                'enemy_spawn_rate': 1.3,
                'player_health': 2,
                'score_multiplier': 1.5
            },
            'nightmare': {
                'enemy_speed': 2.0,
                'enemy_spawn_rate': 1.8,
                'player_health': 1,
                'score_multiplier': 2.0
            }
        }
        self.current_difficulty = 'normal'
    
    def set_difficulty(self, difficulty):
        """设置难度"""
        if difficulty in self.difficulty_settings:
            self.current_difficulty = difficulty
            return True
        return False
    
    def get_settings(self):
        """获取当前难度设置"""
        return self.difficulty_settings[self.current_difficulty]
    
    def adjust_dynamic_difficulty(self, player_performance):
        """动态难度调整"""
        # 根据玩家表现调整难度
        if player_performance > 0.8:  # 表现很好
            return min(1.2, 1.0 + (player_performance - 0.8) * 2)
        elif player_performance < 0.3:  # 表现较差
            return max(0.8, 1.0 - (0.3 - player_performance) * 2)
        else:
            return 1.0


class ScoreDemo:
    """得分系统演示"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("第14章 - 得分系统演示")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # 初始化系统
        self.score_system = ScoreSystem()
        self.achievement_system = AchievementSystem()
        self.game_stats = GameStats()
        self.game_data = GameData()
        self.difficulty_manager = DifficultyManager()
        
        # 演示状态
        self.demo_timer = 0
        self.current_page = 0  # 0: 得分, 1: 成就, 2: 统计, 3: 高分榜
        self.pages = ['得分系统', '成就系统', '游戏统计', '高分榜']
        
        # 模拟游戏开始
        self.game_stats.start_game()
    
    def handle_events(self):
        """处理事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # 模拟击杀敌人
                    points = self.score_system.add_score(100)
                    self.game_stats.enemies_killed += 1
                    self.game_stats.shots_hit += 1
                    
                    # 检查成就
                    self.check_achievements()
                    
                elif event.key == pygame.K_s:
                    # 模拟射击
                    self.game_stats.shots_fired += 1
                    
                elif event.key == pygame.K_LEFT:
                    self.current_page = (self.current_page - 1) % len(self.pages)
                elif event.key == pygame.K_RIGHT:
                    self.current_page = (self.current_page + 1) % len(self.pages)
                    
                elif event.key == pygame.K_r:
                    # 重置演示
                    self.reset_demo()
                    
                elif event.key == pygame.K_h:
                    # 保存高分
                    self.game_data.add_score(self.score_system.score)
                    
                elif event.key == pygame.K_q:
                    return False
                    
        return True
    
    def check_achievements(self):
        """检查成就解锁"""
        # 首次击杀
        self.achievement_system.check_achievement('first_kill', 
                                                self.game_stats.enemies_killed >= 1)
        
        # 连击大师
        self.achievement_system.check_achievement('combo_master', 
                                                self.score_system.streak >= 10)
        
        # 分数成就
        self.achievement_system.check_achievement('score_1000', 
                                                self.score_system.score >= 1000)
        self.achievement_system.check_achievement('score_10000', 
                                                self.score_system.score >= 10000)
        
        # 生存者
        if self.game_stats.start_time:
            survival_time = time.time() - self.game_stats.start_time
            self.achievement_system.check_achievement('survivor', survival_time >= 300)
    
    def reset_demo(self):
        """重置演示"""
        self.score_system = ScoreSystem()
        self.game_stats = GameStats()
        self.game_stats.start_game()
    
    def update(self):
        """更新系统"""
        self.score_system.update()
        self.demo_timer += 1
        
        # 自动演示
        if self.demo_timer % 60 == 0:  # 每秒
            if self.demo_timer % 180 == 0:  # 每3秒自动击杀
                points = self.score_system.add_score(50)
                self.game_stats.enemies_killed += 1
                self.check_achievements()
    
    def draw_score_page(self):
        """绘制得分页面"""
        y = 80
        
        # 当前分数
        score_text = self.font.render(f"当前分数: {self.score_system.score:,}", True, (255, 255, 0))
        self.screen.blit(score_text, (50, y))
        y += 50
        
        # 连击信息
        streak_text = self.font.render(f"连击: {self.score_system.streak} (最高: {self.score_system.max_streak})", True, (255, 255, 255))
        self.screen.blit(streak_text, (50, y))
        y += 40
        
        # 倍数
        multiplier_text = self.font.render(f"得分倍数: {self.score_system.multiplier:.1f}x", True, (0, 255, 255))
        self.screen.blit(multiplier_text, (50, y))
        y += 40
        
        # 等级
        rank_text = self.font.render(f"等级: {self.score_system.get_rank()}", True, (255, 0, 255))
        self.screen.blit(rank_text, (50, y))
        y += 60
        
        # 操作说明
        instructions = [
            "空格键 - 击杀敌人 (+100分)",
            "S键 - 射击 (统计命中率)",
            "H键 - 保存当前分数到高分榜"
        ]
        
        for instruction in instructions:
            text = self.small_font.render(instruction, True, (200, 200, 200))
            self.screen.blit(text, (50, y))
            y += 30
    
    def draw_achievement_page(self):
        """绘制成就页面"""
        y = 80
        
        unlocked_count = self.achievement_system.get_unlocked_count()
        total_count = len(self.achievement_system.achievements)
        
        progress_text = self.font.render(f"成就进度: {unlocked_count}/{total_count}", True, (255, 255, 0))
        self.screen.blit(progress_text, (50, y))
        y += 50
        
        for ach_id, ach_data in self.achievement_system.achievements.items():
            color = (0, 255, 0) if ach_data['unlocked'] else (128, 128, 128)
            status = "✓" if ach_data['unlocked'] else "✗"
            
            ach_text = self.small_font.render(f"{status} {ach_data['name']}: {ach_data['description']}", True, color)
            self.screen.blit(ach_text, (50, y))
            y += 35
    
    def draw_stats_page(self):
        """绘制统计页面"""
        y = 80
        
        stats_info = [
            f"击杀敌人: {self.game_stats.enemies_killed}",
            f"发射子弹: {self.game_stats.shots_fired}",
            f"命中子弹: {self.game_stats.shots_hit}",
            f"命中率: {self.game_stats.get_accuracy():.1f}%",
            f"游戏时长: {time.time() - self.game_stats.start_time:.1f}秒" if self.game_stats.start_time else "游戏时长: 0秒"
        ]
        
        for info in stats_info:
            text = self.font.render(info, True, (255, 255, 255))
            self.screen.blit(text, (50, y))
            y += 45
    
    def draw_highscore_page(self):
        """绘制高分榜页面"""
        y = 80
        
        title = self.font.render("高分榜 TOP 5", True, (255, 255, 0))
        self.screen.blit(title, (50, y))
        y += 50
        
        high_scores = self.game_data.get_high_scores()
        
        if not high_scores:
            no_scores = self.font.render("暂无记录", True, (128, 128, 128))
            self.screen.blit(no_scores, (50, y))
        else:
            for i, score_entry in enumerate(high_scores):
                rank_text = f"{i+1}. {score_entry['player']}: {score_entry['score']:,}"
                color = [(255, 215, 0), (192, 192, 192), (205, 127, 50)][min(i, 2)]  # 金银铜
                if i >= 3:
                    color = (255, 255, 255)
                
                text = self.font.render(rank_text, True, color)
                self.screen.blit(text, (50, y))
                y += 40
    
    def draw(self):
        """绘制界面"""
        self.screen.fill((20, 20, 40))
        
        # 标题和页面导航
        title = self.font.render(f"第14章 - {self.pages[self.current_page]}", True, (255, 255, 255))
        self.screen.blit(title, (50, 20))
        
        nav_text = self.small_font.render("← → 切换页面 | R-重置 | Q-退出", True, (200, 200, 200))
        self.screen.blit(nav_text, (50, 550))
        
        # 绘制当前页面内容
        if self.current_page == 0:
            self.draw_score_page()
        elif self.current_page == 1:
            self.draw_achievement_page()
        elif self.current_page == 2:
            self.draw_stats_page()
        elif self.current_page == 3:
            self.draw_highscore_page()
        
        # 显示新解锁的成就
        if self.achievement_system.newly_unlocked:
            ach_id = self.achievement_system.newly_unlocked[0]
            ach_data = self.achievement_system.achievements[ach_id]
            
            # 成就通知框
            pygame.draw.rect(self.screen, (0, 150, 0), (200, 250, 400, 100))
            pygame.draw.rect(self.screen, (255, 255, 255), (200, 250, 400, 100), 3)
            
            unlock_text = self.font.render("成就解锁!", True, (255, 255, 255))
            name_text = self.small_font.render(ach_data['name'], True, (255, 255, 255))
            desc_text = self.small_font.render(ach_data['description'], True, (200, 200, 200))
            
            self.screen.blit(unlock_text, (210, 260))
            self.screen.blit(name_text, (210, 290))
            self.screen.blit(desc_text, (210, 315))
            
            # 3秒后移除通知
            if self.demo_timer % 180 == 0:
                self.achievement_system.newly_unlocked.clear()
        
        pygame.display.flip()
    
    def run(self):
        """运行演示"""
        print("=" * 50)
        print("第14章 - 游戏得分系统演示")
        print("=" * 50)
        print("功能展示：")
        print("1. 高级得分系统（连击、倍数）")
        print("2. 成就系统")
        print("3. 游戏统计")
        print("4. 高分榜和数据持久化")
        print("5. 难度管理")
        print("\n使用左右箭头键切换页面")
        print("=" * 50)
        
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        
        # 保存数据
        self.game_stats.end_game(self.score_system.score)
        self.game_data.update_achievements(self.achievement_system.achievements)
        self.game_data.update_stats(self.game_stats)
        
        pygame.quit()
        print("演示结束，数据已保存！")


def main():
    """主函数"""
    try:
        demo = ScoreDemo()
        demo.run()
    except pygame.error as e:
        print(f"Pygame错误: {e}")
        print("请确保已安装pygame: pip install pygame")
    except Exception as e:
        print(f"演示错误: {e}")


if __name__ == '__main__':
    main() 