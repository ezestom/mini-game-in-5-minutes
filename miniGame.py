# Create a rock, paper, scissors game with in to console with python

def main():
    # Import random module
    import random

    # Create a list of choices
    choices = ["rock", "paper", "scissors"]

    # Create a variable for the computer choice
    computer = random.choice(choices)

    # Create a variable for the user choice
    user = None

    # Create a while loop to check if the user choice is valid
    while user not in choices:
        # Ask the user for their choice
        user = input("Rock, paper, or scissors?: ").lower()

    # Check if the user and computer choices are the same
    if user == computer:
        print("Computer: ", computer)
        print("User: ", user)
        print("Tie!")

    # Check if the user chooses rock
    elif user == "rock":
        # Check if the computer chooses paper
        if computer == "paper":
            print("Computer: ", computer)
            print("User: ", user)
            print("You lose!")
        # Check if the computer chooses scissors
        else:
            print("Computer: ", computer)
            print("User: ", user)
            print("You win!")

    # Check if the user chooses paper
    elif user == "paper":
        # Check if the computer chooses scissors
        if computer == "scissors":
            print("Computer: ", computer)
            print("User: ", user)
            print("You lose!")
        # Check if the computer chooses rock
        else:
            print("Computer: ", computer)
            print("User: ", user)
            print("You win!")

    # Check if the user chooses scissors
    elif user == "scissors":
        # Check if the computer chooses rock
        if computer == "rock":
            print("Computer: ", computer)
            print("User: ", user)
            print("You lose!")
        # Check if the computer chooses paper
        else:
            print("Computer: ", computer)
            print("User: ", user)
            print("You win!")

    # Check if the user choice is invalid
    else:
        print("Invalid choice!")

    # Ask the user if they want to play again
    play_again = input("Play again? (y/n): ").lower()

    # Check if the user wants to play again
    if play_again == "y":
        # Restart the game
        main()
    else:
        # Say goodbye
         print("Goodbye!")

# Call the main function
main()




