"""Wordle."""
__author__ = "730585444"


def contains_char(word: str, guess: str) -> bool:
    """searches word for guess letter and returns true or false"""
    assert len(guess) == 1
    index = 0
    present = False
    while index < len(word):
        if word[index] == guess:
            present = True
        index +=1
    return present   

print(contains_char("abc", "a"))
