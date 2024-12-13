import numpy as np

current_day = "day13"


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write(line + "\n")


class Machine:
    prize_x: int
    prize_y: int
    A_move_x: int
    A_move_y: int
    B_move_x: int
    B_move_y: int

    def __init__(self, i, data):
        prize_line = data[i + 2].split(" ")
        self.prize_x = int(prize_line[1][2:-1])
        self.prize_y = int(prize_line[2][2:])

        A_line = data[i].split(" ")
        self.A_move_x = int(A_line[2][2:-1])
        self.A_move_y = int(A_line[3][2:])

        B_line = data[i + 1].split(" ")
        self.B_move_x = int(B_line[2][2:-1])
        self.B_move_y = int(B_line[3][2:])

        print(f"{self.prize_x = } {self.prize_y = }")
        print(f"{self.A_move_x = } {self.A_move_y = }")
        print(f"{self.B_move_x = } {self.B_move_y = }")

    def solve_part_1(self):
        Y = [self.prize_x, self.prize_y]
        A = [[self.A_move_x, self.B_move_x], [self.A_move_y, self.B_move_y]]

        res = np.linalg.inv(A).dot(Y)
        return res


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    output = 0

    machines: list[Machine] = []

    for i in range(0, len(data), 3):
        print(f"{data[i]}\n{data[i + 1]}\n{data[i + 2]}")
        machine = Machine(i, data)
        machines.append(machine)
        out = machine.solve_part_1()

        print(f"{out = }")
        A = round(out[0], 5)
        B = round(out[1], 5)

        print(f"{A = } {B = }")
        if A % 1 == 0 and B % 1 == 0:
            tokens = A * 3 + B

            print(f"{tokens = }")

            output += tokens

    return int(output)


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)
    return 0


def do_solve():
    Y = [3, 1]
    A = [[1, -2], [1, -1]]

    res = np.linalg.inv(A).dot(Y)
    print(res)


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # do_solve()
    print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part1_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
