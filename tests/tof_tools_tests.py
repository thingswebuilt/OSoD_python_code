"""tests to check tof_tools functions work as expected"""
from src.tof_tools import average_distance

def test_average_for_perfect_flat_reading(perfect_flat_reading):
    """ "average_distance should always average all provided readings"""
    assert average_distance(perfect_flat_reading) == 1000


def test_average_for_oblique_reading(oblique_reading):
    """ "average_distance should always average all provided readings"""
    assert average_distance(oblique_reading) == 1899.75
