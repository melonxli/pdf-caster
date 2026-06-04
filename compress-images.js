import fs from 'fs';
import path from 'path';
import sharp from 'sharp';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

async function compressImages(dir) {
  const items = fs.readdirSync(dir);
  const webpFiles = items.filter(item => /\.webp$/i.test(item));
  
  console.log(`找到 ${webpFiles.length} 个 WebP 文件\n`);
  
  let totalOriginal = 0;
  let totalNew = 0;
  
  for (const item of webpFiles) {
    const fullPath = path.join(dir, item);
    const originalSize = fs.statSync(fullPath).size;
    totalOriginal += originalSize;
    
    try {
      await sharp(fullPath)
        .webp({ quality: 90, effort: 4 })
        .toFile(fullPath + '.tmp');
      
      fs.unlinkSync(fullPath);
      fs.renameSync(fullPath + '.tmp', fullPath);
      
      const newSize = fs.statSync(fullPath).size;
      totalNew += newSize;
      
      const saved = ((originalSize - newSize) / originalSize * 100).toFixed(1);
      console.log(`${item}: ${(originalSize / 1024).toFixed(1)}KB -> ${(newSize / 1024).toFixed(1)}KB (节省 ${saved}%)`);
    } catch (err) {
      console.error(`Error processing ${item}: ${err.message}`);
      if (fs.existsSync(fullPath + '.tmp')) {
        try { fs.unlinkSync(fullPath + '.tmp'); } catch {}
      }
    }
  }
  
  if (webpFiles.length > 0) {
    console.log(`\n总统计: ${(totalOriginal / 1024 / 1024).toFixed(2)}MB -> ${(totalNew / 1024 / 1024).toFixed(2)}MB`);
    console.log(`总共节省: ${((1 - totalNew / totalOriginal) * 100).toFixed(1)}%`);
  }
}

const targetDir = path.join(__dirname, 'images');
console.log('开始压缩 images 文件夹中的图片...\n');
compressImages(targetDir).then(() => console.log('\n压缩完成!'));
