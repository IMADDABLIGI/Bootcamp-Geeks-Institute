def calculate_pattern(x):

    # print(str(x))
    x_str = str(x)
    total = int(x_str) + int(x_str * 2) + int(x_str * 3) + int(x_str * 4)
    return total

result = calculate_pattern(3)
# print(result)
print(result)
