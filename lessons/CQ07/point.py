"""CQ07."""
from __future__ import annotations
__author__ = "740585444"


class Point:
    x: float
    y: float


def __init__(self, x_int: float, y_int: float):
    self.x = x_int
    self.y = y_int


def scale_by(self, factor: int) -> None:
    """Updates X,Y by a factor."""
    self.x *= factor
    self.y *= factor


def scale(self, factor: int) -> Point:
    """Returns a new point with X and Y equal to self.x * factor and self.y * factor."""
    new_point: Point = Point()
    new_point.x = self.x * factor
    new_point.y = self.y * factor
    return new_point
