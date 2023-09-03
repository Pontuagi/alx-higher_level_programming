#!/usr/bin/node

/*
 * a function that executes x times a function.
 */
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Export the function
module.exports.callMeMoby = callMeMoby;
