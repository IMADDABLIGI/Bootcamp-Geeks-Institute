import { readFile } from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export async function displayFileContent() {
  try {
    const filePath = path.join(__dirname, 'file-data.txt');
    const data = await readFile(filePath, 'utf8');
    console.log('File Content:\n', data);
  } catch (err) {
    console.error('Error reading file:', err.message);
  }
}
