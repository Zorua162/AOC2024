from collections import defaultdict

current_day = "day11"


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write(line + "\n")


def do_rules(stone_groups: dict[int, int]) -> dict[int, int]:
    updated_stone_groups: dict[int, int] = defaultdict(lambda: 0)

    for val, count in stone_groups.items():
        if val == 0:
            updated_stone_groups[1] += count
            continue
        str_val = str(val)
        len_str_val = len(str_val)
        if len_str_val % 2 == 0:
            first_half = str_val[: round(len_str_val / 2)]
            second_half = str_val[round(len_str_val / 2) :]
            print(f"{first_half = } {second_half = }")
            updated_stone_groups[int(first_half)] += count
            updated_stone_groups[int(second_half)] += count
            continue

        # None of the other rules apply so multiple by 2024
        new_value = val * 2024
        updated_stone_groups[new_value] += count

    return updated_stone_groups


def do_iterations(data_path: str, iterations: int) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    stone_groups: dict[int, int] = defaultdict(lambda: 0)

    line = data[0]

    initial_arrangement = [int(group) for group in line.split(" ")]

    for group in initial_arrangement:
        stone_groups[group] += 1

    for i in range(iterations):
        stone_groups = do_rules(stone_groups)
        print(stone_groups)
    print(stone_groups)
    return sum(stone_groups.values())


def part1(data_path: str) -> int:
    return do_iterations(data_path, 25)


def part2(data_path: str) -> int:
    return do_iterations(data_path, 75)


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))
