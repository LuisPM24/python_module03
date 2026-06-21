import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    items_dict: dict[str, int] = {}
    for arg in sys.argv[1:]:
        if ':' not in arg:
            print(f"Error - invalid parameter: '{arg}'")
            continue
        args = arg.split(':')
        if args[0] in items_dict.keys():
            print(f"Redundant item '{args[0]}' - discarding")
            continue
        try:
            items_dict[args[0]] = int(args[1])
        except ValueError as e:
            print(f"Quantity error for '{args[0]}': {e}")
    values_list = list(items_dict.values())
    print(f"Got inventory: {items_dict}")
    print(f"Item list: {list(items_dict.keys())}")
    print(f"Total quantity of the {len(items_dict)} items: {sum(values_list)}")
    value_most = 0
    value_least = 0
    for item, val in items_dict.items():
        print(f"Item {item} represents {round(val/sum(values_list)*100, 1)}%")
        if (item == list(items_dict.keys())[0] or val > value_most):
            value_most = val
            item_most = item
        if (item == list(items_dict.keys())[0] or val < value_least):
            value_least = val
            item_least = item
    print(f"Item most abundant: {item_most} with quantity {value_most}")
    print(f"Item least abundant: {item_least} with quantity {value_least}")
    items_dict.update([('An amazing book', 1)])
    print(f"Updated inventory: {items_dict}")


if __name__ == "__main__":
    main()
