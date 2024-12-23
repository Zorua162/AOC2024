from typing import Any
from typing import Optional
import re

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


def find_valid_towel(
    current_index: int, target_pattern: str, possible_towels: list[str]
) -> Optional[str]:
    for pattern in possible_towels:
        if valid_towel(current_index, target_pattern, pattern):
            return pattern
    return None


def pattern_possible(pattern: str, possible_towels: list[str]) -> bool:
    current_index = 0
    while current_index < len(pattern):
        valid_pattern = find_valid_towel(current_index, pattern, possible_towels)
        if valid_pattern is None:
            return False
        current_index += len(valid_pattern)

    return True


def search_tree(
    target_pattern: str, possible_towels: list[str], current_index: int
) -> tuple[int, bool]:
    # print(f"{current_index = } {len(target_pattern) = }")
    if current_index >= len(target_pattern):
        return current_index, True

    for pattern in possible_towels:
        # print(f"{pattern = } {current_index = } {target_pattern = }")
        if valid_towel(current_index, target_pattern, pattern):
            # print(f"Found valid {pattern = }")
            _, valid = search_tree(
                target_pattern, possible_towels, current_index + len(pattern)
            )

            if valid:
                return current_index, True

    return current_index, False


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    possible_towels = data[0].split(", ")

    patterns = data[1:]

    possible_count = 0

    for pattern in patterns:
        # if pattern_possible(pattern, possible_towels):
        #     possible_count += 1
        # else:
        #     print(f"{pattern = } was invalid")

        _, valid = search_tree(pattern, possible_towels, 0)
        if valid:
            possible_count += 1
    return possible_count


def check_not_filled(filled: list[int], span: tuple[int, int]) -> bool:
    for i in range(span[0], span[1]):
        if filled[i] != 0:
            return False
    return True


def fill(filled: list[int], span: tuple[int, int]) -> list[int]:
    for i in range(span[0], span[1]):
        filled[i] = 1
    return filled


def check_fills(
    target_pattern: str, locations: dict[int, list], check_order: list[str]
) -> bool:
    filled = [0 for _ in target_pattern]
    for pattern in check_order:
        for span in locations[pattern]:
            if check_not_filled(filled, span.span()):
                filled = fill(filled, span.span())
            print(span, span.span(), filled)
            if all([i == 1 for i in filled]):
                return True
    return False


def find_count(target_pattern: str, possible_towels: list[str]) -> int:
    locations = {}
    spans: list[re.Match] = []
    for towel in possible_towels:
        matches = list(re.finditer(towel, target_pattern, re.MULTILINE))
        if len(matches) > 0:
            locations[towel] = list(matches)
        spans.extend(matches)

    check_order = sorted(locations.keys(), key=len, reverse=True)
    fills = set()
    for _ in range(len(locations.keys())):
        fills.add(get_fill(target_pattern, locations, check_order))

    return len(fills)


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    possible_towels = data[0].split(", ")

    patterns = data[1:]

    possible_count = 0

    for pattern in [patterns[0]]:
        possible_count += find_count(pattern, possible_towels)
    return possible_count


if __name__ == "__main__":
    # print(part1(f"{current_day}/example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    print(part2(f"{current_day}/example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
