from pathlib import Path


def read_file_as_list(path: Path) -> list[str]:
    with open(path, "r") as fobj:
        lines = fobj.readlines()
    lines = [l.strip() for l in lines]
    return lines

def read_newline_delimited_blocks(path: Path) -> list[str]:
    with open(path, "r") as fobj:
        contents = fobj.read().strip()
    blocks = [b.strip() for b in contents.split("\n\n")]
    return blocks