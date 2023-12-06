from functools import reduce

# total_time == t_hold + t_travel <-> t_travel == total_time - t_hold
# speed == t_hold
# distance == speed * t_travel
#     == t_hold * (total_time - t_hold)
#     == t_hold*total_time - t_hold**2


def solve(times_allowed: list[int], distances_recorded: list[int]):
    wins_per_race = []

    for t, d in zip(times_allowed, distances_recorded):
        wins = 0
        for t_hold in range(t + 1):
            distance = t_hold * t - t_hold**2
            if distance > d:
                wins += 1
        wins_per_race.append(wins)

    return reduce(lambda x, y: x * y, wins_per_race)


def main():
    TIMES_ALLOWED = [49, 97, 94, 94]
    DISTANCES_RECORDED = [263, 1532, 1378, 1851]
    res1 = solve(TIMES_ALLOWED, DISTANCES_RECORDED)
    print(res1)

    TIMES_ALLOWED = [int("".join([str(el) for el in TIMES_ALLOWED]))]
    DISTANCES_RECORDED = [int("".join([str(el) for el in DISTANCES_RECORDED]))]
    res2 = solve(TIMES_ALLOWED, DISTANCES_RECORDED)
    print(res2)


if __name__ == "__main__":
    main()
