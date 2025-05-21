containerElement = document.getElementById("container")
console.log(containerElement);

// listElements = document.getElementsByClassName("list")[0].lastElementChild

listElement = document.getElementsByClassName("list")[0].lastElementChild.textContent = "Richard"
// console.log(listElement)

parentElement = document.getElementsByClassName("list")[1]
childElement = document.getElementsByClassName("list")[1].children[1]

// console.log(parentElement)
// console.log(childElement)

parentElement.removeChild(childElement)

// Change the name of the first <li> of each <ul> to your name. (Hint : use a loop)

ulElements = document.getElementsByClassName("list")

for (let i = 0; i < 2; i++){
    document.getElementsByClassName("list")[i].children[0].textContent = "Imad"
}

// elem.classList.add(nameOfClass)

ulElements[0].classList.add("student_list")
ulElements[1].classList.add("student_list")

ulElements[0].classList.add("university", "attendance")

containerElement.style.background = "lightBlue"
containerElement.style.padding = "10px"

// containerElement.style.display = "none"
ulElements[1].lastElementChild.style.display = "none"
ulElements[0].lastElementChild.style.border = "1px solid yellow"


bodyElement = document.getElementsByTagName("body")[0]

bodyElement.style.fontSize = "20px";

console.log(bodyElement);