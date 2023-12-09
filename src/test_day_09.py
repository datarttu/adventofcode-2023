from day_09 import *


def test_extrapolate():
    assert extrapolate([0, 3, 6, 9, 12, 15]) == 18


def test_example():
    result = sum([extrapolate(nl) for nl in read_input("../inputs/day_09_example.txt")])
    assert result == 114
