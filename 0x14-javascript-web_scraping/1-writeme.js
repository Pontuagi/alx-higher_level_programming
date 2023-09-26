#!/usr/bin/node

/*
 * a script that write a text to a file
 */
const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <file_path> "<string_to_write>"');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error('Error writing to the file:', err);
  }
});
