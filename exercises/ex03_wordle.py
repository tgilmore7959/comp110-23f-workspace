"""Wordle."""
__author__ = "730585444"
# Bringing in the box emojis as variables
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word = "codes"
guess = ""
letter_guess = ""
# Function to search if a letter is present in the world
def contains_char(secret_word: str, letter_guess: str) -> bool:
    """Searches word for guess letter and returns true or false."""
    assert len(letter_guess) == 1
    index = 0
    present = False
    while index < len(secret_word):
        if secret_word[index] == letter_guess:
            present = True
        index += 1
    return present   


def emojified(secret_word: str, guess: str) -> str:
    """Compares secret_word and Guess returns box emojis."""
    assert len(guess) == len(secret_word)
    # Setting up variables
    index = 0
    result = ""
    while index < len(secret_word):
        if secret_word[index] == guess[index]:
            result += GREEN_BOX
        elif contains_char(secret_word, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result

def input_guess(char_num: int) -> str:
    """Compares input number of characters to input guess"""
    # Sets guess to input term and compares to number of letters allowed returns try again if not eq
    guess = input(f"Enter a {char_num} character word: ")
    while len(guess) != char_num:
        guess = input(f"That wasn't {char_num} chars! Try Again: ")
    return (guess)

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1
    win = False
    number_of_turns = 6
    while turn <= number_of_turns and win == False:
        print(f"=== Turn {turn}/6 ===")
        # Runs input guess with secret_word length and prompts user
        guess = input_guess(len(secret_word))
        # adds emojiboxes
        result = emojified(secret_word, guess)
        print(result)
        if secret_word == guess:
            win = True
            print(f"You won in {turn}/6 turns!")        
        turn += 1
    # exits look if true and not yet 6 trys
    if win == True:
        exit()
    print(f"X/6 - Sorry, Try again tomorrow!")


if __name__ == "__main__":
    main()