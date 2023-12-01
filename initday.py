#!/usr/bin/python

import httpx
import sys


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

    filepath = f"inputs/day{day_number}.txt"

    with open(filepath, "w") as f:
        f.write(r.text)

    print(f"Input saved to {filepath} ✅")


if __name__ == "__main__":
    main()
