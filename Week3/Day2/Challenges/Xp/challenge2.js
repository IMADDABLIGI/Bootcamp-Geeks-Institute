// let str = '*' * 2

// console.log(str)

let str = '*'

for (let i = 1; i <= 6; i++){
    console.log(str)
    str += ' *'
}

let i = 1;
while (i<=6){
    let str= ''
    for (let j = i; j > 0; j--){
        str += '* ';
    }
    console.log(str)
    i++;
}