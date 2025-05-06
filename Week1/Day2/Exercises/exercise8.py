data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

print("<----- Welcome to StarWarz Quiz ----->")
print("Let’s test your knowledge")
print("|--------------------------------------------|")

correct = 0
incorrect = 0

for qst in data:
    dic = dict(qst)
    print(f"Question: ", dic["question"])
    user_answer = input("Answer: ").lower()
    # print(user_answer, "||||", dic["answer"])
    if user_answer == dic["answer"].lower():
        print("Correct")
        correct += 1
    else:
        print("Incorrect")
        incorrect += 1
    print("|-----------------------------|")


print("|--------------------------------------------------------------------|")
print("|--------------------------- Final Result ---------------------------|")
print("|--------------------------------------------------------------------|")

print(f"|---     You got {correct} correct questions and {incorrect} incorrect questions    ---|")
print("|____________________________________________________________________|")
