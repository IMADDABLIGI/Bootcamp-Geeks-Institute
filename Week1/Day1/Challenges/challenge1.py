number = input("Enter a number: ")

length = input("Enter the length of the numbers: ")

range = int(length)

multiplication = int(number)
mul = 1
i = 1

my_list = []

while i <= range:
    sum = i * multiplication
    my_list.append(sum)
    mul = sum
    i += 1

print(f"number: {number} - length {length} ➞ {my_list}")
# print(f"This took me a while")