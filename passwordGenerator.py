import random
all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"


while True:
    try:
        number_of_passwords = int(input("How many passwords would you like to generate?: "))
        if number_of_passwords <= 0:
            raise ValueError
        password_length = int(input("How long would you like your password to be?: "))
        if password_length <= 0:
            raise ValueError
        
        print("\nHere are your passwords:\n")
        
        for i in range(number_of_passwords):
            password = ""
            for j in range(password_length):
                password+=random.choice(all_chars)
            print(password)
        
        
        break
    except ValueError:
        print("Invalid input!")