const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

const sentence = epic.reduce((acc, val) => {
    return (acc + " " + val)
})

console.log(sentence)