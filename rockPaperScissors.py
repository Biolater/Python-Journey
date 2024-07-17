import random

moves = ["rock", "paper", "scissors"]

def play_game():
    computer_move = random.choice(moves)
    player_move = str(input("Enter your move: (rock, paper, scissors): ")).lower()

    while player_move not in moves:
        print("Please enter a valid move")
        player_move = str(input("Enter your move: (rock, paper, scissors): ")).lower()

    if player_move == computer_move:
        print(f"It's a tie! Both chose {player_move}.")
    elif player_move == "rock" and computer_move == "scissors":
        print(f"You win! {player_move} beats {computer_move}.")
    elif player_move == "rock" and computer_move == "paper":
        print(f"You lose! {computer_move} beats {player_move}.")
    elif player_move == "paper" and computer_move == "rock":
        print(f"You win! {player_move} beats {computer_move}.")
    elif player_move == "paper" and computer_move == "scissors":
        print(f"You lose! {computer_move} beats {player_move}.")
    elif player_move == "scissors" and computer_move == "paper":
        print(f"You win! {player_move} beats {computer_move}.")
    elif player_move == "scissors" and computer_move == "rock":
        print(f"You lose! {computer_move} beats {player_move}.")

while True:
    play_game()
    play_again = str(input("Would you like to play again? (yes/no): ")).lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
