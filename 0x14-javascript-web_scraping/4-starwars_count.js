#!/usr/bin/node
const request = require('request');
const web = process.argv[2];
request(web, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(body.split('/people/18/').length - 1);
  }
});
