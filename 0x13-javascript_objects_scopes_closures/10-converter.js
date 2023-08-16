#!/usr/bin/node

/*
 * A function that converts a number from base 10 to another base passed as argument
 */
exports.converter = function (base) {
  if (base <= 1) {
    return;
  }

  function convertToBase (number) {
    if (number >= base) {
      convertToBase(Math.floor(number / base));
    }
    process.stdout.write((number % base).toString());
  }

  return convertToBase;
};
