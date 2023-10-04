#!/usr/bin/node

/*
 * a JavaScript script that adds a <li> element to a list when the user
 * clicks on the tag DIV#add_item
 */

// Wait for the document to be fully loaded
$(document).ready(function () {
  // Click event handler
  $('#add_item').click(function () {
    const newItem = $('<li>Item</li>');

    $('UL.my_list').append(newItem);
  });
});
