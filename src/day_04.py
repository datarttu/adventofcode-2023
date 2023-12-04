import regex as re
from utils import read_file_as_list
from pprint import pprint


def read_cards(filepath: str) -> list[dict]:
    lines = read_file_as_list(filepath)
    cards = []
    for l in lines:
        card_id, contents = l.split(":")
        winning, appearing = contents.split("|")
        common = set(re.findall(r"\d+", winning)) & set(re.findall(r"\d+", appearing))
        cards.append({"card_id": card_id, "wins": len(common), "total_cards": 1})
    return cards


def card_result(card: dict) -> int:
    if card["wins"] == 0:
        return 0
    return pow(2, card["wins"] - 1)


def game(filepath: str) -> int:
    cards = read_cards(filepath)
    results = [card_result(c) for c in cards]
    return sum(results)


# PART 2
def copying_game(filepath: str) -> int:
    cards = read_cards(filepath)
    max_i = len(cards)

    for i, _ in reversed(list(enumerate(cards))):
        wins = cards[i]["wins"]
        if not wins:
            continue
        j1 = min(i + 1, max_i - 1)  # Ref to the first of the next cards
        j2 = min(i + 1 + wins, max_i)  # Ref to the last of the next cards
        cards[i]["total_cards"] += sum(c["total_cards"] for c in cards[j1:j2])

    return sum(c["total_cards"] for c in cards)


def main():
    total = game("../inputs/day_4.txt")
    print(total)
    total_2 = copying_game("../inputs/day_4.txt")
    print(total_2)


if __name__ == "__main__":
    main()
