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

    def __str__(self):
        return f"Location: {self.get_id()}"


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

    def find_perimeter_part2(self, data: list[str]) -> int:
        perimeter = 0
        found_edges: list[str] = []
        for location in self.locations:
            print(location)
            for direction in directions:
                check_x = location.x + direction[0]
                check_y = location.y + direction[1]
                if (
                    not check_inside_data(check_x, check_y, data)
                    or data[check_y][check_x] != self.group_type
                ):
                    edge_id = self.find_edge_id(check_x, check_y, data, direction)
                    if edge_id not in found_edges:
                        perimeter += 1
                        found_edges.append(edge_id)
        print(f"{found_edges = }")
        return perimeter

    def find_edge_id(
        self, x: int, y: int, data: list[str], direction: tuple[int, int]
    ) -> str:
        # Loop all along this edge and find the top most or left most location

        inside_x = x - direction[0]
        inside_y = y - direction[1]

        # if direction[0] != 0:
        #     # search up down
        #     search_dir = (0, -1)
        # else:
        #     # search left right
        #     search_dir = (-1, 0)

        search_dir = rotate(direction)

        search_x = inside_x
        search_y = inside_y
        edge_x = search_x + direction[0]
        edge_y = search_y + direction[1]

        edge_id_locs: list[str] = [Location(edge_x, edge_y).get_id() + str(direction)]

        while True:
            print(f"{direction} {edge_id_locs = }")
            search_x += search_dir[0]
            search_y += search_dir[1]
            edge_x = search_x + direction[0]
            edge_y = search_y + direction[1]

            if (
                check_inside_data(search_x, search_y, data)
                and data[search_y][search_x] != self.group_type
            ):
                break

            if (
                check_inside_data(edge_x, edge_y, data)
                and data[edge_y][edge_x] == self.group_type
            ):
                break

            if not check_inside_data(search_x, search_y, data):
                break

            edge_id_locs.append(Location(edge_x, edge_y).get_id() + str(direction))

            #     pass
            #     # Rules for continuing searching this side of the edge
            #     if (
            #         not check_inside_data(search_x, search_y, data)
            #         or data[search_y][search_x] != self.group_type
            #     ) and data[edge_y][edge_x] != self.group_type:
            #         break
            # else:
            #     if (
            #         not check_inside_data(search_x, search_y, data)
            #         or
            #     ):
            #         break

        return edge_id_locs[-1]


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


def find_groups(data: list[str]) -> list[Group]:
    # keep a list of grouped locations
    already_grouped: list[str] = []
    groups: list[Group] = []

    # scan through each location, recursive search for group, add group to grouped
    # locations

    for j, line in enumerate(data):
        for i, val in enumerate(line):
            location = Location(i, j)
            if location.get_id() not in already_grouped:
                new_group = Group(location, val)
                new_group.find_locations_in_group(data)

                already_grouped.extend(new_group.get_all_location_ids())
                groups.append(new_group)
    return groups


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    # print_grid(data)

    groups = find_groups(data)

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
    # print_grid(data)

    groups = find_groups(data)

    total_price = 0

    for group in groups:
        perimeter = group.find_perimeter_part2(data)
        price = len(group.locations) * perimeter
        print(
            f"A region of {group.group_type} plants with price {len(group.locations)} * {perimeter} = {price}"
        )
        total_price += price

    # Area is just length of list

    return total_price


if __name__ == "__main__":
    # print(part1(f"{current_day}/small_example.txt"))
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    print(part2(f"{current_day}/simple_example.txt"))
    # print(part2(f"{current_day}/part1_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
