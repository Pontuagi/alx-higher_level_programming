#!/usr/bin/node

/*
 * JavaScript script that toggles the class of the <header> element
 * when the user clicks on the tag DIV#toggle_header
 */

// Wait for the document to fully load
$(document).ready(function () {
  // click event handler
  $('#toggle_header').click(function () {
    // toggle red and green classes
    $('header').toggleClass('red green');
  });
});
