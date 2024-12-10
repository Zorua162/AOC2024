from typing import Optional

current_day = "day9"


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def print_to_file(data: str):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        f_out.write(data + "\n")


def compact(values: list[Optional[int]]) -> list[Optional[int]]:
    end_index = len(values) - 1
    start_index = 0

    while True:
        end_value = values.pop()
        while end_value is None:
            end_index -= 1
            end_value = values.pop()

        len_values = len(values)
        if start_index >= len_values:
            values.append(end_value)
            return values
        start_value = values[start_index]
        while start_value is not None:
            start_index += 1
            # print(start_index)
            # print(values)
            if start_index >= len_values:
                values.append(end_value)
                return values
            start_value = values[start_index]
            # A, B, C
            # 0, 1, 2
            # len() = 3

        values[start_index] = end_value


def calc_answer(compacted: list[Optional[int]]) -> int:
    count = 0
    for i, val in enumerate(compacted):
        if val is None:
            continue
        # print(f"{i = }, {val = }, {i*val = }")
        count += i * val
    return count


def expand_data(data: list[str]) -> list[Optional[int]]:
    expanded: list[Optional[int]] = []

    line = data[0]

    i = 0
    free_space = False
    for value in line:
        if not free_space:
            expanded.extend([i] * int(value))
            i += 1
        else:
            expanded.extend([None] * int(value))
        free_space = not free_space
    return expanded


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    expanded = expand_data(data)

    compacted = compact(expanded)

    print(compacted)

    return calc_answer(compacted)


class Group:
    count: int

    def __init__(self, count: int):
        self.count = count

    def __repr__(self):
        return f"({self.count = })"


class Files(Group):
    value: int

    def __init__(self, count: int, value: int):
        super().__init__(count)
        self.value = value

    def __repr__(self):
        return f"({self.count = }, {self.value = })"


class Space(Group):
    def __init__(self, count: int):
        super().__init__(count)


def expand_to_classes(data: list[str]) -> list[Group]:
    line: str = data[0]

    groups: list[Group] = []
    i = 0
    free_space = False
    for val in line:
        if not free_space:
            groups.append(Files(int(val), i))
            i += 1
        else:
            groups.append(Space(int(val)))
        free_space = not free_space

    return groups


def compact_classes(groups: list[Group]) -> list[Group]:
    # Group type alternates so if not last then second last is files
    if type(groups[-1]) is Files:
        end_files_index: Optional[int] = len(groups) - 1
    else:
        end_files_index = len(groups) - 2

    current_end_value = groups[end_files_index].value  # type: ignore

    # print(end_files_index)

    while True:
        if end_files_index is None:
            raise Exception("An Error occurred: Could not find next end files")

        current_end_files = groups[end_files_index]
        # print(current_end_files)
        for i, group in enumerate(groups[:end_files_index]):
            if type(group) is Space and group.count >= current_end_files.count:
                # It fits here!
                groups.remove(current_end_files)
                # print(i)
                groups.insert(i, current_end_files)
                group.count = group.count - current_end_files.count
                # print(groups)

                # Increase the count of the space that was one behind the moved files
                increased_space = groups[end_files_index]
                increased_space.count = increased_space.count + current_end_files.count
                break
        current_end_value -= 1
        print(f"{current_end_value = }")
        if current_end_value < 0:
            return groups
        end_files_index = find_next_end_files(groups, current_end_value)


def find_next_end_files(groups: list[Group], search_end_value) -> Optional[int]:
    for i, group in enumerate(groups):
        # print(i, group)
        if type(group) is Files and group.value == search_end_value:
            return i
    return None


def stringify(groups: list[Group]) -> str:
    out_str: str = ""
    for group in groups:
        if isinstance(group, Files):
            out_str += str(group.value) * group.count
        else:
            out_str += "." * group.count
    return out_str


def listify(groups: list[Group]) -> list[Optional[int]]:
    out_list: list[Optional[int]] = []
    for group in groups:
        if isinstance(group, Files):
            out_list.extend([group.value] * group.count)
        else:
            out_list.extend([None] * group.count)
    return out_list


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    expanded = expand_to_classes(data)

    compacted = compact_classes(expanded)

    # My answer:
    # 0099211177744.333..5555.6666..8888
    # 00992111777.44.333....5555.6666.....8888..

    print(compacted)

    print(stringify(compacted))

    return calc_answer(listify(compacted))


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part1(f"{current_day}/my_test_data.txt"))
    # print(part2(f"{current_day}/part1_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))

# 91111740342 Too low
