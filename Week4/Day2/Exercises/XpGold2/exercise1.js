arr = [1, 2, 3, 4];

const sum = (arr) => {
    let sum = 0;
    for (num in arr) {
        sum += arr[num];
    }
    return sum;
}

console.log(sum(arr)); 

