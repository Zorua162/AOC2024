current_day = "day1"


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write(line)


def create_lists(data: list[str]) -> list[list[int]]:
    """Create lists from the left and right column of numbers"""

    listl = []
    listr = []

    for line in data:
        split = line.split("   ")
        listl.append(int(split[0]))
        listr.append(int(split[1]))

    lists = [listl, listr]

    return lists


def sort_lists(lists: list[list[int]]) -> list[list[int]]:
    """Sort both lists into ascending order"""
    return [sorted(a_list) for a_list in lists]


def find_diffs(lists: list[list[int]]) -> int:
    """Iterate through each pair and find their difference"""
    total_diff = 0
    for i, j in zip(lists[0], lists[1]):
        this_diff = abs(j - i)
        total_diff += this_diff
    return total_diff


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)
    lists = create_lists(data)
    sorted_lists = sort_lists(lists)
    return find_diffs(sorted_lists)


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)
    return 0


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
