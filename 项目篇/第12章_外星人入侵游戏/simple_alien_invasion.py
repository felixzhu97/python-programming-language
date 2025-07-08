#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化版外星人入侵游戏
演示游戏开发的基本概念

游戏规则：
- 使用左右箭头键控制飞船移动
- 按空格键发射子弹
- 击中外星人得分
- 外星人触及飞船或底部时游戏结束
- 按P键开始新游戏
"""

import pygame
import sys
import random


# 游戏设置
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SHIP_SPEED = 5
BULLET_SPEED = 7
ALIEN_SPEED = 1
FPS = 60

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)


class Ship(pygame.sprite.Sprite):
    """玩家飞船类"""
    
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = SHIP_SPEED
        self.moving_left = False
        self.moving_right = False
    
    def update(self):
        """更新飞船位置"""
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
        if self.moving_right and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
    
    def shoot(self):
        """发射子弹"""
        return Bullet(self.rect.centerx, self.rect.top)


class Bullet(pygame.sprite.Sprite):
    """子弹类"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((3, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = BULLET_SPEED
    
    def update(self):
        """更新子弹位置"""
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()


class Alien(pygame.sprite.Sprite):
    """外星人类"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = ALIEN_SPEED
        self.direction = 1  # 1向右，-1向左
    
    def update(self):
        """更新外星人位置"""
        self.rect.x += self.speed * self.direction
    
    def drop_down(self):
        """向下移动一行"""
        self.rect.y += 40
        self.direction *= -1


class Game:
    """游戏主类"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("简化版外星人入侵")
        self.clock = pygame.time.Clock()
        
        # 创建精灵组
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        # 创建飞船
        self.ship = Ship()
        self.all_sprites.add(self.ship)
        
        # 游戏状态
        self.score = 0
        self.game_over = False
        self.font = pygame.font.Font(None, 36)
        
        # 创建外星人群
        self.create_alien_fleet()
    
    def create_alien_fleet(self):
        """创建外星人群"""
        alien_width = 40
        alien_height = 30
        
        # 计算每行外星人数量
        aliens_per_row = SCREEN_WIDTH // (alien_width + 10)
        
        # 创建4行外星人
        for row in range(4):
            for col in range(aliens_per_row - 2):  # 留出边距
                x = 50 + col * (alien_width + 10)
                y = 50 + row * (alien_height + 10)
                alien = Alien(x, y)
                self.aliens.add(alien)
                self.all_sprites.add(alien)
    
    def handle_events(self):
        """处理事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_SPACE and not self.game_over:
                    bullet = self.ship.shoot()
                    self.bullets.add(bullet)
                    self.all_sprites.add(bullet)
                elif event.key == pygame.K_p and self.game_over:
                    self.restart_game()
                elif event.key == pygame.K_q:
                    return False
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
        
        return True
    
    def update(self):
        """更新游戏状态"""
        if self.game_over:
            return
        
        # 更新所有精灵
        self.all_sprites.update()
        
        # 检查子弹与外星人碰撞
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        
        if collisions:
            self.score += len(collisions) * 10
        
        # 如果所有外星人被消灭，创建新的外星人群
        if not self.aliens:
            self.create_alien_fleet()
            # 提高外星人速度
            for alien in self.aliens:
                alien.speed += 0.5
        
        # 检查外星人是否到达边缘
        edge_hit = False
        for alien in self.aliens:
            if alien.rect.left <= 0 or alien.rect.right >= SCREEN_WIDTH:
                edge_hit = True
                break
        
        if edge_hit:
            for alien in self.aliens:
                alien.drop_down()
        
        # 检查外星人与飞船碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.game_over = True
        
        # 检查外星人是否到达底部
        for alien in self.aliens:
            if alien.rect.bottom >= SCREEN_HEIGHT - 50:
                self.game_over = True
                break
    
    def draw(self):
        """绘制游戏画面"""
        self.screen.fill(BLACK)
        
        # 绘制星星背景
        for i in range(50):
            x = (i * 37) % SCREEN_WIDTH
            y = (i * 23) % SCREEN_HEIGHT
            pygame.draw.circle(self.screen, WHITE, (x, y), 1)
        
        # 绘制所有精灵
        self.all_sprites.draw(self.screen)
        
        # 绘制得分
        score_text = self.font.render(f"得分: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # 绘制剩余外星人数量
        alien_count = len(self.aliens)
        alien_text = self.font.render(f"外星人: {alien_count}", True, WHITE)
        self.screen.blit(alien_text, (10, 50))
        
        if self.game_over:
            # 绘制游戏结束信息
            game_over_text = self.font.render("游戏结束!", True, RED)
            restart_text = self.font.render("按P键重新开始", True, WHITE)
            quit_text = self.font.render("按Q键退出", True, WHITE)
            
            # 计算文本位置（居中）
            go_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 30))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 10))
            quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50))
            
            self.screen.blit(game_over_text, go_rect)
            self.screen.blit(restart_text, restart_rect)
            self.screen.blit(quit_text, quit_rect)
        
        pygame.display.flip()
    
    def restart_game(self):
        """重新开始游戏"""
        self.game_over = False
        self.score = 0
        
        # 清空所有精灵组
        self.all_sprites.empty()
        self.bullets.empty()
        self.aliens.empty()
        
        # 重新创建飞船
        self.ship = Ship()
        self.all_sprites.add(self.ship)
        
        # 重新创建外星人群
        self.create_alien_fleet()
    
    def run(self):
        """运行游戏主循环"""
        print("=" * 50)
        print("简化版外星人入侵游戏")
        print("=" * 50)
        print("游戏说明：")
        print("- 左右箭头键：移动飞船")
        print("- 空格键：发射子弹")
        print("- P键：重新开始（游戏结束时）")
        print("- Q键：退出游戏")
        print("=" * 50)
        
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        print("感谢游玩！")


def main():
    """主函数"""
    try:
        game = Game()
        game.run()
    except pygame.error as e:
        print(f"Pygame错误: {e}")
        print("请确保已安装pygame: pip install pygame")
    except Exception as e:
        print(f"游戏错误: {e}")


if __name__ == '__main__':
    main() 