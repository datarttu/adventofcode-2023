import regex as re
from itertools import cycle
from math import lcm
from utils import read_file_as_list


def read_input(filepath: str) -> tuple[str, dict]:
    lines = read_file_as_list(filepath)
    directions = lines[0]
    line_items = [re.findall("(?:[A-Z|1-9]){3}", l) for l in lines[2:]]
    nodes = {li[0]: tuple(li[1:]) for li in line_items}
    return directions, nodes


def walk_to_destination(
    directions: str, nodes: dict, start_key: str, endswith: str
) -> int:
    current_node = start_key
    for i, d in enumerate(cycle(directions)):
        next_node = nodes[current_node][int(d == "R")]
        if next_node.endswith(endswith):
            return i + 1
        current_node = next_node


def multiwalk_to_destination(directions: str, nodes: dict) -> int:
    start_keys = [x for x in nodes.keys() if x.endswith("A")]
    single_walks = [
        walk_to_destination(directions, nodes, sk, "Z") for sk in start_keys
    ]
    return lcm(*single_walks)


def main() -> None:
    directions, nodes = read_input("../inputs/day_08.txt")
    steps = walk_to_destination(directions, nodes, "AAA", "ZZZ")
    print(steps)
    multisteps = multiwalk_to_destination(directions, nodes)
    print(multisteps)


if __name__ == "__main__":
    main()
