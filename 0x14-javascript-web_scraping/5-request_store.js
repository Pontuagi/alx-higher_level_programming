#!/usr/bin/node

/*
 * a script that gets the contents of a webpage and stores it in a file
 */
const request = require('request');
const fs = require('fs');

// Check the number of arguments
if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <URL> <outputFilePath>');
  process.exit(1);
}

// Get the URL and output file path from the command line arguments
const url = process.argv[2];
const outputFilePath = process.argv[3];

// Make a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error making GET request:', error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
  } else {
    // Write the response body to the specified file in UTF-8 encoding
    fs.writeFile(outputFilePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error('Error writing to the file:', writeError);
      }
    });
  }
});
