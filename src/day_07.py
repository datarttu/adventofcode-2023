from dataclasses import dataclass, field
from utils import read_file_as_list

from pprint import pprint


def card_value_mapping() -> dict[str, int]:
    cards = "AKQJT98765432"[::-1]
    values = [i + 2 for i in range(len(cards))]
    return {k: v for k, v in zip(cards, values)}


@dataclass
class Hand:
    cards: str
    type_score: int = field(init=False)
    card_score: int = field(init=False)
    total_score: int = field(init=False)

    def __post_init__(self):
        type_scores = {
            k: i * (10**10)
            for i, k in enumerate(["11111", "1112", "122", "113", "23", "14", "5"])
        }
        unique_values = set(self.cards)
        value_counts = {v: self.cards.count(v) for v in unique_values}
        card_type = "".join(sorted([str(v) for v in value_counts.values()]))
        self.type_score = type_scores[card_type]

        card_score_values = card_value_mapping()
        self.card_score = 0
        for i, c in enumerate(reversed(self.cards)):
            card_value = card_score_values[c]
            self.card_score += card_value * (10 ** (i * 2))

        self.total_score = self.type_score + self.card_score

    def __lt__(self, other):
        return self.total_score < other.total_score


def play(filepath: str) -> int:
    lines = read_file_as_list(filepath)
    hands, bids = [], []
    for l in lines:
        h, b = l.split(" ")
        hands.append(Hand(h))
        bids.append(int(b.strip()))
    ranks = [sorted(hands).index(h) + 1 for h in hands]
    return sum(r * b for r, b in zip(ranks, bids))


def main() -> None:
    print(play("../inputs/day_07.txt"))


if __name__ == "__main__":
    main()
