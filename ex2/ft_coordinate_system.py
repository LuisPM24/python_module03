import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        inp = input("Enter new coordinates as floats in format 'x,y,z': ")
        cdns = inp.split(",")
        if (len(cdns) != 3):
            print("Invalid syntax")
            continue
        form_values = []
        isValid = True
        for cdn in cdns:
            try:
                form_values += [float(cdn.strip())]
            except ValueError as e:
                print(f"Error on parameter '{cdn.strip()}': {e}")
                isValid = False
                break
        if isValid:
            return (form_values[0], form_values[1], form_values[2])


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    tupp1 = get_player_pos()
    print(f"Got a first tuple: ({tupp1[0]}, {tupp1[1]}, {tupp1[2]})")
    print(f"It includes: X={tupp1[0]}, Y={tupp1[1]}, Z={tupp1[2]}")
    sol1 = math.sqrt((tupp1[0])**2 + (tupp1[1]**2 + tupp1[2]**2))
    print(f"Distance to center: {round(sol1, 4)}\n")
    print("Get a second set of coordinates")
    tupp2 = get_player_pos()
    sol = math.sqrt((tupp2[0] - tupp1[0])**2
                    + (tupp2[1] - tupp1[1])**2
                    + (tupp2[2] - tupp1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(sol, 4)}")


if __name__ == "__main__":
    main()
