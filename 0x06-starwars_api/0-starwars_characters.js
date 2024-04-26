#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

/**
 * Fetches and prints all characters of a Star Wars movie.
 * @param {number} movieId - The ID of the Star Wars movie.
 */
function printMovieCharacters (movieId) {
  request(`${API_URL}/films/${movieId}/`, (err, _, body) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
    const charactersURLs = JSON.parse(body).characters;
    const characterNamesPromises = charactersURLs.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(characterNamesPromises)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.error(allErr));
  });
}

const movieId = process.argv[2];
if (!movieId || isNaN(movieId)) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

printMovieCharacters(movieId);
