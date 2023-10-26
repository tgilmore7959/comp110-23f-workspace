"""Testing my smmation function."""

from lessons.sum_evens import sum_evens_in_list

def test_empty_sum() -> None:
    """sum_evens_in_list of empty list should be 0."""
    assert sum_evens_in_list([]) == 0

def test_list_length_1() -> None:
    """Testing on a list of one element"""
    test_list: list[int] = [2]
    assert sum_evens_in_list == 2
    