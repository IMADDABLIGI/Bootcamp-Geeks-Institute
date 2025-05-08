birthdays = {
    "Imad": "2001/02/23",
    "Driss": "1990/11/23",
    "Charlie": "1988/04/10",
    "Diana": "2001/09/05",
    "Ethan": "1993/12/30"
}

print("\nHere are the names you can choose from:")
for name in birthdays:
    print("-", name)

user_input = input("\nEnter the person's name: ")

if user_input in birthdays:
    print(f"\n{user_input}'s birthday is on {birthdays[user_input]}.")
else:
    print(f"\nSorry, we don’t have the birthday information for {user_input}.")
