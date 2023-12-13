import day_13 as d

TEST_INPUT = [
    """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
""",
    """
#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""",
]


def test_transpose():
    expected = """
#.##..#
..##...
##..###
#....#.
.#..#.#
.#..#.#
#....#.
##..###
..##...
""".strip()
    assert d.transpose(TEST_INPUT[0]) == expected


def test_vertical_reflection():
    assert d.vertical_reflection(TEST_INPUT[0]) == 5


def test_horizontal_reflection():
    assert d.horizontal_reflection(TEST_INPUT[1]) == 4


def test_solve_1():
    assert d.solve_1("../inputs/day_13_example.txt") == 405
