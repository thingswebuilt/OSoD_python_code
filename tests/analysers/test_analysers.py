"""tests to check tof_tools functions work as expected"""
import pytest
from osod.tof.analysers import RangeDataAnalyser, RangeDataAnalyserException


def test_average_basic(perfect_flat_reading_data: list[float]):
    """test range anlyser coerrectly calculates average of list of ints"""
    analyser = RangeDataAnalyser(data=[1, 2, 3, 4, 5])
    assert analyser.average == 3


def test_average_empty_list_raises_exception(
    perfect_flat_reading_data: list[float],
):
    """test range anlyser coerrectly calculates average of list of ints"""
    analyser = RangeDataAnalyser()
    with pytest.raises(RangeDataAnalyserException):
        assert analyser.average == 0


def test_average_perfect_flat_reading(
    perfect_flat_reading_data: list[float],
):
    """test range anlyser coerrectly calculates average for perfectly flat data frame"""
    analyser = RangeDataAnalyser(data=perfect_flat_reading_data)
    assert analyser.average == 1000


def test_average_for_oblique_reading(oblique_reading_data: list[float]):
    """ "average_distance should always average all provided readings"""
    analyser = RangeDataAnalyser(data=oblique_reading_data)
    assert analyser.average == 1899.75
