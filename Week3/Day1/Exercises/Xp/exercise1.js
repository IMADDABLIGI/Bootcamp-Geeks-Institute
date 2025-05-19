const people = ["Greg", "Mary", "Devon", "James"];

people.splice(0, 1)

people[2] = "Jason"

people.push("Imad");

console.log(people.indexOf("Mary"))

const copyPeople = people.slice(1, people.length)

console.log(people.indexOf("Foo"));
// -1 Because there is no "Foo" in the people array

const last = people[people.length - 1]


for (let i = 0; i < people.length; i++){
    console.log(people[i]);
}

for (let i = 0; i < people.length; i++){
    console.log(people[i]);
    if (people[i] === "Devon")
            break;
}

//--
// console.log(last);
// console.log(people);

