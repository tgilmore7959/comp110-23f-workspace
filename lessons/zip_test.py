"""Test my zip function."""
__author__ = "730586444"


from lessons.zip import zip


def test_edge() -> None:
    """Tests one edge case."""
    test_list1 = ["cow", "moist"]
    test_list2 = [2]
    assert zip(test_list1, test_list2) == {}


def test_one_item_lists() -> None:
    """Tests one item lists."""
    test_list1 = ["cow"]
    test_list2 = [2]
    assert zip(test_list1, test_list2) == {"cow": 2}


def test_two_item_lists() -> None:
    """Test two item lists."""
    test_list1 = ["cow", "moist"]
    test_list2 = [2, 5]
    assert zip(test_list1, test_list2) == {"cow": 2, "moist": 5}
    