const arr = [1, null, 2, 0, 3, "", 4, false, 5, undefined, NaN];

function removeUndefined(arr) {
    const items = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i]) 
            items.push(arr[i]);
    }
    return items;
}

console.log(removeUndefined(arr));