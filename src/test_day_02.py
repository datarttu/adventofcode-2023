from day_02 import *


def test_rgb_equality_gt():
    a = RGB(1, 2, 3)
    b = RGB(1, 2, 1)
    assert a > b


def test_rgb_equality_eq():
    a = RGB(1, 2, 3)
    b = RGB(1, 2, 3)
    assert a == b


def test_rgb_addition():
    a = RGB(1, 2, 3)
    b = RGB(1, 2, 3)
    assert a + b == RGB(2, 4, 6)


def test_rgb_maxels():
    a = RGB(1, 2, 3)
    b = RGB(3, 2, 1)
    assert a.maxels(b) == RGB(3, 2, 3)
    assert b.maxels(a) == RGB(3, 2, 3)


def test_rgb_from_string_simple():
    a = RGB.from_string("8 green, 6 blue, 20 red")
    assert a == RGB(20, 8, 6)


def test_rgb_from_string_with_missing():
    a = RGB.from_string("2 green")
    assert a == RGB(0, 2, 0)


def test_possible_game():
    g = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", RGB(12, 13, 14))
    assert g.possible


def test_impossible_game():
    g = Game(
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        RGB(12, 13, 14),
    )
    assert not g.possible


def test_example_games_results():
    games = parse_games_from_file("../inputs/day_2_example.txt", RGB(12, 13, 14))
    results = [g.possible for g in games]
    assert results == [True, True, False, False, True]


def test_sum_of_possible_example_game_ids():
    games = parse_games_from_file("../inputs/day_2_example.txt", RGB(12, 13, 14))
    ids = [g.game_id for g in games if g.possible]
    assert sum(ids) == 8


def test_example_games_cubes_required():
    games = parse_games_from_file("../inputs/day_2_example.txt", RGB(12, 13, 14))
    required = [g.cubes_required for g in games]
    expected = [
        RGB(4, 2, 6),
        RGB(1, 3, 4),
        RGB(20, 13, 6),
        RGB(14, 3, 15),
        RGB(6, 3, 2),
    ]
    assert required == expected


def test_example_games_pow():
    games = parse_games_from_file("../inputs/day_2_example.txt", RGB(12, 13, 14))
    powers = [g.cubes_required.pow() for g in games]
    assert sum(powers) == 2286
