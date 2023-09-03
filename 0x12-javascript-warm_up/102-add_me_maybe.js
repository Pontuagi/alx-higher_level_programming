#!/usr/bin/node

/*
 * A function that increments and calls a function
 */
function addMeMaybe(number, theFunction) {
  // Increment the number
  number++;

  // Call the provided function with the incremented number as an argument
  theFunction(number);
}

// Export the function to make it visible from outside
module.exports.addMeMaybe = addMeMaybe;
