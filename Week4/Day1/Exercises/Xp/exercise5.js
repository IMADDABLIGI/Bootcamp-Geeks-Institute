console.log(kgToGramsDeclaration(5));
function kgToGramsDeclaration(kg) {
    return kg * 1000;
}

// console.log(kgToGramsExpression(5));
const kgToGramsExpression = function(kg) {
    return kg * 1000;
};

// Difference is the first can be called before it's defined, while the second cannot.

const kgToGramsArrow = (kg) => kg * 1000;
// console.log(kgToGramsArrow(5));
