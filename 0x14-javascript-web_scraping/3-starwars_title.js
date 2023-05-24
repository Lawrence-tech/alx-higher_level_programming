#!/usr/bin/node
/* A script that prints the title of a Star Wars movie where the episode
   number matches a given integer.
   */

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make an HTTP GET request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    // If an error occurred during the request, log the error object
    console.error(error);
  } else {
    // Parse the response body into a JavaScript object
    const movie = JSON.parse(body);
    // Print the title of the movie
    console.log(movie.title);
  }
});
