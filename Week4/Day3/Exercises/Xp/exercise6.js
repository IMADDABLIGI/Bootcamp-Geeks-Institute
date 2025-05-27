// console.log([2] == [2])
// console.log({} == {})
// Both False


const object1 = { number: 5 }; 
const object2 = object1; 
const object3 = object2; 
const object4 = { number: 5};

object1.number = 4;
console.log(object2.number)
console.log(object3.number)
console.log(object4.number)

//object are called by reference so if u assign an obj to another it will by default point to it

class Animal{
    constructor(name, type, color){
        this.name = name;
        this.type = type;
        this.color = color;
    }
}

const lkalb = new Animal("Max", "Dog", "K7al");


class Mammal extends Animal {
    constructor(name, type, color){
        super(name, type, color);
    }

    sound(sound) {
        console.log(`${sound} I'm a ${this.type}, named ${this.name} and I'm ${this.color}`);
    }
}


// const dog = new Mammal("Max", "Dog", "K7al");
// dog.sound("bark");

const farmerCow = new Mammal("Lily", "cow", "brown and white")
farmerCow.sound("Moooo");