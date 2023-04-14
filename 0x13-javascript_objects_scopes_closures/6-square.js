#!/usr/bin/node

const SquarePar = require('./5-square');

module.exports = class Square extends SquarePar {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let h = this.height; h > 0; h--) {
      console.log(c.repeat(this.width));
    }
  }
};
