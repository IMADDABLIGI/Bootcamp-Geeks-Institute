class Parent:
    def __init__(self, name, age):
        print("Parent Initialized with values", name, age)
        self.name = "test"
        pass

class Child(Parent):
    def __init__(self):
        print("Child Initilized", self.name)


son = Child()