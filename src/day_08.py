import regex as re
from itertools import cycle
from utils import read_file_as_list


def read_input(filepath: str) -> tuple[str, dict]:
    lines = read_file_as_list(filepath)
    directions = lines[0]
    line_items = [re.findall("[A-Z]{3}", l) for l in lines[2:]]
    nodes = {li[0]: tuple(li[1:]) for li in line_items}
    return directions, nodes


def walk_to_destination(directions: str, nodes: dict) -> int:
    current_node = "AAA"
    for i, d in enumerate(cycle(directions)):
        next_node = nodes[current_node][int(d == "R")]
        if next_node == "ZZZ":
            return i + 1
        current_node = next_node


def main() -> None:
    directions, nodes = read_input("../inputs/day_08.txt")
    steps = walk_to_destination(directions, nodes)
    print(steps)


if __name__ == "__main__":
    main()
