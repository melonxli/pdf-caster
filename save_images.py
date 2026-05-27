import base64
import os

# 创建images文件夹
images_dir = "d:/code/caster-pdf/images"
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

# 第一张图片（条纹带盖固定脚杯）
image1_data = """
在这里插入第一张图片的base64数据（用户提供的第一张图片）
"""

# 第二张图片（碳钢固定脚杯）
image2_data = """
在这里插入第二张图片的base64数据（用户提供的第二张图片）
"""

# 保存第一张图片
if image1_data.strip():
    with open(f"{images_dir}/page_02.jpg", "wb") as f:
        f.write(base64.b64decode(image1_data))
    print("保存了第02页图片")

# 保存第二张图片
if image2_data.strip():
    with open(f"{images_dir}/page_03.jpg", "wb") as f:
        f.write(base64.b64decode(image2_data))
    print("保存了第03页图片")

print("\n请手动将您的图片保存为：")
print("- d:/code/caster-pdf/images/page_02.jpg")
print("- d:/code/caster-pdf/images/page_03.jpg")
