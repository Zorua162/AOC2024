from day9.day9_solution import part1, part2, calc_answer
from typing import Optional

current_day = "day9"


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 1928 == output


def test_part1_data_output(get_days_data_fixture):
    output = part1(f"{current_day}/data.txt")
    assert 6421128769094 == output


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part1_example_data.txt")
    assert 2858 == output


def test_part2_checksum() -> None:
    example_str = "00992111777.44.333....5555.6666.....8888.."
    compacted_list: list[Optional[int]] = [
        None if v == "." else int(v) for v in example_str
    ]
    print(compacted_list)
    assert 2858 == calc_answer(compacted_list)


def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert 6448168620520 == output
