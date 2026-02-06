import random
# random module is used to generate a secret random number

# Generate a random 4-digit number between 1000 and 9999
num = random.randrange(1000, 10000)

# Convert the number to string so we can compare digit by digit
num_str = str(num)

# Total chances (lives) given to the player
lives = 7

# Keeps track of how many attempts the user has made
attempt = 1

print("You have", lives, "lives to guess the 4-digit number.")
print("Hint: You will be told if any digit is in the correct position.\n")

# Take the first guess from the user
n = int(input("Guess the 4 digit number: "))

# Loop continues until:
# 1) User guesses the correct number OR
# 2) User runs out of lives
while n != num and lives > 1:

    # Convert the user's guess to string for digit comparison
    # zfill(4) ensures the number has exactly 4 digits
    n_str = str(n).zfill(4)

    # total_match counts how many digits exist in the secret number
    # (regardless of position)
    total_match = 0

    # correct_position checks if at least ONE digit is in the right place
    correct_position = False

    # Loop through each digit position (0 to 3)
    for i in range(4):

        # If digit matches AND position is same
        if n_str[i] == num_str[i]:
            total_match += 1
            correct_position = True

        # If digit exists in the secret number but position is different
        elif n_str[i] in num_str:
            total_match += 1

    # Feedback to the user
    if total_match > 0:
        print("Matched digits (any position):", total_match)
    else:
        print("No digits matched.")

    # YES / NO information for correct position
    if correct_position:
        print("Correct position present: YES")
    else:
        print("Correct position present: NO")

    # One life is used after every wrong guess
    lives -= 1

    # Increase attempt count
    attempt += 1

    print("Lives left:", lives)
    print()

    # Ask for the next guess
    n = int(input("Enter your next guess: "))

# When the loop ends, check final result
if n == num:
    # User guessed correctly
    print("\n🎉 You've become a Mastermind!")
    print("Attempts used:", attempt)
else:
    # User ran out of lives
    print("\n💀 Game Over!")
    print("The correct number was:", num)
