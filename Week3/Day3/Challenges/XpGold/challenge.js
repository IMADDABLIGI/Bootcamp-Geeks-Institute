const log = (str) => {
    console.log(str)
}

const countStars = (listStr) => {
    maxLength = 0;
    for (x in listStr){
        if (listStr[x].length > maxLength){
            maxLength = listStr[x].length;
            // log(listStr[x]);
        }
    }
    return maxLength;
}

const makeStars = (stars) => {
    let starLines = '';
    for (let i = 0; i < stars + 4; i++){
        starLines += '*';
    }
    return starLines;
}

let userStr = "Hello, world, from, Imad";
let listStr = userStr.split(', ')

// log(listStr);

const stars = countStars(listStr);
// log(stars);
const starLine = makeStars(stars);

log(starLine);
for (x in listStr){
    spaces = "";
    for (let i = 0; i < stars - listStr[x].length; i++)
        spaces += " ";
    log(`* ${listStr[x]}${spaces} *`);
}
log(starLine);

