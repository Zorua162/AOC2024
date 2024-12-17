from day17.day17_solution import part1, part2

# import pytest

current_day = "day17"


def test_part1_example_data_output(get_days_example_data_fixture) -> None:
    output = part1(f"{current_day}/example_data.txt")
    assert "4,6,3,5,6,3,5,2,1,0" == output


def test_part1_data_output(get_days_data_fixture):
    output = part1(f"{current_day}/data.txt")
    assert "1,7,6,5,1,0,5,0,7" == output


def test_part1_speed(time_answer):
    part1(f"{current_day}/data.txt")


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part2_example_data.txt")
    assert 117440 == output


def test_part2_speed(time_answer):
    part2(f"{current_day}/data.txt")


def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert "currently unknown" == output
