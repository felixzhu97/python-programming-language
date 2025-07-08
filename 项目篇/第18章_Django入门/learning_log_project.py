#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第18章 - Django入门
学习笔记Web应用项目演示

主要功能：
1. Django项目结构
2. 模型设计
3. 视图和URL配置
4. 模板系统
5. 表单处理
"""

import os
import sqlite3
from datetime import datetime


class LearningLogDemo:
    """学习笔记项目演示"""
    
    def __init__(self):
        self.db_file = 'learning_log.db'
        self.init_database()
    
    def init_database(self):
        """初始化数据库"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        # 创建主题表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS topics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text VARCHAR(200) NOT NULL,
                date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # 创建条目表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_id INTEGER NOT NULL,
                text TEXT NOT NULL,
                date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (topic_id) REFERENCES topics (id)
            )
        ''')
        
        conn.commit()
        conn.close()
        
        # 添加示例数据
        self.add_sample_data()
    
    def add_sample_data(self):
        """添加示例数据"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        # 检查是否已有数据
        cursor.execute('SELECT COUNT(*) FROM topics')
        if cursor.fetchone()[0] > 0:
            conn.close()
            return
        
        # 添加示例主题
        topics = [
            ('Python基础', '学习Python编程语言的基础知识'),
            ('Web开发', '学习使用Django进行Web开发'),
            ('数据科学', '学习使用Python进行数据分析和可视化'),
            ('算法学习', '学习常用算法和数据结构'),
            ('项目经验', '记录实际项目开发的经验和心得')
        ]
        
        for topic, description in topics:
            cursor.execute('INSERT INTO topics (text) VALUES (?)', (topic,))
            topic_id = cursor.lastrowid
            
            # 为每个主题添加示例条目
            entries = self.get_sample_entries(topic)
            for entry in entries:
                cursor.execute(
                    'INSERT INTO entries (topic_id, text) VALUES (?, ?)',
                    (topic_id, entry)
                )
        
        conn.commit()
        conn.close()
    
    def get_sample_entries(self, topic):
        """获取示例条目"""
        entries_dict = {
            'Python基础': [
                '今天学习了Python的基本语法，包括变量、数据类型和控制结构。',
                '深入了解了Python的列表和字典，这些数据结构非常强大。',
                '学习了函数的定义和使用，理解了参数传递的机制。'
            ],
            'Web开发': [
                '开始学习Django框架，了解了MVC（MTV）架构模式。',
                '学习了Django的模型系统，理解了ORM的概念。',
                '今天创建了第一个Django视图和模板。'
            ],
            '数据科学': [
                '学习了NumPy库，了解了数组操作的基础知识。',
                '开始使用matplotlib进行数据可视化，创建了第一个图表。',
                '学习了pandas库，理解了DataFrame的强大功能。'
            ],
            '算法学习': [
                '学习了排序算法，实现了冒泡排序和快速排序。',
                '今天学习了二分查找算法，理解了时间复杂度的概念。',
                '学习了栈和队列数据结构，了解了它们的应用场景。'
            ],
            '项目经验': [
                '完成了第一个Python项目 - 猜数字游戏。',
                '开发了一个简单的待办事项管理器。',
                '参与了团队项目，学习了版本控制和协作开发。'
            ]
        }
        return entries_dict.get(topic, ['这是一个示例条目。'])
    
    def show_topics(self):
        """显示所有主题"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, text, date_added, 
                   (SELECT COUNT(*) FROM entries WHERE topic_id = topics.id) as entry_count
            FROM topics 
            ORDER BY date_added DESC
        ''')
        
        topics = cursor.fetchall()
        conn.close()
        
        print("=" * 60)
        print("学习笔记 - 所有主题")
        print("=" * 60)
        
        if not topics:
            print("还没有任何主题。")
            return
        
        for topic_id, text, date_added, entry_count in topics:
            print(f"ID: {topic_id}")
            print(f"主题: {text}")
            print(f"创建时间: {date_added}")
            print(f"条目数量: {entry_count}")
            print("-" * 40)
    
    def show_topic_entries(self, topic_id):
        """显示指定主题的所有条目"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        # 获取主题信息
        cursor.execute('SELECT text FROM topics WHERE id = ?', (topic_id,))
        topic_result = cursor.fetchone()
        
        if not topic_result:
            print(f"未找到ID为 {topic_id} 的主题。")
            conn.close()
            return
        
        topic_text = topic_result[0]
        
        # 获取条目
        cursor.execute('''
            SELECT id, text, date_added 
            FROM entries 
            WHERE topic_id = ? 
            ORDER BY date_added
        ''', (topic_id,))
        
        entries = cursor.fetchall()
        conn.close()
        
        print("=" * 60)
        print(f"主题: {topic_text}")
        print("=" * 60)
        
        if not entries:
            print("该主题还没有任何条目。")
            return
        
        for entry_id, text, date_added in entries:
            print(f"条目 {entry_id} - {date_added}")
            print(f"{text}")
            print("-" * 40)
    
    def add_topic(self, topic_text):
        """添加新主题"""
        if not topic_text.strip():
            print("主题名称不能为空！")
            return False
        
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO topics (text) VALUES (?)', (topic_text.strip(),))
        topic_id = cursor.lastrowid
        
        conn.commit()
        conn.close()
        
        print(f"成功添加主题: {topic_text}")
        print(f"主题ID: {topic_id}")
        return True
    
    def add_entry(self, topic_id, entry_text):
        """添加新条目"""
        if not entry_text.strip():
            print("条目内容不能为空！")
            return False
        
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        # 检查主题是否存在
        cursor.execute('SELECT text FROM topics WHERE id = ?', (topic_id,))
        if not cursor.fetchone():
            print(f"未找到ID为 {topic_id} 的主题。")
            conn.close()
            return False
        
        cursor.execute(
            'INSERT INTO entries (topic_id, text) VALUES (?, ?)',
            (topic_id, entry_text.strip())
        )
        entry_id = cursor.lastrowid
        
        conn.commit()
        conn.close()
        
        print(f"成功添加条目到主题 {topic_id}")
        print(f"条目ID: {entry_id}")
        return True
    
    def search_entries(self, keyword):
        """搜索条目"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT e.id, e.text, e.date_added, t.text as topic_text
            FROM entries e
            JOIN topics t ON e.topic_id = t.id
            WHERE e.text LIKE ? OR t.text LIKE ?
            ORDER BY e.date_added DESC
        ''', (f'%{keyword}%', f'%{keyword}%'))
        
        results = cursor.fetchall()
        conn.close()
        
        print("=" * 60)
        print(f"搜索结果: '{keyword}'")
        print("=" * 60)
        
        if not results:
            print("未找到相关条目。")
            return
        
        for entry_id, text, date_added, topic_text in results:
            print(f"主题: {topic_text}")
            print(f"条目 {entry_id} - {date_added}")
            # 高亮显示关键词
            highlighted_text = text.replace(keyword, f"**{keyword}**")
            print(f"{highlighted_text}")
            print("-" * 40)
        
        print(f"共找到 {len(results)} 条相关记录")
    
    def get_statistics(self):
        """获取统计信息"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        # 主题数量
        cursor.execute('SELECT COUNT(*) FROM topics')
        topic_count = cursor.fetchone()[0]
        
        # 条目数量
        cursor.execute('SELECT COUNT(*) FROM entries')
        entry_count = cursor.fetchone()[0]
        
        # 最活跃的主题
        cursor.execute('''
            SELECT t.text, COUNT(e.id) as entry_count
            FROM topics t
            LEFT JOIN entries e ON t.id = e.topic_id
            GROUP BY t.id, t.text
            ORDER BY entry_count DESC
            LIMIT 5
        ''')
        
        active_topics = cursor.fetchall()
        
        # 最近的活动
        cursor.execute('''
            SELECT e.date_added, t.text, 
                   SUBSTR(e.text, 1, 50) || '...' as preview
            FROM entries e
            JOIN topics t ON e.topic_id = t.id
            ORDER BY e.date_added DESC
            LIMIT 5
        ''')
        
        recent_activities = cursor.fetchall()
        
        conn.close()
        
        print("=" * 60)
        print("学习笔记统计")
        print("=" * 60)
        print(f"总主题数: {topic_count}")
        print(f"总条目数: {entry_count}")
        print(f"平均每主题条目数: {entry_count/topic_count:.1f}" if topic_count > 0 else "平均每主题条目数: 0")
        
        print("\n最活跃的主题:")
        for topic_text, count in active_topics:
            print(f"  {topic_text}: {count} 条目")
        
        print("\n最近的学习活动:")
        for date_added, topic_text, preview in recent_activities:
            print(f"  {date_added} - {topic_text}")
            print(f"    {preview}")
    
    def export_data(self, filename=None):
        """导出数据"""
        if not filename:
            filename = f"learning_log_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT t.text as topic, e.text as entry, e.date_added
            FROM topics t
            LEFT JOIN entries e ON t.id = e.topic_id
            ORDER BY t.date_added, e.date_added
        ''')
        
        data = cursor.fetchall()
        conn.close()
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("学习笔记导出\n")
            f.write("=" * 50 + "\n")
            f.write(f"导出时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            current_topic = None
            for topic, entry, date_added in data:
                if topic != current_topic:
                    current_topic = topic
                    f.write(f"\n主题: {topic}\n")
                    f.write("-" * 30 + "\n")
                
                if entry:
                    f.write(f"{date_added}: {entry}\n\n")
        
        print(f"数据已导出到: {filename}")


def main():
    """主函数"""
    print("=" * 60)
    print("第18章 - Django学习笔记项目演示")
    print("=" * 60)
    print("注意: 这是一个简化的命令行版本，演示Django项目的核心概念")
    print("实际Django项目会使用Web界面和更复杂的功能")
    
    app = LearningLogDemo()
    
    while True:
        print("\n" + "=" * 40)
        print("学习笔记管理系统")
        print("=" * 40)
        print("1. 查看所有主题")
        print("2. 查看主题条目")
        print("3. 添加新主题")
        print("4. 添加新条目")
        print("5. 搜索条目")
        print("6. 查看统计信息")
        print("7. 导出数据")
        print("0. 退出")
        
        try:
            choice = input("\n请选择操作 (0-7): ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                app.show_topics()
            elif choice == '2':
                topic_id = input("请输入主题ID: ").strip()
                if topic_id.isdigit():
                    app.show_topic_entries(int(topic_id))
                else:
                    print("请输入有效的主题ID（数字）")
            elif choice == '3':
                topic_text = input("请输入新主题名称: ").strip()
                app.add_topic(topic_text)
            elif choice == '4':
                topic_id = input("请输入主题ID: ").strip()
                if topic_id.isdigit():
                    entry_text = input("请输入条目内容: ").strip()
                    app.add_entry(int(topic_id), entry_text)
                else:
                    print("请输入有效的主题ID（数字）")
            elif choice == '5':
                keyword = input("请输入搜索关键词: ").strip()
                if keyword:
                    app.search_entries(keyword)
                else:
                    print("搜索关键词不能为空")
            elif choice == '6':
                app.get_statistics()
            elif choice == '7':
                filename = input("请输入导出文件名（留空使用默认名称）: ").strip()
                app.export_data(filename if filename else None)
            else:
                print("无效选择，请重试")
                
            input("\n按回车键继续...")
            
        except KeyboardInterrupt:
            print("\n\n程序已中断")
            break
        except Exception as e:
            print(f"操作出错: {e}")
            input("按回车键继续...")
    
    print("\n感谢使用学习笔记管理系统！")
    print("在实际Django项目中，您将拥有:")
    print("- 美观的Web界面")
    print("- 用户认证系统")
    print("- 更强大的搜索功能")
    print("- 实时数据更新")
    print("- 响应式设计")


if __name__ == '__main__':
    main() 