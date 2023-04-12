#!/usr/bin/node

const integer = parseInt(process.argv[2]);

if (integer >= 0) {
  for (let a = 0; a < integer; a++) {
    console.log('X'.repeat(integer));
  }
} else {
  console.log('Missing size');
}
