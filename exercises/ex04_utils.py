"""List utility functions."""
___author___ = 730585444


def all(inputlist: list, guess: int) -> bool:
    """Searches for guess within three intiger list."""
    while len(inputlist) != 0:
        number = inputlist[0]
        if number != guess:
            print("False")
            return False
        inputlist.pop(0)
    else:
        print("True")
        return True


def max(inputlist: list) -> int:
    """Determines greatest value."""
    if len(inputlist) == 0:
        raise ValueError("max() arg is an empty list")
    index = 1
    max_number = inputlist[0]
    while index < len(inputlist):
        if max_number <= inputlist[index]:
            max_number = inputlist[index]
        index += 1
    return max_number


def is_equal(list1: list, list2: list) -> True:
    """Are they the same?"""
    if len(list1) != len(list2):
        return False
    index = len(list1) - 1
    while index >= 0:
        if list1[index] != list2[index]:
            return False
        index -= 1      
    return True

        