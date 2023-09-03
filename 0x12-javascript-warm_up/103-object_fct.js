#!/usr/bin/node

/*
 * Update script by adding new function incr that increments the integer value.
 */
const myObject = {
  type: 'object',
  value: 12
};

// Define the incr function
myObject.incr = function incr () {
  this.value++;
};

console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
