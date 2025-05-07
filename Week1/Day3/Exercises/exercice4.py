class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.dic_animals = {}

    def add_animal(self, new_animal):
        if not new_animal in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("The animals in the Zoo are: ")
        for animal in self.animals:
            print(f"| {animal} |", end="")
        print("")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sort_animals = sorted(self.animals)
        dic = {}
        # print(sort_animals)
        for animal in sort_animals:
            key = animal[0]
            if not key in dic:
                dic[key] = []
            dic[key].append(animal)
        self.dic_animals = dic
        print(self.dic_animals)

    def get_groups(self):
        dic = self.dic_animals
        for x, y in dic.items():
            print(f"{x}: {y}")
    


# rabat_zoo = Zoo("Rabat Zoo")
# rabat_zoo.add_animal("Tiger")
# rabat_zoo.add_animal("Eagle")
# rabat_zoo.add_animal("Elephant")
# rabat_zoo.add_animal("Baboon")
# rabat_zoo.add_animal("Bear")
# rabat_zoo.add_animal("Cat")
# rabat_zoo.add_animal("Cougar")
# rabat_zoo.add_animal("Giraffe")
# rabat_zoo.add_animal("Lion")
# rabat_zoo.add_animal("Zebra")

# rabat_zoo.sell_animal("Elephant")
# rabat_zoo.get_animals()

# rabat_zoo.sort_animals()
# rabat_zoo.get_groups()


# Step 2: Create a Zoo instance
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Step 3: Use the Zoo methods
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Bear")
ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()