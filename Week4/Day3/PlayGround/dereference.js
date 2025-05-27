let myCar = {
  color : 'blue',
  details : {
    plateNumber: 123,
    name : "Ford"
  }
}

let myNewCar = {...myCar}
console.log("myNewCar : ", myNewCar) 
// myNewCar :  
// { 
//      color: 'blue', 
//      details: { plateNumber: 123, name: 'Ford' } 
// }

// SHALLOW COPYING
myCar.color = "red"
console.log("myNewCar.color :", myNewCar.color)
// myNewCar.color : blue -- UNCHANGED
console.log("myCar.color :", myCar.color)
// myCar.color : red -- CHANGED