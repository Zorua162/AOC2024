from day2.day2_solution import part1, part2, check_line_safe_part2

current_day = "day2"


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 2 == output


def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert 224 == output


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part1_example_data.txt")
    assert 4 == output


def test_edge_case_1() -> None:
    assert not check_line_safe_part2("5 6 5 8 10 12 17")


def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert 293 == output
