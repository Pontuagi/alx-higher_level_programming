#!/usr/bin/node
/*
 * JavaScript script that fetches and prints how to say “Hello” depending
 * on the language
 */

// Wait for the document to be fully loaded
$(document).ready(function () {
  // Function to fetch and display the translation
  function fetchTranslation() {
    // Get the language code from INPUT#language_code
    const languageCode = $('#language_code').val();

    // Make an AJAX GET request to fetch the translation
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      method: 'POST',
      dataType: 'json',
      data: {
        lang: languageCode,
      },
      success: function (data) {
        // Extract the translation from the response
        const translation = data.hello;

        // Display the translation in the HTML tag DIV#hello
        $('#hello').text(translation);
      },
      error: function () {
        // Handle errors if the request fails
        console.error('Failed to fetch translation data.');
      },
    });
  }

  // Add a click event handler to INPUT#btn_translate
  $('#btn_translate').click(fetchTranslation);

  // Add a keypress event handler to INPUT#language_code
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      // If Enter key is pressed, fetch and display the translation
      fetchTranslation();
    }
  });
});
