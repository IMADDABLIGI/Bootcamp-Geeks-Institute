const isAnagram = (str, find) => {
    find = find.toLowerCase()
    str = str.toLowerCase()
    for (let i = 0; i<str.length; i++){
        if (!find.includes(str[i]))
            return false
    }
    return true
}

console.log(isAnagram("Astronomer", "Moon starer"))