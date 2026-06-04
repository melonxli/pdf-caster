import os
from PIL import Image
from pathlib import Path

images_dir = Path(r"D:\code\caster-pdf\images")
webp_files = list(images_dir.glob('*.webp'))[:120]

print(f"开始压缩 {len(webp_files)} 张图片...")

total_before = 0
total_after = 0

for f in webp_files:
    try:
        size_before = os.path.getsize(f)
        total_before += size_before
        
        img = Image.open(f)
        tmp = f.with_suffix('.tmp')
        img.save(tmp, 'WEBP', quality=90, method=5)
        
        size_after = os.path.getsize(tmp)
        total_after += size_after
        
        os.remove(f)
        os.rename(tmp, f)
        
        print(f"{f.name}: {size_before//1024}KB->{size_after//1024}KB {100*(1-size_after/size_before):.1f}% saved")
        
    except Exception as e:
        print(f"Error with {f.name}: {e}")

print(f"\n总计:")
print(f"压缩前: {total_before//1024//1024} MB")
print(f"压缩后: {total_after//1024//1024} MB")
print(f"节省: {100*(1-total_after/total_before):.1f}%")
