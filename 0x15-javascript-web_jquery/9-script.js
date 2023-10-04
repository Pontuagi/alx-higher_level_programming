/*
 * a JavaScript script that fetches from
 * https://fourtonfish.com/hellosalut/?lang=fr and
 * displays the value of hello from that fetch in the HTML tag DIV#hello
 */
// Wait for the document to be fully loaded
$(document).ready(function () {
  // Make an AJAX GET request to fetch the translation
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      // Extract the translation from the response
      const translation = data.hello;

      // Display the translation in the HTML tag DIV#hello
      $('#hello').text(translation);
    },
    error: function () {
      // Handle errors if the request fails
      console.error('Failed to fetch translation data.');
    }
  });
});
