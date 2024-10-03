#!/usr/bin/node
const file = require('fs');
const request = require('request');
request(process.argv[2]).pipe(file.createWriteStream(process.argv[3]));
