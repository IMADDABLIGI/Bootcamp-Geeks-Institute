let addressNumber = 55;
let addressStreet = "av Bosquet";
let country = "Paris";

// 2. Concatenate to form the globalAddress sentence
let globalAddress = `I live in ${addressNumber} ${addressStreet}, in ${country}`;

// 3. Display the globalAddress
document.getElementById("displayAddress").innerText = globalAddress;


// console.log(document.element.parentNode)



let i = 0;

for (i; i <= 15; i++){
    if (i % 2 === 0)   
        console.log(`${i} is even`)
    else
        console.log(`${i} is odd`)
}

// alert("Hello");

// let age = prompt('How old are you?', 20);

// if (age)
//     alert(`You are ${age} years old!`); // You are 20 years old!

// let person = {
//   firstName: "John",
//   lastName: "Doe",
// };
// person.firstName = "Sarah"
// person.eyeColor= "blue"

// console.log(person) 