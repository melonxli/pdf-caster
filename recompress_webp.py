#!/usr/bin/env python3
"""
重新压缩 WebP 图片，优化文件大小同时保持清晰度
"""
import os
from pathlib import Path
from PIL import Image

def recompress_webp_images(input_dir, quality=90, method=4):
    """
    重新压缩目录中的 WebP 图片
    
    Args:
        input_dir: 输入目录路径
        quality: WebP 质量 (1-100), 默认90以平衡清晰度和文件大小
        method: 压缩方法 (0-6), 0最快, 6最慢但压缩最好
    """
    input_path = Path(input_dir)
    
    # 获取所有 WebP 文件
    webp_files = list(input_path.glob('*.webp'))
    
    if not webp_files:
        print("未找到 WebP 文件")
        return
    
    print(f"找到 {len(webp_files)} 个 WebP 文件")
    print(f"开始重新压缩... (质量: {quality}, 压缩方法: {method})")
    
    success_count = 0
    error_count = 0
    total_original_size = 0
    total_new_size = 0
    
    for webp_file in webp_files:
        try:
            # 获取原始大小
            original_size = os.path.getsize(webp_file)
            total_original_size += original_size
            
            # 打开 WebP 图片
            img = Image.open(webp_file)
            
            # 重新保存为 WebP，使用指定的压缩参数
            temp_file = webp_file.with_suffix('.tmp.webp')
            img.save(temp_file, 'WEBP', quality=quality, method=method)
            
            # 获取新大小
            new_size = os.path.getsize(temp_file)
            total_new_size += new_size
            
            # 计算压缩率
            compression_ratio = 100 * (1 - new_size / original_size)
            
            # 替换原文件
            os.remove(webp_file)
            os.rename(temp_file, webp_file)
            
            success_count += 1
            print(f"✓ {webp_file.name}: {original_size/1024:.1f}KB -> {new_size/1024:.1f}KB ({compression_ratio:.1f}% 节省)")
            
        except Exception as e:
            error_count += 1
            print(f"✗ 压缩失败: {webp_file.name} - {str(e)}")
            # 清理临时文件
            if temp_file.exists():
                os.remove(temp_file)
    
    print(f"\n压缩完成！成功: {success_count}, 失败: {error_count}")
    
    if success_count > 0:
        original_total_mb = total_original_size / (1024 * 1024)
        new_total_mb = total_new_size / (1024 * 1024)
        total_savings = (1 - total_new_size / total_original_size) * 100
        
        print(f"\n总文件大小:")
        print(f"  原始大小: {original_total_mb:.2f} MB")
        print(f"  新大小: {new_total_mb:.2f} MB")
        print(f"  总共节省: {total_savings:.1f}% ({original_total_mb - new_total_mb:.2f} MB)")

if __name__ == "__main__":
    # 设置图片目录
    images_dir = r"D:\code\caster-pdf\images"
    
    # 执行重新压缩，使用质量95保证清晰度，方法4平衡速度和压缩效果
    recompress_webp_images(images_dir, quality=95, method=4)
