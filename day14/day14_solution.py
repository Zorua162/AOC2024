from typing import Any
from collections import defaultdict
from os import listdir
from math import floor
from math import sqrt
from time import sleep
from time import time

current_day = "day14"


def print_grid(grid: list[Any]):
    for line in grid:
        print(line)


def print_to_file(data: list[str], file_name: str = "printed.txt"):
    with open(f"{current_day}/{file_name}", "w") as f_out:
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

    grid_str_list = ["".join([str(i) for i in line]) for line in grid]
    grid_str_list = [line.replace("0", ".") for line in grid_str_list]

    return grid_str_list


def create_robots(data_path: str) -> list[Robot]:
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
    return robots


def move_robots(
    data_path: str,
    grid_wide: int,
    grid_tall: int,
    iterations: int,
    do_print: str = "",
) -> list[Robot]:
    robots = create_robots(data_path)

    for i in range(iterations):
        if i % 1000 == 0:
            print(f"Starting iteration {i}")
        for robot in robots:
            robot.do_step(grid_wide, grid_tall)
        if do_print == "terminal":
            if i < 7400:
                continue

            print(f"Iteration {i}")
            grid = draw_grid(robots, grid_wide, grid_tall)
            print_grid(grid)
        elif do_print == "file":
            grid = draw_grid(robots, grid_wide, grid_tall)
            print_to_file(grid, f"grids/iteration{i}.txt")

    return robots


def part1(data_path: str, grid_wide: int, grid_tall: int) -> int:
    robots = move_robots(data_path, grid_wide, grid_tall, 100)

    draw_grid(robots, grid_wide, grid_tall)

    return do_calculation(robots, grid_wide, grid_tall)


def find_loop(robot: Robot, grid_wide: int, grid_tall: int) -> int:
    start_x = robot.x
    start_y = robot.y
    for i in range(100000):
        robot.do_step(grid_wide, grid_tall)

        # print(f"{robot.x = } {start_x = } {robot.y = } {start_y = }")

        if robot.x == start_x and robot.y == start_y:
            print(f"Looped at iteration {i}")
            # break
    return i


def look_for_loops(data_path: str, grid_wide: int, grid_tall: int):
    robots = create_robots(data_path)

    # for robot in robots:
    robot = robots[0]

    iteration = find_loop(robot, grid_wide, grid_tall)

    print(f"Looped at iteration {iteration}")


def calculate_closeness(robots: list[Robot]) -> int:
    """Sum the distances between each of the robots (this ain't gonna be pretty)"""

    sum: float = 0

    the_man = robots[0]

    for robot in robots:
        sum += sqrt((robot.x - the_man.x) ** 2 + (robot.y - the_man.y) ** 2)

    return int(sum)


def determine_all_closeness(
    data_path: str, grid_wide: int, grid_tall: int, iterations: int
) -> dict[int, int]:
    robots = create_robots(data_path)

    closeness_dict: dict[int, int] = {}
    start = time()
    for i in range(0, iterations):
        if i % 10 == 0:
            now = time()
            elapsed = now - start
            per_time = i / elapsed
            remaining = iterations * per_time
            print(f"Starting iteration {i} {elapsed = } {remaining = }")
        for robot in robots:
            robot.do_step(grid_wide, grid_tall)

        closeness = calculate_closeness(robots)
        closeness_dict[closeness] = i

    return closeness_dict


def do_closeness(
    data_path: str, grid_wide: int, grid_tall: int, iterations: int
) -> int:
    closeness = determine_all_closeness(data_path, grid_wide, grid_tall, 10402)

    print(closeness)

    closest = sorted(closeness.keys())[0]
    iteration = closeness[closest]
    print(f"Closest value is {closest} which was iteration {iteration}")
    return iteration + 1


def part2(data_path: str, grid_wide: int, grid_tall: int) -> int:
    robots = move_robots(data_path, grid_wide, grid_tall, 7492, "terminal")
    draw_grid(robots, grid_wide, grid_tall)

    # look_for_loops(data_path, grid_wide, grid_tall)

    # do_closeness(data_path, grid_wide, grid_tall, 10402)

    return 0


def grid_viewer():
    grids_path = f"{current_day}/grids"
    grids = sorted(listdir(grids_path))

    for i in range(0, len(grids)):
        grid = grids[i]
        grid_path = f"{grids_path}/{grid}"
        print(f"Path to grid is {grid_path}")

        with open(grid_path, "r") as grid_obj:
            print(grid_obj.read())
        sleep(0.1)


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt", 11, 7))
    # print(part1(f"{current_day}/data.txt", 101, 103))
    print(part2(f"{current_day}/data.txt", 101, 103))
    # grid_viewer()


# 221791248 Too high
