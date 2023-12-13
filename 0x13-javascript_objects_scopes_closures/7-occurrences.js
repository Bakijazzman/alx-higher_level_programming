#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let count = 0;
  const len = list.length;
  while (i < len) {
    if (list[i] === searchElement) {
      count++;
    } i++;
  }
  return count;
};
