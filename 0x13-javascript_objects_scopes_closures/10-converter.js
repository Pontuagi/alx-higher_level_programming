#!/usr/bin/node

/*
 * A function that converts a number from base 10 to another base passed as argument
 */
exports.converter = function (base) {
  const hexChars = '0123456789ABCDEF';
  function convertToBase(number, base) {
    if (number === 0) {
      return '';
    }
    const remainder = number % base;
    const quotient = Math.floor(number / base);
    return convertToBase(quotient, base) + hexChars[remainder];
  }

  return function (number) {
    if (base < 2 || base > 36) {
      throw new Error('Base should be between 2 and 36');
    }
    if (isNaN(number) || number < 0) {
      throw new Error('Number should be a positive integer');
    }

    return convertToBase(number, base);
  };
};
