from day18.day18_solution import part1, part2

current_day = "day18"


def test_part1_example_data_output(get_days_example_data_fixture) -> None:
    output: int = part1(f"{current_day}/example_data.txt")
    assert 22 == output


def test_part1_data_output(get_days_data_fixture):
    output = part1(f"{current_day}/data.txt")
    assert 310 == output


def test_time_part1():
    part1(f"{current_day}/data.txt")


def test_part2_example_data_output() -> None:
    output = part2(f"{current_day}/example_data.txt")
    assert "6,1" == output


def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert "16,46" == output


def test_time_part2():
    part2(f"{current_day}/data.txt")
