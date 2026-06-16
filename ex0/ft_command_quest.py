import sys


def main() -> None:
    argc: int
    count: int

    argc = len(sys.argv)
    count = 1
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0][-19:]}")
    if (argc != 1):
        print(f"Arguments received: {argc - 1}")
        while (count < argc):
            print(f"Argument {count}: {sys.argv[count]}")
            count += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
