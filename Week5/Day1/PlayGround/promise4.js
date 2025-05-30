let bankAmount = 1000
let expense = 500

let bankPromise = new Promise((resolve, reject) => {
    if (expense<bankAmount) {
        resolve(expense);
    } else {
        reject("Rejected by the Bank");
    }
});

//1st "then"
bankPromise.then((result) => {
    //result is the argument passed in the resolve function
    console.log(`The expense is ${result} dollars`);
    return result * 1.17;
//2nd "then"
}).then((resultTwo) => {
    //resultTwo is the expense including taxes
    console.log(`The expense included taxes is ${resultTwo} dollars`);
    bankAmount -= resultTwo;
    console.log(`I have ${bankAmount} dollars left in the bank`);
    return bankAmount;
}).catch((error) => {
    console.log(`We have a problem : ${error}`)
});