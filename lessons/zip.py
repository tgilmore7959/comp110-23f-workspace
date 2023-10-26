"""Combining two lists into a dictionary."""
__author__ = "730585444"


def zip(input_list1: list[str], input_list2: list[int]) -> dict[str, int]:
    """Input two lists, get a dict."""
    zipdict: dict[str, int] = {}
    if len(input_list1) == 0 or len(input_list2) == 0:
        return zipdict
    if len(input_list1) != len(input_list2):
        return zipdict
    for item1, item2 in zip(input_list1, input_list2):
        zipdict[item1] = item2
    return zipdict
