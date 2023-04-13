#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { // create empty object if w & h are <= 0
      this.width = w;
      this.height = h;
    }
  }

  print () { // an instance method that prints the rectangle using the char X
    for (let h = this.height; h > 0; h--) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
