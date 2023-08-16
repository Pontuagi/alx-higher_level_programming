#!/usr/bin/node

/*
 * Class Rectangle that defines rectangle
 * Constructor takes 2 arguments w and h
 * If w or h is equal to 0 or not a positive integer, an empty object is created
 */
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
