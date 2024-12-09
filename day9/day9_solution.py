from typing import Optional

current_day = "day9"


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def print_to_file(data: str):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        f_out.write(data + "\n")


def compact(values: list[Optional[int]]) -> list[Optional[int]]:
    end_index = len(values) - 1
    start_index = 0

    while True:
        end_value = values.pop()
        while end_value is None:
            end_index -= 1
            end_value = values.pop()

        len_values = len(values)
        if start_index >= len_values:
            values.append(end_value)
            return values
        start_value = values[start_index]
        while start_value is not None:
            start_index += 1
            # print(start_index)
            # print(values)
            if start_index >= len_values:
                values.append(end_value)
                return values
            start_value = values[start_index]
            # A, B, C
            # 0, 1, 2
            # len() = 3

        values[start_index] = end_value


def calc_answer(compacted: list[Optional[int]]) -> int:
    count = 0
    for i, val in enumerate(compacted):
        if val is None:
            continue
        count += i * val
    return count


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    expanded: list[Optional[int]] = []

    line = data[0]

    i = 0
    free_space = False
    for value in line:
        if not free_space:
            expanded.extend([i] * int(value))
            i += 1
        else:
            expanded.extend([None] * int(value))
        free_space = not free_space

    compacted = compact(expanded)

    print(compacted)

    return calc_answer(compacted)


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)
    return 0


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    print(part1(f"{current_day}/data.txt"))
    # print(part1(f"{current_day}/my_test_data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))

# 91111740342 Too low
