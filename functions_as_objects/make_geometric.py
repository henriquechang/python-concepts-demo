import math
from operator import mul
from functools import reduce


def make_geometric():
    series = []

    def multiplier(new_value):
        series.append(new_value)
        total = reduce(mul, series)
        return math.pow(total, 1/len(series))
    return multiplier


def make_geometric_nonlocal():
    count = 0
    total = 1

    def multiplier(new_value):
        nonlocal count, total
        count += 1
        total *= new_value
        return math.pow(total, 1/count)
    return multiplier
