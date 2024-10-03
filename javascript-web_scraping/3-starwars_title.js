#!/usr/bin/node
const request = require("request");
url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
data = '';
request(url, function(error, response, body) {
  if (error) {
    console.log(error);
  } else {
    data = JSON.parse(body);
    console.log(data.title);
  }
});
