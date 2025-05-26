let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        paid : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

const displayGroceries = () => {
    groceries.fruits.forEach(fruit => {
        console.log(`Fruit: ${fruit}`);
    });
}

// displayGroceries()


const cloneGroceries = () => {
    const user = client;
    client = "Betty";
    // No, because variables in JavaScript are passed by value, not by reference.
    // user is a primitive value that was copied from client at the time of assignment
    const shopping = groceries
    groceries.totalPrice = "35$";
    // console.log(shopping);
    // Beacause objects are called by reference not by value.
    // Again beacause objects are called by reference not by value.

}

cloneGroceries();