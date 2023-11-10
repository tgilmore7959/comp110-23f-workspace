"""One Shot Wordle."""
__author__ = "730585444"
# Setting word to guess
secret_word = "python"
#variables for emojis and guess input
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
#All Letter Boxes initially white
L0 = WHITE_BOX
L1 = WHITE_BOX
L2 = WHITE_BOX
L3 = WHITE_BOX
L4 = WHITE_BOX
L5 = WHITE_BOX
guess = ("")
#is it 6 letters?
while len(guess) != 6:
    guess = input("What is your 6 letter guess? ")
    if len(guess) != 6:
        print("That was not 6 letters! Try again:")
#Making Green Boxes while loop index variable created at 0 and counting up to 5 (6 letters)
#it starts with 0
index = 0
while index < 6:
    if guess[index] == secret_word[0] or guess[index] == secret_word[1] or guess[index] == secret_word [2] or guess[index] == secret_word[3] or guess[index] == secret_word[4] or guess[index] == secret_word[5]:
        if index == 0:
            L0 = YELLOW_BOX
        if index == 1:
            L1 = YELLOW_BOX
        if index == 2:
            L2 = YELLOW_BOX
        if index == 3:
            L3 = YELLOW_BOX
        if index == 4:
            L4 = YELLOW_BOX
        if index == 5:
            L5 = YELLOW_BOX
        index += 1
    else:
        ind = 0
        while ind < 6:
            if guess[ind] == secret_word[index]:
                if index == 0:
                    L0 = GREEN_BOX
                if index == 1:
                    L1 = GREEN_BOX
                if index == 2:
                    L2 = GREEN_BOX
                if index == 3:
                    L3 = GREEN_BOX
                if index == 4:
                    L4 = GREEN_BOX
                if index == 5:
                    L5 = GREEN_BOX
            ind += 1
        index += 1  




#printing the emojis 
print(f"{L0} {L1} {L2} {L3} {L4} {L5}") 
#is it correct?
if guess == secret_word:
    print("Woo! You got it!")
    exit()
else:
    guess != secret_word
    print("Not Quite. Play again soon!")
    exit()