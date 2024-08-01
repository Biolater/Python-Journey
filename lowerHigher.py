import random
number = random.randint(1, 9)



def play_game():
    while True:
        try:
            guess = int(input("Guess a number between 1 and 9: "))
            if guess == number:
                print("You guessed correctly!")
                play_again()
                break
            elif guess < number:
                print("Higher")
                continue
            else:
                print("Lower")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
    
def play_again():
    choice = input("Do you want to play again? (y/n): ").lower().startswith("y")
    if choice:
        play_game()
    else:
        print("Thanks for playing!")    
    
play_game()    
