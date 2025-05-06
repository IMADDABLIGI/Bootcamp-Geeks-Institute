
year = 123879
year_of_birth = 2001
my_age = year - year_of_birth

print("My age in the year", year, "will be", my_age)

tuple = (1, 2, 3, 4, 5)

# tuple[1] = 10
# This will raise an error because tuples are immutable

print(tuple[0])

set = {1, 2, 3, 4, 5}

print(set)

my_dict = {
    "name": "Imad",
    "age": 24,
    "city": "Casablanca"
}

my_dict["name"] = "Imad Dabligi"
print(my_dict["name"])
print(my_dict)
