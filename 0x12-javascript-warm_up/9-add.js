#!/usr/bin/node

/*
 * Script that prints the addition of 2 integers
 */
const { argv } = require('process');

function add (a, b) {
  return (a + b);
}

const sum1 = add(Number(argv[2]), Number(argv[3]));
console.log(sum1);
