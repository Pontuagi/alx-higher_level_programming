#!/usr/bin/node

/*
 * JavaScript script that updates the text color of the <header> element
 * to red (#FF0000):
 */

document.addEventListener('DOMContentLoaded', function() {
  // Select the <header> element using document.querySelector
  const headerElement = document.querySelector('header');

  // Update the text color to red (#FF0000)
  headerElement.style.color = '#FF0000';
});
