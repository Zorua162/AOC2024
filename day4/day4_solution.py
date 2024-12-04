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


def get_lr_diag_hori(start: int, data: list[str]) -> str:
    locs = zip(
        [i for i in range(start, len(data))], [i for i in range(0, len(data[0]))]
    )

    current = ""
    for i, j in locs:
        current += data[j][i]

    return current


def get_lr_diag_vert(start: int, data: list[str]) -> str:
    locs = zip(
        [i for i in range(0, len(data))], [i for i in range(start, len(data[0]))]
    )

    current = ""
    for i, j in locs:
        current += data[j][i]

    return current


def get_rl_diag_hori(start: int, data: list[str]) -> str:
    locs = zip(
        [i for i in range(len(data) - 1 - start, -1, -1)],
        [i for i in range(0, len(data[0]))],
    )

    current = ""
    for i, j in locs:
        print(f"{i = }, {j = }")
        current += data[j][i]

    return current


def get_rl_diag_vert(start: int, data: list[str]) -> str:
    locs = zip(
        [i for i in range(len(data) - 1, -1, -1)],
        [i for i in range(start, len(data[0]))],
    )

    current = ""
    for i, j in locs:
        current += data[j][i]

    return current


def find_diagonal(data: list[str]) -> int:
    # left-right

    diagonals = []
    for i in range(0, len(data[0])):
        diagonals.append(get_lr_diag_hori(i, data))
        diagonals.append(get_rl_diag_hori(i, data))
        if i != 0:
            diagonals.append(get_lr_diag_vert(i, data))
            diagonals.append(get_rl_diag_vert(i, data))

    print(diagonals)

    return find_words(diagonals)


def find_diagonal_old(data: list[str]) -> int:
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

    horiz = find_words(data)

    print(f"{horiz = }")

    count += horiz

    vert = find_vertical(data)

    print(f"{vert = }")

    count += vert

    diag = find_diagonal(data)

    print(f"{diag = }")

    count += diag

    return count


def interrogate_xmas(data: list[str], i: int, j: int) -> bool:
    """Look at 3x3 centered on i, j and see if it matches X-MAS"""

    patterns = ["MMSS", "SSMM", "SMMS", "MSSM"]

    if data[j][i] == "A":
        for pattern in patterns:
            if (
                data[j - 1][i - 1] == pattern[0]
                and data[j - 1][i + 1] == pattern[1]
                and data[j + 1][i + 1] == pattern[2]
                and data[j + 1][i - 1] == pattern[3]
            ):
                return True

    return False


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)
    # Plan is to look at each 3x3 section of the grid and see if it matches an X-MAS

    count = 0

    for i in range(1, len(data[0]) - 1):
        for j in range(1, len(data) - 1):
            if interrogate_xmas(data, i, j):
                count += 1

    return count


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/part1_example_data2.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))

# Part 1
# 2607 Too high
