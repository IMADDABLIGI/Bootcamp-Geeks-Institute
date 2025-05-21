const abbrevName = (str) => {
    const names = str.split(" ");
    if (names.length !== 2) {
        return "Invalid input";
    }
    const firstName = names[0];
    const lastName = names[1];
    
    return `${firstName} ${lastName[0]}`;
}

console.log(abbrevName("John Doe")); // Output: "J.D"