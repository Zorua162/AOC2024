from typing import Optional

current_day = "day6"


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
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


def find_next_obstruction(
    data: list[str], i: int, j: int, direction: tuple[int, int]
) -> tuple[list[str], Optional[int], Optional[int], int, tuple[int, int]]:
    # Step in direction up until finding either a # or outside of the index of data

    blocked = False

    steps = 0

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
        line = list(data[j])
        line[i] = "X"
        data[j] = "".join(line)

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
            data, i, j, current_direction
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


def check_loop(data: list[str], i: int, j: int, direction: tuple[int, int]) -> bool:
    """Check if this obstruction meets the criteria that a loop could be created

    These are:
     - Third next obstruction steps less than first obstruction
     - Nothing blocking steps to get back
    """

    data, i_one, j_one, steps_one, direction_one = find_next_obstruction(
        data, i, j, direction
    )

    if i_one is None or j_one is None:
        return False

    data, i_two, j_two, steps_two, direction_two = find_next_obstruction(
        data, i_one, j_one, direction_one
    )

    if i_two is None or j_two is None:
        return False

    data, i_three, j_three, steps_three, direction_three = find_next_obstruction(
        data, i_two, j_two, direction_two
    )

    if steps_three < steps_one:
        print(f"Failed steps {steps_three = } {steps_one = }")
        return False

    clear_direction = rotate(direction)
    for _ in range(steps_two):
        i += clear_direction[0]
        j += clear_direction[1]
        if data[j][i] != '.':
            print("Failed blocked")
            return False

    return True


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    i, j = find_initial_pos(data)

    if i is None or j is None:
        raise Exception("Initial i or j was None")

    current_direction: tuple[int, int] = (0, -1)

    count = 0

    while True:

        data, i, j, _, current_direction = find_next_obstruction(
            data, i, j, current_direction
        )

        print(f"{i = } {j = } {count = }")

        if i is None or j is None:
            break

        if check_loop(data, i, j, current_direction):
            count += 1

    return count


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    print(part2(f"{current_day}/part1_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
