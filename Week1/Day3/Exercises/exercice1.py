class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Soaad", 5)
cat2 = Cat("labo2a", 5)
cat3 = Cat("Lisa", 5)

def find_oldest(obj1, obj2, obj3):
    if obj1.age >= obj2.age and obj1.age >= obj3.age:
        return obj1
    if obj2.age >= obj1.age and obj2.age >= obj3.age:
        return obj2
    if obj3.age >= obj2.age and obj3.age >= obj1.age:
        return obj3
    
oldest_cat = find_oldest(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")