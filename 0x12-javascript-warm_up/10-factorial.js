#!/usr/bin/node

const factorialNumber = parseInt(process.argv[2]);

function factorial (number) {
  if (number > 1) {
    return number * factorial(number - 1);
  } else {
    return 1;
  }
}

console.log(factorial(factorialNumber));
