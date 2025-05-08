class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"cat {self.name} is walking")
    
    def make_sound(self):
        print(f"{self.name} make sound !!!")

class Siamese(Cat):
    pass
class Bengal(Cat):
    pass
class Chartreux(Cat):
    pass


bengal_obj = Bengal("bengal", 4)
chartreux_obj = Chartreux("chartreux", 3)
siamese_obj = Siamese("siamese", 6)

# bengal_obj.make_sound()

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

class Pets:
    def __init__(self, all_cats):
        self.all_cats = all_cats

    def walk(self):
        cat_list = self.all_cats
        for cat in cat_list:
            cat.walk()

sara_pets = Pets(all_cats)
sara_pets.walk()