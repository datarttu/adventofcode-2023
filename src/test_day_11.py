from day_11 import *


def test_read_expand():
    m = read_expand("../inputs/day_11_example.txt")
    assert m.shape == (12, 13)


def test_distances():
    m = read_expand("../inputs/day_11_example.txt")
    assert sum(distances(m)) == 374
