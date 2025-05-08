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



