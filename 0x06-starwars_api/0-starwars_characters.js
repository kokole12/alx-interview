#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const data = JSON.parse(body).characters;

  for (const personUrl of data) {
    request.get(personUrl, (error, response, body) => {
      if (error) {
        console.log(error);
      }
      const names = JSON.parse(body).name;
      console.log(names);
    });
  }
});
