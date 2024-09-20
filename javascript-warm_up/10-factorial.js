#!/usr/bin/node
const n = parseInt(process.argv[2]);
function factorial (n) {
  if (n === 0 || isNaN(n) || !n) {
    n = 1;
    return (n);
  } else {
    return (n * factorial(n - 1));
  }
}
console.log(factorial(n));
