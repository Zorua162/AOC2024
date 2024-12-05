from collections import defaultdict
from math import floor

current_day = "day5"


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write(line)


def check_rest_of_group_in_valid(valid: list[int], rest_of_group: list[int]) -> bool:
    for i in rest_of_group:
        if i not in valid:
            return False
    return True


def find_mid(group: list[int]) -> int:
    index = floor(len(group) / 2)
    print(f"{index = }")
    return group[index]


def check_valid(rules: dict[int, list[int]], group: list[int]) -> bool:
    valid_rule = True
    for i, val in enumerate(group):
        valid_after = rules[val]
        print(f"{val = } {valid_after = } {group[i+1:] = }")

        if not check_rest_of_group_in_valid(valid_after, group[i + 1 :]):
            valid_rule = False

    return valid_rule


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        # data = [line for line in f_obj.read().split("\n") if line != ""]
        data = f_obj.read()

    split_data = data.split("\n\n")

    rules_list = [i.split("|") for i in split_data[0].split("\n")]

    rules: dict[int, list[int]] = defaultdict(lambda: [])

    for rule in rules_list:
        rules[int(rule[0])].append(int(rule[1]))

    groups = [
        [int(i) for i in nums.split(",")]
        for nums in split_data[1].split("\n")
        if nums != ""
    ]

    print(f"{rules = }, {groups = }")

    count = 0

    # groups = [groups[0]]

    for group in groups:
        valid = check_valid(rules, group)
        print(f"{group = } {valid = }")
        if valid:
            mid = find_mid(group)
            count += mid

    return count


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)
    return 0


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    print(part2(f"{current_day}/part1_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
