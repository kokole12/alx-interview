#!/usr/bin/node
import request from 'request';
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const data = JSON.parse(body).characters;

  for (const person_url of data) {
    request.get(person_url, (error, response, body) => {
      if (error) {
        console.log(error);
      }
      const names = JSON.parse(body).name;
      console.log(names);
    });
  }
});
