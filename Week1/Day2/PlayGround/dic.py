# def check_keywordedarguments(**kwargs):
#     print(kwargs.items())
#     for key, value in kwargs.items():
#         print(key,":",value)

# check_keywordedarguments(name="Sarah", age=24)

# --------------- Return Tuples ---------------
def return_items():
    return "Imad", 24,

name, age = return_items()

print(name)
print(age)


# --------------- Dictionaries ---------------
my_dic = {
    "name": "Imad",
    "age": 24,
    "city": "Casablanca"
}

# del my_dic["name"]

for key, value in my_dic.items():
    print(key, ":", value)
