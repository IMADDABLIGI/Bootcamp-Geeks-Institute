# def age():
#     user_age = input("How old are you?\n>>> ")
#     #######
#     try:
#         user_age = int(user_age)
#         print("I AM AFTER USER_AGE")
#     except:
#         print("Your age is not a real age")
#         user_age = 0
#     #######
#     print(f"Next year, you will be {user_age+1} years old")

# age()

# valid_input = False

# while not valid_input:
#     user_age = input("type in ur age: ")
#     try:
#         user_age = int(user_age)
#         valid_input = True
#     except:
#         print("Type a real number!")



# def fnc():
#     raise Exception("There has been an error here")


# try:
#     fnc()
# except:
#     print("error Occured")

mylist = [1, 3, 5]
print(mylist.__str__())