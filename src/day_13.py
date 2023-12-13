from utils import read_newline_delimited_blocks


def transpose(pattern: str) -> str:
    pattern = pattern.strip()
    l_of_l = [list(s) for s in pattern.split("\n")]
    transposed = list(map(list, zip(*l_of_l)))
    return "\n".join("".join(l) for l in transposed)


def horizontal_reflection(pattern: str) -> int:
    pattern = pattern.strip()
    rows = pattern.split("\n")
    nrows = len(rows)
    for i in range(1, nrows):
        left = rows[:i]
        right = rows[i:]
        compare_len = min(len(left), len(right))
        mirror = list(reversed(left[-compare_len:])) == right[:compare_len]
        if mirror:
            return i
    else:
        return 0


def vertical_reflection(pattern: str) -> int:
    pattern = pattern.strip()
    pattern = transpose(pattern)
    return horizontal_reflection(pattern)


def reflections(patterns: list[str]) -> int:
    h = sum(100 * horizontal_reflection(p) for p in patterns)
    v = sum(vertical_reflection(p) for p in patterns)
    return h + v


def solve_1(filepath: str) -> int:
    patterns = read_newline_delimited_blocks(filepath)
    h = [horizontal_reflection(p) for p in patterns]
    v = [vertical_reflection(p) for p in patterns]
    return sum(h) * 100 + sum(v)


def main() -> None:
    result = solve_1("../inputs/day_13.txt")
    print(result)


if __name__ == "__main__":
    main()
