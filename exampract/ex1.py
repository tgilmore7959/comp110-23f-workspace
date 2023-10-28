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