"""List utility functions."""
___author___ = 730585444


def all(inputlist: list[int], guess: int) -> bool:
    """Searches for guess within three intiger list."""
    # Checks if there was nothing entered for the list
    if len(inputlist) == 0:
        return False 
    # While loop that checks if the first number is a match then removes it
    while len(inputlist) != 0:
        number = inputlist[0]
        if number != guess:
            print("False")
            return False
        inputlist.pop(0)
    else:
        print("True")
        return True


def max(inputlist: list[int]) -> int:
    """Determines greatest value."""
    # Error for no input
    if len(inputlist) == 0:
        raise ValueError("max() arg is an empty list")
    # Initialize var
    index = 1
    max_number = inputlist[0]
    # Whle look goes thru each number makes max number the bigger of the two
    while index < len(inputlist):
        if max_number <= inputlist[index]:
            max_number = inputlist[index]
        index += 1
    return int(max_number)


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Are they the same?"""
    if len(list1) != len(list2):
        return False
    index = len(list1) - 1
    while index >= 0:
        if list1[index] != list2[index]:
            return False
        index -= 1      
    return True

        