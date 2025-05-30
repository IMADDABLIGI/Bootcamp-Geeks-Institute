function startBurger() {
    return new Promise((resolve, reject) => {
        console.log("walking to the butcher...");
        setTimeout(() => {
            console.log("getting the beef from the butcher");
            resolve("beef");
        }, 2000)
    })
}


startBurger()
    .then(meatType => {
        console.log("getting the buns from the bakery");
        return [meatType, "whole grains"];
    })
    .then(([meatType, bunsType]) => {
        console.log("preparing the burger...");
        console.log(`The ${meatType} burger with ${bunsType} buns is created`);
    })