from typing_extensions import Self
from typing import Optional

current_day = "day10"

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write(line + "\n")


class Location:
    x: int
    y: int
    value: Optional[int]

    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        # print(f"{x = }, {y = }")
        if x < 0 or y < 0:
            self.value = None
            return

        try:
            self.value = int(data[y][x])
        except IndexError:
            self.value = None

    def __repr__(self):
        return f"{self.x = }, {self.y = }, {self.value = }"

    def __str__(self):
        return f"{self.x = }, {self.y = }, {self.value = }"


class Route:
    path: list[Location]

    def __init__(self, path: list[Location]):
        self.path = path

    def __repr__(self):
        return f"{self.path = }"

    def finished(self) -> bool:
        return self.path[-1].value == 9

    def find_routes(self, data) -> list[Self]:
        routes: list[Route] = []
        current_end = self.path[-1]
        for direction in directions:
            possible_next_location = Location(
                current_end.x + direction[0], current_end.y + direction[1], data
            )
            pass
            if (
                possible_next_location.value is not None
                and current_end.value is not None
                and possible_next_location.value == current_end.value + 1
            ):
                route_path = self.path.copy()
                route_path.append(possible_next_location)
                routes.append(Route(route_path))

        recursed_routes = []
        for route in routes:
            recursed_routes.extend(route.find_routes(data))

        recursed_routes.extend(routes)

        return recursed_routes  # type: ignore


def count_tops(routes: list[Route]) -> int:
    end_locations: set[str] = set()
    for route in routes:
        end_location = route.path[-1]
        if end_location.value == 9:
            end_locations.add(str(end_location))

    print(f"{end_locations = }")
    return len(end_locations)


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)

    total_routes = 0

    for j, line in enumerate(data):
        for i, val in enumerate(line):
            if val == "0":
                print(f"Starting search at {i = } {j = }")
                routes = Route([Location(i, j, data)]).find_routes(data)
                score = count_tops(routes)
                print(f"Score is {score}")
                total_routes += score

    return total_routes


def count_routes(routes: list[Route]) -> int:
    complete_routes: list[Route] = []
    for route in routes:
        end_location = route.path[-1]
        if end_location.value == 9:
            complete_routes.append(route)

    print(f"{complete_routes = }")
    return len(complete_routes)


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)

    total_routes = 0

    for j, line in enumerate(data):
        for i, val in enumerate(line):
            if val == "0":
                print(f"Starting search at {i = } {j = }")
                routes = Route([Location(i, j, data)]).find_routes(data)
                score = count_routes(routes)
                print(f"Score is {score}")
                total_routes += score
    return 0


if __name__ == "__main__":
    # print(part1(f"{current_day}/simple_data.txt"))
    # print(part1(f"{current_day}/part1_example_data.txt"))
    print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part1_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
