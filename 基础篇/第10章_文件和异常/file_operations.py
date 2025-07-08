#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第10章 文件和异常 - 文件操作详解

本文件详细演示Python中的文件操作，包括：
1. 文件的读取和写入
2. 文件路径操作
3. 文件和目录管理
4. 不同编码的处理
5. 二进制文件操作
6. 临时文件和安全操作
7. 文件监控和处理
8. 实际应用示例

文件操作是程序与外部数据交互的重要方式，掌握文件操作对于数据处理和程序开发至关重要。
"""

import os
import sys
import shutil
import tempfile
import glob
from pathlib import Path
from datetime import datetime


def main():
    """主函数，演示文件操作"""
    print("=" * 60)
    print("第10章 文件和异常 - 文件操作详解")
    print("=" * 60)
    print()
    
    # 1. 基本文件读取
    print("1. 基本文件读取")
    print("-" * 30)
    
    # 创建示例文件
    sample_text = """Python是一种高级编程语言
它简单易学，功能强大
适合初学者和专业开发者
在数据科学、Web开发、人工智能等领域都有广泛应用"""
    
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write(sample_text)
    
    # 读取整个文件
    print("读取整个文件：")
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
    print()
    
    # 逐行读取
    print("逐行读取：")
    with open("sample.txt", "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, 1):
            print(f"第{line_number}行：{line.strip()}")
    print()
    
    # 读取为列表
    print("读取为列表：")
    with open("sample.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, 1):
            print(f"列表第{i}项：{line.strip()}")
    print()
    
    # 2. 文件写入操作
    print("2. 文件写入操作")
    print("-" * 30)
    
    # 写入模式
    print("写入新内容（覆盖原有内容）：")
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write("这是第一行\n")
        file.write("这是第二行\n")
        file.writelines(["这是第三行\n", "这是第四行\n"])
    
    # 读取验证
    with open("output.txt", "r", encoding="utf-8") as file:
        print(file.read())
    
    # 追加模式
    print("追加新内容：")
    with open("output.txt", "a", encoding="utf-8") as file:
        file.write("这是追加的第一行\n")
        file.write("这是追加的第二行\n")
    
    # 读取验证
    with open("output.txt", "r", encoding="utf-8") as file:
        print(file.read())
    
    # 3. 文件路径操作
    print("3. 文件路径操作")
    print("-" * 30)
    
    # 使用os.path模块
    print("使用os.path模块：")
    file_path = "sample.txt"
    print(f"文件路径：{file_path}")
    print(f"绝对路径：{os.path.abspath(file_path)}")
    print(f"文件名：{os.path.basename(file_path)}")
    print(f"目录名：{os.path.dirname(os.path.abspath(file_path))}")
    print(f"文件扩展名：{os.path.splitext(file_path)[1]}")
    print(f"文件存在：{os.path.exists(file_path)}")
    print(f"是否为文件：{os.path.isfile(file_path)}")
    print(f"是否为目录：{os.path.isdir(file_path)}")
    print()
    
    # 使用pathlib模块（推荐）
    print("使用pathlib模块（推荐）：")
    file_path = Path("sample.txt")
    print(f"文件路径：{file_path}")
    print(f"绝对路径：{file_path.absolute()}")
    print(f"文件名：{file_path.name}")
    print(f"文件词干：{file_path.stem}")
    print(f"文件扩展名：{file_path.suffix}")
    print(f"父目录：{file_path.parent}")
    print(f"文件存在：{file_path.exists()}")
    print(f"是否为文件：{file_path.is_file()}")
    print(f"是否为目录：{file_path.is_dir()}")
    print()
    
    # 4. 文件和目录管理
    print("4. 文件和目录管理")
    print("-" * 30)
    
    # 创建目录
    test_dir = Path("test_directory")
    test_dir.mkdir(exist_ok=True)
    print(f"创建目录：{test_dir}")
    
    # 创建嵌套目录
    nested_dir = Path("test_directory/nested/deep")
    nested_dir.mkdir(parents=True, exist_ok=True)
    print(f"创建嵌套目录：{nested_dir}")
    
    # 复制文件
    source_file = Path("sample.txt")
    destination_file = test_dir / "copied_sample.txt"
    shutil.copy2(source_file, destination_file)
    print(f"复制文件：{source_file} -> {destination_file}")
    
    # 移动文件
    moved_file = test_dir / "moved_sample.txt"
    shutil.move(str(destination_file), str(moved_file))
    print(f"移动文件：{destination_file} -> {moved_file}")
    
    # 列出目录内容
    print(f"\n目录 {test_dir} 的内容：")
    for item in test_dir.iterdir():
        item_type = "目录" if item.is_dir() else "文件"
        print(f"  {item.name} ({item_type})")
    
    # 递归列出所有文件
    print(f"\n递归列出所有文件：")
    for item in test_dir.rglob("*"):
        if item.is_file():
            print(f"  {item.relative_to(test_dir)}")
    print()
    
    # 5. 文件属性和元数据
    print("5. 文件属性和元数据")
    print("-" * 30)
    
    file_path = Path("sample.txt")
    if file_path.exists():
        stat_info = file_path.stat()
        print(f"文件大小：{stat_info.st_size} 字节")
        print(f"创建时间：{datetime.fromtimestamp(stat_info.st_ctime)}")
        print(f"修改时间：{datetime.fromtimestamp(stat_info.st_mtime)}")
        print(f"访问时间：{datetime.fromtimestamp(stat_info.st_atime)}")
        print(f"文件权限：{oct(stat_info.st_mode)}")
    print()
    
    # 6. 文件搜索和匹配
    print("6. 文件搜索和匹配")
    print("-" * 30)
    
    # 创建一些测试文件
    test_files = ["test1.txt", "test2.py", "data.json", "config.xml"]
    for file in test_files:
        Path(file).touch()
    
    # 使用glob模块搜索文件
    print("使用glob搜索文件：")
    txt_files = glob.glob("*.txt")
    print(f"所有.txt文件：{txt_files}")
    
    py_files = glob.glob("*.py")
    print(f"所有.py文件：{py_files}")
    
    # 使用pathlib搜索文件
    print("\n使用pathlib搜索文件：")
    current_dir = Path(".")
    for pattern in ["*.txt", "*.py", "*.json"]:
        files = list(current_dir.glob(pattern))
        print(f"{pattern}文件：{[f.name for f in files]}")
    print()
    
    # 7. 不同编码的处理
    print("7. 不同编码的处理")
    print("-" * 30)
    
    # 创建包含中文的文件
    chinese_text = "你好，世界！\n这是一个测试文件。\n包含中文字符。"
    
    # UTF-8编码
    with open("chinese_utf8.txt", "w", encoding="utf-8") as file:
        file.write(chinese_text)
    
    # GBK编码
    with open("chinese_gbk.txt", "w", encoding="gbk") as file:
        file.write(chinese_text)
    
    # 读取不同编码的文件
    print("读取UTF-8编码文件：")
    with open("chinese_utf8.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
    
    print("读取GBK编码文件：")
    with open("chinese_gbk.txt", "r", encoding="gbk") as file:
        content = file.read()
        print(content)
    
    # 编码转换
    print("编码转换：")
    with open("chinese_gbk.txt", "r", encoding="gbk") as file:
        content = file.read()
    
    with open("chinese_converted.txt", "w", encoding="utf-8") as file:
        file.write(content)
    
    print("已将GBK编码文件转换为UTF-8编码")
    print()
    
    # 8. 二进制文件操作
    print("8. 二进制文件操作")
    print("-" * 30)
    
    # 创建二进制数据
    binary_data = bytes([0x48, 0x65, 0x6C, 0x6C, 0x6F])  # "Hello"
    
    # 写入二进制文件
    with open("binary_file.bin", "wb") as file:
        file.write(binary_data)
        file.write(b" World!")
    
    # 读取二进制文件
    with open("binary_file.bin", "rb") as file:
        data = file.read()
        print(f"二进制数据：{data}")
        print(f"转换为字符串：{data.decode('utf-8')}")
    
    # 处理图片等二进制文件（模拟）
    print("\n处理二进制文件（模拟）：")
    sample_binary = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'  # PNG文件头
    
    with open("sample_image.png", "wb") as file:
        file.write(sample_binary)
    
    with open("sample_image.png", "rb") as file:
        header = file.read(16)
        print(f"文件头：{header}")
        print(f"是否为PNG文件：{header.startswith(b'\\x89PNG')}")
    print()
    
    # 9. 临时文件和安全操作
    print("9. 临时文件和安全操作")
    print("-" * 30)
    
    # 创建临时文件
    print("创建临时文件：")
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
        temp_file.write("这是临时文件的内容")
        temp_file_path = temp_file.name
        print(f"临时文件路径：{temp_file_path}")
    
    # 读取临时文件
    with open(temp_file_path, 'r') as file:
        content = file.read()
        print(f"临时文件内容：{content}")
    
    # 删除临时文件
    os.unlink(temp_file_path)
    print("已删除临时文件")
    
    # 使用临时目录
    print("\n使用临时目录：")
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"临时目录：{temp_dir}")
        
        # 在临时目录中创建文件
        temp_file_path = Path(temp_dir) / "temp_file.txt"
        with open(temp_file_path, 'w') as file:
            file.write("临时目录中的文件")
        
        print(f"临时文件：{temp_file_path}")
        print(f"文件存在：{temp_file_path.exists()}")
    
    print("临时目录已自动清理")
    print()
    
    # 10. 文件处理工具函数
    print("10. 文件处理工具函数")
    print("-" * 30)
    
    def count_lines(file_path):
        """计算文件行数"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return sum(1 for _ in file)
        except Exception as e:
            print(f"读取文件时出错：{e}")
            return 0
    
    def count_words(file_path):
        """计算文件词数"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                words = content.split()
                return len(words)
        except Exception as e:
            print(f"读取文件时出错：{e}")
            return 0
    
    def count_characters(file_path):
        """计算文件字符数"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                return len(content)
        except Exception as e:
            print(f"读取文件时出错：{e}")
            return 0
    
    def file_info(file_path):
        """获取文件信息"""
        path = Path(file_path)
        if not path.exists():
            return f"文件 {file_path} 不存在"
        
        lines = count_lines(file_path)
        words = count_words(file_path)
        characters = count_characters(file_path)
        size = path.stat().st_size
        
        return f"""文件信息：{file_path}
大小：{size} 字节
行数：{lines}
词数：{words}
字符数：{characters}"""
    
    # 测试工具函数
    print("文件分析工具：")
    print(file_info("sample.txt"))
    print()
    
    # 11. 批量文件操作
    print("11. 批量文件操作")
    print("-" * 30)
    
    def batch_rename(directory, old_pattern, new_pattern):
        """批量重命名文件"""
        dir_path = Path(directory)
        if not dir_path.exists():
            print(f"目录 {directory} 不存在")
            return
        
        count = 0
        for file_path in dir_path.glob(old_pattern):
            if file_path.is_file():
                new_name = file_path.name.replace(old_pattern.replace('*', ''), new_pattern.replace('*', ''))
                new_path = file_path.parent / new_name
                file_path.rename(new_path)
                print(f"重命名：{file_path.name} -> {new_path.name}")
                count += 1
        
        print(f"总共重命名了 {count} 个文件")
    
    def batch_copy(source_pattern, destination_dir):
        """批量复制文件"""
        dest_path = Path(destination_dir)
        dest_path.mkdir(exist_ok=True)
        
        count = 0
        for file_path in Path(".").glob(source_pattern):
            if file_path.is_file():
                dest_file = dest_path / file_path.name
                shutil.copy2(file_path, dest_file)
                print(f"复制：{file_path} -> {dest_file}")
                count += 1
        
        print(f"总共复制了 {count} 个文件")
    
    # 测试批量操作
    print("批量复制.txt文件：")
    batch_copy("*.txt", "txt_backup")
    print()
    
    # 12. 文件监控和处理
    print("12. 文件监控和处理")
    print("-" * 30)
    
    def monitor_directory(directory, callback):
        """监控目录变化（简单版本）"""
        dir_path = Path(directory)
        if not dir_path.exists():
            print(f"目录 {directory} 不存在")
            return
        
        # 获取初始文件列表
        initial_files = set(dir_path.iterdir())
        
        print(f"开始监控目录：{directory}")
        print(f"初始文件数量：{len(initial_files)}")
        
        # 这里只是一个简单的演示，实际应用中可能需要使用watchdog等库
        import time
        for i in range(3):  # 模拟监控3次
            time.sleep(0.1)
            current_files = set(dir_path.iterdir())
            
            new_files = current_files - initial_files
            deleted_files = initial_files - current_files
            
            if new_files:
                for file_path in new_files:
                    callback(f"新文件：{file_path.name}")
            
            if deleted_files:
                for file_path in deleted_files:
                    callback(f"删除文件：{file_path.name}")
            
            initial_files = current_files
    
    def file_change_handler(message):
        """文件变化处理器"""
        print(f"[监控] {message}")
    
    # 创建一个测试文件来演示监控
    test_file = Path("monitor_test.txt")
    test_file.touch()
    
    # 简单的监控演示
    monitor_directory(".", file_change_handler)
    
    # 清理测试文件
    if test_file.exists():
        test_file.unlink()
    print()
    
    # 13. 文件压缩和解压
    print("13. 文件压缩和解压")
    print("-" * 30)
    
    import zipfile
    
    # 创建压缩文件
    with zipfile.ZipFile("example.zip", "w") as zip_file:
        zip_file.write("sample.txt", "sample.txt")
        zip_file.write("output.txt", "output.txt")
        zip_file.writestr("info.txt", "这是在压缩文件中创建的文本")
    
    print("已创建压缩文件 example.zip")
    
    # 查看压缩文件内容
    with zipfile.ZipFile("example.zip", "r") as zip_file:
        print("压缩文件内容：")
        for file_info in zip_file.infolist():
            print(f"  {file_info.filename} ({file_info.file_size} 字节)")
    
    # 解压文件
    extract_dir = Path("extracted")
    extract_dir.mkdir(exist_ok=True)
    
    with zipfile.ZipFile("example.zip", "r") as zip_file:
        zip_file.extractall(extract_dir)
    
    print(f"已解压到目录：{extract_dir}")
    print()
    
    # 14. 清理临时文件
    print("14. 清理临时文件")
    print("-" * 30)
    
    temp_files = [
        "sample.txt", "output.txt", "chinese_utf8.txt", "chinese_gbk.txt",
        "chinese_converted.txt", "binary_file.bin", "sample_image.png",
        "test1.txt", "test2.py", "data.json", "config.xml", "example.zip"
    ]
    
    cleaned_count = 0
    for file_name in temp_files:
        file_path = Path(file_name)
        if file_path.exists():
            file_path.unlink()
            cleaned_count += 1
    
    # 清理目录
    temp_dirs = ["test_directory", "txt_backup", "extracted"]
    for dir_name in temp_dirs:
        dir_path = Path(dir_name)
        if dir_path.exists():
            shutil.rmtree(dir_path)
            cleaned_count += 1
    
    print(f"已清理 {cleaned_count} 个临时文件和目录")
    print()
    
    print("文件操作最佳实践：")
    print("1. 总是使用with语句打开文件")
    print("2. 明确指定文件编码")
    print("3. 使用pathlib进行路径操作")
    print("4. 处理可能的异常")
    print("5. 及时关闭文件资源")
    print("6. 使用临时文件处理敏感数据")
    print("7. 备份重要文件")
    print("8. 验证文件操作结果")
    print()
    
    print("=== 文件操作演示完成 ===")


if __name__ == "__main__":
    main() 