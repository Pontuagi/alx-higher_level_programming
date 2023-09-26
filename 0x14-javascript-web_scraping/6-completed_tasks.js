#!/usr/bin/node

/*
 * A script that computes the number of tasks completed by user id
 */
const request = require('request');

// Check if the user provided the API URL as an argument
if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

// Get the API URL from the command line argument
const apiUrl = process.argv[2];

// Make a GET request to the API to retrieve the task data
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error making GET request:', error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
  } else {
    try {
      const tasks = JSON.parse(body);

      // Initialize an object to store the count of completed tasks for each user
      const userTaskCount = {};

      // Loop through the tasks and count completed tasks for each user
      tasks.forEach((task) => {
        if (task.completed) {
          if (userTaskCount[task.userId]) {
            userTaskCount[task.userId]++;
          } else {
            userTaskCount[task.userId] = 1;
          }
        }
      });

      // Print the number of completed tasks for each user
      for (const userId in userTaskCount) {
        console.log(`'${userId}': ${userTaskCount[userId]}`);
      }
    } catch (parseError) {
      console.error('Error parsing API response:', parseError);
    }
  }
});
