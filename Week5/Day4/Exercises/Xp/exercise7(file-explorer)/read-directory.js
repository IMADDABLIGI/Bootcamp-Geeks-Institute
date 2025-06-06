import { readdir } from 'fs/promises';

try {
  const files = await readdir('.');
  console.log('Files in the current directory:');
  files.forEach(file => console.log(file));
} catch (error) {
  console.error('Error reading directory:', error);
}
