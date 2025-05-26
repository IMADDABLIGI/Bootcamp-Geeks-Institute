// ------1------
const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];

const result = ['bread', ...vegetables, 'chicken', ...fruits];
console.log(result);
// Result will be an array of fruits and vegetables combined.

// ------2------
const country = "USA";
console.log([...country]);

// Result will be an array of characters ["U", "S", "A"].