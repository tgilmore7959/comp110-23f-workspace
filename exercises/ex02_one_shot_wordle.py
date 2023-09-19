"""One Shot Wordle."""
__author__ = "730585444"
# I wrote a version that got to the yellow box step and absolutly didn't work...rewriting with
# the knowlege that I'll have to change number of letters etc =)
# Setting word to guess
secret_word = "python"
# variables for emojis and number of letters
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# determine number of letters in sec word
number_of_letters = len(secret_word)
# prompt and set var guess
guess = input(f"What is your {number_of_letters}-letter guess? ")
# is it less than
while len(guess) != number_of_letters:
    guess = input(f"That was not {number_of_letters} letters! Try again: ")
# variable for emoji box output
result = ""
# checking for matching (green)
index = 0
while index < number_of_letters:
    if guess[index] == secret_word[index]:
        result += GREEN_BOX + " "
# loop to search all index and if present it gets a yellow box  if false it gets white box then it
# goes back to increase index and repeat ind search.
    else:
        ind = 0
        present = False
        while ind < number_of_letters:
            if guess[index] == secret_word[ind]:
                present = True
            ind += 1
        if present:
            result += YELLOW_BOX + " "
        else:
            result += WHITE_BOX + " "
    index += 1
# printing result emoji boxes
print(result)
# right or wrong
if guess == secret_word:
    print("Woo! You got it!")
    exit()
else:
    guess != secret_word
    print("Not Quite. Play again soon!")
    exit()    
