const makeBurger = () => {
    const meatType = getMeat();
    const bunsType = getBuns();
    const burger = putMeatBetwenBuns(bunsType, meatType);
    return burger;
};

function getMeat() {
    console.log("walking to the butcher...");
    setTimeout(() => {
        console.log("getting the beef from the butcher");
        return "beef"
    }, 2000);
}

function getBuns() {
    console.log("getting the buns from the bakery");
    return "whole grain";
}


function putMeatBetwenBuns(bunsType, meatType) {
    console.log(`creating the ${meatType} burger with ${bunsType} buns`);
    return "Delicious Burger"
}

const burger = makeBurger();
console.log(burger);