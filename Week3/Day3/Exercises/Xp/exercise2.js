const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

const shoppingList = ["banana", "orange", "apple"]


function myBill(){
    let sum = 0;

    for (i in shoppingList){
        if (shoppingList[i] in stock){
            sum += prices[shoppingList[i]]
            stock[shoppingList[i]] -= 1
        }
    }
    // console.log(prices[shoppingList[0]]);
    return sum
}

console.log(myBill());