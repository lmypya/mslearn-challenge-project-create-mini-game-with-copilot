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
# The result is displayed to console
# The user can play again or exit the game
# When the user exits the game, the game displays the number of games won by the user and the computer
# and game thanks user for playing with the game/ computer
# The game is implemented using Python
def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
            if choice in [1, 2, 3]:
                return ["Rock", "Paper", "Scissors"][choice - 1]
            else:
                print("Invalid choice. Please select again.")
        except ValueError:
            print("Invalid input. Please enter a number 1 for Rock, 2 for Paper, 3 for Scissors:")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "User"
    else:
        return "Computer"

def display_welcome_message():
    print("Welcome to Rock, Paper, Scissors game!")
    print("Rules of the game:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("If both players choose the same, it's a tie")
    print("Let's start the game!")
    print()

def main():
    display_welcome_message()
    user_wins = 0
    computer_wins = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "User":
            print("You win!")
            user_wins += 1
        elif winner == "Computer":
            print("Computer wins!")
            computer_wins += 1
        else:
            print("It's a tie!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Final score - User: {user_wins}, Computer: {computer_wins}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
