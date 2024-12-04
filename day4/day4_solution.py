import re
from collections import defaultdict

current_day = "day4"

xmas = re.compile(r"XMAS")
samx = re.compile(r"SAMX")


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write(line)


def find_vertical(data: list[str]) -> int:
    """Find each vertical version of XMAS and SAMX"""
    vertical_data: list[str] = ["" for _ in range(len(data[0]))]

    for i in range(len(data[0])):
        print(f"{i = } {len(data[0]) = } {vertical_data = }")
        for j in range(len(data)):
            vertical_data[j] += data[i][j]

    return find_words(vertical_data)


#   1 2 3
# 1 A B C
# 2 D E F
# 3 G H I


def find_diagonal(data: list[str]) -> int:
    diagonal_lines = defaultdict(lambda: [])
    for vert_offset in range(-len(data[0]), len(data)):
        for i in range(len(data[0])):
            for j in range(len(data)):
                if i == j + vert_offset:
                    diagonal_lines[f"v{vert_offset}"].append(data[i][j])

    for hori_offset in range(-len(data[0]), len(data)):
        for i in range(len(data[0])):
            for j in range(len(data)):
                if i + hori_offset == j:
                    diagonal_lines[f"h{hori_offset}"].append(data[i][j])

    print(diagonal_lines)

    return find_words(["".join(values) for values in diagonal_lines.values()])


def find_words(data: list[str]) -> int:
    """Find each of the possible XMAS words in the word search"""
    count = 0

    for line in data:
        count += len(xmas.findall(line))
        count += len(samx.findall(line))

    return count


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    count = 0

    count += find_words(data)

    count += find_vertical(data)

    count += find_diagonal(data)

    return count


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)
    return 0


if __name__ == "__main__":
    print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/part1_example_data2.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))

# 2607 Too high
