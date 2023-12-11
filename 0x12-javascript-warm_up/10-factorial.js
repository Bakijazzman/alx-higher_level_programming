#!/usr/bin/node
const num = parseInt(process.argv[2]);
function fact (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}
const result = fact(num);
console.log(result);
