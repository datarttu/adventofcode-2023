from day_05 import *


def test_mapper():
    id, mapper = parse_mapper("seed-to-soil map:\n50 98 2\n52 50 48")
    assert id == "seed-soil"
    assert mapper(98) == 50
    assert mapper(99) == 51
    assert mapper(100) == 100
    assert mapper(50) == 52
    assert mapper(97) == 99
    assert mapper(1) == 1


def test_seed_to_soil_mapper():
    seeds, mappers = read_input("../inputs/day_05_example.txt")
    assert seeds == [79, 14, 55, 13]
    soils = [mappers["seed-soil"](s) for s in seeds]
    assert soils == [81, 14, 57, 13]


def test_solve():
    seeds, mappers = read_input("../inputs/day_05_example.txt")
    assert solve(seeds, mappers) == 35
