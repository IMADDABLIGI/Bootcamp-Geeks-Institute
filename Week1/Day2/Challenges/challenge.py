user_word = input("Please type a word: ")

dic = {}

for key, value in enumerate(user_word):

    value = str(value)
    if value in dic:
        dic[value].append(key)
    else:
        dic[value] = [key]
    # pass
    
print(dic)

    
    
    

