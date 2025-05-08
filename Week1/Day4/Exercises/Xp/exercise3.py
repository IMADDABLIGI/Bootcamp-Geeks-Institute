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

