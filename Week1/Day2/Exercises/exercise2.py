# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# family["test"] = 23

family = {}

def calculate(family_dic):
    sum = 0
    for name, age in family_dic.items():
        if age < 3:
            continue
        elif age >= 3 and age <= 12:
            sum += 10
        else:
            sum += 15
    print(f"Your total cost for the movies is {sum}$")

while True:
    name = input("name (Type quit if u finished): ").lower()
    if name == "quit":
        break
    age = input("age: ")
    if not age.isdigit() or not name.isalpha():
        print("<-----> Error: Please provide a valide name and age! <----->")
        continue
    else:
        family[name] = int(age)

calculate(family)
    


# sum = 0
# for age in family.values():
#     if age < 3:
#         continue
#     elif age >= 3 and age <= 12:
#         sum += 10
#     else:
#         sum += 15
        

# print(f"the family’s total cost for the movies is {sum}$")