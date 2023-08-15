#!/usr/bin/node

/*
 * a script that prints 'My number: <first argument converted in integer>'
 * if the first argument can be converted to an integer
 */
const { argv } = require('process');


if (!isNaN(argv[2])) {
  console.log('My number: ' + Number(argv[2]));
} else {
  console.log('Not a number');
}
