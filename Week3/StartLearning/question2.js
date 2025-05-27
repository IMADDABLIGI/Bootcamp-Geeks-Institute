const answer = (arr, target) => {
    const seenNumbers = new Set();
    const result = [];

    for (let i = 0; i < arr.length; i++) {
        const complement = target - arr[i];
        if (seenNumbers.has(complement)) {
            result.push([complement, arr[i]]);
        }
        seenNumbers.add(arr[i]);
    }

    return result.length > 0 ? result : null;
}

console.log(answer([1, 2, 3], 4));