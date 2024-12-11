from typing import Optional

current_day = "day6"


def location_to_id(i: int, j: int, direction: tuple[int, int]) -> str:
    return f"{i =}, {j = }, {direction = }"


class VisitedLocation:
    direction: tuple[int, int]
    x: int
    y: int

    def __init__(self, direction: tuple[int, int], x: int, y: int):
        self.direction = direction
        self.x = x
        self.y = y

    def only_coords_string(self) -> str:
        return f"{self.x =}, {self.y = }"

    def __str__(self) -> str:
        return location_to_id(self.x, self.y, self.direction)


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def print_to_file(data: list[str], name="printed.txt"):
    with open(f"{current_day}/{name}", "w") as f_out:
        for line in data:
            f_out.write(line + "\n")


def find_initial_pos(data: list[str]) -> tuple[Optional[int], Optional[int]]:
    for j, line in enumerate(data):
        for i, val in enumerate(line):
            if val == "^":
                # print(f"{i}, {j}")
                return i, j
    return None, None


def rotate(direction: tuple[int, int]) -> tuple[int, int]:
    i, j = direction
    if i == 1:
        return (0, 1)
    if i == -1:
        return (0, -1)
    if j == 1:
        return (-1, 0)
    if j == -1:
        return (1, 0)

    raise Exception("Impossible set of i ,j")


def get_all_visited_locations(data: list) -> tuple[list[VisitedLocation], bool]:
    visited_locations: list[VisitedLocation] = []

    i, j = find_initial_pos(data)

    if i is None or j is None:
        raise Exception("Initial i or j was None")

    current_direction: tuple[int, int] = (0, -1)

    initial_location = VisitedLocation(current_direction, i, j)
    visited_locations.append(initial_location)

    visited_locations_as_ids = [str(initial_location)]

    while True:
        i, j, current_direction = do_step(data, i, j, current_direction)

        if i is None or j is None:
            break

        if location_to_id(i, j, current_direction) in visited_locations_as_ids:
            return visited_locations, True

        new_location = VisitedLocation(current_direction, i, j)
        visited_locations.append(new_location)
        visited_locations_as_ids.append(str(new_location))

    return visited_locations, False


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    visited_locations, _ = get_all_visited_locations(data)

    coords_locations: list[str] = [
        visited_location.only_coords_string() for visited_location in visited_locations
    ]

    return len(set(coords_locations))


def check_inside_data(i: int, j: int, data: list[str]) -> bool:
    if i <= -1 or j <= -1 or i >= len(data[0]) or j >= len(data):
        return False

    return True


def do_step(
    data: list[str], i: int, j: int, direction: tuple[int, int]
) -> tuple[Optional[int], Optional[int], tuple[int, int]]:
    new_i = i + direction[0]
    new_j = j + direction[1]

    if not check_inside_data(new_i, new_j, data):
        return (None, None, direction)

    if data[new_j][new_i] == "#":
        return (i, j, rotate(direction))

    return (new_i, new_j, direction)


def add_block(
    data: list[str], location: VisitedLocation, value: str = "#"
) -> list[str]:
    line: list[str] = list(data[location.y])

    # We don't edit the initial block as that would alert the guard!
    if line[location.x] == "^":
        return data

    line[location.x] = value

    data[location.y] = "".join(line)

    return data


def part2(data_path: str) -> int:
    """From example, sltn order is
    1-8: 4
    3-6: 1
    3-7: 2
    7-7: 3
    7-9: 6
    """
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    loop_block_location: list[VisitedLocation] = []

    # Get every location where the guard goes
    visited_locations, _ = get_all_visited_locations(data)

    # Try placing a b lock at each of these locations

    for i, location in enumerate(visited_locations):
        print(f"Starting {i}/{len(visited_locations)}")

        edited_data = data.copy()
        edited_data = add_block(edited_data, location)

        _, is_loop = get_all_visited_locations(edited_data)

        if is_loop:
            edited_data = add_block(edited_data, location, "O")
            # print_to_file(edited_data, f"loops/{location}.txt")
            loop_block_location.append(location)

    # Run the sim to see if the guard returns to a prior location

    # If the guard is at a location he has been before and is facing the same direction
    # then he is in a loop

    deduplicated = set(
        [location.only_coords_string() for location in loop_block_location]
    )

    return len(deduplicated)


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part1_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))

# 66: Not the right answer


# Issue is that "double loops" aren't found
# Need to figure out the i, j starting of the fifth example loop and then test against
# it until my solution can find those kinds of loops!
