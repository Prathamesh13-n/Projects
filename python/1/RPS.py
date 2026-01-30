import random
# random module is used to generate the computer choice

# Printing the rules of the game
print(
    "Some rules are there to win this game\n"
    "Rock vs Paper means Paper wins\n"
    "Rock vs Scissors means Rock wins\n"
    "Paper vs Scissors means Scissors wins\n"
)

# Main loop so the game can be played again and again
while True:

    # Asking the user to enter their choice
    print("Enter the choices")
    print("1 Rock")
    print("2 Paper")
    print("3 Scissors")

    # Taking input from the user
    choice = int(input("Enter a number between 1 and 3: "))

    # Checking if the entered choice is valid
    # User must enter only 1, 2, or 3
    while choice < 1 or choice > 3:
        print("Invalid choice. Please enter between 1 and 3.")
        choice = int(input("Enter a number between 1 and 3: "))

    # Assigning name to user choice
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"

    # Displaying user choice
    print("User choice is:", choice_name)

    # Computer randomly selects a choice
    print("Now it is computer turn")
    comp_choice = random.randint(1, 3)

    # Assigning name to computer choice
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"

    # Displaying computer choice
    print("Computer choice is:", comp_choice_name)

    # Deciding the winner
    if choice == comp_choice:
        result = "Draw"
    elif (choice == 1 and comp_choice == 3) or \
         (choice == 2 and comp_choice == 1) or \
         (choice == 3 and comp_choice == 2):
        result = "User"
    else:
        result = "Computer"

    # Printing the result
    if result == "Draw":
        print("It is a tie")
    elif result == "User":
        print("User wins the game")
    else:
        print("Computer wins the game")

    # Asking user if they want to play again
    ans = input("Do you want to play again Y or N: ").lower()

    if ans == "n":
        break

# Final message after game ends
print("Thanks for playing this game. Come again")
