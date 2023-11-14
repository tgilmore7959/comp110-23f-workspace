"""CQ07."""
from __future__ import annotations
__author__ = "740585444"


class Point:
    x: float
    y: float

    def __init__(self, x_int: float, y_int: float):
        """Init."""
        self.x = x_int
        self.y = y_int

    def scale_by(self, factor: int) -> None:
        """Updates X,Y by a factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int | float) -> Point:
        """Returns a new point with X and Y equal to self.x * factor and self.y * factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point

    def __str__(self) -> str:
        return f"x: {self.x}; y: {self.y}"


    def __add__(self, add: int | float) -> Point:
        """Adds add to both x and y."""
        return Point(self.x + add, self.y + add)