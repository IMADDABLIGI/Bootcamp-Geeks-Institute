class Parent:
    def __init__(self, name):
        self.name = name
        print("initilized parent: ", name)
        self.age = 28

    def print_output(self):
        print("Printing")

class Child(Parent):
    pass
    def __init__(self, name):
        # Parent.__init__(self)
        super().__init__(name) #To initialized the parent class
        # super(Child, self).print_output() #To Call the parent function
        # self.print_output()
        print("initilized child")


A = Child("test")
print(A.age)
# A.print_output()
    

# class Animal:
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type
#         print("initilized animal")
    
#     def make_sound(self, sound):
#         print(f"Animal sound: {sound}")

# class Cat(Animal):
#     def __init__(self, name, age, type):
#         print("initilized Cat")
#         super().__init__(name, type)
#         pass

# chat = Cat("Lissa", 2, "cat")
# chat.make_sound("Meeeow")
# print(chat.name)