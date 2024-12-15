from day15.day15_solution import part1, part2
import pytest

current_day = "day15"


@pytest.mark.skip("Fails in CI due to no example data")
def test_part1_example_data_output(get_days_example_data_fixture) -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 2028 == output


def test_larger_example_data_output() -> None:
    output: int = part1(f"{current_day}/example_data.txt")
    assert 10092 == output


def test_part1_data_output(get_days_data_fixture):
    output = part1(f"{current_day}/data.txt")
    assert 1456590 == output


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/example_data.txt")
    assert 9021 == output


def test_part2_data_output(get_days_data_fixture):
    output = part2(f"{current_day}/data.txt")
    assert 1489116 == output
