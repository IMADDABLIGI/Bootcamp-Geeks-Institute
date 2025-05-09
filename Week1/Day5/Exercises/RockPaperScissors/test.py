import random

list = ["r", "p", "s"]
print("|--- Welcome to Rock, Paper, Scissors Game---|")
wins = 0
losts = 0
draw = 0


try:
    while True:
        print("(g) -> Play a new game")
        print("(x) -> show scores and exit")
        c = input("-> ").lower()
        if (c == 'g' or c == 'x'):
            if c == 'g':
                u_i = input("\nSelect (r)ock, (p)aper, (s)cissors: ").lower() #u_i : user input
                if not u_i in list:
                    continue
                random_num = random.randint(0, 2)
                r_i = list[random_num]
                print(f"\n\n----You chouse {u_i}. the computer chose: {r_i}.---\n")
                if (r_i == u_i):
                    print("|--- Result : Draw ---|")
                    draw += 1
                elif (u_i == 'r' and r_i == 's'):
                    print("|--- Result : Win ---|")
                    wins += 1
                elif (u_i == 'p' and r_i == 'r'):
                    print("|--- Result : Win ---|")
                    wins += 1
                elif (u_i == 's' and r_i == 'p'):
                    print("|--- Result : Win ---|")
                    wins += 1
                else:
                    print("|--- Result : Lost ---|")
                    losts += 1
                print("\n")
            elif c == 'x':
                print("|----- Game Result: --------|")
                print(f"You won {wins}")
                print(f"You lost {losts}")
                print(f"You drew {draw}")

                print("Thank you for playing!")
                break

except KeyboardInterrupt:
    print("\n\nGood Bye Stuff :/")  