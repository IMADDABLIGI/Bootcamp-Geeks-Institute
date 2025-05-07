class Farm():
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        dic = self.animals
        if animal_type in dic:
            dic[animal_type] = dic[animal_type] + count
        else:
            dic[animal_type] = count
        self.animals = dic
    
    def get_info(self):
        str = f"{self.name}’s farm\n\n"
        animals = self.animals
        for animal, count in animals.items():
            str += f"{animal} : {count}\n"
        str +=  f"\nE-I-E-I-0!"
        return str



# f = Farm("Firma")
# f.add_animal("Donkey", 2)
# f.add_animal("Donkey", 2)
# f.add_animal("Fish", 2)
# f.add_animal("Dinasours", 20)
# f.add_animal("Dinasours", 2)
# print(f.animals)

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
