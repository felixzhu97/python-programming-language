#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第13章 - 游戏增强功能演示
演示如何为游戏添加高级功能

新增功能：
1. 音效系统
2. 动画效果
3. 粒子系统
4. 道具系统
5. 多种敌人类型
"""

import pygame
import random
import math


class ParticleSystem:
    """粒子系统"""
    
    def __init__(self):
        self.particles = []
    
    def add_explosion(self, x, y, count=10):
        """添加爆炸粒子"""
        for _ in range(count):
            particle = {
                'x': x,
                'y': y,
                'dx': random.uniform(-5, 5),
                'dy': random.uniform(-5, 5),
                'life': 30,
                'color': random.choice([(255, 0, 0), (255, 165, 0), (255, 255, 0)])
            }
            self.particles.append(particle)
    
    def update(self):
        """更新粒子"""
        for particle in self.particles[:]:
            particle['x'] += particle['dx']
            particle['y'] += particle['dy']
            particle['life'] -= 1
            
            if particle['life'] <= 0:
                self.particles.remove(particle)
    
    def draw(self, screen):
        """绘制粒子"""
        for particle in self.particles:
            alpha = int(255 * (particle['life'] / 30))
            color = (*particle['color'], alpha)
            pygame.draw.circle(screen, particle['color'][:3], 
                             (int(particle['x']), int(particle['y'])), 3)


class SoundManager:
    """音效管理器"""
    
    def __init__(self):
        self.sounds = {}
        self.enabled = True
        
        try:
            pygame.mixer.init()
            print("音效系统初始化成功")
        except pygame.error:
            self.enabled = False
            print("音效系统初始化失败")
    
    def create_sound_effect(self, freq, duration=0.1):
        """创建简单的音效"""
        if not self.enabled:
            return None
        
        try:
            sample_rate = 22050
            frames = int(duration * sample_rate)
            arr = []
            for i in range(frames):
                wave = 4096 * math.sin(2 * math.pi * freq * i / sample_rate)
                arr.append([wave, wave])
            sound = pygame.sndarray.make_sound(pygame.array.array('f', arr))
            return sound
        except:
            return None
    
    def load_sounds(self):
        """加载或创建音效"""
        self.sounds['shoot'] = self.create_sound_effect(800, 0.1)
        self.sounds['explosion'] = self.create_sound_effect(200, 0.3)
        self.sounds['powerup'] = self.create_sound_effect(1200, 0.2)
    
    def play(self, sound_name):
        """播放音效"""
        if self.enabled and sound_name in self.sounds and self.sounds[sound_name]:
            self.sounds[sound_name].play()


class PowerUp:
    """道具类"""
    
    def __init__(self, x, y, power_type):
        self.x = x
        self.y = y
        self.power_type = power_type
        self.speed = 2
        self.size = 15
        self.lifetime = 300
        
        # 道具颜色
        self.colors = {
            'speed': (0, 255, 255),      # 青色 - 速度提升
            'multi_shot': (255, 255, 0), # 黄色 - 多重射击
            'shield': (0, 255, 0),       # 绿色 - 护盾
            'score': (255, 0, 255)       # 紫色 - 分数加成
        }
    
    def update(self):
        """更新道具位置"""
        self.y += self.speed
        self.lifetime -= 1
        
        # 闪烁效果
        return self.lifetime > 0 and self.y < 600
    
    def draw(self, screen):
        """绘制道具"""
        color = self.colors.get(self.power_type, (255, 255, 255))
        
        # 闪烁效果
        if self.lifetime < 60 and (self.lifetime // 5) % 2:
            return
        
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.size)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.size, 2)


class AnimatedSprite:
    """动画精灵类"""
    
    def __init__(self, x, y, animation_frames=8):
        self.x = x
        self.y = y
        self.frame = 0
        self.max_frames = animation_frames
        self.frame_rate = 3
        self.frame_count = 0
        self.active = True
    
    def update(self):
        """更新动画"""
        self.frame_count += 1
        if self.frame_count >= self.frame_rate:
            self.frame_count = 0
            self.frame += 1
            if self.frame >= self.max_frames:
                self.active = False
    
    def draw(self, screen):
        """绘制动画"""
        if not self.active:
            return
        
        # 绘制爆炸动画
        radius = int(20 * (self.frame + 1) / self.max_frames)
        colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (255, 255, 255)]
        color_index = min(self.frame // 2, len(colors) - 1)
        color = colors[color_index]
        
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), radius)


class EnhancementDemo:
    """游戏增强功能演示"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("游戏增强功能演示")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        
        # 初始化系统
        self.particle_system = ParticleSystem()
        self.sound_manager = SoundManager()
        self.sound_manager.load_sounds()
        
        # 游戏对象列表
        self.powerups = []
        self.animations = []
        
        # 演示状态
        self.demo_timer = 0
        self.score = 0
        
    def handle_events(self):
        """处理事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.create_explosion_demo()
                elif event.key == pygame.K_p:
                    self.create_powerup_demo()
                elif event.key == pygame.K_s:
                    self.sound_manager.play('shoot')
                elif event.key == pygame.K_e:
                    self.sound_manager.play('explosion')
                elif event.key == pygame.K_u:
                    self.sound_manager.play('powerup')
                elif event.key == pygame.K_q:
                    return False
        return True
    
    def create_explosion_demo(self):
        """创建爆炸演示"""
        x, y = pygame.mouse.get_pos()
        
        # 添加粒子效果
        self.particle_system.add_explosion(x, y, 15)
        
        # 添加动画效果
        animation = AnimatedSprite(x, y)
        self.animations.append(animation)
        
        # 播放音效
        self.sound_manager.play('explosion')
        
        self.score += 10
    
    def create_powerup_demo(self):
        """创建道具演示"""
        power_types = ['speed', 'multi_shot', 'shield', 'score']
        power_type = random.choice(power_types)
        x = random.randint(50, 750)
        
        powerup = PowerUp(x, 0, power_type)
        self.powerups.append(powerup)
        
        self.sound_manager.play('powerup')
    
    def update(self):
        """更新游戏状态"""
        # 更新粒子系统
        self.particle_system.update()
        
        # 更新动画
        self.animations = [anim for anim in self.animations if anim.active]
        for animation in self.animations:
            animation.update()
        
        # 更新道具
        self.powerups = [powerup for powerup in self.powerups if powerup.update()]
        
        # 自动生成演示内容
        self.demo_timer += 1
        if self.demo_timer % 120 == 0:  # 每2秒
            self.create_powerup_demo()
        
        if self.demo_timer % 180 == 0:  # 每3秒
            x = random.randint(100, 700)
            y = random.randint(100, 500)
            self.particle_system.add_explosion(x, y, 8)
    
    def draw(self):
        """绘制游戏画面"""
        # 渐变背景
        for y in range(600):
            color_value = int(20 * (1 - y / 600))
            color = (color_value, color_value, color_value + 20)
            pygame.draw.line(self.screen, color, (0, y), (800, y))
        
        # 绘制粒子系统
        self.particle_system.draw(self.screen)
        
        # 绘制动画
        for animation in self.animations:
            animation.draw(self.screen)
        
        # 绘制道具
        for powerup in self.powerups:
            powerup.draw(self.screen)
        
        # 绘制UI
        title = self.font.render("游戏增强功能演示", True, (255, 255, 255))
        score_text = self.font.render(f"得分: {self.score}", True, (255, 255, 255))
        
        instructions = [
            "空格键 - 创建爆炸效果",
            "P键 - 生成道具",
            "S键 - 射击音效",
            "E键 - 爆炸音效", 
            "U键 - 道具音效",
            "Q键 - 退出"
        ]
        
        self.screen.blit(title, (250, 20))
        self.screen.blit(score_text, (20, 60))
        
        small_font = pygame.font.Font(None, 24)
        for i, instruction in enumerate(instructions):
            text = small_font.render(instruction, True, (200, 200, 200))
            self.screen.blit(text, (20, 100 + i * 25))
        
        pygame.display.flip()
    
    def run(self):
        """运行演示"""
        print("=" * 50)
        print("第13章 - 游戏增强功能演示")
        print("=" * 50)
        print("演示内容：")
        print("1. 粒子爆炸效果")
        print("2. 动画系统")
        print("3. 音效系统")
        print("4. 道具系统")
        print("5. 视觉特效")
        print("\n操作说明已显示在游戏窗口中")
        print("=" * 50)
        
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()
        print("演示结束！")


def main():
    """主函数"""
    try:
        demo = EnhancementDemo()
        demo.run()
    except pygame.error as e:
        print(f"Pygame错误: {e}")
        print("请确保已安装pygame: pip install pygame")
    except Exception as e:
        print(f"演示错误: {e}")


if __name__ == '__main__':
    main() 