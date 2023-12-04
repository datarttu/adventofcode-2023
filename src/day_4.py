import regex as re
from utils import read_file_as_list


def read_cards(filepath: str) -> list[dict]:
    lines = read_file_as_list(filepath)
    cards = []
    for l in lines:
        card_id, contents = l.split(":")
        winning, appearing = contents.split("|")
        common = set(re.findall(r"\d+", winning)) & set(re.findall(r"\d+", appearing))
        cards.append({"card_id": card_id, "common": common})
    return cards


def card_result(card: dict) -> int:
    n_matches = len(card["common"])
    if n_matches == 0:
        return 0
    return pow(2, n_matches - 1)


def game(filepath: str) -> int:
    cards = read_cards(filepath)
    results = [card_result(c) for c in cards]
    return sum(results)


def main():
    total = game("../inputs/day_4.txt")
    print(total)


if __name__ == "__main__":
    main()
