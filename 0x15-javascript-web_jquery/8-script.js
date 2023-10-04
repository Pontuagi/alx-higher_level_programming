#!/usr/bin/node

/*
 * a JavaScript script that fetches and lists the title for all movies by using
 * this URL: https://swapi-api.alx-tools.com/api/films/?format=json
 */

// Wait for the document to be fully loaded
$(document).ready(function () {
  // Make an AJAX GET request to fetch the list of movies
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      // Extract the list of movies from the response
      const movies = data.results;

      // Select the UL#list_movies element
      const listMovies = $('#list_movies');

      // Loop through the movies and add each title to the list
      $.each(movies, function (index, movie) {
        const listItem = $('<li>' + movie.title + '</li>');
        listMovies.append(listItem);
      });
    },
    error: function () {
      // Handle errors if the request fails
      console.error('Failed to fetch movie data.');
    }
  });
});
