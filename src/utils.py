from pathlib import Path


def read_file_as_list(path: Path) -> list[str]:
    with open(path, "r") as fobj:
        lines = fobj.readlines()
    lines = [l.strip() for l in lines]
    return lines
