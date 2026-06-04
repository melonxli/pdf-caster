#!/usr/bin/env python3
"""
压缩 WebP 图片 - 激进压缩模式
使用质量80，追求更小的文件大小
"""
import os
from PIL import Image
from pathlib import Path

images_dir = Path(r"D:\code\caster-pdf\images")
webp_files = list(images_dir.glob("*.webp"))

print(f"找到 {len(webp_files)} 个 WebP 文件")
print("使用质量 80 进行激进压缩...\n")

total_before = 0
total_after = 0
success = 0
failed = 0

for i, f in enumerate(webp_files, 1):
    try:
        size_before = os.path.getsize(f)
        total_before += size_before
        
        # 读取并保存，使用质量80
        img = Image.open(f)
        tmp_file = f.parent / f"{f.stem}_tmp.webp"
        img.save(tmp_file, 'WEBP', quality=80)
        img.close()
        
        size_after = os.path.getsize(tmp_file)
        total_after += size_after
        
        # 替换原文件
        os.remove(f)
        tmp_file.rename(f)
        
        saved = 100 * (1 - size_after / size_before)
        print(f"[{i}/{len(webp_files)}] ✓ {f.name}: {size_before//1024}KB -> {size_after//1024}KB (节省 {saved:.1f}%)")
        success += 1
        
    except Exception as e:
        print(f"[{i}/{len(webp_files)}] ✗ {f.name}: {str(e)[:60]}")
        failed += 1

print(f"\n{'='*60}")
print(f"压缩完成!")
print(f"  成功: {success} 个文件")
print(f"  失败: {failed} 个文件")
if success > 0:
    print(f"  原始大小: {total_before//1024//1024:.2f} MB")
    print(f"  压缩后: {total_after//1024//1024:.2f} MB")
    print(f"  总共节省: {100*(1-total_after/total_before):.1f}%")
print(f"{'='*60}")
