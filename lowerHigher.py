import random
total_guesses = 0
random_number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        total_guesses += 1
        if guess < random_number:
            print("Too low, try again!")
        elif guess > random_number:
            print("Too high, try again!")
        elif guess == random_number:
            break

    except ValueError:
        print("Invalid input!")

print(f"You guessed the number in {total_guesses} guesses!")10