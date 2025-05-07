user_height = input("Enter your height in cm: ")


while not user_height.isdigit():
    print("Please enter a valid number for your height")
    user_height = input("Enter your height in cm: ")


if int(user_height) <= 145:
    print("You are short, grow up so u could ride next time.")
else:
    print("You are tall enough to ride the roller coaster.")


