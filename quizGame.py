questions = [
    {
        "question": "What is the capital of Canada?",
        "options": ["Ottawa", "Toronto", "Vancouver", "Calgary"],
        "answer": "Ottawa"
    },
    {
        "question": "What is the largest country in the world?",
        "options": ["Russia", "Canada", "China", "USA"],
        "answer": "Russia"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["Vatican City", "Monaco", "San Marino", "Liechtenstein"],
        "answer": "Vatican City"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    }
]

def start_game(questions):
    score = 0
    for question in questions:
        print("----------------------------------")
        print(question["question"])
        print ("Options:", question["options"])
        user_answer = input("Enter your answer: ")
        if user_answer == question["answer"]:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
        print("Score:", score)

    print("Game over. You scored", score, "out of", len(questions))
    
    

def play_again():
    play_again = input("Would you like to play again? (yes/no): ")
    if play_again.lower() == "yes":
        return True
    else:
        print("Thanks for playing!")
        return False

start_game(questions)

while play_again():
    start_game(questions)