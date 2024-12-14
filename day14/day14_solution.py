from typing import Any
from collections import defaultdict
from math import floor

current_day = "day14"


def print_grid(grid: list[Any]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write(line + "\n")


class Robot:
    x: int
    y: int
    vx: int
    vy: int

    def __init__(self, x: str, y: str, vx: str, vy: str):
        self.x = int(x)
        self.y = int(y)
        self.vx = int(vx)
        self.vy = int(vy)

    def do_step(self, grid_wide: int, grid_tall: int):
        self.x += self.vx
        self.y += self.vy

        # Went off the left
        if self.x < 0:
            # As self.x is negative adding it will subtract
            self.x = grid_wide + self.x

        # Went off the top
        if self.y < 0:
            self.y = grid_tall + self.y

        # Went off the right
        if self.x >= grid_wide:
            extra = self.x - grid_wide
            self.x = extra

        # Went off the bottom
        if self.y >= grid_tall:
            extra = self.y - grid_tall
            self.y = extra

    def __repr__(self):
        return f"Robot: {self.x = }, {self.y = }"


def do_calculation(robots: list[Robot], grid_wide: int, grid_tall: int) -> int:
    print(f"{len(robots) = }")
    split_x = floor(grid_wide / 2)
    split_y = floor(grid_tall / 2)

    print(f"{split_x = }, {split_y = }")

    # LT, LB,
    counts: dict[str, int] = defaultdict(lambda: 0)

    for robot in robots:
        horizontal_quadrant: str
        vertical_quadrant: str
        print(f"{robot} {split_x = }")
        if robot.x < split_x:
            horizontal_quadrant = "L"
        elif robot.x > split_x:
            horizontal_quadrant = "R"
        else:
            continue

        if robot.y < split_y:
            vertical_quadrant = "T"
        elif robot.y > split_y:
            vertical_quadrant = "B"
        else:
            continue

        quadrant = vertical_quadrant + horizontal_quadrant
        print(f"{robot} {quadrant}")
        counts[quadrant] += 1

    total = 1

    for key, quad_count in counts.items():
        print(f"{key=}: {quad_count}")
        total *= quad_count

    return total


def draw_grid(robots: list[Robot], grid_wide: int, grid_tall: int):
    # line = [0] * grid_wide
    # grid = [line for _ in range(grid_tall)]

    grid = [[0 for _ in range(grid_wide)] for row in range(grid_tall)]

    for robot in robots:
        grid[robot.y][robot.x] += 1

    grid_str = ["".join([str(i) for i in line]) for line in grid]

    print_grid(grid_str)


def part1(data_path: str, grid_wide: int, grid_tall: int) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)
    robots: list[Robot] = []
    for robot_data in data:
        split_robot_data = robot_data.split(" ")
        robot_pos = split_robot_data[0].split(",")
        robot_vel = split_robot_data[1].split(",")
        robots.append(
            Robot(robot_pos[0][2:], robot_pos[1], robot_vel[0][2:], robot_vel[1])
        )

    for _ in range(100):
        for robot in robots:
            robot.do_step(grid_wide, grid_tall)

    draw_grid(robots, grid_wide, grid_tall)

    return do_calculation(robots, grid_wide, grid_tall)


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)
    return 0


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt", 11, 7))
    print(part1(f"{current_day}/data.txt", 101, 103))
    # print(part2(f"{current_day}/part1_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))


# 221791248 Too high
