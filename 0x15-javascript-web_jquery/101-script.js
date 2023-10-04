/*
 * JavaScript script that adds, removes and clears LI elements from a list
 * when the user clicks
 */

// Wait for the document to be fully loaded
$(document).ready(function () {
  // Add a click event handler to DIV#add_item
  $('#add_item').click(function () {
    // Create a new <li> element
    const newItem = $('<li>Item</li>');

    // Add the new <li> element to UL.my_list
    $('ul.my_list').append(newItem);
  });

  // Add a click event handler to DIV#remove_item
  $('#remove_item').click(function () {
    // Remove the last <li> element from UL.my_list
    $('ul.my_list li:last-child').remove();
  });

  // Add a click event handler to DIV#clear_list
  $('#clear_list').click(function () {
    // Remove all <li> elements from UL.my_list
    $('ul.my_list').empty();
  });
});
