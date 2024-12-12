current_day = "day12"

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


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

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_id(self):
        return f"{self.x = }, {self.y = }"


class Group:
    locations: list[Location]
    group_type: str

    def __init__(self, initial_location: Location, type: str):
        self.locations = [initial_location]
        self.group_type = type

    def get_all_location_ids(self):
        return [location.get_id() for location in self.locations]

    def find_locations_in_group(self, data: list[str]) -> list[Location]:
        self.find_neighbors(self.group_type, self.locations[0], data)

        return self.locations

    def find_neighbors(
        self,
        search_type,
        this_location: Location,
        data: list[str],
    ):
        new_locations: list[Location] = []

        i = this_location.x
        j = this_location.y

        for direction in directions:
            x = i + direction[0]
            y = j + direction[1]

            if check_inside_data(x, y, data) and data[y][x] == search_type:
                location = Location(x, y)
                if location.get_id() not in self.get_all_location_ids():
                    new_locations.append(location)

        self.locations.extend(new_locations)

        for location in new_locations:
            self.find_neighbors(search_type, location, data)

    def find_perimeter(self, data: list[str]) -> int:
        perimeter = 0
        for location in self.locations:
            for direction in directions:
                check_x = location.x + direction[0]
                check_y = location.y + direction[1]
                if (
                    not check_inside_data(check_x, check_y, data)
                    or data[check_y][check_x] != self.group_type
                ):
                    perimeter += 1
        return perimeter


def check_at_perimeter(data: list[str], i: int, j: int, group_type: str) -> bool:
    return not check_inside_data(i, j, data) or data[j][i] != group_type


def do_step(
    x: int, y: int, direction: tuple[int, int], backwards: bool = False
) -> tuple[int, int]:
    if backwards:
        return (x - direction[0], y - direction[1])
    return (x + direction[0], y + direction[1])


def rotate(direction: tuple[int, int], clockwise: str = "clockwise") -> tuple[int, int]:
    if clockwise == "clockwise":
        index_add = 1
    else:
        index_add = -1
    index = directions.index(direction)
    # print(f"{index = } {index_add = }")
    new_index = index + index_add
    if new_index >= len(directions):
        new_index = 0
    # print(f"{new_index = } {directions = }")
    return directions[new_index]


def check_inside_data(i: int, j: int, data: list[str]) -> bool:
    if i <= -1 or j <= -1 or i >= len(data[0]) or j >= len(data):
        return False

    return True


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    # print_grid(data)

    # Plan
    # keep a list of grouped locations
    already_grouped: list[str] = []
    groups: list[Group] = []

    # scan through each location, recursive search for group, add group to grouped
    # locations

    for j, line in enumerate(data):
        for i, val in enumerate(line):
            print(f"Starting location {i = } {j = }")
            location = Location(i, j)
            if location.get_id() not in already_grouped:
                new_group = Group(location, val)
                new_group.find_locations_in_group(data)

                already_grouped.extend(new_group.get_all_location_ids())
                groups.append(new_group)

    total_price = 0

    for group in groups:
        perimeter = group.find_perimeter(data)
        price = len(group.locations) * perimeter
        print(
            f"A region of {group.group_type} plants with price {len(group.locations)} * {perimeter} = {price}"
        )
        total_price += price

    # Area is just length of list

    return total_price


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)
    return 0


if __name__ == "__main__":
    # print(part1(f"{current_day}/small_example.txt"))
    # print(part1(f"{current_day}/part1_example_data.txt"))
    print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part1_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
