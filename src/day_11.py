import numpy as np
from scipy.sparse import coo_array
from scipy.spatial.distance import pdist


def read_expand(filepath: str) -> np.array:
    with open(filepath, "r") as f:
        s = f.readlines()
        s = [
            x.replace(".", "0,").replace("#", "1,").strip().removesuffix(",") for x in s
        ]
    m = np.loadtxt(fname=s, dtype=int, delimiter=",")
    m = np.insert(m, np.where(m.sum(axis=1) == 0)[0], 0, axis=0)
    m = np.insert(m, np.where(m.sum(axis=0) == 0)[0], 0, axis=1)
    return m


def distances(m: np.array):
    coordinates = coo_array(m)
    cm = np.transpose(np.array([coordinates.col, coordinates.row]))
    return pdist(cm, metric="cityblock")


def main() -> None:
    m = read_expand("../inputs/day_11.txt")
    ds = distances(m)
    print(sum(ds))


if __name__ == "__main__":
    main()
