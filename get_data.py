from aocd import get_data
from dotenv import load_dotenv
from pathlib import Path
from os import getenv

# loading variables from .env file
load_dotenv()

year = 2024
day = 1


def get_days_data(day_folder: str, day_number: int):
    # Check if file already exists
    file_path = f"{day_folder}/data.txt"
    if not Path(file_path).is_file():
        # Check if session id changed
        if getenv("AOC_SESSION") != getenv("LAST_AOC_SESSION"):
            with open(file_path, "w") as f_obj:
                f_obj.write(get_data(day=day, year=year))
