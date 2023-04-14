#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () {
  this.value++;
}; //  function incr that increments the integer value
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
