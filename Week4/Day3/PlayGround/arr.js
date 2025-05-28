const arr = [1, 2, 3, 4];

let arr2 = [...arr, 5, 6, 7, 8];
console.log(arr2); // [1, 2, 3, 4, 5, 6, 7, 8]


const obj = {
  name: "John",
  age: 30,
  city: "New York"
};

let obj2 = { ...obj, country: "USA", occupation: "Engineer" };
console.log(obj2); // { name: 'John', age: 30, city: 'New York', country: 'USA', occupation: 'Engineer' }