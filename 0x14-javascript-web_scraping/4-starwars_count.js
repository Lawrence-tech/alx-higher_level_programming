#!/usr/bin/node
/* script that prints the number of movies where the
   character “Wedge Antilles” is present.
   */

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

// Make an HTTP GET request to the Star Wars API films endpoint
request(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurred during the request, log the error object
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    // Filter the films where "Wedge Antilles" character is present
    const filteredFilms = films.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
    // Print the number of filtered films
    console.log(filteredFilms.length);
  }
});
