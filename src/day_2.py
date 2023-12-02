import regex as re
from utils import read_file_as_list
from dataclasses import dataclass, fields

from pprint import pprint


@dataclass()
class RGB:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __gt__(self, other):
        """
        RGB(1, 20, 3) > RGB(19, 19, 19) because 20 > 19
        """
        return any(
            getattr(self, color.name) > getattr(other, color.name)
            for color in fields(self)
        )

    def __add__(self, other):
        """
        RGB(1, 2, 3) + RGB(1, 2, 3) == RGB(2, 4, 6)
        """
        return RGB(
            *(
                getattr(self, color.name) + getattr(other, color.name)
                for color in fields(self)
            )
        )

    @classmethod
    def from_string(cls, string: str):
        """
        '8 green, 6 blue, 20 red'
        -> RGB(20, 8, 6)
        """
        totals = []
        for color in fields(cls):
            pattern = r"(\d+) " + color.name
            matches = re.findall(pattern, string)
            if not matches:
                totals.append(0)
            else:
                totals.append(sum([int(val) for val in matches]))
        return cls(*totals)


class Game:
    game_id: int
    possible: bool = True

    def __init__(self, string: str, max_cubes: RGB):
        """Parse a Game from string."""
        parts = string.split(":")
        self.game_id = int(re.findall(r"\d+", parts[0])[0])
        cubesets = parts[1].split(";")
        for cs in cubesets:
            cubes = RGB.from_string(cs)
            if cubes > max_cubes:
                self.possible = False

    def __repr__(self):
        return f"Game {self.game_id}: {self.possible}"


def parse_games_from_file(filepath: str, max_cubes: RGB) -> list[Game]:
    strings = read_file_as_list(filepath)
    return [Game(s, max_cubes) for s in strings]


def main():
    games = parse_games_from_file("../inputs/day_2.txt", RGB(12, 13, 14))
    pprint(games)
    ids = [g.game_id for g in games if g.possible]
    print(f"Sum of the ids of possible games is {sum(ids)}!")


if __name__ == "__main__":
    main()
