#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j = 0;
    const first = this.height;
    const second = this.width;
    while (i < first) {
      let show = '';
      j = 0;
      while (j < second) {
        show += 'X';
        j++;
      }
      console.log(show);
      i++;
    }
  }
}
module.exports = Rectangle;
