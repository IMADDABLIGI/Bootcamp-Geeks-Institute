let age = [20,5,12,43,98,55];

let sum = 0;

for (let x in age){
    sum += age[x]
}

console.log(sum)

let max = 0

for (let x in age){
    if (max < age[x])
        max = age[x]
}
console.log(max);

