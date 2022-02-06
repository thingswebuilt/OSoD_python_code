import json
from sys import implementation

from fixtures.test_data import test_data
from src.example_test import my_cool_function

def test_answer_for_double_figures():
    """"my_cool_function should always increment the input parameter by exactly 1"""
    assert my_cool_function(10) == 11

def test_answer_for_negative_figures():
    """"my_cool_function should always increment the input parameter by exactly 1"""
    function_input = 10
    assert my_cool_function(-1) == 0

def test_other(test_data):
    for number in test_data['numbers']:
        assert my_cool_function(number) == number + 1



