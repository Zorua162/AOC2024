from __future__ import annotations

from typing import Any
from typing import Optional
from typing import Union


current_day = "day15"

move_dict: dict[str, tuple[int, int]] = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, 1),
}


def print_grid(grid: list[Any]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write(line + "\n")


class Location:
    x: int
    y: int

    def __repr__(self):
        return f"({type(self).__name__}: {self.x = }, {self.y = })"

    def do_move(
        self, move: str, wall_map: list[str], boxes: list[Union[Robot, Box]]
    ) -> bool:
        move_vector = move_dict[move]
        new_x = self.x + move_vector[0]
        new_y = self.y + move_vector[1]

        # If the new location is a wall then return
        if wall_map[new_y][new_x] == "#":
            return False

        # Now we see if boxes would block (or should be moved)

        successful = True

        for box in boxes:
            # If a box is at our new coords, then it needs to be moved
            # This then needs to be run on the box that was moved to see if other boxes
            # need to be moved too
            if box.x == new_x and box.y == new_y:
                successful = box.do_move(move, wall_map, boxes)
            if not successful:
                return False

        self.x = new_x
        self.y = new_y
        return True


class Box(Location):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Robot(Location):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = f_obj.read()

    split_data = data.split("\n\n")

    initial_map = split_data[0].split("\n")

    moves = split_data[1][:-1].replace("\n", "")

    print(f"{initial_map = } {moves = }")

    robot: Optional[Robot] = None
    boxes: list[Box] = []

    for j, line in enumerate(initial_map):
        for i, val in enumerate(line):
            if val == "@":
                robot = Robot(i, j)
            elif val == "O":
                boxes.append(Box(i, j))

    if robot is None:
        raise Exception("Robot not found")

    do_moves(robot, boxes, initial_map, moves)

    return calculate_coords(boxes)


def calculate_coords(boxes: list[Box]) -> int:
    total = 0
    for box in boxes:
        total += 100 * box.y + box.x

    return total


def make_empty_map(initial_map: list[str]) -> list[str]:
    current_map: list[str] = []
    for row in initial_map:
        current_map.append(row.replace("O", ".").replace("@", "."))

    return current_map


def output_situation(robot: Robot, boxes: list[Box], empty_map: list[str]):
    current_map: list[list[str]] = [list(row) for row in empty_map]

    for box in boxes:
        current_map[box.y][box.x] = "O"

    current_map[robot.y][robot.x] = "@"

    print_grid(["".join(row) for row in current_map])


def do_moves(robot: Robot, boxes: list[Box], initial_map: list[str], moves: str):
    empty_map: list[str] = make_empty_map(initial_map)
    for move in moves:
        # print(move)
        robot.do_move(move, empty_map, boxes)  # type: ignore
        # output_situation(robot, boxes, empty_map)


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)
    return 0


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/larger_example_data.txt"))
    print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part1_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
