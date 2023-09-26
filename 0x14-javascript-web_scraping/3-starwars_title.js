#!/usr/bin/node

/*
 * A script that prints the title of starwars movie matching a given number
 */
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <int>');
  process.exit(1);
}

const movieId = process.argv[2];

// Creating url from movie id
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// make a get request to the API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error making get request:', error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with ${response.statusCode}`);
  } else {
    try {
      const movieData = JSON.parse(body);
      console.log(`${movieData.title}`);
    } catch (parseError) {
      console.error('Error parsing API response:', parseError);
    }
  }
});
