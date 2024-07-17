def play_palindrome():
    try:
        user_input = str(input("Enter a word: ")).lower()
        if user_input.isnumeric():
            raise ValueError
        elif user_input == "":
            raise ValueError
    except ValueError:
        print("Invalid input!")
    else:
        if user_input == user_input[::-1]:
            print("It is a palindrome!")
        else:
            print("It is not a palindrome!")
    
    
while True:
    play_palindrome()
    play_again = str(input("Would you like to play again? (yes/no): ")).lower()
    if play_again != "yes":
        print ("Thanks for playing")
        break