(function (name) {
    // const navElement = document.getElementById("name");
    // nameElement.textContent = name;
    // nameElement.style.color = "white";
    // nameElement.style.fontSize = "20px";
    const navElement = document.querySelector(".navbar");
    const nameElement = document.createElement("div");
    nameElement.textContent = name;
    nameElement.style.color = "white";
    nameElement.style.fontSize = "20px";
    navElement.appendChild(nameElement);
})("Imad")