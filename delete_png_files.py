#!/usr/bin/env python3
"""
删除指定目录中的所有 PNG 图片
"""
import os
from pathlib import Path

def delete_png_files(input_dir):
    """
    删除目录中的所有 PNG 文件
    
    Args:
        input_dir: 输入目录路径
    """
    input_path = Path(input_dir)
    
    # 获取所有 PNG 文件
    png_files = list(input_path.glob('*.png'))
    
    if not png_files:
        print("未找到 PNG 文件")
        return
    
    print(f"找到 {len(png_files)} 个 PNG 文件")
    print("开始删除...")
    
    success_count = 0
    error_count = 0
    
    for png_file in png_files:
        try:
            # 删除文件
            os.remove(png_file)
            success_count += 1
            print(f"✓ 已删除: {png_file.name}")
            
        except Exception as e:
            error_count += 1
            print(f"✗ 删除失败: {png_file.name} - {str(e)}")
    
    print(f"\n删除完成！成功: {success_count}, 失败: {error_count}")

if __name__ == "__main__":
    # 设置图片目录
    images_dir = r"D:\code\caster-pdf\images"
    
    # 执行删除
    delete_png_files(images_dir)
