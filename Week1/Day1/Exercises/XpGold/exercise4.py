names = ['imad', 'soaad', 'f', 'hmad', 'driss', 'hamza']

user_name = input("Enter your name: ").lower()

if user_name in names:
    print(f"The index of {user_name} is {names.index(user_name)}")
else:
    print(f"{user_name} is not in the list.")
