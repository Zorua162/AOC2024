import re

current_day = "day3"


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write(line)


def do_mults(mul_list: list[str]) -> int:
    count = 0
    for mul in mul_list:
        split_mul = mul.split(",")
        left = int(split_mul[0][4:])
        right = int(split_mul[1][:-1])
        count += left * right
    return count


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)

    count = 0

    for line in data:
        p = re.compile(r"mul\(\d+,\d+\)")
        count += do_mults(p.findall(line))
    return count


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)
    return 0


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
