"""tests to check tof_tools functions work as expected"""
import pytest
from osod.tof_tools import average_distance


TofFixture = list[list[int]]


@pytest.fixture
def perfect_flat_reading() -> TofFixture:
    """pytest fixture to return data for flat tof reading"""
    data = [
        [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],
        [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],
        [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],
        [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],
        [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],
        [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],
        [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],
        [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],
    ]
    return data


@pytest.fixture
def oblique_reading() -> TofFixture:
    """pytest fixture to return data for oblique tof reading"""
    data = [
        [1398, 1560, 1488, 1464, 1523, 1697, 1656, 1853],
        [1635, 1671, 1831, 1646, 1566, 1550, 1760, 1771],
        [1347, 1409, 1981, 1969, 2244, 2077, 2218, 2188],
        [1341, 1373, 2170, 2182, 2396, 2234, 2262, 2158],
        [1946, 1673, 2204, 2257, 2256, 2279, 2273, 2360],
        [1833, 2055, 2069, 2110, 2146, 2157, 2170, 2212],
        [1832, 1932, 1905, 1947, 1943, 1966, 1985, 1987],
        [1766, 1769, 1802, 1804, 1840, 1811, 1826, 1851],
    ]
    return data


def test_average_for_perfect_flat_reading(perfect_flat_reading: TofFixture):
    """ "average_distance should always average all provided readings"""
    assert average_distance(perfect_flat_reading) == 1000


def test_average_for_oblique_reading(oblique_reading: TofFixture):
    """ "average_distance should always average all provided readings"""
    assert average_distance(oblique_reading) == 1899.75
