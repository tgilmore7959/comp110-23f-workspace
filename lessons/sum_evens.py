"""Practic summing over lists."""


def sum_evens_in_list(input_list: list[int]) -> int:
    """Adds up th even numbers."""
    list_sum: int = 0
    for number in input_list:
        if number % 2 == 0:
            list_sum = list_sum += number
    return list_sum  