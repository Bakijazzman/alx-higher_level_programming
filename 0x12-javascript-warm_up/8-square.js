#!/usr/bin/node
const sqr = parseInt(process.argv[2]);
if (!isNaN(sqr)) {
  let i = 0;
  let num = 0;
  while (i < sqr) {
    let print = '';
    num = 0;
    while (num < sqr) {
      print += 'X';
      num++;
    }
    i++;
    console.log(print);
  }
} else {
  console.log('Missing Size');
}
