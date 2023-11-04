"""File to define Bear class."""
__author__ = "730585444"


class Bear:
    """Bears."""

    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Initializing class."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self) -> None:
        """One day goes by."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Reduces (increases score) hunger after eating."""
        self.hunger_score += num_fish
        return None