from day_08 import *


def test_read_directions_and_nodes():
    directions, nodes = read_input("../inputs/day_08_example.txt")
    assert directions == "RL"
    assert len(nodes) == 7
    assert nodes["AAA"] == ("BBB", "CCC")
    assert list(nodes.keys())[0] == "AAA"


def test_walk_to_destination():
    directions, nodes = read_input("../inputs/day_08_example.txt")
    steps = walk_to_destination(directions, nodes, "AAA", "ZZZ")
    assert steps == 2


def test_walk_to_destination_2():
    directions, nodes = read_input("../inputs/day_08_example_2.txt")
    steps = walk_to_destination(directions, nodes, "AAA", "ZZZ")
    assert steps == 6


def test_multiwalk_to_destination():
    directions, nodes = read_input("../inputs/day_08_example_3.txt")
    steps = multiwalk_to_destination(directions, nodes)
    assert steps == 6
