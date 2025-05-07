class MenuManager:
    def __init__(self):
        self.menu = []

    def add_item(self, name, price, spice, gluten):
        self.menu.append({"name" : name, "price" : price, "spice" : spice, "gluten" : gluten})
        print(f"'{name}' has been Added")
        # print(self.menu)
        # for plat in self.menu:
        #     if name == plat["name"]:
        #         self.menu.append({"name" : name, "price" : price, "spice" : spice, "gluten" : gluten})
            # else:
            #     print("had lpla kayn")


    def update_item(self, name, price, spice, gluten):
        for plat in self.menu:
            if plat["name"] == name:
                plat["price"] = price
                plat["spice"] = spice
                plat["gluten"] = gluten
                print(f"'{name}' has been updated")
                return
        print("Hey manager this dish is not ont the menu")

    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.remove(dish)
                print(f"'{name}' has been removed.")
                return
        print(f"'{name}' is not in the menu.")

menu = MenuManager()
menu.add_item("babouch", 5, "A", 5)
menu.add_item("t9alya", 50, "D", 2)
menu.update_item("harira", 6, "C", 0)
menu.update_item("t9alya", 80, "D", 5)
menu.remove_item("t9alya")

# print(menu.menu)


