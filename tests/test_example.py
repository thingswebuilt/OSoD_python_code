from typing import TypedDict
from example import my_cool_function


class TestData(TypedDict):
    """Test data structure typing"""

    numbers: list[int]


def test_answer_for_double_figures():
    """ "my_cool_function should always increment the input parameter by exactly 1"""
    assert my_cool_function(10) == 11


def test_answer_for_negative_figures():
    """ "my_cool_function should always increment the input parameter by exactly 1"""
    assert my_cool_function(-1) == 0


def test_other(test_data: TestData):
    """run test against fixture data"""
    for number in test_data["numbers"]:
        assert my_cool_function(number) == number + 1
