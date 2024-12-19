from typing import Any
from typing import Optional
from typing import Union


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

            print(f"{self.A = }, {self.B = } {self.C = }")
            pass

            if self.pointer >= len(self.instructions) - 1:
                return ",".join([str(i) for i in ans])

    def find_correct_A_example(self) -> int:
        A = 0
        # for i, instruction in enumerate(reversed(self.instructions[-3:-1])):
        for i, instruction in enumerate(reversed(self.instructions)):
            # Solve this instruction backwards from the output point
            print(f"Looking at instruction {instruction = }")

            # The bits at the end of the number need to
            next_required_end_bits = 8 - (instruction % 8)

            A = next_required_end_bits * 3

            print(f"{A = } {next_required_end_bits = }")

        return 0

    def find_correct_A(self) -> int:
        # Example
        # 0,3 A=A/6
        # 5,4 A%8>
        # 3,0 A!=0;p=0

        # Full
        # 2,4 B = A % 8                            B = 1-7
        # 1,3 B = B x 3                            B = B x 0011 = (1-7)
        # 7,5 C = A / (2 ** B)                     C = A / (2, 4, 8, 16, 32, 64, 128 )
        # 4,2 B = B x C                            B = B(1 - 7) x C (big num)
        # 0,3 A = A / (2 ** 3)      A = (1- 7)
        # 1,5 B = B x 5             0010 x 0101    1010 = 10 101010 > 010101
        # 5,5 B % 8 >               0
        # 3,0 if A == 0 END; p=0

        # [f"{x ^ 5:04b}" for x in range(8)]

        output_loc = find_output(self.instructions)

        output_xor = self.instructions[output_loc + 1]

        print(f"{output_loc = } {output_xor = }")

        end_A: int = 0  # Must end as A = 0
        end_B: Union[str, int] = "unknown"  # Unknown at end
        end_C: Union[str, int] = "unknown"  # Unknown at end

        # start_A: Union[str, int] = "output"  # Target to find
        # start_B: int = 0  # Starts as 0
        # start_C: int = 0  # Starts as 0

        A = end_A
        B = end_B
        C = end_C

        possible_A: list[int] = []
        possible_B: list[int] = []
        possible_C: list[int] = []

        # sorted_instructions = sort_instructions(self.instructions)

        for instruction in reversed(self.instructions):
            # Solve this instruction backwards from the output point
            print(f"Looking at instruction {instruction = }")
            # A = (1- 7) (1 - 2 ** 3)
            # Try each of the 1 - 7 paths to reverse way to the set of inputs where:
            # All the output values come out correct
            # The B and C register start at 0

            A, B, C, possible_A, possible_B, possible_C = self.do_round(
                instruction, A, B, C, possible_A, possible_B, possible_C
            )

        # Do the last output one more time to get the correct A
        A, B, C, possible_A, possible_B, possible_C = self.do_round(
            self.instructions[-1], A, B, C, possible_A, possible_B, possible_C
        )

        return A

    def do_round(
        self,
        output: int,
        A: int,
        B: Union[int, str],
        C: Union[int, str],
        possible_A: list[int],
        possible_B: list[int],
        possible_C: list[int],
    ) -> tuple[int, Union[int, str], Union[int, str], list[int], list[int], list[int]]:
        # test

        for i in range(len(self.instructions) - 2, -1, -2):
            opcode = self.instructions[i]
            operand = self.instructions[i + 1]

            A, B, C, possible_A, possible_B, possible_C = self.reverse_instruction(
                output, opcode, operand, A, B, C, possible_A, possible_B, possible_C
            )

        return A, B, C, possible_A, possible_B, possible_C

    def reverse_instruction(
        self,
        output: int,
        opcode: int,
        operand: int,
        A: int,
        B: Union[int, str],
        C: Union[int, str],
        possible_A: list[int],
        possible_B: list[int],
        possible_C: list[int],
    ) -> tuple[int, Union[int, str], Union[int, str], list[int], list[int], list[int]]:
        print(f"reversing instruction {output = } {opcode = } {operand = }")

        # Combo operands 0 through 3 represent literal values 0 through 3.
        # Combo operand 4 represents the value of register A.
        # Combo operand 5 represents the value of register B.
        # Combo operand 6 represents the value of register C.
        # Combo operand 7 is reserved and will not appear in valid programs.

        if opcode == 0:
            # The adv instruction (opcode 0) performs division. The numerator is the
            # value in the A register. The denominator is found by raising 2 to the
            # power of the instruction's combo operand. (So, an operand of 2 would
            # divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result
            # of the division operation is truncated to an integer and then written
            # to the A register.

            if operand == 3:
                # A = A / 8

                possible_A = [A * 8 + i for i in range(2**operand)]

                print(f"{possible_A = }")

        if opcode == 4:
            # The bxc instruction (opcode 4) calculates the bitwise XOR of register B
            # and register C, then stores the result in register B.
            # (For legacy reasons, this instruction reads an operand but ignores it.)

            # This one will confirm for us which last 3 bits it actually is
            pass

        if opcode == 5:
            # The out instruction (opcode 5) calculates the value of its combo operand
            # modulo 8, then outputs that value. (If a program outputs multiple values,
            # they are separated by commas.)
            if operand == 5:
                # Output is B % 8

                if B == 0:
                    B = 0

            if operand == 4:
                if possible_A == []:
                    return A, B, C, possible_A, possible_B, possible_C
                A = find_actual_A_from_output(possible_A, output)

        return A, B, C, possible_A, possible_B, possible_C


def sort_instructions(instructions: list[int]) -> list[int]:
    sorted_instructions: list[int] = instructions
    # Move the 5 to the second to last position
    five_indexes: list[int] = []

    for val in instructions:
        if val == 0:
            five_indexes.append(val)

    for index in five_indexes:
        five_opcode = sorted_instructions.pop(index)
        five_operand = sorted_instructions.pop(index)
        sorted_instructions.append(five_opcode)
        sorted_instructions.append(five_operand)

    return sorted_instructions


def find_actual_A_from_output(possible_A: list[int], output: int) -> int:
    for poss_A in possible_A:
        if poss_A % 8 == output:
            return poss_A
    raise Exception(f"output was not found in possible_A % 8 {possible_A} {output}")


def find_output(instructions: list[int]) -> int:
    for i, val in enumerate(instructions):
        if i % 2 == 0 and val == 5:
            return i
    raise Exception("Failed to find i ")


def part1(data_path: str) -> str:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    register_A = int(data[0].split(": ")[-1])
    register_B = int(data[1].split(": ")[-1])
    register_C = int(data[2].split(": ")[-1])

    instructions = data[3].split(": ")[-1]

    computer = Computer(register_A, register_B, register_C, instructions)

    return computer.do_instructions()


def check_register_value(A: int, B: int, C: int, instructions: str) -> tuple[bool, str]:
    computer = Computer(A, B, C, instructions)
    out = computer.do_instructions()

    if A % 10000 == 0:
        print(out)
    # print(out)
    return out == instructions, out


def part2_attempt1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    register_B = int(data[1].split(": ")[-1])
    register_C = int(data[2].split(": ")[-1])

    instructions = data[3].split(": ")[-1]
    i = 1
    # for i in range(20000000):
    while True:
        if i % 10000 == 0:
            print(f"Starting {i}")
        correct, out = check_register_value(i, register_B, register_C, instructions)
        if correct:
            break
        # i += 1
        if len(out) < len(instructions):
            print(f"Increasing by 10 {out = }")
            i *= 10
        elif len(out) > len(instructions):
            print(f"Decreasing by 10 {out = }")
            i = int(i / 10)
        else:
            i += 1

    return i


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    instructions = data[3].split(": ")[-1]

    computer = Computer(117440, 0, 0, instructions)

    # computer.do_instructions()

    return computer.find_correct_A()

    # return computer.find_correct_A()
    # return computer.find_correct_A_example()


if __name__ == "__main__":
    # print(part1(f"{current_day}/example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    print(part2(f"{current_day}/part2_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))