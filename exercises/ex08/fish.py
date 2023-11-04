"""File to define Fish class."""
__author__ = "730585444"


class Fish:
    """Fishes."""
    
    age: int

    def __init__(self) -> None:
        """Init."""
        self.age = 0
        return None
    
    def one_day(self) -> None:
        """Adds a day."""
        self.age += 1
        return None