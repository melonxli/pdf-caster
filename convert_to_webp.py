#!/usr/bin/env python3
"""
将指定目录中的所有 PNG 图片转换为 WebP 格式
"""
import os
from PIL import Image
from pathlib import Path

def convert_png_to_webp(input_dir, quality=90):
    """
    将目录中的所有 PNG 图片转换为 WebP 格式
    
    Args:
        input_dir: 输入目录路径
        quality: WebP 质量 (1-100)
    """
    input_path = Path(input_dir)
    
    # 获取所有 PNG 文件
    png_files = list(input_path.glob('*.png'))
    
    if not png_files:
        print("未找到 PNG 文件")
        return
    
    print(f"找到 {len(png_files)} 个 PNG 文件")
    print("开始转换...")
    
    success_count = 0
    error_count = 0
    
    for png_file in png_files:
        try:
            # 打开 PNG 图片
            img = Image.open(png_file)
            
            # 转换为 WebP
            webp_file = png_file.with_suffix('.webp')
            img.save(webp_file, 'WEBP', quality=quality)
            
            success_count += 1
            print(f"✓ 已转换: {png_file.name} -> {webp_file.name}")
            
        except Exception as e:
            error_count += 1
            print(f"✗ 转换失败: {png_file.name} - {str(e)}")
    
    print(f"\n转换完成！成功: {success_count}, 失败: {error_count}")
    
    if success_count > 0:
        print(f"\n提示: 您可以选择删除原始 PNG 文件，仅保留 WebP 文件")

if __name__ == "__main__":
    # 设置图片目录
    images_dir = r"D:\code\caster-pdf\images"
    
    # 执行转换
    convert_png_to_webp(images_dir, quality=90)
