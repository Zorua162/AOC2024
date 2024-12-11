from day11.day11_solution import part1, part2

current_day = "day11"


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 55312 == output


def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert 193269 == output


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part1_example_data.txt")
    assert 65601038650482 == output


def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert 228449040027793 == output
