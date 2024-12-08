from typing import Optional

current_day = "day6"


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


def edit_data(data: list[str], i: int, j: int, mark: str) -> list[str]:
    """Put a value into a location in data"""
    if data[j][i] == "#":
        mark = "+"
    line = list(data[j])
    line[i] = mark
    data[j] = "".join(line)
    return data


def find_next_obstruction(
    data: list[str], i: int, j: int, direction: tuple[int, int], marker: str
) -> tuple[list[str], Optional[int], Optional[int], int, tuple[int, int]]:
    # Step in direction up until finding either a # or outside of the index of data

    blocked = False

    steps = 1

    while not blocked:
        i += direction[0]
        j += direction[1]

        if i < 0 or j < 0:
            return data, None, None, steps, rotate(direction)

        try:
            # print(f"{i}, {j}, {data[j][i]}")
            if data[j][i] == "#":
                # print("Found #")
                blocked = True
                break
        except IndexError:
            blocked = True
            return data, None, None, steps, rotate(direction)
        steps += 1
        edit_data(data, i, j, marker)

    return data, i - direction[0], j - direction[1], steps, rotate(direction)


# def do_step(data: list[str]) -> list[str]:


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    i, j = find_initial_pos(data)

    if i is None or j is None:
        raise Exception("Initial i or j was None")

    current_direction: tuple[int, int] = (0, -1)
    count = 0

    while True:

        data, i, j, steps_taken, current_direction = find_next_obstruction(
            data, i, j, current_direction, "X"
        )
        print(f"Starting new direction {current_direction}, {i}, {j}")
        print_grid(data)
        # print_to_file(data)

        count += steps_taken

        if i is None or j is None:
            break

    location_count = 0

    for line in data:
        for loc in line:
            if loc == "X":
                location_count += 1

    return location_count


def check_loop(
    data: list[str], i: int, j: int, steps: int, direction: tuple[int, int]
) -> bool:
    """Check if this obstruction meets the criteria that a loop could be created

    These are:
     - Nothing blocking steps to get back
    """

    print(f"Started at {i = } {j = }")

    loop_data = data.copy()

    loop_data, i_one, j_one, steps_one, direction_one = find_next_obstruction(
        loop_data, i, j, direction, "1"
    )

    if i_one is None or j_one is None:
        return False

    loop_data, i_two, j_two, steps_two, direction_two = find_next_obstruction(
        loop_data, i_one, j_one, direction_one, "2"
    )

    if i_two is None or j_two is None:
        return False

    # if steps_three > steps:
    #     print(f"Failed steps {steps_three = } {steps_one = }")
    #     return False

    clear_direction = direction_two
    j = j_two
    i = i_two
    for _ in range(steps_one):
        i += clear_direction[0]
        j += clear_direction[1]
        if i < 0 or j < 0 or i > len(data[0]) - 1 or j > len(data) - 1:
            print(f"Failed out of range {i = }, {j = }")
            return False
        loc = data[j][i]
        edit_data(loop_data, i, j, "=")
        print_to_file(loop_data)
        if loc == "#":  # or loc == "^":
            print(f"Failed blocked {i = }, {j = } {loc}")
            return False
    edit_data(loop_data, i, j, "O")
    print_to_file(loop_data, name=f"loops/loop{i}-{j}.txt")
    print("Loop found")
    return True


def part2(data_path: str) -> int:
    """From example, sltn order is 1, 2, 4, """
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    i, j = find_initial_pos(data)

    if i is None or j is None:
        raise Exception("Initial i or j was None")

    current_direction: tuple[int, int] = (0, -1)

    count = 0

    while True:

        mark = "X"

        if current_direction[0] != 0:
            mark = "-"
        else:
            mark = "|"

        data, i, j, steps, current_direction = find_next_obstruction(
            data, i, j, current_direction, mark
        )

        print(f"{i = } {j = } {count = }")

        if i is None or j is None:
            break

        if check_loop(data, i, j, steps, current_direction):
            count += 1
            print(f"Current loop count is {count = }")

    return count


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    print(part2(f"{current_day}/part1_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
