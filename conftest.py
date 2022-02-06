import json
import pytest


@pytest.fixture
def test_data() -> dict[str, list[int]]:
    """return test data from json file"""
    with open("tests/data.json", encoding="utf-8") as data_file:
        data = json.load(data_file)
    return data
