import random

class Game:
    def get_user_item(self):
        choices = ['r', 'p', 's']
        while True:
            user_input = input("\nSelect (r)ock, (p)aper, (s)cissors: ").lower()
            # print(user_input)
            if user_input in choices:
                return user_input
            else:
                print("Invalid input. Please try again.")

    def get_computer_item(self):
        return random.choice(['r', 'p', 's'])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'draw'
        elif (user_item == 'r' and computer_item == 's'):
            return 'win'
        elif (user_item == 'p' and computer_item == 'r'):
            return 'win'
        elif (user_item == 's' and computer_item == 'p'):
            return 'win'
        else:
            return 'loss'

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"You selected {user_item}. The computer selected {computer_item}.")
        if result == "draw":
            print("You drew!")
        elif result == "win":
            print("You win!")
        else:
            print("You lose!")

        return result
