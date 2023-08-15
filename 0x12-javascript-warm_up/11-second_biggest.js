#!/usr/bin/node

/*
 * Script that searches for the second biggest integer in the list of arguments
 */
const { argv } = require('process');

function secondLargest (numbers) {
  if (numbers.length <= 1) {
    return (0);
  }

  const largest = Math.max(...numbers);
  let secondLargestNo = -Infinity;

  for (const num of numbers) {
    if (num !== largest && num > secondLargestNo) {
      secondLargestNo = num;
    }
  }

  return (secondLargestNo);
}

const argumentsList = argv.slice(2).map(Number);
const secondLargestInList = secondLargest(argumentsList);
console.log(secondLargestInList);
