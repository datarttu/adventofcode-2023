import regex as re
from pathlib import Path
from utils import read_file_as_list


def extract_digits(from_text: str) -> int:
    """Get the first and last digits from a string,
    and make into an integer.
    Return 0 if no digits found."""
    matches = re.findall(r"\d", from_text)
    if not matches:
        return 0
    return int(matches[0] + matches[-1])


def get_int_lines(text_lines: list[str]) -> list[int]:
    return [extract_digits(l) for l in text_lines]


def calculate_sum_from_file(path: Path) -> int:
    texts = read_file_as_list(path)
    ints = get_int_lines(texts)
    return sum(ints)


# PART 2


def digit_map() -> dict[str, str]:
    spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return {el: str(i + 1) for i, el in enumerate(spelled)}


DIGITS = digit_map()


def get_all_digits(text: str) -> str:
    """Match digits only, whether they be spelled or numeric."""
    pattern = "|".join(DIGITS.keys()) + r"|\d"
    matches = re.findall(pattern, text, overlapped=True)
    str_matches = [str(m) for m in matches]
    digits = []
    for m in str_matches:
        if m in DIGITS.keys():
            digits.append(DIGITS[m])
        else:
            digits.append(m)
    return "".join(digits)


def digitize_texts(text_lines: list[str]) -> list[str]:
    return [get_all_digits(t) for t in text_lines]


def calculate_sum_from_spelled_file(path: Path) -> int:
    texts = read_file_as_list(path)
    texts = digitize_texts(texts)
    ints = get_int_lines(texts)
    return sum(ints)


def main():
    print("PART 1")
    path = Path("../inputs/day1.txt")
    res = calculate_sum_from_file(path)
    print(res)

    print("PART 2")
    new_res = calculate_sum_from_spelled_file(path)
    print(new_res)


if __name__ == "__main__":
    main()
