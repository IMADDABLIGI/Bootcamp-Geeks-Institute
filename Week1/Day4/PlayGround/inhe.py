# class Parent:
#     def __init__(self, name="Test"):
#         self.name = name

#     def print_output(self):
#         print("my name is:", self.name)

# class Child(Parent):
#     pass

# A = Child()
# print(A.name)
# A.print_output()
    

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self, sound):
        print(f"Animal sound: {sound}")

class Cat(Animal):
    pass

chat = Cat("Monica", 2)
chat.make_sound("Meeeow")