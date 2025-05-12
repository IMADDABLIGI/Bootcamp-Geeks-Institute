# Exercise1 -------------------------------------------------------------

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Soaad", 3)
cat2 = Cat("labo2a", 5)
cat3 = Cat("Lisa", 2)

def find_oldest(obj1, obj2, obj3):
    if obj1.age >= obj2.age and obj1.age >= obj3.age:
        return obj1
    if obj2.age >= obj1.age and obj2.age >= obj3.age:
        return obj2
    if obj3.age >= obj2.age and obj3.age >= obj1.age:
        return obj3
    
oldest_cat = find_oldest(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and it's a {oldest_cat.age} years old cat.")

# Exercise2 -------------------------------------------------------------

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print("goes woof!")
    
    def jump(self):
        x = self.height * 2
        print(f"jumps {x} cm high!")

davids_dog = Dog("max", 35)
sarahs_dog = Dog("maxi", 30)

print(f"David’s dog name is {davids_dog.name} and his height is {davids_dog.height}")
print(f"Sarah’s dog name is {sarahs_dog.name} and his height is {sarahs_dog.height}")

davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()


def compare_size(obj1, obj2):
    if obj1.height > obj2.height:
        return obj1
    else:
        return obj2
    
bigger_dog = compare_size(davids_dog, sarahs_dog)
print(f"Bigger dog is {bigger_dog.name}")

# Exercise3 -------------------------------------------------------------

class Song:
    def __init__(self, lyrics):
        # self.lyrics = []
        self.lyrics = lyrics

    def sing_me_a_song(self):
        lyrics = self.lyrics
        for lyric in lyrics:
            print(lyric)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()


# Exercise4 -------------------------------------------------------------

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