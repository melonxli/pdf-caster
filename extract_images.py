import fitz
import os

def extract_images_from_pdf(pdf_path, output_dir):
    """从PDF中提取所有图片"""
    print(f"正在打开PDF: {pdf_path}")
    doc = fitz.open(pdf_path)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_count = 0

    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images(full=True)

        for img_index, img_info in enumerate(images):
            try:
                xref = img_info[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]

                # 保存图片
                image_name = f"page{page_num + 1}_img{img_index + 1}.{image_ext}"
                image_path = os.path.join(output_dir, image_name)

                with open(image_path, "wb") as f:
                    f.write(image_bytes)

                image_count += 1
                print(f"提取图片: {image_name} ({len(image_bytes) / 1024:.2f} KB)")
            except Exception as e:
                print(f"提取图片失败: {e}")

    doc.close()
    print(f"\n总共提取了 {image_count} 张图片")
    return image_count

if __name__ == "__main__":
    pdf_file = "d:/code/rock-caster/德胜画册 - 副本 OCR.pdf"
    output_directory = "d:/code/caster-pdf/images"

    extract_images_from_pdf(pdf_file, output_directory)
