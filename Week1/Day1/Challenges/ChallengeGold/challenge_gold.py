from datetime import datetime

birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")

birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")

current_date = datetime.now()

age = current_date.year - birthdate.year

if current_date.month < birthdate.month or (current_date.month == birthdate.month and current_date.day < birthdate.day):
    age -= 1

candles = age % 10

print(f"""
       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
      {'|:| ' * candles}
""")
