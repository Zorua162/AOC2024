from day14.day14_solution import part1, Robot, draw_grid, do_closeness

current_day = "day14"


def test_robot():
    "p=2,4 v=2,-3"

    robot = Robot("2", "4", "2", "-3")
    print(robot)
    draw_grid([robot], 11, 7)

    for _ in range(5):
        robot.do_step(11, 7)

        print(robot)
        draw_grid([robot], 11, 7)

    assert robot.x == 1
    assert robot.y == 3


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt", 11, 7)
    assert 12 == output


def test_part1_data_output():
    output = part1(f"{current_day}/data.txt", 101, 103)
    assert 208437768 == output


def test_part2_data_output():
    output = do_closeness(f"{current_day}/data.txt", 101, 103, 10402)
    assert 7492 == output
