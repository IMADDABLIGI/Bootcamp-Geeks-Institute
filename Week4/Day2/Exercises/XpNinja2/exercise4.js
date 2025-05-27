const reverseArray = (arr) => {
    let temp = 0;
    const len = arr.length - 1
    for(let i = 0; i < arr.length / 2; i++){
        // console.log(`->`, arr[i], ' - ', arr[len - i])
        temp = arr[i];
        arr[i] = arr[len - i];
        arr[len - i] = temp;
    }
    console.log(arr)
}

const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];

// reverseArray(arr);

reverseArray([1,2,3,4,5,6,7,8,9,10]) // [10,9,8,7,6,5,4,3,2,1]
reverseArray([1,2,3,4,5]) // [5,4,3,2,1]
reverseArray([1,2]) // [2,1]
reverseArray([]) // []