class Bank:
    def __init__(self):
        print("Initialized Bank Class")
        self.__name = "CIH"
        self.location = "Casablanca"
    
    def get__name(self):
        return(self.__name)
    
    def __make_deposit(self):
        print("Making Deposit")

cih = Bank()

print(cih._Bank__name)
cih._Bank__make_deposit()
print(cih.location)
print(cih.get__name())
    
