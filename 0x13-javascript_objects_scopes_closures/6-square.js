#!/usr/bin/node

/*
 * A class square that inherits from square of 5-square.js
 */
const oldSquare = require('./5-square.js');

class Square extends oldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
