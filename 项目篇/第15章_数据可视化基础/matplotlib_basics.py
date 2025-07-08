#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第15章 - 数据可视化基础
使用matplotlib创建各种图表和可视化

主要内容：
1. 基础图表绘制
2. 图表样式和美化
3. 多子图布局
4. 交互式图表
5. 数据分析可视化
"""

import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime, timedelta

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


def basic_line_plot():
    """基础折线图"""
    print("1. 基础折线图演示")
    
    # 生成数据
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) * np.cos(x)
    
    plt.figure(figsize=(12, 8))
    
    # 绘制多条线
    plt.plot(x, y1, label='sin(x)', linewidth=2, color='blue')
    plt.plot(x, y2, label='cos(x)', linewidth=2, color='red', linestyle='--')
    plt.plot(x, y3, label='sin(x)cos(x)', linewidth=2, color='green', linestyle=':')
    
    # 添加标题和标签
    plt.title('三角函数图像', fontsize=16, fontweight='bold')
    plt.xlabel('X 轴', fontsize=12)
    plt.ylabel('Y 轴', fontsize=12)
    
    # 添加图例和网格
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    
    # 设置坐标轴范围
    plt.xlim(0, 10)
    plt.ylim(-1.5, 1.5)
    
    plt.tight_layout()
    plt.show()


def scatter_plot_demo():
    """散点图演示"""
    print("2. 散点图演示")
    
    # 生成随机数据
    np.random.seed(42)
    n = 100
    x = np.random.randn(n)
    y = 2 * x + np.random.randn(n) * 0.5
    colors = np.random.rand(n)
    sizes = 1000 * np.random.rand(n)
    
    plt.figure(figsize=(10, 8))
    
    # 创建散点图
    scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
    
    # 添加颜色条
    plt.colorbar(scatter, label='颜色值')
    
    plt.title('随机散点图', fontsize=16)
    plt.xlabel('X 值', fontsize=12)
    plt.ylabel('Y 值', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def bar_chart_demo():
    """柱状图演示"""
    print("3. 柱状图演示")
    
    # 模拟销售数据
    products = ['手机', '电脑', '平板', '耳机', '手表']
    sales_q1 = [120, 85, 60, 200, 45]
    sales_q2 = [135, 90, 75, 180, 55]
    sales_q3 = [110, 95, 80, 220, 50]
    
    x = np.arange(len(products))
    width = 0.25
    
    plt.figure(figsize=(12, 8))
    
    # 创建分组柱状图
    plt.bar(x - width, sales_q1, width, label='Q1', color='skyblue')
    plt.bar(x, sales_q2, width, label='Q2', color='lightcoral')
    plt.bar(x + width, sales_q3, width, label='Q3', color='lightgreen')
    
    plt.title('季度销售对比', fontsize=16)
    plt.xlabel('产品', fontsize=12)
    plt.ylabel('销售数量', fontsize=12)
    plt.xticks(x, products)
    plt.legend()
    plt.grid(True, alpha=0.3, axis='y')
    
    # 添加数值标签
    for i, (q1, q2, q3) in enumerate(zip(sales_q1, sales_q2, sales_q3)):
        plt.text(i - width, q1 + 2, str(q1), ha='center', va='bottom', fontsize=8)
        plt.text(i, q2 + 2, str(q2), ha='center', va='bottom', fontsize=8)
        plt.text(i + width, q3 + 2, str(q3), ha='center', va='bottom', fontsize=8)
    
    plt.tight_layout()
    plt.show()


def pie_chart_demo():
    """饼图演示"""
    print("4. 饼图演示")
    
    # 市场份额数据
    labels = ['iOS', 'Android', 'Windows', '其他']
    sizes = [25, 60, 10, 5]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    explode = (0, 0.1, 0, 0)  # 突出显示Android
    
    plt.figure(figsize=(10, 8))
    
    # 创建饼图
    wedges, texts, autotexts = plt.pie(sizes, explode=explode, labels=labels, 
                                      colors=colors, autopct='%1.1f%%',
                                      shadow=True, startangle=90)
    
    # 美化文本
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    plt.title('操作系统市场份额', fontsize=16)
    plt.axis('equal')  # 确保饼图是圆形
    
    plt.tight_layout()
    plt.show()


def histogram_demo():
    """直方图演示"""
    print("5. 直方图演示")
    
    # 生成正态分布数据
    np.random.seed(42)
    data1 = np.random.normal(100, 15, 1000)
    data2 = np.random.normal(110, 20, 1000)
    
    plt.figure(figsize=(12, 8))
    
    # 创建直方图
    plt.hist(data1, bins=30, alpha=0.7, label='组A', color='skyblue', density=True)
    plt.hist(data2, bins=30, alpha=0.7, label='组B', color='lightcoral', density=True)
    
    plt.title('成绩分布直方图', fontsize=16)
    plt.xlabel('分数', fontsize=12)
    plt.ylabel('密度', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 添加统计信息
    plt.axvline(np.mean(data1), color='blue', linestyle='--', alpha=0.8, label=f'组A均值: {np.mean(data1):.1f}')
    plt.axvline(np.mean(data2), color='red', linestyle='--', alpha=0.8, label=f'组B均值: {np.mean(data2):.1f}')
    
    plt.tight_layout()
    plt.show()


def subplot_demo():
    """子图演示"""
    print("6. 多子图布局演示")
    
    # 生成数据
    x = np.linspace(0, 10, 100)
    
    # 创建2x2子图
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # 子图1: 正弦波
    ax1.plot(x, np.sin(x), 'b-', linewidth=2)
    ax1.set_title('sin(x)')
    ax1.grid(True, alpha=0.3)
    
    # 子图2: 余弦波
    ax2.plot(x, np.cos(x), 'r-', linewidth=2)
    ax2.set_title('cos(x)')
    ax2.grid(True, alpha=0.3)
    
    # 子图3: 散点图
    y3 = np.random.randn(50)
    x3 = np.random.randn(50)
    ax3.scatter(x3, y3, alpha=0.6)
    ax3.set_title('随机散点')
    ax3.grid(True, alpha=0.3)
    
    # 子图4: 柱状图
    categories = ['A', 'B', 'C', 'D']
    values = [23, 45, 56, 78]
    ax4.bar(categories, values, color=['red', 'green', 'blue', 'orange'])
    ax4.set_title('分类数据')
    
    plt.tight_layout()
    plt.show()


def time_series_demo():
    """时间序列演示"""
    print("7. 时间序列图演示")
    
    # 生成时间序列数据
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(365)]
    
    # 模拟股价数据
    np.random.seed(42)
    prices = [100]
    for i in range(364):
        change = np.random.normal(0, 2)
        new_price = max(prices[-1] + change, 50)  # 防止价格为负
        prices.append(new_price)
    
    plt.figure(figsize=(15, 8))
    
    # 绘制时间序列
    plt.plot(dates, prices, linewidth=1.5, color='blue', alpha=0.8)
    
    # 添加移动平均线
    window = 30
    moving_avg = []
    for i in range(len(prices)):
        if i < window:
            moving_avg.append(np.mean(prices[:i+1]))
        else:
            moving_avg.append(np.mean(prices[i-window+1:i+1]))
    
    plt.plot(dates, moving_avg, linewidth=2, color='red', label=f'{window}日移动平均')
    
    plt.title('股价走势图', fontsize=16)
    plt.xlabel('日期', fontsize=12)
    plt.ylabel('价格 (元)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 格式化日期轴
    import matplotlib.dates as mdates
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()


def heatmap_demo():
    """热力图演示"""
    print("8. 热力图演示")
    
    # 生成相关性矩阵数据
    np.random.seed(42)
    data = np.random.randn(10, 12)
    correlation_matrix = np.corrcoef(data)
    
    plt.figure(figsize=(12, 10))
    
    # 创建热力图
    im = plt.imshow(correlation_matrix, cmap='coolwarm', vmin=-1, vmax=1)
    
    # 添加颜色条
    plt.colorbar(im, label='相关系数')
    
    # 添加数值标签
    for i in range(len(correlation_matrix)):
        for j in range(len(correlation_matrix)):
            text = plt.text(j, i, f'{correlation_matrix[i, j]:.2f}',
                          ha="center", va="center", color="black" if abs(correlation_matrix[i, j]) < 0.5 else "white")
    
    plt.title('相关性热力图', fontsize=16)
    plt.xlabel('变量 Index', fontsize=12)
    plt.ylabel('变量 Index', fontsize=12)
    
    plt.tight_layout()
    plt.show()


def style_demo():
    """图表样式演示"""
    print("9. 图表样式演示")
    
    # 可用样式
    available_styles = ['default', 'seaborn', 'ggplot', 'bmh']
    
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    axes = axes.ravel()
    
    for i, style in enumerate(available_styles):
        try:
            with plt.style.context(style):
                axes[i].plot(x, y, linewidth=2)
                axes[i].set_title(f'样式: {style}', fontsize=12)
                axes[i].grid(True, alpha=0.3)
        except:
            # 如果样式不可用，使用默认样式
            axes[i].plot(x, y, linewidth=2)
            axes[i].set_title(f'样式: {style} (不可用)', fontsize=12)
            axes[i].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def comprehensive_demo():
    """综合演示"""
    print("10. 综合数据可视化演示")
    
    # 创建复杂的多子图布局
    fig = plt.figure(figsize=(20, 12))
    
    # 定义网格布局
    gs = fig.add_gridspec(3, 4, hspace=0.3, wspace=0.3)
    
    # 子图1: 3D表面图
    ax1 = fig.add_subplot(gs[0, :2], projection='3d')
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    surf = ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax1.set_title('3D表面图')
    
    # 子图2: 极坐标图
    ax2 = fig.add_subplot(gs[0, 2:], projection='polar')
    theta = np.linspace(0, 2*np.pi, 100)
    r = 1 + 0.5 * np.sin(5*theta)
    ax2.plot(theta, r, linewidth=3)
    ax2.set_title('极坐标图')
    
    # 子图3: 箱线图
    ax3 = fig.add_subplot(gs[1, :2])
    data_box = [np.random.normal(0, std, 100) for std in range(1, 4)]
    box_plot = ax3.boxplot(data_box, labels=['组1', '组2', '组3'], patch_artist=True)
    colors = ['lightblue', 'lightgreen', 'lightcoral']
    for patch, color in zip(box_plot['boxes'], colors):
        patch.set_facecolor(color)
    ax3.set_title('箱线图')
    ax3.grid(True, alpha=0.3)
    
    # 子图4: 小提琴图
    ax4 = fig.add_subplot(gs[1, 2:])
    violin_data = [np.random.normal(i, 0.5, 100) for i in range(1, 5)]
    parts = ax4.violinplot(violin_data, positions=range(1, 5), showmeans=True)
    ax4.set_title('小提琴图')
    ax4.set_xlabel('组别')
    
    # 子图5: 等高线图
    ax5 = fig.add_subplot(gs[2, :])
    X_contour = np.linspace(-3, 3, 100)
    Y_contour = np.linspace(-3, 3, 100)
    X_contour, Y_contour = np.meshgrid(X_contour, Y_contour)
    Z_contour = np.exp(-(X_contour**2 + Y_contour**2))
    
    contour = ax5.contour(X_contour, Y_contour, Z_contour, levels=10)
    ax5.clabel(contour, inline=True, fontsize=8)
    contourf = ax5.contourf(X_contour, Y_contour, Z_contour, levels=50, alpha=0.6, cmap='viridis')
    fig.colorbar(contourf, ax=ax5, shrink=0.8)
    ax5.set_title('等高线图')
    
    plt.suptitle('综合数据可视化演示', fontsize=20, fontweight='bold')
    plt.show()


def interactive_demo():
    """交互式演示"""
    print("11. 交互式图表演示")
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # 生成数据
    x = np.linspace(0, 10, 100)
    line, = ax.plot(x, np.sin(x), linewidth=2, label='sin(x)')
    
    ax.set_title('交互式图表示例\n(在图表上点击鼠标查看坐标)', fontsize=14)
    ax.set_xlabel('X 轴')
    ax.set_ylabel('Y 轴')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    # 添加点击事件
    def on_click(event):
        if event.inaxes == ax:
            x_click, y_click = event.xdata, event.ydata
            ax.plot(x_click, y_click, 'ro', markersize=8)
            ax.annotate(f'({x_click:.2f}, {y_click:.2f})', 
                       xy=(x_click, y_click), xytext=(10, 10),
                       textcoords='offset points', 
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
                       arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
            plt.draw()
    
    fig.canvas.mpl_connect('button_press_event', on_click)
    
    plt.show()


def main():
    """主函数"""
    print("=" * 60)
    print("第15章 - matplotlib数据可视化基础")
    print("=" * 60)
    
    demos = [
        ("基础折线图", basic_line_plot),
        ("散点图", scatter_plot_demo),
        ("柱状图", bar_chart_demo),
        ("饼图", pie_chart_demo),
        ("直方图", histogram_demo),
        ("多子图布局", subplot_demo),
        ("时间序列图", time_series_demo),
        ("热力图", heatmap_demo),
        ("图表样式", style_demo),
        ("综合演示", comprehensive_demo),
        ("交互式图表", interactive_demo)
    ]
    
    while True:
        print("\n可用的演示:")
        for i, (name, _) in enumerate(demos, 1):
            print(f"{i:2d}. {name}")
        print(" 0. 退出")
        
        try:
            choice = input("\n请选择要运行的演示 (0-11): ").strip()
            
            if choice == '0':
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(demos):
                print(f"\n正在运行: {demos[int(choice)-1][0]}")
                print("-" * 40)
                
                try:
                    demos[int(choice)-1][1]()
                except Exception as e:
                    print(f"运行演示时出错: {e}")
                    print("请确保已安装必要的依赖包:")
                    print("pip install matplotlib numpy")
                
                input("\n按回车键继续...")
            else:
                print("无效选择，请重试")
                
        except KeyboardInterrupt:
            print("\n\n演示已中断")
            break
        except Exception as e:
            print(f"输入错误: {e}")
    
    print("\n感谢使用matplotlib数据可视化演示！")


if __name__ == '__main__':
    main() 