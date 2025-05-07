class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("object has been initialized")

# hmad = Person("Hmad", 42)
# driss = Person("Driss", 27)

# print(hmad.name, hmad.age)
# print(driss.name, driss.age)



class Dog():
    def __init__(self, dog_name): # INITIALIZATION an object and also the object atributes and methods
        print("A new object has been initialized")
        # print(type(self))
        self.name = dog_name
        self.obj_person = Person("Hmad", 42)
    
    def nba7(self, text="hawhaw"):
        print(f"{self.name}: {text}")

lkalb_obj = Dog(dog_name="l3awni")
lkalb_obj.color = "black"

# print(lkalb_obj.color)
# print(lkalb_obj.name)
lkalb_obj.nba7()


