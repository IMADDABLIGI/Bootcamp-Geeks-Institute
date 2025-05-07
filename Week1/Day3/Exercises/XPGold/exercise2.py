class MyList:
    def __init__(self, letters):
        self.letters = letters

    def get_reverts_letters(self):
        return self.letters[::-1]
    
    def get_sorted_letters(self):
        return sorted(self.letters)

my_list = MyList(['I', 'M', 'A', 'D'])

print("Reversed:", my_list.get_reverts_letters())
print("Sorted:", my_list.get_sorted_letters())   