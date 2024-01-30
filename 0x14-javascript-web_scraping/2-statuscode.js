#!/usr/bin/node
const website = process.argv[2];
const requests = require('request');
requests(website, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
