#!/usr/bin/node
const num = process.argv[2];
const conv = parseInt(num);
if (!isNaN(conv)) {
  console.log('My number: ' + conv);
} else {
  console.log('Not a number');
}
