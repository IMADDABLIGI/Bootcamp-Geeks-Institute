number = input("Enter a number: ")

length = input("Enter the length of the numbers: ")

range = int(length)

multiplication = int(number)
mul = 1
i = 1

while i <= range:
    sum = i * multiplication
    print(sum)
    mul = sum
    i += 1

# print(f"This took me a while")