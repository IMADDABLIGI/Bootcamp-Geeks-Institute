// Get a random number between 1 and 100.
// Console.log all even numbers from 0 to the random number.


let number = Math.floor(Math.random() * 100) + 1;
// console.log(`Random number: ${number}`);

for (let i = 0; i <= number; i++) {
    if (i % 2 === 0) {
        console.log(i);
    }
}