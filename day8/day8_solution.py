from collections import defaultdict
from itertools import combinations

current_day = "day8"


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write(line + "\n")


class Node:
    x: int
    y: int
    val: str

    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

    def __str__(self):
        return f"({self.x = }, {self.y = }, {self.val = })"

    def __repr__(self):
        return str(self)


class AntiNode:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x = }, {self.y = })"

    def __repr__(self):
        return str(self)


def calculate_m(x1: int, y1: int, x2: int, y2: int) -> float:
    """(y1 - y2) / (x1 - x2) = m"""
    return (y1 - y2) / (x1 - x2)


def calculate_b(x, y, m):
    """y = mx + b; y-mx = b"""
    return y - m * x


def edit_data(data: list[str], antinode: AntiNode, mark: str) -> list[str]:
    """Put a value into a location in data"""
    line = list(data[antinode.y])
    line[antinode.x] = mark
    data[antinode.y] = "".join(line)
    return data


def check_antinode_in_grid(
    antinodes: list[AntiNode], data: list[str]
) -> tuple[list[AntiNode], list[str]]:

    out_antinodes = []
    for antinode in antinodes:
        if (
            antinode.x >= 0
            and antinode.y >= 0
            and antinode.x < len(data[0])
            and antinode.y < len(data)
        ):
            data = edit_data(data, antinode, "#")
            out_antinodes.append(antinode)

    return out_antinodes, data


def find_antinodes(
    nodes: list[Node], data: list[str]
) -> tuple[list[AntiNode], list[str]]:
    """Determine the number of lines, determine the lines, find the"""

    antinodes: list[AntiNode] = []

    # Pair each set
    for node_1, node_2 in combinations(nodes, 2):

        print(f"{node_1} {node_2}")

        # y = mx + b

        # y - mx = b

        # y1 = mx1 + y2 - mx2

        # (y1 - y2) / (x1 - x2) = m

        # (y2-y1 = m(x2-x1) + b)

        diff_x = node_1.x - node_2.x
        diff_y = node_1.y - node_2.y

        # Todo: determine if antinodes are in the bounds of the grid
        antinodes = [
            AntiNode(node_1.x + diff_x, node_1.y + diff_y),
            AntiNode(node_2.x - diff_x, node_2.y - diff_y),
        ]

        valid_antinodes, data = check_antinode_in_grid(antinodes, data)
        antinodes.extend(valid_antinodes)

    return antinodes, data


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)

    print(f"Grid size is x: {len(data[0])} {len(data)}")
    nodes: dict[str, list[Node]] = defaultdict(lambda: [])

    for j, line in enumerate(data):
        for i, val in enumerate(line):
            if val != ".":
                nodes[val].append(Node(i, j, val))

    print(nodes)

    antiondes: list[AntiNode] = []

    for group, node_list in nodes.items():

        print(f"{group}: {node_list}")
        keep_antinodes, data = find_antinodes(node_list, data)
        antiondes.extend(keep_antinodes)

    print(antiondes)

    print_to_file(data)

    count = 0

    for line in data:
        for val in line:
            if val == "#":
                count += 1

    # return len(antiondes)
    return count


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
