import os
from PIL import Image, ImageDraw, ImageFont
import random

def create_placeholder_image(text, width, height, output_path, bg_color=(240, 240, 240)):
    """创建占位图片"""
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # 绘制边框
    draw.rectangle([0, 0, width-1, height-1], outline=(200, 200, 200), width=2)

    # 添加文字
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()

    # 计算文字位置
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    draw.text((x, y), text, fill=(150, 150, 150), font=font)

    img.save(output_path)
    print(f"创建占位图片: {output_path}")

def create_dimension_diagram(text, width, height, output_path):
    """创建尺寸图"""
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 绘制边框
    draw.rectangle([0, 0, width-1, height-1], outline=(0, 0, 0), width=1)

    # 添加尺寸标注
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()

    # 添加尺寸文字
    draw.text((10, 10), "尺寸图", fill=(100, 100, 100), font=font)
    draw.text((10, height - 30), text, fill=(100, 100, 100), font=font)

    img.save(output_path)
    print(f"创建尺寸图: {output_path}")

if __name__ == "__main__":
    # 创建images文件夹
    images_dir = "d:/code/caster-pdf/images"
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # 创建第02页的产品图和尺寸图
    create_placeholder_image("条纹带盖固定脚杯", 300, 250, f"{images_dir}/product_02.png")
    create_dimension_diagram("D-M-L1", 200, 250, f"{images_dir}/dimension_02.png")

    # 创建第03页的产品图和尺寸图
    create_placeholder_image("碳钢固定脚杯", 300, 250, f"{images_dir}/product_03.png")
    create_dimension_diagram("D-M-L1", 200, 250, f"{images_dir}/dimension_03.png")

    print("\n占位图片创建完成！请将实际的产品图片替换到对应位置。")
