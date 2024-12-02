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


def check_increasing_safe_part2(numbers: list[int]) -> bool:
    """Check if all the numbers increase"""
    # print("Checking increasing")
    skipped_incorrect = False
    current_num = numbers[0]
    for next_number in numbers[1:]:
        # print(f"{next_number = } {current_num = }")
        if (
            next_number < current_num
            or abs(next_number - current_num) > 3
            or abs(next_number - current_num) < 1
        ):
            if not skipped_incorrect:
                skipped_incorrect = True
                continue
            else:
                return False
        current_num = next_number
    print("Increasing safe")
    return True


def check_decreasing_safe_part2(numbers: list[int]) -> bool:
    """Check if all the numbers decrease"""
    # print("Checking decreasing")
    skipped_incorrect = False
    current_num = numbers[0]
    for next_number in numbers[1:]:
        # print(f"{next_number = } {current_num = }")
        if (
            next_number > current_num
            or abs(next_number - current_num) > 3
            or abs(next_number - current_num) < 1
        ):
            if not skipped_incorrect:
                skipped_incorrect = True
                continue
            else:
                return False
        current_num = next_number
    print("Decreasing safe")
    return True


def check_line_safe_part2(line: str) -> bool:
    numbers = [int(i) for i in line.split(" ")]
    increasing_safe = check_increasing_safe_part2(numbers)
    decreasing_safe = check_decreasing_safe_part2(numbers)
    return increasing_safe or decreasing_safe


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    # print_grid(data)
    safe_count = 0
    for line in data:
        if check_line_safe_part2(line):
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
