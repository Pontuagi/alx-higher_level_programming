#!/usr/bin/node

/*
 * a script that imports a dictionary of occurrences by user id
 * and computes a dictionary of user ids by occurrence.
 */

// Import the dictionary from the file 101-data.js
const { dict } = require('./101-data');

// Create a new dictionary for user ids by occurrence
const userIDsByOccurrence = {};

// Loop through the original dictionary to populate the new one
for (const userId in dict) {
  const occurrences = dict[userId];

  if (!userIDsByOccurrence[occurrences]) {
    userIDsByOccurrence[occurrences] = [];
  }

  userIDsByOccurrence[occurrences].push(userId);
}

// Print the new dictionary
console.log(userIDsByOccurrence);
