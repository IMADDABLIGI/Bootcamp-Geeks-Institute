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