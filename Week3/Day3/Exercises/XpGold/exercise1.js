const isBlank = (str) => {
    if (str === "") {
        return true;
    }
    return false;
} 

console.log(isBlank("")); 
console.log(isBlank("Hello"));