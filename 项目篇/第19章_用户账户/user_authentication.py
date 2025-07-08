#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第19章 - 用户账户管理
演示用户认证、权限管理和会话处理

主要功能：
1. 用户注册和登录
2. 密码加密和验证
3. 权限管理
4. 会话管理
"""

import hashlib
import secrets
import sqlite3
import json
from datetime import datetime, timedelta


class UserManager:
    """用户管理系统"""
    
    def __init__(self):
        self.db_file = 'user_system.db'
        self.init_database()
        self.current_user = None
        self.session_data = {}
    
    def init_database(self):
        """初始化数据库"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        # 用户表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(150) UNIQUE NOT NULL,
                email VARCHAR(254) UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                first_name VARCHAR(30),
                last_name VARCHAR(30),
                is_active BOOLEAN DEFAULT 1,
                is_staff BOOLEAN DEFAULT 0,
                date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_login TIMESTAMP
            )
        ''')
        
        # 会话表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                session_id VARCHAR(32) PRIMARY KEY,
                user_id INTEGER NOT NULL,
                data TEXT,
                expires_at TIMESTAMP NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # 用户权限表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_permissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                permission VARCHAR(100) NOT NULL,
                granted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()
        conn.close()
        
        # 创建管理员账户
        self.create_admin_user()
    
    def create_admin_user(self):
        """创建管理员账户"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        # 检查是否已有管理员
        cursor.execute('SELECT COUNT(*) FROM users WHERE username = ?', ('admin',))
        if cursor.fetchone()[0] > 0:
            conn.close()
            return
        
        # 创建管理员
        salt = secrets.token_hex(16)
        password_hash = self.hash_password('admin123', salt)
        
        cursor.execute('''
            INSERT INTO users (username, email, password_hash, salt, 
                             first_name, last_name, is_staff)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', ('admin', 'admin@example.com', password_hash, salt, 
              '管理员', '用户', 1))
        
        admin_id = cursor.lastrowid
        
        # 添加管理员权限
        permissions = ['create_user', 'delete_user', 'view_all_users', 'manage_permissions']
        for perm in permissions:
            cursor.execute(
                'INSERT INTO user_permissions (user_id, permission) VALUES (?, ?)',
                (admin_id, perm)
            )
        
        conn.commit()
        conn.close()
        
        print("管理员账户已创建: admin / admin123")
    
    def hash_password(self, password, salt):
        """密码加密"""
        return hashlib.sha256((password + salt).encode()).hexdigest()
    
    def verify_password(self, password, password_hash, salt):
        """验证密码"""
        return self.hash_password(password, salt) == password_hash
    
    def register_user(self, username, email, password, first_name='', last_name=''):
        """用户注册"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        try:
            # 检查用户名是否已存在
            cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
            if cursor.fetchone():
                return False, "用户名已存在"
            
            # 检查邮箱是否已存在
            cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
            if cursor.fetchone():
                return False, "邮箱已被注册"
            
            # 密码强度检查
            if len(password) < 6:
                return False, "密码长度至少6位"
            
            # 创建用户
            salt = secrets.token_hex(16)
            password_hash = self.hash_password(password, salt)
            
            cursor.execute('''
                INSERT INTO users (username, email, password_hash, salt, 
                                 first_name, last_name)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (username, email, password_hash, salt, first_name, last_name))
            
            user_id = cursor.lastrowid
            
            # 添加基本权限
            basic_permissions = ['view_profile', 'edit_profile']
            for perm in basic_permissions:
                cursor.execute(
                    'INSERT INTO user_permissions (user_id, permission) VALUES (?, ?)',
                    (user_id, perm)
                )
            
            conn.commit()
            return True, f"用户 {username} 注册成功"
            
        except Exception as e:
            conn.rollback()
            return False, f"注册失败: {str(e)}"
        finally:
            conn.close()
    
    def login(self, username, password):
        """用户登录"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, username, email, password_hash, salt, first_name, 
                   last_name, is_active, is_staff
            FROM users 
            WHERE username = ? AND is_active = 1
        ''', (username,))
        
        user = cursor.fetchone()
        
        if not user:
            conn.close()
            return False, "用户不存在或已被禁用"
        
        user_id, username, email, password_hash, salt, first_name, last_name, is_active, is_staff = user
        
        if not self.verify_password(password, password_hash, salt):
            conn.close()
            return False, "密码错误"
        
        # 更新最后登录时间
        cursor.execute(
            'UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = ?',
            (user_id,)
        )
        
        # 获取用户权限
        cursor.execute(
            'SELECT permission FROM user_permissions WHERE user_id = ?',
            (user_id,)
        )
        permissions = [row[0] for row in cursor.fetchall()]
        
        conn.commit()
        conn.close()
        
        # 设置当前用户
        self.current_user = {
            'id': user_id,
            'username': username,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'is_staff': bool(is_staff),
            'permissions': permissions,
            'login_time': datetime.now()
        }
        
        return True, f"欢迎回来，{first_name or username}！"
    
    def logout(self):
        """用户登出"""
        if self.current_user:
            username = self.current_user['username']
            self.current_user = None
            self.session_data = {}
            return f"用户 {username} 已登出"
        return "当前没有用户登录"
    
    def check_permission(self, permission):
        """检查权限"""
        if not self.current_user:
            return False
        
        if self.current_user['is_staff']:
            return True  # 管理员拥有所有权限
        
        return permission in self.current_user['permissions']
    
    def get_user_list(self):
        """获取用户列表（需要权限）"""
        if not self.check_permission('view_all_users'):
            return False, "权限不足"
        
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, username, email, first_name, last_name, 
                   is_active, is_staff, date_joined, last_login
            FROM users
            ORDER BY date_joined DESC
        ''')
        
        users = cursor.fetchall()
        conn.close()
        
        return True, users
    
    def update_profile(self, first_name=None, last_name=None, email=None):
        """更新个人资料"""
        if not self.current_user:
            return False, "请先登录"
        
        if not self.check_permission('edit_profile'):
            return False, "权限不足"
        
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        updates = []
        params = []
        
        if first_name is not None:
            updates.append('first_name = ?')
            params.append(first_name)
        
        if last_name is not None:
            updates.append('last_name = ?')
            params.append(last_name)
        
        if email is not None:
            # 检查邮箱是否已被其他用户使用
            cursor.execute('SELECT id FROM users WHERE email = ? AND id != ?', 
                          (email, self.current_user['id']))
            if cursor.fetchone():
                conn.close()
                return False, "邮箱已被其他用户使用"
            
            updates.append('email = ?')
            params.append(email)
        
        if not updates:
            conn.close()
            return False, "没有要更新的信息"
        
        params.append(self.current_user['id'])
        sql = f"UPDATE users SET {', '.join(updates)} WHERE id = ?"
        
        cursor.execute(sql, params)
        conn.commit()
        conn.close()
        
        # 更新当前用户信息
        if first_name is not None:
            self.current_user['first_name'] = first_name
        if last_name is not None:
            self.current_user['last_name'] = last_name
        if email is not None:
            self.current_user['email'] = email
        
        return True, "个人资料更新成功"
    
    def change_password(self, old_password, new_password):
        """修改密码"""
        if not self.current_user:
            return False, "请先登录"
        
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        # 获取当前密码信息
        cursor.execute(
            'SELECT password_hash, salt FROM users WHERE id = ?',
            (self.current_user['id'],)
        )
        
        result = cursor.fetchone()
        if not result:
            conn.close()
            return False, "用户不存在"
        
        current_hash, salt = result
        
        # 验证旧密码
        if not self.verify_password(old_password, current_hash, salt):
            conn.close()
            return False, "当前密码错误"
        
        # 检查新密码强度
        if len(new_password) < 6:
            conn.close()
            return False, "新密码长度至少6位"
        
        # 生成新的salt和hash
        new_salt = secrets.token_hex(16)
        new_hash = self.hash_password(new_password, new_salt)
        
        # 更新密码
        cursor.execute(
            'UPDATE users SET password_hash = ?, salt = ? WHERE id = ?',
            (new_hash, new_salt, self.current_user['id'])
        )
        
        conn.commit()
        conn.close()
        
        return True, "密码修改成功"
    
    def create_session(self, duration_hours=24):
        """创建会话"""
        if not self.current_user:
            return None
        
        session_id = secrets.token_hex(16)
        expires_at = datetime.now() + timedelta(hours=duration_hours)
        
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO sessions (session_id, user_id, data, expires_at)
            VALUES (?, ?, ?, ?)
        ''', (session_id, self.current_user['id'], json.dumps(self.session_data), expires_at))
        
        conn.commit()
        conn.close()
        
        return session_id
    
    def validate_session(self, session_id):
        """验证会话"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT s.user_id, s.data, u.username, u.first_name, u.last_name
            FROM sessions s
            JOIN users u ON s.user_id = u.id
            WHERE s.session_id = ? AND s.expires_at > CURRENT_TIMESTAMP
        ''', (session_id,))
        
        result = cursor.fetchone()
        conn.close()
        
        if result:
            user_id, data, username, first_name, last_name = result
            self.session_data = json.loads(data) if data else {}
            return {
                'user_id': user_id,
                'username': username,
                'first_name': first_name,
                'last_name': last_name
            }
        
        return None
    
    def get_current_user_info(self):
        """获取当前用户信息"""
        if not self.current_user:
            return "当前没有用户登录"
        
        info = f"""
当前用户信息:
用户名: {self.current_user['username']}
邮箱: {self.current_user['email']}
姓名: {self.current_user['first_name']} {self.current_user['last_name']}
管理员: {'是' if self.current_user['is_staff'] else '否'}
登录时间: {self.current_user['login_time'].strftime('%Y-%m-%d %H:%M:%S')}

权限列表:
"""
        for perm in self.current_user['permissions']:
            info += f"  - {perm}\n"
        
        return info


def main():
    """主函数"""
    print("=" * 60)
    print("第19章 - 用户账户管理系统演示")
    print("=" * 60)
    
    user_manager = UserManager()
    
    while True:
        if user_manager.current_user:
            print(f"\n当前用户: {user_manager.current_user['username']}")
        else:
            print("\n当前状态: 未登录")
        
        print("\n" + "=" * 40)
        print("用户管理系统")
        print("=" * 40)
        print("1. 用户注册")
        print("2. 用户登录")
        print("3. 用户登出")
        print("4. 查看个人信息")
        print("5. 修改个人资料")
        print("6. 修改密码")
        print("7. 查看用户列表（管理员）")
        print("8. 创建会话")
        print("9. 验证会话")
        print("0. 退出")
        
        try:
            choice = input("\n请选择操作 (0-9): ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                print("\n用户注册")
                username = input("用户名: ").strip()
                email = input("邮箱: ").strip()
                password = input("密码: ").strip()
                first_name = input("名字: ").strip()
                last_name = input("姓氏: ").strip()
                
                success, message = user_manager.register_user(
                    username, email, password, first_name, last_name
                )
                print(f"结果: {message}")
                
            elif choice == '2':
                print("\n用户登录")
                username = input("用户名: ").strip()
                password = input("密码: ").strip()
                
                success, message = user_manager.login(username, password)
                print(f"结果: {message}")
                
            elif choice == '3':
                message = user_manager.logout()
                print(f"结果: {message}")
                
            elif choice == '4':
                info = user_manager.get_current_user_info()
                print(info)
                
            elif choice == '5':
                if not user_manager.current_user:
                    print("请先登录")
                    continue
                
                print("\n修改个人资料（留空表示不修改）")
                first_name = input("名字: ").strip() or None
                last_name = input("姓氏: ").strip() or None
                email = input("邮箱: ").strip() or None
                
                success, message = user_manager.update_profile(
                    first_name, last_name, email
                )
                print(f"结果: {message}")
                
            elif choice == '6':
                if not user_manager.current_user:
                    print("请先登录")
                    continue
                
                print("\n修改密码")
                old_password = input("当前密码: ").strip()
                new_password = input("新密码: ").strip()
                
                success, message = user_manager.change_password(old_password, new_password)
                print(f"结果: {message}")
                
            elif choice == '7':
                success, result = user_manager.get_user_list()
                if success:
                    print("\n用户列表:")
                    print("-" * 80)
                    for user in result:
                        user_id, username, email, first_name, last_name, is_active, is_staff, date_joined, last_login = user
                        print(f"ID: {user_id} | 用户名: {username} | 邮箱: {email}")
                        print(f"姓名: {first_name} {last_name} | 管理员: {'是' if is_staff else '否'}")
                        print(f"注册时间: {date_joined} | 最后登录: {last_login or '从未登录'}")
                        print("-" * 80)
                else:
                    print(f"错误: {result}")
                
            elif choice == '8':
                session_id = user_manager.create_session()
                if session_id:
                    print(f"会话创建成功: {session_id}")
                else:
                    print("请先登录")
                
            elif choice == '9':
                session_id = input("请输入会话ID: ").strip()
                user_info = user_manager.validate_session(session_id)
                if user_info:
                    print(f"会话有效，用户: {user_info['username']}")
                else:
                    print("会话无效或已过期")
                
            else:
                print("无效选择，请重试")
                
            input("\n按回车键继续...")
            
        except KeyboardInterrupt:
            print("\n\n程序已中断")
            break
        except Exception as e:
            print(f"操作出错: {e}")
            input("按回车键继续...")
    
    print("\n感谢使用用户管理系统！")


if __name__ == '__main__':
    main() 