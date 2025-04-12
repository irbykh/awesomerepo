import * as fs from 'fs';
import * as path from 'path';
import * as unzipper from 'unzipper';

console.log("Enter the path to the ZIP file:");
const zipFilePath = process.argv[2] || 'file.zip';
const extractPath = './extracted/';

fs.createReadStream(zipFilePath)
  .pipe(unzipper.Parse())
  .on('entry', entry => {
    const filePath = path.join(extractPath, entry.path);
    const resolvedPath = path.resolve(extractPath, entry.path);
    if (resolvedPath.startsWith(path.resolve(extractPath)) && entry.path.indexOf('..') === -1) {
      entry.pipe(fs.createWriteStream(filePath));
    } else {
      console.log('Skipping bad path:', entry.path);
    }
  })
  .on('error', (err) => {
    console.error('Extraction error:', err);
  })
  .on('finish', () => {
    console.log('Extraction complete.');
  });
