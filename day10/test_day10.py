from day10.day10_solution import part1, part2, Route, Location, count_tops
import pytest

current_day = "day10"


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 36 == output


def test_path_one_route_expected() -> None:
    with open(f"{current_day}/part1_example_data.txt", "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    i = 2
    j = 5
    routes = Route([Location(i, j, data)]).find_routes(data)
    score = count_tops(routes)
    assert 1 == score


def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert 746 == output


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part1_example_data.txt")
    assert 81 == output


@pytest.mark.skip("Answer is from AOC website")
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert "currently unknown" == output
