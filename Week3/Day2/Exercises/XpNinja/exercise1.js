// function calculateBMI(obj) {
//     let bmi = obj.Mass / (obj.Height * obj.Height);

//     return bmi;
// }

obj1 = {
    FullName: 'Imad Dabligi',
    Mass: 65,
    Height: 1.90, // HHHHH
    calculateBMI: function(){
        return this.Mass / (this.Height * this.Height);
    }
}
obj2 = {
    FullName: 'Hamza Aboulhana',
    Mass: 80,
    Height: 1.85,
    calculateBMI: function(){
        return this.Mass / (this.Height * this.Height);
    }
}

function compareBMI(obj1, obj2){
    if (obj1.calculateBMI() > obj2.calculateBMI())
        console.log(`${obj1.FullName} has the largest BMI`)
    else
        console.log(`${obj2.FullName} has the largest BMI`)
}


compareBMI(obj1, obj2);
