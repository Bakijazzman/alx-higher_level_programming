#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  const arrayNew = [];
  while (len >= 0) {
    arrayNew[i] = list[len];
    i++;
    len--;
  }
  return arrayNew;
};
