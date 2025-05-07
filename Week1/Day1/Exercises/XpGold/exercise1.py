month = int(input("Enter a month (1 to 12): "))

if month >= 3 and month <= 5:
    print("It's Spring!")
elif month >= 6 and month <= 8:
    print("It's Summer!")
elif month >= 9 and month <= 11:
    print("It's Autumn!")
elif month == 12 or month == 1 or month == 2:
    print("It's Winter!")
else:
    print("Invalid month! Please enter a number between 1 and 12.")
