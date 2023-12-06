from day_06 import *


def test_solve1():
    TIMES_ALLOWED = [7, 15, 30]
    DISTANCES_RECORDED = [9, 40, 200]
    res = solve(TIMES_ALLOWED, DISTANCES_RECORDED)
    assert res == 288
