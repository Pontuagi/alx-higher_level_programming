#!/usr/bin/node

/*
 * a script that prints all characters of a Star Wars movie
 */
const request = require('request');

// Check if the user provided the correct number of arguments
if (process.argv.length !== 3) {
  console.error('Usage: ./100-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

// Get the Movie ID from the command line argument
const movieId = process.argv[2];

// Construct the API URL with the provided Movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error making GET request:', error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
  } else {
    try {
      const movieData = JSON.parse(body);

      // Print the character names
      movieData.characters.forEach((characterUrl) => {
        request.get(characterUrl, (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          }
        });
      });
    } catch (parseError) {
      console.error('Error parsing API response:', parseError);
    }
  }
});
