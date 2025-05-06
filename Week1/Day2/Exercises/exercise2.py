# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# family["test"] = 23

def calculate(age):
    if age < 3:
        return 0
    elif age >= 3 and age <= 12:
        return 10
    else:
        return 15


sum = 0
check = True

while check:
    name = input("name (Type quit if u finished): ").lower()
    if name == "quit":
        check = False
        break
    age = input("age: ")
    if not age.isdigit() or not name.isalpha():
        print("Please provide a valide name and age")
        continue
    else:
        sum += calculate(int(age))

print(f"Your total cost for the movies is {sum}$")
    

# sum = 0

# for age in family.values():
#     if age < 3:
#         continue
#     elif age >= 3 and age <= 12:
#         sum += 10
#     else:
#         sum += 15
        

# print(f"the family’s total cost for the movies is {sum}$")