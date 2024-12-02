import operator
from collections.abc import Callable

current_day = "day2"


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write(line)


def check_decreasing_safe(numbers: list[int]) -> bool:
    """Check if all the numbers decrease"""
    # print("Checking decreasing")
    current_num = numbers[0]
    for next_number in numbers[1:]:
        # print(f"{next_number = } {current_num = }")
        if (
            next_number > current_num
            or abs(next_number - current_num) > 3
            or abs(next_number - current_num) < 1
        ):
            return False
        current_num = next_number
    print("Decreasing safe")
    return True


def check_increasing_safe(numbers: list[int]) -> bool:
    """Check if all the numbers increase"""
    # print("Checking increasing")
    current_num = numbers[0]
    for next_number in numbers[1:]:
        # print(f"{next_number = } {current_num = }")
        if (
            next_number < current_num
            or abs(next_number - current_num) > 3
            or abs(next_number - current_num) < 1
        ):
            return False
        current_num = next_number
    print("Increasing safe")
    return True


def check_line_safe(line: str) -> bool:
    numbers = [int(i) for i in line.split(" ")]

    return check_increasing_safe(numbers) or check_decreasing_safe(numbers)


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    # print_grid(data)
    safe_count = 0
    for line in data:
        if check_line_safe(line):
            print(f"Safe line {line}")
            safe_count += 1
        else:
            print(f"Unsafe line {line}")

    return safe_count


def check_safe(comp, numbers: list[int]) -> tuple[int, bool]:
    """Check if all the numbers increase"""
    # print("Checking increasing")
    current_num = numbers[0]
    for i, next_number in enumerate(numbers[1:]):
        # print(f"{next_number = } {current_num = }")
        if (
            comp(next_number, current_num)
            or abs(next_number - current_num) > 3
            or abs(next_number - current_num) < 1
        ):
            return i, False
        current_num = next_number
    print("Increasing safe")
    return None, True


def check_index_removed_safe(
    numbers: list[int], comp: Callable, index: int
) -> tuple[int, bool]:
    copied_numbers = numbers.copy()
    del copied_numbers[index]
    print(f"{numbers = } {copied_numbers = } {index = } {comp = }")
    return check_safe(comp, copied_numbers)


def check_line_safe_part2(line: str) -> bool:
    numbers = [int(i) for i in line.split(" ")]
    failed_at_increasing, increasing_safe = check_safe(operator.lt, numbers)

    failed_at_decreasing, decreasing_safe = check_safe(operator.gt, numbers)
    first_try_safe = increasing_safe or decreasing_safe
    if not first_try_safe:
        # remove failed at and one after failed at, or all four
        if failed_at_increasing + 1 < len(numbers):
            right_removed_safe_increasing = check_index_removed_safe(
                numbers, operator.lt, failed_at_increasing + 1
            )

        if failed_at_decreasing + 1 < len(numbers):
            right_removed_safe_decreasing = check_index_removed_safe(
                numbers, operator.gt, failed_at_decreasing + 1
            )
        left_removed_increasing = check_index_removed_safe(
            numbers, operator.lt, failed_at_increasing
        )

        left_removed_decreasing = check_index_removed_safe(
            numbers, operator.gt, failed_at_decreasing
        )

        second_try_safe = (
            left_removed_increasing[1]
            or right_removed_safe_increasing[1]
            or left_removed_decreasing[1]
            or right_removed_safe_decreasing[1]
        )

        return second_try_safe
    return first_try_safe


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    # print_grid(data)
    safe_count = 0
    for line in data:
        out = check_line_safe_part2(line)
        print(f"{line} {out = }")
        if out:
            print(f"Safe line {line}")
            safe_count += 1
        else:
            print(f"Unsafe line {line}")

    return safe_count


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part1_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))

# 274 Too low
# 1000 Too high
