import os
from PIL import Image
from pathlib import Path

images_dir = Path(r"D:\code\caster-pdf\images")
webp_files = list(images_dir.glob('*.webp'))[:3]

print(f"测试压缩 {len(webp_files)} 张图片...\n")

for f in webp_files:
    try:
        size_before = os.path.getsize(f)
        print(f"压缩前: {f.name} = {size_before//1024}KB")
        
        img = Image.open(f)
        tmp = f.with_suffix('.tmp.webp')
        img.save(tmp, 'WEBP', quality=90, method=4)
        
        size_after = os.path.getsize(tmp)
        saved_percent = 100 * (1 - size_after / size_before)
        
        print(f"压缩后: {size_after//1024}KB (节省 {saved_percent:.1f}%)")
        
        os.remove(tmp)
        print()
    except Exception as e:
        print(f"Error with {f.name}: {e}")
