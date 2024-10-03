#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const data = process.argv[3];

try {
  fs.writeFileSync(file, data, 'utf-8');
} catch (error) {
  console.log(error);
}
