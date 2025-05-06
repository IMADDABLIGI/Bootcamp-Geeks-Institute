import random

def get_random_temp(season):
    if season == "winter":
        random_num = random.randint(-10, 16)
    if season == "autumn":
        random_num = random.randint(17, 23)
    if season == "spring":
        random_num = random.randint(24, 31)
    if season == "summer":
        random_num = random.randint(32, 40)
    return int(random_num)

# print(get_random_temp())

def main():
    season = ""
    while True:
        season = input("Please type in a season (summer|autumn|winter|spring) : ").lower()
        if season == "winter" or season == "autumn" or season == "spring" or season == "summer":
            break

    random_num = get_random_temp(season)
    print(f"The temperature right now is {random_num} degrees Celsius.")
    if random_num < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 <= random_num < 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 <= random_num <= 23:
        print("Kayn chwiya dl berd f sbah")
    elif 24 <= random_num < 32:
        print("Bda ys5on l7all")
    elif 32 <= random_num <= 40:
        print("Kayn sahd lyouma")

    
main()