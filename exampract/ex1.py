"""Practice Stuff."""


def odds_and_evens(input_list: list[int]) -> list[int]:
    """Finds odd with even index."""
    index: int = 0
    new_list: list[int] = []
    while len(input_list) > index:
        if index % 2 == 0 and input_list[index] % 2 == 1:
            new_list.append(input_list[index])
            index += 1
        else:
            index += 1
    return new_list


def short_words(words: list[str]) -> list[str]:
    """Creates new list with words less than 5 letters."""
    new_list: list[str] = []
    index: int = 0
    while index < len(words):
        if len(words[index]) > 4:
            print(f"{words[index]} is too long")
            index += 1
        else:
            new_list.append(words[index])
            index += 1
    return new_list
