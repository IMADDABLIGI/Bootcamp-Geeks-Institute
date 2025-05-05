user_str = input("Enter a string: ")

i = 0
length = len(user_str)

new_str = ""

while i != length:
    if user_str[i] != user_str[i - 1]:
        new_str += user_str[i]
    i += 1


print(f"user's word : {user_str} ➞ {new_str}")