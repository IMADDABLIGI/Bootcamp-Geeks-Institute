function displayNumbersDivisible(){
    let i = 0
    let sum = 0;
    let numbers = ""
    while (i <= 500){
        if (i % 23 === 0){
            numbers += i
            numbers += ' '
            // numbers.push(i)
            sum += i;
        }
        i++;
    }
    console.log("outcome :", numbers)
    console.log("Sum :",sum)
}

displayNumbersDivisible();