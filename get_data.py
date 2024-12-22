from os import getenv
from dotenv import load_dotenv

from pathlib import Path

from typing import Callable

from aocd import get_data
from aocd import get_puzzle

# loading variables from .env file
load_dotenv()

year_str = getenv("YEAR")
if year_str is None:
    raise Exception("Need to set year in .env file")
year = int(year_str)


def get_or_cache(get_function: Callable, day_number: int, file_path: str) -> str:
    # Get from Cache or AOC website using specified function
    if not Path(file_path).is_file() or getenv("AOC_SESSION") != getenv(
        "LAST_AOC_SESSION"
    ):
        with open(file_path, "w") as f_obj:
            data = get_function(day=day_number, year=year)
            f_obj.write(data)

        return data

    with open(file_path, "r") as f_obj:
        return f_obj.read()


def get_days_data(day_folder: str, day_number: int) -> str:
    print(f"Getting data for day {day_number}")
    file_path = f"{day_folder}/data.txt"
    data = get_data
    print(f"{data = }")
    return get_or_cache(data, day_number, file_path)


def get_example(day: int, year: int) -> str:
    puzzle_data = get_puzzle(getenv("AOC_SESSION"), day=day, year=year)._get_examples()
    print(f"{puzzle_data = }")
    return puzzle_data[0].input_data


def get_days_example_data(day_folder: str, day_number: int):
    print(f"Getting example data for day {day_number}")
    file_path = f"{day_folder}/example_data.txt"
    return get_or_cache(get_example, day_number, file_path)
