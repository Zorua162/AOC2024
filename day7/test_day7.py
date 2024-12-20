from day7.day7_solution import part1, part2
import pytest

current_day = "day7"


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 3749 == output


@pytest.mark.skip("Too slow to be running on CI/CD, solution needs improvement")
def test_part1_data_output(get_days_data_fixture):
    output = part1(f"{current_day}/data.txt")
    assert 2314935962622 == output


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part1_example_data.txt")
    assert 11387 == output


@pytest.mark.skip("Too slow to be running on CI/CD, solution needs improvement")
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert 401477450831495 == output
