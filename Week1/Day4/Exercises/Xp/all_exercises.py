# exercise1 -------------------------------------------------------------

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

# exercise2 -------------------------------------------------------------

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    # @classmethod
    def bark(self):
        return (f"{self.name} is barking")
    
    def run_speed(self):
        return (self.weight / self.age * 10)
    
    def fight(self, other_dog):
        dog1_fight = self.run_speed() * self.weight
        dog2_fight = other_dog.run_speed() * other_dog.weight
        if dog1_fight >= dog2_fight:
            return (f"The dog who won the combat fight is <{self.name}>")
        return (f"The dog who won the combat fight is <{other_dog.name}>")

if __name__ == "__main__":
    dog1 = Dog("Champolice", 5, 15)
    dog2 = Dog("Pitbull", 4, 7)
    dog3 = Dog("Malinoua", 10, 8)

    print(dog1.bark())
    print(dog2.run_speed())
    print(dog1.fight(dog2))

# exercise3 -------------------------------------------------------------

from exercise2 import Dog
import random


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *args):
        print("all play together")

    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        random_num = random.randint(0, 3)
        print(tricks[random_num])

# chien = PetDog("Lkalb", 3, 30, False)
# # chien.train()
# chien.do_a_trick()

my_dog = PetDog("LKALB", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()



# exercise4 -------------------------------------------------------------

class Person():
    def __init__(self, first_name, age, last_name=[]):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        if self.age >= 18:
            return True
        return False


class Family():
    def __init__(self, last_name, members=[]):
        self.last_name = last_name
        self.members = members

    def born(self, first_name, age):
        obj = Person(first_name, age, self.last_name)
        self.members.append(obj)
        # print(self.members)
    
    def check_majority(self, first_name):
        members = self.members
        for member in members:
            if first_name == member.first_name:
                if member.is_18():
                    return print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                return print("Sorry, you are not allowed to go out with your friends.")
        print("this member is not on the family")
                
    def family_presentation(self):
        print(f"----Family last name is {self.last_name} and it’s members are: ")
        members = self.members
        for member in members:
            print(f"{member.first_name} and his age is {member.age}")



father = Person("Saiid", 45)
mother = Person("Saiida", 85)

idrissi = Family("Idrissi", [father, mother])
idrissi.born("Hmida", 18)
# idrissi.born("Soaad", -1)

idrissi.check_majority("Hmida")
idrissi.check_majority("Soaad")
idrissi.family_presentation()