import random
#This is simple rock, paper, scissors game
# Rules of the game:
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
# If both players choose the same, it's a tie
# The game is played against the computer
# The computer randomly selects one of the three options
# The user selects one of the three options using console input (1 for Rock, 2 for Paper, 3 for Scissors)
# If user selects something other than 1, 2, or 3, the game informs about wrong selection
# and asks the user to select again
# Before starting the game, the game displays the rules of the game
# The game displays the user's choice and the computer's choice
# The result is displayed to console
# The user can play again or exit the game
# When the user exits the game, the game displays 
# the number of games won by the user and the computer,
# rounds played by the user and the computer
# and game thanks user for playing with the game/ computer
# The game is implemented using Python
def display_rules():
    print("Welcome to Rock, Paper, Scissors!")
    print("Rules of the game:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("If both players choose the same, it's a tie")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please choose (1 for Rock, 2 for Paper, 3 for Scissors):")
        except ValueError:
            print("Invalid input. Please enter a number (1 for Rock, 2 for Paper, 3 for Scissors):")

def get_computer_choice():
    return random.choice([1, 2, 3])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "user"
    else:
        return "computer"

def main():
    display_rules()
    user_wins = 0
    computer_wins = 0
    rounds_played = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
        print(f"You chose {choices[user_choice]}, Computer chose {choices[computer_choice]}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

        rounds_played += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        #if user enters anything other than 'yes' or 'no', the game will ask the user to enter again
        while play_again not in ["yes", "no"]:
            play_again = input("Invalid input. Please enter 'yes' or 'no': ").lower()
        if play_again != "yes":
            break

    print(f"Thanks for playing! You won {user_wins} times, the computer won {computer_wins} times, and you played {rounds_played} rounds.")

if __name__ == "__main__":
    main()
