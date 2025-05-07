longest_sentence = ""

while True:
    user_sentence = input("Enter the longest sentence you can without the character 'A': ")

    if 'A' in user_sentence.upper():
        print("Your sentence contains 'A'. Try again!")
        continue
    
    if len(user_sentence) > len(longest_sentence):
        longest_sentence = user_sentence
        print("Congratulations! You've entered a new longest sentence!")
