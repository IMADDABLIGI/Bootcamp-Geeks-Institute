const menu = [
  {
    type : "starter",
    name : "Houmous with Pita"
  },
  {
    type : "starter",
    name : "Vegetable Soup with Houmous peas"
  },
  {
    type : "dessert",
    name : "Chocolate Cake"
  }
]

menu.forEach((item) => {
    item.type === "dessert" ? console.log("Kayn Dessert") : ''
})

menu.filter((item) => item.type === 'starter').length !== 3 ? console.log("Not all starter") : console.log("All starter")


const vegetarian = ["vegetable", "houmous", "eggs", "vanilla", "potatoes" ]
if (menu.filter((item) => item.type === 'main course').length !== 1){
    for (veg in vegetarian){
        menu.push({
            type: "main course",
            name: vegetarian[veg]
        })
    }
}

console.log(menu)