let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

let userInput = prompt("Enter your name: ");

// let userInput = "randy";

if (userInput in guestList)
    console.log(`Hi! I'm ${userInput}, and I'm from ${guestList[userInput]}.`)
else
    console.log("Hi! I'm a guest.")