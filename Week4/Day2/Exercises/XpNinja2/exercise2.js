function chunkString(str, length) {
    const arr = [];

    for (let i = 0; i < str.length; i += length) {
        arr.push(str.slice(i, i + length));
    }

    return arr;
}
console.log(chunkString("HelloWorld", 3));
