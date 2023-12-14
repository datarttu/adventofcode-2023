import day_13 as d


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
    blocks = d.read_newline_delimited_blocks("../inputs/day_13_example.txt")
    assert d.transpose(blocks[0]) == expected


def test_vertical_reflection():
    blocks = d.read_newline_delimited_blocks("../inputs/day_13_example.txt")
    assert d.vertical_reflection(blocks[0]) == 5


def test_horizontal_reflection():
    blocks = d.read_newline_delimited_blocks("../inputs/day_13_example.txt")
    assert d.horizontal_reflection(blocks[1]) == 4


def test_solve_1():
    assert d.solve_1("../inputs/day_13_example.txt") == 405


def test_solve_2():
    assert d.solve_2("../inputs/day_13_example.txt") == 400
