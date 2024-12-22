from typing import Any

from copy import deepcopy

import networkx as nx  # type: ignore

from math import ceil
from math import floor

current_day = "day18"

directions = ((0, -1), (1, 0), (0, 1), (-1, 0))


def print_grid(grid: list[Any]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write(line + "\n")


class Grid:
    grid_end: int
    grid: list[list[str]]

    def __init__(self, grid_end):
        self.grid_end = grid_end

        total_grid = grid_end + 1
        self.grid = [["." for _ in range(total_grid)] for _ in range(total_grid)]

        # print_grid(self.grid)

    def add_byte(self, loc: str):
        split_loc = loc.split(",")
        x = int(split_loc[0])
        y = int(split_loc[1])

        self.grid[y][x] = "#"

    def inside_grid(self, x: int, y: int) -> bool:
        return x >= 0 and y >= 0 and x < self.grid_end + 1 and y < self.grid_end + 1

    def add_adjacent_nodes(self, x: int, y: int, G: nx.Graph) -> nx.Graph:
        if self.grid[y][x] == "#":
            return G

        for direction in directions:
            conn_x = x + direction[0]
            conn_y = y + direction[1]
            # print(G.edges())
            if (
                not self.inside_grid(conn_x, conn_y)
                or self.grid[conn_y][conn_x] == "#"
                or (get_node_name(conn_x, conn_y), get_node_name(x, y)) in G.edges()
            ):
                continue
            new_node_name = get_node_name(conn_x, conn_y)
            G.add_node(new_node_name)
            G.add_edge(new_node_name, get_node_name(x, y))

        return G

    def draw_path(self, path: list):
        draw_grid = self.grid.copy()

        for node in path:
            split_node = node.split(",")
            x = int(split_node[0])
            y = int(split_node[1])
            draw_grid[y][x] = "O"

        out_grid = ["".join(row) for row in draw_grid]
        print_grid(out_grid)


def generate_graph(grid: Grid) -> nx.Graph:
    G = nx.Graph()

    G.add_node(get_node_name(0, 0))

    for j in range(len(grid.grid)):
        for i in range(len(grid.grid[0])):
            G = grid.add_adjacent_nodes(j, i, G)

    return G


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    if "example" in data_path:
        max_size = 6
        num_add_bytes = 12
    else:
        max_size = 70
        num_add_bytes = 1024

    grid = Grid(max_size)

    for i in range(num_add_bytes):
        bytes = data[i]
        print(f"{i = }, {bytes = }")
        grid.add_byte(bytes)
    print_grid(["".join(row) for row in grid.grid])

    return find_shortest_path(grid, 0, 0, max_size, max_size)


def get_node_name(x: int, y: int) -> str:
    return f"{x}, {y}"


def find_shortest_path(
    grid: Grid, start_x: int, start_y: int, end_x: int, end_y: int
) -> int:
    G = generate_graph(grid)

    path: list = nx.dijkstra_path(
        G, get_node_name(start_x, start_y), get_node_name(end_x, end_y)
    )

    # grid.draw_path(path)

    return len(path) - 1


def part2(data_path: str) -> str:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    if "example" in data_path:
        max_size = 6
    else:
        max_size = 70

    grid = Grid(max_size)

    found = False
    split = round(len(data) / 2)
    lowest_possible = 0
    highest_possible = len(data)
    while not found:
        # search the left side of this

        if test_possible(deepcopy(grid), split, data, max_size):
            lowest_possible = split
            split = split + ceil((highest_possible - split) / 2)
            print("low")
        else:
            highest_possible = split
            split = split - floor((split - lowest_possible) / 2) - 1
            print("high")

        if split == lowest_possible:
            found = True

    return data[split]


def test_possible(grid: Grid, num_bytes: int, data: list[str], max_size) -> bool:
    for i in range(num_bytes):
        byte = data[i]
        grid.add_byte(byte)

    try:
        find_shortest_path(grid, 0, 0, max_size, max_size)
    except Exception as e:
        print(f"{e} {num_bytes = }")
        return False

    return True


if __name__ == "__main__":
    # print(part1(f"{current_day}/example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/example_data.txt"))
    print(part2(f"{current_day}/data.txt"))

# OO.#OOO
# .O#OO#O
# .OOO#OO
# ...#OO#
# ..#OO#.
# .#.O#..
# #.#OOOO

# OO.#OOO
# .O#OO#O
# .OOO#OO
# ...#OO#
# ..#OO#.
# .#.O#..
# #.#OOOO
