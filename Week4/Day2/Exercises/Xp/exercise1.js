const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

// 1# choice is Blue.

colors.map((color, index) => {
    console.log(`${index + 1}# choice is ${color}.`);
})


colors.forEach((color) => {
    if (color === "Violet")
        console.log("Yeah");
    else
        console.log("No...");
});