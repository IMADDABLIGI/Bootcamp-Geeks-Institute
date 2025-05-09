from game import Game

def get_user_menu_choice():
    print("\n(g) -> Play a new game")
    print("(x) -> Show scores and exit")
    choice = input("-> ").lower()
    if choice in ['g', 'x']:
        # print(choice)
        return choice
    else:
        print("Try again a cheriff.")
        return None

def print_results(results):
    print("\n|--- Game Results ---|")
    print(f"Wins: {results.get('win', 0)}")
    print(f"Losses: {results.get('loss', 0)}")
    print(f"Draws: {results.get('draw', 0)}")
    

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    print("|--- Welcome to Rock, Paper, Scissors Game---|")
    try:
        while True:
            choice = get_user_menu_choice()
            if not choice:
                continue
            if choice == 'g':
                game = Game()
                result = game.play()
                results[result] += 1
            elif choice == 'x':
                print_results(results)
                break
    except KeyboardInterrupt:
        print("\n\nGood Bye Stuff :/")  

if __name__ == "__main__":
    main()
