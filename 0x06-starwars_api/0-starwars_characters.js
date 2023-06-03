#!/usr/bin/node
const id = process.argv.slice(2);  // cmd args
const url = `https://swapi-api.hbtn.io/api/films/${id[0]}/`;

const request = require('request');
request(url, async function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  // convert return body to json
  const bodyJson = JSON.parse(body);
  // iterate through xters url in object
  for (const characters of bodyJson.characters) {
    // fetch their details and wait for response
    await new Promise(function (resolve, reject) {
      request(characters, function (error, response, body) {
        if (error) {
          return console.error(error);
        }
        const xterJson = JSON.parse(body);
        console.log(xterJson.name);
        resolve();
      });
    });
  }
});
