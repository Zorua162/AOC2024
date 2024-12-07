from itertools import product
from math import prod

current_day = "day7"


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write(line)


def solve_equation(operators: tuple[str, ...], numbers: list[int]) -> int:

    val = numbers[0]

    for i, operator in enumerate(operators):
        if operator == "||":
            val = int(str(val) + str(numbers[i + 1]))
        else:
            val = eval(f"{val}{operator}{numbers[i+1]}")

    return val


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    total = 0

    for i, line in enumerate(data):
        print(f"Starting line {i} {line = }")
        split_line = line.split(": ")
        goal_number = int(split_line[0])

        input_numbers = [int(x) for x in split_line[1].split(" ")]

        # print(goal_number, input_numbers)

        num_operators = len(input_numbers) - 1

        possible_out = []

        for operators in product(["*", "+"], repeat=num_operators):
            possible_out.append(solve_equation(operators, input_numbers))

        if goal_number in possible_out:
            # print(f"Valid number {goal_number} {possible_out}")
            total += goal_number

    return total


def check_possible(input_numbers: list[int], goal_number: int):
    """Maximum possible is timing all together, so check that the goal number is possible"""
    prod_nums = prod(input_numbers)
    print(f"{prod_nums = } {prod_nums - goal_number = }")
    return prod_nums > goal_number


def solve_equation_smart(
    operators: tuple[str, ...], numbers: list[int], goal_number: int
) -> int:

    val = numbers[0]

    for i, operator in enumerate(operators):
        if operator == "||":
            val = int(str(val) + str(numbers[i + 1]))
        else:
            val = eval(f"{val}{operator}{numbers[i+1]}")

        if val > goal_number:
            # print("Too big, continuing")
            return val
    # print(f"Val is {val}")

    return val


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:

        data = [line for line in f_obj.read().split("\n") if line != ""]

    total = 0

    for i, line in enumerate(data):
        print(f"Starting line {i} {line = }")
        split_line = line.split(": ")
        goal_number = int(split_line[0])

        input_numbers = [int(x) for x in split_line[1].split(" ")]

        # print(goal_number, input_numbers)

        num_operators = len(input_numbers) - 1

        possible_out = []

        # if not check_possible(input_numbers, goal_number):
        #     print("Not possible with prod")
        #     continue

        for operators in product(["*", "+", "||"], repeat=num_operators):
            possible_out.append(
                solve_equation_smart(operators, input_numbers, goal_number)
            )

        if goal_number in possible_out:
            # print(f"Valid number {goal_number} {possible_out}")
            total += goal_number

    return total


if __name__ == "__main__":
    print("")
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part1_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))
