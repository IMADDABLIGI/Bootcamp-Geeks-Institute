user_input = input("Type some words separated by commas: ")
words = user_input.split(",")
words.sort()
result = ",".join(words)

print("Here are your sorted words:")
print(result)
