from utils import read_newline_delimited_blocks


def transpose(pattern: str) -> str:
    pattern = pattern.strip()
    l_of_l = [list(s) for s in pattern.split("\n")]
    transposed = list(map(list, zip(*l_of_l)))
    return "\n".join("".join(x) for x in transposed)


def mirror_badness(left_side: list[str], right_side: list[str]) -> int:
    left_side = "".join(list(reversed(left_side)))
    right_side = "".join(right_side)
    badness = sum(int(l_el != r_el) for l_el, r_el in zip(left_side, right_side))
    return badness


def horizontal_reflection(pattern: str, qualify_badness: int = 0) -> int:
    pattern = pattern.strip()
    rows = pattern.split("\n")
    nrows = len(rows)
    for i in range(1, nrows):
        left = rows[:i]
        right = rows[i:]
        compare_len = min(len(left), len(right))
        badness = mirror_badness(left[-compare_len:], right[:compare_len])
        if badness == qualify_badness:
            return i
    else:
        return 0


def vertical_reflection(pattern: str, qualify_badness: int = 0) -> int:
    pattern = pattern.strip()
    pattern = transpose(pattern)
    return horizontal_reflection(pattern, qualify_badness)


def reflections(patterns: list[str]) -> int:
    h = sum(100 * horizontal_reflection(p) for p in patterns)
    v = sum(vertical_reflection(p) for p in patterns)
    return h + v


def solve_1(filepath: str) -> int:
    patterns = read_newline_delimited_blocks(filepath)
    h = [horizontal_reflection(p) for p in patterns]
    v = [vertical_reflection(p) for p in patterns]
    return sum(h) * 100 + sum(v)


def solve_2(filepath: str) -> int:
    patterns = read_newline_delimited_blocks(filepath)
    h = [horizontal_reflection(p, 1) for p in patterns]
    v = [vertical_reflection(p, 1) for p in patterns]
    return sum(h) * 100 + sum(v)


def main() -> None:
    result = solve_1("../inputs/day_13.txt")
    print(result)

    result = solve_2("../inputs/day_13.txt")
    print(result)


if __name__ == "__main__":
    main()
