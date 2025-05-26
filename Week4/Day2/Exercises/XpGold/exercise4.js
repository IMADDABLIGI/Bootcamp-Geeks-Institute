const array = [[1],[2],[3],[[[4]]],[[[5]]]]

const newArray = array.flat();

console.log(newArray);

// Using a method, take this array const greeting = [["Hello", "young", "grasshopper!"], ["you", "are"], ["learning", "fast!"]]; and modify it to look like this array: ["Hello young grasshopper!","you are","learning fast!"].

const greeting = [["Hello", "young", "grasshopper!"], ["you", "are"], ["learning", "fast!"]];
const newGreeting = greeting.map(subArray => subArray.join(' '));

console.log(newGreeting);

let perfectGreeting = '';
newGreeting.forEach(sentence => {
    perfectGreeting += ' ' + sentence;
});

console.log(perfectGreeting);

const trapped = [[[[[[[[[[[[[[[[[[[[[[[[[[3]]]]]]]]]]]]]]]]]]]]]]]]]]

const flattenedTrapped = trapped.flat(Infinity);

console.log(flattenedTrapped);

