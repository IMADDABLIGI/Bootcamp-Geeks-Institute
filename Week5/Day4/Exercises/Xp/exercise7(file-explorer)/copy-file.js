import { readFile, writeFile } from 'fs/promises';

try {
  const data = await readFile('source.txt', 'utf8');
  await writeFile('destination.txt', data);
  console.log('File copied successfully!');
} catch (error) {
  console.error('Error copying file:', error);
}
