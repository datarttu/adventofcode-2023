from day_4 import *


def test_card_points():
    cards = read_cards("../inputs/day_4_example.txt")
    results = [card_result(c) for c in cards]
    assert results == [8, 2, 2, 1, 0, 0]


def test_total():
    assert game("../inputs/day_4_example.txt") == 13


def test_copying_game():
    result = copying_game("../inputs/day_4_example.txt")
    assert result == 30
