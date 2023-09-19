""" One Shot Wordle """
__author__ = "730585444"
# Setting word to guess
secret_word = "python"
#variables for emojis and guess input
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
number_of_letters = 6
#prompt and set var guess
guess = input (f"What is your {number_of_letters}-letter guess? ")
