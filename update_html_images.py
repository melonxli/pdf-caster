#!/usr/bin/env python3
"""
将 HTML 文件中的 .png 图片引用替换为 .webp
"""
import re

def update_image_references(html_file):
    """
    更新 HTML 文件中的图片引用
    
    Args:
        html_file: HTML 文件路径
    """
    # 读取文件
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 统计 PNG 引用数量
    png_count = content.count('.png')
    
    if png_count == 0:
        print("未找到 PNG 图片引用")
        return
    
    print(f"找到 {png_count} 个 PNG 图片引用")
    
    # 将 .png 替换为 .webp
    new_content = content.replace('.png', '.webp')
    
    # 统计替换后的 WebP 引用数量
    webp_count = new_content.count('.webp')
    print(f"替换为 {webp_count} 个 WebP 图片引用")
    
    # 保存文件
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ 已更新 HTML 文件: {html_file}")

if __name__ == "__main__":
    # 设置 HTML 文件路径
    html_file = r"D:\code\caster-pdf\index.html"
    
    # 执行更新
    update_image_references(html_file)
