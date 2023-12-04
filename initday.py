#!/usr/bin/python

import httpx
import sys
from pathlib import Path


def main():
    try:
        day_number = sys.argv[1]
    except IndexError as e:
        print("Provide day number as argument.")
        raise e

    with open(".token", "r") as f:
        token = f.readline().strip()
    headers = {"Cookie": f"session={token}"}

    r = httpx.get(
        f"https://adventofcode.com/2023/day/{day_number}/input", headers=headers
    )
    r.raise_for_status()

    filepath = f"inputs/day_{day_number}.txt"

    with open(filepath, "w") as f:
        f.write(r.text)

    print(f"Input saved to {filepath} ✅")

    Path(f"src/day_{day_number:02}.py").touch()
    Path(f"src/test_day_{day_number:02}.py").touch()

    print("Python files created ✅")


if __name__ == "__main__":
    main()
