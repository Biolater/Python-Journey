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
    for i, question in enumerate(questions):
        print(f"\n\nQuestion {i+1}: {question["question"]}")
        print(f"Options: {question["options"]}")
        user_answer = input("Enter your answer: ")
        while user_answer not in question["options"]:
            user_answer = input("Invalid answer. Please enter a valid option: ")
        if user_answer == question["answer"]:
            score+=1
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is: {question["answer"]}")
    print(f"Score: {score}")        

def play_again():
    play_again = str(input("Do you want to play again? (yes/no): ")).lower()
    if play_again != "yes":
        print("Thanks for playing!")
        return False
    else:
        print("Let's play again!")
        return True

start_game(questions)

while play_again():
    start_game(questions)