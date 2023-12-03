import regex as re
from utils import read_file_as_list


def solve_1(filepath: str) -> int:
    schematic = read_file_as_list(filepath)
    rowlen = len(schematic[0])
    flat_schematic = "".join(schematic)
    totallen = len(flat_schematic)

    number_matches = [
        (int(m.group(0)), m.start(0), m.end(0) - 1)
        for m in re.finditer(r"\d+", flat_schematic)
    ]
    # (number, startpos, endpos)
    # Look behind: startpos-1 and range startpos-rowlen-1 to endpos-rowlen+1
    # Look ahead:  endpos+1   and range startpos+rowlen-1 to endpos+rowlen+1
    numbers_with_neighbors = []
    for nm in number_matches:
        indices = [nm[1] - 1]
        indices.extend(range(nm[1] - rowlen - 1, nm[2] - rowlen + 2))
        indices.append(nm[2] + 1)
        indices.extend(range(nm[1] + rowlen - 1, nm[2] + rowlen + 2))
        indices = [i for i in indices if totallen > i >= 0]

        chars = "".join(flat_schematic[i] for i in indices).replace(".", "")

        if chars:
            numbers_with_neighbors.append(nm[0])

    return sum(numbers_with_neighbors)


def solve_2(filepath: str) -> int:
    schematic = read_file_as_list(filepath)
    rowlen = len(schematic[0])
    flat_schematic = "".join(schematic)
    totallen = len(flat_schematic)

    number_matches = [
        (int(m.group(0)), m.start(0), m.end(0))
        for m in re.finditer(r"\d+", flat_schematic)
    ]
    number_positions = [(m[0], set((*range(m[1], m[2]),))) for m in number_matches]

    # For *, startpos == endpos
    star_positions = [m.start(0) for m in re.finditer(r"\*", flat_schematic)]
    star_boxes = []
    for p in star_positions:
        box = (
            *range(p - rowlen - 1, p - rowlen + 2),
            *range(p - 1, p + 2),
            *range(p + rowlen - 1, p + rowlen + 2),
        )
        box = set(el for el in box if totallen > el >= 0)
        star_boxes.append(box)

    gears = []
    for b in star_boxes:
        matching_numbers = []
        for n in number_positions:
            if b.intersection(n[1]):
                matching_numbers.append(n[0])
        gears.append(matching_numbers)
    gears = [g for g in gears if len(g) == 2]

    gear_ratios = [g[0] * g[1] for g in gears]

    return sum(gear_ratios)


def main():
    print(solve_1("../inputs/day_3.txt"))
    print(solve_2("../inputs/day_3.txt"))


if __name__ == "__main__":
    main()
