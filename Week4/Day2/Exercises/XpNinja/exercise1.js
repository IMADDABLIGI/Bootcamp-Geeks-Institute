const data = [
  {
    name: 'Butters',
    age: 3,
    type: 'dog'
  },
   {
    name: 'Cuty',
    age: 5,
    type: 'rabbit'
  },
  {
    name: 'Lizzy',
    age: 6,
    type: 'dog'
  },
  {
    name: 'Red',
    age: 1,
    type: 'cat'
  },
  {
    name: 'Joey',
    age: 3,
    type: 'dog'
  },
  {
    name: 'Rex',
    age: 10,
    type: 'dog'
  },
];

let sum = 0;
let factor = 7;

data.forEach((dog) => {
    if (dog.type == 'dog'){
        sum += (factor * dog.age)
    }
})

console.log(sum)

sum = data.reduce((acc, nextValue) => {
    // console.log(acc)
    // console.log(nextValue)
    if (nextValue.type === 'dog')
        return acc + nextValue.age * 7;
    return acc
}, 0);

console.log(sum)