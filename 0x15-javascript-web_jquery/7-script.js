#!/usr/bin/node

/*
 * JavaScript script that fetches the character name from
 * this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
 */

// Wait for the document to be fully loaded
$(document).ready(function () {
  // Make an AJAX GET request to fetch the character data
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      // Extract the character name from the response
      const characterName = data.name;

      // Display the character name in the HTML tag DIV#character
      $('#character').text(characterName);
    },
    error: function () {
      // Handle errors if the request fails
      console.error('Failed to fetch character data.');
    }
  });
});
