"""Summing the elements of a list using different loops."""
___author___ = 730585444


def w_sum(vals: list[float]) -> float:
    sum = 0.0
    index = 0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum2 = 0.0
    for elem in vals:
       sum2 += elem
    return sum2

def f_range_sum(vals: list[float]) -> float:
    sum3 = 0.0
    for index in range(len(vals)):
        sum3 += vals[index]
    return sum3
