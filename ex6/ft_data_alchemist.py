import random


def main() -> None:
    capi = []
    capitalized_only = []
    normal_dict: dict[str, int] = {}
    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam"
    ]
    capi = {name.capitalize() for name in players}
    capitalized_only = {name for name in players if name == name.capitalize()}
    normal_dict = {name: random.randint(0, 1000) for name in capi}
    aver = round(sum(normal_dict.values())/len(normal_dict.keys()), 2)
    higher_dict = {name: random.randint(round(aver, 0), 1000) for name in capi}
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capi}")
    print(f"New list with capitalized names only: {capitalized_only}")
    print(f"Score dict: {normal_dict}")
    print(f"Score aver: {aver}")
    print(f"High scores: {higher_dict}")


if __name__ == "__main__":
    main()
