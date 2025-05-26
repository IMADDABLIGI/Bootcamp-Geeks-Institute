const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th","st","nd","rd"];



// Write a JavaScript program that displays the colors in the following order : “1st choice is Blue .” “2nd choice is Green.” “3rd choice is Red.” ect…

colors.forEach((color, index) => {
    let suffix = ordinal[(index + 1)];
    if (index == 0 || index == 1 || index == 2)
        console.log(`${index + 1}${suffix} choice is ${color}.`);
    else
        console.log(`${index + 1}th choice is ${color}.`);
})