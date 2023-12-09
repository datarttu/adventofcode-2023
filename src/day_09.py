from collections import deque
from itertools import pairwise
from utils import read_file_as_list


def read_input(filepath) -> list[list[int]]:
    return [[int(x) for x in l.split(" ")] for l in read_file_as_list(filepath)]


def extrapolate(numbers: list[int]) -> int:
    diffs = deque([numbers])

    while not all(d == 0 for d in diffs[-1]):
        diffs.append([j - i for i, j in pairwise(diffs[-1])])

    while len(diffs) > 1:
        last = diffs.pop()
        diffs[-1].append(diffs[-1][-1] + last[-1])

    return diffs[-1][-1]


def main() -> None:
    results = [extrapolate(nl) for nl in read_input("../inputs/day_09.txt")]
    print(sum(results))


if __name__ == "__main__":
    main()
