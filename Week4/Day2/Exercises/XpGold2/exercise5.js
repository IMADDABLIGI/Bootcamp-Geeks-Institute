const startLine = '     ||<- Start line';
let turtle = '🐢';
let rabbit = '🐇';

turtle = turtle.padStart(9, ' ');
rabbit = rabbit.padStart(9, ' ');

console.log(startLine);
console.log(turtle);
console.log(rabbit);

turtle = turtle.trim().padEnd(9, '=');
// this will add '=' to the end of the turtle string