const repeat = (str, num) => {
    let sentence = '';
    for (let i = 0; i < num; i++) {
        sentence += str;
    }
    return  sentence;
}

console.log(repeat('Ha!', 3));