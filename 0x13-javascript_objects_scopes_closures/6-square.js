#!/usr/bin/node

const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    let i = 0;
    let j = 0;
    const first = this.height;
    const second = this.width;
    while (i < first) {
      let show = '';
      j = 0;
      while (j < second) {
        if (!c) {
          show += 'X';
          j++;
        } else {
          show += c;
          j++;
        }
      }
      console.log(show);
      i++;
    }
  }
}
module.exports = Square;
