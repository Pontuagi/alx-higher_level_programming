#!/usr/bin/node

/*
 * A script that prints an array of strings in separate lines using a loop
 */

const array1 = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let i = 0;
while (i < array1.length) {
  console.log(array1[i]);
  i++;
}
