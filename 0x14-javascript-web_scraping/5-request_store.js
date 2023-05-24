#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

// Make an HTTP GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    // If an error occurred during the request, log the error object
    console.error(error);
  } else if (response.statusCode !== 200) {
    // If the response status code is not 200 (OK), display an error message
    console.error(`Request failed with status code ${response.statusCode}`);
  } else {
    // Write the body response to the specified file
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
      if (err) {
        // If an error occurred while writing the file, log the error object
        console.error(err);
      } else {
        console.log(`Successfully saved the response to ${filePath}`);
      }
    });
  }
});
