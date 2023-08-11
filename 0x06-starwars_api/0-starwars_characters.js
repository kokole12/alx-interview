#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const getFromPeoople = (characters, index) => {
  if (characters.length === index) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      getFromPeoople(characters, index + 1);
    }
  });
};
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const data = JSON.parse(body).characters;

  // for (const personUrl of data) {
  //   request.get(personUrl, (error, response, body) => {
  //     if (error) {
  //       console.log(error);
  //     }
  //     const names = JSON.parse(body).name;
  //     console.log(names);
  //   });
  // }
  getFromPeoople(data, 0);
});
