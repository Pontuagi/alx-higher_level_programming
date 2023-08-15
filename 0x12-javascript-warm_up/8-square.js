#!/usr/bin/node

/*
 * A script that prints a square
 */
const { argv } = require('process');

if (!argv[2] || isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const numberOfX = Number(argv[2]);

  for (let i = 0; i < numberOfX; i++) {
    console.log('X'.repeat(numberOfX));
  }
}
