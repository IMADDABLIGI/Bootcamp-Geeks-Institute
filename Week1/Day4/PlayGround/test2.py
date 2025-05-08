class Parent:
    def __init__(self, name):
        self.name = name
        # print("Parent has been initialized")

    def fnc(self):
        print("ANA Parent")


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        # print("Child has been initialized")

    def fnc(self):
        print("ANA Child")

    def test(self):
        super(Child, self).fnc()
        # self.fnc()



son = Child("Driss", 15)
son.test()