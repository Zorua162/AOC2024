from __future__ import annotations

from typing import Any
from typing import Optional
import re

from collections import defaultdict


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


def check_valid(
    target_pattern: str, current_index: int, current_valid: re.Match[str]
) -> bool:
    current_group = current_valid.group()
    for i in range(0, len(current_group)):
        if target_pattern[current_index + i] != current_group[i]:
            return False
    return True


def search_valid_fills(
    start_location_dict: dict[int, list],
    target_pattern: str,
    current_index: int,
) -> int:
    current_valid_locs = start_location_dict[current_index]

    # print(f"{current_valid_locs = } {current_index = } {len(target_pattern) = }")

    if current_index == len(target_pattern):
        return 1

    valid_patterns = 0

    for current_valid in current_valid_locs:
        # if current valid doesn't match with pattern then return valid patterns
        if not check_valid(target_pattern, current_index, current_valid):
            return valid_patterns

        # otherwise start searching next with moved index to new location based on
        # currently valid towel pattern

        valid_patterns += search_valid_fills(
            start_location_dict,
            target_pattern,
            current_index + len(current_valid.group()),
        )

    # Return only valid found
    return valid_patterns


def find_count(target_pattern: str, possible_towels: list[str]) -> int:
    start_location_dict: dict[int, list] = defaultdict(lambda: [])

    # Get all the patterns and their locations in the target pattern
    for towel in possible_towels:
        matches = list(re.finditer(towel, target_pattern, re.MULTILINE))

        for match in matches:
            start_location_dict[match.span()[0]].append(match)

    valid_patterns = search_valid_fills(start_location_dict, target_pattern, 0)

    return valid_patterns


def stack_towels(possible_towels: list[str]):
    for towel in possible_towels:
        print(towel)


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    possible_towels = data[0].split(", ")

    patterns = data[1:]

    possible_count = 0

    stack_towels(possible_towels)

    for pattern in patterns:
        print(f"Starting pattern {pattern}")
        possible_count += find_count(pattern, possible_towels)

    return possible_count


if __name__ == "__main__":
    # print(part1(f"{current_day}/example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/example_data.txt"))
    print(part2(f"{current_day}/data.txt"))
