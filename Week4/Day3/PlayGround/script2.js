// const address = {
//   street: 'Evergreen Terrace',
//   number: '742',
//   city: 'Springfield',
//   state: 'NT',
//   zip: '49007',
// };

// const {street: a, city: c} = address;
// console.log(c, a)

const person = {
    name : "Imad",
    age: 28,
    eat: function (){
        console.log(`${this.name} is Eating`)
    }
}

// console.log(person)
person.eat()