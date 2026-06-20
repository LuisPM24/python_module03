import random


def gen_player_achievements() -> set[str]:
    achievements = [
        "42 Hater",
        "Pls, take a shower",
        "Running in the 90's",
        "Another One Bites the Dust",
        "Example of achievements",
        "Hello, I'm under the water",
        "A fake achievement",
        "You actually touched grass!!!",
        "I want to cry",
        "The ring of Sauron",
        "Bro is reading the achievements",
        "It's called 'football', not 'soccer'",
        "Yooo Mr. White",
        "You got an achievement!",
        "Galaxy Brain",
        "Oi Hughie..."
    ]
    amount_achv = random.randint(2, 6)
    return (set(random.sample(achievements, amount_achv)))


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    players = ["Alice", "Bob", "Charlie", "Dylan"]
    sets = {name: gen_player_achievements() for name in players}
    for name, achv in sets.items():
        print(f"Player {name}: {achv}")
    for name in players[1:]:
        dist_achv = sets[players[0]].union(sets[name])
    print(f"\nAll distinct achievements: {dist_achv}\n")
    for name in players[1:]:
        inter_achv = sets[players[0]].intersection(sets[name])
    print(f"Common achievements: {inter_achv}\n")
    for name, achv in sets.items():
        for aux_name, aux_achv in sets.items():
            if aux_name != name:
                res = sets[name].difference(aux_achv)
        print(f"Only {name} has: {res}")
    print()
    for name, achv in sets.items():
        print(f"{name} is missing: {dist_achv.difference(sets[name])}")


if __name__ == "__main__":
    main()
