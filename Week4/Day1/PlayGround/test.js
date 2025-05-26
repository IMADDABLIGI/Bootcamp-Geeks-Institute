console.log("string text line 1\n\
string text line 2");
// "string text line 1
// string text line 2"

// (function (name) {
//     console.log("Hello " + name);
// })("Sarah")




// function outside(x) {
//   function inside(y) {
//     return x + y;
//   }
//   return inside;
// }
// let fnInside = outside(3);
// console.log(fnInside) 
// // function inside(y) {
// //    return x + y;
// //  }
// console.dir(fnInside) 
// // Closure (outside) x: 3

// let result = fnInside(5); // The same as calling outside(3)(5)
// console.log(result) // returns 8

// const add = a => b => a + b;
// const result = add(2)(3)
// console.log(result) // console.log 5

let c = { greeting: 'Hey!' };
let d;

d = c;
c.greeting = 'Hello';
console.log(d.greeting);