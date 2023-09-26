#!/usr/bin/node

/*
 * A script that prints the number of movies where the character
 * 'Wedge Antilles' is present
 */
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <URL>');
  process.exit(1);
}

const movieUrl = process.argv[2];

request.get(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error making Get Request:', error);
  } else if (response.statusCode !== 200) {
    console.error(`Requet failed with ${response.statusCode} code`);
  } else {
    try {
      const filmsData = JSON.parse(body);
      const antillesMovies = filmsData.results.filter((film) => {
        return film.characters.includes(
          'https://swapi-api.alx-tools.com/api/people/18/');
      });
      console.log(`${antillesMovies.length}`);
    } catch (parseError) {
      console.error('Error parsing API response:', parseError);
    }
  }
});
