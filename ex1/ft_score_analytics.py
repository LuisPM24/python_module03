import sys


def print_scores(score_list: list[int]) -> None:
    print(f"Scores processed: {score_list}")
    print(f"Total players: {len(score_list)}")
    print(f"Total score: {sum(score_list)}")
    print(f"Average score: {sum(score_list)/len(score_list)}")
    print(f"High score: {max(score_list)}")
    print(f"Low score: {min(score_list)}")
    print(f"Score range: {max(score_list) - min(score_list)}")


def main() -> None:
    score_list: list[int]

    score_list = []
    print("=== Player Score Analytics ===")
    if (len(sys.argv) != 1):
        for (argv) in (sys.argv[1:]):
            try:
                score_list += [int(argv)]
            except ValueError:
                print(f"Invalid parameter: '{argv}'")
    if (len(score_list)) == 0:
        print("No scores provided. Usage: python3 ", end="")
        print("ft_score_analytics.py <score1> <score2> ...")
    else:
        print_scores(score_list)


if __name__ == "__main__":
    main()
