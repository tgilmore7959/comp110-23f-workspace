"""EX07 'dict' unit tests"""
__author__ = "730585444"


from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance
import pytest

# Invert Tests
def test_blank() -> None:
    """Tests blank input."""
    test_dict = {}
    assert invert(test_dict) == {}

def test_one() -> None:
    """Tests one item dict."""
    test_dict = {"cow": "moist"}
    assert invert(test_dict) == {"moist": "cow"}

def test_two() -> None:
    """Tests two dict."""
    test_dict = {"moist": "cow", "happy": "horse"}
    assert invert(test_dict) == {"cow": "moist", "horse": "happy"}

def test_Keyerror() -> None:
    """Tests duplicate in dict."""
    with pytest.raises(KeyError):
        test_dict = {"moist": "cow", "happy": "cow"}
        invert(test_dict)

# Testing favorite_color
def test_blank_favorite_color() -> None:
    """Tests blank favorite color."""
    test_dict = {}
    assert favorite_color(test_dict) == ""

def test_one_favorite_color() -> None:
    """Tests list of one."""
    test_dict = {"Danny": "orange"}
    assert favorite_color(test_dict) == "orange"

def test_two_favorite() -> None:
    """Tests two of three and pics greater."""
    test_dict = {"Danny": "orange", "Daddy": "orange", "Me": "black"}
    assert favorite_color(test_dict) == "orange"

# Testing count

def test_count_blank() -> None:
    """Tests empty dict."""
    test_dict = {}
    assert count(test_dict) == {}

def test_count_one() -> None:
    """Tests counting one item."""
    test_list = ["fourtytwo"]
    assert count(test_list) == {"fourtytwo": 1}

def test_count_multiple() -> None:
    """Tests multiple items."""
    test_list = ["fourtytwo", "fourtytwo", "moist"]
    assert count(test_list) == {"fourtytwo": 2, "moist": 1}

# Testing alphabetizer

def test_alph_blank() -> None:
    """Tests blank alphabetizer."""
    test_list = []
    assert alphabetizer(test_list) == {}

def test_alph_one() -> None:
    """Tests one item in list."""
    test_list = ["moist"]
    assert alphabetizer(test_list) == {"m": ["moist"]}

def test_alph_three() -> None:
    """Tests three items."""
    test_list = ["moist", "man", "pretty"]
    assert alphabetizer(test_list) == {"m": ["moist", "man"], "p": ["pretty"]}
    
# Testing Attendance

def test_attend_blank() -> None:
    """Testing blank for error."""
    test_dict = {}
    with pytest. raises(TypeError):
        update_attendance(test_dict)

def test_one_attend() -> None:
    """Tests one attendence entry."""
    test_dict = {}
    assert update_attendance(test_dict, "monday", "Tommy") == {"monday": ["Tommy"]}

def test_three_attend() -> None:
    """Tests three items."""
    test_dict ={"tuesday": ["Billy"], "Monday": ["Sally"]}
    assert update_attendance(test_dict, "Monday", "Gertrude") == {"tuesday": ["Billy"], "Monday": ["Sally", "Gertrude"]}

