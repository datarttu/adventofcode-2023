from typing import Callable


def make_converter(range_lines: list[list[int]]) -> Callable:
    source_starts = [rl[1] for rl in range_lines]
    source_ends = [rl[1] + rl[2] - 1 for rl in range_lines]
    destination_deltas = [rl[0] - rl[1] for rl in range_lines]

    def converter(x: int):
        for ss, se, dd in zip(source_starts, source_ends, destination_deltas):
            if ss <= x <= se:
                return x + dd
        return x

    return converter


def parse_mapper(str_map: str) -> tuple[str, list]:
    k, v = str_map.strip().split(":\n")
    k = k.replace("-to-", "-").replace(" map", "")
    v = [[int(nr) for nr in sublist.split(" ")] for sublist in v.split("\n")]
    return k, make_converter(v)


def read_input(filepath: str) -> tuple[list[int], dict]:
    with open(filepath, "r") as fobj:
        contents = fobj.read()
    blocks = contents.split("\n\n")
    seeds = [int(s) for s in blocks[0].split(": ")[1].split(" ")]
    mappers = {k: v for k, v in [parse_mapper(m) for m in blocks[1:]]}
    return seeds, mappers


def solve(seeds: list[int], mappers: dict[str, Callable]) -> int:
    results = seeds
    from_type = "seed"
    while True:
        key = next(x for x in mappers.keys() if x.startswith(from_type))
        results = [mappers[key](r) for r in results]
        _, from_type = key.split("-")
        if from_type == "location":
            return min(results)


def main():
    seeds, mappers = read_input("../inputs/day_05.txt")
    print(solve(seeds, mappers))


if __name__ == "__main__":
    main()
