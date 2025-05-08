# class Man():
#     sex = "Male"

#     @staticmethod
#     def get_nicknames():
#         return ["Bro", "Dude", "Buddy", Man.sex]


# m = Man()
# print(Man.sex)
# print(m.get_nicknames())
# print(m.sex)
# print(Man.get_nicknames())

# Static Method does not require a self instance to work

# Classic Method is a method that it does not depend on the instance but in the class itself 

class MyClass:
    __counter = 0

    @classmethod
    def add(cls,a): 
        return cls.__counter + a

    @staticmethod
    def increment():
        MyClass.__counter += 1

my_class_add = MyClass.add(3)
print(my_class_add)
# >> 3

new_class = MyClass()
new_class.__counter = 1

MyClass.increment()

print(new_class.add(3))
print(new_class.add(4))