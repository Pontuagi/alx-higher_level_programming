#!/usr/bin/node

/*
 * A script that reads and prints the content of a file
 */

const fs = require('fs');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <file_path');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
  } else {
    console.log(data);
  }
});
