from day5.day5_solution import part1, part2

current_day = "day5"


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 143 == output


def test_part1_data_output(get_days_data_fixture):
    output = part1(f"{current_day}/data.txt")
    assert 5166 == output


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part1_example_data.txt")
    assert 123 == output


def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert 4679 == output
