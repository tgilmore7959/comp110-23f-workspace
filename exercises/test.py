""" One Shot Wordle """
__author__ = "Your Student PID"

# Set the secret word
secret_word = "python"

# Constants for emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Prompt for a guess
guess = input("What is your 6-letter guess? ")

# Check if the guess is 6 letters
while len(guess) != 6:
    print("That was not 6 letters! Try again:")
    guess = input("What is your 6-letter guess? ")

# Initialize variables for emojis
result = ""

# Check each index for correct matches
index = 0
while index < 6:
    if guess[index] == secret_word[index]:
        result += GREEN_BOX
    else:
        index2 = 0
        found = False
        while index2 < 6 and not found:
            if guess[index] == secret_word[index2]:
                found = True
            index2 += 1
        if found:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    index += 1

# Print the emoji result
print(result)

# Check if the guess is correct
if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")