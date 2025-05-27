const arr = [1, 2, 2, 3, 4, 4, 5];

function removeDuplicates(arr) {
    const uniqueItems = [];
    for (let i = 0; i < arr.length; i++) {
        if (!uniqueItems.includes(arr[i])) {
            uniqueItems.push(arr[i]);
        }
    }
    return uniqueItems;
}

console.log(removeDuplicates(arr));
