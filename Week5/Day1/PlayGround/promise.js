function getMeat() {
    console.log("walking to the butcher...");
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log("getting the beef from the butcher");
            resolve("beef");
        }, 2000);
    });
}

function getBuns() {
    console.log("getting the buns from the bakery");
    return "whole grain";
}

function putMeatBetwenBuns(bunsType, meatType) {
    console.log(`creating the ${meatType} burger with ${bunsType} buns`);
    return "Delicious Burger";
}


const makeBurger = async () => {
    const meatType = await getMeat();
    const bunsType = getBuns();
    const burger = putMeatBetwenBuns(bunsType, meatType);
    return burger;
};

(async () => {
    const burger = await makeBurger();
    console.log(burger);
})();