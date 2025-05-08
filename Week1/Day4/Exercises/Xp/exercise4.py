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