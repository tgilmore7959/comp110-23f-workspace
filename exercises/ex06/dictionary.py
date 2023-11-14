"""Dictionary Functions."""


__author__ = "730585444"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the strings."""
    output_dict = dict()
    for key in input_dict:
        value = input_dict[key]
        # Dup check
        if value in output_dict:
            raise KeyError(f"Duplicate found: {value}")
        # switcheroo
        output_dict[value] = key
    return output_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Finds most popular color."""
    # Creates a dictionary that will have the color and count
    color_count: dict[str, int] = {}
    # Cycles through checks if in dict if so, adds one if not, adds the color
    for name in color_dict:
        color = color_dict[name]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    # Making a counter high number gets replaced
    favorite: str = ""
    high_number = 0
    for color in color_count:
        count = color_count[color]
        if count > high_number:
            favorite = color
            high_number = count
    return favorite
        

def count(input_list: list[str]) -> dict[str, int]:
    """Word Counter from list."""
    output_dict: dict[str, int] = {}
    for item in input_list:
        if item in output_dict:
            output_dict[item] += 1
        else:
            output_dict[item] = 1
    return output_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Alphabetizes and categorizes by letter."""
    new_dict: dict[str, list[str]] = {}
    for word in input_list:
        # Gets first letter
        first_letter = word[0].lower()
        # Checks if in dict
        if first_letter not in new_dict:
            # adds if not in there
            new_dict[first_letter] = []
        # adds word    
        new_dict[first_letter].append(word)
    return new_dict


def update_attendance(attend: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Takes current list of attendence and adds students."""
    # checks if day in log and adds if nec
    if day not in attend:
        attend[day] = []
    # adds student to the day 
    if student not in attend[day]:   
        attend[day].append(student)
    return attend