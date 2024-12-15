import os
import pytest
from get_data import get_days_data, get_days_example_data
import pathlib


@pytest.fixture
def get_days_data_fixture():
    path = pathlib.PurePath(os.getenv("PYTEST_CURRENT_TEST"))
    day_folder = path.parent.name
    day_number = int(day_folder[3:])
    get_days_data(day_folder, day_number)


@pytest.fixture
def get_days_example_data_fixture():
    path = pathlib.PurePath(os.getenv("PYTEST_CURRENT_TEST"))
    day_folder = path.parent.name
    day_number = int(day_folder[3:])
    get_days_example_data(day_folder, day_number)
