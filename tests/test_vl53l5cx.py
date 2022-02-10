"""tests to check tof_tools functions work as expected"""
import itertools
import pytest
from osod.tof.models import Vl53l5cxMode, Vl53l5cxReading


@pytest.fixture
def perfect_flat_reading() -> Vl53l5cxReading:
    """pytest fixture to return data for flat tof reading"""
    raw_sensor_data = (
        (1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000),
        (1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000),
        (1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000),
        (1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000),
        (1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000),
        (1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000),
        (1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000),
        (1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000),
    )
    flattened_data = list(itertools.chain.from_iterable(raw_sensor_data))
    return Vl53l5cxReading(flattened_data)


@pytest.fixture
def oblique_reading() -> Vl53l5cxReading:
    """pytest fixture to return data for oblique tof reading"""
    raw_sensor_data = (
        (1398, 1560, 1488, 1464, 1523, 1697, 1656, 1853),
        (1635, 1671, 1831, 1646, 1566, 1550, 1760, 1771),
        (1347, 1409, 1981, 1969, 2244, 2077, 2218, 2188),
        (1341, 1373, 2170, 2182, 2396, 2234, 2262, 2158),
        (1946, 1673, 2204, 2257, 2256, 2279, 2273, 2360),
        (1833, 2055, 2069, 2110, 2146, 2157, 2170, 2212),
        (1832, 1932, 1905, 1947, 1943, 1966, 1985, 1987),
        (1766, 1769, 1802, 1804, 1840, 1811, 1826, 1851),
    )
    flattened_data = list(itertools.chain.from_iterable(raw_sensor_data))
    return Vl53l5cxReading(flattened_data)


def test_single_requires_1_elements():
    """attempting to initialise a value model with the incorrect number of paramaters
    for the selected mode should raise a ValueError"""
    sensor_mode = Vl53l5cxMode.SINGLE
    # try instantiating with 0 to 100 elements. expect all except 16 to raise an error
    for i in range(1, 101):
        raw_sensor_data = [1] * i
        if i != 1:
            # expect this to raise an error
            with pytest.raises(ValueError) as e_info:
                Vl53l5cxReading(raw_sensor_data, mode=sensor_mode)
                assert e_info.value == (
                    f"Unexpected number of data elements for TofValue. Expected 64, received {i}"
                )
        else:
            Vl53l5cxReading(raw_sensor_data, mode=sensor_mode)


def test_four_by_four_requires_16_elements():
    """attempting to initialise a value model with the incorrect number of paramaters
    for the selected mode should raise a ValueError"""
    sensor_mode = Vl53l5cxMode.FOURBYFOUR
    # try instantiating with 0 to 100 elements. expect all except 16 to raise an error
    for i in range(1, 101):
        raw_sensor_data = [1] * i
        if i != 16:
            # expect this to raise an error
            with pytest.raises(ValueError) as e_info:
                Vl53l5cxReading(raw_sensor_data, mode=sensor_mode)
                assert e_info.value == (
                    f"Unexpected number of data elements for TofValue. Expected 64, received {i}"
                )
        else:
            Vl53l5cxReading(raw_sensor_data, mode=sensor_mode)


def test_eight_by_eight_requires_64_elements():
    """attempting to initialise a value model with the incorrect number of paramaters
    for the selected mode should raise a ValueError"""
    sensor_mode = Vl53l5cxMode.EIGHTBYEIGHT
    # try instantiating with 0 to 100 elements. expect all except 64 to raise an error
    for i in range(1, 101):
        raw_sensor_data = [1] * i
        if i != 64:
            # expect this to raise an error
            with pytest.raises(ValueError) as e_info:
                Vl53l5cxReading(raw_sensor_data, mode=sensor_mode)
                assert e_info.value == (
                    f"Unexpected number of data elements for TofValue. Expected 64, received {i}"
                )
        else:
            Vl53l5cxReading(raw_sensor_data, mode=sensor_mode)


def test_average_for_perfect_flat_reading(perfect_flat_reading: Vl53l5cxReading):
    """ "average_distance should always average all provided readings"""
    assert perfect_flat_reading.average == 1000


def test_average_for_oblique_reading(oblique_reading: Vl53l5cxReading):
    """ "average_distance should always average all provided readings"""
    assert oblique_reading.average == 1899.75
