// elem.setAttribute(name, value)

navbarElement = document.getElementById("navBar")

navbarElement.setAttribute("id", "socialNetworkNavigation")

let newLi = document.createElement('li')

// Syntax : document.createTextNode('text') 
let newTextNode = document.createTextNode('Logout');

// Syntax: `element.appendChild`
newLi.appendChild(newTextNode)

// console.log(newLi)

// ulElement = navbarElement.firstElementChild
ulElement = document.getElementsByTagName("ul")[0]
// console.log(ulElement);

ulElement.appendChild(newLi)

firstElement = ulElement.firstElementChild.textContent
lastElement = ulElement.lastElementChild.textContent
console.log(firstElement)
console.log(lastElement)