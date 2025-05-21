function changeEnough(itemPrice, amountOfChange){
    let sum = 0
    const change = [0.25, 0.10, 0.05, 0.01]
    
    let i = 0;
    while (i < 4){
        sum += amountOfChange[i] * change[i];
        i++;
    }
    // console.log(sum)
    // for (x in amountOfChange)
    //     sum += amountOfChange[x]

    if (sum >= itemPrice)
        return true;
    return false;
}

purchase = changeEnough(4.25, [25, 20, 5, 0])

console.log(purchase)

console.log(changeEnough(14.11, [2,100,0,0]))
console.log(changeEnough(0.75, [0,0,20,5]))