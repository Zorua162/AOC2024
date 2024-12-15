from day1.day1_solution import part1, part2

current_day = "day1"


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 11 == output


def test_part1_data_output(get_days_data_fixture):
    output = part1(f"{current_day}/data.txt")
    assert 2057374 == output


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part1_example_data.txt")
    assert 31 == output


def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert 23177084 == output
