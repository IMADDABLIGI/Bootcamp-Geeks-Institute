function findAvg(gradesList){
    let sum = 0
    for (grade in gradesList){
        sum += gradesList[grade]
    }
    // console.log(sum)
    avg = sum / gradesList.length
    console.log(avg)
    if (avg > 65)
        console.log("You passed")
    else
        console.log("You failed and must repeat the course.")
}

gradesList = [8, 2, 6, 4]

findAvg(gradesList)