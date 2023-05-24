#!/usr/bin/node
// A script that prints all characters of a Star Wars movie:

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const charactersUrls = movieData.characters;

      // Helper function to fetch character data
      const fetchCharacterData = (characterUrl) => {
        return new Promise((resolve, reject) => {
          request(characterUrl, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              if (response.statusCode === 200) {
                const characterData = JSON.parse(body);
                resolve(characterData.name);
              } else {
                reject(`Request failed with status code: ${response.statusCode}`);
              }
            }
          });
        });
      };

      // Fetch character data for each character URL
      Promise.all(charactersUrls.map(fetchCharacterData))
        .then((characterNames) => {
          characterNames.forEach((name) => {
            console.log(name);
          });
        })
        .catch((error) => {
          console.error(error);
        });
    } else {
      console.error(`Request failed with status code: ${response.statusCode}`);
    }
  }
});
