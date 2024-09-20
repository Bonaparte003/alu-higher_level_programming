#!/usr/bin/node
const a = process.argv.length - 2;
if (a === 0) {
  console.log('No argument');
} else if (a === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
