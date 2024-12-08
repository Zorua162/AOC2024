from itertools import product

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
        val = eval(f"{val}{operator}{numbers[i+1]}")

    return val


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    total = 0

    for line in data:
        split_line = line.split(": ")
        goal_number = int(split_line[0])

        input_numbers = [int(x) for x in split_line[1].split(" ")]

        # print(goal_number, input_numbers)

        num_operators = len(input_numbers) - 1

        # for i in range(2 ** (num_operators - 1), 2 ** num_operators):
        #     operators = f"{bin(i)}"[2:]
        #     print(operators)
        #     operators = operators.replace("1", "+")
        #     operators = operators.replace("0", "*")
        #     print(operators)

        possible_out = []

        for operators in product(["*", "+"], repeat=num_operators):
            possible_out.append(solve_equation(operators, input_numbers))

        if goal_number in possible_out:
            # print(f"Valid number {goal_number} {possible_out}")
            total += goal_number

    return total


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)
    return 0


if __name__ == "__main__":
    print("")
    # print(part1(f"{current_day}/part1_example_data.txt"))
    print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
