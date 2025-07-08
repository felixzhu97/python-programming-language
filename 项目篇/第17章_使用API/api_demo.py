#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第17章 - 使用API
演示如何使用各种API获取数据并可视化

主要功能：
1. REST API调用
2. 数据解析和处理
3. API认证
4. 错误处理
5. 数据可视化
"""

import requests
import json
import time
import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False


class APIDemo:
    """API演示类"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Python API Demo 1.0'
        })
    
    def github_api_demo(self):
        """GitHub API演示"""
        print("=" * 50)
        print("1. GitHub API演示")
        print("=" * 50)
        
        try:
            # 获取用户信息
            username = 'octocat'  # GitHub示例用户
            url = f'https://api.github.com/users/{username}'
            
            print(f"正在获取用户 {username} 的信息...")
            response = self.session.get(url)
            
            if response.status_code == 200:
                user_data = response.json()
                
                print(f"用户名: {user_data.get('name', 'N/A')}")
                print(f"GitHub用户名: {user_data.get('login', 'N/A')}")
                print(f"粉丝数: {user_data.get('followers', 0)}")
                print(f"关注数: {user_data.get('following', 0)}")
                print(f"公开仓库数: {user_data.get('public_repos', 0)}")
                print(f"创建时间: {user_data.get('created_at', 'N/A')}")
                
                # 获取仓库信息
                repos_url = f'https://api.github.com/users/{username}/repos'
                repos_response = self.session.get(repos_url)
                
                if repos_response.status_code == 200:
                    repos = repos_response.json()
                    
                    # 分析仓库数据
                    languages = {}
                    stars_total = 0
                    
                    for repo in repos[:10]:  # 只分析前10个仓库
                        language = repo.get('language', 'Unknown')
                        if language:
                            languages[language] = languages.get(language, 0) + 1
                        stars_total += repo.get('stargazers_count', 0)
                    
                    print(f"\n仓库语言分布:")
                    for lang, count in sorted(languages.items(), key=lambda x: x[1], reverse=True):
                        print(f"  {lang}: {count} 个仓库")
                    
                    # 可视化
                    if languages:
                        plt.figure(figsize=(10, 6))
                        
                        plt.subplot(1, 2, 1)
                        plt.pie(languages.values(), labels=languages.keys(), autopct='%1.1f%%')
                        plt.title(f'{username} 的编程语言分布')
                        
                        plt.subplot(1, 2, 2)
                        repo_names = [repo['name'][:15] for repo in repos[:5]]
                        repo_stars = [repo['stargazers_count'] for repo in repos[:5]]
                        
                        plt.bar(repo_names, repo_stars)
                        plt.title('热门仓库 Star 数')
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        plt.show()
                        
            else:
                print(f"API请求失败: {response.status_code}")
                
        except Exception as e:
            print(f"GitHub API演示出错: {e}")
    
    def weather_api_demo(self):
        """天气API演示（模拟数据）"""
        print("=" * 50)
        print("2. 天气API演示")
        print("=" * 50)
        
        # 模拟天气API响应
        mock_weather_data = {
            "city": "北京",
            "temperature": 15,
            "humidity": 65,
            "pressure": 1013,
            "wind_speed": 12,
            "description": "晴朗",
            "forecast": [
                {"day": "今天", "high": 18, "low": 8, "condition": "晴朗"},
                {"day": "明天", "high": 20, "low": 10, "condition": "多云"},
                {"day": "后天", "high": 16, "low": 6, "condition": "小雨"},
                {"day": "第4天", "high": 14, "low": 4, "condition": "阴天"},
                {"day": "第5天", "high": 19, "low": 9, "condition": "晴朗"}
            ]
        }
        
        print(f"城市: {mock_weather_data['city']}")
        print(f"当前温度: {mock_weather_data['temperature']}°C")
        print(f"湿度: {mock_weather_data['humidity']}%")
        print(f"气压: {mock_weather_data['pressure']} hPa")
        print(f"风速: {mock_weather_data['wind_speed']} km/h")
        print(f"天气: {mock_weather_data['description']}")
        
        # 可视化天气预报
        forecast = mock_weather_data['forecast']
        days = [f['day'] for f in forecast]
        highs = [f['high'] for f in forecast]
        lows = [f['low'] for f in forecast]
        
        plt.figure(figsize=(12, 6))
        
        x = range(len(days))
        plt.plot(x, highs, 'ro-', label='最高温度', linewidth=2, markersize=8)
        plt.plot(x, lows, 'bo-', label='最低温度', linewidth=2, markersize=8)
        
        plt.fill_between(x, highs, lows, alpha=0.3, color='gray')
        
        plt.xlabel('日期')
        plt.ylabel('温度 (°C)')
        plt.title(f'{mock_weather_data["city"]} 5天天气预报')
        plt.xticks(x, days)
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # 添加温度标签
        for i, (high, low) in enumerate(zip(highs, lows)):
            plt.annotate(f'{high}°', (i, high), textcoords="offset points", 
                        xytext=(0,10), ha='center')
            plt.annotate(f'{low}°', (i, low), textcoords="offset points", 
                        xytext=(0,-15), ha='center')
        
        plt.tight_layout()
        plt.show()
    
    def json_placeholder_demo(self):
        """JSONPlaceholder API演示"""
        print("=" * 50)
        print("3. JSONPlaceholder API演示")
        print("=" * 50)
        
        try:
            # 获取用户列表
            print("获取用户数据...")
            users_response = self.session.get('https://jsonplaceholder.typicode.com/users')
            
            if users_response.status_code == 200:
                users = users_response.json()
                print(f"获取到 {len(users)} 个用户")
                
                # 获取帖子数据
                print("获取帖子数据...")
                posts_response = self.session.get('https://jsonplaceholder.typicode.com/posts')
                
                if posts_response.status_code == 200:
                    posts = posts_response.json()
                    print(f"获取到 {len(posts)} 篇帖子")
                    
                    # 分析数据
                    user_posts = {}
                    for post in posts:
                        user_id = post['userId']
                        user_posts[user_id] = user_posts.get(user_id, 0) + 1
                    
                    # 获取用户名映射
                    user_names = {user['id']: user['name'] for user in users}
                    
                    # 可视化用户发帖数量
                    user_ids = list(user_posts.keys())
                    post_counts = list(user_posts.values())
                    names = [user_names.get(uid, f'User {uid}') for uid in user_ids]
                    
                    plt.figure(figsize=(15, 8))
                    
                    plt.subplot(2, 1, 1)
                    bars = plt.bar(range(len(names)), post_counts)
                    plt.title('用户发帖数量统计')
                    plt.xlabel('用户')
                    plt.ylabel('帖子数量')
                    plt.xticks(range(len(names)), [name[:15] for name in names], rotation=45)
                    
                    # 添加数值标签
                    for bar, count in zip(bars, post_counts):
                        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                                str(count), ha='center', va='bottom')
                    
                    # 帖子标题长度分布
                    title_lengths = [len(post['title']) for post in posts]
                    
                    plt.subplot(2, 1, 2)
                    plt.hist(title_lengths, bins=20, alpha=0.7, color='skyblue')
                    plt.title('帖子标题长度分布')
                    plt.xlabel('标题长度（字符数）')
                    plt.ylabel('频次')
                    
                    plt.tight_layout()
                    plt.show()
                    
                    print(f"平均帖子标题长度: {sum(title_lengths)/len(title_lengths):.1f} 字符")
                    print(f"最活跃用户: {user_names[max(user_posts, key=user_posts.get)]}")
                    
        except Exception as e:
            print(f"JSONPlaceholder API演示出错: {e}")
    
    def rate_limiting_demo(self):
        """API限流演示"""
        print("=" * 50)
        print("4. API限流和错误处理演示")
        print("=" * 50)
        
        # 模拟API限流
        api_calls = []
        max_calls_per_minute = 5
        
        def make_api_call(call_id):
            """模拟API调用"""
            current_time = time.time()
            
            # 检查限流
            recent_calls = [t for t in api_calls if current_time - t < 60]
            
            if len(recent_calls) >= max_calls_per_minute:
                print(f"API调用 {call_id}: 限流中，请稍后重试")
                return False
            
            # 模拟API响应时间
            time.sleep(0.5)
            api_calls.append(current_time)
            
            # 模拟随机错误
            import random
            if random.random() < 0.2:  # 20%错误率
                print(f"API调用 {call_id}: 服务器错误 (500)")
                return False
            
            print(f"API调用 {call_id}: 成功")
            return True
        
        # 演示API调用
        successful_calls = 0
        failed_calls = 0
        
        for i in range(10):
            print(f"\n尝试API调用 {i+1}...")
            if make_api_call(i+1):
                successful_calls += 1
            else:
                failed_calls += 1
        
        # 统计结果
        print(f"\n调用统计:")
        print(f"成功: {successful_calls}")
        print(f"失败: {failed_calls}")
        print(f"成功率: {successful_calls/(successful_calls+failed_calls)*100:.1f}%")
        
        # 可视化调用结果
        labels = ['成功', '失败']
        sizes = [successful_calls, failed_calls]
        colors = ['green', 'red']
        
        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.title('API调用结果统计')
        plt.axis('equal')
        plt.show()
    
    def data_aggregation_demo(self):
        """数据聚合演示"""
        print("=" * 50)
        print("5. 多API数据聚合演示")
        print("=" * 50)
        
        # 模拟从多个API获取数据
        social_media_data = {
            "twitter": {"followers": 1500, "posts": 320, "engagement": 4.2},
            "instagram": {"followers": 2800, "posts": 180, "engagement": 6.8},
            "facebook": {"followers": 1200, "posts": 95, "engagement": 3.1},
            "youtube": {"followers": 850, "posts": 25, "engagement": 12.5}
        }
        
        e_commerce_data = {
            "sales": [12000, 15000, 11000, 18000, 16000],
            "orders": [120, 150, 110, 180, 160],
            "customers": [800, 920, 750, 1100, 980]
        }
        
        print("社交媒体数据:")
        for platform, data in social_media_data.items():
            print(f"{platform}: {data['followers']} 粉丝, {data['posts']} 帖子, {data['engagement']}% 互动率")
        
        # 可视化聚合数据
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        
        # 社交媒体粉丝数
        platforms = list(social_media_data.keys())
        followers = [data['followers'] for data in social_media_data.values()]
        
        bars1 = ax1.bar(platforms, followers, color=['skyblue', 'pink', 'lightgreen', 'orange'])
        ax1.set_title('各平台粉丝数量')
        ax1.set_ylabel('粉丝数')
        
        # 添加数值标签
        for bar, count in zip(bars1, followers):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50,
                    str(count), ha='center', va='bottom')
        
        # 互动率对比
        engagement = [data['engagement'] for data in social_media_data.values()]
        ax2.plot(platforms, engagement, 'ro-', linewidth=2, markersize=8)
        ax2.set_title('各平台互动率')
        ax2.set_ylabel('互动率 (%)')
        ax2.grid(True, alpha=0.3)
        
        # 电商销售趋势
        days = ['周一', '周二', '周三', '周四', '周五']
        ax3.plot(days, e_commerce_data['sales'], 'b-', label='销售额', linewidth=2)
        ax3_twin = ax3.twinx()
        ax3_twin.plot(days, e_commerce_data['orders'], 'r--', label='订单数', linewidth=2)
        
        ax3.set_title('电商数据趋势')
        ax3.set_ylabel('销售额', color='blue')
        ax3_twin.set_ylabel('订单数', color='red')
        ax3.legend(loc='upper left')
        ax3_twin.legend(loc='upper right')
        
        # 综合仪表板
        total_followers = sum(followers)
        total_posts = sum(data['posts'] for data in social_media_data.values())
        avg_engagement = sum(engagement) / len(engagement)
        total_sales = sum(e_commerce_data['sales'])
        
        metrics = ['总粉丝数', '总帖子数', '平均互动率', '总销售额']
        values = [total_followers/1000, total_posts, avg_engagement, total_sales/1000]
        
        ax4.bar(metrics, values, color=['purple', 'brown', 'navy', 'darkgreen'])
        ax4.set_title('综合指标概览')
        ax4.set_ylabel('数值')
        
        plt.tight_layout()
        plt.show()
        
        print(f"\n综合分析结果:")
        print(f"社交媒体总粉丝: {total_followers:,}")
        print(f"平均互动率: {avg_engagement:.1f}%")
        print(f"本周总销售额: ¥{total_sales:,}")


def main():
    """主函数"""
    print("=" * 60)
    print("第17章 - 使用API演示")
    print("=" * 60)
    
    api_demo = APIDemo()
    
    demos = [
        ("GitHub API演示", api_demo.github_api_demo),
        ("天气API演示", api_demo.weather_api_demo),
        ("JSONPlaceholder API", api_demo.json_placeholder_demo),
        ("API限流处理", api_demo.rate_limiting_demo),
        ("多API数据聚合", api_demo.data_aggregation_demo)
    ]
    
    while True:
        print("\n可用的演示:")
        for i, (name, _) in enumerate(demos, 1):
            print(f"{i}. {name}")
        print("0. 退出")
        
        try:
            choice = input("\n请选择要运行的演示 (0-5): ").strip()
            
            if choice == '0':
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(demos):
                print(f"\n正在运行: {demos[int(choice)-1][0]}")
                
                try:
                    demos[int(choice)-1][1]()
                except Exception as e:
                    print(f"运行演示时出错: {e}")
                
                input("\n按回车键继续...")
            else:
                print("无效选择，请重试")
                
        except KeyboardInterrupt:
            print("\n\n演示已中断")
            break
        except Exception as e:
            print(f"输入错误: {e}")
    
    print("\n感谢使用API演示！")


if __name__ == '__main__':
    main() 