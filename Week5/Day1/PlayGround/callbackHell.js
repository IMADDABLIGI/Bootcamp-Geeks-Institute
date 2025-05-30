function getMeat(callback) {
    console.log("walking to the butcher...");
    setTimeout(() => {
        console.log("getting the beef from the butcher");
        callback("beef");
    }, 2000);
}

function getBuns(callback) {
    console.log("getting the buns from the bakery");
    callback("whole grains");
}


function putMeatBetwenBuns(bunsType, meatType, callback) {
    console.log("preparing the burger...");
    callback(`The ${meatType} burger with ${bunsType} buns is created`)
}

const makeBurger = () => {
    getMeat((meatType) => {

        getBuns((bunsType) => {

            putMeatBetwenBuns(bunsType, meatType, (finalBurger) => {
                console.log(finalBurger);
                
            })
        })
    })
}

const burger = makeBurger();