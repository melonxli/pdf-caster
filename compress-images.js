import fs from 'fs';
import path from 'path';
import sharp from 'sharp';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

async function compressImages(dir) {
  const items = fs.readdirSync(dir);
  
  for (const item of items) {
    const fullPath = path.join(dir, item);
    const stat = fs.statSync(fullPath);
    
    if (stat.isDirectory()) {
      await compressImages(fullPath);
    } else if (/\.(jpg|jpeg|png)$/i.test(item)) {
      const originalSize = stat.size;
      
      try {
        await sharp(fullPath)
          .png({ quality: 90, compressionLevel: 9 })
          .toFile(fullPath + '.tmp');
        
        fs.unlinkSync(fullPath);
        fs.renameSync(fullPath + '.tmp', fullPath);
        
        const newStat = fs.statSync(fullPath);
        const saved = ((originalSize - newStat.size) / originalSize * 100).toFixed(1);
        console.log(`${item}: ${(originalSize / 1024).toFixed(1)}KB -> ${(newStat.size / 1024).toFixed(1)}KB (节省 ${saved}%)`);
      } catch (err) {
        console.error(`Error processing ${item}: ${err.message}`);
      }
    }
  }
}

const targetDir = path.join(__dirname, 'images');
console.log('开始压缩图片...\n');
compressImages(targetDir).then(() => console.log('\n完成!'));
