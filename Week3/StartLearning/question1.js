// Clean the room function:

// Given an input of [1,2,4,591,392,391,2,5,10,2,1,1,1,20,20], make a function that organizes these, into individual array that is ordered.

// For example answer(ArrayFromAbove) should return: [[1,1,1,1],[2,2,2], 4,5,10,[20,20], 391, 392,591].
const answer = (arr) => {
    const sortedArr = arr.sort((a, b) => a - b);
    const result = [];
    let currentGroup = [];

    for (let i = 0; i < sortedArr.length; i++) {
        if (currentGroup.length === 0 || sortedArr[i] === currentGroup[0]) {
            currentGroup.push(sortedArr[i]);
        } else {
            result.push(currentGroup.length > 1 ? currentGroup : currentGroup[0]);
            currentGroup = [sortedArr[i]];
        }
    }

    if (currentGroup.length > 0)
        result.push(currentGroup.length > 1 ? currentGroup : currentGroup[0]);

    return result;
};

const inputArray = [1, 2, 4, 591, 392, 391, 2, 5, 10, 2, 1, 1, 1, 20, 20];
console.log(answer(inputArray));