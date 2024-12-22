from typing import Any

current_day = "day19"


def print_grid(grid: list[Any]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write(line + "\n")


def valid_towel(current_index: int, target_pattern: str, pattern: str) -> bool:
    for i, val in enumerate(pattern):
        check_pos = current_index + i
        if check_pos >= len(target_pattern):
            return False

        check_val = target_pattern[check_pos]
        if check_val != val:
            return False
    return True


def search_tree(
    target_pattern: str,
    possible_towels: list[str],
    current_index: int,
    valid_count: int,
) -> tuple[int, bool, int]:
    # print(f"{current_index = } {len(target_pattern) = }")
    if current_index >= len(target_pattern):
        valid_count += 1

    for pattern in possible_towels:
        # print(f"{pattern = } {current_index = } {target_pattern = }")
        if valid_towel(current_index, target_pattern, pattern):
            # print(f"Found valid {pattern = }")
            _, valid, valid_count = search_tree(
                target_pattern,
                possible_towels,
                current_index + len(pattern),
                valid_count,
            )

            if valid:
                return current_index, True, valid_count

    return current_index, False, valid_count


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    possible_towels = data[0].split(", ")

    patterns = data[1:]

    possible_count = 0

    for pattern in patterns:
        print(f"Starting {pattern= }")
        valid_count = 0
        _, valid, valid_count = search_tree(pattern, possible_towels, 0, valid_count)
        if valid:
            possible_count += 1
    return possible_count


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    possible_towels = data[0].split(", ")

    patterns = data[1:]

    total_valid = 0

    for pattern in patterns:
        print(f"Starting {pattern = }")
        _, _, valid_count = search_tree(pattern, possible_towels, 0, 0)
        total_valid += valid_count
    return total_valid


if __name__ == "__main__":
    # print(part1(f"{current_day}/example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/example_data.txt"))
    print(part2(f"{current_day}/data.txt"))
