function hotelCost(){
    let numNight = '';
    const costNight = 140;
    
    while (1){
        numNight = Number(prompt("Please provide the number of nights you would like to stay in the hotel"))
        if (numNight)
            // numNight = Number(numNight)
            // return (numNight * costNight)
            if (numNight < 0)
                alert("Nice try Diddy");
            else
                break;
        }
        // console.log("-->",numNight);
        return (numNight * costNight)
}

// console.log(hotelCost())

const planeRideCost = () => {
    let dest;
    let capitalizedCity;
    let cityObj = {
        "London": 183,
        "Paris": 220
    }

    while(1){
        dest = prompt("What is ur destination")
        if (dest){
            capitalizedCity = dest.charAt(0).toUpperCase() + dest.slice(1).toLowerCase();
            break;
        }
    }
    if (capitalizedCity in cityObj){
        return (cityObj[capitalizedCity]);
    }
    return 300;
}
// console.log(planeRideCost())


const rentalCarCost = () => {
    let numDays;
    const costDay = 40;
    
    while (1){
        numDays = Number(prompt("Please provide the number of days you would like to rent the car"))
        if (numDays)
            if (numDays < 0)
                alert("Nice try Diddy");
            else
                break;
        }
        if (numDays > 10){
            let discount = (numDays * costDay * 0.05);
            return ((numDays * costDay) - discount);
        }

        // console.log("-->",numDays);
        return (numDays * costDay)
}
// console.log(rentalCarCost())

const totalVacationCost = () => {
    nightCost = hotelCost();
    planeCost = planeRideCost()
    carCost = rentalCarCost()


    totalCost = `The car cost: ${carCost}, the hotel cost: ${nightCost}, the plane tickets cost: ${planeCost}.`
    return totalCost
}

console.log(totalVacationCost())