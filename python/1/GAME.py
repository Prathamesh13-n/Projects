# Import random module to select a random word
import random

# Store fruit names in a single string
somewords = """apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon"""

# Convert the string into a list so a random word can be chosen
somewords = somewords.split()

# Select one random word from the list
word = random.choice(somewords)

# Execute the game only when this file is run directly
if __name__ == "__main__":

    # Display game instructions
    print("Guess the word!")
    print("Hint: The word is a fruit")

    # Display hidden word using underscores
    for _ in word:
        print("_", end=" ")
    print()

    # Store all letters guessed by the user
    letter_guessed = ""

    # Number of chances depends on the length of the word
    chances = len(word) + 2

    # Flag is used to check whether the user has won
    flag = 0

    try:
        # Continue the game until chances are over or the word is guessed
        while chances > 0 and flag == 0:

            # Show remaining chances
            print("\nRemaining chances:", chances)

            # Take a letter input from the user
            guess = input("Enter a letter to guess: ").lower()

            # Ensure the input contains only alphabet letters
            if not guess.isalpha():
                print("Enter only alphabet letters")
                continue

            # Ensure only one letter is entered
            elif len(guess) != 1:
                print("Enter only one letter")
                continue

            # Prevent guessing the same letter again
            elif guess in letter_guessed:
                print("You already guessed that letter")
                continue

            # Store the guessed letter
            letter_guessed += guess

            # Reduce chances only if the guessed letter is wrong
            if guess not in word:
                chances -= 1

            # Display the word with guessed letters and remaining blanks
            for char in word:
                if char in letter_guessed:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
            print()

            # Check if all letters of the word are guessed
            if set(word).issubset(set(letter_guessed)):
                print("Congratulations, you won!")
                print("The word was:", word)
                flag = 1

        # Display loss message if chances are finished
        if flag == 0:
            print("You lost! Try again")
            print("The word was:", word)

    # Handle keyboard interruption safely
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye")
        exit()
