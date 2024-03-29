#!/usr/bin/node

/*
 * A class square that inherits from square of 5-square.js
 */
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  constructor (size) {
    super(size);
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
