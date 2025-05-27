const words = ["hwow","hey","bye"];

result = words.every((word) =>{
    return (word[0] === 'h')
})

// console.log(result)

const cars = ["bmw", "audi", "mercedes"];

const cars2 = cars.map((car, index, arr) => {
    console.log(`${arr[index]} - ${car}`, arr[index] == car);
    // arr[index] = arr[index] += " is a car";
    return arr[index] += " is a car";
})

console.log(cars2);
// console.log(cars);