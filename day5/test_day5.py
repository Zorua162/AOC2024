from day5.day5_solution import part1, part2
import pytest

current_day = "day5"


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 143 == output


def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert 5166 == output


@pytest.mark.skip("Not started yet")
def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part1_example_data.txt")
    assert 123 == output


@pytest.mark.skip("Answer is from AOC website")
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert "currently unknown" == output
