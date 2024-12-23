from __future__ import annotations

from typing import Any
from typing import Optional
import re

from itertools import groupby


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


def fill(
    target_pattern: str, filled: list[int], match: re.Match[str]
) -> tuple[list[int], bool]:
    pre_filled = filled.copy()
    span = match.span()
    match_val = match.group()
    for i, val in enumerate(match_val):
        loc = span[0] + i
        # print(f"{target_pattern = } {match_val = } {loc = } {filled = } ")
        if filled[loc] == 1 or target_pattern[loc] != val:
            return pre_filled, False
        filled[loc] = 1
    # print(f"Valid fill {filled}")
    return filled, True


class FillContent:
    spans: list[re.Match[str]]

    def __init__(self):
        self.spans = []

    def append(self, span: re.Match[str]):
        self.spans.append(span)

    def __eq__(self, comp: object) -> bool:
        if not isinstance(comp, FillContent):
            return False
        self_str = self.full_str()
        comp_str = comp.full_str()
        # print(f"{self_str = }\n{comp_str = }")
        return self_str == comp_str

    def full_str(self):
        return "".join(sorted([f"{span.span()}{span.group()}" for span in self.spans]))

    def short_str(self):
        return re.sub(r"\(\d, \d\)", "", self.full_str(), 0)

    def __repr__(self):
        return f"({self.full_str()})"

    # def __lt__(self, comp) -> bool:


def get_fill(
    target_pattern: str,
    locations: dict[str, list[re.Match[str]]],
    check_order: list[str],
) -> Optional[FillContent]:
    filled = [0 for _ in target_pattern]
    fill_content = FillContent()
    for pattern in check_order:
        for span in locations[pattern]:
            if check_not_filled(filled, span.span()):
                filled, include = fill(target_pattern, filled, span)
                if include:
                    # print(f"Including {span}")
                    fill_content.append(span)
            # print(f"{span = }, {span.span() = }, {filled = }")
            if all([i == 1 for i in filled]):
                # print(f"{fill_content = }")
                return fill_content
    return None


def remove_duplicates(fills: list[FillContent]) -> list[FillContent]:
    # fills = [sorted(fill) for fill in fills]

    # print(f"pre-duplicate removal {len(fills) = } {fills = }")

    fills = list(fills for fills, _ in groupby(fills))
    # print(f"post-duplicate removal {len(fills) = } {fills = }")

    return fills


def find_count(target_pattern: str, possible_towels: list[str]) -> int:
    locations: dict[str, list[re.Match[str]]] = {}
    spans: list[re.Match] = []

    # Get all the patterns and their locations in the target pattern
    for towel in possible_towels:
        matches = list(re.finditer(towel, target_pattern, re.MULTILINE))
        if len(matches) > 0:
            locations[towel] = list(matches)
        spans.extend(matches)

    # Try each order of these possible spans to figure out which are valid
    span_values: list[str] = [span.group() for span in spans]
    check_order = sorted(span_values, key=len, reverse=True)
    fills: list[FillContent] = []
    for _ in range(len(spans)):
        fill = get_fill(target_pattern, locations, check_order)
        if fill is not None:
            fills.append(fill)
            pass
        order_end = check_order.pop()
        check_order.insert(0, order_end)
        print(f"{check_order = }")

    fills = remove_duplicates(fills)
    for fill in fills:
        print(f"{fill.short_str()} {fill.full_str()}")

    return len(fills)


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    possible_towels = data[0].split(", ")

    patterns = data[1:]

    possible_count = 0

    for pattern in [patterns[3]]:
        possible_count += find_count(pattern, possible_towels)
    return possible_count


if __name__ == "__main__":
    # print(part1(f"{current_day}/example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    print(part2(f"{current_day}/example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
