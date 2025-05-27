const letters = ['x', 'y', 'z', 'z'];

let obj = {}

for (let i = 0; i < letters.length; i++){
    if (!(letters[i] in obj))
        obj[letters[i]] = i;
}

console.log(obj)

obj = letters.reduce((acc, letter) => {
    acc[letter] = (acc[letter] || 0) + 1;
    return acc;
}
, {});
console.log(obj);