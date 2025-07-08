#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第16章 - 下载数据
演示如何下载、处理和可视化各种数据源

主要功能：
1. CSV文件处理
2. JSON数据处理  
3. 网络数据获取
4. 数据清洗和分析
"""

import csv
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


class DataDownloader:
    """数据下载器类"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def download_csv_data(self):
        """下载CSV数据演示"""
        print("=" * 50)
        print("1. CSV数据处理演示")
        print("=" * 50)
        
        # 创建模拟CSV数据
        sample_data = {
            'date': [datetime.now() - timedelta(days=i) for i in range(30, 0, -1)],
            'temperature': [20 + 10 * np.sin(i * 0.2) + np.random.normal(0, 2) for i in range(30)],
            'humidity': [50 + 20 * np.cos(i * 0.15) + np.random.normal(0, 5) for i in range(30)],
            'pressure': [1013 + np.random.normal(0, 10) for _ in range(30)]
        }
        
        # 保存为CSV
        with open('weather_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['日期', '温度', '湿度', '气压'])
            for i in range(len(sample_data['date'])):
                writer.writerow([
                    sample_data['date'][i].strftime('%Y-%m-%d'),
                    f"{sample_data['temperature'][i]:.1f}",
                    f"{sample_data['humidity'][i]:.1f}",
                    f"{sample_data['pressure'][i]:.1f}"
                ])
        
        # 读取并分析CSV数据
        dates, temps, humidity, pressure = [], [], [], []
        with open('weather_data.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dates.append(datetime.strptime(row['日期'], '%Y-%m-%d'))
                temps.append(float(row['温度']))
                humidity.append(float(row['湿度']))
                pressure.append(float(row['气压']))
        
        # 可视化
        fig, axes = plt.subplots(3, 1, figsize=(12, 10))
        
        axes[0].plot(dates, temps, 'b-', marker='o', linewidth=2)
        axes[0].set_title('温度趋势')
        axes[0].set_ylabel('温度 (°C)')
        axes[0].grid(True, alpha=0.3)
        
        axes[1].plot(dates, humidity, 'g-', marker='s', linewidth=2)
        axes[1].set_title('湿度趋势')
        axes[1].set_ylabel('湿度 (%)')
        axes[1].grid(True, alpha=0.3)
        
        axes[2].plot(dates, pressure, 'r-', marker='^', linewidth=2)
        axes[2].set_title('气压趋势')
        axes[2].set_ylabel('气压 (hPa)')
        axes[2].set_xlabel('日期')
        axes[2].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        print(f"已处理 {len(dates)} 条天气记录")
        print(f"平均温度: {np.mean(temps):.1f}°C")
        print(f"平均湿度: {np.mean(humidity):.1f}%")
        print(f"平均气压: {np.mean(pressure):.1f}hPa")
    
    def process_json_data(self):
        """JSON数据处理演示"""
        print("=" * 50)
        print("2. JSON数据处理演示")
        print("=" * 50)
        
        # 创建模拟JSON数据
        sample_json = {
            "用户统计": {
                "总用户数": 10000,
                "活跃用户": 7500,
                "新用户": 500
            },
            "地区分布": [
                {"地区": "北京", "用户数": 2000, "增长率": 15.5},
                {"地区": "上海", "用户数": 1800, "增长率": 12.3},
                {"地区": "广州", "用户数": 1500, "增长率": 18.7},
                {"地区": "深圳", "用户数": 1400, "增长率": 22.1},
                {"地区": "其他", "用户数": 3300, "增长率": 8.9}
            ],
            "每日活跃": [
                {"日期": "2024-01-01", "活跃数": 6800},
                {"日期": "2024-01-02", "活跃数": 7200},
                {"日期": "2024-01-03", "活跃数": 7500},
                {"日期": "2024-01-04", "活跃数": 7100},
                {"日期": "2024-01-05", "活跃数": 7800}
            ]
        }
        
        # 保存JSON文件
        with open('user_data.json', 'w', encoding='utf-8') as file:
            json.dump(sample_json, file, ensure_ascii=False, indent=2)
        
        # 读取并分析JSON数据
        with open('user_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # 可视化地区分布
        regions = [item['地区'] for item in data['地区分布']]
        users = [item['用户数'] for item in data['地区分布']]
        growth = [item['增长率'] for item in data['地区分布']]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # 用户数饼图
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
        wedges, texts, autotexts = ax1.pie(users, labels=regions, colors=colors, 
                                          autopct='%1.1f%%', startangle=90)
        ax1.set_title('用户地区分布')
        
        # 增长率柱状图
        bars = ax2.bar(regions, growth, color=colors)
        ax2.set_title('各地区增长率')
        ax2.set_ylabel('增长率 (%)')
        ax2.tick_params(axis='x', rotation=45)
        
        # 添加数值标签
        for bar, rate in zip(bars, growth):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                    f'{rate}%', ha='center', va='bottom')
        
        plt.tight_layout()
        plt.show()
        
        print("JSON数据分析结果:")
        print(f"总用户数: {data['用户统计']['总用户数']:,}")
        print(f"活跃用户: {data['用户统计']['活跃用户']:,}")
        print(f"最高增长率地区: {max(data['地区分布'], key=lambda x: x['增长率'])['地区']}")
    
    def fetch_api_data(self):
        """API数据获取演示"""
        print("=" * 50)
        print("3. API数据获取演示")
        print("=" * 50)
        
        # 模拟API响应数据
        mock_api_data = {
            "status": "success",
            "data": {
                "stocks": [
                    {"symbol": "AAPL", "price": 150.25, "change": 2.15},
                    {"symbol": "GOOGL", "price": 2800.50, "change": -15.30},
                    {"symbol": "MSFT", "price": 420.75, "change": 8.90},
                    {"symbol": "AMZN", "price": 3100.00, "change": 25.60},
                    {"symbol": "TSLA", "price": 800.40, "change": -12.35}
                ],
                "crypto": [
                    {"symbol": "BTC", "price": 65000, "change": 5.2},
                    {"symbol": "ETH", "price": 4200, "change": -2.1},
                    {"symbol": "ADA", "price": 2.15, "change": 8.7}
                ]
            },
            "timestamp": datetime.now().isoformat()
        }
        
        # 保存模拟数据
        with open('market_data.json', 'w', encoding='utf-8') as file:
            json.dump(mock_api_data, file, ensure_ascii=False, indent=2)
        
        # 分析股票数据
        stocks = mock_api_data['data']['stocks']
        symbols = [stock['symbol'] for stock in stocks]
        prices = [stock['price'] for stock in stocks]
        changes = [stock['change'] for stock in stocks]
        
        # 可视化
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # 股价图
        bars1 = ax1.bar(symbols, prices, color=['green' if p > 1000 else 'blue' for p in prices])
        ax1.set_title('股票价格')
        ax1.set_ylabel('价格 ($)')
        
        # 添加价格标签
        for bar, price in zip(bars1, prices):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50,
                    f'${price:.2f}', ha='center', va='bottom')
        
        # 涨跌图
        colors = ['green' if c > 0 else 'red' for c in changes]
        bars2 = ax2.bar(symbols, changes, color=colors)
        ax2.set_title('价格变化')
        ax2.set_ylabel('变化 ($)')
        ax2.axhline(y=0, color='black', linestyle='-', alpha=0.3)
        
        # 添加变化标签
        for bar, change in zip(bars2, changes):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2, 
                    height + (1 if height > 0 else -2),
                    f'${change:.2f}', ha='center', 
                    va='bottom' if height > 0 else 'top')
        
        plt.tight_layout()
        plt.show()
        
        print("股票市场分析:")
        gainers = [s for s in stocks if s['change'] > 0]
        losers = [s for s in stocks if s['change'] < 0]
        print(f"上涨股票: {len(gainers)} 只")
        print(f"下跌股票: {len(losers)} 只")
        if gainers:
            best_performer = max(gainers, key=lambda x: x['change'])
            print(f"最佳表现: {best_performer['symbol']} (+${best_performer['change']:.2f})")
        if losers:
            worst_performer = min(losers, key=lambda x: x['change'])
            print(f"最差表现: {worst_performer['symbol']} (${worst_performer['change']:.2f})")
    
    def pandas_demo(self):
        """Pandas数据处理演示"""
        print("=" * 50)
        print("4. Pandas数据处理演示")
        print("=" * 50)
        
        try:
            # 创建示例数据集
            np.random.seed(42)
            dates = pd.date_range('2024-01-01', periods=100, freq='D')
            data = {
                '日期': dates,
                '销售额': np.random.normal(10000, 2000, 100).round(2),
                '订单数': np.random.poisson(50, 100),
                '客户数': np.random.normal(200, 30, 100).round(0).astype(int),
                '地区': np.random.choice(['北区', '南区', '东区', '西区'], 100),
                '产品类型': np.random.choice(['电子', '服装', '食品', '图书'], 100)
            }
            
            df = pd.DataFrame(data)
            
            # 保存数据
            df.to_csv('sales_data.csv', index=False, encoding='utf-8')
            
            # 数据分析
            print("数据集概览:")
            print(f"数据形状: {df.shape}")
            print(f"列名: {list(df.columns)}")
            print("\n基础统计:")
            print(df.describe())
            
            # 按地区分组分析
            region_stats = df.groupby('地区').agg({
                '销售额': ['sum', 'mean'],
                '订单数': 'sum',
                '客户数': 'mean'
            }).round(2)
            
            print("\n各地区销售统计:")
            print(region_stats)
            
            # 可视化
            fig, axes = plt.subplots(2, 2, figsize=(15, 12))
            
            # 销售额趋势
            df.set_index('日期')['销售额'].plot(ax=axes[0,0], title='销售额趋势')
            axes[0,0].set_ylabel('销售额')
            
            # 地区销售分布
            region_sales = df.groupby('地区')['销售额'].sum()
            region_sales.plot(kind='bar', ax=axes[0,1], title='各地区总销售额')
            axes[0,1].set_ylabel('销售额')
            axes[0,1].tick_params(axis='x', rotation=45)
            
            # 产品类型分布
            product_sales = df.groupby('产品类型')['销售额'].sum()
            product_sales.plot(kind='pie', ax=axes[1,0], title='产品类型销售占比', autopct='%1.1f%%')
            
            # 销售额分布直方图
            df['销售额'].hist(bins=20, ax=axes[1,1], title='销售额分布')
            axes[1,1].set_xlabel('销售额')
            axes[1,1].set_ylabel('频次')
            
            plt.tight_layout()
            plt.show()
            
        except ImportError:
            print("未安装pandas，跳过pandas演示")
            print("安装命令: pip install pandas")
    
    def data_cleaning_demo(self):
        """数据清洗演示"""
        print("=" * 50)
        print("5. 数据清洗演示")
        print("=" * 50)
        
        # 创建包含脏数据的数据集
        dirty_data = [
            ['张三', '25', '北京', '50000', '2023-01-15'],
            ['李四', 'unknown', '上海', '60000', '2023-02-20'],
            ['王五', '35', '', '75000', '2023-03-10'],
            ['', '28', '广州', '45000', '2023-04-05'],
            ['赵六', '30', '深圳', 'N/A', '2023-05-12'],
            ['孙七', '45', '北京', '80000', 'invalid_date'],
            ['周八', '33', '上海', '55000', '2023-06-18'],
            ['吴九', '29', '北京', '52000', '2023-07-22']
        ]
        
        headers = ['姓名', '年龄', '城市', '薪资', '入职日期']
        
        # 保存原始数据
        with open('dirty_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(dirty_data)
        
        # 数据清洗
        cleaned_data = []
        issues_found = []
        
        for i, row in enumerate(dirty_data):
            name, age, city, salary, date = row
            original_row = row.copy()
            issues = []
            
            # 处理姓名缺失
            if not name or name.strip() == '':
                name = f'员工{i+1}'
                issues.append('姓名缺失')
            
            # 处理年龄
            if age == 'unknown' or not age.isdigit():
                age = '30'  # 默认年龄
                issues.append('年龄无效')
            else:
                age = int(age)
                if age < 18 or age > 65:
                    age = 30
                    issues.append('年龄超出合理范围')
            
            # 处理城市缺失
            if not city or city.strip() == '':
                city = '未知'
                issues.append('城市缺失')
            
            # 处理薪资
            if salary == 'N/A' or not salary.replace(',', '').isdigit():
                salary = '50000'  # 默认薪资
                issues.append('薪资无效')
            else:
                salary = int(salary.replace(',', ''))
            
            # 处理日期
            try:
                datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                date = '2023-01-01'  # 默认日期
                issues.append('日期格式错误')
            
            cleaned_row = [name, age, city, salary, date]
            cleaned_data.append(cleaned_row)
            
            if issues:
                issues_found.append({
                    '行号': i + 1,
                    '原始数据': original_row,
                    '清洗后': cleaned_row,
                    '问题': ', '.join(issues)
                })
        
        # 保存清洗后的数据
        with open('cleaned_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(cleaned_data)
        
        # 统计清洗结果
        print(f"原始数据: {len(dirty_data)} 行")
        print(f"清洗后数据: {len(cleaned_data)} 行")
        print(f"发现问题: {len(issues_found)} 处")
        
        print("\n数据质量问题详情:")
        for issue in issues_found:
            print(f"行 {issue['行号']}: {issue['问题']}")
        
        # 可视化清洗前后对比
        ages_before = [int(row[1]) if row[1].isdigit() else 0 for row in dirty_data]
        ages_after = [row[1] for row in cleaned_data]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # 清洗前年龄分布
        valid_ages_before = [age for age in ages_before if age > 0]
        ax1.hist(valid_ages_before, bins=10, alpha=0.7, color='red')
        ax1.set_title('清洗前年龄分布')
        ax1.set_xlabel('年龄')
        ax1.set_ylabel('人数')
        
        # 清洗后年龄分布
        ax2.hist(ages_after, bins=10, alpha=0.7, color='green')
        ax2.set_title('清洗后年龄分布')
        ax2.set_xlabel('年龄')
        ax2.set_ylabel('人数')
        
        plt.tight_layout()
        plt.show()


def main():
    """主函数"""
    print("=" * 60)
    print("第16章 - 下载数据演示")
    print("=" * 60)
    
    downloader = DataDownloader()
    
    demos = [
        ("CSV数据处理", downloader.download_csv_data),
        ("JSON数据处理", downloader.process_json_data),
        ("API数据获取", downloader.fetch_api_data),
        ("Pandas数据分析", downloader.pandas_demo),
        ("数据清洗", downloader.data_cleaning_demo)
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
    
    print("\n感谢使用数据下载演示！")


if __name__ == '__main__':
    main() 