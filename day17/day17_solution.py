from typing import Any
from typing import Optional


from math import trunc

current_day = "day17"


def print_grid(grid: list[Any]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write(line + "\n")


class Computer:
    A: int
    B: int
    C: int
    pointer: int = 0
    instructions: list[int]

    def __init__(self, A: int, B: int, C: int, instructions: str):
        self.A = A
        self.B = B
        self.C = C

        self.instructions = [int(val) for val in instructions.split(",")]

        self.pointer = 0

    def do_instruction(self, opcode: int, operand: int) -> Optional[int]:
        if operand == 4:
            val = self.A
        elif operand == 5:
            val = self.B
        elif operand == 6:
            val = self.C
        else:
            val = operand

        # adv
        if opcode == 0:
            self.A = trunc(self.A / (2**val))

        # bxl
        elif opcode == 1:
            self.B = self.B ^ operand

        # bsl
        elif opcode == 2:
            self.B = val % 8

        # jnz
        elif opcode == 3:
            if self.A != 0:
                self.pointer = operand
                return None

        # bxc
        elif opcode == 4:
            self.B = self.B ^ self.C

        # out
        elif opcode == 5:
            self.pointer += 2
            return val % 8

        # bdv
        elif opcode == 6:
            self.B = trunc(self.A / (2**val))

        # cdv
        elif opcode == 7:
            self.C = trunc(self.A / (2**val))

        self.pointer += 2
        return None

    def do_instructions(self) -> str:
        ans = []
        while True:
            # print(self.pointer)
            opcode = self.instructions[self.pointer]
            operand = self.instructions[self.pointer + 1]

            out = self.do_instruction(opcode, operand)
            if out is not None:
                ans.append(out)

            if self.pointer >= len(self.instructions) - 1:
                return ",".join([str(i) for i in ans])


def part1(data_path: str) -> str:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    register_A = int(data[0].split(": ")[-1])
    register_B = int(data[1].split(": ")[-1])
    register_C = int(data[2].split(": ")[-1])

    instructions = data[3].split(": ")[-1]

    computer = Computer(register_A, register_B, register_C, instructions)

    return computer.do_instructions()


def check_register_value(A: int, B: int, C: int, instructions: str) -> bool:
    computer = Computer(A, B, C, instructions)
    out = computer.do_instructions()
    return out == instructions


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    register_B = int(data[1].split(": ")[-1])
    register_C = int(data[2].split(": ")[-1])

    instructions = data[3].split(": ")[-1]

    for i in range(20000000):
        print(f"Starting {i}")
        if check_register_value(i, register_B, register_C, instructions):
            break

    return i


if __name__ == "__main__":
    # print(part1(f"{current_day}/example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))
