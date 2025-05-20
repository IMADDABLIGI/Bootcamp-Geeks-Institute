const numbers = [5,0,9,1,7,4,2,6,3,8];

// console.log(numbers.toString())

let str = numbers.toString()

str = numbers.join("")

// console.log(str)

function checkSorted(str){
    for (let x = 0; x < str.length - 1; x++){
        if (str[x] < str[x + 1])
            return false
    }
    return true
}


function swapNum(str, i) {
  let arr = str.split('');        
  let temp = arr[i];
  arr[i] = arr[i + 1];
  arr[i + 1] = temp;
  return arr.join('');
}


let i;
let isSorted = false;
while(!isSorted){

    i = 0
    while (i < str.length){
        if (str[i] < str[i+1])
            str = swapNum(str, i)
        console.log(str);
        i++;
    }
    isSorted = checkSorted(str)
}
