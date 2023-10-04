#!/usr/bin/node

/*
 * a JavaScript script that adds the class red to the <header> element
 * when the user clicks on the tag DIV#red_header
 */

// Wait for the document to be fully loaded
$(document).ready(function () {
  const redHead = $('#red_header');
  const head = $('header');

  redHead.click(function () {
    head.addClass('red');
  });
});
