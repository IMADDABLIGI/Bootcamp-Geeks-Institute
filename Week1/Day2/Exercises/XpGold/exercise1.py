birthdays = {
    "Imad": "2001/02/23",
    "Driss": "1990/11/23",
    "Charlie": "1988/04/10",
    "Diana": "2001/09/05",
    "Ethan": "1993/12/30"
}

name = input("Enter the person's name: ")

if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we don't have a birthday for {name}.")
