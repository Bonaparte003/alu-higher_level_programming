#!/usr/bin/node
const fs = require('fs');

const file = process.argv[2];
try {
  const data = fs.readFileSync(file, 'utf-8');
  console.log(data);
} catch (error) {
  console.log(error);
}
