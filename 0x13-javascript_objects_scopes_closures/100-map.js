#!/usr/bin/node

/*
 * a script that imports an array and computes a new array.\
 */

// Import the list from the file 100-data.js
const { list } = require('./100-data');

// Compute a new array using map
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log(list);
console.log(newList);
