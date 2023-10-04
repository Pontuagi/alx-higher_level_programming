#!/usr/bin/node

/*
 * JavaScript script that updates the text of the <header> element
 * to New Header!!! when the user clicks on DIV#update_header
 */

// Wait for the document to be fully loaded
$(document).ready(function () {
  // Add a click event handler
  $('#update_header').click(function () {
    // Update the text of the <header>
    $('header').text('New Header!!!');
  });
});
