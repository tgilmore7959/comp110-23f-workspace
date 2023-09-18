### One Shot Wordle ###
__author__ = "730585444"
###Setting word to guess
secret_word = "python"
###variables for emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
###is it 6 letters?
while True:
    guess: str = input("What is your 6-letter guess? ")
    if len(guess) == 6:
        break
    else: 
        print("That was not 6 letters! Try again: ")
if guess[0] == secret_word[0]:
    print(GREEN_BOX)
if str(guess) == secret_word:
    print("Woo! You got it!")
else:
    print("Not Quite. Play again soon!")    