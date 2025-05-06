import random

def random_generation(user_num):
    if user_num>= 1 and user_num<=100:
        random_num = random.randint(1, 100)
        print(f"User number: {user_num}\nRandom number: {random_num}")
        if user_num == random_num:
            print("success message")
        else:
            print("fail message")
    else:
        print("Please enter a number between 1 and 100.")


random_generation(99)