import json
import pytest

@pytest.fixture
def test_data():
    with open('tests/data.json') as f:
        data = json.load(f)
    return data