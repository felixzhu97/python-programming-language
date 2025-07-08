#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增强版外星人入侵游戏
第13章 - 添加音效、动画效果、粒子系统等高级功能

新增功能：
- 音效系统
- 爆炸动画
- 粒子效果
- 不同类型外星人
- Power-up道具
- 背景滚动
"""

import pygame
import sys
import random
import math


# 游戏设置
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SHIP_SPEED = 6
BULLET_SPEED = 8
ALIEN_SPEED = 1
FPS = 60

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)


class Particle(pygame.sprite.Sprite):
    """粒子效果类"""
    
    def __init__(self, x, y, color=WHITE, speed_range=(1, 5)):
        super().__init__()
        self.x = x
        self.y = y
        size = random.randint(1, 3)
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        
        # 随机速度和方向
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(*speed_range)
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed
        
        # 生命周期
        self.life = random.randint(20, 40)
        self.max_life = self.life
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.center = (int(self.x), int(self.y))
        
        # 渐变消失
        self.life -= 1
        alpha = int(255 * (self.life / self.max_life))
        self.image.set_alpha(max(0, alpha))
        
        if self.life <= 0:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    """爆炸动画类"""
    
    def __init__(self, x, y, size=30):
        super().__init__()
        self.images = []
        self.size = size
        
        # 创建爆炸动画帧
        for i in range(8):
            radius = int(size * (i + 1) / 8)
            surface = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
            colors = [RED, ORANGE, YELLOW, WHITE]
            color = colors[min(i // 2, len(colors) - 1)]
            pygame.draw.circle(surface, color, (size, size), radius)
            self.images.append(surface)
        
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(x, y))
        self.frame = 0
        self.frame_rate = 2  # 动画速度
        self.frame_count = 0
    
    def update(self):
        self.frame_count += 1
        if self.frame_count >= self.frame_rate:
            self.frame_count = 0
            self.frame += 1
            
            if self.frame >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frame]


class PowerUp(pygame.sprite.Sprite):
    """道具类"""
    
    def __init__(self, x, y, power_type='speed'):
        super().__init__()
        self.power_type = power_type
        
        # 根据类型设置外观
        colors = {
            'speed': CYAN,
            'multi_shot': YELLOW,
            'shield': GREEN,
            'score': PURPLE
        }
        
        self.image = pygame.Surface((20, 20))
        self.image.fill(colors.get(power_type, WHITE))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 2
        self.lifetime = 300  # 5秒生命周期
    
    def update(self):
        self.rect.y += self.speed
        self.lifetime -= 1
        
        # 闪烁效果
        if self.lifetime < 60:
            if (self.lifetime // 5) % 2:
                self.image.set_alpha(128)
            else:
                self.image.set_alpha(255)
        
        if self.lifetime <= 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()


class AlienType1(pygame.sprite.Sprite):
    """普通外星人"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = ALIEN_SPEED
        self.direction = 1
        self.points = 10
        self.hp = 1
    
    def update(self):
        self.rect.x += self.speed * self.direction
    
    def drop_down(self):
        self.rect.y += 40
        self.direction *= -1


class AlienType2(pygame.sprite.Sprite):
    """快速外星人"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((35, 25))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = ALIEN_SPEED * 1.5
        self.direction = 1
        self.points = 20
        self.hp = 1
    
    def update(self):
        self.rect.x += self.speed * self.direction
    
    def drop_down(self):
        self.rect.y += 40
        self.direction *= -1


class AlienType3(pygame.sprite.Sprite):
    """强化外星人"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((45, 35))
        self.image.fill(RED)
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = ALIEN_SPEED * 0.8
        self.direction = 1
        self.points = 50
        self.hp = 2
        self.max_hp = 2
    
    def update(self):
        self.rect.x += self.speed * self.direction
        
        # 根据血量改变颜色
        if self.hp < self.max_hp:
            self.image.fill((200, 100, 100))
    
    def drop_down(self):
        self.rect.y += 40
        self.direction *= -1
    
    def take_damage(self):
        self.hp -= 1
        return self.hp <= 0


class Ship(pygame.sprite.Sprite):
    """增强版飞船"""
    
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        self.speed = SHIP_SPEED
        self.moving_left = False
        self.moving_right = False
        
        # 道具效果
        self.speed_boost = 1.0
        self.multi_shot = False
        self.shield = False
        self.power_timers = {}
    
    def update(self):
        # 移动
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= int(self.speed * self.speed_boost)
        if self.moving_right and self.rect.right < SCREEN_WIDTH:
            self.rect.x += int(self.speed * self.speed_boost)
        
        # 更新道具计时器
        expired_powers = []
        for power, timer in self.power_timers.items():
            self.power_timers[power] = timer - 1
            if timer <= 0:
                expired_powers.append(power)
        
        # 移除过期道具效果
        for power in expired_powers:
            self.remove_power(power)
            del self.power_timers[power]
        
        # 护盾效果
        if self.shield:
            self.image.fill(CYAN)
        else:
            self.image.fill(BLUE)
    
    def add_power(self, power_type, duration=300):
        """添加道具效果"""
        self.power_timers[power_type] = duration
        
        if power_type == 'speed':
            self.speed_boost = 2.0
        elif power_type == 'multi_shot':
            self.multi_shot = True
        elif power_type == 'shield':
            self.shield = True
    
    def remove_power(self, power_type):
        """移除道具效果"""
        if power_type == 'speed':
            self.speed_boost = 1.0
        elif power_type == 'multi_shot':
            self.multi_shot = False
        elif power_type == 'shield':
            self.shield = False
    
    def shoot(self):
        """发射子弹"""
        bullets = []
        if self.multi_shot:
            # 三发子弹
            bullets.append(Bullet(self.rect.centerx, self.rect.top))
            bullets.append(Bullet(self.rect.centerx - 20, self.rect.top))
            bullets.append(Bullet(self.rect.centerx + 20, self.rect.top))
        else:
            # 单发子弹
            bullets.append(Bullet(self.rect.centerx, self.rect.top))
        
        return bullets


class Bullet(pygame.sprite.Sprite):
    """子弹类"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 12))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = BULLET_SPEED
    
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()


class Star(pygame.sprite.Sprite):
    """背景星星"""
    
    def __init__(self):
        super().__init__()
        size = random.randint(1, 2)
        self.image = pygame.Surface((size, size))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = random.randint(-SCREEN_HEIGHT, 0)
        self.speed = random.uniform(1, 3)
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = random.randint(-50, 0)
            self.rect.x = random.randint(0, SCREEN_WIDTH)


class SoundManager:
    """音效管理器"""
    
    def __init__(self):
        self.sounds = {}
        self.enabled = True
        
        try:
            pygame.mixer.init()
            # 这里可以加载实际的音效文件
            # self.sounds['shoot'] = pygame.mixer.Sound('sounds/shoot.wav')
            # self.sounds['explosion'] = pygame.mixer.Sound('sounds/explosion.wav')
        except pygame.error:
            self.enabled = False
    
    def play(self, sound_name):
        """播放音效"""
        if self.enabled and sound_name in self.sounds:
            self.sounds[sound_name].play()


class EnhancedGame:
    """增强版游戏主类"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("增强版外星人入侵")
        self.clock = pygame.time.Clock()
        
        # 音效管理器
        self.sound_manager = SoundManager()
        
        # 精灵组
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.particles = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        
        # 创建飞船
        self.ship = Ship()
        self.all_sprites.add(self.ship)
        
        # 创建背景星星
        for _ in range(100):
            star = Star()
            self.stars.add(star)
            self.all_sprites.add(star)
        
        # 游戏状态
        self.score = 0
        self.level = 1
        self.lives = 3
        self.game_over = False
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # 创建外星人群
        self.create_alien_fleet()
        
        # 道具生成计时器
        self.powerup_timer = 0
    
    def create_alien_fleet(self):
        """创建多样化的外星人群"""
        alien_types = [AlienType1, AlienType2, AlienType3]
        alien_width = 50
        alien_height = 40
        
        # 计算每行外星人数量
        aliens_per_row = SCREEN_WIDTH // (alien_width + 15)
        
        # 创建多行外星人，混合不同类型
        for row in range(5):
            for col in range(aliens_per_row - 2):
                x = 75 + col * (alien_width + 15)
                y = 75 + row * (alien_height + 15)
                
                # 根据行决定外星人类型
                if row < 2:
                    alien_class = AlienType1
                elif row < 4:
                    alien_class = AlienType2
                else:
                    alien_class = AlienType3
                
                alien = alien_class(x, y)
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
                    bullets = self.ship.shoot()
                    for bullet in bullets:
                        self.bullets.add(bullet)
                        self.all_sprites.add(bullet)
                    self.sound_manager.play('shoot')
                elif event.key == pygame.K_r and self.game_over:
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
        for bullet in self.bullets:
            hit_aliens = pygame.sprite.spritecollide(bullet, self.aliens, False)
            for alien in hit_aliens:
                bullet.kill()
                
                # 处理不同类型外星人的伤害
                if hasattr(alien, 'take_damage'):
                    if alien.take_damage():
                        self.handle_alien_death(alien)
                else:
                    self.handle_alien_death(alien)
        
        # 检查外星人边缘碰撞
        edge_hit = False
        for alien in self.aliens:
            if alien.rect.left <= 0 or alien.rect.right >= SCREEN_WIDTH:
                edge_hit = True
                break
        
        if edge_hit:
            for alien in self.aliens:
                alien.drop_down()
        
        # 检查外星人与飞船碰撞
        if not self.ship.shield:
            hit_ship = pygame.sprite.spritecollide(self.ship, self.aliens, False)
            if hit_ship:
                self.handle_ship_hit()
        
        # 检查外星人到达底部
        for alien in self.aliens:
            if alien.rect.bottom >= SCREEN_HEIGHT - 50:
                self.handle_ship_hit()
                break
        
        # 检查道具与飞船碰撞
        hit_powerups = pygame.sprite.spritecollide(self.ship, self.powerups, True)
        for powerup in hit_powerups:
            self.handle_powerup(powerup)
        
        # 生成道具
        self.powerup_timer += 1
        if self.powerup_timer > 600:  # 10秒
            self.powerup_timer = 0
            if random.random() < 0.3:  # 30%几率
                self.spawn_powerup()
        
        # 检查关卡完成
        if not self.aliens:
            self.next_level()
    
    def handle_alien_death(self, alien):
        """处理外星人死亡"""
        # 添加分数
        self.score += alien.points
        
        # 创建爆炸效果
        explosion = Explosion(alien.rect.centerx, alien.rect.centery)
        self.explosions.add(explosion)
        self.all_sprites.add(explosion)
        
        # 创建粒子效果
        for _ in range(10):
            particle = Particle(alien.rect.centerx, alien.rect.centery, 
                              color=random.choice([RED, ORANGE, YELLOW]))
            self.particles.add(particle)
            self.all_sprites.add(particle)
        
        alien.kill()
        self.sound_manager.play('explosion')
    
    def handle_ship_hit(self):
        """处理飞船被击中"""
        self.lives -= 1
        
        # 创建爆炸效果
        explosion = Explosion(self.ship.rect.centerx, self.ship.rect.centery, size=50)
        self.explosions.add(explosion)
        self.all_sprites.add(explosion)
        
        if self.lives <= 0:
            self.game_over = True
        else:
            # 重置飞船位置
            self.ship.rect.centerx = SCREEN_WIDTH // 2
            self.ship.rect.bottom = SCREEN_HEIGHT - 20
    
    def handle_powerup(self, powerup):
        """处理道具收集"""
        if powerup.power_type == 'score':
            self.score += 100
        else:
            self.ship.add_power(powerup.power_type)
    
    def spawn_powerup(self):
        """生成道具"""
        power_types = ['speed', 'multi_shot', 'shield', 'score']
        power_type = random.choice(power_types)
        x = random.randint(50, SCREEN_WIDTH - 50)
        powerup = PowerUp(x, 0, power_type)
        self.powerups.add(powerup)
        self.all_sprites.add(powerup)
    
    def next_level(self):
        """下一关"""
        self.level += 1
        
        # 清空子弹
        self.bullets.empty()
        
        # 创建新的外星人群
        self.create_alien_fleet()
        
        # 提高难度
        global ALIEN_SPEED
        ALIEN_SPEED *= 1.1
    
    def restart_game(self):
        """重新开始游戏"""
        self.game_over = False
        self.score = 0
        self.level = 1
        self.lives = 3
        
        # 重置速度
        global ALIEN_SPEED
        ALIEN_SPEED = 1
        
        # 清空所有精灵组
        self.all_sprites.empty()
        self.bullets.empty()
        self.aliens.empty()
        self.explosions.empty()
        self.particles.empty()
        self.powerups.empty()
        
        # 重新创建游戏对象
        self.ship = Ship()
        self.all_sprites.add(self.ship)
        
        # 重新创建背景
        for _ in range(100):
            star = Star()
            self.stars.add(star)
            self.all_sprites.add(star)
        
        self.create_alien_fleet()
    
    def draw(self):
        """绘制游戏画面"""
        self.screen.fill(BLACK)
        
        # 绘制所有精灵
        self.all_sprites.draw(self.screen)
        
        # 绘制UI信息
        score_text = self.font.render(f"得分: {self.score}", True, WHITE)
        level_text = self.font.render(f"关卡: {self.level}", True, WHITE)
        lives_text = self.font.render(f"生命: {self.lives}", True, WHITE)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 50))
        self.screen.blit(lives_text, (10, 90))
        
        # 显示道具状态
        y_offset = 130
        for power, timer in self.ship.power_timers.items():
            power_text = self.small_font.render(f"{power}: {timer//60}s", True, CYAN)
            self.screen.blit(power_text, (10, y_offset))
            y_offset += 25
        
        # 游戏结束界面
        if self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            game_over_text = self.font.render("游戏结束!", True, RED)
            score_final = self.font.render(f"最终得分: {self.score}", True, WHITE)
            restart_text = self.font.render("按R键重新开始", True, WHITE)
            quit_text = self.font.render("按Q键退出", True, WHITE)
            
            # 居中显示
            texts = [game_over_text, score_final, restart_text, quit_text]
            total_height = len(texts) * 40
            start_y = (SCREEN_HEIGHT - total_height) // 2
            
            for i, text in enumerate(texts):
                rect = text.get_rect(center=(SCREEN_WIDTH//2, start_y + i * 40))
                self.screen.blit(text, rect)
        
        pygame.display.flip()
    
    def run(self):
        """运行游戏主循环"""
        print("=" * 60)
        print("增强版外星人入侵游戏")
        print("=" * 60)
        print("新功能：")
        print("- 三种不同类型的外星人")
        print("- 爆炸动画和粒子效果")
        print("- 四种道具：速度提升、多重射击、护盾、额外分数")
        print("- 滚动星空背景")
        print("- 关卡系统和难度递增")
        print("\n控制说明：")
        print("- 左右箭头键：移动飞船")
        print("- 空格键：发射子弹")
        print("- R键：重新开始（游戏结束时）")
        print("- Q键：退出游戏")
        print("=" * 60)
        
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        print("感谢游玩增强版游戏！")


def main():
    """主函数"""
    try:
        game = EnhancedGame()
        game.run()
    except pygame.error as e:
        print(f"Pygame错误: {e}")
        print("请确保已安装pygame: pip install pygame")
    except Exception as e:
        print(f"游戏错误: {e}")


if __name__ == '__main__':
    main() 