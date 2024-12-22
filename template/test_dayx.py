from template.dayx_solution import part1, part2
import pytest

current_day = "template"


def test_part1_example_data_output(get_days_example_data_fixture) -> None:
    output: int = part1(f"{current_day}/example_data.txt")
    assert 0 == output


@pytest.mark.skip("Answer is from AOC website")
def test_part1_data_output(get_days_data_fixture):
    output = part1(f"{current_day}/data.txt")
    assert "currently unknown" == output


@pytest.mark.skip("Enable once answer has been found to determine if unoptimized")
def test_time_part1():
    part1(f"{current_day}/data.txt")


@pytest.mark.skip("Part 2 not started yet")
def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/example_data.txt")
    assert 0 == output


@pytest.mark.skip("Answer is from AOC website")
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert "currently unknown" == output


@pytest.mark.skip("Enable once answer has been found to determine if unoptimized")
def test_time_part2():
    part2(f"{current_day}/data.txt")
