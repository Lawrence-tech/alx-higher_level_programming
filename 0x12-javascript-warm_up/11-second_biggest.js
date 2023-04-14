#!/usr/bin/node

let snum = parseInt(process.argv[3]);

if (isNaN(snum)) {
  console.log('0');
  process.exit();
}

let fnum = parseInt(process.argv[2]);

if (fnum < snum) {
  const temp = fnum;
  fnum = snum;
  snum = temp;
}

for (let i = 4; i < process.argv.length; i++) {
  const next = parseInt(process.argv[i]);
  if (next > snum) {
    if (next > fnum) {
      snum = fnum;
      fnum = next;
    } else {
      snum = next;
    }
  }
}
console.log(snum);
