from day12.day12_solution import part1, part2

current_day = "day12"


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 1930 == output


def test_part1_data_output(get_days_data_fixture):
    output = part1(f"{current_day}/data.txt")
    assert 1533644 == output


def test_part2_simple_data_output() -> None:
    output: int = part2(f"{current_day}/simple_example.txt")
    assert 80 == output


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part1_example_data.txt")
    assert 1206 == output


def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert 936718 == output
