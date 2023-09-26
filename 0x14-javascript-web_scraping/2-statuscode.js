#!/usr/bin/node

/*
 * A script that displays the status code of a GET request
 */
const request = require('request');

// Check Url argument
if (process.argv.length !== 3) {
  console.error('Usage: ./3-statuscode.js <URL>');
  process.exit(1);
}

// Get the url from command line argument
const url = process.argv[2];

// Make a get request
request.get(url, (error, response) => {
  if (error) {
    console.error('Error making Get Request:', error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
