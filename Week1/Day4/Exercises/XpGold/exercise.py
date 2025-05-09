class BankAccount:
    def __init__(self, username, password, balance=0):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            print(f"Welcome {username} you are now authenticated")

    
    def deposit(self, money):
        if not self.authenticated:
            raise Exception("You are not authenticated to make a deposit")
        if money <= 0:
            raise Exception("You can't deposit a negative number")
        self.balance += money
        print(f"You have deposit this ammount of money {money}, your new balance is {self.balance}")
    
    def withdraw(self, money):
        if not self.authenticated:
            raise Exception("You are not authenticated to make a withdraw")
        if money <= 0:
            raise Exception("You can't withdraw a negative number")
        self.balance -= money
        print(f"You have withdrawed this ammount of money {money}, your new balance is {self.balance}")


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, money):
        if self.balance > self.minimum_balance:
            super(MinimumBalanceAccount, self).withdraw(money)
        else:
            raise Exception("Your balance is not higher than your minimum_balance")

try:
    Hmad = MinimumBalanceAccount("Imad", "1234", 50, 20)
    # Hmad.deposit(2)
    Hmad.authenticate("Imad", "1234")
    Hmad.withdraw(2)
    Hmad.deposit(200)
    Hmad.withdraw(0.5)

except Exception as e:
    print(e)
