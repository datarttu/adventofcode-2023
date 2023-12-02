from day_1 import *


def test_calculate_sum_from_file():
    total = calculate_sum_from_file(Path("../inputs/day1_example.txt"))
    assert total == 142


def test_replace_spelled_digits():
    orig = "eightwothree"
    res = get_all_digits(orig)
    assert res == "823"


def test_get_int_lines():
    texts = read_file_as_list(Path("../inputs/day1_example2.txt"))
    texts = digitize_texts(texts)
    ints = get_int_lines(texts)
    assert ints == [29, 83, 13, 24, 42, 14, 76]


def test_calculate_sum_from_spelled_file():
    total = calculate_sum_from_spelled_file(Path("../inputs/day1_example2.txt"))
    assert total == 281
