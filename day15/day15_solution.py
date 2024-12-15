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
        return f"({self.__hash__} {type(self).__name__}: {self.x = }, {self.y = })"

    def do_move(
        self,
        move: str,
        wall_map: list[str],
        boxes: list[Union[Box, LargeBox]],
        already_moved: list[Union[Box, LargeBox]],
    ) -> tuple[bool, list[Union[Box, LargeBox]]]:
        # print(f"Doing move for {self}")
        move_vector = move_dict[move]
        new_x = self.x + move_vector[0]
        new_y = self.y + move_vector[1]

        # If the new location is a wall then return
        if wall_map[new_y][new_x] == "#":
            return False, already_moved

        # Now we see if boxes would block (or should be moved)
        if isinstance(self, LargeBox):
            if wall_map[new_y][new_x + 1] == "#":
                return False, already_moved

        successful = True

        for box in boxes:
            if self == box:
                continue
            successful, already_moved = try_move(
                new_x, new_y, box, move, wall_map, boxes, already_moved
            )
            if isinstance(self, LargeBox) and not self == box:
                successful_right, already_moved = try_move(
                    new_x + 1, new_y, box, move, wall_map, boxes, already_moved
                )

                successful = successful and successful_right

            if not successful:
                return False, already_moved

        self.x = new_x
        self.y = new_y
        if isinstance(self, Box) or isinstance(self, LargeBox):
            # print(f"Appending to already_moved {self = } {already_moved = }")
            already_moved.append(self)
        return True, already_moved


def try_move(
    new_x: int,
    new_y: int,
    box: Union[Box, LargeBox],
    move: str,
    wall_map: list[str],
    boxes: list[Union[Box, LargeBox]],
    already_moved: list[Union[Box, LargeBox]],
) -> tuple[bool, list[Union[Box, LargeBox]]]:
    successful = True
    # If a box is at our new coords, then it needs to be moved
    # This then needs to be run on the box that was moved to see if other boxes
    # need to be moved too
    if box.x == new_x and box.y == new_y:
        successful, already_moved = box.do_move(move, wall_map, boxes, already_moved)

    if isinstance(box, LargeBox):
        if box.x + 1 == new_x and box.y == new_y:
            successful, already_moved = box.do_move(
                move, wall_map, boxes, already_moved
            )
    return successful, already_moved


class Box(Location):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class LargeBox(Location):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Robot(Location):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def parse_data(data_path: str) -> tuple[str, list[str]]:
    with open(data_path, "r") as f_obj:
        data = f_obj.read()

    split_data = data.split("\n\n")

    initial_map = split_data[0].split("\n")

    moves = split_data[1][:-1].replace("\n", "")

    return moves, initial_map


def calculate_coords(boxes: list[Union[Box, LargeBox]]) -> int:
    total = 0
    for box in boxes:
        total += 100 * box.y + box.x

    return total


def make_empty_map(initial_map: list[str]) -> list[str]:
    current_map: list[str] = []
    for row in initial_map:
        current_map.append(
            row.replace("O", ".").replace("@", ".").replace("[", ".").replace("]", ".")
        )

    return current_map


def output_situation(
    robot: Robot, boxes: list[Union[Box, LargeBox]], empty_map: list[str]
):
    current_map: list[list[str]] = [list(row) for row in empty_map]

    for box in boxes:
        # print(f"{box}")
        if isinstance(box, Box):
            current_map[box.y][box.x] = "#"
        else:
            current_map[box.y][box.x] = "["
            current_map[box.y][box.x + 1] = "]"

    current_map[robot.y][robot.x] = "@"

    # print_grid(["".join(row) for row in current_map])


def do_moves(
    robot: Robot, boxes: list[Union[Box, LargeBox]], initial_map: list[str], moves: str
):
    empty_map: list[str] = make_empty_map(initial_map)
    for move in moves:
        already_moved: list[Union[Box, LargeBox]] = []
        # print(f"{move = }")
        successful, already_moved = robot.do_move(move, empty_map, boxes, already_moved)  # type: ignore
        if not successful:
            # print(f"{already_moved = }")
            # Undo the move for that box
            for box in already_moved:
                box.x -= move_dict[move][0]
                box.y -= move_dict[move][1]

        output_situation(robot, boxes, empty_map)


def expand_map(initial_map: list[str]) -> list[str]:
    expanded_map = []
    for row in initial_map:
        expanded_map.append(
            row.replace("#", "##")
            .replace(".", "..")
            .replace("O", "[]")
            .replace("@", "@.")
        )

    return expanded_map


def part1(data_path: str) -> int:
    moves, initial_map = parse_data(data_path)
    print(f"{initial_map = } {moves = }")

    robot: Optional[Robot] = None
    boxes: list[Union[Box, LargeBox]] = []

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


def part2(data_path: str) -> int:
    moves, initial_map = parse_data(data_path)

    expanded_map = expand_map(initial_map)

    print_grid(expanded_map)

    robot: Optional[Robot] = None
    boxes: list[Union[Box, LargeBox]] = []

    for j, line in enumerate(expanded_map):
        for i, val in enumerate(line):
            if val == "@":
                robot = Robot(i, j)
            elif val == "[":
                boxes.append(LargeBox(i, j))

    if robot is None:
        raise Exception("Robot not found")

    do_moves(robot, boxes, expanded_map, moves)

    return calculate_coords(boxes)


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    # print(part2(f"{current_day}/larger_example_data.txt"))
    # print(part2(f"{current_day}/my_test_case.txt"))
    print(part2(f"{current_day}/data.txt"))
